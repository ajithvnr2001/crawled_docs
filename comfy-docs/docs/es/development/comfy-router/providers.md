---
url: https://docs.comfy.org/es/development/comfy-router/providers/
title: Proveedores de servicio de Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:26.066981+00:00
---

# Proveedores de servicio de Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/providers/

## En esta página

Volver arriba

  * Cobertura de proveedores



Models

# Proveedores de servicio de Comfy Router

Copiar páginaCopiar página

Consulta qué proveedores pueden servir cada modelo de Comfy Router y cómo seleccionar otro proveedor.

Copiar páginaCopiar página

Todos los modelos usan `POST /v2/models/{provider}/{model}`. Comfy es el proveedor predeterminado. Para los modelos con cobertura alternativa, `model_provider` selecciona otro proveedor sin cambiar el ID del modelo ni el cuerpo de la solicitud. Consulta [`model_provider`, `strict_mode` y `fallback_provider`](https://docs.comfy.org/es/development/comfy-router/reference#post-v2modelsprovidermodel) en la referencia de la API.

## 

​

Cobertura de proveedores

Modelo / proveedor| **Comfy (predeterminado)**| **fal**| **Higgsfield**| **Pika**| **Runware**| **Tencent**| **WaveSpeed**  
---|---|---|---|---|---|---|---  
[Dreamina Seedance 2.0 260128](https://docs.comfy.org/es/development/comfy-router/models/byteplus/dreamina-seedance-2-0-260128/code)| ✓| ✓| ✓| ✓| ✓| -| ✓  
[Dreamina Seedance 2.5 260628](https://docs.comfy.org/es/development/comfy-router/models/byteplus/dreamina-seedance-2-5-260628/code)| ✓| ✓| ✓| -| ✓| -| ✓  
[GPT Image 2](https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2/code)| ✓| ✓| -| ✓| ✓| -| ✓  
[GPT Image 2.5 Flare](https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-5-flare/code)| ✓| ✓| -| -| ✓| -| ✓  
[GPT Image 2.5 Sunburst](https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code)| ✓| ✓| -| -| ✓| -| ✓  
[Kling 3.0 Turbo](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-3-0-turbo/code)| ✓| -| ✓| -| -| -| -  
[Kling V3](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v3/code)| ✓| -| ✓| -| -| ✓| -  
[Nano Banana 2](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-2/code)| ✓| ✓| -| ✓| ✓| -| ✓  
[Nano Banana Pro](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-pro/code)| ✓| ✓| -| ✓| ✓| -| ✓  
[Wan 3.0 Video](https://docs.comfy.org/es/development/comfy-router/models/wan/wan3-0-video/code)| ✓| -| ✓| -| -| -| -  
  
`strict_mode=false` (el valor predeterminado) traduce la solicitud y la respuesta nativas del proveedor seleccionado. Los campos que no se pueden traducir se enumeran en el encabezado de respuesta `X-Comfy-Router-Dropped-Params`.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/providers.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/providers)

[Precios](https://docs.comfy.org/es/development/comfy-router/pricing)[Claude Fable 5.1](https://docs.comfy.org/es/development/comfy-router/models/anthropic/claude-fable-5-1/code)
