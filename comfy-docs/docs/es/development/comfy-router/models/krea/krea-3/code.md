---
url: https://docs.comfy.org/es/development/comfy-router/models/krea/krea-3/code/
title: Usa Krea 3 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-19T16:26:10.712981+00:00
---

# Usa Krea 3 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/krea/krea-3/code/

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



Krea

# Usa Krea 3 con Comfy Router

Copiar páginaCopiar página

Llama a krea/krea-3 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API de `krea/krea-3`, servida por Comfy Router de Krea. **Entrada:** texto, imagen · **Salida:** imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `krea/krea-3` **Endpoint:** `POST https://api.comfy.org/v2/models/krea/krea-3`

  * Esperar el resultado

  * Encolar y recoger después




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "krea/krea-3",
            {
                "prompt": "A ceramic coffee mug on a clean studio background",
                "resolution": "1k",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("krea/krea-3", {
      prompt: "A ceramic coffee mug on a clean studio background",
      resolution: "1k",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/krea/krea-3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A ceramic coffee mug on a clean studio background\", \"resolution\": \"1k\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/krea/krea-3/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "krea/krea-3",
                {
                    "prompt": "A ceramic coffee mug on a clean studio background",
                    "resolution": "1k",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que necesita otro proceso
    
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
    const handle = await comfy.models.submit("krea/krea-3", {
      prompt: "A ceramic coffee mug on a clean studio background",
      resolution: "1k",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/krea/krea-3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A ceramic coffee mug on a clean studio background\", \"resolution\": \"1k\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/krea/krea-3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/krea/krea-3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

aspect_ratio

string

1:1, 4:5, 3:4, 2:3, 9:16, 5:4, 4:3, 3:2, 16:9 o 21:9. Úsalo junto con resolution; omítelo para el encuadre automático.

image_urls

string[]

URL de imágenes de entrada, hasta 8. Más de 8 entradas se rechazan antes de hacer ninguna obtención (400 en /proxy/krea; la comprobación del esquema de Comfy Router responde primero con 422). El image_url que devuelve subir la imagen a POST /proxy/krea/assets (campo `file` del formulario multipart) siempre se acepta. Que se acepten otras URL https públicas depende del entorno: donde no se aceptan, cualquier enlace que no sea una URL https en el host app-uploads.krea.ai se rechaza con 400 y el mensaje ‘image_urls must be image_url values returned by POST /proxy/krea/assets’, así que sube la imagen en su lugar; donde sí se aceptan, se acepta cualquier URL de imagen https pública, y una URL malformada o que no sea https se rechaza con 400 (una URL cuyo puerto sea numérico pero esté fuera de rango no la detecta esta comprobación y puede fallar con 502 en su lugar). En ese caso, una solicitud con cualquier entrada de image_urls que no sea un enlace de app-uploads.krea.ai (una URL https pública, o un URI data: en base64 donde se acepten) también se rechaza con 400 antes de cualquier obtención, salvo que todo el cuerpo de la solicitud se envíe como application/json en lugar de multipart, sea UTF-8 válido, tenga como máximo 25100288 bytes y solo lleve los campos que declara este esquema. Para una URL https bien formada en ese caso, una referencia que quien llama puede corregir se rechaza con 400 indicando su host: su host no resuelve o no es accesible públicamente cuando se comprueba antes de la obtención, redirige más veces de las permitidas, a una URL que no es https o a un host que no es accesible públicamente, devuelve un 4xx distinto de 408 o 429, no es una imagen, es una imagen en un formato que no se puede leer, su cabecera de tamaño de imagen no está dentro de los primeros 2 MiB, o una respuesta sin longitud declarada o con codificación chunked termina antes de su cabecera de tamaño de imagen. Cualquier otro fallo al obtenerla produce un error 502 en POST /proxy/krea (Comfy Router responde con 500 internal_error): un fallo transitorio de DNS, TLS o conexión, un timeout, un 408, 429, 5xx u otro estado distinto de 200 del origen, o un host que pasó esa comprobación pero no resuelve o no es accesible públicamente cuando la obtención establece la conexión. Algunos de estos se resuelven al reintentar (un error del resolver, un timeout, una conexión interrumpida, un origen que responde 5xx, 408 o 429, o un host cuya respuesta DNS cambia a una dirección no pública entre la comprobación del host y la conexión, que al reintentar puede tener éxito o recibir el 400 por un host no público); otros fallan de la misma manera siempre, por ejemplo un certificado TLS en el que la obtención no confía (autofirmado, caducado o para el nombre de host incorrecto), o un origen que responde un 2xx distinto de 200 o un 3xx que la obtención no sigue (como 204, 206, 300, 304 o 305, o un 301, 302, 303, 307 o 308 sin Location), así que si un reintento falla de la misma manera, sube la imagen en su lugar. Una solicitud en cola a través de Comfy Router no reintenta ese fallo cuando alguno de sus image_urls no es un enlace de app-uploads.krea.ai, así que reenvíala tú mismo si la causa puede desaparecer. Donde no se aceptan otras URL, un enlace de app-uploads.krea.ai que no sea una carga activa falla con un error 5xx; donde sí se aceptan, se rechaza con 400 como cualquier otra referencia inaccesible. Mientras un servidor aún no haya aprendido cuál se aplica, cualquier URL https cuyo host no sea un enlace de app-uploads.krea.ai, sea público o no, falla con un error 503 que puedes reintentar sin riesgo (una solicitud en cola se reintenta automáticamente ante él). El 400 de una solicitud en cola solo lleva el detalle genérico invalid_input, así que no muestra ni el host ni el texto anterior, y la cola no lo reintenta. Un 400 en cola puede venir de cualquier campo, no solo de image_urls (por ejemplo, una resolution o un thinking_mode no compatibles), así que revisa primero los demás campos. Si son válidos, sube cada imagen a POST /proxy/krea/assets y reenvía con esos valores image_url y una nueva Idempotency-Key (o ninguna): reutilizar la clave con un cuerpo modificado se rechaza con 409 invalid_input, que no dice nada sobre las imágenes, y reutilizarla con el mismo cuerpo se responde con 201 junto con el request_id original e Idempotent-Replayed: true, así que no inicia una nueva ejecución, y su URL de resultado devuelve el mismo 400 (su URL de estado responde 200 con error_type invalid_input). Donde se aceptan otras URL https públicas, si ese reenvío también falla con 400, el problema es la propia imagen (por ejemplo, no es una imagen compatible o su cabecera de tamaño de imagen no está dentro de los primeros 2 MiB). Donde no se aceptan, esa misma imagen subida falla con un 5xx (500 internal_error en Comfy Router) en lugar de ese 400, y el problema sigue siendo la imagen, así que volver a subirla no ayuda. Solo se leen los primeros 2 MiB de cada imagen para encontrar su tamaño, así que una imagen cuya información de tamaño no se pueda leer dentro de esa ventana (como un JPEG con más de 2 MiB de metadatos incrustados, o un PNG con paleta en el que los datos de transparencia, o si no los hay, el inicio de su primer chunk de datos de imagen, estén más allá de 2 MiB, por ejemplo después de más de 2 MiB de chunks de texto o de perfil de color) se rechaza con 400 indicando que su cabecera de tamaño de imagen no está dentro de los primeros 2 MiB, se haya subido o no; vuelve a guardarla sin los metadatos grandes, o guarda un PNG con paleta como un PNG sin paleta. Envía un host internacionalizado en su forma ASCII (punycode); un nombre de host no ASCII se rechaza por no existir. Omítelo para texto a imagen.

model

string

berry (predeterminado, calidad) o jam (velocidad).

negative_prompt

string

prompt

string

requerido

Qué generar. Con image_urls, la instrucción de edición; describe qué debe cambiar y qué debe permanecer igual.

regional_edit

boolean

Establécelo en true para una edición local que mantenga el resto de la imagen. Requiere el modelo berry y al menos una imagen en image_urls.

resolution

string

requerido

1k o 2k.

seed

integer

thinking_mode

string

fast (predeterminado), high o ultra. High y ultra planifican las ediciones complejas con más detalle y tardan más. Ultra requiere resolution 2k.

Generado a partir del esquema que Router expone en `GET /v2/models/krea/krea-3/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

completed_at

string (date-time)

requerido

Formato: `date-time`

created_at

string (date-time)

requerido

Formato: `date-time`

error

object

Solo se define cuando el estado es failed. Una tarea cancelada no lo incluye.

error.code

string

requerido

Por qué falló la tarea: content_policy, invalid_request, validation_failed, model_unavailable, insufficient_balance, timeout, auto_cancelled, provider_error, internal o node_app_node_failed. Trata un código desconocido como internal.

error.message

string

Opcional. Texto libre del proveedor para provider_error e internal.

error.param

string

El parámetro de la solicitud que debes cambiar, presente con invalid_request y validation_failed.

job_id

string (uuid)

requerido

Formato: `uuid`

result

object

requerido

La generación finalizada. Aquí no admite nulo, a diferencia de `KreaJob`: si una tarea terminal tiene un `result` sin `urls`, se responde con un error de Comfy Router, así que una respuesta `200` siempre lo incluye.

result.style_id

string

Lo establecen las tareas de loraTraining, no una generación; una respuesta `200` de estos modelos lleva `urls`.

result.urls

string (uri)[]

requerido

Las imágenes generadas, como enlaces descargables. Al menos uno, porque una tarea `completed` con `urls` vacío es `success_without_output` y nunca llega a este documento.

status

string

requerido

Siempre es `completed` en este documento: es el único estado que Router reporta como éxito, y el vocabulario de Krea se compara sin distinción de mayúsculas y minúsculas.Valores posibles: `completed`

## Ejemplos

### Entrada
    
    
    {
      "prompt": "A ceramic coffee mug on a clean studio background",
      "resolution": "1k"
    }
    

### Salida
    
    
    {
      "completed_at": "2027-01-01T00:00:37Z",
      "created_at": "2027-01-01T00:00:00Z",
      "job_id": "7f1c2e84-5b90-4a37-8d61-2c0f9ab4e153",
      "result": {
        "urls": [
          "https://example.invalid/krea/krea-2/generated.png"
        ]
      },
      "status": "completed"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/krea/krea-3/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/krea/krea-3/code)

[Krea 2](https://docs.comfy.org/es/development/comfy-router/models/krea/krea-2/code)[LTX 2.5 Fast](https://docs.comfy.org/es/development/comfy-router/models/ltx/ltx-2-5-fast/code)
