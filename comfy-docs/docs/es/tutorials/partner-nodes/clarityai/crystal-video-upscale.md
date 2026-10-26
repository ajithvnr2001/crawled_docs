---
url: https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-video-upscale/
title: Clarity AI Crystal Video Upscaler en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.811194+00:00
---

# Clarity AI Crystal Video Upscaler en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-video-upscale/

## En esta página

Volver arriba

  * Para qué sirve Crystal Video Upscaler
  * Ejemplo de salida
  * Usarlo
  * Flujo de trabajo de Crystal Video Upscaler
    * Pasos para ejecutar
  * Controles del nodo
  * Límites
  * Empezar



Clarity AI

# Clarity AI Crystal Video Upscaler en ComfyUI

Copiar páginaCopiar página

Aumenta la escala de video con el nodo asociado Clarity AI Crystal Video Upscaler de ComfyUI: sube el tamaño de cuadro y conserva la frecuencia de cuadros y el audio.

Copiar páginaCopiar página

**Clarity AI Crystal Video Upscaler** aumenta la resolución de un clip existente en lugar de generar una escena nueva. Vuelve a renderizar cada cuadro a un tamaño mayor manteniéndose cerca de la fuente, de modo que los rostros, los bordes y las texturas finas vuelven más nítidos en lugar de ser reemplazados por detalle inventado. Está pensado para restaurar video de IA comprimido o suave, ampliar clips generados para pantallas grandes y dar a un material editado un acabado más limpio. En ComfyUI, el modelo se ejecuta mediante el nodo asociado **Clarity AI Crystal Video Upscale**. Es un nodo de API en la nube: necesita una cuenta de Comfy con créditos y no descarga ningún modelo local. Conectas un video y obtienes un video ampliado, con la frecuencia de cuadros y la pista de audio de la fuente conservadas. Consulta [Precios de los nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer la tarifa por segundo. El nodo tiene un único control, `scale_factor`, que multiplica el ancho y el alto de cada cuadro. La salida está limitada a 9 megapíxeles por cuadro y 360 megapíxeles-segundo por clip, así que un clip largo o un cuadro que ya es grande vuelve ampliado por menos que el factor que solicitaste en lugar de fallar.

## 

​

Para qué sirve Crystal Video Upscaler

  * **Detalle fiel** : vuelve a renderizar los cuadros a un tamaño mayor manteniéndose fiel a la fuente, en lugar de generar contenido nuevo
  * **Mantiene el clip intacto** : la frecuencia de cuadros y la pista de audio de la fuente se conservan
  * **Un solo control** : `scale_factor` define cuánto más grande es la salida
  * **Límites flexibles** : cuando un clip es demasiado grande o largo, se le aplica upscale con un factor menor en lugar de rechazarlo



## 

​

Ejemplo de salida

Ampliación de un clip de carretera a 2x, con la frecuencia de cuadros y la pista de audio conservadas: ![Vista previa del flujo de trabajo Clarity AI Crystal Video Upscaler](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_video_upscale-1.webp)

## 

​

Usarlo

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI a continuación. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

Para usar los Nodos asociados, debes asegurarte de haber iniciado sesión correctamente y de estar utilizando un entorno de red permitido. Consulta la sección [Descripción general de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview) de la documentación para conocer los requisitos específicos de uso de los Nodos asociados.

  * Usuarios locales

  * Usuarios de Cloud




Asegúrate de que tu ComfyUI esté actualizado.

  * [Descargar ComfyUI](https://www.comfy.org/download)
  * [Guía de actualización](https://docs.comfy.org/es/installation/update_comfyui)

Los flujos de trabajo de esta guía se encuentran en las [Plantillas de flujos de trabajo](https://docs.comfy.org/es/interface/features/template). Si no los encuentras en las plantillas, es posible que tu ComfyUI esté desactualizado.Si faltan nodos al cargar un flujo de trabajo, estas son las posibles razones:

  1. No estás usando la última versión de ComfyUI (versión nocturna)
  2. Algunos nodos fallaron al importarse durante el inicio



  * [Cloud](https://cloud.comfy.org) se actualizará después del lanzamiento estable de ComfyUI.

Por lo tanto, si notas que falta algún nodo central en este documento, puede deberse a que los nuevos nodos centrales aún no se han publicado en la última versión estable. Espera al próximo lanzamiento estable.

## 

​

Flujo de trabajo de Crystal Video Upscaler

Carga un clip, define el factor de escalado y ejecuta. El flujo de trabajo envía el video al nodo Clarity AI Crystal Video Upscale y guarda el resultado escalado.

## Descargar flujo de trabajo

Descarga el JSON o busca “Clarity AI: Crystal Video Upscaler” en la Biblioteca de plantillas

**Material de entrada**

## desert_highway_encounter.mp4

Cárgalo en el nodo `LoadVideo` que alimenta el nodo Clarity AI Crystal Video Upscale

### 

​

Pasos para ejecutar

  1. **Cargar un video** : sube o selecciona tu clip de origen en el nodo **Load Video**
  2. **Definir el factor de escala** : ingresa un valor en el nodo **Clarity AI Crystal Video Upscale**. `2.0` duplica el ancho y el alto
  3. **Haz clic en Queue** o presiona `Ctrl+Enter` para generar



## 

​

Controles del nodo

Control| Valores| Efecto  
---|---|---  
`video`| un video| Clip de origen. La salida conserva su frecuencia de cuadros y su pista de audio  
`model`| `crystal-video-upscaler`| El modelo que llama el nodo  
`scale_factor`| 1.0 a 200.0, predeterminado 2.0| Multiplica el ancho y el alto de la fuente. Se reduce automáticamente cuando el resultado superaría el límite de cuadros o de clip  
  
## 

​

Límites

  * La salida está limitada a **9 megapíxeles por fotograma** y **360 megapíxeles-segundo por clip**. Los clips largos y los fotogramas que ya son grandes se escalan menos que el factor solicitado.
  * Cada lado del video de origen está limitado a 5120 píxeles, y el factor de escala se reduce para ajustarse a ese límite.
  * Los clips por encima de 30 fps cuestan 2x, por encima de 60 fps 3x, y así sucesivamente.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Clarity AI: Crystal Video Upscaler`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/clarityai/crystal-video-upscale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/clarityai/crystal-video-upscale)

[Vcube](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/vcube)[Gemini Omni Flash](https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-omni-flash)
