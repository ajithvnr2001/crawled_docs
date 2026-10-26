---
url: https://docs.comfy.org/es/built-in-nodes/Canny/
title: Canny - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:37.887371+00:00
---

# Canny - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Canny/

Filtros

# Canny - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Extrae todas las líneas de borde de las fotos, como usar un bolígrafo para delinear una foto, dibujando los contornos y los límites de detalle de los objetos.

Copiar páginaCopiar página

Extrae todas las líneas de borde de las fotos, como usar un bolígrafo para delinear una foto, dibujando los contornos y los límites de detalle de los objetos.

## 

​

Principio de funcionamiento

Imagina que eres un artista que necesita usar un bolígrafo para delinear una foto. El nodo Canny actúa como un asistente inteligente, ayudándote a decidir dónde dibujar líneas (bordes) y dónde no. Este proceso es como una tarea de cribado:

  * **El umbral alto** es el «estándar de líneas que deben dibujarse»: solo se dibujarán las líneas de contorno muy obvias y claras, como los contornos faciales de las personas y las estructuras de los edificios.
  * **El umbral bajo** es el «estándar de líneas que definitivamente no deben dibujarse»: los bordes demasiado débiles se ignorarán para evitar dibujar ruido y líneas sin sentido.
  * **Área intermedia** : los bordes entre ambos estándares se dibujarán si se conectan con las «líneas que deben dibujarse», pero no se dibujarán si están aislados.

La salida final es una imagen en blanco y negro, donde las partes blancas son las líneas de borde detectadas y las partes negras son áreas sin bordes.

## 

​

Entradas

Nombre del parámetro| Descripción de la función| Tipo de datos| Tipo de entrada| Predeterminado| Rango  
---|---|---|---|---|---  
`imagen`| Foto original que necesita extracción de bordes| IMAGE| Entrada| -| -  
`umbral_bajo`| Umbral bajo, determina qué tan débiles son los bordes que se ignoran. Los valores más bajos conservan más detalles, pero pueden producir ruido| FLOAT| Widget| 0.4| 0.01-0.99  
`umbral_alto`| Umbral alto, determina qué tan fuertes son los bordes que se conservan. Los valores más altos solo mantienen las líneas de contorno más obvias| FLOAT| Widget| 0.8| 0.01-0.99  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| Imagen de bordes en blanco y negro; las líneas blancas son los bordes detectados y las áreas negras son las partes sin bordes| IMAGE  
  
## 

​

Comparación de parámetros

![Imagen original](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Canny/input.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=b52726f24f334b769b6742dc0af3b7d4) ![Comparación de parámetros](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Canny/compare.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=77aaab6e6c62c1d3cdfa11d0fa4deb2d) **Problemas comunes:**

  * Bordes discontinuos: intenta reducir el umbral alto
  * Demasiado ruido: aumenta el umbral bajo
  * Faltan detalles importantes: reduce el umbral bajo
  * Bordes demasiado irregulares: verifica la calidad y la resolución de la imagen de entrada



> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Canny.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Canny)

[Extractor de puntos clave SDPose](https://docs.comfy.org/es/built-in-nodes/SDPoseKeypointExtractor)[ColorTransfer](https://docs.comfy.org/es/built-in-nodes/ColorTransfer)
