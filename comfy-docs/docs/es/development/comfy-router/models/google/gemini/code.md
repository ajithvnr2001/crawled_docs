---
url: https://docs.comfy.org/es/development/comfy-router/models/google/gemini/code/
title: Usa Google Gemini con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:45.691078+00:00
---

# Usa Google Gemini con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/google/gemini/code/

## En esta página

Volver arriba

  * Inicio rápido
  * Antes de lanzar



Google

# Usa Google Gemini con Comfy Router

Copiar páginaCopiar página

Fragmentos de Python, TypeScript y cURL para llamar a modelos de texto de Google Gemini por HTTP con Comfy Router; campos de solicitud y forma del resultado.

Copiar páginaCopiar página

Referencia de API de Google Gemini. Google Gemini es la familia de modelos de texto multimodales de Google: abarca desde la redacción rápida hasta el razonamiento profundo en los niveles Flash y Pro.

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. Elige el modelo que quieres invocar. Todo lo que aparece a continuación, desde los fragmentos hasta el esquema y los ejemplos, depende de tu elección.

  * Gemini 3.1 Pro

  * Gemini 3.5 Flash

  * Gemini 2.5 Pro

  * Gemini 2.5 Flash




**ID del modelo:** `vertexai/gemini-3.1-pro-preview`**Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview`

  * Esperar el resultado

  * Encolar y recoger más tarde




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
                "vertexai/gemini-3.1-pro-preview",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-3.1-pro-preview", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge una vez que está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "vertexai/gemini-3.1-pro-preview",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-3.1-pro-preview", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

contents

object[]

requerido

El contenido de la conversación actual con el modelo. Para consultas de un solo turno, es una única instancia. Para consultas de varios turnos, es un campo repetido que contiene el historial de la conversación y la solicitud más reciente.

​

contents[].parts

object[]

requerido

​

contents[].parts[].fileData

object

Datos basados en URI.

​

contents[].parts[].fileData.fileUri

string

URI

​

contents[].parts[].fileData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de las imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

contents[].parts[].inlineData

object

Datos en línea en bytes sin procesar. Para gemini-2.0-flash-lite y gemini-2.0-flash, puedes especificar hasta 3000 imágenes usando inlineData.

​

contents[].parts[].inlineData.data

string (byte)

La codificación base64 de la imagen, el PDF o el video que se incluye en línea en el prompt. Cuando incluyes medios en línea, también debes especificar el tipo de medio (mimeType) de los datos. Límite de tamaño: 20MBFormato: `byte`

​

contents[].parts[].inlineData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para obtener más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de las imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

contents[].parts[].mediaProcessing

string

Cómo lee el modelo el video de esta parte. Establece “AGENTIC” para que el modelo decida qué segmentos inspeccionar, en lugar del muestreo de fotogramas a tasa fija. Omítelo para usar el muestreo de tasa fija predeterminado. Compatible con gemini-3.7-flash y modelos Flash más recientes.

​

contents[].parts[].text

string

Un prompt de texto o fragmento de código.

​

contents[].parts[].thought

boolean

Indica que esta parte es un paso de pensamiento o razonamiento del modelo.

​

contents[].role

string

Valores posibles: `user`, `model`

​

generationConfig

object

Configuraciones de muestreo, longitud y salida para la generación. Todos los campos son opcionales: los campos a continuación que declaran un `default` lo aplican cuando se omiten, y el resto recurre al comportamiento propio del modelo.

​

generationConfig.imageConfig

object

Configuración para la generación de imágenes

​

generationConfig.imageConfig.aspectRatio

string

Relación de aspecto de las imágenes generadas

​

generationConfig.imageConfig.imageOutputOptions

object

Opcional. El formato de salida de imagen para las imágenes generadas.

​

generationConfig.imageConfig.imageOutputOptions.compressionQuality

integer

Opcional. La calidad de compresión de la imagen de salida.

​

generationConfig.imageConfig.imageOutputOptions.mimeType

string

Opcional. El formato de imagen con el que se debe guardar la salida, en las rutas de Vertex AI: solicitudes atendidas por las credenciales propias de Comfy y solicitudes BYOK autenticadas con una cuenta de servicio de GCP. Los valores aceptados allí son `image/png` y `image/jpeg`, se comparan sin distinguir mayúsculas y minúsculas y se normalizan a minúsculas antes de reenviar la solicitud; cualquier otro valor se rechaza con un 400 que nombra este campo. Si se omite, el valor predeterminado es `image/png`. Una solicitud BYOK autenticada con una clave API de Google AI Studio es la excepción: ese upstream no tiene tal propiedad y rechaza toda la llamada si está presente, así que el campo se elimina de la solicitud en lugar de respetarse o rechazarse, y el formato de salida es el que elija AI Studio. En todas las rutas, lee el tipo de medio desde la parte de la respuesta que recibes (`inlineData.mimeType`, o `fileData.mimeType` cuando `uploadImagesToStorage` está establecido) en lugar de suponer el valor que enviaste.

​

generationConfig.imageConfig.imageSize

string

Opcional. Especifica el tamaño de las imágenes generadas. Los valores admitidos son 1K, 2K, 4K. Si no se especifica, el modelo usará el valor predeterminado 1K.

​

generationConfig.maxOutputTokens

integer

Número máximo de tokens que se pueden generar en la respuesta. Un token es aproximadamente 4 caracteres. 100 tokens corresponden a unas 60-80 palabras.Alcance: `16` a `65536`

​

generationConfig.responseModalities

`TEXT`, `IMAGE`[]

​

generationConfig.seed

integer

Cuando la semilla se fija a un valor específico, el modelo hace su mejor esfuerzo para dar la misma respuesta en solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o las configuraciones de los parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando usas el mismo valor de semilla. De forma predeterminada, se usa un valor de semilla aleatorio. Disponible para los siguientes modelos: gemini-2.5-flash, gemini-2.5-pro, gemini-2.5-flash-preview-04-1, gemini-2.5-pro-preview-05-0, gemini-2.0-flash-lite-00, gemini-2.0-flash-001

​

generationConfig.stopSequences

string[]

​

generationConfig.temperature

number

predeterminado:"1"

La temperatura se usa para el muestreo durante la generación de la respuesta, que ocurre cuando se aplican topP y topK. La temperatura controla el grado de aleatoriedad en la selección de tokens. Las temperaturas más bajas son buenas para prompts que requieren una respuesta menos abierta o creativa, mientras que las temperaturas más altas pueden dar lugar a resultados más diversos o creativos. Una temperatura de 0 significa que siempre se seleccionan los tokens de mayor probabilidad. En este caso, las respuestas para un prompt dado son en su mayoría deterministas, pero aún es posible una pequeña cantidad de variación. Si el modelo devuelve una respuesta demasiado genérica, demasiado corta, o el modelo da una respuesta de respaldo, intenta aumentar la temperaturaAlcance: `0` a `2`Formato: `float`

​

generationConfig.thinkingConfig

object

Opcional. Configuración para las funciones de pensamiento. El pensamiento es un proceso en el que el modelo descompone una tarea compleja en pasos más pequeños para generar una respuesta de mayor calidad.

​

generationConfig.thinkingConfig.includeThoughts

boolean

Opcional. Si es verdadero, el modelo incluirá sus razonamientos en la respuesta.

​

generationConfig.thinkingConfig.thinkingBudget

integer

Opcional. El presupuesto de tokens para el proceso de razonamiento del modelo. El modelo hará su mejor esfuerzo por mantenerse dentro de este presupuesto.

​

generationConfig.thinkingConfig.thinkingLevel

string

Opcional. El nivel de razonamiento del modelo.Valores posibles: `THINKING_LEVEL_UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH`, `MINIMAL`

​

generationConfig.topK

integer

predeterminado:"40"

Top-K cambia cómo el modelo selecciona los tokens de salida. Un top-K de 1 significa que el siguiente token seleccionado es el más probable entre todos los tokens del vocabulario del modelo. Un top-K de 3 significa que el siguiente token se selecciona entre los 3 tokens más probables usando la temperatura.Alcance: `1` a `…`

​

generationConfig.topP

number

predeterminado:"0.95"

Si se especifica, se usa el muestreo de núcleo. Top-P cambia cómo el modelo selecciona los tokens de salida. Los tokens se seleccionan desde los más probables (consulta top-K) hasta los menos probables, hasta que la suma de sus probabilidades sea igual al valor de top-P. Por ejemplo, si los tokens A, B y C tienen una probabilidad de 0.3, 0.2 y 0.1 y el valor de top-P es 0.5, el modelo seleccionará A o B como siguiente token usando la temperatura y excluirá C como candidato. Especifica un valor más bajo para respuestas menos aleatorias y un valor más alto para respuestas más aleatorias.Alcance: `0` a `1`Formato: `float`

​

safetySettings

object[]

Configuraciones por solicitud para bloquear contenido no seguro. Se aplican en GenerateContentResponse.candidates.

​

safetySettings[].category

string

requerido

Valores posibles: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

safetySettings[].threshold

string

requerido

Valores posibles: `OFF`, `BLOCK_NONE`, `BLOCK_LOW_AND_ABOVE`, `BLOCK_MEDIUM_AND_ABOVE`, `BLOCK_ONLY_HIGH`

​

systemInstruction

object

Instrucciones para orientar al modelo hacia un mejor rendimiento. Por ejemplo, “Responde de la forma más concisa posible” o “No uses términos técnicos en tu respuesta”. Las cadenas de texto cuentan para el límite de tokens. El campo role de systemInstruction se ignora y no afecta el rendimiento del modelo. Nota: Solo se debe usar texto en parts y el contenido de cada part debe estar en un párrafo separado.

​

systemInstruction.parts

object[]

requerido

Una lista de parts ordenadas que componen un solo mensaje. Diferentes parts pueden tener diferentes tipos MIME de IANA. Para conocer los límites de las entradas, como la cantidad máxima de tokens o la cantidad de imágenes, consulta las especificaciones del modelo en la página de modelos de Google.

​

systemInstruction.parts[].text

string

Un prompt de texto o un fragmento de código.

​

systemInstruction.role

string

La identidad de la entidad que crea el mensaje. Se admiten los siguientes valores: user: indica que el mensaje lo envía una persona real, normalmente un mensaje generado por el usuario. model: indica que el mensaje lo genera el modelo. El valor model se usa para insertar mensajes del modelo en la conversación durante conversaciones de varios turnos. En conversaciones de un solo turno, este campo puede dejarse en blanco o sin establecer.Valores posibles: `user`, `model`

​

tools

object[]

Un fragmento de código que permite al sistema interactuar con sistemas externos para realizar una acción o un conjunto de acciones fuera del conocimiento y el alcance del modelo. Consulta Llamada a funciones.

​

tools[].functionDeclarations

object[]

​

tools[].functionDeclarations[].description

string

​

tools[].functionDeclarations[].name

string

requerido

​

tools[].functionDeclarations[].parameters

object

Esquema JSON para los parámetros de la función

​

uploadImagesToStorage

boolean

Si es verdadero, las imágenes generadas se subirán al almacenamiento en la nube y se devolverán como URL firmadas en lugar de datos base64 insertados. Las URL vencen después de 24 horas.

​

videoMetadata

object

Para entradas de video, el desplazamiento de inicio y fin del video en formato Duration. Por ejemplo, para especificar un clip de 10 segundos que comienza en 1:00, establece “startOffset”: { “seconds”: 60 } y “endOffset”: { “seconds”: 70 }. Los metadatos solo deben especificarse mientras los datos del video se presentan en inlineData o fileData.

​

videoMetadata.endOffset

object

Representa un desplazamiento de duración para posiciones en la línea de tiempo de un video.

​

videoMetadata.endOffset.nanos

integer

Fracciones de segundo con signo y resolución de nanosegundos. Los valores negativos de segundos con fracciones deben tener valores de nanos no negativos.Alcance: `0` a `999999999`

​

videoMetadata.endOffset.seconds

integer

Segundos con signo del intervalo de tiempo. Debe estar entre -315,576,000,000 y +315,576,000,000 inclusive.Alcance: `-315576000000` a `315576000000`

​

videoMetadata.startOffset

object

Representa un desplazamiento de duración para posiciones en la línea de tiempo de un video.

​

videoMetadata.startOffset.nanos

integer

Fracciones de segundo con signo y resolución de nanosegundos. Los valores negativos de segundos con fracciones deben tener valores de nanos no negativos.Alcance: `0` a `999999999`

​

videoMetadata.startOffset.seconds

integer

Segundos con signo del intervalo de tiempo. Debe estar entre -315,576,000,000 y +315,576,000,000, ambos incluidos.Alcance: `-315576000000` a `315576000000`

Generado a partir del esquema que Router publica en `GET /v2/models/vertexai/gemini-3.1-pro-preview/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

