---
url: https://docs.comfy.org/es/development/comfy-router/models/fal/crystal-upscaler/code/
title: Usa Crystal Upscaler con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:03.328567+00:00
---

# Usa Crystal Upscaler con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/fal/crystal-upscaler/code/

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

# Usa Crystal Upscaler con Comfy Router

Copiar páginaCopiar página

Llama a fal/crystal-upscaler con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API de `fal/crystal-upscaler`, servida por Comfy Router desde fal. **Entrada:** Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `fal/crystal-upscaler` **Endpoint:** `POST https://api.comfy.org/v2/models/fal/crystal-upscaler`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "fal/crystal-upscaler",
            {
                "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
                "scale_factor": 2,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("fal/crystal-upscaler", {
      image_url: "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
      scale_factor: 2,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/fal/crystal-upscaler \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png\", \"scale_factor\": 2}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/fal/crystal-upscaler/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "fal/crystal-upscaler",
                {
                    "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
                    "scale_factor": 2,
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("fal/crystal-upscaler", {
      image_url: "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
      scale_factor: 2,
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía la solicitud. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/fal/crystal-upscaler/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png\", \"scale_factor\": 2}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/fal/crystal-upscaler/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge el resultado. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/fal/crystal-upscaler/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

creativity

number

predeterminado:"0"

Cuánto detalle nuevo puede inventar el modelo. 0 mantiene el resultado lo más cercano posible a la entrada.Rango: `0` a `10`

​

image_url

string

requerido

URL de la imagen de entrada (JPEG, PNG, WebP, GIF o AVIF, como máximo 100 MB).

​

output_format

string

predeterminado:"\"jpg\""

Formato de la imagen de salida: png o jpg.

​

scale_factor

number

predeterminado:"2"

Factor aplicado a cada lado de la imagen de entrada. fal cobra por megapíxel de salida, así que el precio crece con el cuadrado de este valor.Rango: `1` a `200`

Generado a partir del esquema que Router sirve en `GET /v2/models/fal/crystal-upscaler/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

images

object[]

requerido

Las imágenes con upscale.

​

images[].content_type

string

Tipo MIME del archivo de imagen.

​

images[].file_name

string

Nombre del archivo de imagen.

​

images[].file_size

integer

Tamaño del archivo de imagen en bytes.

​

images[].height

integer

Alto de la imagen en píxeles. fal envía null.

​

images[].url

string

requerido

URL de la imagen con upscale.

​

images[].width

integer

Ancho de la imagen en píxeles. fal envía null.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
      "scale_factor": 2
    }
    

### 

​

Salida
    
    
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "upscaled.png",
          "file_size": 1412332,
          "height": null,
          "url": "https://example.invalid/fal/crystal-upscaler/upscaled.png",
          "width": null
        }
      ]
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/fal/crystal-upscaler/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/fal/crystal-upscaler/code)

[Eleven V4](https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-v4/code)[Crystal Video Upscaler](https://docs.comfy.org/es/development/comfy-router/models/fal/crystal-video-upscaler/code)
