---
url: https://docs.comfy.org/es/interface/features/autogrow-inputs/
title: Entradas din\u00e1micas: ranuras de nodo con crecimiento autom\u00e1tico en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:29.173765+00:00
---

# Entradas dinámicas: ranuras de nodo con crecimiento automático en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/interface/features/autogrow-inputs/

## En esta página

Volver arriba

  * Cómo funcionan las entradas de crecimiento automático
  * Nodos que usan entradas de crecimiento automático



Componentes de funciones

# Entradas dinámicas: ranuras de nodo con crecimiento automático en ComfyUI

Copiar páginaCopiar página

Las entradas de crecimiento automático añaden ranuras nuevas a un nodo al rellenar la última, para recibir más imágenes, máscaras o latentes.

Copiar páginaCopiar página

![Nodo Batch Images con una imagen conectada y una entrada libre debajo](https://mintcdn.com/dripart/U2iZLdB9XBorZSfA/images/interface/features/autogrow/autogrow-1.png?fit=max&auto=format&n=U2iZLdB9XBorZSfA&q=85&s=b702db2e40661333c41b9783a2090f38) Algunos nodos de ComfyUI tienen **entradas de crecimiento automático** , también llamadas **entradas dinámicas**. Estos nodos no muestran una lista fija de ranuras. Agregan otra entrada en cuanto conectas la última que estaba libre, así que un solo nodo puede procesar por lotes dos imágenes o veinte sin ninguna configuración adicional.

## 

​

Cómo funcionan las entradas de crecimiento automático

  1. **Conecta la última entrada libre.** En el ejemplo de esta página, una fuente de imagen está conectada a `image0` en el nodo **Batch Images** , mientras que `image1` sigue libre.
  2. **Observa cómo crece el nodo.** En cuanto rellenas la última entrada libre, el nodo añade una nueva entrada vacía debajo. En la imagen siguiente, la nueva entrada `image2` aparece después de conectar `image1`.
  3. **Repite según sea necesario.** Cada vez que rellenas la última entrada, el nodo vuelve a crecer, hasta alcanzar el número máximo de entradas que permite ese nodo.

![Nodo Batch Images con dos entradas conectadas y una entrada libre recién añadida resaltada](https://mintcdn.com/dripart/U2iZLdB9XBorZSfA/images/interface/features/autogrow/autogrow-2.png?fit=max&auto=format&n=U2iZLdB9XBorZSfA&q=85&s=cafe6c1aa5420a7c2445ff30fb499548) Otros dos detalles que conviene conocer:

  * **El orden importa.** Las entradas se pasan al nodo en el orden en que aparecen, así que `image0` va antes que `image1` y así sucesivamente. Tenlo en cuenta cuando el resultado dependa de la secuencia, por ejemplo cuando procesas por lotes imágenes que pasan por un modelo de video.
  * **La entrada libre es un marcador de posición.** Solo forma parte de los datos del nodo una vez que conectas algo a ella. Un nodo que permite cero entradas se sigue ejecutando cuando todas las ranuras están vacías.



## 

​

Nodos que usan entradas de crecimiento automático

Nodo| Entrada que crece| Entradas máximas  
---|---|---  
**Batch Images**| `image`| 50  
**Batch Masks**| `mask`| 50  
**Batch Latents**| `latent`| 50  
**And** / **Or**| `value`| 10  
**Nano Banana 2** y otros nodos asociados que reciben imágenes de referencia| `image_1`, `image_2`, etcétera| hasta 14 imágenes  
  
Cada nodo decide sus propios límites. Pasa el cursor sobre la entrada en ComfyUI para leer su información emergente cuando no estés seguro de cuántos valores acepta.

El crecimiento automático forma parte del esquema de nodos V3 de ComfyUI. Si escribes nodos personalizados, consulta [Entradas dinámicas](https://docs.comfy.org/es/custom-nodes/v3_migration#dynamic-inputs) para conocer la API de la plantilla `Autogrow`.

## Nodo Batch Images

Combina varias imágenes en un solo lote, con tantas entradas como necesites.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/features/autogrow-inputs.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/features/autogrow-inputs)

[Documentación de nodos](https://docs.comfy.org/es/interface/features/node-docs)[Editor de máscara](https://docs.comfy.org/es/interface/maskeditor)
