---
url: https://docs.comfy.org/es/get_started/cloud/
title: Comfy Cloud - Plataforma oficial de ComfyUI en la nube impulsada por RTX 6000 Pro - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:02.707385+00:00
---

# Comfy Cloud - Plataforma oficial de ComfyUI en la nube impulsada por RTX 6000 Pro - ComfyUI

> Source: https://docs.comfy.org/es/get_started/cloud/

## En esta página

Volver arriba

  * ¿Qué es Comfy Cloud?
    * Funciones principales
  * Nube vs local
    * Nodos personalizados en Comfy Cloud
  * Precios y suscripción
    * Límites de concurrencia
  * Dominios permitidos en el firewall de Comfy Cloud
  * Cómo usar ComfyUI Cloud
  * Comentarios
    * Cómo detener/salir de Comfy Cloud
  * Preguntas frecuentes
  * Próximos pasos



# Comfy Cloud - Plataforma oficial de ComfyUI en la nube impulsada por RTX 6000 Pro

Copiar páginaCopiar página

Ejecuta flujos de trabajo de ComfyUI en línea con Comfy Cloud, la plataforma oficial con GPUs NVIDIA RTX 6000 Pro. Sin instalación local.

Copiar páginaCopiar página

## Accede a Comfy Cloud

Abre ComfyUI Cloud

## 

​

¿Qué es Comfy Cloud?

ComfyUI Cloud es la versión en la nube de ComfyUI, con las mismas funciones que la versión local. Todo viene preinstalado y listo para usar.

### 

​

Funciones principales

## Sin configuración

No se requiere instalación. Todos los modelos y nodos personalizados están preinstalados y listos para usar

## GPUs potentes

Ejecuta flujos de trabajo rápidamente en las potentes GPUs de nuestros servidores, sin necesidad de tener tu propio hardware

## Siempre actualizado

Se actualiza solo a las últimas versiones y funciones de ComfyUI

## Acceso desde cualquier lugar

Usa ComfyUI desde cualquier dispositivo con conexión a internet. No necesitas instalar nada localmente

## Colaboración en equipo

Crea espacios de trabajo en equipo para colaborar con los miembros de tu equipo. Comparte planes de suscripción, créditos y flujos de trabajo.

## 

​

Nube vs local

