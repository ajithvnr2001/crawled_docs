---
url: https://docs.comfy.org/es/development/comfy-router/api/
title: Descripci\u00f3n general de la API de Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:53.438957+00:00
---

# Descripción general de la API de Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/api/

## En esta página

Volver arriba

  * Guías
  * Ejemplos por modelo
  * Próximos pasos



Router API

# Descripción general de la API de Comfy Router

Copiar páginaCopiar página

Cómo funciona la API de Comfy Router: una ruta por ID de modelo y guías de descubrimiento, esquemas, solicitudes en cola, errores y facturación.

Copiar páginaCopiar página

Elige un modelo, revisa su esquema y llama a `POST /v2/models/{provider}/{model}`. La ruta y la autenticación son las mismas para todos los modelos. Cada modelo acepta su propio cuerpo de solicitud nativo y devuelve su propio resultado nativo.

## 

​

Guías

## Descubrir modelos

Enumera el catálogo, recórrelo por páginas y consulta la entrada de un modelo.

## Esquemas y resultados

Obtén el esquema de entrada y salida de un modelo y lee su resultado.

## Solicitudes en cola

Envía una ejecución ahora y luego consúltala, recógela o cancélala más tarde.

## Errores y reintentos

Lee las respuestas de error y reintenta sin un segundo cargo.

## Facturación

Qué se cobra, la facturación por rechazo de política y la conciliación del uso.

## 

​

Ejemplos por modelo

  * [Google Gemini](https://docs.comfy.org/es/development/comfy-router/models/google/gemini/code)
  * [Nano Banana 2](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-2/code)
  * [Nano Banana 2 Lite](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-2-lite/code)
  * [Nano Banana Pro](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-pro/code)
  * [FLUX 1.1 Pro Ultra](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-1-1-pro-ultra-image/code)
  * [FLUX Kontext](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-1-kontext/code)
  * [FLUX Video Upscale](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-video-upscale/code)
  * [FLUX 3 Video](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-3-video/code)
  * [Ideogram 4](https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v4/code)



## 

​

Próximos pasos

  * [Inicio rápido](https://docs.comfy.org/es/development/comfy-router/quickstart): instalación, invocación y guardado de la imagen.
  * [Modelos](https://docs.comfy.org/es/development/comfy-router/models): explora el catálogo y consulta ejemplos de solicitud específicos de cada modelo.
  * [Encabezados](https://docs.comfy.org/es/development/comfy-router/headers): autenticación, idempotencia, IDs de solicitud y ritmo de reintentos.
  * [Referencia de la API](https://docs.comfy.org/es/development/comfy-router/reference): parámetros de los endpoints, esquemas y códigos de respuesta.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/api.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/api)

[Inicio rápido](https://docs.comfy.org/es/development/comfy-router/quickstart)[Descubrir modelos](https://docs.comfy.org/es/development/comfy-router/discover-models)
