---
url: https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-reseason/code/
title: Usa Image Edit Reseason con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:58.797665+00:00
---

# Usa Image Edit Reseason con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-reseason/code/

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

# Usa Image Edit Reseason con Comfy Router

Copiar páginaCopiar página

Llama a bria/image-edit-reseason desde Comfy Router: endpoint, forma de la solicitud y respuesta de Router.

Copiar páginaCopiar página

Referencia de API para `bria/image-edit-reseason`, servida por Comfy Router desde Bria. **Entrada:** Imagen, Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **ID del modelo:** `bria/image-edit-reseason` **Endpoint:** `POST https://api.comfy.org/v2/models/bria/image-edit-reseason`

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
            "bria/image-edit-reseason",
            {
                "image": "https://picsum.photos/id/237/960/540",
                "season": "winter",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("bria/image-edit-reseason", {
      image: "https://picsum.photos/id/237/960/540",
      season: "winter",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bria/image-edit-reseason \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://picsum.photos/id/237/960/540\", \"season\": \"winter\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bria/image-edit-reseason/requests`. El router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "bria/image-edit-reseason",
                {
                    "image": "https://picsum.photos/id/237/960/540",
                    "season": "winter",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado del router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("bria/image-edit-reseason", {
      image: "https://picsum.photos/id/237/960/540",
      season: "winter",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. El router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/bria/image-edit-reseason/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://picsum.photos/id/237/960/540\", \"season\": \"winter\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indique cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bria/image-edit-reseason/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/bria/image-edit-reseason/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

image

string

requerido

La imagen que se va a editar. Los tipos de entrada admitidos son una cadena codificada en Base64 o una URL que apunte a un archivo de imagen de acceso público. Formatos aceptados: JPEG, JPG, PNG, WEBP.

​

season

string

requerido

La estación que se va a aplicar, una de “spring”, “summer”, “autumn” o “winter”. También se acepta texto personalizado.

Generado a partir del esquema que Router sirve en `GET /v2/models/bria/image-edit-reseason/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

object

Objeto de error (solo está presente cuando el estado es ERROR)

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

Objeto de resultado (solo está presente cuando el estado es COMPLETED)

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

Versión refinada del prompt, o null en una generación COMPLETED que Bria no refinó. Es anulable porque la clave está PRESENTE con valor null en lugar de omitirse; se observó en vivo en bria/image-edit-gen-fill.

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
      "image": "https://picsum.photos/id/237/960/540",
      "season": "winter"
    }
    

### 

​

Salida
    
    
    {
      "request_id": "0b3f9d7e-2c41-4a8b-9f10-6d5c8e2a4b71",
      "result": {
        "image_url": "https://example.invalid/bria/image-edit-reseason/generated.png",
        "seed": 42
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/bria/image-edit-reseason/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/bria/image-edit-reseason/code)

[Image Edit Replace Object By Text](https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-replace-object-by-text/code)[Image Edit Restore](https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-restore/code)