candidates

object[]

​

candidates[].citationMetadata

object

​

candidates[].citationMetadata.citations

object[]

​

candidates[].citationMetadata.citations[].authors

string[]

​

candidates[].citationMetadata.citations[].endIndex

integer

​

candidates[].citationMetadata.citations[].license

string

​

candidates[].citationMetadata.citations[].publicationDate

string (date)

Formato: `date`

​

candidates[].citationMetadata.citations[].startIndex

integer

​

candidates[].citationMetadata.citations[].title

string

​

candidates[].citationMetadata.citations[].uri

string

​

candidates[].content

object

El contenido de la conversación actual con el modelo. En consultas de un solo turno, es una única instancia. En consultas de varios turnos, es un campo repetido que contiene el historial de la conversación y la última solicitud.

​

candidates[].content.parts

object[]

requerido

​

candidates[].content.parts[].fileData

object

Datos basados en URI.

​

candidates[].content.parts[].fileData.fileUri

string

URI

​

candidates[].content.parts[].fileData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de las imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

candidates[].content.parts[].inlineData

object

Datos en línea en bytes sin procesar. Para gemini-2.0-flash-lite y gemini-2.0-flash, puedes especificar hasta 3000 imágenes usando inlineData.

​

candidates[].content.parts[].inlineData.data

