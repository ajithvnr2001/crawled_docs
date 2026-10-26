---
url: https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-2/code/
title: Usa Nano Banana 2 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:06.159887+00:00
---

# Usa Nano Banana 2 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-2/code/

## En esta página

Volver arriba

  * Inicio rápido
  * Proveedores de servicio
  * Esquema
    * Entrada
    * Salida
  * Ejemplos
    * Entrada
    * Salida
  * Antes de lanzar



Google

# Usa Nano Banana 2 con Comfy Router

Copiar páginaCopiar página

Fragmentos de Python, TypeScript y cURL para generar imágenes con Nano Banana 2 (Gemini 3.1 Flash Image) a través de Comfy Router, y campos de la solicitud

Copiar páginaCopiar página

Referencia de API de Nano Banana 2. Nano Banana 2 (Gemini 3.1 Flash Image) genera imágenes a partir de texto y edita una imagen de entrada cuando se proporciona una. **Entrada:** Texto, Imagen, Video · **Salida:** Imagen + Texto

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `vertexai/gemini-3.1-flash-image` **Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image`

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
                "vertexai/gemini-3.1-flash-image",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "a single red maple leaf on a plain white background, studio lighting",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "responseModalities": ["IMAGE"],
                        "imageConfig": {
                            "aspectRatio": "1:1",
                        },
                    },
                },
            )
    
        print("image (base64):", result["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    type Result = { candidates: { content: { parts: { inlineData: { data: string } }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-3.1-flash-image", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "a single red maple leaf on a plain white background, studio lighting",
            },
          ],
        },
      ],
      generationConfig: {
        responseModalities: ["IMAGE"],
        imageConfig: {
          aspectRatio: "1:1",
        },
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image (base64):", result.data.candidates[0].content.parts[0].inlineData.data);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"a single red maple leaf on a plain white background, studio lighting\"}]}], \"generationConfig\": {\"responseModalities\":[\"IMAGE\"],\"imageConfig\":{\"aspectRatio\":\"1:1\"}}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image/requests`. El Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) repasa el estado, la cancelación y la recogida.

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
                "vertexai/gemini-3.1-flash-image",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "a single red maple leaf on a plain white background, studio lighting",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "responseModalities": ["IMAGE"],
                        "imageConfig": {
                            "aspectRatio": "1:1",
                        },
                    },
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada lanza aquí el error tipado del Router.
            result = await handle.get()
    
        print("image (base64):", result["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    type Result = { candidates: { content: { parts: { inlineData: { data: string } }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-3.1-flash-image", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "a single red maple leaf on a plain white background, studio lighting",
            },
          ],
        },
      ],
      generationConfig: {
        responseModalities: ["IMAGE"],
        imageConfig: {
          aspectRatio: "1:1",
        },
      },
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image (base64):", result.data.candidates[0].content.parts[0].inlineData.data);
    
    
    
    # 1. Envía. El Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"a single red maple leaf on a plain white background, studio lighting\"}]}], \"generationConfig\": {\"responseModalities\":[\"IMAGE\"],\"imageConfig\":{\"aspectRatio\":\"1:1\"}}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Proveedores de servicio

Este modelo es servida por Comfy Router directamente a menos que la solicitud nombre otro proveedor. Los proveedores a continuación también lo sirven, en el mismo endpoint y con el mismo ID de modelo, seleccionados con el parámetro de consulta `model_provider`.

  * **Comfy** (predeterminado): `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image`
  * **fal** , como `fal/fal-nano-banana-2`: `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image?model_provider=fal`
  * **Pika** , como `pika/pika-nano-banana-2`: `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image?model_provider=pika`
  * **Runware** , como `runware/runware-nano-banana-2`: `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image?model_provider=runware`
  * **WaveSpeed** , como `wavespeed/wavespeed-nano-banana-2`: `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-flash-image?model_provider=wavespeed`

