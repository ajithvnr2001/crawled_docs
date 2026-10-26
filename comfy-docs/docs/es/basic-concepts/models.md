---
url: https://docs.comfy.org/es/basic-concepts/models/
title: Modelos de ComfyUI: archivos, carpetas y nodos de carga - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:29.780341+00:00
---

# Modelos de ComfyUI: archivos, carpetas y nodos de carga - ComfyUI

> Source: https://docs.comfy.org/es/basic-concepts/models/

## En esta página

Volver arriba

  * Modelos en términos sencillos
    * Modelos compatibles en ComfyUI
  * Usa modelos en ComfyUI
    * Prepárate para descargas de gran tamaño
  * Más allá del checkpoint principal
  * Desinstalar modelos
  * Agregar rutas de modelos adicionales
    * Abrir el archivo de configuración
    * Estructura de ejemplo
    * Agregar rutas de nodos personalizados adicionales
  * Problemas comunes
  * ¿Quieres un poco más de contexto?



Conceptos básicos

# Modelos de ComfyUI: archivos, carpetas y nodos de carga

Copiar páginaCopiar página

Cómo encajan los archivos de modelo en los flujos de trabajo de ComfyUI: dónde van, cómo cargarlos y soluciones comunes.

Copiar páginaCopiar página

## 

​

Modelos en términos sencillos

En ComfyUI, los **modelos** son los archivos de pesos que realmente ejecutan tu flujo de trabajo. Incluyen **checkpoints** , **VAEs** , **LoRAs** , **ControlNets** y upscalers. La instalación de la aplicación es pequeña. Estos archivos **no** se incluyen de forma predeterminada. Normalmente los **descargas de la web** , los colocas en `ComfyUI/models/` (o sigues las indicaciones de una plantilla) y luego eliges el archivo en el **nodo cargador** correcto (en el lienzo, suelen aparecer como nodos cuyos nombres empiezan por **Load**).

### 

​

