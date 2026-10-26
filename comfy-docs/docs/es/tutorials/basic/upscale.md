---
url: https://docs.comfy.org/es/tutorials/basic/upscale/
title: Flujo de trabajo de upscale de im\u00e1genes en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:42.074988+00:00
---

# Flujo de trabajo de upscale de imágenes en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/basic/upscale/

## En esta página

Volver arriba

  * ¿Qué es el upscale de imágenes?
  * Flujo de trabajo de upscale
    * Instalación de modelos
    * Flujo de trabajo y recursos
    * Completar el flujo de trabajo paso a paso
  * Flujo de trabajo combinado de texto a imagen
  * Consejos adicionales



Basic Examples

# Flujo de trabajo de upscale de imágenes en ComfyUI

Copiar páginaCopiar página

Haz upscale de imágenes en ComfyUI: carga un modelo de upscale, arma el flujo de trabajo y encadénalo después de texto a imagen para obtener mayor resolución.

Copiar páginaCopiar página

## 

​

¿Qué es el upscale de imágenes?

La ampliación de imágenes es el proceso de convertir imágenes de baja resolución en imágenes de alta resolución mediante algoritmos. A diferencia de los métodos tradicionales de interpolación, los modelos de ampliación con IA (como ESRGAN) pueden reconstruir detalles de forma inteligente mientras mantienen la calidad de la imagen. Por ejemplo, el modelo SD1.5 predeterminado suele tener problemas para generar imágenes de gran tamaño. Para obtener resultados de alta resolución, por lo general generamos primero imágenes más pequeñas y después aplicamos técnicas de ampliación. Este artículo abarca uno de los muchos métodos de ampliación de ComfyUI. En este tutorial, te mostraremos cómo:

  1. Descargar e instalar modelos de ampliación
  2. Realizar una ampliación básica de imágenes
  3. Combinar flujos de trabajo de texto a imagen con la ampliación



¿Buscas opciones de ampliación más avanzadas? Consulta nuestra completa [Guía de ampliación de imágenes](https://docs.comfy.org/es/tutorials/utility/image-upscale), que abarca varios modelos y casos de uso, como la mejora de retratos, la fotografía de productos y mucho más.

## 

​

Flujo de trabajo de upscale

### 

​

Instalación de modelos

Descarga de los modelos ESRGAN requeridos:

1

Visitar OpenModelDB

Visita [OpenModelDB](https://openmodeldb.info/) para buscar y descargar modelos de ampliación (por ejemplo, RealESRGAN)![OpenModelDB](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e5a63a5efe9b72af78d7331179cef6ba)Como se muestra:

  1. Filtra los modelos por tipo de imagen con el selector de categoría
  2. El factor de ampliación del modelo se indica en la esquina superior derecha (por ejemplo, 2x en la captura de pantalla)

Usaremos el modelo [4x-ESRGAN](https://openmodeldb.info/models/4x-ESRGAN) para este tutorial. Haz clic en el botón `Download` en la página de detalles del modelo.![OpenModelDB_download](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=678b9869dfcf612056bdc38fcec2f8f4)

2

Guardar los archivos del modelo en el directorio

Guarda el archivo del modelo (.pth) en el directorio `ComfyUI/models/upscale_models`

### 

​

Flujo de trabajo y recursos

Descarga y arrastra la siguiente imagen a ComfyUI para cargar el flujo de trabajo básico de ampliación: ![Flujo de trabajo de ampliación](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/upscale_workflow.png)

Puedes arrastrar directamente a ComfyUI las imágenes que contienen JSON de flujo de trabajo en sus metadatos o cargarlas con el menú `Workflows` -> `Open (ctrl+o)`.

Usa esta imagen en un tamaño más pequeño como entrada: ![Entrada de ampliación](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ce8c5f3cd94c0cbde5ded50f09204d5b)

### 

​

Completar el flujo de trabajo paso a paso

Sigue los pasos del diagrama a continuación para asegurarte de que el flujo de trabajo se ejecute correctamente. ![Flujo de trabajo de ampliación](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=632d1202982e8e7c59974a4152304967)

  1. Asegúrate de que `Load Upscale Model` cargue `4x-ESRGAN.pth`
  2. Sube la imagen de entrada al nodo `Load Image`
  3. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen

Los componentes principales son los nodos `Load Upscale Model` y `Upscale Image (Using Model)`, que reciben una imagen de entrada y la amplían con el modelo seleccionado.

## 

​

Flujo de trabajo combinado de texto a imagen

Una vez que domines la ampliación básica, puedes combinarla con el flujo de trabajo de [texto a imagen](https://docs.comfy.org/es/tutorials/basic/text-to-image). Para conocer los conceptos básicos de texto a imagen, consulta el [tutorial de texto a imagen](https://docs.comfy.org/es/tutorials/basic/text-to-image). Descarga y arrastra esta imagen a ComfyUI para cargar el flujo de trabajo combinado: ![Flujo de trabajo de ampliación de texto a imagen](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=98c8d536f0a76025092f8fec157002f8) Este flujo de trabajo conecta la imagen de salida de texto a imagen directamente con los nodos de ampliación para el procesamiento final.

## 

​

Consejos adicionales

Características de los modelos:

  * **RealESRGAN** : Ampliación de uso general
  * **BSRGAN** : Destaca con texto y bordes definidos
  * **SwinIR** : Conserva las texturas naturales, ideal para paisajes



  1. **Ampliación encadenada** : combina varios nodos de ampliación (por ejemplo, 2x → 4x) para lograr un aumento ultra alto
  2. **Flujo de trabajo híbrido** : conecta nodos de ampliación después de la generación para crear pipelines de “generar+mejorar”
  3. **Pruebas comparativas** : distintos modelos funcionan mejor con tipos de imagen específicos; prueba varias opciones



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/basic/upscale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/basic/upscale)

[Outpaint](https://docs.comfy.org/es/tutorials/basic/outpaint)[LoRA](https://docs.comfy.org/es/tutorials/basic/lora)
