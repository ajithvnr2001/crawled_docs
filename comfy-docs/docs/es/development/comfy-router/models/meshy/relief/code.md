---
url: https://docs.comfy.org/es/development/comfy-router/models/meshy/relief/code/
title: Usar Relief con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:25.994442+00:00
---

# Usar Relief con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/meshy/relief/code/

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

# Usar Relief con Comfy Router

Copiar páginaCopiar página

Llama a meshy/relief desde Comfy Router: endpoint, forma de la solicitud y respuesta.

Copiar páginaCopiar página

Referencia de API de `meshy/relief`, que Comfy Router ofrece desde Meshy. **Entrada:** Imagen · **Salida:** Imagen + 3D

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **ID del modelo:** `meshy/relief` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/relief`

  * Esperar el resultado

  * Poner en cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "meshy/relief",
            {
                "image_url": "https://example.invalid/meshy/relief/logo.png",
                "variant": "low",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("meshy/relief", {
      image_url: "https://example.invalid/meshy/relief/logo.png",
      variant: "low",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/relief \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://example.invalid/meshy/relief/logo.png\", \"variant\": \"low\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/meshy/relief/requests`. Router responde `201` con un `request_id` en cuanto se acepta la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "meshy/relief",
                {
                    "image_url": "https://example.invalid/meshy/relief/logo.png",
                    "variant": "low",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("meshy/relief", {
      image_url: "https://example.invalid/meshy/relief/logo.png",
      variant: "low",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/meshy/relief/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://example.invalid/meshy/relief/logo.png\", \"variant\": \"low\"}"
    
    # 2. Sondea hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/relief/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/meshy/relief/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

base_thickness_mm

number

Grosor de la placa base en milímetros, de 0.1 a 10. Con remove_base en true, omítelo o envía 0.Alcance: `0` a `10`

bend_angle

number

predeterminado:"60"

Ángulo de curvatura en grados. Por debajo de 1, el relieve permanece plano.Alcance: `0` a `360`

bend_axis

string

`xz` (predeterminado, curva los bordes izquierdo y derecho) o `yz` (curva los bordes superior e inferior). Solo se aplica cuando bend_mode es convex o concave.

bend_mode

string

`off` (predeterminado), `convex` o `concave`.

carving_depth_mm

number

Profundidad de tallado en milímetros. El valor predeterminado es 6 para variant high y 3 para variant low.Alcance: `0` a `60`

carving_mode

string

`emboss` (predeterminado) o `engrave`.

color_mapping

boolean

predeterminado:"false"

Colorea el modelo a partir de la imagen. GLB, OBJ, FBX y USDZ conservan el color; STL y 3MF permanecen blancos. El costo no cambia.

image_url

string

requerido

Una URL pública o un data URI de una imagen jpg, jpeg, png o webp. Como máximo 20 MB y al menos 32 x 32 píxeles. Las áreas transparentes se rellenan con negro.

mesh_resolution

integer

predeterminado:"1024"

Puntos a lo largo del lado más largo. Los valores más grandes generan archivos mucho más grandes (aproximadamente 150 MB en GLB y 300 MB en STL con 2048).Alcance: `512` a `2048`

removal_threshold

number

predeterminado:"0.01"

Umbral de eliminación de fondo. Solo se aplica cuando remove_base es true.Alcance: `0.01` a `1`

remove_base

boolean

predeterminado:"false"

Recorta el fondo para que el relieve no tenga placa base.

should_generate_model

boolean

predeterminado:"true"

Establécelo en false para obtener solo un mapa de profundidad, sin modelo ni vista previa. El costo no cambia.

size_mm

number

predeterminado:"60"

Longitud del lado más largo en milímetros.Alcance: `20` a `250`

target_formats

string[]

Los formatos de modelo que se van a generar. Uno o más de glb, obj, fbx, stl, usdz y 3mf. El valor predeterminado es glb y stl.

variant

string

`low` (predeterminado) da una profundidad leve y un detalle más fino, para trabajo con láser o CNC. `high` da un relieve más profundo y escultórico, para impresión 3D. También establece el carving_depth_mm predeterminado.

Generado a partir del esquema que Router sirve en `GET /v2/models/meshy/relief/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

consumed_credits

integer

Créditos de Meshy que usó la tarea. 0 si la tarea falló.

created_at

integer

Marca de tiempo de creación de la tarea, en milisegundos.Formato: `int64`

depth_map_url

string

URL descargable del PNG de mapa de profundidad en escala de grises de 16 bits y 2k. Los valores son relativos, no milímetros.

expires_at

integer

Marca de tiempo de expiración del resultado de la tarea, en milisegundos. 0 si no ha finalizado.Formato: `int64`

finished_at

integer

Marca de tiempo de finalización de la tarea, en milisegundos. 0 si no ha finalizado.Formato: `int64`

id

string

requerido

Identificador único de la tarea.

model_urls

object

URLs descargables de los archivos del modelo de relieve, una por cada formato solicitado. Vacío si la tarea es solo de mapa de profundidad.

model_urls.3mf

string

URL descargable del archivo 3MF.

model_urls.fbx

string

URL descargable del archivo FBX.

model_urls.glb

string

URL descargable del archivo GLB, en metros.

model_urls.mtl

string

URL descargable del archivo de material MTL para el archivo OBJ.

model_urls.obj

string

URL descargable del archivo OBJ.

model_urls.stl

string

URL descargable del archivo STL binario, en milímetros.

model_urls.usdz

string

URL descargable del archivo USDZ.

preceding_tasks

integer

La cantidad de tareas precedentes. Solo tiene sentido cuando el estado es PENDING.

progress

integer

Progreso de la tarea. 0 si no ha comenzado, 100 cuando se completa correctamente.Alcance: `0` a `100`

started_at

integer

Marca de tiempo de inicio de la tarea, en milisegundos. 0 si no ha comenzado.Formato: `int64`

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

texture_urls

object[]

URLs de texturas. Presente solo con color_mapping en true.

texture_urls[].base_color

string

URL descargable de la imagen del mapa de color base.

texture_urls[].metallic

string

URL descargable de la imagen del mapa metálico.

texture_urls[].normal

string

URL descargable de la imagen del mapa de normales.

texture_urls[].roughness

string

URL descargable de la imagen del mapa de rugosidad.

thumbnail_url

string

URL descargable de la vista previa de imagen. Vacío si la tarea es solo de mapa de profundidad.

type

string

Tipo de la tarea. Siempre relief.

## Ejemplos

### Entrada
    
    
    {
      "image_url": "https://example.invalid/meshy/relief/logo.png",
      "variant": "low"
    }
    

### Salida
    
    
    {
      "consumed_credits": 20,
      "created_at": 1767225600000,
      "depth_map_url": "https://example.invalid/meshy/relief/depth.png",
      "finished_at": 1767225663000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "model_urls": {
        "glb": "https://example.invalid/meshy/relief/model.glb",
        "stl": "https://example.invalid/meshy/relief/model.stl"
      },
      "progress": 100,
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "thumbnail_url": "https://example.invalid/meshy/relief/preview.png",
      "type": "relief"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/meshy/relief/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/meshy/relief/code)

[Meshy N1](https://docs.comfy.org/es/development/comfy-router/models/meshy/meshy-n1/code)[Remesh](https://docs.comfy.org/es/development/comfy-router/models/meshy/remesh/code)
