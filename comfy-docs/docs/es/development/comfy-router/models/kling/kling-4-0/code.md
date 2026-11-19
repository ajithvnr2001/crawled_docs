---
url: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-4-0/code/
title: Usar Kling 4.0 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-19T16:26:09.956191+00:00
---

# Usar Kling 4.0 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-4-0/code/

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



Kling

# Usar Kling 4.0 con Comfy Router

Copiar páginaCopiar página

Llama a kling/kling-4.0 a través de Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `kling/kling-4.0`, servido por Comfy Router desde Kling. **Entrada:** Texto, Imagen, Video · **Salida:** Video

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `kling/kling-4.0` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-4.0`

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
            "kling/kling-4.0",
            {
                "contents": [
                    {
                        "text": "The fox turns toward the camera.",
                        "type": "prompt",
                    },
                    {
                        "type": "first_frame",
                        "url": "https://example.com/fox.png",
                    },
                ],
                "settings": {
                    "duration": 3,
                    "resolution": "720p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("kling/kling-4.0", {
      contents: [
        {
          text: "The fox turns toward the camera.",
          type: "prompt",
        },
        {
          type: "first_frame",
          url: "https://example.com/fox.png",
        },
      ],
      settings: {
        duration: 3,
        resolution: "720p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-4.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"text\":\"The fox turns toward the camera.\",\"type\":\"prompt\"},{\"type\":\"first_frame\",\"url\":\"https://example.com/fox.png\"}], \"settings\": {\"duration\":3,\"resolution\":\"720p\"}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/kling/kling-4.0/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [La entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "kling/kling-4.0",
                {
                    "contents": [
                        {
                            "text": "The fox turns toward the camera.",
                            "type": "prompt",
                        },
                        {
                            "type": "first_frame",
                            "url": "https://example.com/fox.png",
                        },
                    ],
                    "settings": {
                        "duration": 3,
                        "resolution": "720p",
                    },
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("kling/kling-4.0", {
      contents: [
        {
          text: "The fox turns toward the camera.",
          type: "prompt",
        },
        {
          type: "first_frame",
          url: "https://example.com/fox.png",
        },
      ],
      settings: {
        duration: 3,
        resolution: "720p",
      },
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/kling/kling-4.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"text\":\"The fox turns toward the camera.\",\"type\":\"prompt\"},{\"type\":\"first_frame\",\"url\":\"https://example.com/fox.png\"}], \"settings\": {\"duration\":3,\"resolution\":\"720p\"}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-4.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/kling/kling-4.0/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

contents

object[]

El prompt y los medios de entrada. Incluir solo elementos “prompt”, “first_frame”, “middle_frame” y “last_frame” selecciona imagen a video (un prompt y hasta 10 fotogramas); incluir cualquier “refer_image”, “feature_video”, “base_video”, “element” o “voice” selecciona omni video (hasta 15 entradas, con como máximo 10 imágenes, 5 videos, 7 elementos y 3 voces). Una solicitud con un “feature_video”, un “base_video” o un elemento de personaje de video se factura con la tarifa de entrada de video.

contents[].element_id

string

ID del elemento, cuando el tipo es “element”.

contents[].id

string

ID de referencia para esta entrada, usado como @id en el prompt. Debe ser único dentro de la tarea. Requerido para “element” y “voice”.

contents[].text

string

Prompt de texto, cuando el tipo es “prompt”. Hasta 26,000 caracteres en inglés u 11,000 en caracteres de otro idioma; comfy-api exige de 1 a 26,000 caracteres, y Kling rechaza el texto no inglés más largo. Haz referencia a otras entradas como @id.

contents[].type

string

requerido

Tipo de entrada. Imagen a video acepta solo “prompt”, “first_frame”, “middle_frame” y “last_frame”, y rechaza cualquier otro tipo. Omni video también acepta “refer_image”, “feature_video” (un video de referencia), “base_video” (el video a editar, como máximo uno), “element” y “voice”.Valores posibles: `prompt`, `first_frame`, `middle_frame`, `last_frame`, `refer_image`, `feature_video`, `base_video`, `element`, `voice`

contents[].url

string

URL de imagen o video, cuando el tipo es un fotograma, “refer_image”, “feature_video” o “base_video”. Las imágenes también pueden ser Base64. Las imágenes son .jpg, .jpeg o .png de hasta 30MB, con al menos 300px por lado y una relación de aspecto entre 2:5 y 5:2. Los videos son .mp4 o .mov de hasta 300MB y de 3 a 30 segundos de duración.

contents[].voice_id

string

ID de voz, cuando el tipo es “voice”. Una voz predefinida de Kling o una voz personalizada.

options

object

Configuración general, como las opciones de marca de agua. `options.callback_url` y `options.external_task_id` no son compatibles con Kling 4.0; Comfy Router rechaza una solicitud que establezca cualquiera de los dos dentro de `options`. Un `callback_url` o `external_task_id` de nivel superior no forma parte de este esquema y se elimina antes de que la solicitud llegue a Kling.

options.watermark_info

object

Indica si se generan resultados con marca de agua de forma simultánea. Las marcas de agua personalizadas no son compatibles. Un null explícito se trata como ausente, igual que lo hacen la comprobación de Kling 4.0 en /proxy y Kling.

options.watermark_info.enabled

boolean

true significa generar el resultado con marca de agua, false significa no generarlo. Valor predeterminado false.

prompt

string

Prompt de texto a video. Requerido cuando `contents` está ausente o vacío, y rechazado junto con un `contents` no vacío. Hasta 26,000 caracteres en inglés u 11,000 en caracteres de otro idioma; comfy-api exige de 1 a 26,000 caracteres, y Kling rechaza el texto no inglés más largo.

settings

object

requerido

Configuración de salida, como resolución, relación de aspecto y duración.

settings.aspect_ratio

string

Relación de aspecto (ancho:alto) de los fotogramas generados. Una de “21:9”, “16:9”, “9:16”, “1:1”, “4:3” o “3:4” para texto a video (predeterminada “16:9”), esas mismas o “adaptive” para omni video (predeterminada “adaptive”). Imagen a video sigue a las imágenes. Un null explícito se trata como ausente, igual que lo hacen la comprobación de Kling 4.0 en /proxy y Kling.Valores posibles: `21:9`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `adaptive`

settings.duration

integer

Duración del video en segundos, de 3 a 30. Requerido a menos que `contents` contenga un “base_video”, donde una edición puede omitirlo para conservar la duración del video base. Esa llamada se retiene y se estima con el máximo de 30 segundos en la resolución solicitada, un límite superior en lugar del precio, y se factura según el precio que Kling reporta para la tarea finalizada.Alcance: `3` a `30`

settings.resolution

string

requerido

Resolución del video generado. Una de “720p” o “1080p”. Requerido.Valores posibles: `720p`, `1080p`

Generado a partir del esquema que Router publica en `GET /v2/models/kling/kling-4.0/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

