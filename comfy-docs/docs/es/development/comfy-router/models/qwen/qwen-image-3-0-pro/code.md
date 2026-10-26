---
url: https://docs.comfy.org/es/development/comfy-router/models/qwen/qwen-image-3-0-pro/code/
title: Usa Qwen Image 3.0 Pro con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:16.854849+00:00
---

# Usa Qwen Image 3.0 Pro con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/qwen/qwen-image-3-0-pro/code/

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



Qwen

# Usa Qwen Image 3.0 Pro con Comfy Router

Copiar páginaCopiar página

Llama a qwen/qwen-image-3.0-pro con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `qwen/qwen-image-3.0-pro`, servida por Comfy Router desde Qwen. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los ejemplos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el ejemplo de cURL es la misma llamada por HTTP directo. **ID del modelo:** `qwen/qwen-image-3.0-pro` **Endpoint:** `POST https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro`

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
            "qwen/qwen-image-3.0-pro",
            {
                "input": {
                    "messages": [
                        {
                            "content": [
                                {
                                    "text": "A single red maple leaf on a plain white background.",
                                },
                            ],
                            "role": "user",
                        },
                    ],
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("qwen/qwen-image-3.0-pro", {
      input: {
        messages: [
          {
            content: [
              {
                text: "A single red maple leaf on a plain white background.",
              },
            ],
            role: "user",
          },
        ],
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"messages\":[{\"content\":[{\"text\":\"A single red maple leaf on a plain white background.\"}],\"role\":\"user\"}]}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "qwen/qwen-image-3.0-pro",
                {
                    "input": {
                        "messages": [
                            {
                                "content": [
                                    {
                                        "text": "A single red maple leaf on a plain white background.",
                                    },
                                ],
                                "role": "user",
                            },
                        ],
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
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
    const handle = await comfy.models.submit("qwen/qwen-image-3.0-pro", {
      input: {
        messages: [
          {
            content: [
              {
                text: "A single red maple leaf on a plain white background.",
              },
            ],
            role: "user",
          },
        ],
      },
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"messages\":[{\"content\":[{\"text\":\"A single red maple leaf on a plain white background.\"}],\"role\":\"user\"}]}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indique cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

input

object

requerido

El objeto de parámetros de entrada que contiene los mensajes de la solicitud

​

input.messages

object[]

requerido

El arreglo de contenido de la solicitud. Solo se admiten conversaciones de un solo turno, por lo que el arreglo debe contener exactamente un objeto

​

input.messages[].content

object[]

requerido

El arreglo de contenido del mensaje. La generación de texto a imagen contiene un objeto de texto; la edición de imágenes contiene de 1 a 3 objetos de imagen y un objeto de texto

​

input.messages[].content[].image

string

La URL o los datos codificados en Base64 de una imagen de entrada. Se admiten de 1 a 3 imágenes para la edición de imágenes

​

input.messages[].content[].text

string

El prompt positivo que describe el contenido, el estilo y la composición de la imagen que se va a generar o editar

​

input.messages[].role

string

requerido

El rol del remitente del mensaje. Debe establecerse en userValores posibles: `user`

​

model

string

El ID del modelo que se llama para la generación y edición de imágenes multimodales. Los valores disponibles son qwen-image-3.0-pro y qwen-image-3.0. NO aparece en la lista `required` de este esquema porque Comfy Router lo completa a partir del segmento de ruta `{model}` de /v2/models/qwen/{model}, así que quien llama al Router lo omite; en cambio, una llamada directa v1 a la ruta /proxy/ debe proporcionarlo.

​

parameters

object

Parámetros adicionales para controlar la generación de imágenes

​

parameters.n

integer

predeterminado:"1"

La cantidad de imágenes de salida. Alcance 1-6, el valor predeterminado es 1Rango: `1` a `6`

​

parameters.negative_prompt

string

El prompt negativo que describe el contenido que no quieres que aparezca en la imagen

​

parameters.prompt_extend

boolean

predeterminado:"true"

Si se habilita la reescritura inteligente del prompt. El valor predeterminado es true

​

parameters.prompt_extend_mode

string

predeterminado:"\"direct\""

El método de reescritura del prompt, direct (predeterminado, compatible con T2I e I2I) o agent (solo T2I)Valores posibles: `direct`, `agent`

​

parameters.seed

integer

Semilla numérica aleatoria para controlar la aleatoriedad. Rango [0, 2147483647]Rango: `0` a `2147483647`

​

parameters.size

string

La resolución de la imagen de salida en el formato ancho _alto, por ejemplo 1024_ 1024\. La API acepta un área en píxeles entre 262144 (512 _512) y 6553600 (2560_ 2560) con una relación de aspecto entre 1:8 y 8:1. Si no se especifica, el modelo recomienda automáticamente una resolución basada en el prompt

​

parameters.watermark

boolean

predeterminado:"false"

Si se agrega una marca de agua. El valor predeterminado es false

Generado a partir del esquema que Router sirve en `GET /v2/models/qwen/qwen-image-3.0-pro/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

code

string

El código de error de la solicitud fallida (no se devuelve si la solicitud tiene éxito)

​

message

string

Información detallada sobre la solicitud fallida (no se devuelve si la solicitud tiene éxito)

​

output

object

Contiene los resultados de generación del modelo

​

output.choices

object[]

La lista de opciones de resultado

​

output.choices[].finish_reason

string

El motivo por el que se detuvo la tarea. El valor es stop cuando la tarea finaliza normalmente

​

output.choices[].message

object

El mensaje que devuelve el modelo

​

output.choices[].message.content

object[]

El contenido del mensaje que contiene la información de la imagen generada

​

output.choices[].message.content[].image

string

La URL de la imagen generada en formato PNG. El enlace es válido durante 24 horas

​

output.choices[].message.content[].text

string

Un elemento textual que se devuelve en lugar de una imagen. Un elemento que solo lleva este campo NO produjo ningún recurso, así que quien llama debe basarse en `image` para determinar la finalización y no en la presencia de un elemento de contenido

​

output.choices[].message.role

string

El rol del mensaje. Fijo como assistant

​

request_id

string

Identificador único de la solicitud

​

usage

object

El uso de recursos de esta llamada. Solo se devuelve en caso de éxito

​

usage.input_image_count

integer

La cantidad de imágenes de entrada en la solicitud. Devuelve 0 para texto a imagen

​

usage.input_image_type

string

El nivel de facturación de la imagen de entrada, qima_input_1k o qima_input_2k, determinado por el área en píxeles de la resolución de salida

​

usage.output_height

integer

La altura de la imagen de salida final en píxeles

​

usage.output_image_count

integer

La cantidad real de imágenes de salida devueltas

​

usage.output_image_type

string

El nivel de facturación de la imagen de salida, qima_output_1k o qima_output_2k, determinado por el área en píxeles de la resolución de salida

​

usage.output_width

integer

El ancho de la imagen de salida final en píxeles

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input": {
        "messages": [
          {
            "content": [
              {
                "text": "A single red maple leaf on a plain white background."
              }
            ],
            "role": "user"
          }
        ]
      }
    }
    

### 

​

Salida
    
    
    {
      "output": {
        "choices": [
          {
            "finish_reason": "stop",
            "message": {
              "content": [
                {
                  "image": "https://example.invalid/qwen/generated.png"
                }
              ],
              "role": "assistant"
            }
          }
        ]
      },
      "request_id": "9f2c1b3a-5d4e-4a67-8b90-1c2d3e4f5a6b",
      "usage": {
        "input_image_count": 0,
        "output_height": 512,
        "output_image_count": 1,
        "output_image_type": "qima_output_1k",
        "output_width": 512
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/qwen/qwen-image-3-0-pro/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/qwen/qwen-image-3-0-pro/code)

[P Video 2](https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code)[Qwen Image 3.0](https://docs.comfy.org/es/development/comfy-router/models/qwen/qwen-image-3-0/code)
