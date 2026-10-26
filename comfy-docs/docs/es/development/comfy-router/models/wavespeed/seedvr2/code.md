---
url: https://docs.comfy.org/es/development/comfy-router/models/wavespeed/seedvr2/code/
title: Usa Seedvr 2 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:24.846007+00:00
---

# Usa Seedvr 2 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/wavespeed/seedvr2/code/

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



WaveSpeed

# Usa Seedvr 2 con Comfy Router

Copiar páginaCopiar página

Llama a wavespeed/seedvr2 a través de Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `wavespeed/seedvr2`, que Comfy Router proporciona desde WaveSpeed. **Entrada:** Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `wavespeed/seedvr2` **Endpoint:** `POST https://api.comfy.org/v2/models/wavespeed/seedvr2`

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
            "wavespeed/seedvr2",
            {
                "image": "https://images.pexels.com/photos/346529/pexels-photo-346529.jpeg",
                "target_resolution": "4k",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("wavespeed/seedvr2", {
      image: "https://images.pexels.com/photos/346529/pexels-photo-346529.jpeg",
      target_resolution: "4k",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/wavespeed/seedvr2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://images.pexels.com/photos/346529/pexels-photo-346529.jpeg\", \"target_resolution\": \"4k\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/wavespeed/seedvr2/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "wavespeed/seedvr2",
                {
                    "image": "https://images.pexels.com/photos/346529/pexels-photo-346529.jpeg",
                    "target_resolution": "4k",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("wavespeed/seedvr2", {
      image: "https://images.pexels.com/photos/346529/pexels-photo-346529.jpeg",
      target_resolution: "4k",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/wavespeed/seedvr2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://images.pexels.com/photos/346529/pexels-photo-346529.jpeg\", \"target_resolution\": \"4k\"}"
    
    # 2. Consultar hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/wavespeed/seedvr2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/wavespeed/seedvr2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

enable_base64_output

boolean

predeterminado:"false"

Si está habilitado, la salida se codificará en una cadena BASE64 en lugar de una URL.

​

image

string

requerido

La URL de la imagen a la que se aplicará upscale.

​

output_format

string

predeterminado:"\"jpeg\""

El formato de la imagen de salida.Valores posibles: `jpeg`, `png`, `webp`

​

target_resolution

string

predeterminado:"\"4k\""

La resolución objetivo de la imagen de salida.Valores posibles: `2k`, `4k`, `8k`

Generado a partir del esquema que Router sirve en `GET /v2/models/wavespeed/seedvr2/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

code

integer

El código de estado del sobre propio de WavespeedAI, que refleja un estado HTTP (200 en el documento que describe este esquema). Wavespeed informa algunos fallos aquí en lugar de en el estado del transporte.

​

data

object

requerido

​

data.created_at

string

Marca de tiempo ISO-8601 de cuándo Wavespeed creó la predicción.

​

data.error

string

El motivo del fallo en texto libre de Wavespeed, una cadena vacía cuando no hay ninguno. Una predicción que falló de verdad llega a un cliente de Router como un error de Comfy Router en lugar de como este documento.

​

data.id

string

El identificador de Wavespeed para la predicción que Router envió y consultó.

​

data.model

string

El id de modelo de Wavespeed con el que corrió la predicción.

​

data.outputs

string[]

requerido

La generación finalizada. Presente y no vacía en el documento que devuelve Router; esta lista ES el resultado. Cada elemento es una URL al contenido generado (un MP4 para `wavespeed/flashvsr`, una imagen para los dos upscalers) o, para los dos ids de imagen cuando la solicitud estableció `enable_base64_output`, los propios bytes codificados en base64. Los enlaces son propios de Wavespeed y caducan.

​

data.status

string

requerido

El estado terminal de la predicción tal como lo escribió Wavespeed. Aquí no se restringe a un enum: Router reenvía el valor sin cambios y el clasificador de sondeo lo pasa a minúsculas antes de comparar, así que un éxito puede llegar legítimamente como `completed`, `succeeded`, `success` o `done`, en cualquier combinación de mayúsculas y minúsculas.

​

data.timings

object

Las mediciones de tiempo propias de Wavespeed.

​

data.timings.inference

integer

Tiempo de inferencia en milisegundos. El número de Wavespeed, no el cargo de Comfy.

​

data.urls

object

Los enlaces propios de Wavespeed para la predicción.

​

data.urls.get

string

La URL del resultado de la predicción que consultó Router.

​

message

string

Mensaje de estado del sobre, por ejemplo `success`.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "image": "https://images.pexels.com/photos/346529/pexels-photo-346529.jpeg",
      "target_resolution": "4k"
    }
    

### 

​

Salida
    
    
    {
      "code": 200,
      "data": {
        "created_at": "2027-01-01T00:00:00Z",
        "error": "",
        "id": "3f6c1a90-2b47-4d18-9a55-7c0e8b21d4f3",
        "outputs": [
          "https://example.invalid/wavespeed/seedvr2/upscaled.png"
        ],
        "status": "completed",
        "timings": {
          "inference": 4200
        }
      },
      "message": "success"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/wavespeed/seedvr2/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/wavespeed/seedvr2/code)

[Flashvsr](https://docs.comfy.org/es/development/comfy-router/models/wavespeed/flashvsr/code)[Ultimate Image Upscaler](https://docs.comfy.org/es/development/comfy-router/models/wavespeed/ultimate-image-upscaler/code)
