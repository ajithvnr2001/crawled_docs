---
url: https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-1/
title: OpenAI GPT-Image-1 en ComfyUI: texto a imagen y relleno inteligente - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:53.238707+00:00
---

# OpenAI GPT-Image-1 en ComfyUI: texto a imagen y relleno inteligente - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-1/

## En esta página

Volver arriba

  * En qué destaca GPT-Image-1
  * Salidas de ejemplo
  * Descripción de parámetros
    * Parámetros requeridos
    * Parámetros de widget
    * Parámetros opcionales
  * Ejemplos de uso
    * Ejemplo de texto a imagen
    * Ejemplo de imagen a imagen
    * Ejemplo de entrada con varias imágenes
    * Flujo de trabajo de relleno inteligente
  * Preguntas frecuentes



OpenAI

# OpenAI GPT-Image-1 en ComfyUI: texto a imagen y relleno inteligente

Copiar páginaCopiar página

Genera y edita imágenes con OpenAI GPT-Image-1 en ComfyUI: texto a imagen, imagen a imagen con referencia, relleno inteligente con máscara y varias imágenes de entrada.

Copiar páginaCopiar página

![Captura de pantalla del nodo OpenAI GPT-Image-1](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=243b4200a707b55f1c4fd88d4edf51a9) OpenAI GPT-Image-1 forma parte de la serie de Nodos asociados de ComfyUI, que permite generar imágenes con el modelo **GPT-Image-1** de OpenAI. Es el mismo modelo que se usa para generar imágenes en ChatGPT 4o. El nodo **OpenAI GPT-Image-1** genera imágenes de forma síncrona a través de la API de generación de imágenes de OpenAI. Recibe prompts de texto y devuelve imágenes que coinciden con la descripción. GPT-Image-1 es el modelo de generación de imágenes más avanzado de OpenAI disponible en la actualidad, capaz de crear imágenes muy detalladas y realistas.

## 

​

En qué destaca GPT-Image-1

  * Generación de texto a imagen
  * Funcionalidad de edición de imágenes (Relleno inteligente mediante máscaras)
  * Generación de imagen a imagen a partir de una imagen de referencia
  * Entrada de varias imágenes: combina varias imágenes de referencia en una sola generación



## 

​

Salidas de ejemplo

Generación de texto a imagen a partir de un solo prompt de texto: ![Flujo de trabajo openai-gpt-image-1 de ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/text2image.png) Generación de imagen a imagen a partir de una imagen de referencia: ![Flujo de trabajo openai-gpt-image-1 de ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/image2image.png) Entrada de varias imágenes, combinando varias imágenes de referencia en una sola generación: ![Ejemplo de entrada de varias imágenes](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/multiple_image_input.png) Relleno inteligente, reemplazando un área enmascarada de una imagen de entrada: ![Flujo de trabajo openai-gpt-image-1 de ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/inpaint.png)

Para usar los Nodos asociados, debes asegurarte de haber iniciado sesión correctamente y de estar utilizando un entorno de red permitido. Consulta la sección [Descripción general de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview) de la documentación para conocer los requisitos específicos de uso de los Nodos asociados.

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

Descripción de parámetros

### 

​

Parámetros requeridos

Parámetro| Tipo| Descripción  
---|---|---  
`prompt`| Texto| Prompt de texto que describe el contenido de la imagen que quieres generar  
  
### 

​

Parámetros de widget

Parámetro| Tipo| Opciones| Predeterminado| Descripción  
---|---|---|---|---  
`seed`| Entero| 0-2147483647| 0| Semilla aleatoria utilizada para controlar los resultados de generación  
`quality`| Opción| low, medium, high| low| Ajuste de calidad de imagen; afecta el costo y el tiempo de generación  
`background`| Opción| opaque, transparent| opaque| Indica si la imagen devuelta tiene fondo  
`size`| Opción| auto, 1024x1024, 1024x1536, 1536x1024| auto| Tamaño de la imagen generada  
`n`| Entero| 1-8| 1| Número de imágenes a generar  
  
### 

​

Parámetros opcionales

Parámetro| Tipo| Opciones| Predeterminado| Descripción  
---|---|---|---|---  
`image`| Imagen| Cualquier entrada de imagen| None| Imagen de referencia opcional para la edición de imágenes  
`mask`| Máscara| Entrada de máscara| None| Máscara opcional para relleno inteligente (las áreas blancas se reemplazarán)  
  
