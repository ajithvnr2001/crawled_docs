---
url: https://docs.comfy.org/es/development/comfy-router/models/runway/aleph2/code/
title: Usa Aleph 2 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:19.338528+00:00
---

# Usa Aleph 2 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/runway/aleph2/code/

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



Runway

# Usa Aleph 2 con Comfy Router

Copiar páginaCopiar página

Llama a runway/aleph2 con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `runway/aleph2`, servida por Comfy Router desde Runway. **Entrada:** Video, Texto, Imagen · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP directo. **ID del modelo:** `runway/aleph2` **Endpoint:** `POST https://api.comfy.org/v2/models/runway/aleph2`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY desde el entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "runway/aleph2",
            {
                "promptText": "recolor the scene in cool blue tones",
                "videoUri": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY desde el entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("runway/aleph2", {
      promptText: "recolor the scene in cool blue tones",
      videoUri: "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/runway/aleph2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"promptText\": \"recolor the scene in cool blue tones\", \"videoUri\": \"https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/runway/aleph2/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY desde el entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "runway/aleph2",
                {
                    "promptText": "recolor the scene in cool blue tones",
                    "videoUri": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY desde el entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("runway/aleph2", {
      promptText: "recolor the scene in cool blue tones",
      videoUri: "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/runway/aleph2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"promptText\": \"recolor the scene in cool blue tones\", \"videoUri\": \"https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/runway/aleph2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/runway/aleph2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

contentModeration

object

Configuraciones que afectan el comportamiento del sistema de moderación de contenido.

​

contentModeration.publicFigureThreshold

string

Cuando se establece en `low`, el sistema de moderación de contenido será menos estricto para evitar generaciones que incluyan figuras públicas reconocibles.Valores posibles: `auto`, `low`

​

keyframes

object[]

Imágenes de orientación cronometradas colocadas en puntos específicos del video de entrada. Hasta 5 fotogramas clave.

​

model

string

Modelo que se usará para la generación. En la ruta de Comfy Router `POST /v2/models/runway/{model}`, este campo se toma de la ruta y NO DEBE enviarse; en la ruta v1 `POST /proxy/runway/video_to_video`, es requerido y está restringido al RunwayVideoToVideoModelEnum (`aleph2`).

​

promptImage

object[]

Una lista de hasta 5 fotogramas clave de imagen para orientar la edición en puntos específicos del video.

​

promptImage[].position

`first`, `last` | object

requerido

La posición en el video de salida donde debe aplicarse la imagen.

​

promptImage[].uri

string

requerido

Una URL HTTPS, una URI de Runway o una URI de datos que contenga una imagen codificada.

​

promptText

string

requerido

Una cadena no vacía de hasta 1000 caracteres que describa qué debería aparecer en la salida.

​

seed

integer

Semilla aleatoria para la generación.Rango: `0` a `4294967295`Formato: `int64`

​

videoUri

string

requerido

El video de entrada que se va a editar (URL HTTPS, URI de carga de Runway o URI de datos). Debe durar 30 segundos o menos.

Generado a partir del esquema que Router sirve en `GET /v2/models/runway/aleph2/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

createdAt

string (date-time)

requerido

Marca de tiempo de creación de la tareaFormato: `date-time`

​

id

string

requerido

ID de la tarea

​

output

string[]

Las URL de los recursos de la generación finalizada: para `runway/gen4_turbo` y `runway/aleph2`, cada elemento es una URL de VIDEO. Está presente una vez que la tarea finaliza correctamente; esta lista ES el resultado.

​

progress

number

Valor flotante entre 0 y 1 que representa el progreso de la tarea. Solo está disponible si el estado es RUNNING.Rango: `0` a `1`Formato: `float`

​

status

string

requerido

Estados posibles de una tarea de Runway.Valores posibles: `SUCCEEDED`, `RUNNING`, `FAILED`, `PENDING`, `CANCELLED`, `THROTTLED`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "promptText": "recolor the scene in cool blue tones",
      "videoUri": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"
    }
    

### 

​

Salida
    
    
    {
      "createdAt": "2027-01-01T00:00:00Z",
      "id": "5f7c1b28-9a03-4e61-8d2f-1b2c3d4e5f60",
      "output": [
        "https://example.invalid/runway/gen4_turbo/generated.mp4"
      ],
      "status": "SUCCEEDED"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/runway/aleph2/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/runway/aleph2/code)

[Recraft V4](https://docs.comfy.org/es/development/comfy-router/models/recraft/recraftv4/code)[Gen 4 Image](https://docs.comfy.org/es/development/comfy-router/models/runway/gen4-image/code)
