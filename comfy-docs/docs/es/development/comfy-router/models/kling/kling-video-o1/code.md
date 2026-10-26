---
url: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-video-o1/code/
title: Usa Kling Video O1 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:08.426895+00:00
---

# Usa Kling Video O1 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-video-o1/code/

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

# Usa Kling Video O1 con Comfy Router

Copiar páginaCopiar página

Llama a kling/kling-video-o1 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `kling/kling-video-o1`, proporcionada por Comfy Router de Kling. **Entrada:** Texto, Imagen, Video · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP directo. **ID del modelo:** `kling/kling-video-o1` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-video-o1`

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
            "kling/kling-video-o1",
            {
                "aspect_ratio": "16:9",
                "duration": "5",
                "mode": "pro",
                "prompt": "A paper boat drifting down a rain-soaked street at dusk.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("kling/kling-video-o1", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "pro",
      prompt: "A paper boat drifting down a rain-soaked street at dusk.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-video-o1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"pro\", \"prompt\": \"A paper boat drifting down a rain-soaked street at dusk.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/kling/kling-video-o1/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "kling/kling-video-o1",
                {
                    "aspect_ratio": "16:9",
                    "duration": "5",
                    "mode": "pro",
                    "prompt": "A paper boat drifting down a rain-soaked street at dusk.",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("kling/kling-video-o1", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "pro",
      prompt: "A paper boat drifting down a rain-soaked street at dusk.",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/kling/kling-video-o1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"pro\", \"prompt\": \"A paper boat drifting down a rain-soaked street at dusk.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-video-o1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/kling/kling-video-o1/requests/$REQUEST_ID \
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

La relación de aspecto del fotograma del video generado (ancho:alto). Es requerida cuando no se usan las funciones de referencia de primer fotograma o de edición de video.Valores posibles: `16:9`, `9:16`, `1:1`

​

callback_url

string (uri)

La dirección de notificación de callback para el resultado de esta tarea. Si se configura, el servidor notificará activamente cuando cambie el estado de la tarea.Formato: `uri`

​

duration

string

predeterminado:"\"5\""

Duración del video en segundos. Cuando usas la función de edición de video (refer_type: base), la duración de salida es la misma que la del video de entrada y este parámetro no es válido.Valores posibles: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`

​

element_list

object[]

Lista de elementos de referencia configurada según el ID de elemento.

​

element_list[].element_id

integer

requerido

ID del elementoFormato: `int64`

​

external_task_id

string

ID de tarea personalizado. Debe ser único dentro de una misma cuenta de usuario.

​

image_list

object[]

Lista de imágenes de referencia. Puede incluir imágenes de referencia del elemento, la escena, el estilo, etc., o usarse como primer o último fotograma para generar videos.

​

image_list[].image_url

string

Codificación Base64 de la imagen o URL de la imagen (asegúrate de que sea accesible). Los formatos admitidos incluyen .jpg/.jpeg/.png. El tamaño del archivo no puede superar los 10 MB. Las dimensiones de ancho y alto no deben ser inferiores a 300 px, con una relación de aspecto entre 1:2.5 y 2.5:1.

​

image_list[].type

string

Indica si la imagen es el primer o el último fotograma. first_frame es el primer fotograma, end_frame es el último fotograma. Actualmente no se admite solo el fotograma final.Valores posibles: `first_frame`, `end_frame`

​

mode

string

predeterminado:"\"pro\""

Modo de generación de video. std: Modo Estándar, genera videos en 720P, con buena relación costo-beneficio. pro: Modo Profesional, genera videos en 1080P, con una salida de video de mayor calidad.Valores posibles: `pro`, `std`

​

model_name

string

Nombre del modelo. Omítelo o envía null cuando uses Comfy Router; el modelo se selecciona según la ruta de la solicitud. Un nombre proporcionado debe coincidir con esa ruta.

​

multi_prompt

object[]

Información de cada storyboard, como los prompts y la duración. Admite hasta 6 storyboards, con un mínimo de 1. Es requerido cuando multi_shot es true y shot_type es customize.

​

multi_prompt[].duration

string

Duración de este storyboard en segundos. No debe superar la duración total de la tarea ni ser inferior a 1. La suma de las duraciones de todos los storyboards equivale a la duración total de la tarea.

​

multi_prompt[].index

integer

