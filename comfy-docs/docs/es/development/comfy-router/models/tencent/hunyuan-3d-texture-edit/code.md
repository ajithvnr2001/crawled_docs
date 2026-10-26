---
url: https://docs.comfy.org/es/development/comfy-router/models/tencent/hunyuan-3d-texture-edit/code/
title: Usa Hunyuan 3D Texture Edit con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:19.743620+00:00
---

# Usa Hunyuan 3D Texture Edit con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/tencent/hunyuan-3d-texture-edit/code/

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



Tencent

# Usa Hunyuan 3D Texture Edit con Comfy Router

Copiar páginaCopiar página

Llama a tencent/hunyuan-3d-texture-edit mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `tencent/hunyuan-3d-texture-edit`, servida por Comfy Router desde Tencent. **Entrada:** 3D, Texto · **Salida:** 3D

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `tencent/hunyuan-3d-texture-edit` **Endpoint:** `POST https://api.comfy.org/v2/models/tencent/hunyuan-3d-texture-edit`

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
            "tencent/hunyuan-3d-texture-edit",
            {
                "File3D": {
                    "Type": "FBX",
                    "Url": "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.fbx",
                },
                "Prompt": "a kitten",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("tencent/hunyuan-3d-texture-edit", {
      File3D: {
        Type: "FBX",
        Url: "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.fbx",
      },
      Prompt: "a kitten",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/tencent/hunyuan-3d-texture-edit \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"File3D\": {\"Type\":\"FBX\",\"Url\":\"https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.fbx\"}, \"Prompt\": \"a kitten\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/tencent/hunyuan-3d-texture-edit/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recopila cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recopilación.

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
                "tencent/hunyuan-3d-texture-edit",
                {
                    "File3D": {
                        "Type": "FBX",
                        "Url": "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.fbx",
                    },
                    "Prompt": "a kitten",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("tencent/hunyuan-3d-texture-edit", {
      File3D: {
        Type: "FBX",
        Url: "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.fbx",
      },
      Prompt: "a kitten",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/tencent/hunyuan-3d-texture-edit/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"File3D\": {\"Type\":\"FBX\",\"Url\":\"https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.fbx\"}, \"Prompt\": \"a kitten\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/tencent/hunyuan-3d-texture-edit/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recopila. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue ejecutándose.
    curl https://api.comfy.org/v2/models/tencent/hunyuan-3d-texture-edit/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

EnablePBR

boolean

Indica si se habilita el parámetro de textura PBR; solo se admite cuando usas Prompt.

​

File3D

object

requerido

Archivo 3D de entrada para la edición de texturas

​

File3D.Type

string

requerido

Tipo de formato del archivo 3DValores posibles: `FBX`

​

File3D.Url

string (uri)

requerido

URL del archivo 3D cuya textura se editaFormato: `uri`

​

Image

object

Imagen de referencia: datos Base64 o URL de la imagen

​

Image.Base64

string

Imagen codificada en Base64. Resolución de 128 a 4096 por lado; el Base64 convertido debe ser menor de 10 MB. Formatos: jpg, jpeg, png.

​

Image.Url

string (uri)

URL de la imagen. Si se proporcionan tanto Base64 como Url, prevalece Url.Formato: `uri`

​

Prompt

string

Describe la edición de texturas. Se requiere Image o Prompt; no pueden coexistir.

Generado a partir del esquema que Router publica en `GET /v2/models/tencent/hunyuan-3d-texture-edit/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

Response

object

requerido

​

Response.ErrorCode

string

Código de error de Tencent, documentado como cadena vacía cuando no hay error. Router no lo lee una vez que `Status` está presente.

​

Response.ErrorMessage

string

Mensaje de error de Tencent, documentado como cadena vacía cuando no hay error. Router no lo lee una vez que `Status` está presente.

​

Response.RequestId

string

Identificador de solicitud propio de Tencent, para solucionar problemas con Tencent. No es el ID de trabajo ni un recurso.

​

Response.ResultFile3Ds

object[]

requerido

Los archivos 3D generados por la tarea finalizada. Presentes y no vacíos en el documento que devuelve Router; al menos una entrada incluye una `Url` que se puede recuperar. Los enlaces son de Tencent y están documentados como válidos durante 24 horas.

​

Response.ResultFile3Ds[].PreviewImageUrl

string (uri)

URL de la vista previa de imagenFormato: `uri`

​

Response.ResultFile3Ds[].Type

string

Formato de archivo. Una tarea finalizada puede devolver varias entradas en un orden no fijo, y no todas las entradas son una malla: se ha observado que las operaciones de UV y topología inteligente devuelven mallas OBJ, GLB y FBX junto a una IMAGE (una textura PNG). Selecciona una entrada por `Type` y no por posición. Deliberadamente no es un enum: los valores anteriores son solo los observados, este componente se comparte con operaciones cuyo resultado nunca se ha observado (part, texture-edit), y el esquema de salida es descriptivo, por lo que un valor no listado que devuelva Tencent no debe convertir un resultado correcto en una violación del esquema.

​

Response.ResultFile3Ds[].Url

string (uri)

URL del archivo (válida durante 24 horas)Formato: `uri`

​

Response.Status

string

requerido

Valores posibles: `DONE`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "File3D": {
        "Type": "FBX",
        "Url": "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.fbx"
      },
      "Prompt": "a kitten"
    }
    

### 

​

Salida
    
    
    {
      "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "9a1c0d4e-77b2-4e0c-8f2e-2f9a1c0d4e77",
        "ResultFile3Ds": [
          {
            "PreviewImageUrl": "https://example.invalid/tencent/hunyuan-3d-texture-edit/preview.png",
            "Type": "GLB",
            "Url": "https://example.invalid/tencent/hunyuan-3d-texture-edit/retextured.glb"
          }
        ],
        "Status": "DONE"
      }
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/tencent/hunyuan-3d-texture-edit/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/tencent/hunyuan-3d-texture-edit/code)

[Hunyuan 3D Smart Topology](https://docs.comfy.org/es/development/comfy-router/models/tencent/hunyuan-3d-smart-topology/code)[Hunyuan 3D Uv](https://docs.comfy.org/es/development/comfy-router/models/tencent/hunyuan-3d-uv/code)
