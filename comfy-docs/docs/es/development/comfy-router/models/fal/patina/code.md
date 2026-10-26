---
url: https://docs.comfy.org/es/development/comfy-router/models/fal/patina/code/
title: Usa Patina con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:03.891562+00:00
---

# Usa Patina con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/fal/patina/code/

## En esta página

Volver arriba

  * Inicio rápido
  * Esquema
    * Entrada
    * Salida
  * Ejemplos
    * Entrada
    * Salida
  * Antes de lanzar



fal

# Usa Patina con Comfy Router

Copiar páginaCopiar página

Llama a fal/patina con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `fal/patina`, servida por Comfy Router desde fal. **Entrada:** Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `fal/patina` **Endpoint:** `POST https://api.comfy.org/v2/models/fal/patina`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "fal/patina",
            {
                "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("fal/patina", {
      image_url: "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/fal/patina \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/fal/patina/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "fal/patina",
                {
                    "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del Proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o fue cancelada lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("fal/patina", {
      image_url: "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o fue cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/fal/patina/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/fal/patina/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/fal/patina/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

enable_safety_checker

boolean

predeterminado:"true"

Habilita el verificador de seguridad para las imágenes.

​

image_url

string

requerido

URL de la imagen de entrada (fotografía o render).

​

maps

string[]

Qué mapas PBR se deben predecir. De forma predeterminada, los cinco.

​

output_format

string

predeterminado:"\"png\""

Formato de la imagen de salida: jpeg, png o webp.

​

seed

integer

Semilla aleatoria para un denoising reproducible.

​

sync_mode

boolean

predeterminado:"false"

Si es true, devuelve las imágenes como URI de datos en lugar de URL de CDN.

Generado a partir del esquema que Router sirve en `GET /v2/models/fal/patina/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

images

object[]

Imagen de textura repetible generada junto con los mapas de material PBR predichos. La textura base solo tiene una url; cada entrada de mapa también incluye un map_type.

​

images[].map_type

string

El tipo de mapa PBR (basecolor, normal, roughness, metalness, height). Ausente para la imagen de textura base.

​

images[].url

string

URL de la imagen generada.

​

prompt

string

El prompt utilizado para la generación de la textura (posiblemente ampliado).

​

seed

integer

Semilla utilizada para la generación de la textura.

​

timings

object

Desglose de tiempos de extremo a extremo (segundos).

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png"
    }
    

### 

​

Salida
    
    
    {
      "images": [
        {
          "map_type": "basecolor",
          "url": "https://example.invalid/fal/patina/basecolor.png"
        },
        {
          "map_type": "normal",
          "url": "https://example.invalid/fal/patina/normal.png"
        },
        {
          "map_type": "roughness",
          "url": "https://example.invalid/fal/patina/roughness.png"
        }
      ],
      "prompt": "weathered copper roof tiles",
      "seed": 1234567,
      "timings": {
        "inference": 6.25
      }
    }
    

## 

​

Antes de lanzar

Los SDK crean una `Idempotency-Key` y la reutilizan para los reintentos automáticos. Para los reintentos manuales, reutiliza la clave original. Router puede mantener la conexión abierta hasta 10 minutos. Cuando una solicitud falla, Router envía un encabezado de respuesta `X-Comfy-Error-Type` que explica el motivo. Un `422` significa que Router rechazó la entrada antes de llamar al proveedor, y un `413` significa que el cuerpo de la solicitud era más grande de lo que Router acepta. Descarga los recursos generados de inmediato, porque [las URL de resultados pueden caducar](https://docs.comfy.org/es/development/comfy-router/reference#recursos-del-resultado). Cualquier límite de tamaño mencionado en la descripción de un campo más arriba es el límite propio del proveedor para ese campo, citado de la especificación del proveedor. Router aplica un tope aparte al cuerpo completo de la solicitud, con el que cuentan los medios codificados en base64: consulta [tamaño del cuerpo de la solicitud](https://docs.comfy.org/es/development/comfy-router/limitations#los-cuerpos-de-las-solicitudes-tienen-un-l%C3%ADmite). Esta página documenta un modelo socio al que se llama a través de Comfy Router. El mismo paquete `comfy-sdk` / `@comfyorg/sdk` también incluye un segundo cliente, para ejecutar todo un gráfico de flujo de trabajo de ComfyUI en Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, con `client.workflows`, `client.assets` y `client.jobs`. Consulta [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks).

## Encabezados

Autenticación, idempotencia, IDs de solicitud, agrupaciones de errores, ritmo de reintentos y límites de gasto.

## Uso de la API de Router

Descubrimiento de modelos, errores de validación, reintentos y facturación.

## Limitaciones

Lo que Router no hace hoy y qué usar en su lugar.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/fal/patina/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/fal/patina/code)

[H3 Max](https://docs.comfy.org/es/development/comfy-router/models/fal/h3-max/code)[AI Image Upscaler Precision V2](https://docs.comfy.org/es/development/comfy-router/models/freepik/ai-image-upscaler-precision-v2/code)