Número de secuencia de la toma

​

multi_prompt[].prompt

string

Prompt de este storyboard. Longitud máxima de 512 caracteres.

​

multi_shot

boolean

predeterminado:"false"

Indica si se genera un video de varias tomas. Cuando es true, el parámetro prompt no es válido. Cuando es false, los parámetros shot_type y multi_prompt no son válidos.

​

prompt

string

Prompts de texto, que pueden incluir descripciones positivas y negativas. No debe superar los 2500 caracteres. Puedes especificar elementos, imágenes o videos con el formato <<<>>> como <<element_1>>, <<<image_1>>>, <<<video_1>>>.

​

shot_type

string

Método de storyboard. Es requerido cuando el parámetro multi_shot está en true.Valores posibles: `customize`, `intelligence`

​

sound

string

predeterminado:"\"off\""

Indica si se genera sonido de forma simultánea al generar el video.Valores posibles: `on`, `off`

​

video_list

object[]

Lista de videos de referencia. Puede usarse como video de referencia de una función o como video a editar; de forma predeterminada es el video a editar.

​

video_list[].keep_original_sound

string

Indica si se conserva el sonido original del video. yes indica que se conserva, no indica que no se conserva.Valores posibles: `yes`, `no`

​

video_list[].refer_type

string

Tipo de video de referencia. feature es el video de referencia de una función, base es el video a editar.Valores posibles: `feature`, `base`

​

video_list[].video_url

string

requerido

URL del video cargado. Solo se admiten los formatos .mp4/.mov. Duración entre 3 y 10 segundos. La resolución debe estar entre 720 px y 2160 px. Se admiten velocidades de fotogramas de 24 a 60 fps. Solo se puede cargar 1 video, con un tamaño que no supere los 200 MB.

​

watermark_info

object

Indica si se generan resultados con marca de agua de forma simultánea. Actualmente no se admiten marcas de agua personalizadas.

​

watermark_info.enabled

boolean

true significa que se genera la marca de agua, false significa que no se genera.

Generado a partir del esquema que Router sirve en `GET /v2/models/kling/kling-video-o1/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

code

integer

Código de error

​

data

object

​

data.created_at

integer

Hora de creación de la tarea, marca de tiempo Unix en milisegundos

​

data.final_unit_deduction

string

Unidades de deducción de la tarea

​

data.task_id

string

ID de la tarea

​

data.task_info

object

​

data.task_info.external_task_id

string

​

data.task_result

object

​

data.task_result.videos

object[]

​

data.task_result.videos[].duration

string

Duración total del video en segundos

​

data.task_result.videos[].id

string

ID del video generado

​

data.task_result.videos[].url

string (uri)

URL del video generadoFormato: `uri`

​

data.task_result.videos[].watermark_url

string (uri)

URL del video generado con marca de agua, formato de protección contra enlaces directosFormato: `uri`

​

data.task_status

string

Estado de la tareaValores posibles: `submitted`, `processing`, `succeed`, `failed`

​

data.task_status_msg

string

Información del estado de la tarea; muestra el motivo del fallo cuando la tarea falla

​

data.updated_at

integer

Hora de actualización de la tarea, marca de tiempo Unix en milisegundos

​

data.watermark_info

object

​

data.watermark_info.enabled

boolean

​

message

string

Mensaje de error

​

request_id

string

ID de la solicitud

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "aspect_ratio": "16:9",
      "duration": "5",
      "mode": "pro",
      "prompt": "A paper boat drifting down a rain-soaked street at dusk."
    }
    

### 

​

Salida
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "task_id": "kling-task-1a2b3c4d5e6f",
        "task_result": {
          "videos": [
            {
              "duration": "5",
              "id": "kling-video-6f5e4d3c2b1a",
              "url": "https://example.invalid/kling/kling-v2-5-turbo/generated.mp4"
            }
          ]
        },
        "task_status": "succeed",
        "task_status_msg": "",
        "updated_at": 1798761840000
      },
      "message": "SUCCEED",
      "request_id": "9f2c1a04-7b6e-4d38-8a51-3c0e7d9b2f46"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kling/kling-video-o1/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kling/kling-video-o1/code)

[Kling V3](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v3/code)[Videos Avatar Image 2video](https://docs.comfy.org/es/development/comfy-router/models/kling/videos-avatar-image2video/code)
