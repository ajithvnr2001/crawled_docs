---
url: https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-product-holding/code/
title: Usa Image Edit Product Holding con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:58.318009+00:00
---

# Usa Image Edit Product Holding con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-product-holding/code/

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



Bria

# Usa Image Edit Product Holding con Comfy Router

Copiar páginaCopiar página

Llama a bria/image-edit-product-holding con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `bria/image-edit-product-holding`, servida por Comfy Router de Bria. **Entrada:** Imagen, Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **ID del modelo:** `bria/image-edit-product-holding` **Endpoint:** `POST https://api.comfy.org/v2/models/bria/image-edit-product-holding`

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
            "bria/image-edit-product-holding",
            {
                "person_image": "https://labs-assets.bria.ai/api-examples/product-holding/person.jpg",
                "product_images": ["https://labs-assets.bria.ai/api-examples/product-holding/product.jpg"],
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("bria/image-edit-product-holding", {
      person_image: "https://labs-assets.bria.ai/api-examples/product-holding/person.jpg",
      product_images: ["https://labs-assets.bria.ai/api-examples/product-holding/product.jpg"],
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bria/image-edit-product-holding \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"person_image\": \"https://labs-assets.bria.ai/api-examples/product-holding/person.jpg\", \"product_images\": [\"https://labs-assets.bria.ai/api-examples/product-holding/product.jpg\"]}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bria/image-edit-product-holding/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) te guía por el estado, la cancelación y la recogida.

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
                "bria/image-edit-product-holding",
                {
                    "person_image": "https://labs-assets.bria.ai/api-examples/product-holding/person.jpg",
                    "product_images": ["https://labs-assets.bria.ai/api-examples/product-holding/product.jpg"],
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("bria/image-edit-product-holding", {
      person_image: "https://labs-assets.bria.ai/api-examples/product-holding/person.jpg",
      product_images: ["https://labs-assets.bria.ai/api-examples/product-holding/product.jpg"],
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
    curl https://api.comfy.org/v2/models/bria/image-edit-product-holding/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"person_image\": \"https://labs-assets.bria.ai/api-examples/product-holding/person.jpg\", \"product_images\": [\"https://labs-assets.bria.ai/api-examples/product-holding/product.jpg\"]}"
    
    # 2. Consultar hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bria/image-edit-product-holding/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/bria/image-edit-product-holding/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

aspect_ratio

string

Relación de aspecto de la imagen de salida, uno de “1:1”, “2:3”, “3:2”, “3:4”, “4:3”, “4:5”, “5:4”, “9:16” o “16:9”. Por defecto, la relación de aspecto de person_image.

​

instruction

string

Indicación adicional opcional para esta toma, por ejemplo “Replace the paper coffee cup in her right hand with the can, logo facing the camera”. Envía solo el detalle que quieres orientar, no un prompt completo.

​

output_type

string

Formato de la imagen de salida, “png” o “jpeg”.

​

person_image

string

requerido

La foto de la persona que se va a editar. URL de acceso público o codificada en Base64. Formatos aceptados: JPEG, JPG, PNG, WEBP.

​

product_images

string[]

requerido

De una a tres imágenes del producto, como el empaque, un segundo ángulo o un artículo complementario. Cada entrada es una URL de acceso público o está codificada en Base64, igual que person_image.

​

seed

integer

Semilla para una generación determinista. Si se omite, se usa una semilla aleatoria.

​

sync

boolean

Debe ser falso u omitirse. El modo síncrono de Bria (verdadero) se rechaza en lugar de reenviarse, tanto en Comfy Router como en la ruta `/proxy/` propia de esta operación: Comfy Router fija el modo de retorno antes del despacho y consulta el resultado dentro de la llamada, y la ruta `/proxy/` devuelve el request_id y el status_url que hay que consultar.

​

visual_output_content_moderation

boolean

Si es verdadero, devuelve 422 cuando falla la moderación de la salida visual.

Generado a partir del esquema que Router sirve en `GET /v2/models/bria/image-edit-product-holding/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

object

Objeto de error (solo presente cuando el estado es ERROR)

​

error.code

integer

Código de error.

​

error.details

string

Detalles adicionales del error.

​

error.message

string

Mensaje de error.

​

request_id

string

Identificador único de la solicitud.

​

result

object

Objeto de resultado (solo presente cuando el estado es COMPLETED)

​

result.image_url

string

URL de la imagen generada o editada.

​

result.prompt

string

Prompt original.

​

result.refined_prompt

string

Versión refinada del prompt, o null en una generación COMPLETED que Bria no refinó. Es nullable porque la clave está PRESENT con null en lugar de omitida; observado en vivo en bria/image-edit-gen-fill.

​

result.seed

integer

Semilla usada para la generación.

​

result.structured_instruction

string

La instrucción estructurada, un documento JSON serializado como cadena, que devuelve `/v2/structured_instruction/generate`. Esa operación no rellena ninguna de las dos URL.

​

result.structured_prompt

string

El prompt estructurado detallado en JSON.

​

result.video_url

string

URL del video generado.

​

status

string

Estado actual de la solicitud.Valores posibles: `IN_PROGRESS`, `COMPLETED`, `ERROR`, `UNKNOWN`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "person_image": "https://labs-assets.bria.ai/api-examples/product-holding/person.jpg",
      "product_images": [
        "https://labs-assets.bria.ai/api-examples/product-holding/product.jpg"
      ]
    }
    

### 

​

Salida
    
    
    {
      "request_id": "0b3f9d7e-2c41-4a8b-9f10-6d5c8e2a4b71",
      "result": {
        "image_url": "https://example.invalid/bria/image-edit-product-holding/generated.png"
      },
      "status": "COMPLETED"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/bria/image-edit-product-holding/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/bria/image-edit-product-holding/code)

[Image Edit Increase Resolution](https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-increase-resolution/code)[Image Edit Product Virtual Tryon](https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-product-virtual-tryon/code)
