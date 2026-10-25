---
url: https://docs.comfy.org/es/get_started/first_generation/
title: Primeros pasos con la generaci\u00f3n de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:48.193382+00:00
---

# Primeros pasos con la generación de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/get_started/first_generation/

## En esta página

  * Acerca de Texto a imagen
  * Tutorial del flujo de trabajo de texto a imagen de ComfyUI
    * 1\. Inicia ComfyUI
    * 2\. Carga el flujo de trabajo predeterminado de texto a imagen
    * 3\. Instalación de modelos
    * 4\. Cargar el modelo y generar tu primera imagen
  * Solución de problemas
    * Problemas al cargar modelos



# Primeros pasos con la generación de imágenes con IA

Copiar páginaCopiar página

Genera tu primera imagen con IA con ComfyUI. Aprende a cargar flujos de trabajo de ejemplo, instalar modelos y completar tu primera generación de texto a imagen.

Copiar páginaCopiar página

Esta guía está pensada para **usuarios locales** que ejecutan ComfyUI en su propio dispositivo. Si prefieres no instalar nada localmente, prueba nuestro servicio oficial en la nube.

## Prueba Comfy Cloud

Ejecuta ComfyUI en línea sin configuración alguna. Inicia sesión con Google para obtener **400 créditos gratis cada mes**.

Esta guía tiene como objetivo ayudarte a comprender las operaciones básicas de ComfyUI y completar tu primera generación de imágenes. Cubriremos:

  1. Cargando flujos de trabajo de ejemplo 
     * Cargando desde las plantillas de flujos de trabajo de ComfyUI
     * Cargando desde imágenes con metadatos de flujo de trabajo
  2. Orientación para la instalación de modelos 
     * Instalación automática de modelos
     * Instalación manual de modelos
  3. Completar tu primera generación de texto a imagen



## 

​

Acerca de Texto a imagen

