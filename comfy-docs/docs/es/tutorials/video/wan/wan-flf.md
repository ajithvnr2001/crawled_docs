---
url: https://docs.comfy.org/es/tutorials/video/wan/wan-flf/
title: Wan2.1 FLF2V en ComfyUI: generaci\u00f3n de video con primer y \u00faltimo fotograma - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:01.121690+00:00
---

# Wan2.1 FLF2V en ComfyUI: generación de video con primer y último fotograma - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan-flf/

## En esta página

Volver arriba

  * Ejemplo del flujo de trabajo nativo de Wan2.1 FLF2V 720P en ComfyUI
    * 1\. Descargar los archivos del flujo de trabajo y los archivos de entrada relacionados
    * 2\. Instalar los modelos manualmente
    * 3\. Ejecutar el flujo de trabajo paso a paso



Wan2.1

# Wan2.1 FLF2V en ComfyUI: generación de video con primer y último fotograma

Copiar páginaCopiar página

Genera video 720p entre un primer y último fotograma con el flujo de trabajo nativo Wan2.1 FLF2V en ComfyUI, con archivos de modelo y pasos de configuración.

Copiar páginaCopiar página

Wan FLF2V (generación de video de primer y último fotograma) es un modelo de generación de video de código abierto desarrollado por el equipo Alibaba Tongyi Wanxiang. Su licencia de código abierto es [Apache 2.0](https://github.com/Wan-Video/Wan2.1?tab=Apache-2.0-1-ov-file). Solo necesitas proporcionar dos imágenes como fotogramas inicial y final, y el modelo genera automáticamente los fotogramas de transición intermedios, produciendo un video en alta definición de 720p lógicamente coherente y de movimiento natural. **Aspectos técnicos destacados**

  1. **Control preciso del primer y último fotograma** : la tasa de coincidencia de los fotogramas inicial y final alcanza el 98%, definiendo los límites del video mediante las escenas inicial y final, y rellenando de forma inteligente los cambios dinámicos intermedios para lograr transiciones de escena y efectos de transformación de objetos.
  2. **Generación de video estable y fluida** : gracias al uso de características semánticas CLIP y mecanismos de atención cruzada, la tasa de vibración del video se reduce en un 37% en comparación con modelos similares, lo que garantiza transiciones naturales y fluidas.
  3. **Capacidades creativas multifuncionales** : admite el embedding dinámico de subtítulos en chino e inglés y la generación de estilos anime, realista, fantástico y otros, adaptándose a distintas necesidades creativas.
  4. **Salida HD de 720p** : genera directamente videos de 1280x720 sin posprocesamiento, adecuados para redes sociales y aplicaciones comerciales.
  5. **Soporte del ecosistema de código abierto** : los pesos del modelo, el código y el marco de entrenamiento son totalmente de código abierto, lo que permite su despliegue en las principales plataformas de IA.

**Principios técnicos y arquitectura**

  1. **Arquitectura DiT** : basada en modelos de difusión y en la arquitectura Diffusion Transformer, combinada con el mecanismo Full Attention para optimizar el modelado de dependencias espacio-temporales, garantizando la coherencia del video.
  2. **Codificador variacional causal 3D** : la tecnología Wan-VAE comprime los fotogramas HD a 1/128 de su tamaño mientras conserva los detalles dinámicos sutiles, lo que reduce significativamente los requisitos de memoria.
  3. **Estrategia de entrenamiento en tres etapas** : parte de un preentrenamiento a resolución 480P, escala gradualmente a 720P y equilibra la calidad de generación y la eficiencia computacional mediante una optimización por fases.

**Enlaces relacionados**

  * **Repositorio de GitHub** : [GitHub](https://github.com/Wan-Video/Wan2.1)
  * **Página del modelo en Hugging Face** : [Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P)
  * **Comunidad ModelScope** : [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-FLF2V-14B-720P)



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

Ejemplo del flujo de trabajo nativo de Wan2.1 FLF2V 720P en ComfyUI

### 

​

1\. Descargar los archivos del flujo de trabajo y los archivos de entrada relacionados

Dado que este modelo está entrenado con imágenes de alta resolución, usar tamaños más pequeños puede no dar buenos resultados. En el ejemplo usamos un tamaño de 720 * 1280, lo que puede hacer que los usuarios con poca VRAM tengan dificultades para ejecutarlo con fluidez y que la generación tarde mucho tiempo. Si lo necesitas, ajusta el tamaño de generación de video para hacer pruebas. Ten en cuenta que un tamaño de generación pequeño puede no producir buenos resultados con este modelo.

Actualiza ComfyUI a la última versión y luego descarga el archivo del flujo de trabajo y arrástralo a ComfyUI, o busca “Wan2.1 FLF2V 720P” en la biblioteca de plantillas en `Workflow` → `Browse Templates` → `Video`. ![Vista previa del flujo de trabajo Wan2.1 FLF2V 720P](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_flf2v_720_f16-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.1 FLF2V” en la biblioteca de plantillas

## Imagen inicial: wan2.1_flf2v_720_f16_start_image.png

Fotograma inicial para la generación del video (nodo LoadImage 52). Descarga y usa esta imagen, o reemplázala por la tuya.

## Imagen final: wan2.1_flf2v_720_f16_end_image.png

Fotograma final para la generación del video (nodo LoadImage 72). Descarga y usa esta imagen, o reemplázala por la tuya.

### 

​

2\. Instalar los modelos manualmente

Todos los modelos que se usan en esta guía están disponibles [aquí](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files). **Modelos de difusión** : elige una versión según tu hardware

## Modelo de difusión: Wan2.1 FLF2V 14B FP16

wan2.1_flf2v_720p_14B_fp16.safetensors : precisión completa, requiere más VRAM. Colócalo en `ComfyUI/models/diffusion_models/`

## Modelo de difusión: Wan2.1 FLF2V 14B FP8

wan2.1_flf2v_720p_14B_fp8_e4m3fn.safetensors : versión cuantizada, menor uso de VRAM. Colócalo en `ComfyUI/models/diffusion_models/`

Si ya has probado antes flujos de trabajo relacionados con Wan Video, es posible que ya tengas los siguientes archivos.

**Codificadores de texto** : elige una versión

## Codificador de texto: UMT5 XXL FP16

umt5_xxl_fp16.safetensors : codificador de texto de precisión completa. Colócalo en `ComfyUI/models/text_encoders/`

## Codificador de texto: UMT5 XXL FP8

umt5_xxl_fp8_e4m3fn_scaled.safetensors : codificador de texto cuantizado. Colócalo en `ComfyUI/models/text_encoders/`

**VAE**

## VAE: Wan2.1 VAE

wan_2.1_vae.safetensors : VAE de Wan2.1 para codificar y decodificar. Colócalo en `ComfyUI/models/vae/`

**CLIP Vision**

## CLIP Vision: CLIP Vision H

clip_vision_h.safetensors : codificador CLIP Vision. Colócalo en `ComfyUI/models/clip_vision/`

Ubicación de almacenamiento de los archivos
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   └─── wan2.1_flf2v_720p_14B_fp16.safetensors           # o la versión FP8
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors           # o la versión que elijas
    │   ├───📂 vae/
    │   │   └─── wan_2.1_vae.safetensors
    │   └───📂 clip_vision/
    │       └─── clip_vision_h.safetensors   
    

### 

​

3\. Ejecutar el flujo de trabajo paso a paso

![Pasos del flujo de trabajo nativo Wan2.1 FLF2V 720P](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f52356ef98601526215d4c21802f261f)

  1. Asegúrate de que el nodo `Load Diffusion Model` haya cargado `wan2.1_flf2v_720p_14B_fp16.safetensors` o `wan2.1_flf2v_720p_14B_fp8_e4m3fn.safetensors`
  2. Asegúrate de que el nodo `Load CLIP` haya cargado `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Asegúrate de que el nodo `Load VAE` haya cargado `wan_2.1_vae.safetensors`
  4. Asegúrate de que el nodo `Load CLIP Vision` haya cargado `clip_vision_h.safetensors`
  5. Sube el fotograma inicial al nodo `Start_image`
  6. Sube el fotograma final al nodo `End_image`
  7. (Opcional) Modifica los prompts positivo y negativo; se admiten tanto el chino como el inglés
  8. (**Importante**) En `WanFirstLastFrameToVideo` usamos 720 _1280 como tamaño predeterminado, ya que es un modelo de 720P, por lo que usar un tamaño pequeño no dará buenos resultados. Usa un tamaño cercano a 720_ 1280 para obtener una buena generación.
  9. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter`, para ejecutar la generación de video



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan-flf.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan-flf)

[Wan2.1 Fun InP](https://docs.comfy.org/es/tutorials/video/wan/fun-inp)[Bernini-R](https://docs.comfy.org/es/tutorials/video/bytedance/bernini-r)
