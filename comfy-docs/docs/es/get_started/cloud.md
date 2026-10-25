---
url: https://docs.comfy.org/es/get_started/cloud/
title: Comfy Cloud - Plataforma oficial de ComfyUI en la nube impulsada por RTX 6000 Pro - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:47.984397+00:00
---

# Comfy Cloud - Plataforma oficial de ComfyUI en la nube impulsada por RTX 6000 Pro - ComfyUI

> Source: https://docs.comfy.org/es/get_started/cloud/

## En esta página

  * ¿Qué es Comfy Cloud?
    * Funciones principales
  * Nube vs local
  * Precios y suscripción
  * Lista de permitidos del firewall de Comfy Cloud
  * Cómo usar ComfyUI Cloud
  * Retroalimentación
    * Cómo detener/salir de Comfy Cloud
  * Preguntas frecuentes
  * Próximos pasos



# Comfy Cloud - Plataforma oficial de ComfyUI en la nube impulsada por RTX 6000 Pro

Copiar páginaCopiar página

Ejecuta flujos de trabajo de ComfyUI en línea con Comfy Cloud, la plataforma oficial en la nube impulsada por GPUs NVIDIA RTX 6000 Pro. No se requiere instalación local.

Copiar páginaCopiar página

## Accede a Comfy Cloud

Haz clic aquí para acceder directamente a ComfyUI Cloud

## 

​

¿Qué es Comfy Cloud?

ComfyUI Cloud es la versión en la nube de ComfyUI, con las mismas funciones que la versión local. Todo está preinstalado y listo para usar.

### 

​

Funciones principales

## Sin configuración

No se requiere instalación. Todos los modelos y nodos personalizados están preinstalados y listos para usar

## GPUs potentes

Ejecuta flujos de trabajo rápidamente en las potentes GPUs de nuestros servidores, sin necesidad de tener tu propio hardware

## Siempre actualizado

Se mantiene automáticamente al día con las últimas versiones y funciones de ComfyUI

## Acceso desde cualquier lugar

Usa ComfyUI desde cualquier dispositivo con conexión a internet. No necesitas instalar nada localmente

## Colaboración en equipo

Crea espacios de trabajo en equipo para colaborar con los miembros de tu equipo. Comparte planes de suscripción, créditos y flujos de trabajo.

## 

​

Nube vs local

