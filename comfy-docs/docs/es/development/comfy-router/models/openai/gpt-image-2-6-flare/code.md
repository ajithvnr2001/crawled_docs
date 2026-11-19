---
url: https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-6-flare/code/
title: Usa GPT Image 2.6 Flare con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-19T16:26:10.475039+00:00
---

# Usa GPT Image 2.6 Flare con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-6-flare/code/

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



OpenAI

# Usa GPT Image 2.6 Flare con Comfy Router

Copiar páginaCopiar página

Llama a openai/gpt-image-2.6-flare mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API de `openai/gpt-image-2.6-flare`, servido por Comfy Router desde OpenAI. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **Model ID:** `openai/gpt-image-2.6-flare` **Endpoint:** `POST https://api.comfy.org/v2/models/openai/gpt-image-2.6-flare`

  * Esperar el resultado

  * Enviar a la cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "openai/gpt-image-2.6-flare",
            {
                "prompt": "a rocketship on a launchpad",
                "quality": "low",
                "size": "1024x1024",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("openai/gpt-image-2.6-flare", {
      prompt: "a rocketship on a launchpad",
      quality: "low",
      size: "1024x1024",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/openai/gpt-image-2.6-flare \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a rocketship on a launchpad\", \"quality\": \"low\", \"size\": \"1024x1024\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/openai/gpt-image-2.6-flare/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, ya sea desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica paso a paso el estado, la cancelación y la recogida del resultado.

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
                "openai/gpt-image-2.6-flare",
                {
                    "prompt": "a rocketship on a launchpad",
                    "quality": "low",
                    "size": "1024x1024",
                },
            )
            print("request_id:", handle.request_id)  # junto con el model ID, es todo lo que necesita otro proceso
    
            # Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga nativa del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("openai/gpt-image-2.6-flare", {
      prompt: "a rocketship on a launchpad",
      quality: "low",
      size: "1024x1024",
    });
    console.log("requestId:", handle.requestId); // junto con el model ID, es todo lo que necesita otro proceso
    
    // Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/openai/gpt-image-2.6-flare/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a rocketship on a launchpad\", \"quality\": \"low\", \"size\": \"1024x1024\"}"
    
    # 2. Consultar el estado hasta que sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/openai/gpt-image-2.6-flare/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/openai/gpt-image-2.6-flare/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Proveedores de servicio

Comfy Router sirve este modelo directamente, a menos que la solicitud indique otro proveedor. Los proveedores a continuación también lo sirven, en el mismo endpoint y con el mismo ID de modelo, seleccionados con el parámetro de consulta `model_provider`.

  * **Comfy** (predeterminado): `POST https://api.comfy.org/v2/models/openai/gpt-image-2.6-flare`
  * **MiniMax** , como `minimax/minimax-gpt-image-2.6-flare`: `POST https://api.comfy.org/v2/models/openai/gpt-image-2.6-flare?model_provider=minimax`

