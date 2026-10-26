---
url: https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code/
title: Usa GPT Image 2.5 Sunburst con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:15.249264+00:00
---

# Usa GPT Image 2.5 Sunburst con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code/

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

# Usa GPT Image 2.5 Sunburst con Comfy Router

Copiar páginaCopiar página

Llama a openai/gpt-image-2.5-sunburst a través de Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `openai/gpt-image-2.5-sunburst`, servida por Comfy Router desde OpenAI. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `openai/gpt-image-2.5-sunburst` **Endpoint:** `POST https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst`

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
            "openai/gpt-image-2.5-sunburst",
            {
                "prompt": "a rocketship on a launchpad",
                "quality": "low",
                "size": "1024x1024",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("openai/gpt-image-2.5-sunburst", {
      prompt: "a rocketship on a launchpad",
      quality: "low",
      size: "1024x1024",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a rocketship on a launchpad\", \"quality\": \"low\", \"size\": \"1024x1024\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica cómo consultar el estado, cancelar y recoger el resultado.

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
                "openai/gpt-image-2.5-sunburst",
                {
                    "prompt": "a rocketship on a launchpad",
                    "quality": "low",
                    "size": "1024x1024",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
            # Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
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
    const handle = await comfy.models.submit("openai/gpt-image-2.5-sunburst", {
      prompt: "a rocketship on a launchpad",
      quality: "low",
      size: "1024x1024",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a rocketship on a launchpad\", \"quality\": \"low\", \"size\": \"1024x1024\"}"
    
    # 2. Consulta el estado hasta que sea COMPLETED, esperando los segundos de Retry-After que indique cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Proveedores de servicio

Comfy Router sirve este modelo directamente a menos que la solicitud indique otro proveedor. Los proveedores a continuación también lo sirven, en el mismo endpoint y con el mismo ID de modelo, seleccionados con el parámetro de consulta `model_provider`.

  * **Comfy** (predeterminado): `POST https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst`
  * **fal** , como `fal/fal-gpt-image-2.5-sunburst`: `POST https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst?model_provider=fal`
  * **Runware** , como `runware/runware-gpt-image-2.5-sunburst`: `POST https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst?model_provider=runware`
  * **WaveSpeed** , como `wavespeed/wavespeed-gpt-image-2.5-sunburst`: `POST https://api.comfy.org/v2/models/openai/gpt-image-2.5-sunburst?model_provider=wavespeed`

`strict_mode` tiene como valor predeterminado falso, por lo que Router traduce el cuerpo de la solicitud nativo documentado en esta página al esquema propio del proveedor y traduce la respuesta de vuelta. Consulta [`model_provider`, `strict_mode` y `fallback_provider`](https://docs.comfy.org/es/development/comfy-router/reference#post-v2modelsprovidermodel) en la referencia de la API, y [Proveedores de servicio](https://docs.comfy.org/es/development/comfy-router/providers) para cada modelo enrutado de esta manera.

## 

​

Esquema

### 

​

Entrada

​

background

string

Transparencia del fondo. `auto` deja que el modelo elija.Valores posibles: `transparent`, `opaque`, `auto`

​

image

string | string[]

La imagen o imágenes de origen que quieres editar. LA PRESENCIA DE ESTE CAMPO SELECCIONA LA OPERACIÓN DE EDICIÓN: omítelo por completo para la generación de texto a imagen. El ejemplo publicado del modelo es la llamada de GENERACIÓN, que omite este campo. Agregar `image` es toda la diferencia entre los dos modos (mismo endpoint, mismo id de modelo), salvo que un prompt de edición describe el CAMBIO que quieres y no la escena, así que el cuerpo de edición de abajo se lee distinto del ejemplo de generación aunque solo este campo sea estructuralmente nuevo. Puedes copiarlo tal cual está impreso: `{"prompt": "give the rocketship rainbow coloring", "image": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="], "size": "1024x1024"}`. El payload es un PNG 1x1 completo, no una abreviatura, y este cuerpo está fijado como caso aceptado en las propias pruebas de validación de solicitudes de Router. Sustituye los bytes por los de tu propia imagen. Acepta una imagen o un arreglo de ellas; gpt-image-1 y posteriores aceptan hasta 16, y Router lo aplica desde este esquema antes de despachar.

​

mask

string

Una imagen, ya sea como una URL https que Router obtiene en nombre de quien llama, o como un URI `data:image/<format>;base64,<payload>` que lleva los bytes en línea. Los tipos de imagen aceptados son png, webp y jpeg, y ese conjunto se APLICA en el momento de la resolución en lugar de dejarlo al proveedor: un svg, gif, avif o tiff se rechaza aquí, nombrando la imagen que enviaste, en vez de convertirse en un error de socio a dos saltos de la causa. Prefiere la forma con URL. Un payload base64 se infla aproximadamente 4/3 y el cuerpo completo de la solicitud tiene un límite de 100 MiB, así que la forma en línea llega como máximo a una imagen de origen de unos 75 MB; una URL evita eso por completo. Los límites de medios por imagen y por solicitud indicados al final de esta descripción son más estrictos que el límite del cuerpo, así que para una imagen de cualquier tamaño real son los que encuentras primero. LA URL DEBE RESOLVERSE SIN TUS CREDENCIALES. Router la obtiene del lado del servidor y no envía ninguna credencial de quien llama con la solicitud, así que una URL prefirmada (aquella cuya firma está en la cadena de consulta) es la forma admitida. Un endpoint autenticado como `/api/assets/{id}/content` responde a Router con 401 en lugar de la imagen; solicita tú mismo esa URL y pasa la URL firmada a la que redirige. LA OBTENCIÓN ESTÁ LIMITADA A UN CONJUNTO NOMBRADO DE HOSTS en lugar de a internet abierta, y la misma lista se vuelve a aplicar a cada salto de redirección y también a la URL que envías; por eso una URL en cualquier otro host, o una que redirija fuera de la lista, se rechaza antes de contactar a ningún proveedor. Hoy esa lista es únicamente la entrega de recursos de Comfy: una URL firmada de `storage.googleapis.com` dentro de un bucket de recursos de Comfy, que es la forma a la que `/api/assets/{id}/content` te redirige. Un CDN de socio o un host https simple NO está en la lista. SE ESTÁN DESPLEGANDO DOS AMPLIACIONES Y HOY AMBAS ESTÁN DESACTIVADAS POR DEFECTO. Se publican detrás de UN único interruptor y se habilitan juntas, así que trata todo lo siguiente como algo próximo y no como algo sobre lo que construir todavía: pregunta antes de apoyarte en cualquiera de las dos. La PRIMERA es el bucket en el que `POST /customers/storage` firma tu carga. Hasta que el despliegue llegue a tu entorno, una URL de carga de ese endpoint se rechaza aquí, aunque el bucket sea de Comfy y el host sea el mismo; por eso “sube a Comfy y luego pasa la URL” TODAVÍA no funciona, y la forma que sí funciona es la URL firmada a la que redirige `/api/assets/{id}/content`. La SEGUNDA se HABILITA POR CUENTA en lugar de para todos a la vez, porque el bucket detrás de estos hosts es tuyo y no nuestro: incluso con el interruptor anterior activado, una cuenta a la que no se le habilitaron los medios entrantes de terceros se rechaza, y se le dice con esas palabras en lugar de decirle que el host no es compatible. Pide a tu contacto de Comfy que la habilite para tu cuenta. Además, admite estos hosts de almacenamiento de objetos de terceros, donde el bucket es tuyo y Router no reclama ninguna propiedad sobre él: Cloudflare R2 (`<account>.r2.cloudflarestorage.com`, `pub-<hash>.r2.dev`), Amazon S3 (`s3.amazonaws.com` y `s3.<region>.amazonaws.com`, tanto en la forma path-style como en la forma con el prefijo `<bucket>.`), Azure Blob Storage (`<account>.blob.core.windows.net`) y Alibaba Cloud OSS (`<bucket>.oss-<region>.aliyuncs.com`, incluido el endpoint `oss-accelerate`). Son endpoints de almacenamiento de objetos específicamente: un endpoint de propósito general en el mismo dominio del proveedor, como un trigger de Alibaba Function Compute, no está en la lista y se rechaza. LO QUE SE COMPARA ES LA FORMA DEL NOMBRE DE HOST, NO EL PROVEEDOR: por eso nombrar un proveedor arriba NO significa que se acepte toda URL que ese proveedor pueda emitir, y vale la pena enunciar directamente tres casos límite, porque quien llama puede llegar razonablemente con cualquiera de ellos. Un DOMINIO PERSONALIZADO de R2 (`cdn.example.com`) NO se acepta: Cloudflare documenta `pub-<hash>.r2.dev` como un nombre de host de depuración con límite de tasa y dirige el tráfico de producción a un dominio personalizado, pero un dominio personalizado no lleva nada en su nombre de host que lo identifique como R2, así que Router no puede distinguirlo de cualquier otro host y lo rechaza; prefirma el endpoint `<account>.r2.cloudflarestorage.com` o usa la forma `pub-<hash>.r2.dev`. El endpoint dualstack IPv6 de S3 (`s3.dualstack.<region>.amazonaws.com`) tampoco se acepta; usa el endpoint regional simple. Tampoco la zona DNS alternativa de Azure Blob (`<account>.z<N>.blob.storage.azure.net`); usa `<account>.blob.core.windows.net`. El rechazo que recibes nombra estas mismas formas, así que no tienes que venir aquí a leerlas. Los marcadores `<account>` y `pub-<hash>` de arriba muestran la forma con la que normalmente llegarás; no son una restricción de profundidad. La coincidencia se hace sobre el sufijo de dominio del almacenamiento de objetos, así que también se acepta un nombre más profundo bajo el mismo espacio de nombres (`a.b.pub-<hash>.r2.dev`). Lo que NO se amplía con eso es el espacio de nombres en sí: el sufijo sigue teniendo que ser uno de los que aparecen en la lista. El ejemplo de abajo muestra solo la forma: un valor real también lleva los parámetros de consulta de firma, que aquí se omiten a propósito porque un ejemplo publicado vive en la especificación para siempre y una firma real es a la vez una credencial filtrada y un enlace que deja de funcionar. Cada imagen está limitada a 25 MiB y las imágenes de una misma solicitud a 64 MiB en total.

​

model

string

El modelo gpt-image que se va a ejecutar. Router inserta el id del modelo direccionado, así que quien llama a /v2/models/openai/gpt-image-2 no envía este campo.

​

moderation

string

Configuración de moderación de contenidoValores posibles: `low`, `auto`

​

n

integer

El número de imágenes a generar (1-10).Rango: de `1` a `10`

​

output_compression

integer

Nivel de compresión para JPEG o WebP (0-100)Rango: de `0` a `100`

​

output_format

string

Formato de la imagen de salidaValores posibles: `png`, `webp`, `jpeg`

​

partial_images

integer

Solo tiene sentido junto con un stream en vivo, que esta superficie no puede servir: `stream` se fija en `false` incluso cuando lo envías. En una generación, cualquier valor distinto de `0` o `null` se rechaza con un 400, tanto si la solicitud envía también `stream: true` como si no; en una solicitud que lleva `image`, el campo se descarta en lugar de reenviarse. Omítelo.Rango: de `0` a `3`

​

prompt

string

requerido

Una descripción de texto de la imagen que se va a generar, o de la edición que se debe hacer en `image`.

​

quality

string

La calidad de la imagen generada o editada. `xhigh` y `max` son los dos niveles para los que se agregaron gpt-image-2.5-flare y gpt-image-2.5-sunburst; `standard` y `hd` son grafías de la época de dall-e que ningún modelo admitido lee.Valores posibles: `auto`, `low`, `medium`, `high`, `xhigh`, `max`, `standard`, `hd`

​

size

string

Tamaño de la imagen (p. ej., 1024x1024, 1536x1024, auto)

​

stream

boolean

Declarado para que quien lo envíe no sea rechazado, pero INERTE en esta superficie: Router lo FIJA en `false` antes del despacho, porque captura la respuesta del proveedor en lugar de retransmitir un `text/event-stream` (una solicitud que lleva `image` descarta el campo, ya que la edición se recodifica sin él). Ninguna superficie de Comfy sirve el streaming de imágenes parciales de gpt-image: la entrada v1 `POST /proxy/openai/images/generations` rechaza `stream: true` con un 400 y nunca reenvía la solicitud al proveedor, así que omite el campo y lee la respuesta completada como un solo cuerpo JSON. Como el stream nunca se abre, la restricción de OpenAI sobre combinar `stream: true` con `n` mayor que 1 no aplica aquí; `n` se reenvía tal como se envía.

​

user

string

Un identificador único para la supervisión de usuarios finales

Generado a partir del esquema que Router sirve en `GET /v2/models/openai/gpt-image-2.5-sunburst/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

data

object[]

​

data[].b64_json

string

Datos de la imagen codificados en Base64

​

data[].revised_prompt

string

Prompt revisado

​

data[].url

string

URL de la imagen

​

usage

object

​

usage.input_tokens

integer

​

usage.input_tokens_details

object

​

usage.input_tokens_details.image_tokens

integer

​

usage.input_tokens_details.text_tokens

integer

​

usage.output_tokens

integer

​

usage.output_tokens_details

object

​

usage.output_tokens_details.image_tokens

integer

​

usage.output_tokens_details.text_tokens

integer

​

usage.total_tokens

integer

​

background

string

Indica si el fondo de la imagen generada es `opaque` o `transparent`, tal como OpenAI lo resolvió para esta generación. El parámetro de la solicitud tiene `auto` por defecto, así que aquí es donde quien no lo ancló se entera de cuál se produjo.

​

created

integer

Marca de tiempo Unix, en segundos, del momento en que se completó la generación. Es el único miembro que OpenAI declara como REQUIRED en una respuesta de generación de imágenes, por lo que está presente siempre que OpenAI sea el productor; una respuesta servida por fal, pika, wavespeed o runware sobre cualquiera de los ids con respaldo alternativo lo omite por completo, igual que los otros cuatro miembros de parámetros resueltos. Se declara como `int64` porque un valor de época actual está lo bastante cerca de 2^31 como para que un `integer` sin formato genere un campo de 32 bits en muchos generadores de SDK.Formato: `int64`

​

output_format

string

La codificación de los bytes en `data[].b64_json`: `png`, `webp` o `jpeg`. Es el formato que OpenAI codificó realmente, que es el `output_format` de la solicitud cuando se envió uno y `png` cuando no se envió ninguno, de modo que un decodificador puede basarse en él en lugar de volver a deducir el formato a partir de la solicitud.

​

quality

string

El nivel de calidad con el que realmente se ejecutó la generación. OpenAI informa uno de `low`, `medium`, `high`, `xhigh` o `max`. Es el nivel RESUELTO, no un eco de la solicitud, cuyo propio `quality` tiene `auto` por defecto.

​

size

string

Las dimensiones en píxeles con las que realmente se ejecutó la generación, con el formato `<width>x<height>`. Es el tamaño RESUELTO: el `size` de la solicitud tiene `auto` por defecto y admite `auto` de forma explícita, así que este es el único lugar donde se informan las dimensiones realmente usadas.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "prompt": "a rocketship on a launchpad",
      "quality": "low",
      "size": "1024x1024"
    }
    

### 

​

Salida
    
    
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code)

[GPT Image 2.5 Flare](https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-5-flare/code)[GPT Image 2](https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2/code)
