---
url: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-video-edit/
title: FLUX Video Edit: edici\u00f3n de video con prompts de texto en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.682948+00:00
---

# FLUX Video Edit: edición de video con prompts de texto en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-video-edit/

## En esta página

Volver arriba

  * Para qué sirve la edición de video Flux
  * Ejemplo de salida
  * Usarlo
  * Flujo de trabajo FLUX Video Edit
  * Escribir la instrucción de edición
  * Referencia de opciones del nodo
  * Límites
  * Empezar



Black Forest Labs

# FLUX Video Edit: edición de video con prompts de texto en ComfyUI

Copiar páginaCopiar página

Edita un clip existente en ComfyUI con el nodo asociado FLUX Video Edit: cambia objetos, reestiliza el video o modifica textos y diálogos en pantalla.

Copiar páginaCopiar página

FLUX Video Edit es el endpoint de edición de video guiada por texto de Black Forest Labs, disponible en ComfyUI como nodo asociado. Le pasas un clip de origen y una instrucción en lenguaje natural, y reescribe el metraje para que coincida con esa instrucción. La edición cambia lo que ocurre en la toma, no cómo está rodada. La duración, el encuadre, el movimiento de cámara y la pista de audio provienen del clip de origen, así que el resultado encaja de vuelta en tu edición sin resincronizar nada. Eso lo hace útil para eliminar, añadir o reemplazar objetos, cambiar el estilo del metraje, cambiar el escenario, reescribir el texto en pantalla y reemplazar el diálogo hablado. El nodo se ejecuta por completo en los servidores de Black Forest Labs a través de la API de Comfy. No se requieren descargas de modelos ni una GPU local; necesitas una cuenta de Comfy API con créditos.

## 

​

Para qué sirve la edición de video Flux

  * **Solo instrucciones** : Describe el cambio con palabras, sin máscaras, sin imágenes de referencia y sin entradas de control
  * **Estructura preservada** : La duración, el encuadre, el movimiento de cámara y el audio provienen del clip de origen
  * **Ediciones a nivel de objeto** : Elimina, agrega o reemplaza objetos, personajes y elementos de fondo
  * **Cambio de estilo** : Cambia la apariencia, la iluminación o el entorno del material que ya tienes
  * **Texto y diálogo** : Reescribe el texto en pantalla y reemplaza las líneas habladas
  * **Hasta 15 segundos** : Acepta clips de origen de 0.7 a 15 segundos



## 

​

Ejemplo de salida

Reemplazar al intérprete en un clip existente manteniendo la pose, la iluminación y la cámara:

## 

​

Usarlo

## Llámalo desde código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript y cURL listos para copiar y pegar

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI a continuación. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujo de trabajo FLUX Video Edit

Edita un clip que ya tengas: carga el video, describe el cambio en el prompt y ejecuta. El flujo de trabajo envía el clip a Black Forest Labs mediante el nodo asociado FLUX Video Edit y guarda el clip editado con `SaveVideo`.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Flux Video Edit” en Biblioteca de plantillas

## 

​

Escribir la instrucción de edición

El prompt es el único control creativo, así que vale la pena escribirlo con cuidado:

  * Describe solo lo que cambia en pantalla. Todo lo que no menciones debe permanecer como estaba.
  * Nombra el sujeto y el resultado en la misma frase; por ejemplo, “reemplaza al guitarrista por un gorila en la misma pose”.
  * Escribe la instrucción en lenguaje sencillo, hasta 4096 caracteres. El detalle sobre la forma, el material o la acción se corresponde aproximadamente con cuánto cambia el modelo.
  * Mantén el diálogo de reemplazo cerca de la duración del habla original, ya que la nueva línea tiene que ajustarse al tiempo que ocupa el habla original. Un clip silencioso permanece en silencio.
  * La semilla no hace que una ejecución sea reproducible. FLUX elige su propia semilla, así que la misma instrucción en el mismo clip puede dar un resultado diferente.



## 

​

Referencia de opciones del nodo

Opción| Valores| Predeterminado| Notas  
---|---|---|---  
`video`| clip de origen| Requerido| De 0.7 a 15 segundos, al menos 160x160 píxeles  
`prompt`| texto| Vacío| Qué cambiar, en lenguaje natural, hasta 4096 caracteres  
`auto_downscale`| on / off| on| Reduce la resolución de las fuentes con un área mayor a 1280x704 antes de subirlas, manteniendo la relación de aspecto  
`safety_tolerance`| 0 a 4| 4| Avanzado. Tolerancia de moderación, `0` es la más estricta  
`seed`| 0 a 4294967295| 42| FLUX elige su propia semilla, por lo que los resultados no son deterministas independientemente de este valor  
  
## 

​

Límites

  * Los clips de origen duran entre 0.7 y 15 segundos y deben medir al menos 160x160 píxeles.
  * La salida se renderiza a 24 fps y se limita a aproximadamente 0.9 megapíxeles por fotograma (1280x704), así que si la fuente es más grande, el resultado será más pequeño.
  * El cobro se calcula por segundo de clip. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing).



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Flux Video Edit`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/black-forest-labs/flux-video-edit.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/black-forest-labs/flux-video-edit)

[Flux 3 Video](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-3-video)[Flux Video Upscale](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-video-upscale)
