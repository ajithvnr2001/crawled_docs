---
url: https://docs.comfy.org/es/development/comfy-router/models/synclabs/sync-3/code/
title: Usa Sync 3 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:20.070468+00:00
---

# Usa Sync 3 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/synclabs/sync-3/code/

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



Synclabs

# Usa Sync 3 con Comfy Router

Copiar páginaCopiar página

Llama a synclabs/sync-3 con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API de `synclabs/sync-3`, servida por Comfy Router desde Synclabs. **Entrada:** Video, Imagen, Audio, Texto · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `synclabs/sync-3` **Endpoint:** `POST https://api.comfy.org/v2/models/synclabs/sync-3`

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
            "synclabs/sync-3",
            {
                "input": [
                    {
                        "type": "video",
                        "url": "https://example.invalid/synclabs/sync-3/speaker.mp4",
                    },
                    {
                        "type": "audio",
                        "url": "https://example.invalid/synclabs/sync-3/voiceover.wav",
                    },
                ],
                "options": {
                    "sync_mode": "bounce",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("synclabs/sync-3", {
      input: [
        {
          type: "video",
          url: "https://example.invalid/synclabs/sync-3/speaker.mp4",
        },
        {
          type: "audio",
          url: "https://example.invalid/synclabs/sync-3/voiceover.wav",
        },
      ],
      options: {
        sync_mode: "bounce",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/synclabs/sync-3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": [{\"type\":\"video\",\"url\":\"https://example.invalid/synclabs/sync-3/speaker.mp4\"},{\"type\":\"audio\",\"url\":\"https://example.invalid/synclabs/sync-3/voiceover.wav\"}], \"options\": {\"sync_mode\":\"bounce\"}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/synclabs/sync-3/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "synclabs/sync-3",
                {
                    "input": [
                        {
                            "type": "video",
                            "url": "https://example.invalid/synclabs/sync-3/speaker.mp4",
                        },
                        {
                            "type": "audio",
                            "url": "https://example.invalid/synclabs/sync-3/voiceover.wav",
                        },
                    ],
                    "options": {
                        "sync_mode": "bounce",
                    },
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("synclabs/sync-3", {
      input: [
        {
          type: "video",
          url: "https://example.invalid/synclabs/sync-3/speaker.mp4",
        },
        {
          type: "audio",
          url: "https://example.invalid/synclabs/sync-3/voiceover.wav",
        },
      ],
      options: {
        sync_mode: "bounce",
      },
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/synclabs/sync-3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": [{\"type\":\"video\",\"url\":\"https://example.invalid/synclabs/sync-3/speaker.mp4\"},{\"type\":\"audio\",\"url\":\"https://example.invalid/synclabs/sync-3/voiceover.wav\"}], \"options\": {\"sync_mode\":\"bounce\"}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/synclabs/sync-3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/synclabs/sync-3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

dubParams

object

Parámetros de doblaje adjuntos a una solicitud de generación de Sync Labs

​

dubParams.numSpeakers

integer

Número de hablantes en el video de origen; 0 activa la detección automática

​

dubParams.providerName

string

requerido

Proveedor que se usará para el doblaje (por ejemplo, elevenlabs)

​

dubParams.sourceLang

string

Código del idioma de origen; por defecto es auto

​

dubParams.targetLang

string

requerido

Código del idioma objetivo para el doblaje

​

input

object[]

requerido

Elementos de entrada; exactamente una entrada visual (video o imagen) y una entrada de audio o de texto

​

input[].assetId

string

ID de un recurso de la biblioteca multimedia de Sync Labs

​

input[].provider

object

Configuración del proveedor de texto a voz para una entrada de texto de Sync Labs

​

input[].provider.name

string

requerido

Nombre del proveedor TTS (por ejemplo, elevenlabs)

​

input[].provider.script

string

requerido

Guion que se usará para la generación

​

input[].provider.similarityBoost

number

Qué tan fielmente debe ceñirse la IA a la voz originalFormato: `double`

​

input[].provider.stability

number

Estabilidad de la voz; los valores más bajos introducen una gama emocional más ampliaFormato: `double`

​

input[].provider.voiceId

string

requerido

ID de voz de Sync (voz clonada del Studio) o ID de voz de ElevenLabs

​

input[].refId

string

Identificador de referencia usado para vincular esta entrada a las definiciones de segmentos

​

input[].segments_frames

integer[][]

Obsoleto: usa el arreglo segments de nivel superior en su lugar

​

input[].segments_secs

number[][]

Obsoleto: usa el arreglo segments de nivel superior en su lugar

​

input[].type

string

requerido

Tipo de entrada (video, imagen, audio o texto)

​

input[].url

string

URL del contenido multimedia que se usará para la generación

​

model

string

Nombre del modelo que se usará para la generación; solo se admite sync-3. En la ruta de Comfy Router `POST /v2/models/synclabs/{model}`, este campo se toma de la ruta y se puede omitir.

​

options

object

Opciones adicionales disponibles para una generación de Sync Labs

​

options.active_speaker_detection

object

Configuración de la detección del hablante activo

​

options.active_speaker_detection.auto_detect

boolean

Si se debe detectar automáticamente al hablante activo y aplicarle la generación

​

options.active_speaker_detection.bounding_boxes

integer[][]

Arreglo por cuadro de cuadros delimitadores [x1, y1, x2, y2] para el rostro detectado

​

options.active_speaker_detection.bounding_boxes_url

string

URL de un archivo JSON que contiene los cuadros delimitadores

​

options.active_speaker_detection.coordinates

integer[]

Coordenadas de píxel [x, y] en el cuadro del video de origen identificado por frame_number

​

options.active_speaker_detection.frame_number

integer

Índice del cuadro que corresponde a las coordenadas proporcionadas para la selección manual del hablante

​

options.active_speaker_detection.v3

boolean

Si se debe usar ASD v3

​

options.model_mode

string

Región de edición para el modelo (labios, rostro, cabeza); solo funciona con react-1

​

options.occlusion_detection_enabled

boolean

Si se debe detectar la oclusión durante la generación

​

options.prompt

string

Prompt de emoción; solo funciona con react-1

​

options.sync_mode

string

Cómo manejar las discrepancias de duración entre el video y el audio (bounce, loop, cut_off, silence, remap)

​

options.temperature

number

Qué tan expresivo puede ser el lipsync, de 0 a 1Formato: `double`

​

outputFileName

string

Nombre de archivo base para la salida generada, sin extensión

​

projectId

string

De manera opcional, vincula esta generación a un proyecto de Sync Labs

​

segments

object[]

Definiciones de segmentos que aplican distintas entradas de audio a distintos segmentos de video

​

segments[].audioInput

object

requerido

Configuración de la entrada de audio para un segmento específico

​

segments[].audioInput.endTime

number

Hora de finalización opcional, en segundos, para recortar el audio de referenciaFormato: `double`

​

segments[].audioInput.refId

string

requerido

ID de referencia de la entrada de audio o de texto a voz que se usará para este segmento

​

segments[].audioInput.startTime

number

Hora de inicio opcional, en segundos, para recortar el audio de referenciaFormato: `double`

​

segments[].endTime

number

requerido

Hora de finalización del segmento, en segundosFormato: `double`

​

segments[].optionsOverride

object

Anular las opciones de generación para un segmento específico

​

segments[].optionsOverride.active_speaker_detection

object

Configuración de la detección del hablante activo

​

segments[].optionsOverride.active_speaker_detection.auto_detect

boolean

Si se debe detectar y aplicar automáticamente la generación al hablante activo

​

segments[].optionsOverride.active_speaker_detection.bounding_boxes

integer[][]

Arreglo por fotograma de cuadros delimitadores [x1, y1, x2, y2] del rostro detectado

​

segments[].optionsOverride.active_speaker_detection.bounding_boxes_url

string

URL de un archivo JSON que contiene los cuadros delimitadores

​

segments[].optionsOverride.active_speaker_detection.coordinates

integer[]

Coordenadas en píxeles [x, y] dentro del fotograma del video de origen identificado por frame_number

​

segments[].optionsOverride.active_speaker_detection.frame_number

integer

Índice del fotograma que corresponde a las coordenadas proporcionadas para la selección manual del hablante

​

segments[].optionsOverride.active_speaker_detection.v3

boolean

Si se debe usar ASD v3

​

segments[].optionsOverride.occlusion_detection_enabled

boolean

Anula la detección de oclusión para este segmento

​

segments[].optionsOverride.sync_mode

string

Anula el modo de sincronización para este segmento

​

segments[].optionsOverride.temperature

number

Anula la temperatura (0-1) para este segmentoFormato: `double`

​

segments[].startTime

number

requerido

Hora de inicio del segmento en segundosFormato: `double`

​

webhookUrl

string

URL del webhook para las actualizaciones del estado de generación

Generado a partir del esquema que Router sirve en `GET /v2/models/synclabs/sync-3/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

createdAt

string

La fecha y hora en que se creó la generación

​

error

string

El mensaje de error si la generación falló

​

errorCode

string

Código de error estable y legible por máquina si la generación falló

​

id

string

Identificador único de la generación

​

input

object[]

Los elementos de entrada usados para la generación

​

input[].assetId

string

ID de un recurso de la biblioteca de medios de Sync Labs

​

input[].provider

object

Configuración del proveedor de texto a voz para una entrada de texto de Sync Labs

​

input[].provider.name

string

requerido

Nombre del proveedor de TTS (p. ej., elevenlabs)

​

input[].provider.script

string

requerido

Guion que se usará para la generación

​

input[].provider.similarityBoost

number

Qué tan fielmente debe ceñirse la IA a la voz originalFormato: `double`

​

input[].provider.stability

number

Estabilidad de la voz; los valores más bajos introducen un rango emocional más amplioFormato: `double`

​

input[].provider.voiceId

string

requerido

ID de voz de Sync (voz clonada del Studio) o ID de voz de ElevenLabs

​

input[].refId

string

Identificador de referencia que se usa para vincular esta entrada con las definiciones de segmento

​

input[].segments_frames

integer[][]

Obsoleto: usa el array segments de nivel superior en su lugar

​

input[].segments_secs

number[][]

Obsoleto: usa el array segments de nivel superior en su lugar

​

input[].type

string

requerido

Tipo de entrada (video, imagen, audio o texto)

​

input[].url

string

URL del medio que se usará para la generación

​

model

string

El nombre del modelo usado para la generación

​

options

object

Opciones adicionales disponibles para una generación de Sync Labs

​

options.active_speaker_detection

object

Configuración de detección del hablante activo

​

options.active_speaker_detection.auto_detect

boolean

Indica si se debe detectar automáticamente al hablante activo y aplicarle la generación

​

options.active_speaker_detection.bounding_boxes

integer[][]

Array por fotograma de cuadros delimitadores [x1, y1, x2, y2] para la cara detectada

​

options.active_speaker_detection.bounding_boxes_url

string

URL de un archivo JSON que contiene cuadros delimitadores

​

options.active_speaker_detection.coordinates

integer[]

Coordenadas de píxel [x, y] en el fotograma de video de origen identificado por frame_number

​

options.active_speaker_detection.frame_number

integer

Índice de fotograma que corresponde a las coordenadas proporcionadas para la selección manual del hablante

​

options.active_speaker_detection.v3

boolean

Indica si se debe usar ASD v3

​

options.model_mode

string

Región de edición para el modelo (labios, cara, cabeza); solo funciona con react-1

​

options.occlusion_detection_enabled

boolean

Indica si se debe detectar oclusión durante la generación

​

options.prompt

string

Prompt de emoción; solo funciona con react-1

​

options.sync_mode

string

Cómo manejar los desajustes de duración entre video y audio (bounce, loop, cut_off, silence, remap)

​

options.temperature

number

Qué tan expresiva puede ser la sincronización labial, de 0 a 1Formato: `double`

​

outputDuration

number

La duración del medio de salida en segundosFormato: `double`

​

outputFileName

string

El nombre de archivo saneado aplicado al medio de salida

​

outputUrl

string

La URL del medio de salida

​

projectId

string

El ID del proyecto al que está asociada esta generación

​

segmentOutputUrl

string

La URL del medio de salida del segmento

​

segments

object[]

Los segmentos de la generación

​

segments[].audioInput

object

requerido

Configuración de entrada de audio para un segmento específico

​

segments[].audioInput.endTime

number

Tiempo de finalización opcional en segundos para recortar el audio de referenciaFormato: `double`

​

segments[].audioInput.refId

string

requerido

ID de referencia de la entrada de audio/texto a voz que se usará para este segmento

​

segments[].audioInput.startTime

number

Tiempo de inicio opcional en segundos para recortar el audio de referenciaFormato: `double`

​

segments[].endTime

number

requerido

Tiempo de finalización del segmento en segundosFormato: `double`

​

segments[].optionsOverride

object

Sobrescribir las opciones de generación para un segmento específico

​

segments[].optionsOverride.active_speaker_detection

object

Configuración de detección del hablante activo

​

segments[].optionsOverride.active_speaker_detection.auto_detect

boolean

Indica si se debe detectar y aplicar automáticamente la generación al hablante activo

​

segments[].optionsOverride.active_speaker_detection.bounding_boxes

integer[][]

Arreglo por fotograma de cuadros delimitadores [x1, y1, x2, y2] para el rostro detectado

​

segments[].optionsOverride.active_speaker_detection.bounding_boxes_url

string

URL de un archivo JSON que contiene los cuadros delimitadores

​

segments[].optionsOverride.active_speaker_detection.coordinates

integer[]

Coordenadas en píxeles [x, y] en el fotograma del video de origen identificado por frame_number

​

segments[].optionsOverride.active_speaker_detection.frame_number

integer

Índice de fotograma que corresponde a las coordenadas proporcionadas para la selección manual del hablante

​

segments[].optionsOverride.active_speaker_detection.v3

boolean

Indica si se debe usar ASD v3

​

segments[].optionsOverride.occlusion_detection_enabled

boolean

Sobrescribe la detección de oclusión para este segmento

​

segments[].optionsOverride.sync_mode

string

Sobrescribe el modo de sincronización para este segmento

​

segments[].optionsOverride.temperature

number

Sobrescribe la temperatura (0-1) para este segmentoFormato: `double`

​

segments[].startTime

number

requerido

Tiempo de inicio del segmento en segundosFormato: `double`

​

status

string

El estado de la generación (PENDING, PROCESSING, COMPLETED, FAILED, REJECTED)

​

synthesizedAudioUrl

string

La URL del audio sintetizado a partir de una entrada de texto (TTS)

​

webhookUrl

string

La URL del endpoint del webhook

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input": [
        {
          "type": "video",
          "url": "https://example.invalid/synclabs/sync-3/speaker.mp4"
        },
        {
          "type": "audio",
          "url": "https://example.invalid/synclabs/sync-3/voiceover.wav"
        }
      ],
      "options": {
        "sync_mode": "bounce"
      }
    }
    

### 

​

Salida
    
    
    {
      "createdAt": "2026-01-01T00:00:00.000Z",
      "id": "9a3d0c1e-0000-4000-8000-000000000000",
      "model": "sync-3",
      "outputDuration": 4.25,
      "outputFileName": "lipsync",
      "outputUrl": "https://example.invalid/synclabs/sync-3/output.mp4",
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/synclabs/sync-3/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/synclabs/sync-3/code)

[Gen 4 Turbo](https://docs.comfy.org/es/development/comfy-router/models/runway/gen4-turbo/code)[Hunyuan 3D Part](https://docs.comfy.org/es/development/comfy-router/models/tencent/hunyuan-3d-part/code)
