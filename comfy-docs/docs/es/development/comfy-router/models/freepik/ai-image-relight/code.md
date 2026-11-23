---
url: https://docs.comfy.org/es/development/comfy-router/models/freepik/ai-image-relight/code/
title: Usa AI Image Relight con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-23T19:03:20.923062+00:00
---

# Usa AI Image Relight con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/freepik/ai-image-relight/code/

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



Freepik

# Usa AI Image Relight con Comfy Router

Copiar páginaCopiar página

Llama a freepik/ai-image-relight con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `freepik/ai-image-relight`, servido por Comfy Router desde Freepik. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `freepik/ai-image-relight` **Endpoint:** `POST https://api.comfy.org/v2/models/freepik/ai-image-relight`

  * Esperar el resultado

  * Encolar y obtener más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "freepik/ai-image-relight",
            {
                "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
                "prompt": "warm golden-hour sunlight from the left",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("freepik/ai-image-relight", {
      image: "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      prompt: "warm golden-hour sunlight from the left",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/freepik/ai-image-relight \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\", \"prompt\": \"warm golden-hour sunlight from the left\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/freepik/ai-image-relight/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se obtiene cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la obtención del resultado.

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
                "freepik/ai-image-relight",
                {
                    "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
                    "prompt": "warm golden-hour sunlight from the left",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o fue cancelada lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("freepik/ai-image-relight", {
      image: "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      prompt: "warm golden-hour sunlight from the left",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o fue cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/freepik/ai-image-relight/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\", \"prompt\": \"warm golden-hour sunlight from the left\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/freepik/ai-image-relight/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/freepik/ai-image-relight/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

advanced_settings

object

advanced_settings.blacks

integer

predeterminado:"50"

Ajusta el nivel de color negro en la imagen.Alcance: `0` a `100`

advanced_settings.brightness

integer

predeterminado:"50"

Ajusta el nivel de brillo en la imagen.Alcance: `0` a `100`

advanced_settings.contrast

integer

predeterminado:"50"

Ajusta el nivel de contraste en la imagen.Alcance: `0` a `100`

advanced_settings.engine

string

predeterminado:"\"automatic\""

Preajuste de motor para la reiluminación:

  * balanced: opción equilibrada y de uso general
  * cool: más brillante, con tonos más fríos
  * real: busca mejorar la calidad fotográfica (experimental)
  * illusio: optimizado para ilustraciones y dibujos
  * fairy: adecuado para imágenes de temática fantástica
  * colorful_anime: ideal para anime, dibujos animados y colores vibrantes
  * hard_transform: modifica significativamente la imagen original
  * softy: efecto un poco más suave, adecuado para diseños gráficos Valores posibles: `automatic`, `balanced`, `cool`, `real`, `illusio`, `fairy`, `colorful_anime`, `hard_transform`, `softy`



advanced_settings.fixed_generation

boolean

predeterminado:"false"

Al activarlo, usar las mismas configuraciones genera siempre la misma imagen.

advanced_settings.saturation

integer

predeterminado:"50"

Ajusta el nivel de saturación en la imagen.Alcance: `0` a `100`

advanced_settings.transfer_light_a

string

predeterminado:"\"automatic\""

Ajusta la intensidad de la transferencia de luz.Valores posibles: `automatic`, `low`, `medium`, `normal`, `high`, `high_on_faces`

advanced_settings.transfer_light_b

string

predeterminado:"\"automatic\""

También modifica la intensidad de la transferencia de luz. Puedes combinarlo con transfer_light_a para obtener efectos variados.Valores posibles: `automatic`, `composition`, `straight`, `smooth_in`, `smooth_out`, `smooth_both`, `reverse_both`, `soft_in`, `soft_out`, `soft_mid`, `strong_mid`, `style_shift`, `strong_shift`

advanced_settings.whites

integer

predeterminado:"50"

Ajusta el nivel de color blanco en la imagen.Alcance: `0` a `100`

change_background

boolean

predeterminado:"true"

Al activarlo, cambia el fondo según el prompt o la imagen de referencia. Útil para ubicación de productos y retratos.

image

string

requerido

Base64 o URL de la imagen que se va a reiluminar

interpolate_from_original

boolean

predeterminado:"false"

Al activarlo, la imagen final se interpola a partir de la original usando el control de intensidad de la transferencia de luz.

light_transfer_strength

integer

predeterminado:"100"

Nivel de intensidad de la transferencia de luz. 0% mantiene el resultado más cercano al original, 100% es la transferencia máxima.Alcance: `0` a `100`

preserve_details

boolean

predeterminado:"true"

Conserva la textura y los detalles pequeños de la imagen original. Útil para fotografía de productos, textos, etc.

prompt

string

Puedes guiar el proceso de generación e influir en la transferencia de luz con un prompt descriptivo. IMPORTANTE: puedes enfatizar aspectos específicos de la luz en tu prompt usando un número entre paréntesis, de 1 a 1.4, como “(dark scene:1.3)”.

style

string

predeterminado:"\"standard\""

Preajuste de estilo para la operación de reiluminación.Valores posibles: `standard`, `darker_but_realistic`, `clean`, `smooth`, `brighter`, `contrasted_n_hdr`, `just_composition`

transfer_light_from_lightmap

string

Base64 o URL del mapa de luz para la transferencia de luz. Incompatible con ‘transfer_light_from_reference_image’

transfer_light_from_reference_image

string

Base64 o URL de la imagen de referencia para la transferencia de luz. Incompatible con ‘transfer_light_from_lightmap’

webhook_url

string (uri)

URL de callback opcional que recibirá notificaciones asíncronas cada vez que la tarea cambie de estado.Formato: `uri`

Generado a partir del esquema que Router sirve en `GET /v2/models/freepik/ai-image-relight/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

data

object

requerido

data.generated

string (uri)[]

requerido

Las URL de las imágenes de la generación finalizada. Presentes y no vacías en el documento que devuelve Router; esta lista ES el resultado. Los enlaces son propios de Freepik y caducan.

data.status

string

requerido

Valores posibles: `COMPLETED`

data.task_id

string (uuid)

Formato: `uuid`

## Ejemplos

### Entrada
    
    
    {
      "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      "prompt": "warm golden-hour sunlight from the left"
    }
    

### Salida
    
    
    {
      "data": {
        "generated": [
          "https://example.invalid/freepik/ai-image-relight/relit.png"
        ],
        "status": "COMPLETED",
        "task_id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
      }
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/freepik/ai-image-relight/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/freepik/ai-image-relight/code)

[Patina](https://docs.comfy.org/es/development/comfy-router/models/fal/patina/code)[AI Image Style Transfer](https://docs.comfy.org/es/development/comfy-router/models/freepik/ai-image-style-transfer/code)