## 

​

Ejemplos de uso

### 

​

Ejemplo de texto a imagen

La imagen siguiente contiene un flujo de trabajo sencillo de texto a imagen. Descarga la imagen y arrástrala a ComfyUI para cargar el flujo de trabajo correspondiente. ![flujo de trabajo de ComfyUI openai-gpt-image-1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/text2image.png) El flujo de trabajo correspondiente es muy sencillo: ![ejemplo de flujo de trabajo de ComfyUI openai-gpt-image-1](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e7308997e027153d914a61418a9c0058) Solo tienes que cargar el nodo `OpenAI GPT-Image-1`, escribir en el nodo `prompt` la descripción de la imagen que quieres generar, conectar un nodo `Save Image` y luego ejecutar el flujo de trabajo.

### 

​

Ejemplo de imagen a imagen

La imagen siguiente contiene un flujo de trabajo sencillo de imagen a imagen. Descarga la imagen y arrástrala a ComfyUI para cargar el flujo de trabajo correspondiente. ![flujo de trabajo de ComfyUI openai-gpt-image-1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/image2image.png) Usaremos la siguiente imagen como entrada: ![entrada del flujo de trabajo de ComfyUI openai-gpt-image-1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/input.webp) En este flujo de trabajo usamos el nodo `OpenAI GPT-Image-1` para generar imágenes y el nodo `Load Image` para cargar la imagen de entrada, que luego se conecta a la entrada `image` del nodo `OpenAI GPT-Image-1`. ![ejemplo de flujo de trabajo de ComfyUI openai-gpt-image-1](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=05cab30de9ab5bc2e0865c0a367f82fc)

### 

​

Ejemplo de entrada con varias imágenes

Descarga la imagen siguiente y arrástrala a ComfyUI para cargar el flujo de trabajo correspondiente. ![Ejemplo de entrada con varias imágenes](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/multiple_image_input.png) Usa la imagen del sombrero que aparece a continuación como imagen de entrada adicional. ![Sombrero](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/hat.webp) El flujo de trabajo correspondiente se muestra en la siguiente imagen: ![Ejemplo de entrada con varias imágenes](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=125236ed762b17ae1e711fa702663f74) El nodo `Batch Images` se usa para cargar varias imágenes en el nodo `OpenAI GPT-Image-1`.

### 

​

Flujo de trabajo de relleno inteligente

GPT-Image-1 también admite la función de edición de imágenes, que te permite especificar las zonas que quieres reemplazar mediante una máscara. A continuación se muestra un ejemplo sencillo de flujo de trabajo de relleno inteligente: Descarga la imagen siguiente y arrástrala a ComfyUI para cargar el flujo de trabajo correspondiente. Seguiremos usando la imagen de entrada de la sección del flujo de trabajo de imagen a imagen. ![flujo de trabajo de ComfyUI openai-gpt-image-1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/inpaint.png) El flujo de trabajo correspondiente se muestra en la imagen ![ejemplo de flujo de trabajo de ComfyUI openai-gpt-image-1](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=12d74944bf8905025606740b820918a8) En comparación con el flujo de trabajo de imagen a imagen, aquí usamos el MaskEditor del nodo `Load Image` desde el menú del clic derecho para dibujar una máscara y luego la conectamos a la entrada `mask` del nodo `OpenAI GPT-Image-1` para completar el flujo de trabajo. **Notas**

  * La máscara y la imagen deben tener el mismo tamaño
  * Al introducir imágenes grandes, el nodo redimensiona automáticamente la imagen a un tamaño adecuado



## 

​

Preguntas frecuentes

¿Por qué no encuentro los Nodos asociados?

