---
url: https://docs.comfy.org/es/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer/
title: Higgsfield Genjutsu en ComfyUI: transferencia de movimiento de video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:50.023587+00:00
---

# Higgsfield Genjutsu en ComfyUI: transferencia de movimiento de video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer/

## En esta página

Volver arriba

  * Higgsfield Genjutsu: transferencia de movimiento
  * Controles del nodo
  * Consejos para el prompt
  * Empezar



Higgsfield

# Higgsfield Genjutsu en ComfyUI: transferencia de movimiento de video

Copiar páginaCopiar página

Higgsfield Genjutsu en ComfyUI: cambia el reparto de un video con 1 a 8 imágenes de referencia; el clip fuente conserva movimiento, cámara y audio.

Copiar páginaCopiar página

**Higgsfield Genjutsu Motion Transfer** reconstruye un video existente en lugar de generar uno nuevo. El clip de origen conserva su movimiento, el movimiento de cámara, el ritmo y el audio, mientras que el elenco, la locación, el vestuario y el estilo se reconstruyen a partir de 1 a 8 imágenes de referencia. Tú describes qué debería ser distinto y el resto de la toma se queda tal como se filmó. Higgsfield ofrece Genjutsu en dos modos, Motion Transfer y Object Swap. ComfyUI expone Motion Transfer a través del nodo `HiggsfieldMotionTransferNode` en la categoría `partner/video/Higgsfield`. Es un nodo de API en la nube: necesita una cuenta de Comfy con créditos, no descarga ningún modelo y cobra por segundo de salida, porque la duración del resultado sigue al clip de origen. El nodo resulta útil cuando la actuación ya existe y solo hay que cambiar el aspecto. Cambia el elenco de un clip de teléfono por otro personaje, traslada una grabación a una locación que nunca estuvo disponible, cambia el estilo del metraje para otro mercado o produce varias variantes de una misma toma sin filmar cada una por separado.

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

Higgsfield Genjutsu: transferencia de movimiento

Transforma un video a partir de imágenes de referencia mientras el clip de origen conserva su movimiento, el movimiento de cámara, el ritmo y el audio.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Higgsfield Genjutsu: Motion Transfer” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos `LoadVideo` y `LoadImage` correspondientes:

## rooftop_dancer.mp4

`LoadVideo` · clip de movimiento de origen

## snow_queen_ref.png

`LoadImage` · referencia de personaje · `image_1`

## ice_palace_ref.png

`LoadImage` · referencia de escena · `image_2`

## 

​

Controles del nodo

Control| Valores| Efecto  
---|---|---  
`model`| `genjutsu-v1.0`| El modelo Genjutsu. Al seleccionarlo, se muestran las entradas a continuación  
`video`| 4 a 30 segundos| Clip fuente del que se conservan el movimiento, el movimiento de cámara, la sincronización y el audio. Se rechaza un clip más corto, y uno más largo se recorta a sus primeros 30 segundos  
`reference_images`| 1 a 8 imágenes| Los personajes, ubicaciones o estilos que se usarán. Conecta una imagen por ranura (`image_1`, `image_2`, y así sucesivamente); una entrada por lotes cuenta una vez por imagen, y el total entre todas las ranuras no puede superar 8  
`prompt`| texto, opcional| Describe el resultado, por ejemplo, qué referencia reemplaza a qué persona, o un nuevo escenario  
`resolution`| `480p`, `720p`, `1080p`| Resolución de salida, por defecto `720p`  
`seed`| entero| Solo controla si el nodo se vuelve a ejecutar. Los resultados pueden variar entre ejecuciones con la misma semilla  
  
La duración de la salida sigue al clip fuente preparado, por lo que un clip de 12 segundos devuelve un video de 12 segundos.

## 

​

Consejos para el prompt

  * **Nombra qué reemplaza cada referencia.** El prompt es opcional, pero es el único lugar donde puedes indicar qué imagen corresponde a cada persona u objeto. Escríbelo como una instrucción breve: por ejemplo, convertir al bailarín en el personaje de la primera imagen de referencia y usar la segunda para el nuevo entorno.
  * **Mantén un conjunto de referencias reducido.** Una imagen por elemento suele ser suficiente: un personaje, una ubicación, un cambio de vestuario o un estilo. Agregar más imágenes le da al modelo más elementos que combinar, lo que hace que el resultado sea menos predecible.
  * **Usa el encuadre que quieres.** La salida conserva el movimiento y la cámara del clip de origen, así que elige un video de origen cuyo encuadre ya se ajuste al resultado. Una actuación en primer plano sigue siendo un primer plano.
  * **Describe el cambio, no toda la escena.** Todo lo que no se menciona en el prompt se reconstruye a partir de las referencias, así que no hace falta repetir el movimiento, el ritmo ni el audio.
  * **Espera variaciones entre ejecuciones.** La semilla no fija el resultado; las mismas configuraciones pueden producir una toma diferente.



## 

​

Empezar

  1. Actualiza ComfyUI a la versión 0.40.0 o posterior
  2. Ve a la **Biblioteca de plantillas** y busca `Higgsfield Genjutsu`
  3. Carga el clip de origen en el nodo `LoadVideo` y las imágenes de referencia en los nodos `LoadImage`
  4. Escribe el prompt, elige una `resolution` y ejecuta el flujo de trabajo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer)

[HeyGen Video 1.0](https://docs.comfy.org/es/tutorials/partner-nodes/heygen/heygen-video-1)[HitPaw](https://docs.comfy.org/es/tutorials/partner-nodes/hitpaw/overview)
