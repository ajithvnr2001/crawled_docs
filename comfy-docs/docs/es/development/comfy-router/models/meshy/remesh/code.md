---
url: https://docs.comfy.org/es/development/comfy-router/models/meshy/remesh/code/
title: Usa Remesh con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:12.006254+00:00
---

# Usa Remesh con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/meshy/remesh/code/

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

# Usa Remesh con Comfy Router

Copiar páginaCopiar página

Llama a meshy/remesh mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `meshy/remesh`, servida por Comfy Router desde Meshy. **Entrada:** 3D · **Salida:** 3D

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `meshy/remesh` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/remesh`

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
            "meshy/remesh",
            {
                "input_task_id": "0193abcd-0000-0000-0000-000000000000",
                "origin_at": "bottom",
                "resize_height": 1,
                "target_formats": ["glb", "fbx"],
                "target_polycount": 50000,
                "topology": "quad",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("meshy/remesh", {
      input_task_id: "0193abcd-0000-0000-0000-000000000000",
      origin_at: "bottom",
      resize_height: 1,
      target_formats: ["glb", "fbx"],
      target_polycount: 50000,
      topology: "quad",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/remesh \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input_task_id\": \"0193abcd-0000-0000-0000-000000000000\", \"origin_at\": \"bottom\", \"resize_height\": 1, \"target_formats\": [\"glb\",\"fbx\"], \"target_polycount\": 50000, \"topology\": \"quad\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/meshy/remesh/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "meshy/remesh",
                {
                    "input_task_id": "0193abcd-0000-0000-0000-000000000000",
                    "origin_at": "bottom",
                    "resize_height": 1,
                    "target_formats": ["glb", "fbx"],
                    "target_polycount": 50000,
                    "topology": "quad",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("meshy/remesh", {
      input_task_id: "0193abcd-0000-0000-0000-000000000000",
      origin_at: "bottom",
      resize_height: 1,
      target_formats: ["glb", "fbx"],
      target_polycount: 50000,
      topology: "quad",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló genera un rechazo aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/meshy/remesh/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input_task_id\": \"0193abcd-0000-0000-0000-000000000000\", \"origin_at\": \"bottom\", \"resize_height\": 1, \"target_formats\": [\"glb\",\"fbx\"], \"target_polycount\": 50000, \"topology\": \"quad\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/remesh/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/meshy/remesh/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

convert_format_only

boolean

predeterminado:"false"

Si es verdadero, solo cambia el formato del archivo de modelo de entrada, ignorando otras entradas como topology, resize_height y target_polycount.

​

input_task_id

string

El ID de la tarea completada de Image to 3D o Text to 3D a la que deseas aplicar remesh. Requerido si no proporcionas model_url.

​

model_url

string

Una URL de acceso público o un data URI a un modelo 3D. Formatos admitidos: glb, gltf, obj, fbx, stl. Requerido si no proporcionas input_task_id.

​

origin_at

string

Posición del origen.Valores posibles: `bottom`, `center`, “

​

resize_height

number

predeterminado:"0"

Redimensiona el modelo a una altura determinada medida en metros. 0 significa que no se redimensiona.

​

target_formats

`glb`, `fbx`, `obj`, `usdz`, `blend`, `stl`[]

predeterminado:"[\"glb\"]"

Una lista de formatos objetivo para el modelo con remesh aplicado.

​

target_polycount

integer

predeterminado:"30000"

Especifica la cantidad objetivo de polígonos en el modelo generado. El rango válido es de 100 a 300,000.Rango: `100` a `300000`

​

topology

string

predeterminado:"\"triangle\""

Especifica la topología del modelo generado.Valores posibles: `quad`, `triangle`

Generado a partir del esquema que Router sirve en `GET /v2/models/meshy/remesh/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

created_at

integer

Marca de tiempo de cuándo se creó la tarea, en milisegundos.Formato: `int64`

​

finished_at

integer

Marca de tiempo de cuándo finalizó la tarea, en milisegundos. 0 si no ha finalizado.Formato: `int64`

​

id

string

requerido

Identificador único de la tarea.

​

model_urls

object

URLs descargables de los archivos del modelo 3D con remesh aplicado.

​

model_urls.blend

string

URL descargable del archivo de Blender.

​

model_urls.fbx

string

URL descargable del archivo FBX.

​

model_urls.glb

string

URL descargable del archivo GLB.

​

model_urls.obj

string

URL descargable del archivo OBJ.

​

model_urls.stl

string

URL descargable del archivo STL.

​

model_urls.usdz

string

URL descargable del archivo USDZ.

​

preceding_tasks

integer

La cantidad de tareas precedentes. Solo tiene sentido cuando el estado es PENDING.

​

progress

integer

Progreso de la tarea. 0 si no ha comenzado, 100 cuando se completa con éxito.Rango: `0` a `100`

​

started_at

integer

Marca de tiempo de cuándo comenzó la tarea, en milisegundos. 0 si no ha comenzado.Formato: `int64`

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

type

string

Tipo de la tarea de Remesh.Valores posibles: `remesh`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input_task_id": "0193abcd-0000-0000-0000-000000000000",
      "origin_at": "bottom",
      "resize_height": 1,
      "target_formats": [
        "glb",
        "fbx"
      ],
      "target_polycount": 50000,
      "topology": "quad"
    }
    

### 

​

Salida
    
    
    {
      "created_at": 1767225600000,
      "finished_at": 1767225663000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "model_urls": {
        "fbx": "https://example.invalid/meshy/remesh/model.fbx",
        "glb": "https://example.invalid/meshy/remesh/model.glb",
        "obj": "https://example.invalid/meshy/remesh/model.obj"
      },
      "progress": 100,
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "type": "remesh"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/meshy/remesh/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/meshy/remesh/code)

[Meshy 7](https://docs.comfy.org/es/development/comfy-router/models/meshy/meshy-7/code)[Rigging](https://docs.comfy.org/es/development/comfy-router/models/meshy/rigging/code)
