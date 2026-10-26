---
url: https://docs.comfy.org/es/development/comfy-router/models/meshy/meshy-6/code/
title: Usa Meshy 6 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:10.797594+00:00
---

# Usa Meshy 6 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/meshy/meshy-6/code/

## En esta página

Volver arriba

  * Inicio rápido
  * Esquema
    * Entrada
    * variante preview
    * variante refine
    * Salida
  * Ejemplos
    * Entrada
    * Salida
  * Antes de lanzar



Meshy

# Usa Meshy 6 con Comfy Router

Copiar páginaCopiar página

Llama a meshy/meshy-6 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `meshy/meshy-6`, servida por Comfy Router de Meshy. **Entrada:** Texto · **Salida:** 3D

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `meshy/meshy-6` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/meshy-6`

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
            "meshy/meshy-6",
            {
                "art_style": "realistic",
                "mode": "preview",
                "prompt": "a red cube",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("meshy/meshy-6", {
      art_style: "realistic",
      mode: "preview",
      prompt: "a red cube",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/meshy-6 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"art_style\": \"realistic\", \"mode\": \"preview\", \"prompt\": \"a red cube\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/meshy/meshy-6/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "meshy/meshy-6",
                {
                    "art_style": "realistic",
                    "mode": "preview",
                    "prompt": "a red cube",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("meshy/meshy-6", {
      art_style: "realistic",
      mode: "preview",
      prompt: "a red cube",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/meshy/meshy-6/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"art_style\": \"realistic\", \"mode\": \"preview\", \"prompt\": \"a red cube\"}"
    
    # 2. Consulta en bucle hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/meshy-6/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/meshy/meshy-6/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

#### 

​

variante `preview`

​

ai_model

string

El modelo de Meshy que se ejecutará. En la ruta de Comfy Router, este valor lo proporciona la ruta (`/v2/models/meshy/{model}`) y puede omitirse o enviarse como null; Router escribe aquí el modelo de la ruta después de la validación. En la ruta v1 /proxy, consulta MeshyTextTo3DPreviewRequest, que lo restringe a MeshyAiModel.

​

art_style

string

predeterminado:"\"realistic\""

Describe el estilo artístico que deseas para el objeto.Valores posibles: `realistic`, `sculpture`

​

geometry_resolution

string

predeterminado:"\"standard\""

Resolución de la geometría de la malla generada. 2k y 4k ejecutan el pase Ultra para obtener un detalle de superficie más fino. 2k y 4k requieren ai_model meshy-7.1 o latest.Valores posibles: `standard`, `2k`, `4k`

​

is_a_t_pose

boolean

predeterminado:"false"

Obsoleto. Usa pose_mode en su lugar. Indica si se debe generar el modelo en pose A/T.

​

mode

string

requerido

Este campo debe establecerse en “preview” al crear una tarea de vista previa.Valores posibles: `preview`

​

moderation

boolean

predeterminado:"false"

Cuando es true, el contenido de entrada se someterá a revisión para detectar contenido potencialmente dañino.

​

pose_mode

string

Especifica el modo de pose del modelo generado.Valores posibles: `a-pose`, `t-pose`, “

​

prompt

string

requerido

Describe qué tipo de objeto es el modelo 3D. Máximo 800 caracteres.

​

should_remesh

boolean

predeterminado:"false"

Controla si se habilita la fase de remallado. Cuando es false, devuelve la malla triangular de mayor precisión. De forma predeterminada, es true para Meshy 5 y false para Meshy 6 y 7.

​

symmetry_mode

string

predeterminado:"\"auto\""

Controla el comportamiento de simetría durante la generación del modelo.Valores posibles: `off`, `auto`, `on`

​

target_polycount

integer

predeterminado:"30000"

Especifica el número objetivo de polígonos en el modelo generado. El rango válido es de 100 a 300,000.Rango: `100` a `300000`

​

topology

string

predeterminado:"\"triangle\""

Especifica la topología del modelo generado.Valores posibles: `quad`, `triangle`

​

ultra_mode

boolean

predeterminado:"false"

Obsoleto. Usa geometry_resolution en su lugar; true equivale a geometry_resolution 2k. Solo se admite cuando ai_model es meshy-7, meshy-7.1 o latest. La excepción es meshy-7: geometry_resolution 2k requiere meshy-7.1 o latest, así que en meshy-7, ultra_mode true es la forma de solicitar el pase Ultra.

#### 

​

variante `refine`

​

ai_model

string

El modelo de Meshy que se ejecutará. En la ruta de Comfy Router, este valor lo proporciona la ruta (`/v2/models/meshy/{model}`) y puede omitirse o enviarse como null; Router escribe aquí el modelo de la ruta después de la validación. En la ruta v1 /proxy, consulta MeshyTextTo3DRefineRequest, que lo restringe a MeshyAiModel.

​

enable_pbr

boolean

predeterminado:"false"

Genera mapas PBR (metálico, rugosidad, normal) además del color base. Ten en cuenta que enable_pbr debe establecerse en false cuando uses el estilo Sculpture.

​

mode

string

requerido

Este campo debe establecerse en “refine” al crear una tarea de refinado.Valores posibles: `refine`

​

moderation

boolean

predeterminado:"false"

Cuando es true, el contenido de entrada se someterá a revisión para detectar contenido potencialmente dañino.

​

preview_task_id

string

requerido

El id de la tarea de vista previa correspondiente. El estado de la tarea de vista previa indicada debe ser SUCCEEDED.

​

texture_image_url

string

Proporciona una imagen 2D para guiar el proceso de texturizado. Admite formatos .jpg, .jpeg y .png, o un URI de datos codificado en base64.

​

texture_prompt

string

Proporciona un prompt de texto adicional para guiar el proceso de texturizado. Máximo 800 caracteres.

​

texture_resolution

string

predeterminado:"\"2k\""

Resolución de textura de las texturas generadas. Una de 2k, 4k u 8k. 4k y 8k requieren ai_model meshy-6, meshy-7, meshy-7.1 o latest.Valores posibles: `2k`, `4k`, `8k`

Generado a partir del esquema que Router sirve en `GET /v2/models/meshy/meshy-6/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

