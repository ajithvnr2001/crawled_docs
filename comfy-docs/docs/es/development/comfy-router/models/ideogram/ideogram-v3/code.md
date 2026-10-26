---
url: https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v3/code/
title: Usa Ideogram V3 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:07.564587+00:00
---

# Usa Ideogram V3 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v3/code/

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



Ideogram

# Usa Ideogram V3 con Comfy Router

Copiar páginaCopiar página

Llama a ideogram/ideogram-v3 con Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `ideogram/ideogram-v3`, servida por Comfy Router desde Ideogram. **Entrada:** Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `ideogram/ideogram-v3` **Endpoint:** `POST https://api.comfy.org/v2/models/ideogram/ideogram-v3`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea una clave de idempotencia automáticamente y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "ideogram/ideogram-v3",
            {
                "prompt": "A beautiful mountain landscape",
                "rendering_speed": "TURBO",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea una clave de idempotencia automáticamente y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("ideogram/ideogram-v3", {
      prompt: "A beautiful mountain landscape",
      rendering_speed: "TURBO",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A beautiful mountain landscape\", \"rendering_speed\": \"TURBO\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/ideogram/ideogram-v3/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "ideogram/ideogram-v3",
                {
                    "prompt": "A beautiful mountain landscape",
                    "rendering_speed": "TURBO",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("ideogram/ideogram-v3", {
      prompt: "A beautiful mountain landscape",
      rendering_speed: "TURBO",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A beautiful mountain landscape\", \"rendering_speed\": \"TURBO\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ideogram/ideogram-v3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

aspect_ratio

string

Relación de aspecto en formato WxH

​

color_palette

object

​

color_palette.members

object[]

Colores explícitos con pesos opcionales

​

color_palette.members[].color

string

Código de color hexadecimal

​

color_palette.members[].weight

number

Peso opcional para el color (0-1)Rango: `0` a `1`

​

color_palette.name

string

Nombre de la paleta de colores

​

magic_prompt

string

Indica si se habilita la mejora mágica del promptValores posibles: `AUTO`, `ON`, `OFF`

​

negative_prompt

string

Prompt de texto que especifica qué evitar en la generación

​

num_images

integer

Número de imágenes a generarRango: `1` a `…`

​

prompt

string

requerido

El prompt de texto para la generación de imágenes

​

rendering_speed

string

predeterminado:"\"DEFAULT\""

requerido

La configuración de velocidad de renderizado que controla el equilibrio entre la velocidad de generación y la calidadValores posibles: `DEFAULT`, `TURBO`, `QUALITY`

​

resolution

string

Resolución de la imagen en formato WxH

​

seed

integer

Valor de semilla para una generación reproducible

​

style_codes

string[]

Arreglo de códigos de estilo en formato hexadecimal

​

style_type

string

predeterminado:"\"GENERAL\""

Valores posibles: `AUTO`, `GENERAL`, `REALISTIC`, `DESIGN`, `FICTION`

Generado a partir del esquema que Router publica en `GET /v2/models/ideogram/ideogram-v3/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

created

string (date-time)

Marca de tiempo de creación de la generación.Formato: `date-time`

​

data

object[]

Arreglo con la información de las imágenes generadas.

​

data[].is_image_safe

boolean

Indica si la imagen se considera segura.

​

data[].prompt

string

El prompt usado para generar esta imagen.

​

data[].resolution

string

La resolución de la imagen generada (p. ej., ‘1024x1024’).

​

data[].seed

integer

El valor de semilla usado para esta generación.

​

data[].style_type

string

El tipo de estilo usado para la generación (p. ej., ‘REALISTIC’, ‘ANIME’).

​

data[].url

string

URL de la imagen generada.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "prompt": "A beautiful mountain landscape",
      "rendering_speed": "TURBO"
    }
    

### 

​

Salida
    
    
    {
      "created": "2026-01-01T00:00:00Z",
      "data": [
        {
          "is_image_safe": true,
          "prompt": "A poster for a jazz festival, bold typography, warm colours",
          "resolution": "1024x1024",
          "seed": 918273645,
          "style_type": "REALISTIC",
          "url": "https://example.invalid/ideogram/ideogram-v3/generated.png"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/ideogram/ideogram-v3/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/ideogram/ideogram-v3/code)

[Ideogram 4.5](https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-4-5/code)[Ideogram 4.0](https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v4/code)