string (byte)

La codificación base64 de la imagen, el PDF o el video que quieres incluir en línea en el prompt. Cuando incluyes medios en línea, también debes especificar el tipo de medio (mimeType) de los datos. Límite de tamaño: 20MBFormato: `byte`

​

candidates[].content.parts[].inlineData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de las imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

candidates[].content.parts[].mediaProcessing

string

Cómo lee el modelo el video de esta parte. Configura “AGENTIC” para que el modelo decida qué segmentos inspeccionar, en lugar del muestreo de fotogramas a tasa fija. Omítelo para usar el muestreo de tasa fija predeterminado. Compatible con gemini-3.7-flash y los modelos Flash más recientes.

​

candidates[].content.parts[].text

string

Un prompt de texto o un fragmento de código.

​

candidates[].content.parts[].thought

boolean

Indica que esta parte es un paso de pensamiento o razonamiento del modelo.

​

candidates[].content.role

string

Valores posibles: `user`, `model`

​

candidates[].finishReason

string

​

candidates[].safetyRatings

object[]

​

candidates[].safetyRatings[].category

string

Valores posibles: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

candidates[].safetyRatings[].probability

string

La probabilidad de que el contenido infrinja la categoría de seguridad especificadaValores posibles: `NEGLIGIBLE`, `LOW`, `MEDIUM`, `HIGH`, `UNKNOWN`

​

createTime

string

Marca de tiempo de cuándo se creó la respuesta.

​

modelVersion

string

La versión del modelo usada para generar la respuesta.

​

promptFeedback

object

​

promptFeedback.blockReason

string

​

promptFeedback.blockReasonMessage

string

​

promptFeedback.safetyRatings

object[]

​

promptFeedback.safetyRatings[].category

string

Valores posibles: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

promptFeedback.safetyRatings[].probability

string

La probabilidad de que el contenido infrinja la categoría de seguridad especificadaValores posibles: `NEGLIGIBLE`, `LOW`, `MEDIUM`, `HIGH`, `UNKNOWN`

​

responseId

string

Identificador único de la respuesta.

​

usageMetadata

object

​

usageMetadata.cachedContentTokenCount

integer

Solo salida. Número de tokens en la parte en caché de la entrada (el contenido en caché).

​

usageMetadata.candidatesTokenCount

integer

Número de tokens en la(s) respuesta(s).

​

usageMetadata.candidatesTokensDetails

object[]

Desglose de los tokens de candidatos por modalidad.

​

usageMetadata.candidatesTokensDetails[].modality

string

Tipo de modalidad del contenido de entrada o salida.Valores posibles: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.candidatesTokensDetails[].tokenCount

integer

Número de tokens de la modalidad indicada.

​

usageMetadata.promptTokenCount

integer

Número de tokens de la solicitud. Cuando se establece cachedContent, este sigue siendo el tamaño total efectivo del prompt, lo que significa que incluye el número de tokens del contenido en caché.

​

usageMetadata.promptTokensDetails

object[]

Desglose de los tokens del prompt por modalidad.

​

usageMetadata.promptTokensDetails[].modality

string

Tipo de modalidad del contenido de entrada o salida.Valores posibles: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.promptTokensDetails[].tokenCount

integer

Número de tokens de la modalidad indicada.