ComfyUI ofrece una versión oficial en la nube, [Comfy Cloud](https://comfy.org/cloud), y una versión de código abierto que puedes autoalojar. Si tienes una GPU potente, ejecutar ComfyUI en local es una gran opción. La nube, en cambio, es un servicio en línea listo al instante: abre la URL, sin instalar ni configurar nada.

Categoría| Comfy Cloud| Autoalojado (ComfyUI local)  
---|---|---  
**Costo**|  Nivel gratuito y planes de suscripción de pago| Gratis  
**GPU**|  Potentes Blackwell RTX 6000 Pro| Usa tu propia GPU  
**Conocimientos técnicos**|  No se requieren conocimientos técnicos.| Aunque Desktop y Portable facilitan el comienzo, tendrás que resolver por tu cuenta la instalación de nodos personalizados y el entorno local.  
**Nodos personalizados**|  Usa nodos personalizados preinstalados y olvídate de los problemas de compatibilidad.| Instala cualquier nodo personalizado que quieras, pero tendrás que administrarlo tú mismo.  
**Modelos**|  Usa modelos preinstalados. Importa modelos desde Civitai y Hugging Face.| Usa cualquier modelo que quieras, pero primero tendrás que descargarlo.  
**Diferencias destacadas**|  Es fácil incorporar a tu equipo con [Espacios de trabajo](https://docs.comfy.org/es/cloud/workspace)| Funciona sin conexión, personalizable sin límites  
**Empezar**| [Ejecutar ComfyUI Cloud](https://comfy.org/cloud)| [Instalar ComfyUI localmente](https://docs.comfy.org/es/installation/system_requirements)  
  
### 

​

Nodos personalizados en Comfy Cloud

Comfy Cloud ejecuta un conjunto fijo de nodos personalizados que mantiene Comfy. No puedes instalar tus propios paquetes de nodos allí, así que un flujo de trabajo que dependa de un paquete que Cloud no incluye no se ejecutará tal cual. Comfy Cloud marca los nodos que no puede ejecutar en dos sitios: quedan señalados en el lienzo, y la pestaña Errors del [panel derecho](https://docs.comfy.org/es/interface/right-side-panel) los lista bajo **Unsupported Node Packs**. Esos nodos se reportan automáticamente para priorizar el soporte de esos paquetes en Cloud. Para ejecutar el flujo de trabajo, reemplaza esos nodos por otros compatibles, o ábrelo en una instalación local de ComfyUI.

## 

​

Precios y suscripción

## Consulta los precios

Consulta las opciones de precios y suscripción de Comfy Cloud

### 

​

Límites de concurrencia

La interfaz de Comfy Cloud no permite ejecutar más de un flujo de trabajo a la vez. Cada persona puede ejecutar un flujo de trabajo a la vez en el editor; los flujos adicionales esperan en la cola y se ejecutan uno tras otro. Ejecutar varios trabajos en paralelo solo se admite cuando envías los flujos de trabajo a través de la API, lo que requiere una suscripción de pago. Consulta [Tareas simultáneas](https://docs.comfy.org/es/development/deploy/cloud-usage#tareas-simult%C3%A1neas) en la documentación para desarrolladores para más detalles. En los planes Team y Enterprise, la concurrencia es por miembro: cada persona del espacio de trabajo tiene su propio límite de concurrencia, por lo que los trabajos en ejecución de un miembro nunca bloquean a los de otro.

## 

​

Dominios permitidos en el firewall de Comfy Cloud

Permite el tráfico saliente HTTPS y WebSocket en TCP 443 hacia:

  * **Aplicación:** `cloud.comfy.org`, `api.comfy.org`, `cdn.comfy.org`
  * **Cargas y salidas:** `comfy-hub-assets.comfy.org`, `storage.googleapis.com`
  * **Inicio de sesión:** `dreamboothy.firebaseapp.com`, `identitytoolkit.googleapis.com`, `securetoken.googleapis.com`, `apis.google.com`, `challenges.cloudflare.com`
  * **Otras funciones:** `registry.comfy.org`, `*.algolia.net`, `media.comfy.org`



## 

​

Cómo usar ComfyUI Cloud

Usar ComfyUI Cloud es casi igual que usar ComfyUI en local. Si es tu primera vez con ComfyUI, aquí van unos consejos rápidos:

1

Selecciona una plantilla

Haz clic en el icono de plantillas en la barra lateral izquierda para explorar los flujos de trabajo disponibles.![Abrir plantilla de flujo de trabajo](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a32875bb4e6d1c92ea4f893831aff925)

2

Selecciona el flujo de trabajo que quieres ejecutar

Haz clic en la plantilla que quieres ejecutar.![Seleccionar plantilla de flujo de trabajo](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b16043c4ad9372834eb7fe49c1180eee)

3

Actualiza las entradas de la plantilla

  1. En el flujo de trabajo cargado, como todos los modelos ya están preinstalados en la nube, las plantillas quedan listas para ejecutarse en cuanto se cargan.
  2. Si necesitas cambiar algo, basta con aportar imágenes de entrada o prompts de texto. Revisa el nodo `Load Image` o el nodo `CLIP Text Encode`. ![Revisar entradas](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=56ca79d24c79e666146c927263c96e99)



4

Ejecuta tu flujo de trabajo

Si todo está bien, haz clic en el icono **Run** o usa el atajo `Ctrl + Enter` para ejecutar el flujo de trabajo.![Ejecutar flujo de trabajo](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=546f1e0003941deba2006a36d8f9ed34)

5

Ver la salida

Tras pulsar Run, el servicio empezará a asignar una máquina a tu flujo de trabajo. Puedes ver el estado de ejecución en el panel de cola.![Ver cola](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=4ac366407cf13fa84e55ef7948cff36e)

6

Guardar el contenido localmente

Cuando termine la ejecución, puedes guardar el contenido generado en tu equipo. Según el tipo de recurso:

  * Guardar imágenes

  * Guardar videos

  * Guardar audio

  * Guardar recursos 3D




En el panel de cola o en el nodo Save Image, haz clic derecho sobre la imagen generada y elige **Save Image** para guardarla en local.![Guardar recursos de imagen](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a15e70a3649537fb8c6adc50689dfbe7)

En el panel de cola o en el nodo de guardar video:

  1. Haz clic en los tres puntos del reproductor del navegador para abrir el menú
  2. Selecciona **Download** para guardar el video en local. ![Guardar recursos de video](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=2c987025c1c25e954a3065775ef5223d)



En el panel de cola o en el nodo de guardar audio:

  1. Haz clic en los tres puntos del reproductor del navegador para abrir el menú
  2. Selecciona **Download** para guardar el audio en local. ![Guardar recursos de audio](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8d876d9c3b89b2ae9f1e84ba8b3e9887)



En el menú del nodo de visor 3D, elige **Export** , selecciona el formato y el archivo 3D se guardará en local.![Guardar recursos 3D](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5e121107826658a3e1725b8d9840d94b)

## 

​

Comentarios

Si tienes alguna idea, sugerencia o te encuentras con un problema, haz clic en el icono **Feedback**. Nos lo enviará directamente. ![Feedback](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f1306e3587e441fc9964ffc0f9e4cc73)

### 

​

Cómo detener/salir de Comfy Cloud

Las sesiones de Cloud solo cobran mientras la GPU está en uso. Al cerrar la pestaña del navegador, la sesión se detiene sola: puedes cerrarla cuando quieras, como cualquier pestaña.

## 

​

Preguntas frecuentes

## Ver preguntas frecuentes

Consulta las preguntas frecuentes sobre Comfy Cloud: precios, funciones, limitaciones y más

## 

​

Próximos pasos

## Cloud API

Ejecuta flujos de trabajo de forma programática mediante la Cloud API

## Tutoriales

Explora tutoriales para aprender flujos de trabajo de ComfyUI

## Soporte

Únete a nuestra comunidad de Discord para recibir ayuda

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/get_started/cloud.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/get_started/cloud)

[Inicio](https://docs.comfy.org/es)[Requisitos del sistema](https://docs.comfy.org/es/installation/system_requirements)