Texto a imagen es una función fundamental de dibujo con IA que genera imágenes a partir de descripciones de texto. Es una de las funciones más utilizadas en la generación de arte con IA. Puedes pensar en el proceso como si le explicaras tus requisitos (prompts positivos y negativos) a un artista (el modelo de dibujo), quien luego creará lo que deseas. Las explicaciones detalladas sobre texto a imagen se cubrirán en el capítulo [Texto a imagen](https://docs.comfy.org/tutorials/basic/text-to-image).

## 

​

Tutorial del flujo de trabajo de texto a imagen de ComfyUI

### 

​

1\. Inicia ComfyUI

Asegúrate de haber seguido la [guía de instalación](https://docs.comfy.org/es/installation/system_requirements) para iniciar ComfyUI y poder entrar correctamente a la interfaz de ComfyUI. Como alternativa, puedes usar [Comfy Cloud](https://docs.comfy.org/es/get_started/cloud) para utilizar ComfyUI sin necesidad de instalación alguna. ![Interfaz de ComfyUI](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/desktop/comfyui-interface.jpg?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=5fc5c0932897a4ab0076db79fec7b4ea) Si no has instalado ComfyUI, elige la versión adecuada para instalar según tu dispositivo.

Comfy Desktop

Comfy Desktop permite la instalación independiente en **Windows** , **macOS (Apple Silicon)** y **Linux** (AppImage y `.deb`).

  * El código fuente está en [GitHub](https://github.com/Comfy-Org/Comfy-Desktop)



Las instalaciones de Desktop siguen por defecto la versión **estable** de ComfyUI. Si quieres cada última confirmación (commit), usa la versión portable o una instalación manual con git, o cambia el canal de actualización de la instancia a **Latest on GitHub**.

A continuación puedes elegir la instalación adecuada para tu sistema y hardware

  * Windows

  * macOS (Apple Silicon)

  * Linux




## Guía de instalación de Comfy Desktop (Windows)

Adecuada para **Windows** 10 o posterior. Se recomienda GPU NVIDIA o AMD.

## Guía de instalación de Comfy Desktop (macOS)

Adecuada para macOS con **Apple Silicon**

## Guía de instalación de Comfy Desktop (Linux)

Instala el AppImage o el `.deb`, o compila y ejecuta desde el código fuente.

ComfyUI Portable (Windows)

La versión portable es una versión de ComfyUI que integra un entorno Python integrado independiente; con la versión portable puedes probar las últimas funciones, actualmente solo es compatible con el sistema **Windows**

## Guía de instalación de ComfyUI Portable (Windows)

Compatible con la versión de ComfyUI para **Windows** que se ejecuta en **GPU Nvidia** o **solo con CPU** , siempre usa las últimas confirmaciones (commits) y es completamente portable.

Instalación manual

## Guía de instalación manual de ComfyUI

Compatible con todos los tipos de sistema y de GPU (Nvidia, AMD, Intel, Apple Silicon, Ascend NPU, Cambricon MLU)

### 

​

2\. Carga el flujo de trabajo predeterminado de texto a imagen

Por lo general, ComfyUI carga automáticamente el flujo de trabajo predeterminado de texto a imagen al iniciarse. Sin embargo, puedes probar distintos métodos para cargar flujos de trabajo y familiarizarte con las operaciones básicas de ComfyUI:

  * Cargar desde imágenes con metadatos

  * Cargar desde workflow.json




Todas las imágenes generadas por ComfyUI contienen metadatos, incluida la información del flujo de trabajo. Puedes cargar flujos de trabajo de las siguientes maneras:

  * Arrastrando y soltando en la interfaz una imagen generada por ComfyUI
  * Usando el menú **Workflows** -> **Open** para abrir una imagen

Prueba a cargar el flujo de trabajo usando esta imagen de ejemplo: ![Flujo de trabajo Texto a imagen de ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/text-to-image-workflow.png)

Los flujos de trabajo de ComfyUI se pueden almacenar en formato JSON. Puedes exportar flujos de trabajo usando el menú **Workflows** -> **Export**.Intenta descargar y cargar este flujo de trabajo de ejemplo:[Descargar text-to-image.json](https://github.com/Comfy-Org/docs/blob/main/public/text-to-image.json)Después de descargar, usa el menú **Workflows** -> **Open** para cargar el archivo JSON.

### 

​

3\. Instalación de modelos

La mayoría de las instalaciones de ComfyUI no incluyen modelos base por defecto. Después de cargar el flujo de trabajo, si no tienes instalado el modelo [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors), verás este mensaje: Primero, ComfyUI te advertirá que faltan algunos modelos: ![Advertencia de modelos faltantes](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/missing_model_warning_1.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=0587d7f045f981756c232644569b3b59) Haz clic en la advertencia para ver qué modelo falta y el enlace de descarga: ![Detalles del modelo faltante](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/missing_model_warning_2.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=bf61da1c5711d935b7d49dd7e236f275) Por defecto, los modelos se almacenan en `<your ComfyUI installation>/ComfyUI/models/` con subcarpetas como `checkpoints`, `embeddings`, `vae`, `lora`, `upscale_model`, etc. ComfyUI detecta los modelos en estas carpetas y en las rutas configuradas en `extra_model_paths.yaml` al iniciar.

  * Comfy Desktop (Encontrar la carpeta de modelos)

  * ComfyUI Portable (Encontrar la carpeta de modelos)




Haz clic en el menú de la cápsula en la parte superior de la aplicación de escritorio y luego abre la pestaña **Storage** para revisar tus directorios de modelos. La cápsula solo existe en la aplicación de escritorio, no cuando ComfyUI se ejecuta en un navegador. Haz clic en el icono de carpeta junto a un directorio para abrirlo en tu administrador de archivos.![Menú de la cápsula de Comfy Desktop: pestaña Storage mostrando la configuración de directorios de modelos](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)

Para la versión portable, la carpeta de modelos suele estar ubicada en:`ComfyUI_windows_portable/ComfyUI/models/`

Puedes instalar modelos mediante:

  * Descarga automática

  * Instalación manual




Después de hacer clic en el botón **Download** , ComfyUI ejecutará la descarga y el comportamiento variará según la versión que estés usando.

  * Comfy Desktop

  * ComfyUI Portable




La versión de escritorio completará automáticamente la descarga del modelo y lo guardará en el directorio `<your ComfyUI installation location>/ComfyUI/models/checkpoints`. Puedes esperar a que se complete la instalación o ver el progreso de la instalación en el panel de modelos de la barra lateral.![Progreso de descarga del modelo](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/desktop_download_status.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=a1573451803b46539fca14c1b1ef4dd2)

Las descargas automáticas suelen obtener los modelos de **Hugging Face**. Asegúrate de que tu red pueda llegar de forma confiable a Hugging Face.Si la descarga **no se inicia** o muestra **ningún progreso durante mucho tiempo** , copia el enlace del modelo desde los detalles del modelo faltante (o usa la sección de instalación manual a continuación) e instala el modelo manualmente.

El navegador realizará las descargas de archivos. Guarda el archivo en el directorio `<your ComfyUI installation location>/ComfyUI_windows_portable/ComfyUI/models/checkpoints` después de que se complete la descarga.

Visita [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) y sigue esta guía:![Descarga del modelo de Hugging Face](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=15c2560c44e7e4276b6a351809f7bf9f)Guarda el archivo descargado en:

  * Comfy Desktop

  * ComfyUI Portable




Guarda en `<your ComfyUI installation>/ComfyUI/models/checkpoints`![Ubicación de guardado del modelo en Comfy Desktop](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=275add7233b1f048455cff0f162847b9)

Guarda en `ComfyUI_windows_portable/ComfyUI/models/checkpoints`![Ubicación de guardado del modelo en ComfyUI Portable](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=48976b87bcfdba962b119d901c43b286)

Actualiza o reinicia ComfyUI después de guardar.

### 

​

4\. Cargar el modelo y generar tu primera imagen

Después de instalar o actualizar modelos, presiona **`R`** en tu teclado para actualizar las definiciones de objetos y las listas de modelos en los nodos (por ejemplo, el menú desplegable en **Load Checkpoint**). Luego continúa con los pasos a continuación: ![Ejecutar flujo de trabajo](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/run_workflow.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=d8cb64b219e93cfd903723255d5e7d11)

  1. En el nodo **Load Checkpoint** , asegúrate de que **v1-5-pruned-emaonly-fp16.safetensors** esté seleccionado
  2. Haz clic en `Run` o presiona `Ctrl + Enter` para generar

El resultado aparecerá en el nodo **Save Image**. Haz clic derecho para guardarlo localmente. ![Resultado de la primera generación de imagen con ComfyUI](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/result.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=dd253cd626d72716f52322245c5526cc) Para instrucciones detalladas de texto a imagen, consulta nuestra guía completa:

## Guía del flujo de trabajo de texto a imagen de ComfyUI

Haz clic aquí para ver las instrucciones detalladas del flujo de trabajo de texto a imagen

## 

​

Solución de problemas

### 

​

Problemas al cargar modelos

Si el nodo `Load Checkpoint` no muestra ningún modelo o muestra “null”, verifica la ubicación donde instalaste tus modelos e intenta actualizar o reiniciar ComfyUI.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/get_started/first_generation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/get_started/first_generation)

[Solución de problemas](https://docs.comfy.org/es/manager/troubleshooting)
