---
url: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v2-6/code/
title: Usa Kling V2.6 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:08.121996+00:00
---

# Usa Kling V2.6 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v2-6/code/

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

# Usa Kling V2.6 con Comfy Router

Copiar páginaCopiar página

Llama a kling/kling-v2-6 con Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `kling/kling-v2-6`, servida por Comfy Router de Kling. **Entrada:** Texto · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP directo. **ID del modelo:** `kling/kling-v2-6` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-v2-6`

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
            "kling/kling-v2-6",
            {
                "aspect_ratio": "16:9",
                "duration": "5",
                "mode": "std",
                "prompt": "A red fox trotting through falling snow, cinematic lighting.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("kling/kling-v2-6", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "std",
      prompt: "A red fox trotting through falling snow, cinematic lighting.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-v2-6 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"std\", \"prompt\": \"A red fox trotting through falling snow, cinematic lighting.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/kling/kling-v2-6/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge, desde este proceso o desde otro, en cuanto está listo. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) describe el estado, la cancelación y la recogida.

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
                "kling/kling-v2-6",
                {
                    "aspect_ratio": "16:9",
                    "duration": "5",
                    "mode": "std",
                    "prompt": "A red fox trotting through falling snow, cinematic lighting.",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("kling/kling-v2-6", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "std",
      prompt: "A red fox trotting through falling snow, cinematic lighting.",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/kling/kling-v2-6/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"std\", \"prompt\": \"A red fox trotting through falling snow, cinematic lighting.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-v2-6/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/kling/kling-v2-6/requests/$REQUEST_ID \
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

predeterminado:"\"16:9\""

Relación de aspecto del videoValores posibles: `16:9`, `9:16`, `1:1`

​

callback_url

string (uri)

La dirección de notificación de callbackFormato: `uri`

​

camera_control

object

​

camera_control.config

object

​

camera_control.config.horizontal

number

Controla el movimiento de la cámara a lo largo del eje horizontal (eje x). Un valor negativo indica izquierda y un valor positivo indica derecha.Rango: `-10` a `10`

​

camera_control.config.pan

number

Controla la rotación de la cámara en el plano vertical (eje x). Un valor negativo indica rotación hacia abajo y un valor positivo indica rotación hacia arriba.Rango: `-10` a `10`

​

camera_control.config.roll

number

Controla la cantidad de balanceo de la cámara (eje z). Un valor negativo indica sentido antihorario y un valor positivo indica sentido horario.Rango: `-10` a `10`

​

camera_control.config.tilt

number

Controla la rotación de la cámara en el plano horizontal (eje y). Un valor negativo indica rotación a la izquierda y un valor positivo indica rotación a la derecha.Rango: `-10` a `10`

​

camera_control.config.vertical

number

Controla el movimiento de la cámara a lo largo del eje vertical (eje y). Un valor negativo indica hacia abajo y un valor positivo indica hacia arriba.Rango: `-10` a `10`

​

camera_control.config.zoom

number

Controla el cambio en la distancia focal de la cámara. Un valor negativo indica un campo de visión más estrecho y un valor positivo indica un campo de visión más amplio.Rango: `-10` a `10`

​

camera_control.type

string

Tipo de movimiento de cámara predefinido. simple: movimiento de cámara personalizable. down_back: la cámara desciende y se mueve hacia atrás. forward_up: la cámara avanza e inclina hacia arriba. right_turn_forward: rota a la derecha y avanza. left_turn_forward: rota a la izquierda y avanza.Valores posibles: `simple`, `down_back`, `forward_up`, `right_turn_forward`, `left_turn_forward`

​

cfg_scale

number

predeterminado:"0.5"

Flexibilidad en la generación de video. Cuanto mayor sea el valor, menor será el grado de flexibilidad del modelo y mayor la relevancia respecto al prompt del usuario.Rango: `0` a `1`Formato: `float`

​

duration

string

predeterminado:"\"5\""

Duración del video en segundosValores posibles: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`

​

external_task_id

string

ID de tarea personalizado

​

mode

string

predeterminado:"\"std\""

Modo de generación de video. std: modo estándar, que es rentable. pro: modo profesional, genera videos de mayor duración pero con una salida de mayor calidad.Valores posibles: `std`, `pro`

​

model_name

string

Nombre del modelo. Omítelo o envía null cuando uses Comfy Router; el modelo se selecciona mediante la ruta de la solicitud. Un nombre proporcionado debe coincidir con esa ruta.

​

multi_prompt

object[]

Información de cada storyboard, como los prompts y la duración. Admite hasta 6 storyboards, con un mínimo de 1. Es requerido cuando multi_shot es true y shot_type es customize.

​

multi_prompt[].duration

string

Duración de este storyboard en segundos. No debe superar la duración total de la tarea ni ser menor que 1. La suma de las duraciones de todos los storyboards es igual a la duración total de la tarea.

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

Indica si se genera video con múltiples tomas. Cuando es true, el parámetro prompt no es válido. Cuando es false, los parámetros shot_type y multi_prompt no son válidos.

​

negative_prompt

string

Prompt de texto negativo. Se recomienda complementar la información del prompt negativo mediante oraciones negativas directamente dentro de los prompts positivos.

​

prompt

string

Prompt de texto positivo. Usa <<<voice_1>>> para especificar una voz que coincida con el orden del parámetro voice_list. Una tarea puede hacer referencia a hasta 2 tonos. Al especificar un tono, el valor del parámetro sound debe estar en on.

​

shot_type

string

Método de storyboard. Es requerido cuando el parámetro multi_shot está establecido en true.Valores posibles: `customize`, `intelligence`

​

sound

string

predeterminado:"\"off\""

Indica si se genera sonido simultáneamente al generar videos. Solo las versiones V2.6 y posteriores del modelo admiten este parámetro.Valores posibles: `on`, `off`

​

voice_list

object[]

Lista de voces a las que se hace referencia al generar videos. Admite hasta 2 voces; haz referencia a ellas en `prompt` como <<<voice_1>>> y <<<voice_2>>> según el orden de la lista. Requiere `sound` establecido en “on”, lo cual solo admiten las versiones V2.6 y posteriores del modelo; en un modelo anterior, o con `sound` en su valor predeterminado “off”, las voces no se aplican.

​

voice_list[].voice_id

string

requerido

ID de voz devuelto a través de la API de personalización de voces o un ID de voz predefinido del sistema.

​

watermark_info

object

Indica si se generan resultados con marca de agua simultáneamente. Actualmente no se admiten marcas de agua personalizadas.

​

watermark_info.enabled

boolean

true significa generar marca de agua, false significa no generarla.

Generado a partir del esquema que Router sirve en `GET /v2/models/kling/kling-v2-6/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

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

Las unidades de deducción de la tarea

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

URL del video generado con marca de agua, en formato de protección contra hotlinkingFormato: `uri`

​

data.task_status

string

Estado de la tareaValores posibles: `submitted`, `processing`, `succeed`, `failed`

​

data.task_status_msg

string

Información del estado de la tarea, que muestra el motivo del fallo cuando la tarea falla

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
      "mode": "std",
      "prompt": "A red fox trotting through falling snow, cinematic lighting."
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kling/kling-v2-6/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kling/kling-v2-6/code)

[Kling V2.5 Turbo](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v2-5-turbo/code)[Kling V3 Omni](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v3-omni/code)