`strict_mode` tiene como valor predeterminado false, por lo que Router traduce el cuerpo de la solicitud nativa documentado en esta página al esquema propio del proveedor y traduce la respuesta de vuelta. Consulta [`model_provider`, `strict_mode` y `fallback_provider`](https://docs.comfy.org/es/development/comfy-router/reference#post-v2modelsprovidermodel) en la Referencia de la API, y [Proveedores de servicio](https://docs.comfy.org/es/development/comfy-router/providers) para cada modelo enrutado de esta manera.

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

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para obtener más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

contents[].parts[].inlineData

object

Datos en línea en bytes sin procesar. Para gemini-2.0-flash-lite y gemini-2.0-flash, puedes especificar hasta 3000 imágenes usando inlineData.

​

contents[].parts[].inlineData.data

string (byte)

La codificación base64 de la imagen, el PDF o el video que quieres incluir en línea en el prompt. Cuando incluyes medios en línea, también debes especificar el tipo de medio (mimeType) de los datos. Límite de tamaño: 20MBFormato: `byte`

​

contents[].parts[].inlineData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para obtener más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de imágenes.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

contents[].parts[].mediaProcessing

string

Cómo lee el modelo el video de esta parte. Establece “AGENTIC” para que el modelo decida qué segmentos inspeccionar, en lugar de un muestreo de fotogramas a tasa fija. Omite el campo para usar el muestreo de tasa fija predeterminado. Compatible con gemini-3.7-flash y modelos Flash más recientes.

​

contents[].parts[].text

string

Un prompt de texto o un fragmento de código.

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

Opcional. El formato de salida de imagen para las imágenes generadas.

​

generationConfig.imageConfig.imageOutputOptions.compressionQuality

integer

Opcional. La calidad de compresión de la imagen de salida.

​

generationConfig.imageConfig.imageOutputOptions.mimeType

string

Opcional. El formato de imagen con el que se debe guardar la salida, en las rutas de Vertex AI: solicitudes atendidas por las credenciales propias de Comfy y solicitudes BYOK autenticadas con una cuenta de servicio de GCP. Los valores aceptados allí son `image/png` e `image/jpeg`, comparados sin distinguir mayúsculas y normalizados a minúsculas antes de reenviar la solicitud; cualquier otro valor se rechaza con un 400 que nombra este campo. El valor predeterminado es `image/png` cuando se omite. Una solicitud BYOK autenticada con una clave API de Google AI Studio es la excepción: ese upstream no tiene tal propiedad y rechaza toda la llamada si está presente, así que el campo se descarta de la solicitud en lugar de respetarse o rechazarse, y el formato de salida es el que elija AI Studio. En todas las rutas, vuelve a leer el tipo de medio desde la parte de la respuesta que recibes (`inlineData.mimeType`, o `fileData.mimeType` cuando `uploadImagesToStorage` está configurado) en lugar de asumir el valor que enviaste.

​

generationConfig.imageConfig.imageSize

string

Opcional. Especifica el tamaño de las imágenes generadas. Los valores admitidos son 1K, 2K, 4K. Si no se especifica, el modelo usará el valor predeterminado 1K.

​

generationConfig.maxOutputTokens

integer

Número máximo de tokens que se pueden generar en la respuesta. Un token equivale aproximadamente a 4 caracteres. 100 tokens corresponden a unas 60-80 palabras.Rango: `16` a `65536`

​

generationConfig.responseModalities

`TEXT`, `IMAGE`[]

​

generationConfig.seed

integer

Cuando la semilla se fija a un valor específico, el modelo hace su mejor esfuerzo por proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o las configuraciones de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando usas el mismo valor de semilla. De forma predeterminada, se usa un valor de semilla aleatorio. Disponible para los siguientes modelos: gemini-2.5-flash, gemini-2.5-pro, gemini-2.5-flash-preview-04-1, gemini-2.5-pro-preview-05-0, gemini-2.0-flash-lite-00, gemini-2.0-flash-001

​

generationConfig.stopSequences

string[]

​

generationConfig.temperature

number

predeterminado:"1"

La temperatura se usa para el muestreo durante la generación de respuestas, que ocurre cuando se aplican topP y topK. La temperatura controla el grado de aleatoriedad en la selección de tokens. Las temperaturas más bajas son buenas para prompts que requieren una respuesta menos abierta o creativa, mientras que las temperaturas más altas pueden llevar a resultados más diversos o creativos. Una temperatura de 0 significa que siempre se seleccionan los tokens de mayor probabilidad. En este caso, las respuestas para un prompt dado son en su mayoría deterministas, pero aún es posible una pequeña cantidad de variación. Si el modelo devuelve una respuesta demasiado genérica, demasiado corta, o el modelo da una respuesta de respaldo, intenta aumentar la temperaturaRango: `0` a `2`Formato: `float`

​

generationConfig.thinkingConfig

object

Opcional. Configuración para las funciones de pensamiento. El pensamiento es un proceso en el que el modelo descompone una tarea compleja en pasos más pequeños para generar una respuesta de mayor calidad.

​

generationConfig.thinkingConfig.includeThoughts

boolean

Opcional. Si es verdadero, el modelo incluirá sus pensamientos en la respuesta.

​

generationConfig.thinkingConfig.thinkingBudget

integer

Opcional. El presupuesto de tokens para el proceso de pensamiento del modelo. El modelo hará su mejor esfuerzo por mantenerse dentro de este presupuesto.

​

generationConfig.thinkingConfig.thinkingLevel

string

Opcional. El nivel de pensamiento para el modelo.Valores posibles: `THINKING_LEVEL_UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH`, `MINIMAL`

​

generationConfig.topK

integer

predeterminado:"40"

Top-K cambia cómo el modelo selecciona tokens para la salida. Un top-K de 1 significa que el siguiente token seleccionado es el más probable entre todos los tokens del vocabulario del modelo. Un top-K de 3 significa que el siguiente token se selecciona entre los 3 tokens más probables usando la temperatura.Rango: `1` a `…`

​

generationConfig.topP

number

predeterminado:"0.95"

Si se especifica, se usa muestreo de núcleo. Top-P cambia cómo el modelo selecciona tokens para la salida. Los tokens se seleccionan desde el más (ver top-K) hasta el menos probable hasta que la suma de sus probabilidades sea igual al valor de top-P. Por ejemplo, si los tokens A, B y C tienen una probabilidad de 0.3, 0.2 y 0.1 y el valor de top-P es 0.5, entonces el modelo seleccionará A o B como el siguiente token usando la temperatura y excluye a C como candidato. Especifica un valor más bajo para respuestas menos aleatorias y un valor más alto para respuestas más aleatorias.Rango: `0` a `1`Formato: `float`

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

Instrucciones para el modelo para orientarlo hacia un mejor rendimiento. Por ejemplo, “Responde de la forma más concisa posible” o “No uses términos técnicos en tu respuesta”. Las cadenas de texto cuentan para el límite de tokens. El campo role de systemInstruction se ignora y no afecta el rendimiento del modelo. Nota: Solo se debe usar texto en las partes y el contenido de cada parte debe estar en un párrafo separado.

​

systemInstruction.parts

object[]

requerido

Una lista de partes ordenadas que componen un solo mensaje. Las diferentes partes pueden tener diferentes tipos MIME de IANA. Para conocer los límites de las entradas, como el número máximo de tokens o el número de imágenes, consulta las especificaciones del modelo en la página de modelos de Google.

​

systemInstruction.parts[].text

string

Un prompt de texto o un fragmento de código.

​

systemInstruction.role

string

La identidad de la entidad que crea el mensaje. Se admiten los siguientes valores: user: Esto indica que el mensaje lo envía una persona real, normalmente un mensaje generado por el usuario. model: Esto indica que el mensaje lo genera el modelo. El valor model se usa para insertar mensajes del modelo en la conversación durante conversaciones de varios turnos. Para conversaciones que no son de varios turnos, este campo se puede dejar en blanco o sin configurar.Valores posibles: `user`, `model`

​

tools

object[]

Un fragmento de código que permite al sistema interactuar con sistemas externos para realizar una acción, o un conjunto de acciones, fuera del conocimiento y alcance del modelo. Consulta Llamada a funciones.

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

Esquema JSON de los parámetros de la función

​

uploadImagesToStorage

boolean

Si es verdadero, las imágenes generadas se suben al almacenamiento en la nube y se devuelven como URLs firmadas en lugar de datos base64 en línea. Las URLs caducan a las 24 horas.

​

videoMetadata

object

Para entrada de video, el desplazamiento de inicio y fin del video en formato Duration. Por ejemplo, para especificar un clip de 10 segundos que comienza en 1:00, establece “startOffset”: { “seconds”: 60 } y “endOffset”: { “seconds”: 70 }. Los metadatos solo deben especificarse mientras los datos del video se presentan en inlineData o fileData.

​

videoMetadata.endOffset

object

Representa un desplazamiento de duración para posiciones en la línea de tiempo del video.

​

videoMetadata.endOffset.nanos

integer

Fracciones de segundo con signo y resolución de nanosegundos. Los valores negativos de segundos con fracciones deben seguir teniendo valores de nanos no negativos.Rango: `0` a `999999999`

​

videoMetadata.endOffset.seconds

integer

Segundos con signo del intervalo de tiempo. Debe estar entre -315,576,000,000 y +315,576,000,000 inclusive.Rango: `-315576000000` a `315576000000`

​

videoMetadata.startOffset

object

Representa un desplazamiento de duración para posiciones en la línea de tiempo del video.

​

videoMetadata.startOffset.nanos

integer

Fracciones de segundo con signo y resolución de nanosegundos. Los valores negativos de segundos con fracciones deben seguir teniendo valores de nanos no negativos.Rango: `0` a `999999999`

​

videoMetadata.startOffset.seconds

integer

Segundos con signo del intervalo de tiempo. Debe estar entre -315,576,000,000 y +315,576,000,000 inclusive.Rango: `-315576000000` a `315576000000`

Generado a partir del esquema que Router sirve en `GET /v2/models/vertexai/gemini-3.1-flash-image/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

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

El contenido de la conversación actual con el modelo. Para consultas de un solo turno, esta es una única instancia. Para consultas de varios turnos, este es un campo repetido que contiene el historial de la conversación y la solicitud más reciente.

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

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para obtener más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de la imagen.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

candidates[].content.parts[].inlineData

object

Datos insertados en bytes sin procesar. Para gemini-2.0-flash-lite y gemini-2.0-flash, puedes especificar hasta 3000 imágenes usando inlineData.

​

candidates[].content.parts[].inlineData.data

string (byte)

La codificación base64 de la imagen, PDF o video para incluir directamente en el prompt. Cuando incluyes medios directamente, también debes especificar el tipo de medio (mimeType) de los datos. Límite de tamaño: 20MBFormato: `byte`

​

candidates[].content.parts[].inlineData.mimeType

string

El tipo de medio del archivo especificado en los campos data o fileUri. Los valores aceptables incluyen los siguientes. Para gemini-2.0-flash-lite y gemini-2.0-flash, la duración máxima de un archivo de audio es de 8.4 horas y la duración máxima de un archivo de video (sin audio) es de una hora. Para obtener más información, consulta los requisitos de audio y video de Gemini. Los archivos de texto deben estar codificados en UTF-8. El contenido del archivo de texto cuenta para el límite de tokens. No hay límite en la resolución de la imagen.Valores posibles: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

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

La versión del modelo utilizada para generar la respuesta.

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

Solo de salida. Número de tokens en la parte en caché de la entrada (el contenido en caché).

​

usageMetadata.candidatesTokenCount

integer

Número de tokens en la respuesta o respuestas.

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

Número de tokens para la modalidad dada.

​

usageMetadata.promptTokenCount

integer

Número de tokens en la solicitud. Cuando cachedContent está configurado, este valor sigue siendo el tamaño total efectivo del prompt, lo que significa que incluye el número de tokens del contenido en caché.

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

Número de tokens para la modalidad dada.

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

Número de tokens para la modalidad dada.

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
              "text": "a single red maple leaf on a plain white background, studio lighting"
            }
          ]
        }
      ],
      "generationConfig": {
        "responseModalities": [
          "IMAGE"
        ],
        "imageConfig": {
          "aspectRatio": "1:1"
        }
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
                "inlineData": {
                  "mimeType": "image/png",
                  "data": "PGJhc2U2ND4="
                }
              }
            ]
          },
          "finishReason": "STOP"
        }
      ],
      "usageMetadata": {
        "promptTokenCount": 12,
        "candidatesTokenCount": 1290
      }
    }
    

De forma predeterminada, las partes de imagen generadas contienen bytes en base64 en `inlineData.data` y un tipo de medio en `inlineData.mimeType`. Decodifica los bytes y guárdalos en un archivo. Con `uploadImagesToStorage: true`, las imágenes subidas usan en su lugar `fileData.fileUri` para una URL firmada y `fileData.mimeType` para el tipo de medio. Descarga estas imágenes antes de que las URL expiren, 24 horas después de su creación. Un fallo en la subida deja esa imagen en línea, así que revisa cada parte en busca de `inlineData` o `fileData`; también pueden aparecer partes de texto, y no se garantiza que la imagen sea la primera parte. La ruta `candidates[0].content.parts[0].inlineData.data` de los ejemplos de inicio rápido anteriores lee la única parte en línea de la respuesta de ejemplo de esta página; frente a una respuesta real, recorre `parts` en busca de la clave que quieras en lugar de indexar la posición 0.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/google/nano-banana-2/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/google/nano-banana-2/code)

[Nano Banana 2 Lite](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-2-lite/code)[Nano Banana Pro](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-pro/code)
