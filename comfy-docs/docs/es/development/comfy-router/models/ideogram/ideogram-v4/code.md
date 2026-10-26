---
url: https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v4/code/
title: Usa Ideogram 4.0 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:07.976330+00:00
---

# Usa Ideogram 4.0 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v4/code/

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

# Usa Ideogram 4.0 con Comfy Router

Copiar páginaCopiar página

Fragmentos de Python, TypeScript y cURL para generar imágenes con Ideogram 4.0 por HTTP con Comfy Router, más los campos de solicitud y la forma del resultado.

Copiar páginaCopiar página

Referencia de API de Ideogram 4.0. Ideogram 4.0 es el modelo de texto a imagen de Ideogram, que renderiza texto legible dentro de las imágenes generadas. **Entrada:** Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `ideogram/ideogram-v4` **Endpoint:** `POST https://api.comfy.org/v2/models/ideogram/ideogram-v4`

  * Esperar el resultado

  * Enviar y recoger más tarde




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "ideogram/ideogram-v4",
                {
                    "text_prompt": "a single red maple leaf on a plain white background, studio lighting",
                    "resolution": "1024x1024",
                    "rendering_speed": "DEFAULT",
                },
            )
    
        print("image:", result["data"][0]["url"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    type Result = { data: { url: string }[] };
    const result = await comfy.models.run<Result>("ideogram/ideogram-v4", {
      text_prompt: "a single red maple leaf on a plain white background, studio lighting",
      resolution: "1024x1024",
      rendering_speed: "DEFAULT",
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.data[0].url);
    
    
    
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v4 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text_prompt\": \"a single red maple leaf on a plain white background, studio lighting\", \"resolution\": \"1024x1024\", \"rendering_speed\": \"DEFAULT\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/ideogram/ideogram-v4/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "ideogram/ideogram-v4",
                {
                    "text_prompt": "a single red maple leaf on a plain white background, studio lighting",
                    "resolution": "1024x1024",
                    "rendering_speed": "DEFAULT",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print("image:", result["data"][0]["url"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    type Result = { data: { url: string }[] };
    const handle = await comfy.models.submit<Result>("ideogram/ideogram-v4", {
      text_prompt: "a single red maple leaf on a plain white background, studio lighting",
      resolution: "1024x1024",
      rendering_speed: "DEFAULT",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.data[0].url);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v4/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text_prompt\": \"a single red maple leaf on a plain white background, studio lighting\", \"resolution\": \"1024x1024\", \"rendering_speed\": \"DEFAULT\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ideogram/ideogram-v4/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v4/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

enable_copyright_detection

boolean

Activa la detección de derechos de autor posterior a la generación (comprobaciones de semejanza y logotipos de Hive).

​

json_prompt

object

prompt estructurado de V4. Desactiva Magic Prompt; se consume directamente. Proporciona exactamente uno de text_prompt o json_prompt.

​

rendering_speed

string

predeterminado:"\"DEFAULT\""

El ajuste de velocidad de renderizado que controla el equilibrio entre la velocidad de generación y la calidadValores posibles: `DEFAULT`, `TURBO`, `QUALITY`

​

resolution

string

Resolución de salida en WIDTHxHEIGHT. Omítela para dejar que el modelo elija una relación de aspecto. Valores 2K admitidos: 2048x2048, 1440x2880, 2880x1440, 1664x2496, 2496x1664, 1792x2240, 2240x1792, 1440x2560, 2560x1440, 1600x2560, 2560x1600, 1728x2304, 2304x1728, 1296x3168, 3168x1296, 1152x2944, 2944x1152, 1248x3328, 3328x1248, 1280x3072, 3072x1280.

​

text_prompt

string

prompt en lenguaje natural. Activa Magic Prompt automáticamente. Proporciona exactamente uno de text_prompt o json_prompt.

Generado a partir del esquema que Router sirve en `GET /v2/models/ideogram/ideogram-v4/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

created

string (date-time)

Marca de tiempo en la que se creó la generación.Formato: `date-time`

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

El prompt utilizado para generar esta imagen.

​

data[].resolution

string

La resolución de la imagen generada (p. ej., ‘1024x1024’).

​

data[].seed

integer

El valor de semilla utilizado para esta generación.

​

data[].style_type

string

El tipo de estilo utilizado para la generación (p. ej., ‘REALISTIC’, ‘ANIME’).

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
      "text_prompt": "a single red maple leaf on a plain white background, studio lighting",
      "resolution": "1024x1024",
      "rendering_speed": "DEFAULT"
    }
    

### 

​

Salida
    
    
    {
      "response_type": "url",
      "created": "2026-08-27T21:00:00Z",
      "data": [
        {
          "url": "https://.../image.png",
          "prompt": "a single red maple leaf on a plain white background, studio lighting",
          "resolution": "1024x1024",
          "seed": 1234567890,
          "is_image_safe": true
        }
      ]
    }
    

La URL es temporal. Descarga la imagen cuanto antes si necesitas conservarla.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/ideogram/ideogram-v4/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/ideogram/ideogram-v4/code)

[Ideogram V3](https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v3/code)[P Image Ideogram](https://docs.comfy.org/es/development/comfy-router/models/ideogram/p-image-ideogram/code)