​

usageMetadata.thoughtsTokenCount

integer

Número de tokens presentes en la salida de pensamientos.

​

usageMetadata.toolUsePromptTokenCount

integer

Número de tokens presentes en los prompts de uso de herramientas.

​

usageMetadata.toolUsePromptTokensDetails

object[]

Desglose de los tokens del prompt de uso de herramientas por modalidad.

​

usageMetadata.toolUsePromptTokensDetails[].modality

string

Tipo de modalidad del contenido de entrada o salida.Valores posibles: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.toolUsePromptTokensDetails[].tokenCount

integer

Número de tokens de la modalidad indicada.

​

usageMetadata.totalTokenCount

integer

Número total de tokens (prompt + candidatos).

​

usageMetadata.trafficType

string

Tipo de tráfico usado para la solicitud (p. ej., PROVISIONED_THROUGHPUT).

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "text": "Describe a single red maple leaf on a white background in one sentence."
            }
          ]
        }
      ],
      "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 256
      }
    }
    

### 

​

Salida
    
    
    {
      "candidates": [
        {
          "content": {
            "role": "model",
            "parts": [
              {
                "text": "A single red maple leaf rests on a plain white background, its edges sharp and its color deep."
              }
            ]
          },
          "finishReason": "STOP"
        }
      ],
      "usageMetadata": {
        "promptTokenCount": 18,
        "candidatesTokenCount": 24
      }
    }
    

