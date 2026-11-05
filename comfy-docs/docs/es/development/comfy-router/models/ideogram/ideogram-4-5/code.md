---
url: https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-4-5/code/
title: Usa Ideogram 4.5 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-05T15:16:36.232294+00:00
---

# Usa Ideogram 4.5 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-4-5/code/

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



Ideogram

# Usa Ideogram 4.5 con Comfy Router

Copiar páginaCopiar página

Llama a ideogram/ideogram-4-5 desde Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `ideogram/ideogram-4-5`, servida por Comfy Router de Ideogram. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `ideogram/ideogram-4-5` **Endpoint:** `POST https://api.comfy.org/v2/models/ideogram/ideogram-4-5`

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
            "ideogram/ideogram-4-5",
            {
                "prompt": "A poster for a jazz festival, bold typography, warm colours",
                "quality": "low",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("ideogram/ideogram-4-5", {
      prompt: "A poster for a jazz festival, bold typography, warm colours",
      quality: "low",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/ideogram/ideogram-4-5 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A poster for a jazz festival, bold typography, warm colours\", \"quality\": \"low\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/ideogram/ideogram-4-5/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "ideogram/ideogram-4-5",
                {
                    "prompt": "A poster for a jazz festival, bold typography, warm colours",
                    "quality": "low",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("ideogram/ideogram-4-5", {
      prompt: "A poster for a jazz festival, bold typography, warm colours",
      quality: "low",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló genera un rechazo aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-4-5/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A poster for a jazz festival, bold typography, warm colours\", \"quality\": \"low\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ideogram/ideogram-4-5/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-4-5/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

context_window

string

Solo Precise Edit; requiere `image`. La región de la imagen de origen sobre la que trabaja la edición, de modo que una imagen muy grande se puede editar en una zona y devolver a tamaño completo con el resto intacto. `none` (el valor predeterminado) edita la imagen entera. `auto` ajusta una región alrededor de `mask` y requiere una. En caso contrario, envía `y_min,x_min,y_max,x_max` como cuatro bordes de píxel enteros no negativos, con `y_max` mayor que `y_min` y `x_max` mayor que `x_min`, al menos 256 píxeles por lado, una relación de aspecto entre 1:6 y 6:1, y como máximo 4,194,304 píxeles de área. Un valor distinto de `none` en una solicitud sin `image` se rechaza. `context_window` solo se acepta donde la puerta de la ventana de contexto está habilitada; donde no lo está, cualquier valor distinto de `none` se rechaza con 422.

​

enable_copyright_detection

boolean

Activa la detección de derechos de autor posterior a la generación.

​

image

string

Una imagen, ya sea una URL https que Router descarga en nombre de quien llama, o un URI `data:image/<format>;base64,<payload>` que lleva los bytes en línea. Los tipos de imagen aceptados son png, webp y jpeg, y ese conjunto se APLICA al resolver la solicitud en lugar de dejarlo al proveedor: un svg, gif, avif o tiff se rechaza aquí, indicando la imagen enviada, en vez de convertirse en un error del socio a dos saltos de la causa. Prefiere la forma de URL. Un payload base64 se infla aproximadamente 4/3 y el cuerpo completo de la solicitud está limitado a 100 MiB, así que la forma en línea se agota cerca de una imagen de origen de 75 MB; una URL evita ese problema por completo. Los límites de multimedia por imagen y por solicitud que se indican al final de esta descripción son más estrictos que el límite del cuerpo, así que para una imagen de tamaño real son los que encuentras primero. LA URL DEBE RESOLVERSE SIN TUS CREDENCIALES. Router la descarga en el servidor y no envía ninguna credencial de quien llama con la solicitud, así que la forma admitida es una URL prefirmada, es decir, una cuya firma está en la cadena de consulta. Un endpoint autenticado como `/api/assets/{id}/content` responde a Router con 401 en lugar de la imagen; solicita esa URL tú mismo y pasa la URL firmada a la que redirige. LA DESCARGA ESTÁ LIMITADA A UN CONJUNTO NOMBRADO DE HOSTS y no a internet abierto, y la misma lista se vuelve a aplicar a cada salto de redirección además de a la URL enviada: por eso una URL en cualquier otro host, o una que redirija fuera de la lista, se rechaza antes de contactar con ningún proveedor. Hoy esa lista es solo el reparto de assets de Comfy: una URL firmada de `storage.googleapis.com` bajo un bucket de assets de Comfy, que es la forma a la que te redirige `/api/assets/{id}/content`. Un CDN de un socio o un host https normal NO está en la lista. HAY DOS AMPLIACIONES EN DESPLIEGUE Y AMBAS ESTÁN DESACTIVADAS POR DEFECTO HOY. Se publican tras UN solo interruptor y se habilitan juntas, así que considera todo lo siguiente como algo futuro y no como algo sobre lo que construir todavía: pregunta antes de basarte en cualquiera de las dos. La PRIMERA es el bucket en el que `POST /customers/storage` firma tu subida. Hasta que el despliegue llegue a tu entorno, una URL de subida de ese endpoint se rechaza aquí, aunque el bucket sea de Comfy y el host el mismo: así que “subir a Comfy y luego pasar la URL” NO funciona todavía, y la forma que sí funciona es la URL firmada a la que redirige `/api/assets/{id}/content`. La SEGUNDA se HABILITA POR CUENTA y no para todos a la vez, porque el bucket que hay detrás de estos hosts es tuyo y no nuestro: incluso con el interruptor anterior activado, una cuenta que no tenga habilitada la multimedia entrante de terceros recibe un rechazo, y se le indica con esas mismas palabras en lugar de decirle que el host no es compatible. Pide a tu contacto de Comfy que la habilite para tu cuenta. Además admite estos hosts de almacenamiento de objetos de terceros, donde el bucket es tuyo y Router no reclama su propiedad: Cloudflare R2 (`<account>.r2.cloudflarestorage.com`, `pub-<hash>.r2.dev`), Amazon S3 (`s3.amazonaws.com` y `s3.<region>.amazonaws.com`, tanto en la forma de estilo de ruta como en la prefijada con `<bucket>.`), Azure Blob Storage (`<account>.blob.core.windows.net`) y Alibaba Cloud OSS (`<bucket>.oss-<region>.aliyuncs.com`, incluido el endpoint `oss-accelerate`). Son endpoints de almacenamiento de objetos específicamente: un endpoint de propósito general en el mismo dominio del proveedor, como un trigger de Alibaba Function Compute, no está en la lista y se rechaza. LO QUE SE COMPARA ES LA FORMA DEL NOMBRE DE HOST Y NO EL PROVEEDOR: por eso nombrar arriba un proveedor NO significa que se acepte cualquier URL que ese proveedor pueda emitir, y conviene enumerar tres casos casi válidos porque quien llama puede llegar razonablemente con cada uno de ellos. Un DOMINIO PERSONALIZADO de R2 (`cdn.example.com`) NO se acepta: Cloudflare documenta `pub-<hash>.r2.dev` como un nombre de host de depuración con límite de tasa y dirige el tráfico de producción a un dominio personalizado, pero un dominio personalizado no lleva nada en su nombre de host que lo identifique como R2, así que Router no puede distinguirlo de cualquier otro host y lo rechaza: prefirma el endpoint `<account>.r2.cloudflarestorage.com` o usa la forma `pub-<hash>.r2.dev`. El endpoint dualstack IPv6 de S3 (`s3.dualstack.<region>.amazonaws.com`) tampoco se acepta; usa el endpoint regional simple. Tampoco la zona DNS alternativa de Azure Blob (`<account>.z<N>.blob.storage.azure.net`); usa `<account>.blob.core.windows.net`. El rechazo que recibes nombra estas mismas formas, así que no tienes que venir aquí a leerlas. Los marcadores `<account>` y `pub-<hash>` de arriba muestran la forma con la que llegarás normalmente; no son una restricción de profundidad. La comparación es sobre el sufijo de dominio del almacenamiento de objetos, así que también se acepta un nombre más profundo bajo el mismo espacio de nombres (`a.b.pub-<hash>.r2.dev`). Lo que NO se amplía con eso es el espacio de nombres en sí: el sufijo todavía tiene que ser uno de los listados. El ejemplo siguiente muestra solo la forma: un valor real además lleva los parámetros de consulta de firma, que aquí se omiten deliberadamente porque un ejemplo publicado permanece en la especificación para siempre y una firma real es a la vez una credencial filtrada y un enlace que deja de funcionar. Cada imagen está limitada a 25 MiB y las imágenes de una solicitud a 64 MiB en total. La única excepción es Precise Edit de ideogram/ideogram-4-5 (una llamada que envía `image`) cuando `context_window` está disponible: ahí cada imagen puede llegar a 50 MB (50,000,000 bytes) y 67,108,864 píxeles, y las imágenes de una solicitud a 128 MiB en total.

​

images

string[]

Imágenes de origen opcionales para la operación de generar. La primera es la fuente principal y el resto son referencias. Hasta cinco, o cuatro con una máscara.

​

magic_prompt

string

Solo para generar. Reescritura de prompts para texto a imagen. Los valores admitidos son auto, on y off. El valor predeterminado es auto.

​

mask

string

Una imagen, ya sea una URL https que Router descarga en nombre de quien llama, o un URI `data:image/<format>;base64,<payload>` que lleva los bytes en línea. Los tipos de imagen aceptados son png, webp y jpeg, y ese conjunto se APLICA al resolver la solicitud en lugar de dejarlo al proveedor: un svg, gif, avif o tiff se rechaza aquí, indicando la imagen enviada, en vez de convertirse en un error del socio a dos saltos de la causa. Prefiere la forma de URL. Un payload base64 se infla aproximadamente 4/3 y el cuerpo completo de la solicitud está limitado a 100 MiB, así que la forma en línea se agota cerca de una imagen de origen de 75 MB; una URL evita ese problema por completo. Los límites de multimedia por imagen y por solicitud que se indican al final de esta descripción son más estrictos que el límite del cuerpo, así que para una imagen de tamaño real son los que encuentras primero. LA URL DEBE RESOLVERSE SIN TUS CREDENCIALES. Router la descarga en el servidor y no envía ninguna credencial de quien llama con la solicitud, así que la forma admitida es una URL prefirmada, es decir, una cuya firma está en la cadena de consulta. Un endpoint autenticado como `/api/assets/{id}/content` responde a Router con 401 en lugar de la imagen; solicita esa URL tú mismo y pasa la URL firmada a la que redirige. LA DESCARGA ESTÁ LIMITADA A UN CONJUNTO NOMBRADO DE HOSTS y no a internet abierto, y la misma lista se vuelve a aplicar a cada salto de redirección además de a la URL enviada: por eso una URL en cualquier otro host, o una que redirija fuera de la lista, se rechaza antes de contactar con ningún proveedor. Hoy esa lista es solo el reparto de assets de Comfy: una URL firmada de `storage.googleapis.com` bajo un bucket de assets de Comfy, que es la forma a la que te redirige `/api/assets/{id}/content`. Un CDN de un socio o un host https normal NO está en la lista. HAY DOS AMPLIACIONES EN DESPLIEGUE Y AMBAS ESTÁN DESACTIVADAS POR DEFECTO HOY. Se publican tras UN solo interruptor y se habilitan juntas, así que considera todo lo siguiente como algo futuro y no como algo sobre lo que construir todavía: pregunta antes de basarte en cualquiera de las dos. La PRIMERA es el bucket en el que `POST /customers/storage` firma tu subida. Hasta que el despliegue llegue a tu entorno, una URL de subida de ese endpoint se rechaza aquí, aunque el bucket sea de Comfy y el host el mismo: así que “subir a Comfy y luego pasar la URL” NO funciona todavía, y la forma que sí funciona es la URL firmada a la que redirige `/api/assets/{id}/content`. La SEGUNDA se HABILITA POR CUENTA y no para todos a la vez, porque el bucket que hay detrás de estos hosts es tuyo y no nuestro: incluso con el interruptor anterior activado, una cuenta que no tenga habilitada la multimedia entrante de terceros recibe un rechazo, y se le indica con esas mismas palabras en lugar de decirle que el host no es compatible. Pide a tu contacto de Comfy que la habilite para tu cuenta. Además admite estos hosts de almacenamiento de objetos de terceros, donde el bucket es tuyo y Router no reclama su propiedad: Cloudflare R2 (`<account>.r2.cloudflarestorage.com`, `pub-<hash>.r2.dev`), Amazon S3 (`s3.amazonaws.com` y `s3.<region>.amazonaws.com`, tanto en la forma de estilo de ruta como en la prefijada con `<bucket>.`), Azure Blob Storage (`<account>.blob.core.windows.net`) y Alibaba Cloud OSS (`<bucket>.oss-<region>.aliyuncs.com`, incluido el endpoint `oss-accelerate`). Son endpoints de almacenamiento de objetos específicamente: un endpoint de propósito general en el mismo dominio del proveedor, como un trigger de Alibaba Function Compute, no está en la lista y se rechaza. LO QUE SE COMPARA ES LA FORMA DEL NOMBRE DE HOST Y NO EL PROVEEDOR: por eso nombrar arriba un proveedor NO significa que se acepte cualquier URL que ese proveedor pueda emitir, y conviene enumerar tres casos casi válidos porque quien llama puede llegar razonablemente con cada uno de ellos. Un DOMINIO PERSONALIZADO de R2 (`cdn.example.com`) NO se acepta: Cloudflare documenta `pub-<hash>.r2.dev` como un nombre de host de depuración con límite de tasa y dirige el tráfico de producción a un dominio personalizado, pero un dominio personalizado no lleva nada en su nombre de host que lo identifique como R2, así que Router no puede distinguirlo de cualquier otro host y lo rechaza: prefirma el endpoint `<account>.r2.cloudflarestorage.com` o usa la forma `pub-<hash>.r2.dev`. El endpoint dualstack IPv6 de S3 (`s3.dualstack.<region>.amazonaws.com`) tampoco se acepta; usa el endpoint regional simple. Tampoco la zona DNS alternativa de Azure Blob (`<account>.z<N>.blob.storage.azure.net`); usa `<account>.blob.core.windows.net`. El rechazo que recibes nombra estas mismas formas, así que no tienes que venir aquí a leerlas. Los marcadores `<account>` y `pub-<hash>` de arriba muestran la forma con la que llegarás normalmente; no son una restricción de profundidad. La comparación es sobre el sufijo de dominio del almacenamiento de objetos, así que también se acepta un nombre más profundo bajo el mismo espacio de nombres (`a.b.pub-<hash>.r2.dev`). Lo que NO se amplía con eso es el espacio de nombres en sí: el sufijo todavía tiene que ser uno de los listados. El ejemplo siguiente muestra solo la forma: un valor real además lleva los parámetros de consulta de firma, que aquí se omiten deliberadamente porque un ejemplo publicado permanece en la especificación para siempre y una firma real es a la vez una credencial filtrada y un enlace que deja de funcionar. Cada imagen está limitada a 25 MiB y las imágenes de una solicitud a 64 MiB en total. La única excepción es Precise Edit de ideogram/ideogram-4-5 (una llamada que envía `image`) cuando `context_window` está disponible: ahí cada imagen puede llegar a 50 MB (50,000,000 bytes) y 67,108,864 píxeles, y las imágenes de una solicitud a 128 MiB en total.

​

num_images

integer

predeterminado:"1"

Número de imágenes a devolver. Cada una se factura.Rango: `1` a `8`

​

prompt

string

requerido

La instrucción o descripción de la imagen, de 1 a 10,000 caracteres.

​

quality

string

Nivel de calidad, que también es la tarifa facturada. Con imágenes de origen: very_low, low, medium o high (predeterminado medium). Sin imágenes de origen: low, medium o high (predeterminado high); very_low en una solicitud de texto a imagen se rechaza.Valores posibles: `very_low`, `low`, `medium`, `high`

​

reference_images

string[]

Imágenes de referencia opcionales para Precise Edit; requiere `image`. Hasta cuatro, o tres con una máscara.

​

seed

integer

Semilla para obtener resultados reproducibles.Rango: `0` a `2147483647`

​

size

string

Solo para generar. Tamaño de salida: auto (predeterminado), source (requiere images) o WIDTHxHEIGHT. Omítelo cuando envíes una máscara; se rechaza una solicitud que especifique ambos.

Generado a partir del esquema que Router publica en `GET /v2/models/ideogram/ideogram-4-5/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

data

object[]

Las imágenes generadas.

​

data[].is_image_safe

boolean

Indica si la imagen se considera segura. Usa solo las imágenes en las que este valor sea verdadero.

​

data[].prompt

string

El prompt usado para generar esta imagen.

​

data[].resolution

string

La resolución de la imagen generada.

​

data[].seed

integer

La semilla usada para esta imagen.

​

data[].url

string

URL de la imagen generada.

​

generation_id

string

El identificador de la generación.

​

seed

integer

La semilla usada para la generación.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "prompt": "A poster for a jazz festival, bold typography, warm colours",
      "quality": "low"
    }
    

### 

​

Salida
    
    
    {
      "data": [
        {
          "is_image_safe": true,
          "prompt": "A poster for a jazz festival, bold typography, warm colours",
          "resolution": "2048x2048",
          "seed": 918273645,
          "url": "https://example.invalid/ideogram/ideogram-4-5/generated.png"
        }
      ],
      "generation_id": "gen_0123456789",
      "seed": 918273645
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/ideogram/ideogram-4-5/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/ideogram/ideogram-4-5/code)

[Higgsfield Kling 3 Pro](https://docs.comfy.org/es/development/comfy-router/models/higgsfield/higgsfield-kling-3-pro/code)[Ideogram V3](https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v3/code)