`strict_mode` tiene como valor predeterminado false, por lo que Router traduce el cuerpo de la solicitud nativo documentado en esta página al esquema propio del proveedor y traduce la respuesta de vuelta. Consulta [`model_provider`, `strict_mode` y `fallback_provider`](https://docs.comfy.org/es/development/comfy-router/reference#post-v2modelsprovidermodel) en la referencia de la API, y [Proveedores de servicio](https://docs.comfy.org/es/development/comfy-router/providers) para todos los modelos enrutados de esta manera.

## Esquema

### Entrada

background

string

Transparencia del fondo. `auto` deja que el modelo elija.Valores posibles: `transparent`, `opaque`, `auto`

frame_count

integer

El número de fotogramas del GIF animado (2-16, el rango propio de OpenAI), significativo solo con `output_format: "gif"`: se rechaza si se usa junto con cualquier otro `output_format`. Si se omite en una solicitud GIF, toma el valor predeterminado de OpenAI de 9, EXCEPTO que Comfy además limita este campo por entorno (ROUTER_OPENAI_IMAGE_GIF_MAX_FRAMES, nunca por encima del máximo propio de este campo de 16): se rechaza un valor por encima del límite configurado, y se rechaza un `frame_count` omitido en lugar de reducirlo silenciosamente cuando el valor predeterminado de 9 supera el límite configurado, de modo que se le indica a quien llama que establezca `frame_count` explícitamente en lugar de recibir una animación silenciosamente más pequeña que el valor predeterminado de OpenAI. El número de fotogramas también limita la cotización previa y el límite de 64 MiB del resultado, y ambos escalan con él.Alcance: `2` a `16`

frame_duration_ms

integer

Los milisegundos que se muestra cada fotograma (el rango propio de OpenAI es 20-2000, redondeado a 10 ms), significativo solo con `output_format: "gif"`: se rechaza si se usa junto con cualquier otro `output_format`. Si se omite en una solicitud GIF, toma el valor predeterminado propio de OpenAI de 200.Alcance: `20` a `2000`

image

string | string[]

La imagen o imágenes de origen que se van a editar. LA PRESENCIA DE ESTE CAMPO SELECCIONA LA OPERACIÓN DE EDICIÓN: omítelo por completo para la generación de texto a imagen. El ejemplo publicado del modelo es la llamada de GENERACIÓN, que omite este campo. Añadir `image` es toda la diferencia entre los dos modos: mismo endpoint, mismo id de modelo, excepto que un prompt de edición describe el CAMBIO que quieres en lugar de la escena, así que el cuerpo de edición de abajo se lee de forma distinta al ejemplo de generación aunque solo este campo sea estructuralmente nuevo. Se puede copiar exactamente como se muestra: `{"prompt": "give the rocketship rainbow coloring", "image": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="], "size": "1024x1024"}`. La carga útil es un PNG completo de 1x1, no una abreviatura, y este cuerpo está fijado como un caso aceptado en las pruebas de validación de solicitudes del propio Router. Sustituye los bytes de tu propia imagen. Acepta una imagen o un arreglo de ellas; gpt-image-1 y versiones posteriores aceptan hasta 16, lo que Router aplica desde este esquema antes de despachar.

mask

string

Una imagen, ya sea como una URL https que Router obtiene en nombre de quien llama o como un URI `data:image/<format>;base64,<payload>` que lleva los bytes en línea. Los tipos de imagen aceptados son png, webp y jpeg, y ese conjunto se EXIGE en el momento de resolución en lugar de dejarlo al proveedor: un svg, gif, avif o tiff se rechaza aquí, nombrando la imagen que enviaste, en lugar de convertirse en un error de socio a dos saltos de la causa. Prefiere la forma de URL. Una carga útil base64 se infla aproximadamente 4/3 y todo el cuerpo de la solicitud está limitado a 100 MiB, así que la forma en línea llega como máximo a cerca de una imagen de origen de 75 MB; una URL evita eso por completo. Los límites de medios por imagen y por solicitud indicados al final de esta descripción son más estrictos que el límite del cuerpo, así que para una imagen de cualquier tamaño real son los que encuentras primero. LA URL DEBE RESOLVERSE SIN TUS CREDENCIALES. Router la obtiene del lado del servidor y no envía ninguna credencial de quien llama con la solicitud, así que una URL prefirmada, una cuya firma está en la cadena de consulta, es la forma admitida. Un endpoint autenticado como `/api/assets/{id}/content` responde a Router 401 en lugar de la imagen; solicita esa URL tú mismo y pasa la URL firmada a la que redirige. LA OBTENCIÓN ESTÁ CONFINADA A UN CONJUNTO NOMBRADO DE HOSTS en lugar de la internet abierta, y la misma lista se vuelve a aplicar a cada salto de redirección, así como a la URL que envías, de modo que una URL en cualquier otro host, o una que redirige fuera de la lista, se rechaza antes de contactar a cualquier proveedor. Hoy esa lista es solo la entrega de recursos propia de Comfy: una URL firmada de `storage.googleapis.com` bajo un bucket de recursos de Comfy, que es la forma a la que te redirige `/api/assets/{id}/content`. Un CDN de socio o un host https simple NO está en la lista. DOS AMPLIACIONES SE ESTÁN DESPLEGANDO Y HOY AMBAS ESTÁN DESACTIVADAS DE FORMA PREDETERMINADA. Se lanzan detrás de UN único interruptor y se habilitan juntas, así que trata todo lo siguiente como algo futuro en lugar de algo sobre lo que construir todavía: pregunta antes de depender de cualquiera de las dos. La PRIMERA es el bucket en el que `POST /customers/storage` firma tu carga. Hasta que el despliegue llegue a tu entorno, una URL de carga de ese endpoint se rechaza aquí, aunque el bucket sea propio de Comfy y el host sea el mismo, así que “subir a Comfy y luego pasar la URL” TODAVÍA NO funciona, y la forma que sí funciona es la URL firmada a la que redirige `/api/assets/{id}/content`. La SEGUNDA SE HABILITA POR CUENTA en lugar de para todos a la vez, porque el bucket detrás de estos hosts es tuyo y no nuestro: incluso una vez que el interruptor anterior está activado, se rechaza una cuenta a la que no se le han habilitado los medios entrantes de terceros, y se le dice eso con esas palabras en lugar de decirle que el host no es compatible. Pide a tu contacto de Comfy que lo habilite para tu cuenta. Además, admite estos hosts de almacenamiento de objetos de terceros, donde el bucket es tuyo y Router no reclama su propiedad: Cloudflare R2 (`<account>.r2.cloudflarestorage.com`, `pub-<hash>.r2.dev`), Amazon S3 (`s3.amazonaws.com` y `s3.<region>.amazonaws.com`, ya sea en la forma de estilo de ruta o en la forma con prefijo `<bucket>.`), Azure Blob Storage (`<account>.blob.core.windows.net`) y Alibaba Cloud OSS (`<bucket>.oss-<region>.aliyuncs.com`, incluido el endpoint `oss-accelerate`). Esos son endpoints de almacenamiento de objetos específicamente: un endpoint de propósito general en el mismo dominio del proveedor, como un desencadenador de Alibaba Function Compute, no está en la lista y se rechaza. LO QUE SE COMPARA ES LA FORMA DEL NOMBRE DE HOST, NO EL PROVEEDOR: así que nombrar un proveedor arriba NO significa que se acepte cada URL que ese proveedor pueda emitir, y tres casos que casi coinciden merecen mencionarse directamente porque quien llama puede llegar razonablemente con cada uno de ellos. Un DOMINIO PERSONALIZADO de R2 (`cdn.example.com`) NO se acepta: Cloudflare documenta `pub-<hash>.r2.dev` como un nombre de host de depuración con límite de velocidad y dirige el tráfico de producción a un dominio personalizado en su lugar, pero un dominio personalizado no lleva nada en su nombre de host que lo identifique como R2, así que Router no puede distinguirlo de cualquier otro host y lo rechaza: prefirma el endpoint `<account>.r2.cloudflarestorage.com` o usa la forma `pub-<hash>.r2.dev`. El endpoint dualstack IPv6 de S3 (`s3.dualstack.<region>.amazonaws.com`) tampoco se acepta; usa el endpoint regional simple. Tampoco se acepta la zona DNS alternativa de Azure Blob (`<account>.z<N>.blob.storage.azure.net`); usa `<account>.blob.core.windows.net`. El rechazo que recibes nombra estas mismas formas, así que no tienes que venir aquí a leerlas. Los marcadores de posición `<account>` y `pub-<hash>` anteriores muestran la forma con la que normalmente llegarás; no son una restricción de profundidad. La coincidencia se hace sobre el sufijo de dominio del almacenamiento de objetos, así que un nombre más profundo bajo el mismo espacio de nombres (`a.b.pub-<hash>.r2.dev`) también se acepta. Lo que NO se amplía con eso es el espacio de nombres en sí: el sufijo todavía tiene que ser uno de los enumerados. El ejemplo de abajo solo muestra la forma: un valor real también lleva los parámetros de consulta de firma, que se omiten deliberadamente aquí porque un ejemplo publicado vive en la especificación para siempre y una firma real es a la vez una credencial filtrada y un enlace que deja de funcionar. Cada imagen tiene un límite de 25 MiB y las imágenes de una solicitud tienen un límite de 64 MiB en total. La única excepción es ideogram/ideogram-4-5 Precise Edit (una llamada que envía `image`) donde `context_window` está disponible: allí cada imagen puede ser de hasta 50 MB (50,000,000 bytes) y 67,108,864 píxeles, y las imágenes de una solicitud de hasta 128 MiB en total.

model

string

El modelo gpt-image que se va a ejecutar. Router inserta el id del modelo al que se apunta, así que quien llama a /v2/models/openai/gpt-image-2.6-flare no envía esto.

moderation

string

Ajuste de moderación de contenidoValores posibles: `low`, `auto`

n

integer

El número de imágenes a generar (1-10). Una solicitud de GIF (consulta `output_format`) rechaza cualquier valor distinto de 1: la propia descripción de OpenAI llama a `n` en una solicitud de GIF «el número de animaciones», que Router no tarifica para v1.Alcance: `1` a `10`

output_compression

integer

Nivel de compresión para JPEG o WebP (0-100). Se rechaza en una solicitud de GIF: OpenAI no acepta un nivel de compresión para una salida animada.Alcance: `0` a `100`

output_format

string

Formato de la imagen de salida. `gif` además rechaza `image` (las ediciones de GIF aún no están disponibles), `n` distinto de 1, un `size` distinto de 512x512 (incluidos los casos de campo omitido, `auto`, valor malformado o tamaños bien formados como 1024x1024), `stream: true`, `partial_images` mayor que 0 y `output_compression` (consulta la descripción de cada campo), y se rechaza de plano a menos que Comfy lo haya habilitado para este entorno. Una `mask` en una generación de GIF (sin `image`) se elimina en lugar de rechazarse; consulta `mask`.Valores posibles: `png`, `webp`, `jpeg`, `gif`

partial_images

integer

Solo tiene sentido junto con un flujo en vivo, que esta superficie no puede servir, exactamente como en OpenAIImageRouterRequest: consulta la descripción de ese campo. Un valor mayor que 0 se rechaza en una solicitud de GIF, por la misma razón que `stream: true`; 0 se acepta.Alcance: `0` a `3`

prompt

string

requerido

Una descripción de texto de la imagen a generar, o de la edición que se hará a `image`.

quality

string

La calidad de la imagen generada o editada. `xhigh` y `max` son los dos niveles para los que se añadieron gpt-image-2.5-flare y gpt-image-2.5-sunburst; `standard` y `hd` son grafías de la era dall-e que ningún modelo admitido interpreta.Valores posibles: `auto`, `low`, `medium`, `high`, `xhigh`, `max`, `standard`, `hd`

size

string

Tamaño de la imagen (p. ej., 1024x1024, 1536x1024, auto). Una solicitud de GIF (consulta `output_format`) solo admite 512x512 y rechaza omitir este campo, `auto`, un valor malformado y cualquier otro tamaño bien formado (incluido 1024x1024): un tamaño explícito de 512x512 es lo que mantiene finitos la cotización previa y el límite de resultado de 64 MiB antes de un recuento de fotogramas que los multiplica.

stream

boolean

Se declara para que quien lo envíe no sea rechazado, pero es INERTE en esta superficie exactamente como en OpenAIImageRouterRequest: consulta la descripción de ese campo. `true` se rechaza en una solicitud de GIF (la guía de OpenAI indica que la salida GIF no admite streaming); `false` se acepta.

user

string

Un identificador único para la supervisión de usuarios finales

Generado a partir del esquema que Router sirve en `GET /v2/models/openai/gpt-image-2.6-flare/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

data

object[]

data[].b64_json

string

Datos de imagen codificados en Base64

data[].revised_prompt

string

Prompt revisado

data[].url

string

URL de la imagen

usage

object

usage.input_tokens

integer

usage.input_tokens_details

object

usage.input_tokens_details.image_tokens

integer

usage.input_tokens_details.text_tokens

integer

usage.output_tokens

integer

usage.output_tokens_details

object

usage.output_tokens_details.image_tokens

integer

usage.output_tokens_details.text_tokens

integer

usage.total_tokens

integer

background

string

Indica si el fondo de la imagen generada es `opaque` o `transparent`, tal como OpenAI lo resolvió para esta generación. El parámetro de la solicitud tiene `auto` por defecto, así que aquí es donde quien no lo ancló se entera de cuál se produjo.

created

integer

Marca de tiempo Unix, en segundos, de cuándo se completó la generación. Es el único miembro que OpenAI declara REQUIRED en una respuesta de generación de imágenes, así que está presente siempre que OpenAI sea el productor; una respuesta servida por fal, minimax, wavespeed o runware en cualquiera de los ids respaldados por alternativas lo omite por completo, igual que los otros cuatro miembros de parámetros resueltos. Se declara `int64` porque un valor de época de la actualidad está lo bastante cerca de 2^31 como para que un `integer` sin formato genere un campo de 32 bits en muchos generadores de SDK.Formato: `int64`

output_format

string

La codificación de los bytes en `data[].b64_json`: `png`, `webp` o `jpeg`. Es el formato que OpenAI realmente codificó, que es el `output_format` de la solicitud cuando se envió uno y `png` cuando no se envió ninguno, así que un decodificador puede basarse en él en lugar de volver a derivar el formato a partir de la solicitud.

quality

string

El nivel de calidad al que realmente se ejecutó la generación. OpenAI informa uno de `low`, `medium`, `high`, `xhigh` o `max`. Es el nivel RESUELTO, no un eco de la solicitud, cuyo propio `quality` tiene `auto` por defecto.

size

string

Las dimensiones en píxeles a las que realmente se ejecutó la generación, con el formato `<width>x<height>`. Es el tamaño RESUELTO: el `size` de la solicitud tiene `auto` por defecto y admite `auto` de forma explícita, así que este es el único lugar donde se informan las dimensiones que realmente se usaron.

## Ejemplos

### Entrada
    
    
    {
      "prompt": "a rocketship on a launchpad",
      "quality": "low",
      "size": "1024x1024"
    }
    

### Salida
    
    
    {
      "created": 1767225600,
      "data": [
        {
          "b64_json": "PGJhc2U2ND4="
        }
      ],
      "usage": {
        "input_tokens": 12,
        "input_tokens_details": {
          "image_tokens": 0,
          "text_tokens": 12
        },
        "output_tokens": 1056,
        "total_tokens": 1068
      }
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/openai/gpt-image-2-6-flare/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/openai/gpt-image-2-6-flare/code)

[GPT Image 2.5 Sunburst](https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code)[GPT Image 2.6 Sunburst](https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-6-sunburst/code)
