---
url: https://docs.comfy.org/es/development/comfy-router/models/meshy/meshy-n1/code/
title: Usar Meshy N1 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:26.223848+00:00
---

# Usar Meshy N1 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/meshy/meshy-n1/code/

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



Meshy

# Usar Meshy N1 con Comfy Router

Copiar páginaCopiar página

Llama a meshy/meshy-n1 con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `meshy/meshy-n1`, servida por Comfy Router desde Meshy. **Entrada:** Imagen, 3D · **Salida:** 3D

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `meshy/meshy-n1` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/meshy-n1`

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
            "meshy/meshy-n1",
            {
                "image_style_url": "https://example.invalid/meshy/n1/front.png",
                "model_url": "https://cdn.meshy.ai/model/example_model_2.glb",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("meshy/meshy-n1", {
      image_style_url: "https://example.invalid/meshy/n1/front.png",
      model_url: "https://cdn.meshy.ai/model/example_model_2.glb",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/meshy-n1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_style_url\": \"https://example.invalid/meshy/n1/front.png\", \"model_url\": \"https://cdn.meshy.ai/model/example_model_2.glb\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/meshy/meshy-n1/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida del resultado.

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
                "meshy/meshy-n1",
                {
                    "image_style_url": "https://example.invalid/meshy/n1/front.png",
                    "model_url": "https://cdn.meshy.ai/model/example_model_2.glb",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("meshy/meshy-n1", {
      image_style_url: "https://example.invalid/meshy/n1/front.png",
      model_url: "https://cdn.meshy.ai/model/example_model_2.glb",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló provoca aquí un rechazo.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/meshy/meshy-n1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_style_url\": \"https://example.invalid/meshy/n1/front.png\", \"model_url\": \"https://cdn.meshy.ai/model/example_model_2.glb\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/meshy-n1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras todavía se ejecuta.
    curl https://api.comfy.org/v2/models/meshy/meshy-n1/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

ai_model

string

El modelo de Meshy que se va a ejecutar. En la ruta de Comfy Router, este valor lo proporciona la ruta (`/v2/models/meshy/{model}`) y puede omitirse o enviarse como null; Router escribe aquí el modelo de la ruta después de la validación.

enable_original_uv

boolean

Usa el UV original del modelo en lugar de generar UV nuevos.

enable_pbr

boolean

predeterminado:"false"

meshy-n1 no genera mapas PBR, por lo que solo se acepta false.Valores posibles: `false`

image_style_url

string

Una imagen de referencia, usada como vista frontal. Admite jpg, jpeg, png y webp, o un URI de datos base64. No la envíes con multiview_image_urls.

input_task_id

string

El ID de una tarea de Meshy completada cuya malla se va a texturizar. Requerido si no se proporciona model_url.

model_url

string

Una URL de acceso público o un URI de datos que apunte a un modelo 3D. Formatos admitidos: glb, gltf, obj, fbx, stl. Requerido si no se proporciona input_task_id. Como máximo 7,999,999 caras triangulares.

multiview_image_urls

string[]

De una a cuatro imágenes de referencia del mismo objeto. La primera imagen es la vista frontal. No las envíes con image_style_url.

target_formats

string[]

Los formatos de modelo que se van a generar. Uno o más de glb, obj, fbx, stl, usdz y 3mf.

texture_resolution

string

predeterminado:"\"2k\""

Resolución de textura del mapa de color base. meshy-n1 solo admite 2k.Valores posibles: `2k`

Generado a partir del esquema que Router expone en `GET /v2/models/meshy/meshy-n1/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

created_at

integer

Marca de tiempo de creación de la tarea, en milisegundos.

expires_at

integer

Marca de tiempo de expiración del resultado de la tarea, en milisegundos.

finished_at

integer

Marca de tiempo de finalización de la tarea, en milisegundos. 0 si no ha finalizado.

id

string

requerido

Identificador único de la tarea.

image_style_url

string

La entrada de imagen que se usó para crear la tarea de texturizado.

model_urls

object

URL de descarga de los archivos del modelo 3D texturizado.

model_urls.fbx

string

URL de descarga del archivo FBX.

model_urls.glb

string

URL de descarga del archivo GLB.

model_urls.mtl

string

URL de descarga del archivo de material MTL para el archivo OBJ.

model_urls.obj

string

URL de descarga del archivo OBJ.

model_urls.stl

string

URL de descarga del archivo STL.

model_urls.usdz

string

URL de descarga del archivo USDZ.

multiview_image_urls

string[]

Las imágenes de referencia que se usaron para crear la tarea de texturizado.

preceding_tasks

integer

La cantidad de tareas anteriores. Solo es relevante cuando el estado es PENDING.

progress

integer

Progreso de la tarea. 0 si no ha comenzado, 100 cuando se completa con éxito.Alcance: de `0` a `100`

started_at

integer

Marca de tiempo de inicio de la tarea, en milisegundos. 0 si no ha comenzado.

status

string

requerido

Valores posibles: `SUCCEEDED`

task_error

object

Objeto de error que contiene el mensaje de error si la tarea falló.

task_error.message

string

Mensaje de error detallado.

text_style_prompt

string

El prompt de texto que se usó para crear la tarea de texturizado.

texture_urls

object[]

Un arreglo de objetos de URL de textura generados a partir de la tarea.

texture_urls[].base_color

string

URL de descarga de la imagen del mapa de color base.

texture_urls[].metallic

string

URL de descarga de la imagen del mapa metálico.

texture_urls[].normal

string

URL de descarga de la imagen del mapa de normales.

texture_urls[].roughness

string

URL de descarga de la imagen del mapa de rugosidad.

thumbnail_url

string

URL de descarga de la imagen en miniatura del archivo del modelo.

type

string

Tipo de la tarea de Retexture.Valores posibles: `retexture`

## Ejemplos

### Entrada
    
    
    {
      "image_style_url": "https://example.invalid/meshy/n1/front.png",
      "model_url": "https://cdn.meshy.ai/model/example_model_2.glb"
    }
    

### Salida
    
    
    {
      "created_at": 1767225600000,
      "finished_at": 1767225621000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "model_urls": {
        "fbx": "https://example.invalid/meshy/retexture/model.fbx",
        "glb": "https://example.invalid/meshy/retexture/model.glb"
      },
      "progress": 100,
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "texture_urls": [
        {
          "base_color": "https://example.invalid/meshy/retexture/texture_0.png"
        }
      ],
      "thumbnail_url": "https://example.invalid/meshy/retexture/preview.png",
      "type": "retexture"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/meshy/meshy-n1/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/meshy/meshy-n1/code)

[Meshy 7](https://docs.comfy.org/es/development/comfy-router/models/meshy/meshy-7/code)[Relief](https://docs.comfy.org/es/development/comfy-router/models/meshy/relief/code)