Modelos compatibles en ComfyUI

  * **La cobertura integrada / de primera parte es intencionalmente limitada** , pero crece con el tiempo a medida que ComfyUI y el ecosistema de código abierto evolucionan. Cuando un modelo obtiene soporte de primera clase, **normalmente verás una nueva entrada en la[biblioteca de plantillas de flujos de trabajo](https://docs.comfy.org/es/interface/features/template)** que muestra el gráfico esperado y la combinación de modelos.
  * **No todos los checkpoints ni archivos de pesos funcionan de inmediato.** Para los **modelos con soporte nativo y sus pesos complementarios habituales** , mantén ComfyUI **[actualizado](https://docs.comfy.org/es/installation/update_comfyui)** y confirma que el flujo de trabajo correspondiente existe en la **[biblioteca de plantillas](https://docs.comfy.org/es/interface/features/template)** antes de asumir que tus archivos están en el lugar equivocado.
  * **Muchos otros modelos se habilitan mediante nodos personalizados de la comunidad.** Las rutas, los nodos cargadores y la disposición del gráfico pueden diferir de la orientación genérica sobre `ComfyUI/models/` de esta página. **Sigue siempre el README o la documentación de cada proyecto.** ComfyUI es muy extensible, por lo que las implementaciones varían según el autor. Para la instalación y la resolución de problemas, consulta [Cómo instalar nodos personalizados](https://docs.comfy.org/es/installation/install_custom_node).



## 

​

Usa modelos en ComfyUI

  1. **Consigue que los archivos estén en el lugar correcto.** Descárgalos desde sitios de la comunidad como [Hugging Face](https://huggingface.co), [Civitai](https://civitai.green) o la página de un proyecto en [GitHub](https://github.com), y luego colócalos dentro de `ComfyUI/models/`, en la subcarpeta correspondiente a ese tipo (por ejemplo `checkpoints`, `loras`, `vae`).
  2. **Añade el nodo cargador correspondiente.** Elige el cargador para ese tipo de modelo (checkpoint, LoRA, VAE, etc.). En la lista de nodos, los títulos suelen empezar por **Load**.
  3. **Selecciona el archivo** en el desplegable de ese nodo cargador.
  4. **Conecta el nodo cargador** con el resto del gráfico. Si copiaste archivos a mano mientras ComfyUI estaba abierto, **reinicia** la aplicación (o actualiza según sea necesario) para que las listas se actualicen.



### 

​

Prepárate para descargas de gran tamaño

Un solo modelo generativo suele ocupar **muchos gigabytes**. Reserva espacio en disco y tiempo cuando descargues o sincronices.

## 

​

Más allá del checkpoint principal

El checkpoint de difusión principal hace mucho, pero muchos flujos de trabajo añaden **modelos auxiliares más pequeños** , por ejemplo:

  * **LoRA** : complementos ligeros ajustados para un estilo, un personaje o un concepto
  * **ControlNet** : orientación adicional a partir de bordes, profundidad, pose, etc.
  * **Relleno inteligente** : rellena o reemplaza regiones dentro de una imagen existente

![modelos auxiliares](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=0f49a29f61c23ccd32ec5a15207b8f9c)

## 

​

Desinstalar modelos

Todavía no hay un botón de “desinstalar” en la interfaz. Para eliminar un modelo, **elimina su archivo** (o archivos) de la carpeta dentro de `ComfyUI/models/` donde lo colocaste.

## 

​

Agregar rutas de modelos adicionales

Si quieres gestionar tus archivos de modelo fuera de `ComfyUI/models`, puede que tengas alguno de estos motivos:

  * Tienes varias instancias de ComfyUI y quieres que compartan los archivos de modelo para ahorrar espacio en disco
  * Tienes distintos programas con interfaz gráfica (como WebUI) y quieres que usen los mismos archivos de modelo
  * Los archivos de modelo no se reconocen o no se encuentran

Ofrecemos una forma de agregar rutas de búsqueda de modelos adicionales mediante el archivo de configuración `extra_model_paths.yaml`.

### 

​

Abrir el archivo de configuración

  * Instalación portable/manual

  * Comfy Desktop




En el caso de las versiones de ComfyUI como la [portable](https://docs.comfy.org/es/installation/comfyui_portable_windows) y la [manual](https://docs.comfy.org/es/installation/manual_install), puedes encontrar un archivo de ejemplo llamado `extra_model_paths.yaml.example` en el directorio raíz de ComfyUI:
    
    
    ComfyUI/extra_model_paths.yaml.example
    

Cópialo y cámbiale el nombre a `extra_model_paths.yaml` para usarlo. Déjalo en el directorio raíz de ComfyUI, en `ComfyUI/extra_model_paths.yaml`. También puedes encontrar el archivo de ejemplo de configuración [aquí](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example)

Si usas la aplicación [Comfy Desktop](https://docs.comfy.org/es/installation/desktop/windows), haz clic en el menú de la cápsula en la parte superior de la aplicación de escritorio, luego abre la pestaña **Almacenamiento** y agrega allí tus directorios de modelos. La cápsula solo existe en la aplicación de escritorio, no cuando ComfyUI se ejecuta en el navegador.![Menú de la cápsula de Comfy Desktop: pestaña Almacenamiento con la configuración de directorios de modelos](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)O ábrelo directamente en:

  * Windows

  * macOS



    
    
    C:\Users\YourUsername\AppData\Roaming\ComfyUI\extra_models_config.yaml
    
    
    
    ~/Library/Application Support/ComfyUI/extra_models_config.yaml
    

Debes mantener el archivo en el mismo directorio, no muevas estos archivos a otros lugares.

Si el archivo no existe, puedes crearlo tú mismo con cualquier editor de texto.

### 

​

Estructura de ejemplo

Supongamos que quieres agregar las siguientes rutas de modelos a ComfyUI:
    
    
    📁 YOUR_PATH/
      ├── 📁models/
      |   ├── 📁 loras/
      |   │   └── xxxxx.safetensors
      |   ├── 📁 checkpoints/
      |   │   └── xxxxx.safetensors
      |   ├── 📁 vae/
      |   │   └── xxxxx.safetensors
      |   └── 📁 controlnet/
      |       └── xxxxx.safetensors
    

Después puedes configurar el archivo `extra_model_paths.yaml` como se muestra abajo para que ComfyUI reconozca las rutas de modelos en tu dispositivo:
    
    
    my_custom_config:
        base_path: YOUR_PATH
        loras: models/loras/
        checkpoints: models/checkpoints/
        vae: models/vae/
        controlnet: models/controlnet/
    

o
    
    
    my_custom_config:
        base_path: YOUR_PATH/models/
        loras: loras
        checkpoints: checkpoints
        vae: vae
        controlnet: controlnet
    

Para la versión de escritorio, agrega la configuración a la ruta de configuración existente sin sobrescribir la configuración de rutas generada durante la instalación. Haz una copia de seguridad del archivo correspondiente antes de modificarlo, para que puedas restaurarlo si te equivocas.

O puedes consultar el [extra_model_paths.yaml.example](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example) predeterminado para ver más opciones de configuración. Después de guardar, debes **reiniciar ComfyUI** para que los cambios tengan efecto. Abajo está el ejemplo de configuración original:
    
    
    #Rename this to extra_model_paths.yaml and ComfyUI will load it
    
    
    #config for a1111 ui
    #all you have to do is change the base_path to where yours is installed
    a111:
        base_path: path/to/stable-diffusion-webui/
    
        checkpoints: models/Stable-diffusion
        configs: models/Stable-diffusion
        vae: models/VAE
        loras: |
             models/Lora
             models/LyCORIS
        upscale_models: |
                      models/ESRGAN
                      models/RealESRGAN
                      models/SwinIR
        embeddings: embeddings
        hypernetworks: models/hypernetworks
        controlnet: models/ControlNet
    
    #config for comfyui
    #your base path should be either an existing comfy install or a central folder where you store all of your models, loras, etc.
    
    #comfyui:
    #     base_path: path/to/comfyui/
    #     # You can use is_default to mark that these folders should be listed first, and used as the default dirs for eg downloads
    #     #is_default: true
    #     checkpoints: models/checkpoints/
    #     clip: models/clip/
    #     clip_vision: models/clip_vision/
    #     configs: models/configs/
    #     controlnet: models/controlnet/
    #     diffusion_models: |
    #                  models/diffusion_models
    #                  models/unet
    #     embeddings: models/embeddings/
    #     loras: models/loras/
    #     upscale_models: models/upscale_models/
    #     vae: models/vae/
    
    #other_ui:
    #    base_path: path/to/ui
    #    checkpoints: models/checkpoints
    #    gligen: models/gligen
    #    custom_nodes: path/custom_nodes
    
    

Por ejemplo, si tu WebUI está en `D:\stable-diffusion-webui\`, puedes modificar la configuración correspondiente a
    
    
    a111:
        base_path: D:\stable-diffusion-webui\
        checkpoints: models/Stable-diffusion
        configs: models/Stable-diffusion
        vae: models/VAE
        loras: |
             models/Lora
             models/LyCORIS
        upscale_models: |
                      models/ESRGAN
                      models/RealESRGAN
                      models/SwinIR
        embeddings: embeddings
        hypernetworks: models/hypernetworks
        controlnet: models/ControlNet
    

### 

​

Agregar rutas de nodos personalizados adicionales

Además de agregar modelos externos, también puedes agregar rutas de nodos personalizados que no estén en la ruta predeterminada de ComfyUI.

Ten en cuenta que esto no cambiará la ruta de instalación predeterminada de los nodos personalizados, sino que agregará una búsqueda de rutas adicional al iniciar ComfyUI. Aún necesitas completar la instalación de las dependencias de los nodos personalizados en el entorno correspondiente para garantizar la integridad del entorno de ejecución.

Abajo hay un ejemplo de configuración simple (MacOS); modifícalo según tu situación real y agrégalo al archivo de configuración correspondiente, guárdalo y reinicia ComfyUI para que los cambios tengan efecto:
    
    
    my_custom_nodes:
      custom_nodes: /Users/your_username/Documents/extra_custom_nodes
    

## 

​

Problemas comunes

¿ComfyUI es compatible con modelos en formato GGUF?

ComfyUI no es compatible de forma nativa con modelos en formato GGUF. Para usar modelos GGUF, necesitas instalar Nodos personalizados de la Comunidad como [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF).

¿Por qué no encuentro mi modelo?

Si instalaste un modelo pero no lo encuentras en ComfyUI, prueba estos pasos:

  * Verifica que el modelo esté en la ubicación correcta:
    * Ruta predeterminada: `ComfyUI/models/` (p. ej. `checkpoints`, `loras`, `vae`)
    * Para **Comfy Desktop** : Haz clic en el menú cápsula en la parte superior de la aplicación de escritorio y luego abre la pestaña **Storage** para revisar tus directorios de modelos. La cápsula solo existe en la aplicación de escritorio, no cuando ComfyUI se ejecuta en un navegador.
![Menú cápsula de Comfy Desktop: pestaña Storage mostrando las configuraciones de los directorios de modelos](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)
  * Presiona la tecla `r` para actualizar las definiciones de nodos y que ComfyUI pueda detectar el modelo
  * Reinicia ComfyUI
  * Asegúrate de que el modelo correcto esté seleccionado en el nodo cargador



## 

​

¿Quieres un poco más de contexto?

¿Qué significa “modelo” aquí?

Aquí, un **modelo** es un archivo de datos que codifica lo que una red aprendió. Contiene suficiente información para convertir entradas (como texto y ruido) en salidas (como una imagen). Ejemplos comunes en flujos de trabajo de imagen son los checkpoints de **diffusion** , los codificadores de texto/imagen como **CLIP** , y los **upscalers** como RealESRGAN.

Modelos base y variantes de la comunidad

Los grandes modelos **base** de laboratorios y proyectos de código abierto son de propósito general. La comunidad a menudo los **afina** o fusiona en nuevos checkpoints y LoRAs que se ven mejor para un estilo determinado, se ejecutan un poco más ligeros o añaden un nuevo comportamiento. Esto es similar a elegir un checkpoint favorito en Civitai o Hugging Face.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/basic-concepts/models.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/basic-concepts/models)

[Enlaces](https://docs.comfy.org/es/basic-concepts/links)[Dependencias](https://docs.comfy.org/es/basic-concepts/dependencies)