**ID del modelo:** `vertexai/gemini-3.5-flash`**Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash`

  * Esperar el resultado

  * Enviar a la cola y recoger más tarde




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
                "vertexai/gemini-3.5-flash",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-3.5-flash", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "vertexai/gemini-3.5-flash",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-3.5-flash", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

contents

object[]

requerido

El contenido de la conversación actual con el modelo. Para consultas de un solo turno, es una sola instancia. Para consultas de varios turnos, es un campo repetido que contiene el historial de la conversación y la solicitud más reciente.

​

contents[].parts

object[]

requerido

​

contents[].parts[].fileData

object

Datos basados en URI.

​

contents[].parts[].fileData.fileUri

string

URI

​

contents[].parts[].fileData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para obtener más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de las imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

contents[].parts[].inlineData

object

Datos en línea en bytes sin procesar. Para gemini-2.0-flash-lite y gemini-2.0-flash, puedes especificar hasta 3000 imágenes mediante inlineData.

​

contents[].parts[].inlineData.data

string (byte)

La codificación base64 de la imagen, el PDF o el video para incluir en línea en el prompt. Cuando incluyes contenido multimedia en línea, también debes especificar el tipo de medio (mimeType) de los datos. Límite de tamaño: 20MBFormato: `byte`

​

contents[].parts[].inlineData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para obtener más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

contents[].parts[].mediaProcessing

string

Cómo lee el modelo el video de esta parte. Establece “AGENTIC” para permitir que el modelo decida qué segmentos inspeccionar, en lugar del muestreo de fotogramas a tasa fija. Omítelo para usar el muestreo a tasa fija predeterminado. Compatible con gemini-3.7-flash y los modelos Flash más recientes.

​

contents[].parts[].text

string

Un prompt de texto o fragmento de código.

​

contents[].parts[].thought

boolean

Indica que esta parte es un paso de pensamiento/razonamiento del modelo.

​

contents[].role

string

Valores posibles: `user`, `model`

​

generationConfig

object

Configuraciones de muestreo, longitud y salida para la generación. Todos los campos son opcionales: los campos siguientes que declaran un `default` lo aplican cuando se omiten, y el resto recurre al comportamiento propio del modelo.

​

generationConfig.imageConfig

object

Configuración para la generación de imágenes

​

generationConfig.imageConfig.aspectRatio

string

Relación de aspecto de las imágenes generadas

​

generationConfig.imageConfig.imageOutputOptions

object

Opcional. El formato de salida de las imágenes generadas.

​

generationConfig.imageConfig.imageOutputOptions.compressionQuality

integer

Opcional. La calidad de compresión de la imagen de salida.

​

generationConfig.imageConfig.imageOutputOptions.mimeType

string

Opcional. El formato de imagen con el que se debe guardar la salida, en las rutas de Vertex AI: las solicitudes atendidas por las credenciales propias de Comfy y las solicitudes BYOK autenticadas con una cuenta de servicio de GCP. Los valores aceptados allí son `image/png` y `image/jpeg`, que se comparan sin distinguir mayúsculas de minúsculas y se normalizan a minúsculas antes de reenviar la solicitud; cualquier otro valor se rechaza con un error 400 que menciona este campo. Si se omite, el valor predeterminado es `image/png`. La excepción es una solicitud BYOK autenticada con una clave API de Google AI Studio: ese servicio upstream no tiene tal propiedad y rechaza toda la llamada si está presente, por lo que el campo se descarta de la solicitud en lugar de respetarse o rechazarse, y el formato de salida es el que elija AI Studio. En todas las rutas, lee el tipo de medio desde la parte de la respuesta que recibes (`inlineData.mimeType`, o `fileData.mimeType` cuando `uploadImagesToStorage` está configurado) en lugar de asumir el valor que enviaste.

​

generationConfig.imageConfig.imageSize

string

Opcional. Especifica el tamaño de las imágenes generadas. Los valores admitidos son 1K, 2K, 4K. Si no se especifica, el modelo usará el valor predeterminado 1K.

​

generationConfig.maxOutputTokens

integer

Número máximo de tokens que se pueden generar en la respuesta. Un token equivale aproximadamente a 4 caracteres. 100 tokens corresponden a aproximadamente 60-80 palabras.Alcance: `16` a `65536`

​

generationConfig.responseModalities

`TEXT`, `IMAGE`[]

​

generationConfig.seed

integer

Cuando la semilla se fija a un valor específico, el modelo hace su mejor esfuerzo para proporcionar la misma respuesta en solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o las configuraciones de parámetros, como la temperatura, puede provocar variaciones en la respuesta incluso cuando usas el mismo valor de semilla. De forma predeterminada, se usa un valor de semilla aleatorio. Disponible para los siguientes modelos: gemini-2.5-flash, gemini-2.5-pro, gemini-2.5-flash-preview-04-1, gemini-2.5-pro-preview-05-0, gemini-2.0-flash-lite-00, gemini-2.0-flash-001

​

generationConfig.stopSequences

string[]

​

generationConfig.temperature

number

predeterminado:"1"

La temperatura se usa para el muestreo durante la generación de la respuesta, que ocurre cuando se aplican topP y topK. La temperatura controla el grado de aleatoriedad en la selección de tokens. Las temperaturas más bajas son buenas para prompts que requieren una respuesta menos abierta o creativa, mientras que las temperaturas más altas pueden dar lugar a resultados más diversos o creativos. Una temperatura de 0 significa que siempre se seleccionan los tokens con mayor probabilidad. En este caso, las respuestas para un prompt dado son en su mayoría deterministas, pero todavía es posible una pequeña cantidad de variación. Si el modelo devuelve una respuesta demasiado genérica, demasiado corta, o el modelo da una respuesta de respaldo, prueba aumentar la temperaturaAlcance: `0` a `2`Formato: `float`

​

generationConfig.thinkingConfig

object

Opcional. Configuración para las funciones de razonamiento. El razonamiento es un proceso en el que el modelo descompone una tarea compleja en pasos más pequeños para generar una respuesta de mayor calidad.

​

generationConfig.thinkingConfig.includeThoughts

boolean

Opcional. Si es verdadero, el modelo incluirá sus razonamientos en la respuesta.

​

generationConfig.thinkingConfig.thinkingBudget

integer

Opcional. El presupuesto de tokens para el proceso de razonamiento del modelo. El modelo hará su mejor esfuerzo por mantenerse dentro de este presupuesto.

​

generationConfig.thinkingConfig.thinkingLevel

string

Opcional. El nivel de razonamiento del modelo.Valores posibles: `THINKING_LEVEL_UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH`, `MINIMAL`

​

generationConfig.topK

integer

predeterminado:"40"

Top-K cambia la forma en que el modelo selecciona los tokens para su salida. Un top-K de 1 significa que el siguiente token seleccionado es el más probable entre todos los tokens del vocabulario del modelo. Un top-K de 3 significa que el siguiente token se selecciona entre los 3 tokens más probables usando la temperatura.Alcance: `1` a `…`

​

generationConfig.topP

number

predeterminado:"0.95"

Si se especifica, se usa el muestreo de núcleo. Top-P cambia la forma en que el modelo selecciona los tokens para su salida. Los tokens se seleccionan del más (ver top-K) al menos probable hasta que la suma de sus probabilidades sea igual al valor de top-P. Por ejemplo, si los tokens A, B y C tienen una probabilidad de 0.3, 0.2 y 0.1 y el valor de top-P es 0.5, entonces el modelo seleccionará A o B como el siguiente token usando la temperatura y excluirá a C como candidato. Especifica un valor más bajo para respuestas menos aleatorias y un valor más alto para respuestas más aleatorias.Alcance: `0` a `1`Formato: `float`

​

safetySettings

object[]

Configuraciones por solicitud para bloquear contenido inseguro. Se aplican a GenerateContentResponse.candidates.

​

safetySettings[].category

string

requerido

Valores posibles: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

safetySettings[].threshold

string

requerido

Valores posibles: `OFF`, `BLOCK_NONE`, `BLOCK_LOW_AND_ABOVE`, `BLOCK_MEDIUM_AND_ABOVE`, `BLOCK_ONLY_HIGH`

​

systemInstruction

object

Instrucciones para el modelo que lo orientan hacia un mejor rendimiento. Por ejemplo, “Responde de la forma más concisa posible” o “No uses términos técnicos en tu respuesta”. Las cadenas de texto cuentan para el límite de tokens. El campo role de systemInstruction se ignora y no afecta el rendimiento del modelo. Nota: Solo se debe usar texto en parts y el contenido de cada part debe estar en un párrafo separado.

​

systemInstruction.parts

object[]

requerido

Una lista de parts ordenados que componen un solo mensaje. Diferentes parts pueden tener diferentes tipos MIME de IANA. Para conocer los límites de las entradas, como el número máximo de tokens o el número de imágenes, consulta las especificaciones del modelo en la página de modelos de Google.

​

systemInstruction.parts[].text

string

Un prompt de texto o fragmento de código.

​

systemInstruction.role

string

La identidad de la entidad que crea el mensaje. Se admiten los siguientes valores: user: Indica que el mensaje lo envía una persona real, típicamente un mensaje generado por el usuario. model: Indica que el mensaje lo genera el modelo. El valor model se usa para insertar mensajes del modelo en la conversación durante conversaciones de varios turnos. Para conversaciones de un solo turno, este campo puede dejarse en blanco o sin establecer.Valores posibles: `user`, `model`

​

tools

object[]

Un fragmento de código que permite al sistema interactuar con sistemas externos para realizar una acción, o un conjunto de acciones, fuera del conocimiento y el alcance del modelo. Consulta Llamada a funciones.

​

tools[].functionDeclarations

object[]

​

tools[].functionDeclarations[].description

string

​

tools[].functionDeclarations[].name

string

requerido

​

tools[].functionDeclarations[].parameters

object

Esquema JSON para los parámetros de la función

​

uploadImagesToStorage

boolean

Si es verdadero, las imágenes generadas se subirán al almacenamiento en la nube y se devolverán como URLs firmadas en lugar de datos base64 en línea. Las URLs vencen después de 24 horas.

​

videoMetadata

object

Para entradas de video, el desplazamiento de inicio y fin del video en formato Duration. Por ejemplo, para especificar un clip de 10 segundos que comienza en 1:00, establece “startOffset”: { “seconds”: 60 } y “endOffset”: { “seconds”: 70 }. Los metadatos solo deben especificarse mientras los datos del video se presenten en inlineData o fileData.

​

videoMetadata.endOffset

object

Representa un desplazamiento de duración para las posiciones de la línea de tiempo del video.

​

videoMetadata.endOffset.nanos

integer

Fracciones de segundo con signo y resolución de nanosegundos. Los valores de segundos negativos con fracciones deben seguir teniendo valores de nanos no negativos.Alcance: `0` a `999999999`

​

videoMetadata.endOffset.seconds

integer

Segundos con signo del intervalo de tiempo. Debe estar entre -315,576,000,000 y +315,576,000,000 inclusive.Alcance: `-315576000000` a `315576000000`

​

videoMetadata.startOffset

object

Representa un desplazamiento de duración para las posiciones de la línea de tiempo del video.

​

videoMetadata.startOffset.nanos

integer

Fracciones de segundo con signo y resolución de nanosegundos. Los valores negativos de segundos con fracciones deben seguir teniendo valores de nanos no negativos.Alcance: `0` a `999999999`

​

videoMetadata.startOffset.seconds

integer

Segundos con signo del intervalo de tiempo. Debe estar entre -315,576,000,000 y +315,576,000,000 inclusive.Alcance: `-315576000000` a `315576000000`

Generado a partir del esquema que Router sirve en `GET /v2/models/vertexai/gemini-3.5-flash/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

