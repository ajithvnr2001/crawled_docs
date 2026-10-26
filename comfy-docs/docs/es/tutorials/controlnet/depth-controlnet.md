---
url: https://docs.comfy.org/es/tutorials/controlnet/depth-controlnet/
title: Depth ControlNet en ComfyUI: controla la estructura de la escena - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:41.901063+00:00
---

# Depth ControlNet en ComfyUI: controla la estructura de la escena - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/controlnet/depth-controlnet/

## En esta página

Volver arriba

  * Introducción a los mapas de profundidad y Depth ControlNet
    * Escenarios de aplicación de los mapas de profundidad con ControlNet
  * Explicación del ejemplo de flujo de trabajo de ControlNet en ComfyUI
    * 1\. Recursos del flujo de trabajo de ControlNet
    * 2\. Instalación de modelos
    * 3\. Ejecución del flujo de trabajo paso a paso
  * Combinar el control de profundidad con otras técnicas



ControlNet

# Depth ControlNet en ComfyUI: controla la estructura de la escena

Copiar páginaCopiar página

Lee un mapa de profundidad, conéctalo a ControlNet y mantén la arquitectura, los retratos y las fotos de producto en la distribución espacial que definas.

Copiar páginaCopiar página

## 

​

Introducción a los mapas de profundidad y Depth ControlNet

Un mapa de profundidad es un tipo especial de imagen que usa valores de escala de grises para representar la distancia entre los objetos de una escena y el observador o la cámara. En un mapa de profundidad, el valor de escala de grises es inversamente proporcional a la distancia: las áreas más claras (más cercanas al blanco) indican objetos más cercanos, mientras que las áreas más oscuras (más cercanas al negro) indican objetos más lejanos. ![Imagen de profundidad](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_input.png) Depth ControlNet es un modelo ControlNet entrenado específicamente para comprender y utilizar la información de los mapas de profundidad. Ayuda a la IA a interpretar correctamente las relaciones espaciales, lo que garantiza que las imágenes generadas respeten la estructura espacial especificada por el mapa de profundidad y permite un control preciso de las distribuciones espaciales tridimensionales.

### 

​

Escenarios de aplicación de los mapas de profundidad con ControlNet

Los mapas de profundidad tienen numerosas aplicaciones en distintos escenarios:

  1. **Escenas de retrato** : Controla la relación espacial entre los sujetos y los fondos, evitando distorsiones en áreas críticas como el rostro
  2. **Escenas de paisaje** : Controla las relaciones de jerarquía entre el primer plano, el plano medio y el fondo
  3. **Escenas de arquitectura** : Controla la estructura espacial y las relaciones de perspectiva de los edificios
  4. **Presentación de productos** : Controla la separación y la posición espacial de los productos respecto a sus fondos

En este ejemplo, usaremos un mapa de profundidad para generar una escena de visualización arquitectónica.

## 

​

Explicación del ejemplo de flujo de trabajo de ControlNet en ComfyUI

### 

​

1\. Recursos del flujo de trabajo de ControlNet

Descarga la imagen del flujo de trabajo que aparece a continuación y arrástrala a ComfyUI para cargar el flujo de trabajo: ![Flujo de trabajo de profundidad](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_controlnet.png)

Las imágenes que llevan el JSON del flujo de trabajo en sus metadatos se pueden arrastrar directamente a ComfyUI o cargar con el menú `Workflows` -> `Open (ctrl+o)`. Esta imagen ya incluye los enlaces de descarga de los modelos correspondientes, y al arrastrarla a ComfyUI se te pedirá automáticamente que los descargues.

Descarga la imagen que aparece a continuación, que usaremos como entrada: ![Imagen de profundidad](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_input.png)

### 

​

2\. Instalación de modelos

Si tu red no puede completar correctamente la descarga automática de los modelos correspondientes, intenta descargar manualmente los modelos que aparecen a continuación y colócalos en los directorios indicados:

  * [architecturerealmix_v11.safetensors](https://civitai.com/api/download/models/431755?type=Model&format=SafeTensor&size=full&fp=fp16)
  * [control_v11f1p_sd15_depth_fp16.safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11f1p_sd15_depth_fp16.safetensors?download=true)


    
    
    ComfyUI/
    ├── models/
    │   ├── checkpoints/
    │   │   └── architecturerealmix_v11.safetensors
    │   └── controlnet/
    │       └── control_v11f1p_sd15_depth_fp16.safetensors
    

### 

​

3\. Ejecución del flujo de trabajo paso a paso

![Flujo de trabajo de ComfyUI: diagrama de flujo de ControlNet de profundidad](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7bcb7a518e96e88c6ccb73c1a7eb7087)

  1. Asegúrate de que `Load Checkpoint` pueda cargar **architecturerealmix_v11.safetensors**
  2. Asegúrate de que `Load ControlNet` pueda cargar **control_v11f1p_sd15_depth_fp16.safetensors**
  3. Haz clic en `Upload` en el nodo `Load Image` para subir la imagen de profundidad proporcionada anteriormente
  4. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de la imagen



## 

​

Combinar el control de profundidad con otras técnicas

Según tus distintas necesidades creativas, puedes combinar el ControlNet de profundidad con otros tipos de ControlNet para lograr mejores resultados:

  1. **Profundidad + Arte lineal** : mantiene las relaciones espaciales mientras refuerza los contornos; ideal para arquitectura, productos y diseño de personajes.
  2. **Profundidad + Pose** : controla la postura del personaje y mantiene relaciones espaciales correctas; ideal para escenas con personajes.

Para obtener más información sobre cómo usar varios modelos ControlNet juntos, consulta el ejemplo de [Combinar ControlNet](https://docs.comfy.org/es/tutorials/controlnet/mixing-controlnets).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/controlnet/depth-controlnet.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/controlnet/depth-controlnet)

[Pose ControlNet](https://docs.comfy.org/es/tutorials/controlnet/pose-controlnet-2-pass)[Depth T2I Adapter](https://docs.comfy.org/es/tutorials/controlnet/depth-t2i-adapter)