Actualiza tu ComfyUI a la última versión (el último commit o la última [versión de escritorio](https://www.comfy.org/download)). Es posible que agreguemos más compatibilidad con API en el futuro y se actualicen los nodos correspondientes, así que mantén tu ComfyUI actualizado.

Ten en cuenta que debes distinguir entre la versión nocturna y la versión de lanzamiento. En algunos casos, la última versión `release` puede no actualizarse a tiempo en comparación con la versión `nightly`. Como todavía estamos iterando rápidamente, asegúrate de usar la última versión cuando no encuentres el nodo correspondiente.

¿Por qué no puedo usar / iniciar sesión en los Nodos asociados?

El acceso a la API requiere que tu solicitud actual se base en un entorno de red seguro. Los requisitos actuales para acceder a la API son los siguientes:

  * La red local solo permite el acceso desde `127.0.0.1` o `localhost`, lo que puede significar que no puedas usar los Nodos asociados en un servicio de ComfyUI iniciado con el parámetro `--listen` en un entorno de LAN.
  * Poder acceder a nuestro servicio de API normalmente (es posible que se requiera un servicio de proxy en algunas regiones).
  * Tu cuenta no tiene suficientes [créditos](https://docs.comfy.org/es/interface/credits).



¿Por qué no puedo usar un Nodo asociado incluso después de iniciar sesión, o por qué me sigue pidiendo que inicie sesión mientras lo uso?

  * Actualmente, solo se admite el acceso desde `127.0.0.1` o `localhost`.
  * Asegúrate de que tu cuenta tenga suficientes créditos.



¿Se pueden usar los Nodos asociados de forma gratuita?

Los Nodos asociados requieren créditos para las llamadas a la API de modelos de código cerrado, por lo que no admiten el uso gratuito.

¿Cómo comprar créditos?

Consulta la siguiente documentación:

  1. [Cuenta de Comfy](https://docs.comfy.org/es/interface/user): busca la sección `User` en el menú de configuraciones para iniciar sesión.
  2. [Créditos](https://docs.comfy.org/es/interface/credits): después de iniciar sesión, la interfaz de configuraciones mostrará el menú de créditos. Puedes comprar créditos en `Settings` → `Credits`. Usamos un sistema de prepago, por lo que no habrá cargos inesperados.
  3. Completa el pago a través de Stripe.
  4. Comprueba si los créditos se han actualizado. Si no es así, intenta reiniciar o actualizar la página.



¿Se pueden reembolsar los créditos no utilizados?

Actualmente, no admitimos reembolsos de créditos. Si crees que hay un error que resulte en un saldo sin usar debido a problemas técnicos, por favor [contacta con soporte](mailto:support@comfy.org).

¿Los créditos pueden quedar en negativo?

Los créditos no están pensados para usarse como un saldo negativo ni como una línea de crédito. Sin embargo, debido a condiciones de carrera en las que los nodos asociados no siempre informan los costos antes de la ejecución, una sola ejecución puede consumir más créditos que tu saldo restante y dar como resultado temporalmente un saldo negativo después de completarse. Cuando tu saldo sea negativo, no podrás ejecutar Nodos asociados hasta que recargues y restaures un saldo positivo. Asegúrate de tener suficientes créditos antes de realizar llamadas a la API.

¿Dónde puedo consultar el uso y los gastos?

Visita el menú [Créditos](https://docs.comfy.org/es/interface/credits) después de iniciar sesión para consultar los créditos correspondientes.

¿Es posible usar mi propia clave API?

Actualmente, los Nodos asociados todavía están en fase de pruebas y aún no admiten esta función, pero hemos considerado agregarla.

¿Expiran los créditos?

Sí, la expiración depende del tipo de créditos:

  * **Créditos mensuales** : expiran al final de tu período de facturación
  * **Créditos de recarga** : expiran 1 año a partir de la fecha de compra



¿Se pueden transferir o compartir los créditos?

No, tus créditos no se pueden transferir a otros usuarios y están limitados a la cuenta con la sesión iniciada actualmente, pero no restringimos la cantidad de dispositivos que pueden iniciar sesión.

¿Puedo usar la misma cuenta en diferentes dispositivos?

No limitamos la cantidad de dispositivos que pueden iniciar sesión; puedes usar tu cuenta donde quieras.

¿Cómo puedo solicitar que se elimine mi cuenta o mi información?

Envía una solicitud por correo electrónico a [support@comfy.org](mailto:support@comfy.org) y eliminaremos tu información.

¿Existe moderación de contenido para los Nodos asociados?

Los Nodos asociados envían tus entradas (prompts, imágenes y otro contenido) a proveedores externos para su procesamiento. Estos proveedores aplican sus propias políticas de moderación de contenido. No envíes contenido NSFW ni otro contenido prohibido a los Nodos API.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/openai/gpt-image-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/openai/gpt-image-1)

[Gpt Image 2](https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2)[Quiver AI](https://docs.comfy.org/es/tutorials/partner-nodes/quiver/overview)
