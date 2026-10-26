---
url: https://docs.comfy.org/es/development/comfy-router/models/byteplus/seedream-4-0-250828/code/
title: Usa Seedream 4.0 250828 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:01.552325+00:00
---

# Usa Seedream 4.0 250828 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/byteplus/seedream-4-0-250828/code/

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



BytePlus

# Usa Seedream 4.0 250828 con Comfy Router

Copiar páginaCopiar página

Llama a byteplus/seedream-4-0-250828 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `byteplus/seedream-4-0-250828`, servida por Comfy Router desde BytePlus. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP puro. **ID del modelo:** `byteplus/seedream-4-0-250828` **Endpoint:** `POST https://api.comfy.org/v2/models/byteplus/seedream-4-0-250828`

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
            "byteplus/seedream-4-0-250828",
            {
                "prompt": "A red fox trotting through a snowy pine forest, cinematic lighting",
                "response_format": "url",
                "watermark": False,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("byteplus/seedream-4-0-250828", {
      prompt: "A red fox trotting through a snowy pine forest, cinematic lighting",
      response_format: "url",
      watermark: false,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/byteplus/seedream-4-0-250828 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A red fox trotting through a snowy pine forest, cinematic lighting\", \"response_format\": \"url\", \"watermark\": false}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/byteplus/seedream-4-0-250828/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "byteplus/seedream-4-0-250828",
                {
                    "prompt": "A red fox trotting through a snowy pine forest, cinematic lighting",
                    "response_format": "url",
                    "watermark": False,
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, exactamente el valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("byteplus/seedream-4-0-250828", {
      prompt: "A red fox trotting through a snowy pine forest, cinematic lighting",
      response_format: "url",
      watermark: false,
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
    curl https://api.comfy.org/v2/models/byteplus/seedream-4-0-250828/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A red fox trotting through a snowy pine forest, cinematic lighting\", \"response_format\": \"url\", \"watermark\": false}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/byteplus/seedream-4-0-250828/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/byteplus/seedream-4-0-250828/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

guidance_scale

number

Controla qué tan fielmente se alinea la imagen de salida con el prompt de entrada. Rango [1, 10]. Los valores más altos producen una mayor adherencia al prompt. No es compatible con seedream-5.0-pro, 5.0-lite, 4.5 ni 4.0.Rango: `1` a `10`Formato: `float`

​

image

string | string[]

Seedream-5.0-pro, 5.0-lite, 4.5 y 4.0 admiten este parámetro.Introduce la codificación Base64 o una URL accesible de la imagen que quieres editar. Seedream-5.0-pro, 5.0-lite, 4.5 y 4.0 admiten introducir una sola imagen o varias imágenes (consulta el ejemplo de mezcla de varias imágenes).• URL de la imagen: asegúrate de que la URL de la imagen sea accesible. • Codificación Base64: el formato debe ser data:image/<image format>;base64,<Base64 encoding>. Nota: <image format> debe estar en minúsculas, por ejemplo, data:image/png;base64,<base64_image>.Comfy Router limita toda la solicitud JSON a 100 MiB, incluida la expansión de base64 y todas las imágenes de referencia. Usa URLs para las entradas que superen este límite de transporte.Una imagen de entrada debe cumplir los siguientes requisitos: • Formato de imagen: jpeg, png (seedream-5.0-pro, 5.0-lite, 4.5 y 4.0 también admiten webp, bmp, tiff y gif; seedream-5.0-pro también admite heic y heif) • Relación de aspecto (ancho/alto): en el rango [1/16, 16] para seedream-5.0-pro, 5.0-lite, 4.5 y 4.0 • Ancho y alto (px): > 14 • Tamaño: no más de 10 MB (30 MB para seedream-5.0-pro) • Píxeles totales: no más de 6000x6000 (36,000,000 px) para seedream-5.0-pro • Máximo de 14 imágenes de referencia (10 para seedream-5.0-pro y 5.0-flash)En el escenario de separación de capas (con layer_decomposition habilitado), image es requerido y solo se admite una única imagen de entrada (pasar varias imágenes devuelve un error). Las imágenes de entrada deben ser png, jpeg, webp, bmp, tiff o gif (no se admiten heic ni heif), de hasta 30 MB, con un total de píxeles en el rango [512x512, 6000x6000] y una relación de aspecto en [1/16, 16].

​

layer_decomposition

boolean

predeterminado:"false"

Controla si la separación de capas está habilitada. Solo seedream-5.0-pro y 5.0-flash admiten este parámetro. true: Modo de separación de capas. El modelo descompone la única imagen de entrada en una imagen base más varias capas (hasta 16) y devuelve la información de posición y contenido de cada capa producida, incluidos el orden de apilamiento (z_index), la caja delimitadora (bounding_box), el nombre (name) y la descripción (description). false: Modo estándar de generación de imágenes; no se realiza separación de capas. Notas sobre el modo de separación de capas: solo se admite una única imagen de entrada (pasar varias imágenes devuelve un error); si alguna capa individual no se genera, toda la solicitud falla: no se admite el éxito parcial; se devuelven como máximo 17 imágenes (1 imagen base + 16 capas). sequential_image_generation, sequential_image_generation_options, tools y stream devuelven un error si se pasan.

​

model

string

Identificador del modelo. Modelos compatibles: seedream-4-0-250828, seedream-4-5-251128, seedream-5-0-260128, seedream-5-0-pro-260628 y seedream-5-0-flash-260915. Una llamada directa v1 a POST /proxy/byteplus/api/v3/images/generations DEBE proporcionarlo: el proxy rechaza cualquier otro valor, y también su omisión, con un 400. NO está en la lista `required` de este esquema porque Comfy Router lo rellena a partir del segmento de ruta `{model}` de /v2/models/byteplus/{model}, así que quien llama a Router lo omite.

​

optimize_prompt_options

object

Configuración de la función de optimización de prompt. Solo seedream-5.0-pro/5.0-lite/4.5 (solo admiten el modo standard) y seedream-4.0 admiten este parámetro.

​

optimize_prompt_options.mode

string

predeterminado:"\"standard\""

Establece el modo de la función de optimización de prompt. standard = mayor calidad, mayor tiempo de generación. fast = más rápido, pero con una calidad más media.Posibles valores: `standard`, `fast`

​

output_format

string

predeterminado:"\"jpeg\""

Especifica el formato de la imagen de salida. Solo seedream-5.0-pro, 5.0-flash y 5.0-lite admiten este parámetro. En el escenario de separación de capas, output_format solo controla el formato de la imagen base; cada capa siempre se emite como png.Posibles valores: `png`, `jpeg`

​

prompt

string

Descripción de texto para la generación o transformación de imágenes. Opcional en el escenario de separación de capas (seedream-5.0-pro o 5.0-flash con layer_decomposition habilitado): si se proporciona un prompt, el modelo reconoce y separa los elementos que especifiques según la intención del prompt; si no se proporciona ningún prompt, el modelo detecta automáticamente todos los elementos principales de la imagen y los separa en capas independientes.

​

response_format

string

predeterminado:"\"url\""

Especifica el formato de la imagen generada que se devuelve en la respuestaPosibles valores: `url`, `b64_json`

​

seed

integer

predeterminado:"-1"

Semilla aleatoria para controlar la estocasticidad de la generación de imágenes. Rango: [-1, 2147483647]. Si no se especifica, se generará una semilla automáticamente. Para reproducir la misma salida, usa el mismo valor de semilla.Rango: `-1` a `2147483647`

​

sequential_image_generation

string

Controla si se deshabilita la función de generación por lotes. Este parámetro solo es compatible con seedream-5.0-lite, 4.5 y 4.0 (no es compatible con seedream-5.0-pro ni 5.0-flash). Valores válidos: auto: En modo automático, el modelo determina automáticamente si devolver varias imágenes y cuántas imágenes incluirá según el prompt del usuario. disabled: Deshabilita la función de generación por lotes. El modelo solo generará una imagen.Posibles valores: `auto`, `disabled`

​

sequential_image_generation_options

object

Solo seedream-5.0-lite, 4.5 y 4.0 admiten este parámetro (no lo admiten seedream-5.0-pro ni 5.0-flash). Configuración de la función de generación de imágenes por lotes. Este parámetro solo tiene efecto cuando sequential_image_generation se establece en auto.

​

sequential_image_generation_options.max_images

integer

predeterminado:"15"

Especifica el número máximo de imágenes para generar en esta solicitud. Número de imágenes de referencia de entrada + Número de imágenes generadas ≤ 15.Rango: `1` a `15`

​

size

string

“seedream-4-0-250828”: Establece la especificación de la imagen generada. Hay dos métodos disponibles, pero no se pueden usar juntos. Método 1 | Especifica la resolución. Valores opcionales: 1K, 2K, 4K Método 2 | Especifica el ancho y el alto en píxeles. Predeterminado: 2048x2048, píxeles totales: [1024x1024, 4096x4096], relación de aspecto: [1/16, 16] “seedream-4-5-251128”: Dos métodos disponibles. Método 1 | Especifica la resolución. Valores opcionales: 2K, 4K Método 2 | Especifica el ancho y el alto en píxeles. Predeterminado: 2048x2048, píxeles totales: [2560x1440, 4096x4096], relación de aspecto: [1/16, 16] “seedream-5-0-260128”: Dos métodos disponibles. Método 1 | Especifica la resolución. Valores opcionales: 2K, 3K Método 2 | Especifica el ancho y el alto en píxeles. Predeterminado: 2048x2048, píxeles totales: [2560x1440, ~3072x3072], relación de aspecto: [1/16, 16] “seedream-5-0-pro-260628”: Dos métodos disponibles (no se pueden usar juntos). Método 1 | Especifica la resolución y describe en el prompt la relación de aspecto, la forma o el propósito de la imagen; el modelo decide el tamaño final. Valores opcionales: 1K, 2K Método 2 | Especifica el ancho y el alto en píxeles. Predeterminado: 1024x1024, píxeles totales: [1024x1024 (1048576), 2048x2048 (4194304)], relación de aspecto: [1/16, 16] “seedream-5-0-flash-260915”: Dos métodos disponibles (no se pueden usar juntos). Método 1 | Especifica la resolución y describe en el prompt la relación de aspecto, la forma o el propósito de la imagen; el modelo decide el tamaño final. Valores opcionales: 1K, 1.5K, 2K. Predeterminado: 2K Método 2 | Especifica el ancho y el alto en píxeles. Píxeles totales: [1280x720 (921600), 2048x2048x1.1025 (4624220)], relación de aspecto: [1/16, 16] “seedream-5-0-pro-260628” y “seedream-5-0-flash-260915” con layer_decomposition habilitado: Solo se admite el método basado en la resolución. Valores opcionales: 1K, 1.5K, 2K, auto. Predeterminado: auto. La imagen base se genera con la resolución especificada y la relación de aspecto de la imagen de entrada original; cada capa se genera con una resolución cercana a la especificada, manteniendo la relación de aspecto que tenía en la imagen original. auto: La salida se basa en el tamaño y la relación de aspecto de la imagen de entrada. Las entradas dentro de [1280x720, ~2048x2048] se generan con el tamaño original de entrada; las entradas menores que 1K se generan a 1K; las entradas mayores que 2K se generan a 2K.

​

stream

boolean

predeterminado:"false"

Comfy Router establece en false un flag stream proporcionado explícitamente porque captura un resultado JSON completo. En el proxy v1, este campo controla si se habilita el modo de salida en streaming. Solo seedream-5.0-lite, 4.5 y 4.0 admiten este parámetro (no lo admiten seedream-5.0-pro ni 5.0-flash). false = Todas las imágenes de salida se devuelven a la vez. true = Cada imagen de salida se devuelve inmediatamente después de generarse.

​

watermark

boolean

predeterminado:"true"

Especifica si se añade una marca de agua a la imagen generada. false = Sin marca de agua, true = Añade una marca de agua con la etiqueta ‘AI generated’

Generado a partir del esquema que Router ofrece en `GET /v2/models/byteplus/seedream-4-0-250828/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

created

integer

Marca de tiempo Unix (en segundos) que indica el momento en que se creó la solicitud

​

data

object[]

Contiene información sobre las imágenes generadas. En el escenario de separación por capas, el primer elemento del arreglo es la imagen base (z_index=0) y los elementos siguientes son las capas, ordenadas por z_index creciente.

​

data[].b64_json

string

Datos de imagen codificados en Base64 (si response_format es “b64_json”)

​

data[].bounding_box

object

La información de la caja delimitadora de la región que ocupa la capa actual dentro de la imagen base. Solo las capas devuelven este campo; la imagen base cubre todo el lienzo y no devuelve bounding_box. Se devuelve solo cuando layer_decomposition es verdadero.

​

data[].bounding_box.absolute

integer[]

Las coordenadas absolutas en píxeles de la caja delimitadora de la capa, en el sistema de coordenadas de la imagen base de salida con la esquina superior izquierda en (0, 0). Formato de coordenadas: [left, top, right, bottom].

​

data[].bounding_box.normalized

integer[]

Las coordenadas cuantizadas por mil (normalizadas) de la caja delimitadora de la capa, asignadas proporcionalmente a un rango entero discreto de [0, 1000] según el tamaño de la imagen base, truncadas como máximo en 1000. Formato de coordenadas: [left, top, right, bottom].

​

data[].description

string

Una descripción detallada del elemento separado actual, que ofrece características de capa más ricas (como color, estado o material) que name. Solo las capas devuelven este campo; la imagen base no lo hace. Se devuelve solo cuando layer_decomposition es verdadero.

​

data[].name

string

El nombre o etiqueta del elemento separado actual, generado automáticamente por el modelo a partir de las características del sujeto separado. Solo las capas devuelven este campo; la imagen base no lo hace. Se devuelve solo cuando layer_decomposition es verdadero.

​

data[].output_format

string

El formato de archivo de la imagen de salida. Solo seedream-5.0-pro admite este campo.

​

data[].size

string

El ancho y el alto de la imagen en píxeles, en el formato <width>x<height>. Solo seedream-5.0-pro, 5.0-lite, 4.5 y 4.0 admiten este parámetro.

​

data[].url

string (uri)

URL para descargar la imagen (si response_format es “url”)Formato: `uri`

​

data[].z_index

integer

El orden de apilamiento de la capa, que aumenta de abajo hacia arriba: 0 es la capa más baja (la imagen base); los valores mayores quedan más arriba. Úsalo para recomponer las capas en la imagen completa con el orden de apilamiento correcto. Se devuelve solo cuando layer_decomposition es verdadero.

​

error

object

Información de error (si la hay)

​

error.code

string

Código de error de ModelArk ascendente. SensitiveContentDetected, InputTextSensitiveContentDetected, InputImageSensitiveContentDetected, InputVideoSensitiveContentDetected, InputAudioSensitiveContentDetected, OutputTextSensitiveContentDetected, OutputImageSensitiveContentDetected, OutputVideoSensitiveContentDetected y OutputAudioSensitiveContentDetected identifican rechazos por políticas de contenido. Una familia puede incluir un motivo separado por puntos, como InputImageSensitiveContentDetected.PrivacyInformation, OutputVideoSensitiveContentDetected.PolicyViolation u OutputImageSensitiveContentDetected.DeepFake. Es una cadena abierta, no una enumeración: otros códigos describen fallos de validación y del proveedor. Router reconoce las familias de políticas en las respuestas de error HTTP 400 y en las respuestas de tarea fallida HTTP 200 sin sobrescribir los fallos de transporte.

​

error.message

string

Mensaje de error

​

model

string

El ID del modelo utilizado para la solicitud

​

usage

object

​

usage.generated_images

integer

Número de imágenes generadas por el modelo

​

usage.input_images

integer

El número de imágenes de entrada al modelo. Solo seedream-5.0-pro admite este campo.

​

usage.output_tokens

integer

El número de tokens utilizados para la imagen generada por el modelo.

​

usage.total_tokens

integer

El número total de tokens consumidos por esta solicitud.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "prompt": "A red fox trotting through a snowy pine forest, cinematic lighting",
      "response_format": "url",
      "watermark": false
    }
    

### 

​

Salida
    
    
    {
      "created": 1767225600,
      "data": [
        {
          "size": "1024x1024",
          "url": "https://example.invalid/byteplus/seedream-4-0-250828/generated.png"
        }
      ],
      "model": "seedream-4-0-250828",
      "usage": {
        "generated_images": 1
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/byteplus/seedream-4-0-250828/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/byteplus/seedream-4-0-250828/code)

[Seedance 1.5 Pro 251215](https://docs.comfy.org/es/development/comfy-router/models/byteplus/seedance-1-5-pro-251215/code)[Seedream 4.5 251128](https://docs.comfy.org/es/development/comfy-router/models/byteplus/seedream-4-5-251128/code)