code

integer

Código de error. 0 indica éxito.

data

object[]

Tareas que coinciden con la consulta.

data[].billing

object[]

Detalles de facturación de la tarea.

data[].billing[].amount

string

Cantidad de consumo, con precisión de dos decimales.

data[].billing[].cash_type

string

Cuenta de efectivo desde la que se cobró el cargo (solo está presente cuando charge_type es “cash”), por ejemplo “balance”. Algunas tareas la devuelven; otras pueden omitirla.

data[].billing[].charge_type

string

Tipo de cuenta de consumo. “cash” para saldo, “unit” para un paquete de recursos.

data[].billing[].currency

string

Código de moneda ISO 4217 de `amount` y `list_price`, por ejemplo “USD”. Algunas tareas lo devuelven; otras pueden omitirlo.

data[].billing[].list_price

string

Precio de lista de la tarea antes de cualquier descuento, como cadena decimal. Algunas tareas lo devuelven; otras pueden omitirlo.

data[].billing[].package_type

string

Tipo de paquete de recursos consumibles (solo está presente cuando charge_type es “unit”). Uno de “video”, “image” o “audio”.

data[].create_time

integer

Hora de creación de la tarea. Marca de tiempo Unix en milisegundos.Formato: `int64`

data[].external_id

string

El ID de tarea personalizado de esta tarea, si existe.

data[].id

string

El ID de la tarea.

data[].message

string

Información del estado de la tarea, que muestra el motivo del fallo cuando la tarea falla.

data[].outputs

object[]

Salidas generadas de la tarea.

data[].outputs[].duration

string

Duración del video generado en segundos.

data[].outputs[].group_id

string

Marcador de agrupación, presente solo en imágenes agrupadas.