art_style

string

El art_style sin modificar que se usó para crear la tarea de vista previa.

​

created_at

integer

Marca de tiempo de creación de la tarea, en milisegundos.Formato: `int64`

​

finished_at

integer

Marca de tiempo de finalización de la tarea, en milisegundos. 0 si no ha finalizado.Formato: `int64`

​

id

string

requerido

Identificador único de la tarea.

​

model_urls

object

URLs descargables de los archivos de modelo 3D texturizado generados por Meshy.

​

model_urls.fbx

string

URL descargable del archivo FBX.

​

model_urls.glb

string

URL descargable del archivo GLB.

​

model_urls.mtl

string

URL descargable del archivo MTL.

​

model_urls.obj

string

URL descargable del archivo OBJ.

​

model_urls.usdz

string

URL descargable del archivo USDZ.

​

negative_prompt

string

Campo obsoleto que se mantiene por compatibilidad con versiones anteriores.

​

preceding_tasks

integer

El número de tareas anteriores. Solo es relevante cuando el estado es PENDING.

​

progress

integer

Progreso de la tarea. 0 si no ha comenzado, 100 cuando se completa con éxito.Rango: `0` a `100`

​

prompt

string

El prompt sin modificar que se usó para crear la tarea.

​

started_at

integer

Marca de tiempo de inicio de la tarea, en milisegundos. 0 si no ha comenzado.Formato: `int64`

​

status

string

requerido

Valores posibles: `SUCCEEDED`

​

task_error

object

Objeto de error que contiene el mensaje de error si la tarea falló.

​

task_error.message

string

Mensaje de error detallado.

​

texture_image_url

string

URL descargable de la imagen de textura que se usó para guiar el proceso de texturizado.

​

texture_prompt

string

Prompt de texto adicional proporcionado para guiar el proceso de texturizado durante la etapa de refinado.

​

texture_richness

string

Campo obsoleto que se mantiene por compatibilidad con versiones anteriores.

​

texture_urls

object[]

Un arreglo de objetos de URL de textura generados a partir de la tarea.

​

texture_urls[].base_color

string

URL descargable de la imagen del mapa de color base.

​

texture_urls[].metallic

string

URL descargable de la imagen del mapa metálico.

​

texture_urls[].normal

string

URL descargable de la imagen del mapa de normales.

​

texture_urls[].roughness

string

URL descargable de la imagen del mapa de rugosidad.

​

thumbnail_url

string

URL descargable de la imagen en miniatura del archivo de modelo.

​

type

string

Tipo de la tarea de texto a 3D.Valores posibles: `text-to-3d-preview`, `text-to-3d-refine`

​

video_url

string

Campo obsoleto que devuelve la URL descargable del video de vista previa.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "art_style": "realistic",
      "mode": "preview",
      "prompt": "a red cube"
    }
    

### 

​

Salida
    
    
    {
      "art_style": "realistic",
      "created_at": 1767225600000,
      "finished_at": 1767225719000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "model_urls": {
        "fbx": "https://example.invalid/meshy/text-to-3d/model.fbx",
        "glb": "https://example.invalid/meshy/text-to-3d/model.glb",
        "mtl": "https://example.invalid/meshy/text-to-3d/model.mtl",
        "obj": "https://example.invalid/meshy/text-to-3d/model.obj",
        "usdz": "https://example.invalid/meshy/text-to-3d/model.usdz"
      },
      "progress": 100,
      "prompt": "a red cube",
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "thumbnail_url": "https://example.invalid/meshy/text-to-3d/thumbnail.png",
      "type": "text-to-3d-preview"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/meshy/meshy-6/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/meshy/meshy-6/code)

[Animations](https://docs.comfy.org/es/development/comfy-router/models/meshy/animations/code)[Meshy 7.1](https://docs.comfy.org/es/development/comfy-router/models/meshy/meshy-7-1/code)
