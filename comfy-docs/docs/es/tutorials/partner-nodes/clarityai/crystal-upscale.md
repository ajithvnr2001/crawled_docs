---
url: https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-upscale/
title: Clarity AI Crystal Upscaler en ComfyUI: ampliaci\u00f3n fiel - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.663881+00:00
---

# Clarity AI Crystal Upscaler en ComfyUI: ampliación fiel - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-upscale/

## En esta página

Volver arriba

  * Flujos de trabajo disponibles
    * Ampliación de imagen
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Controles del nodo
  * Consejos
  * Empezar



Clarity AI

# Clarity AI Crystal Upscaler en ComfyUI: ampliación fiel

Copiar páginaCopiar página

Amplía imágenes con Crystal Upscaler de Clarity AI en ComfyUI: restauración fiel de detalles hasta 100 megapíxeles, con factor de escala y control de creatividad.

Copiar páginaCopiar página

**Clarity AI Crystal Upscaler** es un ampliador de imágenes de alta fidelidad en ComfyUI. En lugar de inventar contenido nuevo, vuelve a renderizar la imagen a un tamaño mayor manteniéndose fiel al original: los rostros, la piel y la textura fina recuperan su nitidez, y la estructura de la imagen se conserva. Está pensado para retratos, fotos de producto y ampliaciones listas para impresión, donde el detalle fiel importa más que una reinterpretación creativa. En ComfyUI el modelo se ejecuta a través del nodo asociado **Clarity AI Crystal Upscale**. Es un nodo de API en la nube: necesita una cuenta de Comfy con créditos y no descarga ningún modelo local. Entra una imagen y sale una imagen ampliada, junto con una comparación lado a lado. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver la tarifa por megapíxel. La salida está limitada a 100 megapíxeles y 65535 píxeles por lado. El nodo multiplica el ancho y el alto de la entrada por el `scale_factor`, así que una fuente más pequeña o un factor menor es la manera de mantenerte dentro del límite.

## 

​

Flujos de trabajo disponibles

### 

​

Ampliación de imagen

Amplía una sola imagen y compara el resultado con el original. La plantilla carga una imagen de origen, la amplía a 2x y muestra una vista de `ImageCompare` con la entrada y la salida. ![Vista previa del flujo de trabajo de Clarity AI Crystal Upscale](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_upscale-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Clarity AI: Crystal Upscaler” en la Biblioteca de plantillas

**Material de entrada**

## watch_spa_black.png

Carga esta imagen en el nodo `LoadImage` que alimenta al nodo Clarity AI Crystal Upscale

### 

​

Resumen del flujo de trabajo

La plantilla usa cuatro nodos:

  * **LoadImage** : proporciona la imagen de origen
  * **ClarityCrystalUpscaleNode** : el nodo principal, configurado con el modelo `crystal-upscaler`
  * **SaveImageAdvanced** : guarda la salida ampliada como PNG
  * **ImageCompare** : muestra el resultado ampliado junto al original



### 

​

Pasos para ejecutar

  1. **Cargar una imagen** : sube o selecciona tu imagen de origen en el nodo **LoadImage**
  2. **Seleccionar el modelo** : mantén `crystal-upscaler` en el nodo **Clarity AI Crystal Upscale**
  3. **Establecer el factor de escala** : elige cuánto ampliar la imagen, de 1x a 200x
  4. **Establecer la creatividad** : `0` se mantiene lo más cerca posible del original; los valores más altos permiten que el modelo reconstruya más detalles
  5. **Haz clic en Queue** o presiona `Ctrl+Enter` para generar



## 

​

Controles del nodo

Control| Valores| Efecto  
---|---|---  
`image`| una imagen| Imagen de origen. El nodo acepta exactamente una imagen; se rechaza un lote  
`scale_factor`| 1.0 a 200.0, predeterminado 2.0| Multiplica el ancho y el alto de la entrada. La salida está limitada a 100 megapíxeles y 65535 píxeles por lado  
`creativity`| 0 a 10, predeterminado 0| `0` conserva el original con mayor fidelidad. Los valores más altos permiten que el modelo reconstruya más detalle en lugar de seguir estrictamente la fuente. No tiene efecto cuando el lado más corto de la imagen es de 256 píxeles o menos  
  
## 

​

Consejos

  * **Empieza con 2x y sube el factor solo si lo necesitas**. El factor multiplica ambos lados de la imagen, así que un factor grande puede llevar la salida por encima de 100 megapíxeles o de 65535 píxeles por lado y hacer que la ejecución falle.
  * **Configura`creativity` en 0 para fotos de producto y de archivo**. Así se mantiene lo más cerca posible de la fuente; súbelo solo cuando quieras que el modelo reconstruya textura que la fuente ya no contiene.
  * **Las entradas pequeñas ignoran`creativity`**. Las imágenes cuyo lado más corto mide 256 píxeles o menos dan el mismo resultado independientemente del valor.
  * **Revisa la vista de comparación**. La plantilla empareja la salida con la entrada, así que puedes juzgar si el detalle añadido es fiel antes de lanzar un renderizado grande.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Clarity AI: Crystal Upscaler`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/clarityai/crystal-upscale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/clarityai/crystal-upscale)

[Seedream 5 Lite](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-lite)[Nano Banana 2.1](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-1)