candidates

object[]

​

candidates[].citationMetadata

object

​

candidates[].citationMetadata.citations

object[]

​

candidates[].citationMetadata.citations[].authors

string[]

​

candidates[].citationMetadata.citations[].endIndex

integer

​

candidates[].citationMetadata.citations[].license

string

​

candidates[].citationMetadata.citations[].publicationDate

string (date)

Formato: `date`

​

candidates[].citationMetadata.citations[].startIndex

integer

​

candidates[].citationMetadata.citations[].title

string

​

candidates[].citationMetadata.citations[].uri

string

​

candidates[].content

object

El contenido de la conversación actual con el modelo. Para consultas de un solo turno, es una instancia única. Para consultas de varios turnos, es un campo repetido que contiene el historial de la conversación y la última solicitud.

​

candidates[].content.parts

object[]

requerido

​

candidates[].content.parts[].fileData

object

Datos basados en URI.

​

candidates[].content.parts[].fileData.fileUri

string

URI

​

candidates[].content.parts[].fileData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de las imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

candidates[].content.parts[].inlineData

object

Datos en línea en bytes sin procesar. Para gemini-2.0-flash-lite y gemini-2.0-flash, puedes especificar hasta 3000 imágenes usando inlineData.

​

candidates[].content.parts[].inlineData.data

string (byte)

La codificación base64 de la imagen, PDF o video que se incluirá en línea en el prompt. Cuando incluyas medios en línea, también debes especificar el tipo de medio (mimeType) de los datos. Límite de tamaño: 20MBFormato: `byte`

​

candidates[].content.parts[].inlineData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de las imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

candidates[].content.parts[].mediaProcessing

string

Cómo lee el modelo el video de esta parte. Establece “AGENTIC” para que el modelo decida qué segmentos inspeccionar, en lugar del muestreo de fotogramas a tasa fija. Omítelo para usar el muestreo a tasa fija predeterminado. Compatible con gemini-3.7-flash y modelos Flash más recientes.

​

candidates[].content.parts[].text

string

Un prompt de texto o fragmento de código.

​

candidates[].content.parts[].thought

boolean

Indica que esta parte es un paso de pensamiento/razonamiento del modelo.

​

candidates[].content.role

string

Valores posibles: `user`, `model`

​

candidates[].finishReason

string

​

candidates[].safetyRatings

object[]

​

candidates[].safetyRatings[].category

string

Valores posibles: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

candidates[].safetyRatings[].probability

string

La probabilidad de que el contenido infrinja la categoría de seguridad especificadaValores posibles: `NEGLIGIBLE`, `LOW`, `MEDIUM`, `HIGH`, `UNKNOWN`

​

createTime

string

Marca de tiempo de cuándo se creó la respuesta.

​

modelVersion

string

La versión del modelo que se usó para generar la respuesta.

​

promptFeedback

object

​

promptFeedback.blockReason

string

​

promptFeedback.blockReasonMessage

string

​

promptFeedback.safetyRatings

object[]

​

promptFeedback.safetyRatings[].category

string

Valores posibles: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

promptFeedback.safetyRatings[].probability

string

La probabilidad de que el contenido infrinja la categoría de seguridad especificadaValores posibles: `NEGLIGIBLE`, `LOW`, `MEDIUM`, `HIGH`, `UNKNOWN`

​

responseId

string

Identificador único de la respuesta.

​

usageMetadata

object

​

usageMetadata.cachedContentTokenCount

integer

Solo salida. Cantidad de tokens en la parte en caché de la entrada (el contenido en caché).

​

usageMetadata.candidatesTokenCount

integer

Cantidad de tokens en la respuesta o respuestas.

​

usageMetadata.candidatesTokensDetails

object[]

Desglose de los tokens de candidatos por modalidad.

​

usageMetadata.candidatesTokensDetails[].modality

string

Tipo de modalidad del contenido de entrada o de salida.Valores posibles: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.candidatesTokensDetails[].tokenCount

integer

Cantidad de tokens para la modalidad indicada.

​

usageMetadata.promptTokenCount

integer

Cantidad de tokens en la solicitud. Cuando se establece cachedContent, este sigue siendo el tamaño total efectivo del prompt, es decir, incluye la cantidad de tokens del contenido en caché.

