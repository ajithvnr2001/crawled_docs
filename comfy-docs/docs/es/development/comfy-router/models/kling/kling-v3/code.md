---
url: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v3/code/
title: Usa Kling V3 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:08.557969+00:00
---

# Usa Kling V3 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v3/code/

## En esta página

Volver arriba

  * Inicio rápido
  * Proveedores que lo sirven
  * Esquema
    * Entrada
    * Salida
  * Ejemplos
    * Entrada
    * Salida
  * Antes de lanzar



Kling

# Usa Kling V3 con Comfy Router

Copiar páginaCopiar página

Llama a kling/kling-v3 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `kling/kling-v3`, proporcionada por Comfy Router de Kling. **Entrada:** Texto · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `kling/kling-v3` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-v3`

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
            "kling/kling-v3",
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
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("kling/kling-v3", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "std",
      prompt: "A red fox trotting through falling snow, cinematic lighting.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-v3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"std\", \"prompt\": \"A red fox trotting through falling snow, cinematic lighting.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/kling/kling-v3/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "kling/kling-v3",
                {
                    "aspect_ratio": "16:9",
                    "duration": "5",
                    "mode": "std",
                    "prompt": "A red fox trotting through falling snow, cinematic lighting.",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("kling/kling-v3", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "std",
      prompt: "A red fox trotting through falling snow, cinematic lighting.",
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
    curl https://api.comfy.org/v2/models/kling/kling-v3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"std\", \"prompt\": \"A red fox trotting through falling snow, cinematic lighting.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-v3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras todavía se está ejecutando.
    curl https://api.comfy.org/v2/models/kling/kling-v3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Proveedores que lo sirven

Comfy Router sirve este modelo directamente a menos que la solicitud indique otro proveedor. Los proveedores siguientes también lo sirven, en el mismo endpoint y con el mismo ID de modelo, y se seleccionan con el parámetro de consulta `model_provider`.

  * **Comfy** (predeterminado): `POST https://api.comfy.org/v2/models/kling/kling-v3`
  * **Higgsfield** , como `higgsfield/higgsfield-kling-3-std`: `POST https://api.comfy.org/v2/models/kling/kling-v3?model_provider=higgsfield`
  * **Tencent** : `POST https://api.comfy.org/v2/models/kling/kling-v3?model_provider=tencent`

`strict_mode` tiene como valor predeterminado falso, por lo que Router traduce el cuerpo de la solicitud nativo documentado en esta página al esquema propio del proveedor y traduce la respuesta de vuelta. Consulta [`model_provider`, `strict_mode` y `fallback_provider`](https://docs.comfy.org/es/development/comfy-router/reference#post-v2modelsprovidermodel) en la Referencia de la API, y [Proveedores que lo sirven](https://docs.comfy.org/es/development/comfy-router/providers) para todos los modelos enrutados de esta forma.

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

Dirección de notificación del callbackFormato: `uri`

​

camera_control

object

​

camera_control.config

object

​

camera_control.config.horizontal

number

Controla el movimiento de la cámara a lo largo del eje horizontal (eje x). Negativo indica izquierda, positivo indica derecha.Rango: `-10` a `10`

​

camera_control.config.pan

number

Controla la rotación de la cámara en el plano vertical (eje x). Negativo indica rotación hacia abajo, positivo indica rotación hacia arriba.Rango: `-10` a `10`

​

camera_control.config.roll

number

Controla la cantidad de balanceo de la cámara (eje z). Negativo indica sentido antihorario, positivo indica sentido horario.Rango: `-10` a `10`

​

camera_control.config.tilt

number

Controla la rotación de la cámara en el plano horizontal (eje y). Negativo indica rotación a la izquierda, positivo indica rotación a la derecha.Rango: `-10` a `10`

​

camera_control.config.vertical

number

Controla el movimiento de la cámara a lo largo del eje vertical (eje y). Negativo indica hacia abajo, positivo indica hacia arriba.Rango: `-10` a `10`

​

camera_control.config.zoom

number

Controla el cambio en la distancia focal de la cámara. Negativo indica un campo de visión más estrecho, positivo indica un campo de visión más amplio.Rango: `-10` a `10`

​

camera_control.type

string

Tipo de movimientos de cámara predefinidos. simple: movimiento de cámara personalizable. down_back: la cámara desciende y se mueve hacia atrás. forward_up: la cámara avanza y se inclina hacia arriba. right_turn_forward: gira a la derecha y avanza. left_turn_forward: gira a la izquierda y avanza.Valores posibles: `simple`, `down_back`, `forward_up`, `right_turn_forward`, `left_turn_forward`

​

cfg_scale

number

predeterminado:"0.5"

Flexibilidad en la generación de video. Cuanto mayor sea el valor, menor será el grado de flexibilidad del modelo y más fuerte la relevancia respecto al prompt del usuario.Rango: `0` a `1`Formato: `float`

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

Información de cada storyboard, como los prompts y la duración. Admite hasta 6 storyboards, con un mínimo de 1. Requerido cuando multi_shot es true y shot_type es customize.

​

multi_prompt[].duration

string

Duración de este storyboard en segundos. No debe superar la duración total de la tarea ni ser inferior a 1. La suma de las duraciones de todos los storyboards equivale a la duración total de la tarea.

​

multi_prompt[].index

integer

Número de secuencia del plano

​

multi_prompt[].prompt

string

Prompt de este storyboard. Longitud máxima de 512 caracteres.

​

multi_shot

boolean

predeterminado:"false"

Indica si se genera video multi-shot. Cuando es true, el parámetro prompt no es válido. Cuando es false, los parámetros shot_type y multi_prompt no son válidos.

​

negative_prompt

string

Prompt de texto negativo. Se recomienda complementar la información del prompt negativo mediante frases negativas directamente en los prompts positivos.

​

prompt

string

Prompt de texto positivo. Usa <<<voice_1>>> para especificar una voz que coincida con el orden del parámetro voice_list. Una tarea puede hacer referencia a hasta 2 tonos. Cuando especifiques un tono, el valor del parámetro sound debe estar en on.

​

shot_type

string

Método de storyboard. Requerido cuando el parámetro multi_shot está establecido en true.Valores posibles: `customize`, `intelligence`

​

sound

string

predeterminado:"\"off\""

Indica si se genera sonido simultáneamente al generar videos. Solo las versiones V2.6 y posteriores del modelo admiten este parámetro.Valores posibles: `on`, `off`

​

voice_list

object[]

Lista de voces a las que se hace referencia al generar videos. Admite hasta 2 voces; referéncialas en `prompt` como <<<voice_1>>> y <<<voice_2>>> según el orden de la lista. Requiere `sound` establecido en “on”, que solo admiten las versiones V2.6 y posteriores del modelo; en un modelo anterior, o con `sound` en su valor predeterminado “off”, las voces no se aplican.

​

voice_list[].voice_id

string

requerido

ID de voz devuelto por la API de personalización de voces o un ID de voz preestablecido del sistema.

​

watermark_info

object

Indica si se generan resultados con marca de agua simultáneamente. Actualmente no se admite una marca de agua personalizada.

​

watermark_info.enabled

boolean

true significa generar marca de agua, false significa no generarla.

Generado a partir del esquema que Router expone en `GET /v2/models/kling/kling-v3/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

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

URL del video generado con marca de agua, formato de protección contra hotlinkingFormato: `uri`

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kling/kling-v3/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kling/kling-v3/code)

[Kling V3 Omni](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v3-omni/code)[Kling Video O1](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-video-o1/code)
