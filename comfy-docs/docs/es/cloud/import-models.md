---
url: https://docs.comfy.org/es/cloud/import-models/
title: Importar modelos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:48.767026+00:00
---

# Importar modelos - ComfyUI

> Source: https://docs.comfy.org/es/cloud/import-models/

## En esta página

Volver arriba

  * Descripción general
  * Requisitos
  * Cómo importar modelos
    * 1\. Accede a la función de importación
    * 2\. Pega el enlace
  * Cómo ver los modelos importados
  * Cómo obtener enlaces de importación de modelos
    * 1\. Obtener el enlace desde Civitai
    * 2\. Obtener el enlace desde Hugging Face
  * Importar modelos privados
    * 1\. Genera tus claves API
    * 2\. Guarda tus claves API
    * 3\. Importa el modelo privado
  * Preguntas frecuentes



Exclusivas de Cloud

# Importar modelos

Copiar páginaCopiar página

Aprende a importar modelos desde Civitai y Hugging Face a Comfy Cloud

Copiar páginaCopiar página

Esta es una función de **Comfy Cloud** y solo está disponible en la Versión de la Nube. Para aprender más acerca de Comfy Cloud, consulta [Comfy Cloud](https://docs.comfy.org/es/get_started/cloud).

## 

​

Descripción general

Comfy Cloud te permite importar modelos directamente desde Civitai y Hugging Face. Esta función está disponible para usuarios con una suscripción **Creator** o superior.

## 

​

Requisitos

  * **Suscripción** : plan Creador o superior
  * **Fuentes compatibles** : Civitai y Hugging Face



## 

​

Cómo importar modelos

### 

​

1\. Accede a la función de importación

![Importar](https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=0621b50c1cc510ddcdd5bb69f96625b7)

  1. Haz clic en el botón **Modelos** de la barra lateral izquierda para abrir la Biblioteca de modelos.
  2. En la ventana de la Biblioteca de modelos, haz clic en el botón **Importar**.



### 

​

2\. Pega el enlace

  1. Pega el enlace del modelo que obtuviste de Hugging Face o Civitai. ![Ventana de importación](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=077d3bf113f8139db1ce9f94e3c42202)
  2. Si el enlace es válido, verás un indicador de confirmación y podrás hacer clic en el botón `Continue` para continuar. ![Ventana de importación](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=3b35abf880dc14c6d0186e1e6a104f92)
  3. Selecciona el tipo de modelo y la carpeta de destino. ![Ventana de importación](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=10c28ec6293b6d2658d2899ebbae072f)
  4. Espera a que el modelo termine de descargarse. ![Ventana de importación](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=d80d9bb488937b1b2493dfc4929b7a17)
  5. Una vez descargado, puedes encontrar el modelo en tu Biblioteca de modelos.



## 

​

Cómo ver los modelos importados

En la Biblioteca de modelos, selecciona “Mis modelos” en el filtro desplegable para filtrar los modelos que importaste. ![Modelos importados](https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=9e0b5c5f1a200c7337f94aa67d7ffd36)

## 

​

Cómo obtener enlaces de importación de modelos

### 

​

1\. Obtener el enlace desde Civitai

  1. Ve a [Civitai](https://civitai.com/) y busca el modelo que quieres importar.
  2. Haz clic derecho en el botón de descarga y selecciona “Copiar dirección del enlace” para obtener el enlace de descarga del modelo.

![Copiar enlace de Civitai](https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=48e3791d2dda7a9df235b1b4e73b0942)

### 

​

2\. Obtener el enlace desde Hugging Face

  1. Ve a [Hugging Face](https://huggingface.co/) y busca el repositorio del modelo que quieres importar.
  2. Ve a la página de archivos del modelo. El formato compatible es “.safetensors”. Haz clic en el nombre del modelo específico para entrar a su página de detalles.

![Copiar enlace del modelo de Huggingface](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=786214df669fd53613b295e6bd6e8cef)

  3. En la página de detalles, haz clic en el botón `Copy Download Link` para obtener el enlace de descarga del modelo.

![Copiar enlace del modelo de Huggingface](https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=4681f3e56576eb36ad4e26287bebc65b)

## 

​

Importar modelos privados

Si quieres importar modelos privados desde Hugging Face o Civitai, primero debes configurar tus claves API.

### 

​

1\. Genera tus claves API

Primero, debes generar claves API desde las plataformas correspondientes:

  * Civitai

  * Hugging Face




  1. Inicia sesión en Civitai y visita <https://civitai.com/user/account>.
  2. Genera tu clave API en la configuración de la cuenta. ![Clave API de Civitai](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=50e93b8937fe90a70f7aec140db65d30)



  1. Visita <https://huggingface.co/settings/tokens>.
  2. Genera tu token de API. ![Clave API de Hugging Face](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=32729b7a20a9ebe16d546c4836b92b49)
  3. Asegúrate de que tu token tenga acceso de lectura a los repositorios que contienen los modelos privados que quieres importar. ![Permisos del token de Hugging Face](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=2ae808aa8052e3cc98e8d91b5fde551c)



### 

​

2\. Guarda tus claves API

  1. Ve a [Configuraciones de Comfy Cloud](https://cloud.comfy.org) y navega hasta la sección **Credenciales**.

![Credenciales de configuración](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=15ea8a8aeeb50da9bedc00429c9c05b1)

  2. Haz clic para agregar tus claves API (puedes nombrar la clave como quieras):

![Agregar clave secreta](https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=b87a3c87203a4e3929ae41295281a823)

  3. Asegúrate de que tus claves API tengan permisos de acceso a los modelos privados que quieres importar.



### 

​

3\. Importa el modelo privado

Una vez que tus claves API estén configuradas, puedes importar modelos privados usando el mismo proceso que para los modelos públicos:

  1. Obtén el enlace del modelo desde Hugging Face o Civitai.
  2. Pega el enlace en la ventana de importación.
  3. El sistema usará automáticamente tus claves API guardadas para acceder al modelo privado.



Asegúrate de que tu clave API tenga los permisos necesarios para acceder al modelo privado específico que quieres importar.

## 

​

Preguntas frecuentes

¿Hay restricciones sobre los modelos que puedo subir?

Sí. Solo se admiten archivos **safetensors**. En la práctica, no hay límite de tamaño de archivo (hasta 100GB).

¿Los modelos que subo son privados o se comparten con todos?

Los modelos que importas son **privados para ti**. Solo tú puedes ver los modelos de tu biblioteca.

¿Puedo subir mis propios modelos personalizados desde mi disco duro local?

Por ahora, primero debes subir el modelo a un **repositorio público de Hugging Face o Civitai** y luego importarlo desde esas plataformas.

¿Puedo subir archivos de modelos divididos en partes?

No. Debes combinar los archivos de modelos divididos en partes en un solo archivo antes de importar.

¿Esta función está incluida en mi suscripción actual a la nube?

Esta función solo está disponible para los planes **Creator** y **Pro**.

¿Esta función está disponible en las versiones Desktop o portable de Comfy?

No. Es una función **exclusiva de la nube**.

¿Puedo eliminar un modelo que subí?

Sí. Puedes eliminar los modelos que importaste. Ten en cuenta que los modelos que sube el equipo interno de Comfy no se pueden eliminar.

¿Qué tipos de modelos puedo importar (BYOM)?

No solo los ejemplos a continuación. BYOM admite cualquier carpeta de modelos que Comfy Cloud muestre en el **selector de tipo de importación** durante la importación. Esa lista proviene de las carpetas de modelos de ComfyUI compatibles con Comfy Cloud y es la fuente de referencia.En la práctica, si ComfyUI trata un archivo como un peso de modelo (checkpoint, LoRA, VAE, ControlNet, embedding, upscaler, IP-Adapter, SAM, codificador de audio y similares), puedes importarlo siempre que la carpeta aparezca en ese selector.Ejemplos comunes:

  * **Checkpoints y UNets** : `checkpoints`, `diffusion_models`
  * **LoRAs y adaptadores** : `loras`, `animatediff_motion_lora`, `cogvideox_loras` y carpetas de adaptadores similares
  * **VAE** : `vae`, `vae_approx`
  * **ControlNet** : `controlnet`
  * **CLIP y codificadores de texto** : `clip_vision`, `text_encoders`
  * **Embeddings / inversión textual** : `embeddings` (haz referencia en los prompts de `CLIPTextEncode` con `embedding:my-embedding-name`)
  * **Upscalers** : `upscale_models`, `latent_upscale_models`
  * **Visión / segmentación / eliminación** : `ipadapter`, `gligen`, `sams`, `sam3`, `rmbg`, `ultralytics_bbox`, `ultralytics_segm`
  * **Otras carpetas del selector** : `audio_encoders`, `model_patches`, `style_models`, `photomaker`, `LLM`, `CogVideo` y más

Lo que realmente limita la importación no es la categoría del modelo, sino estas reglas:

  * **Formato de archivo** : solo `.safetensors` (incluso si ComfyUI localmente admite `.ckpt`, `.pth` o `.onnx` para esa carpeta)
  * **Fuente** : solo enlaces de descarga de Civitai o Hugging Face (no se permite subir archivos locales directamente)
  * **Carpeta bloqueada** : los modelos `nlf` no se pueden importar



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/cloud/import-models.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/cloud/import-models)

[Publicar flujos de trabajo](https://docs.comfy.org/es/cloud/publish-workflow)[Texto a imagen](https://docs.comfy.org/es/tutorials/basic/text-to-image)