​

usageMetadata.promptTokensDetails

object[]

Desglose de los tokens del prompt por modalidad.

​

usageMetadata.promptTokensDetails[].modality

string

Tipo de modalidad del contenido de entrada o de salida.Valores posibles: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.promptTokensDetails[].tokenCount

integer

Cantidad de tokens para la modalidad indicada.

​

usageMetadata.thoughtsTokenCount

integer

Cantidad de tokens presentes en la salida de pensamientos.

​

usageMetadata.toolUsePromptTokenCount

integer

Cantidad de tokens presentes en los prompts de uso de herramientas.

​

usageMetadata.toolUsePromptTokensDetails

object[]

Desglose de los tokens de los prompts de uso de herramientas por modalidad.

​

usageMetadata.toolUsePromptTokensDetails[].modality

string

Tipo de modalidad del contenido de entrada o de salida.Valores posibles: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.toolUsePromptTokensDetails[].tokenCount

integer

Cantidad de tokens para la modalidad indicada.

​

usageMetadata.totalTokenCount

integer

Cantidad total de tokens (prompt + candidatos).

​

usageMetadata.trafficType

string

Tipo de tráfico usado para la solicitud (p. ej., PROVISIONED_THROUGHPUT).

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "text": "Describe a single red maple leaf on a white background in one sentence."
            }
          ]
        }
      ],
      "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 256
      }
    }
    

### 

​

Salida
    
    
    {
      "candidates": [
        {
          "content": {
            "role": "model",
            "parts": [
              {
                "text": "A single red maple leaf rests on a plain white background, its edges sharp and its color deep."
              }
            ]
          },
          "finishReason": "STOP"
        }
      ],
      "usageMetadata": {
        "promptTokenCount": 18,
        "candidatesTokenCount": 24
      }
    }
    

**ID del modelo:** `vertexai/gemini-2.5-pro`**Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "vertexai/gemini-2.5-pro",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-2.5-pro", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Queued delivery](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "vertexai/gemini-2.5-pro",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-2.5-pro", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

 _Los campos siguen la especificación de API publicada por Google y se verifican contra ella en CI. El esquema propio de Router para este modelo aún no está publicado, así que las solicitudes se reenvían al proveedor sin validar._

​

contents

object[]

requerido

La conversación hasta ahora, con los turnos más antiguos primero. Una parte es `text`, o `inlineData` para enviar una imagen, audio o video junto con el prompt.

​

contents[].role

string

requerido

Quién escribió el turno.Valores posibles: `user`, `model`

​

contents[].parts

object[]

requerido

Las partes de contenido del turno.

​

contents[].parts[].text

string

Una parte de texto.

​

contents[].parts[].inlineData

object

Una parte de medios en línea.

​

contents[].parts[].inlineData.mimeType

string

Tipo de medio, por ejemplo `image/png`.

​

contents[].parts[].inlineData.data

string

Bytes del medio codificados en Base64.

​

systemInstruction

object

Prompt de sistema aplicado a toda la conversación.

​

systemInstruction.parts

object[]

​

systemInstruction.parts[].text

string

​

generationConfig

object

Configuraciones de muestreo y longitud.

​

generationConfig.temperature

number

Aleatoriedad del muestreo. Los valores predeterminados son específicos del modelo.Alcance: `0` a `2`

​

generationConfig.topP

number

Umbral de muestreo nucleus. Los valores predeterminados son específicos del modelo.

​

generationConfig.topK

integer

Corte de muestreo top-k. Los valores predeterminados son específicos del modelo.

​

generationConfig.maxOutputTokens

integer

Límite superior de tokens generados.

​

generationConfig.seed

integer

Semilla para un muestreo reproducible.

​

generationConfig.stopSequences

string[]

Cadenas que finalizan la generación cuando se producen.

​

generationConfig.thinkingConfig

object

Controles de esfuerzo de razonamiento en los modelos que lo admiten.

​

generationConfig.thinkingConfig.thinkingLevel

string

Valores posibles: `MINIMAL`, `LOW`, `MEDIUM`, `HIGH`

​

generationConfig.thinkingConfig.includeThoughts

boolean

Devuelve el razonamiento del modelo junto con la respuesta.

​

tools

object[]

Declaraciones de funciones que el modelo puede llamar.

​

tools[].functionDeclarations

object[]

​

tools[].functionDeclarations[].name

string

​

tools[].functionDeclarations[].description

string

​

tools[].functionDeclarations[].parameters

object

Esquema JSON para los argumentos de la función.

### 

​

Salida

El router devuelve la respuesta nativa de Google sin cambios. El texto está en `candidates[0].content.parts[0].text`.

​

candidates

object[]

Candidatos generados; uno, a menos que hayas solicitado más.

​

candidates[].content

object

​

candidates[].content.role

string

Valores posibles: `model`

​

candidates[].content.parts

object[]

​

candidates[].content.parts[].text

string

El texto generado.

​

candidates[].content.parts[].functionCall

object

Aparece cuando el modelo eligió llamar a una de tus `tools`.

​

candidates[].content.parts[].functionCall.name

string

​

candidates[].content.parts[].functionCall.args

object

​

candidates[].finishReason

string

Por qué se detuvo la generación: `STOP`, `MAX_TOKENS`, `SAFETY`, …

​

usageMetadata

object

Recuento de tokens de la llamada.

​

usageMetadata.promptTokenCount

integer

Tokens en el prompt.

​

usageMetadata.candidatesTokenCount

integer

Tokens en los candidatos generados.

​

promptFeedback

object

Aparece cuando el prompt en sí fue bloqueado. Comprueba si `candidates` está presente antes de leer el resultado; `usageMetadata` también puede aparecer en una respuesta bloqueada.

​

promptFeedback.blockReason

string

