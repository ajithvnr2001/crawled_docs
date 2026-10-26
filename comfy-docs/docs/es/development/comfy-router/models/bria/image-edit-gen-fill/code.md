---
url: https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-gen-fill/code/
title: Usa Image Edit Gen Fill con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:58.582284+00:00
---

# Usa Image Edit Gen Fill con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-gen-fill/code/

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

# Usa Image Edit Gen Fill con Comfy Router

Copiar páginaCopiar página

Llama a bria/image-edit-gen-fill mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `bria/image-edit-gen-fill`, servida por Comfy Router desde Bria. **Entrada:** Imagen, Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `bria/image-edit-gen-fill` **Endpoint:** `POST https://api.comfy.org/v2/models/bria/image-edit-gen-fill`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    with Comfy() as client:
        result = client.models.run(
            "bria/image-edit-gen-fill",
            {
                "image": "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAC2klEQVR42u3TQQ0AQAgEMeTgX8W5gi8OjoROVgGhUdLhwgkEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAAkACQAJAAkACQAJAAkACQAJAAkACQAFjSy7SPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8IIAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASABIAEgASABIAEgASABIAEgASABIAEgASABIAAgACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkAadSRm+WukYdfewAAAABJRU5ErkJggg==",
                "mask": "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAB+klEQVR42u3TMQEAAAzCMPyb3l4c8CQa2gQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJg7phRoAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwABI0AAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAeuAhLMg9zyQgAAAAASUVORK5CYII=",
                "prompt": "a small green leaf",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("bria/image-edit-gen-fill", {
      image: "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAC2klEQVR42u3TQQ0AQAgEMeTgX8W5gi8OjoROVgGhUdLhwgkEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAAkACQAJAAkACQAJAAkACQAJAAkACQAFjSy7SPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8IIAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASABIAEgASABIAEgASABIAEgASABIAEgASABIAAgACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkAadSRm+WukYdfewAAAABJRU5ErkJggg==",
      mask: "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAB+klEQVR42u3TMQEAAAzCMPyb3l4c8CQa2gQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJg7phRoAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwABI0AAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAeuAhLMg9zyQgAAAAASUVORK5CYII=",
      prompt: "a small green leaf",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bria/image-edit-gen-fill \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAC2klEQVR42u3TQQ0AQAgEMeTgX8W5gi8OjoROVgGhUdLhwgkEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAAkACQAJAAkACQAJAAkACQAJAAkACQAFjSy7SPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8IIAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASABIAEgASABIAEgASABIAEgASABIAEgASABIAAgACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkAadSRm+WukYdfewAAAABJRU5ErkJggg==\", \"mask\": \"iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAB+klEQVR42u3TMQEAAAzCMPyb3l4c8CQa2gQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJg7phRoAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwABI0AAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAeuAhLMg9zyQgAAAAASUVORK5CYII=\", \"prompt\": \"a small green leaf\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bria/image-edit-gen-fill/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "bria/image-edit-gen-fill",
                {
                    "image": "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAC2klEQVR42u3TQQ0AQAgEMeTgX8W5gi8OjoROVgGhUdLhwgkEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAAkACQAJAAkACQAJAAkACQAJAAkACQAFjSy7SPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8IIAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASABIAEgASABIAEgASABIAEgASABIAEgASABIAAgACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkAadSRm+WukYdfewAAAABJRU5ErkJggg==",
                    "mask": "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAB+klEQVR42u3TMQEAAAzCMPyb3l4c8CQa2gQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJg7phRoAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwABI0AAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAeuAhLMg9zyQgAAAAASUVORK5CYII=",
                    "prompt": "a small green leaf",
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    const handle = await comfy.models.submit("bria/image-edit-gen-fill", {
      image: "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAC2klEQVR42u3TQQ0AQAgEMeTgX8W5gi8OjoROVgGhUdLhwgkEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAAkACQAJAAkACQAJAAkACQAJAAkACQAFjSy7SPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8IIAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASABIAEgASABIAEgASABIAEgASABIAEgASABIAAgACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkAadSRm+WukYdfewAAAABJRU5ErkJggg==",
      mask: "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAB+klEQVR42u3TMQEAAAzCMPyb3l4c8CQa2gQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJg7phRoAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwABI0AAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAeuAhLMg9zyQgAAAAASUVORK5CYII=",
      prompt: "a small green leaf",
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/bria/image-edit-gen-fill/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAC2klEQVR42u3TQQ0AQAgEMeTgX8W5gi8OjoROVgGhUdLhwgkEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAAkACQAJAAkACQAJAAkACQAJAAkACQAFjSy7SPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8IIAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASABIAEgASABIAEgASABIAEgASABIAEgASABIAAgACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkAadSRm+WukYdfewAAAABJRU5ErkJggg==\", \"mask\": \"iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAB+klEQVR42u3TMQEAAAzCMPyb3l4c8CQa2gQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJg7phRoAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwABI0AAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAeuAhLMg9zyQgAAAAASUVORK5CYII=\", \"prompt\": \"a small green leaf\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bria/image-edit-gen-fill/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/bria/image-edit-gen-fill/requests/$REQUEST_ID \
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

La imagen que se va a editar. Los tipos de entrada admitidos son una cadena codificada en Base64 o una URL que apunte a un archivo de imagen accesible públicamente. Formatos aceptados: JPEG, JPG, PNG, WEBP.

​

mask

string

requerido

La máscara que define el área a rellenar. Cadena codificada en Base64 o URL que apunte a un archivo de imagen accesible públicamente. Los píxeles blancos (255) marcan la región en la que se generará, los píxeles negros (0) se conservan.

​

negative_prompt

string

Un prompt de texto que especifica conceptos, estilos u objetos que se deben excluir del área generada.

​

preserve_alpha

boolean

Controla si las áreas parcialmente transparentes de la imagen de entrada se conservan en la salida.

​

prompt

string

requerido

Descripción de texto de lo que se debe generar dentro del área enmascarada.

​

prompt_content_moderation

boolean

Cuando está habilitado, aplica moderación de contenido al prompt. Devuelve 422 si el prompt no supera la moderación.

​

refine_prompt

boolean

Cuando es verdadero (predeterminado), el prompt se ajusta automáticamente para obtener resultados de generación óptimos.

​

seed

integer

Semilla para la generación determinista. Si se omite, se usa una semilla aleatoria.

​

sync

boolean

Cuando es `false` (predeterminado), la solicitud se procesa de forma asíncrona. Cuando es verdadero, la API mantiene la conexión abierta hasta que finaliza. En COMFY ROUTER ese segundo modo se rechaza en lugar de reenviarse: Router fija el modo de retorno antes del despacho y consulta el resultado dentro de la llamada, de modo que `POST /v2/models/bria/{model}` responde 422 invalid_input para cualquier `sync` que esta ruta transporte distinto de `false` o `null`. La llamada síncrona sigue disponible en la ruta `/proxy/` propia de esta operación, que es la superficie que también describe este esquema.

​

visual_input_content_moderation

boolean

Cuando está habilitado, aplica moderación de contenido a la entrada visual. Devuelve 422 si la imagen no supera la moderación.

​

visual_output_content_moderation

boolean

Cuando está habilitado, aplica moderación de contenido al resultado visual. Devuelve 422 si la salida no supera la moderación.

Generado a partir del esquema que Router sirve en `GET /v2/models/bria/image-edit-gen-fill/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

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

Versión refinada del prompt, o null en una generación COMPLETED que Bria no refinó. Es anulable porque la clave está PRESENTE y contiene null en lugar de omitirse; observado en vivo en bria/image-edit-gen-fill.

​

result.seed

integer

Semilla utilizada para la generación.

​

result.structured_instruction

string

La instrucción estructurada, un documento JSON serializado como cadena, que devuelve `/v2/structured_instruction/generate`. Esa operación no completa ninguna de las dos URL.

​

result.structured_prompt

string

El prompt estructurado JSON detallado.

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
      "image": "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAC2klEQVR42u3TQQ0AQAgEMeTgX8W5gi8OjoROVgGhUdLhwgkEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAEgASABIAAkACQAJAAkACQAJAAkACQAJAAkACQAFjSy7SPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8IIAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASABIAEgASABIAEgASABIAEgASABIAEgASABIAAgACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkACQAJAAkAadSRm+WukYdfewAAAABJRU5ErkJggg==",
      "mask": "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAAB+klEQVR42u3TMQEAAAzCMPyb3l4c8CQa2gQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJg7phRoAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAANgAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYAAMYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwAAYwABI0AAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGwAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAGMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAeuAhLMg9zyQgAAAAASUVORK5CYII=",
      "prompt": "a small green leaf"
    }
    

### 

​

Salida
    
    
    {
      "request_id": "0b3f9d7e-2c41-4a8b-9f10-6d5c8e2a4b71",
      "result": {
        "image_url": "https://example.invalid/bria/image-edit-remove-background/generated.png",
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/bria/image-edit-gen-fill/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/bria/image-edit-gen-fill/code)

[Image Edit Expand](https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-expand/code)[Image Edit Increase Resolution](https://docs.comfy.org/es/development/comfy-router/models/bria/image-edit-increase-resolution/code)
