---
url: https://docs.comfy.org/es/tutorials/video/cosmos/cosmos-predict2-video2world/
title: Cosmos Predict2 Video2World en ComfyUI: generaci\u00f3n de video a partir de una imagen - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:58.957155+00:00
---

# Cosmos Predict2 Video2World en ComfyUI: generación de video a partir de una imagen - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/cosmos/cosmos-predict2-video2world/

## En esta página

Volver arriba

  * Flujo de trabajo Cosmos Predict2 Video2World
    * 1\. Archivo del flujo de trabajo
    * 2\. Instalación manual de los modelos
    * 3\. Completar el flujo de trabajo paso a paso



Cosmos

# Cosmos Predict2 Video2World en ComfyUI: generación de video a partir de una imagen

Copiar páginaCopiar página

Genera video realista desde una imagen en ComfyUI con el flujo de trabajo Cosmos-Predict2 Video2World de NVIDIA, con instalación manual incluida.

Copiar páginaCopiar página

Cosmos-Predict2 es el modelo fundacional de mundo físico de nueva generación de NVIDIA, diseñado específicamente para tareas de generación y predicción visual de alta calidad en escenarios de IA física. El modelo ofrece una precisión física excepcional, interactividad con el entorno y capacidad de reproducción de detalles, lo que permite simular de forma realista fenómenos físicos complejos y escenas dinámicas. Cosmos-Predict2 admite varios métodos de generación, como Texto a imagen (Text2Image) y Video-to-World (Video2World), y se usa ampliamente en simulación industrial, conducción autónoma, planificación urbana, investigación científica y otros campos. Es una herramienta fundacional clave para impulsar la integración profunda de la visión inteligente y el mundo físico.

## GitHub

Código fuente y documentación de Cosmos-Predict2

## Hugging Face

Colección de modelos Cosmos-Predict2

Esta guía te acompaña paso a paso para completar la generación **Video2World** en ComfyUI. Para la sección de texto a imagen, consulta lo siguiente:

## Cosmos Predict2 Texto a imagen

Usar Cosmos-Predict2 para la generación de texto a imagen

## Ejecutar en Comfy Cloud

Ejecuta los flujos de trabajo de Cosmos-Predict2 en Comfy Cloud con GPU potentes

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

Flujo de trabajo Cosmos Predict2 Video2World

Al probar la versión 2B, se usan alrededor de 16 GB de VRAM.

### 

​

1\. Archivo del flujo de trabajo

Descarga el video de abajo y arrástralo a ComfyUI para cargar el flujo de trabajo. El flujo de trabajo ya incluye los enlaces de descarga de los modelos.

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud con los modelos ya instalados

## Descargar el archivo del flujo de trabajo

Descarga el archivo del flujo de trabajo en formato JSON

Descarga la siguiente imagen para usarla como entrada: ![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/cosmos/predict2/input.png)

### 

​

2\. Instalación manual de los modelos

Si la descarga del modelo no se completó correctamente, puedes intentar descargarlo manualmente en esta sección. **Modelo de difusión**

## Modelo de difusión

cosmos_predict2_2B_video2world_480p_16fps.safetensors

Para otras ponderaciones, visita [Cosmos_Predict2_repackaged](https://huggingface.co/Comfy-Org/Cosmos_Predict2_repackaged) para descargarlas. **Codificador de texto**

## Codificador de texto

oldt5_xxl_fp8_e4m3fn_scaled.safetensors

**VAE**

## VAE

wan_2.1_vae.safetensors

Ubicación de los archivos
    
    
    📂 ComfyUI/
    ├──📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └─── cosmos_predict2_2B_video2world_480p_16fps.safetensors
    │   ├── 📂 text_encoders/
    │   │   └─── oldt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   └── 📂 vae/
    │       └──  wan_2.1_vae.safetensors
    

### 

​

3\. Completar el flujo de trabajo paso a paso

![Guía de pasos del flujo de trabajo](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/cosmos/cosmos_predict2_2B_video2world_480p_16fps_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ea0b6deafa617381a38a57ccb3c92014) Sigue los pasos de la imagen para ejecutar el flujo de trabajo:

  1. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado `cosmos_predict2_2B_video2world_480p_16fps.safetensors`
  2. Asegúrate de que el nodo `Load CLIP` tenga cargado `oldt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado `wan_2.1_vae.safetensors`
  4. Sube la imagen de entrada proporcionada en el nodo `Load Image`
  5. (Opcional) Si necesitas control del primer y del último fotograma, usa el atajo `Ctrl(cmd) + B` para habilitar la entrada del último fotograma
  6. (Opcional) Puedes modificar los prompts en el nodo `ClipTextEncode`
  7. (Opcional) Modifica el tamaño y la cantidad de fotogramas en el nodo `CosmosPredict2ImageToVideoLatent`
  8. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo
  9. Cuando termine la generación, el video se guardará automáticamente en el directorio `ComfyUI/output/`; también puedes verlo en el nodo `save video`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/cosmos/cosmos-predict2-video2world.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/cosmos/cosmos-predict2-video2world)

[HunyuanVideo 1.5](https://docs.comfy.org/es/tutorials/video/hunyuan/hunyuan-video-1-5)[Kandinsky 5.0](https://docs.comfy.org/es/tutorials/video/kandinsky/kandinsky-5)
