---
url: https://docs.comfy.org/es/development/comfy-router/models/recraft/recraftv3/code/
title: Usa Recraft V3 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:17.521913+00:00
---

# Usa Recraft V3 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/recraft/recraftv3/code/

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



Recraft

# Usa Recraft V3 con Comfy Router

Copiar páginaCopiar página

Llama a recraft/recraftv3 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `recraft/recraftv3`, servida por Comfy Router de Recraft. **Entrada:** Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `recraft/recraftv3` **Endpoint:** `POST https://api.comfy.org/v2/models/recraft/recraftv3`

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
            "recraft/recraftv3",
            {
                "n": 1,
                "prompt": "A single red maple leaf on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("recraft/recraftv3", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/recraft/recraftv3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/recraft/recraftv3/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "recraft/recraftv3",
                {
                    "n": 1,
                    "prompt": "A single red maple leaf on a plain white background.",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
            # Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("recraft/recraftv3", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que necesita otro proceso
    
    // Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/recraft/recraftv3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    
    # 2. Consulta en bucle hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/recraft/recraftv3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/recraft/recraftv3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

controls

object

Los controles de la imagen generada

​

controls.artistic_level

integer

Define el tono artístico de tu imagen. En un nivel simple, la persona mira directamente a la cámara con un estilo estático y limpio. Los niveles dinámicos y excéntricos introducen movimiento y creatividad.Rango: `0` a `5`

​

controls.background_color

object

Valores de color RGB

​

controls.background_color.rgb

integer[]

requerido

​

controls.colors

object[]

Un arreglo de colores preferidos

​

controls.colors[].rgb

integer[]

requerido

​

controls.no_text

boolean

No incrustar diseños de texto

​

model

string

El modelo que se usará para la generación (por ejemplo, “recraftv3”). Este campo NO está restringido a un enum: el proxy reenvía lo que envíe quien llama. Las grafías que Comfy distribuye (el conjunto que Comfy Router direcciona como `recraft/<model>`) son recraftv2, recraftv3, recraftv4, recraftv4_pro, recraftv4_1, recraftv4_1_utility, recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_styles, recraftv4_styles_pro, recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_styles_vector y recraftv4_styles_pro_vector. Se escriben aquí en lugar de nombrarlas por referencia porque el componente RecraftGenerationModel que las declara no recibe `$ref` desde ningún lado y por eso queda podado de la especificación que se sirve en GET /openapi, así que un puntero hacia él quedaría colgando en el documento servido. Las cuatro grafías `recraftv4_styles*` además requieren `style_id`; consulta ese campo.

​

n

integer

La cantidad de imágenes a generar. Recraft acepta de 1 a 6.Rango: `1` a `6`

​

prompt

string

requerido

El prompt de texto que describe la imagen a generar

​

response_format

string

Valores posibles: `url`, `b64_json`

​

size

string

El tamaño de la imagen generada (por ejemplo, “1024x1024”)

​

style

string

El estilo que se aplicará a la imagen generada (por ejemplo, “digital_illustration”)

​

style_id

string

El ID de estilo que se aplicará a la imagen generada (por ejemplo, “123e4567-e89b-12d3-a456-426614174000”). Si se proporciona style_id, no se debe proporcionar style. Requerido por los cuatro modelos `recraftv4_styles*`: Recraft los rechaza si no hay un style_id o una referencia de estilo. Genera uno con `POST /proxy/recraft/styles`, que este mismo proxy sirve con las mismas credenciales. Nada en esta ruta hace cumplir la pareja: el cuerpo se reenvía a Recraft sin cambios, así que una llamada a `recraftv4_styles*` sin él llega al socio y regresa con un 4xx.

Generado a partir del esquema que Router sirve en `GET /v2/models/recraft/recraftv3/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

created

integer

requerido

Marca de tiempo Unix de cuando se creó la generación

​

credits

integer

requerido

Cantidad de créditos usados para la generación

​

data

object[]

requerido

Arreglo con la información de las imágenes generadas

​

data[].b64_json

string

Datos de la imagen codificados en Base64 (se incluye en lugar de `url` cuando la solicitud estableció `response_format: b64_json`)

​

data[].image_id

string

Identificador único de la imagen generada

​

data[].url

string

URL para acceder a la imagen generada (se incluye cuando `response_format` es `url`, el valor predeterminado)

​

style_id

string

El id de estilo resuelto, que Recraft devuelve cuando se usan referencias de estilo (notablemente en los modelos con entrada requerida recraftv4_styles*); se puede reutilizar como `style_id` en solicitudes posteriores.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "n": 1,
      "prompt": "A single red maple leaf on a plain white background."
    }
    

### 

​

Salida
    
    
    {
      "created": 1767225600,
      "credits": 1,
      "data": [
        {
          "image_id": "3f7a1b28-5c0d-4e91-8a6f-1b2c3d4e5f60",
          "url": "https://example.invalid/recraft/recraftv3/generated.png"
        }
      ]
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/recraft/recraftv3/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/recraft/recraftv3/code)

[Recraft V2](https://docs.comfy.org/es/development/comfy-router/models/recraft/recraftv2/code)[Recraft V4.1 Pro Vector](https://docs.comfy.org/es/development/comfy-router/models/recraft/recraftv4-1-pro-vector/code)