data[].outputs[].id

string

ID de salida generado por el sistema.

data[].outputs[].mp3_duration

string

Duración del audio MP3 generado en segundos.

data[].outputs[].mp3_url

string

URL del MP3 del audio generado (con protección contra hotlinking).

data[].outputs[].name

string

Nombre del material generado.

data[].outputs[].owned_by

string

Fuente del material. “kling” indica la biblioteca oficial; los números son IDs de creador.

data[].outputs[].status

string

Estado del material. Uno de “succeeded” o “deleted”.

data[].outputs[].type

string

Tipo de contenido de salida. Uno de “video”, “image”, “audio”, “voice” o “element”.

data[].outputs[].url

string

URL del resultado generado (con protección contra hotlinking). Se borra después de 30 días.

data[].outputs[].watermark_url

string

URL del resultado con marca de agua (con protección contra hotlinking).

data[].outputs[].wav_duration

string

Duración del audio WAV generado en segundos.

data[].outputs[].wav_url

string

URL del WAV del audio generado (con protección contra hotlinking).

data[].status

string

Estado de la tarea. Uno de “submitted”, “processing”, “succeeded” o “failed”.

data[].update_time

integer

Hora de actualización de la tarea. Marca de tiempo Unix en milisegundos.Formato: `int64`

message

string

Mensaje de error.

request_id

string

ID de solicitud generado por el sistema.

## Ejemplos

### Entrada
    
    
    {
      "contents": [
        {
          "text": "The fox turns toward the camera.",
          "type": "prompt"
        },
        {
          "type": "first_frame",
          "url": "https://example.com/fox.png"
        }
      ],
      "settings": {
        "duration": 3,
        "resolution": "720p"
      }
    }
    

### Salida
    
    
    {
      "code": 0,
      "data": [
        {
          "create_time": 1798761600000,
          "id": "kling-v2-task-7c8d9e0f1a2b",
          "message": "",
          "outputs": [
            {
              "duration": "5",
              "id": "kling-v2-output-2b1a0f9e8d7c",
              "type": "video",
              "url": "https://example.invalid/kling/v2/generated.mp4"
            }
          ],
          "status": "succeeded",
          "update_time": 1798761820000
        }
      ],
      "message": "SUCCEED",
      "request_id": "3d7e5c91-0b42-4f68-9a13-8e2c6d4b0a75"
    }
    

## Antes de lanzar

Los SDK crean una `Idempotency-Key` y la reutilizan para los reintentos automáticos. Para los reintentos manuales, reutiliza la clave original. Router puede mantener la conexión abierta hasta 10 minutos. Cuando una solicitud falla, Router envía un encabezado de respuesta `X-Comfy-Error-Type` que explica el motivo. Un `422` significa que Router rechazó la entrada antes de llamar al proveedor, y un `413` significa que el cuerpo de la solicitud era más grande de lo que Router acepta. Descarga los recursos generados de inmediato, porque [las URL de resultados pueden caducar](https://docs.comfy.org/es/development/comfy-router/reference#recursos-del-resultado). Cualquier límite de tamaño mencionado en la descripción de un campo más arriba es el límite propio del proveedor para ese campo, citado de la especificación del proveedor. Router aplica un tope aparte al cuerpo completo de la solicitud, con el que cuentan los medios codificados en base64: consulta [tamaño del cuerpo de la solicitud](https://docs.comfy.org/es/development/comfy-router/limitations#los-cuerpos-de-las-solicitudes-tienen-un-l%C3%ADmite). Esta página documenta un modelo socio al que se llama a través de Comfy Router. El mismo paquete `comfy-sdk` / `@comfyorg/sdk` también incluye un segundo cliente, para ejecutar todo un gráfico de flujo de trabajo de ComfyUI en Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, con `client.workflows`, `client.assets` y `client.jobs`. Consulta [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks).

## Encabezados

Autenticación, idempotencia, IDs de solicitud, agrupaciones de errores, ritmo de reintentos y límites de gasto.

## Uso de la API de Router

Descubrimiento de modelos, errores de validación, reintentos y facturación.

## Limitaciones

Lo que Router no hace hoy y qué usar en su lugar.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kling/kling-4-0/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kling/kling-4-0/code)

[Kling 3.0 Turbo](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-3-0-turbo/code)[Kling Image 4.0](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-image-4-0/code)
