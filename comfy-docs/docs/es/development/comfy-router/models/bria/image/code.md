---
url: https://docs.comfy.org/es/development/comfy-router/models/bria/image/code/
title: Usa Image con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:59.623263+00:00
---

# Usa Image con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/bria/image/code/

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



Bria

# Usa Image con Comfy Router

Copiar páginaCopiar página

Llama a bria/image mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `bria/image`, proporcionada por Comfy Router de Bria. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `bria/image` **Endpoint:** `POST https://api.comfy.org/v2/models/bria/image`

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
            "bria/image",
            {
                "prompt": "A red vintage bicycle leaning against a brick wall in soft morning light",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("bria/image", {
      prompt: "A red vintage bicycle leaning against a brick wall in soft morning light",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bria/image \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A red vintage bicycle leaning against a brick wall in soft morning light\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bria/image/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. La [entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) describe el estado, la cancelación y la recogida.

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
                "bria/image",
                {
                    "prompt": "A red vintage bicycle leaning against a brick wall in soft morning light",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
            # Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("bria/image", {
      prompt: "A red vintage bicycle leaning against a brick wall in soft morning light",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/bria/image/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A red vintage bicycle leaning against a brick wall in soft morning light\"}"
    
    # 2. Sondea hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bria/image/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/bria/image/requests/$REQUEST_ID \
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

predeterminado:"\"1:1\""

Relación de aspecto de la imagen de salida, una de “1:1”, “2:3”, “3:2”, “3:4”, “4:3”, “4:5”, “5:4”, “9:16”, “16:9”, “16:10”, “10:16”, “2:1”, “1:2”, “21:9”, “9:21”, “3:1”, “1:3”, “4:1”, “1:4”, “5:1” o “1:5”. Bria rechaza las relaciones desde “16:10” en adelante con “4MP”, con un refinamiento que envía tanto prompt como structured_prompt, y con imágenes que no tienen prompt.

​

images

string[]

Una imagen de referencia que inspira la nueva imagen. URL disponible públicamente o codificada en Base64. Formatos aceptados: JPEG, JPG, PNG, WEBP. Debe contener exactamente un elemento.

​

ip_signal

boolean

predeterminado:"false"

Si es verdadero, devuelve una advertencia por posible contenido con IP en el prompt.

​

model_version

string

La versión del modelo que se va a usar. Solo se acepta “FIBO”; omítela para ejecutar el mismo modelo.

​

output_type

string

predeterminado:"\"png\""

Formato de la imagen de salida, “png” o “jpeg”.

​

prompt

string

Instrucción basada en texto. Úsala sola para generar una nueva imagen, o con images o structured_prompt para guiar o refinar el resultado.

​

prompt_content_moderation

boolean

predeterminado:"true"

Si es verdadero, devuelve 422 cuando falla la moderación del prompt.

​

resolution

string

predeterminado:"\"1MP\""

Resolución de la imagen de salida, “1MP” o “4MP”. “4MP” mejora los detalles de la imagen pero aumenta la latencia en unos 30 segundos.

​

seed

integer

Semilla para una generación determinista. Si se omite, se usa una semilla aleatoria.

​

structured_prompt

string

Una cadena que contiene el prompt estructurado en formato JSON, del resultado de una generación anterior. Úsala con la misma semilla para recrear esa imagen, o cambia parte de ella para refinar la imagen.

​

sync

boolean

Debe ser false u omitirse. El modo síncrono de Bria (true) se rechaza en lugar de reenviarse, tanto en Comfy Router como en la ruta `/proxy/` propia de esta operación: Comfy Router fija el modo de retorno antes del despacho y consulta el resultado dentro de la llamada, y la ruta `/proxy/` devuelve el request_id y el status_url que se deben consultar.

​

visual_input_content_moderation

boolean

predeterminado:"true"

Si es verdadero, devuelve 422 cuando falla la moderación de las imágenes.

​

visual_output_content_moderation

boolean

predeterminado:"true"

Si es verdadero, devuelve 422 cuando falla la moderación de la salida visual.

Generado a partir del esquema que Router sirve en `GET /v2/models/bria/image/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

object

Objeto de error (solo presente cuando el estado es ERROR)

​

error.code

integer

Código de error.

​

error.details

string

Detalles adicionales del error.

​

error.message

string

Mensaje de error.

​

request_id

string

Identificador único de la solicitud.

​

result

object

Objeto de resultado (solo presente cuando el estado es COMPLETED)

​

result.image_url

string

URL de la imagen generada o editada.

​

result.prompt

string

Prompt original.

​

result.refined_prompt

string

Versión refinada del prompt, o null en una generación COMPLETED que Bria no refinó. Es anulable porque la clave está PRESENTE con null en lugar de omitirse; se observó en vivo en bria/image-edit-gen-fill.

​

result.seed

integer

Semilla usada para la generación.

​

result.structured_instruction

string

La instrucción estructurada, un documento JSON serializado como cadena, que devuelve `/v2/structured_instruction/generate`. Esa operación no rellena ninguna de las dos URL.

​

result.structured_prompt

string

El prompt estructurado detallado en JSON.

​

result.video_url

string

URL del video generado.

​

status

string

Estado actual de la solicitud.Valores posibles: `IN_PROGRESS`, `COMPLETED`, `ERROR`, `UNKNOWN`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "prompt": "A red vintage bicycle leaning against a brick wall in soft morning light"
    }
    

### 

​

Salida
    
    
    {
      "request_id": "0b3f9d7e-2c41-4a8b-9f10-6d5c8e2a4b71",
      "result": {
        "image_url": "https://example.invalid/bria/image/generated.png",
        "seed": 42
      },
      "status": "COMPLETED"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/bria/image/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/bria/image/code)

[Image Edit Restore](https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-restore/code)[Video Edit Erase](https://docs.comfy.org/es/development/comfy-router/models/bria/video-edit-erase/code)