ComfyUI ofrece tanto una versión oficial en la nube, [Comfy Cloud](https://comfy.org/cloud), como una versión de código abierto autoalojada. Si tienes una GPU potente, ejecutar ComfyUI localmente es una gran opción. La versión en la nube, por otro lado, es un servicio en línea que está listo para usar al instante: simplemente abre la URL, sin necesidad de instalación ni configuración.

Categoría| Comfy Cloud| Autoalojado (ComfyUI local)  
---|---|---  
**Costo**|  Nivel gratuito y planes de suscripción de pago| Gratis  
**GPU**|  Potentes Blackwell RTX 6000 Pro| Usa tu propia GPU  
**Conocimientos técnicos**|  No se requieren conocimientos técnicos.| Aunque las versiones de escritorio y portátil te ofrecen formas sencillas de empezar, tendrás que solucionar problemas con la instalación de nodos personalizados y con la instalación local.  
**Nodos personalizados**|  Usa nodos personalizados preinstalados y olvídate de los problemas de compatibilidad.| Instala cualquier nodo personalizado que quieras, pero tendrás que administrarlo tú mismo.  
**Modelos**|  Usa modelos preinstalados. Importa modelos desde Civitai y Hugging Face.| Usa cualquier modelo que quieras, pero primero tendrás que descargarlo.  
**Diferencias destacadas**|  Es fácil incorporar a tu equipo con [Espacios de trabajo](https://docs.comfy.org/cloud/workspace)| Funciona sin conexión, personalizable sin límites  
**Empezar**| [Ejecutar ComfyUI Cloud](https://comfy.org/cloud)| [Instalar ComfyUI localmente](https://docs.comfy.org/es/installation/system_requirements)  
  
## 

​

Precios y suscripción

## Consulta los precios

Consulta las opciones de precios y suscripción de Comfy Cloud

## 

​

Lista de permitidos del firewall de Comfy Cloud

Permite el tráfico saliente HTTPS y WebSocket en TCP 443 hacia:

  * **Aplicación:** `cloud.comfy.org`, `api.comfy.org`, `cdn.comfy.org`
  * **Cargas y salidas:** `comfy-hub-assets.comfy.org`, `storage.googleapis.com`
  * **Inicio de sesión:** `dreamboothy.firebaseapp.com`, `identitytoolkit.googleapis.com`, `securetoken.googleapis.com`, `apis.google.com`, `challenges.cloudflare.com`
  * **Otras funciones:** `registry.comfy.org`, `*.algolia.net`, `media.comfy.org`



## 

​

Cómo usar ComfyUI Cloud

Usar ComfyUI Cloud es esencialmente lo mismo que usar tu ComfyUI local. Si es tu primera vez usando ComfyUI, aquí tienes algunos consejos rápidos para empezar:

1

Selecciona una plantilla

Haz clic en el icono de plantillas en la barra lateral izquierda para explorar los flujos de trabajo disponibles.![Abrir plantilla de flujo de trabajo](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a32875bb4e6d1c92ea4f893831aff925)

2

Selecciona el flujo de trabajo que quieres ejecutar

Haz clic en la plantilla que quieres ejecutar.![Seleccionar plantilla de flujo de trabajo](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b16043c4ad9372834eb7fe49c1180eee)

3

Actualiza las entradas de la plantilla

  1. En el flujo de trabajo cargado, como hemos preinstalado todos los modelos en la versión de la Nube, todas las plantillas están listas para ejecutarse inmediatamente después de cargarse.
  2. Si necesitas hacer cambios, solo tienes que proporcionar imágenes de entrada o prompts de texto. Revisa el nodo `Load Image` o el nodo `CLIP Text Encode`. ![Revisar entradas](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=56ca79d24c79e666146c927263c96e99)



4

Ejecuta tu flujo de trabajo

Si todo es correcto, haz clic en el icono “Ejecutar” o usa el atajo “Ctrl + Enter” para ejecutar el flujo de trabajo.![Ejecutar flujo de trabajo](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=546f1e0003941deba2006a36d8f9ed34)

5

Ver la salida

Después de hacer clic en ejecutar, nuestro servicio comenzará a asignar una máquina para tu flujo de trabajo. Puedes consultar el estado de ejecución del flujo de trabajo correspondiente en el panel de Cola.![Ver cola](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=4ac366407cf13fa84e55ef7948cff36e)

6

Guardar el contenido localmente

Una vez completada la ejecución del flujo de trabajo, puedes guardar el contenido generado localmente. Según el tipo de recurso, el método para guardar es el siguiente:

  * Guardar imágenes

  * Guardar vídeos

  * Guardar audio

  * Guardar recursos 3D




En el panel de Cola o en el nodo de guardar imagen, haz clic derecho sobre la imagen generada y selecciona “Guardar imagen” para guardarla localmente.![Guardar recursos de imagen](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a15e70a3649537fb8c6adc50689dfbe7)

En el panel de Cola o en el nodo de guardar vídeo:

  1. Haz clic en los tres puntos del componente de reproducción del navegador para abrir el menú
  2. Selecciona “Descargar” para guardar el vídeo localmente. ![Guardar recursos de vídeo](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=2c987025c1c25e954a3065775ef5223d)



En el panel de Cola o en el nodo de guardar audio:

  1. Haz clic en los tres puntos del componente de reproducción del navegador para abrir el menú
  2. Selecciona “Descargar” para guardar el archivo de audio localmente. ![Guardar recursos de audio](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8d876d9c3b89b2ae9f1e84ba8b3e9887)



En el menú del nodo de visor 3D, selecciona la opción “Exportar”, elige el formato en el que quieres guardar y el archivo 3D se guardará localmente.![Guardar recursos 3D](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5e121107826658a3e1725b8d9840d94b)

## 

​

Retroalimentación

Si tienes alguna idea, sugerencia o te encuentras con algún problema, simplemente haz clic en el icono de “Retroalimentación”. Esto nos enviará tu retroalimentación directamente. ![Retroalimentación](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f1306e3587e441fc9964ffc0f9e4cc73)

### 

​

Cómo detener/salir de Comfy Cloud

Las sesiones de Cloud solo te cobran mientras la GPU está ejecutándose activamente. Cuando cierras la pestaña del navegador, la sesión se detiene automáticamente: puedes cerrarla en cualquier momento, igual que una pestaña normal del navegador.

## 

​

Preguntas frecuentes

## Ver preguntas frecuentes

Consulta las preguntas frecuentes y sus respuestas acerca de Comfy Cloud, incluidos precios, funciones, limitaciones y más

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
