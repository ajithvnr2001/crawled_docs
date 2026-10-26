---
url: https://docs.comfy.org/es/cloud-nodes/overview/
title: Nodos de Comfy Cloud - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:48.040397+00:00
---

# Nodos de Comfy Cloud - ComfyUI

> Source: https://docs.comfy.org/es/cloud-nodes/overview/

## En esta página

Volver arriba

  * Qué es
  * Primeros pasos
  * Nodos disponibles
  * Facturación
  * Limitaciones
  * Relacionado



Nodos de Comfy Cloud

# Nodos de Comfy Cloud

Copiar páginaCopiar página

Ejecuta flujos de trabajo seleccionados en las GPU de Comfy Cloud desde una instalación local de ComfyUI, sin necesidad de suscripción

Copiar páginaCopiar página

Un nodo de Comfy Cloud es un nodo normal de ComfyUI que envía su tarea para que se ejecute en las GPU de Comfy en lugar de en la máquina local. Colócalo en un gráfico como cualquier otro nodo. No se requiere suscripción: basta con una cuenta y créditos, igual que con cualquier otro nodo asociado.

Los nodos de Comfy Cloud ejecutan modelos de código abierto en la nube. No deben confundirse con los Nodos asociados.

## 

​

Qué es

Cada nodo de Comfy Cloud ejecuta un flujo de trabajo fijo sobre una versión de modelo fijada, de modo que un gráfico guardado sigue produciendo el mismo resultado con el tiempo. Tu gráfico, tus prompts y tus entradas permanecen en tu máquina, salvo lo que el nodo envía para ejecutar la tarea.

## 

​

Primeros pasos

Los nodos de Comfy Cloud vienen incluidos con ComfyUI **v0.34.5 o posterior**. Forman parte del núcleo de ComfyUI, así que no hay nada que instalar por separado.

1

Actualizar ComfyUI

Actualiza a la v0.34.5 o posterior. Consulta [Cómo actualizar ComfyUI](https://docs.comfy.org/es/installation/update_comfyui) para las rutas de instalación portable, de escritorio y manual.

2

Reiniciar ComfyUI

Los nodos solo se registran al iniciar, así que no aparecerán hasta que reinicies.

3

Buscar un nodo

Busca **Comfy Cloud** en la biblioteca de nodos y luego conecta uno a tu gráfico como cualquier otro nodo. Cada nodo lleva el sufijo `[BETA]` en su nombre para mostrar.

## 

​

Nodos disponibles

Ocho nodos en el lanzamiento, entre imagen, video y audio:

Nodo| Modalidad  
---|---  
Comfy Cloud Flux 2 Text to Image| Imagen  
Comfy Cloud Mage Flow Text to Image| Imagen  
Comfy Cloud Mage Flow Turbo Text to Image| Imagen  
Comfy Cloud Z-Image Turbo Text to Image| Imagen  
Comfy Cloud MiniMax H3 Text to Video| Video  
Comfy Cloud MiniMax H3 Image to Video| Video  
Comfy Cloud MiniMax H3 First-Last Frame to Video| Video  
Comfy Cloud MiniMax Music 3 Text to Audio| Audio  
  
## 

​

Facturación

Los nodos de Comfy Cloud se facturan por segundo de GPU en créditos, que se muestran en el nodo antes de ejecutarlo. No hay suscripción ni mínimo mensual.

## 

​

Limitaciones

  * Aún no puedes traer tu propio LoRA o checkpoint. Cada nodo expone un conjunto fijo de pesos alojados. La carga directa es un siguiente paso previsto, no disponible en esta versión.



## 

​

Relacionado

  * [Precios de Comfy Cloud](https://comfy.org/pricing)
  * [Descripción general de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview) (el catálogo aparte de nodos de API de terceros)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/cloud-nodes/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/cloud-nodes/overview)

[Relleno de video con VOID](https://docs.comfy.org/es/tutorials/utility/void-video-inpainting)[Descripción general](https://docs.comfy.org/es/tutorials/partner-nodes/overview)