Por qué se bloqueó el prompt. No se devuelven candidatos; reformula el prompt y vuelve a intentarlo.Valores posibles: `SAFETY`, `OTHER`, `BLOCKLIST`, `PROHIBITED_CONTENT`, `IMAGE_SAFETY`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "text": "Describe a single red maple leaf on a white background in one sentence."
            }
          ]
        }
      ],
      "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 256
      }
    }
    

### 

​

Salida
    
    
    {
      "candidates": [
        {
          "content": {
            "role": "model",
            "parts": [
              {
                "text": "A single red maple leaf rests on a plain white background, its edges sharp and its color deep."
              }
            ]
          },
          "finishReason": "STOP"
        }
      ],
      "usageMetadata": {
        "promptTokenCount": 18,
        "candidatesTokenCount": 24
      }
    }
    

**ID del modelo:** `vertexai/gemini-2.5-flash`**Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash`

  * Esperar el resultado

  * Encolar y recoger más tarde




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
                "vertexai/gemini-2.5-flash",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-2.5-flash", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "vertexai/gemini-2.5-flash",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-2.5-flash", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras todavía se ejecuta.
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

 _Los campos siguen la especificación de API publicada por Google y se verifican contra ella en CI. El esquema propio de Router para este modelo aún no está publicado, así que las solicitudes se reenvían al proveedor sin validar._

​

contents

object[]

requerido

La conversación hasta ahora, más antiguos primero. Una parte es `text`, o `inlineData` para enviar una imagen, audio o video junto al prompt.

​

contents[].role

string

requerido

Quién escribió el turno.Valores posibles: `user`, `model`

​

contents[].parts

object[]

requerido

Las partes de contenido del turno.

​

contents[].parts[].text

string

Una parte de texto.

​

contents[].parts[].inlineData

object

Una parte de medios en línea.

​

contents[].parts[].inlineData.mimeType

string

Tipo de medio, por ejemplo `image/png`.

​

contents[].parts[].inlineData.data

string

Bytes del medio codificados en Base64.

​

systemInstruction

object

Prompt de sistema aplicado a toda la conversación.

​

systemInstruction.parts

object[]

​

systemInstruction.parts[].text

string

​

generationConfig

object

Configuraciones de muestreo y longitud.

​

generationConfig.temperature

number

Aleatoriedad del muestreo. Los valores predeterminados son específicos del modelo.Alcance: `0` a `2`

​

generationConfig.topP

number

Umbral de muestreo de núcleo. Los valores predeterminados son específicos del modelo.

​

generationConfig.topK

integer

Punto de corte del muestreo top-k. Los valores predeterminados son específicos del modelo.

​

generationConfig.maxOutputTokens

integer

Límite superior de tokens generados.

​

generationConfig.seed

integer

Semilla para un muestreo reproducible.

​

generationConfig.stopSequences

string[]

Cadenas que finalizan la generación cuando se producen.

​

generationConfig.thinkingConfig

object

Controles de esfuerzo de razonamiento en los modelos que lo admiten.

​

generationConfig.thinkingConfig.thinkingLevel

string

Valores posibles: `MINIMAL`, `LOW`, `MEDIUM`, `HIGH`

​

generationConfig.thinkingConfig.includeThoughts

boolean

Devuelve el razonamiento del modelo junto con la respuesta.

​

tools

object[]

Declaraciones de funciones que el modelo puede llamar.

​

tools[].functionDeclarations

object[]

​

tools[].functionDeclarations[].name

string

​

tools[].functionDeclarations[].description

string

​

tools[].functionDeclarations[].parameters

object

Esquema JSON para los argumentos de la función.

### 

​

Salida

El router devuelve la respuesta nativa de Google sin cambios. El texto está en `candidates[0].content.parts[0].text`.

​

candidates

object[]

Candidatos generados; uno, a menos que hayas solicitado más.

​

candidates[].content

object

​

candidates[].content.role

string

Valores posibles: `model`

​

candidates[].content.parts

object[]

​

candidates[].content.parts[].text

string

El texto generado.

​

candidates[].content.parts[].functionCall

object

Presente cuando el modelo eligió llamar a una de tus `tools`.

​

candidates[].content.parts[].functionCall.name

string

​

candidates[].content.parts[].functionCall.args

object

​

candidates[].finishReason

string

Por qué se detuvo la generación: `STOP`, `MAX_TOKENS`, `SAFETY`, …

​

usageMetadata

object

Recuento de tokens de la llamada.

​

usageMetadata.promptTokenCount

integer

Tokens en el prompt.

​

usageMetadata.candidatesTokenCount

integer

Tokens en los candidatos generados.

​

promptFeedback

object

Presente cuando el prompt en sí fue bloqueado. Verifica si `candidates` está presente antes de leer el resultado; `usageMetadata` también puede aparecer en una respuesta bloqueada.

​

promptFeedback.blockReason

string

Por qué se bloqueó el prompt. No se devuelven candidatos; reformula el prompt y reintenta.Valores posibles: `SAFETY`, `OTHER`, `BLOCKLIST`, `PROHIBITED_CONTENT`, `IMAGE_SAFETY`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "text": "Describe a single red maple leaf on a white background in one sentence."
            }
          ]
        }
      ],
      "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 256
      }
    }
    

### 

​

Salida
    
    
    {
      "candidates": [
        {
          "content": {
            "role": "model",
            "parts": [
              {
                "text": "A single red maple leaf rests on a plain white background, its edges sharp and its color deep."
              }
            ]
          },
          "finishReason": "STOP"
        }
      ],
      "usageMetadata": {
        "promptTokenCount": 18,
        "candidatesTokenCount": 24
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/google/gemini/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/google/gemini/code)

[Gemini Nano Banana 2.1](https://docs.comfy.org/es/development/comfy-router/models/google/gemini-nano-banana-2-1/code)[Nano Banana 2 Lite](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-2-lite/code)
