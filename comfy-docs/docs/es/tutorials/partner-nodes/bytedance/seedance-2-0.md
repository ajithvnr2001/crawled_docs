---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-0/
title: Seedance 2.0 - Generaci\u00f3n de video con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.194950+00:00
---

# Seedance 2.0 - Generación de video con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-0/

## En esta página

Volver arriba

  * En qué destaca Seedance 2.0
  * Flujos de trabajo disponibles
    * Texto a video (T2V)
    * Referencia a video (R2V)
    * Primer y último fotograma a video (FLF2V)
    * Referencia a video 4K (R2V 4K)
    * Convertir un storyboard en video
  * Seedance 2.0 Mini
    * Seedance 2.0 Mini de texto a video
    * Seedance 2.0 Mini de referencia a video
  * Usar retratos de personas reales y retratos generados con IA en ComfyUI para Seedance 2.0
    * Retrato generado con IA
    * Retrato de persona real



ByteDance

# Seedance 2.0 - Generación de video con IA

Copiar páginaCopiar página

Genera video desde texto, imágenes, video y audio con Seedance 2.0 en ComfyUI: audio sincronizado, personajes consistentes y control de cámara cinematográfico.

Copiar páginaCopiar página

Seedance 2.0 es el modelo de generación de video multimodal de nueva generación de ByteDance, ahora disponible en ComfyUI. Acepta texto, imágenes, video y audio como entradas unificadas y produce video de alta calidad con audio sincronizado, personajes consistentes y movimiento de cámara cinematográfico en una sola pasada.

## 

​

En qué destaca Seedance 2.0

  * **Entrada multimodal** : crea prompts con texto además de imágenes, video y audio
  * **Sincronía de audio y video** : genera video y audio juntos
  * **Control de dirección** : los movimientos de cámara y el ritmo de los planos se mantienen bajo control
  * **Consistencia** : mantén los personajes y las escenas estables a lo largo de un clip
  * **Edición y extensión** : edita el material o extiende los clips sin empezar de nuevo

Con estas capacidades, Seedance 2.0 se adapta a una amplia variedad de casos de uso, incluidos publicidad, series cortas, previsualización de cine, exhibición de productos, contenido con personajes virtuales y recursos para juegos y animación.

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

Flujos de trabajo disponibles

### 

​

Texto a video (T2V)

Genera un video a partir de un prompt de texto, con Seedance 2.0 encargándose de la escena, el movimiento y el ritmo. ![Vista previa del flujo de trabajo Texto a video de Seedance 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_t2v-1.webp)

## Ejecutar Texto a video en Cloud

Prueba el flujo de trabajo Texto a video al instante en Comfy Cloud.

## Descargar el flujo de trabajo Texto a video

Descarga el JSON del flujo de trabajo.

### 

​

Referencia a video (R2V)

Usa imágenes, video o audio de referencia para guiar el aspecto, el movimiento y el ritmo y mantener resultados coherentes. ![Vista previa del flujo de trabajo Seedance 2.0 de referencia a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v-1.webp)

## Ejecuta la referencia a video en Cloud

Prueba el flujo de trabajo de referencia a video al instante en Comfy Cloud.

## Descargar el flujo de trabajo de referencia a video

Descarga el JSON del flujo de trabajo.

### 

​

Primer y último fotograma a video (FLF2V)

Proporciona un fotograma inicial y un fotograma final, y Seedance 2.0 genera el movimiento y las transiciones entre ellos. ![Vista previa del flujo de trabajo FLF2V de Seedance 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_flf2v-1.webp)

## Ejecutar FLF2V en Cloud

Prueba el flujo de trabajo de primer y último fotograma a video al instante en Comfy Cloud.

## Descargar el flujo de trabajo FLF2V

Descarga el JSON del flujo de trabajo.

### 

​

Referencia a video 4K (R2V 4K)

Genera video 4K a partir de imágenes de referencia con Seedance 2.0. El flujo de trabajo 4K sigue el mismo flujo de referencia que el R2V estándar: proporciona referencias de sujeto, vestuario o escena, y el modelo renderiza el clip final a resolución 4K para pantallas grandes y recortes en posproducción. ![Seedance 2.0 Reference-to-Video 4K workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v_4k-1.webp)

## Ejecutar Reference-to-Video 4K en Cloud

Prueba el flujo de trabajo Reference-to-Video 4K al instante en Comfy Cloud.

## Descargar el flujo de trabajo Reference-to-Video 4K

Descarga el JSON del flujo de trabajo.

### 

​

Convertir un storyboard en video

Convierte un storyboard en video en dos pasadas. Primero, genera el storyboard: Nano Banana 2 y GPT Image dibujan cada panel, un nodo Gemini escribe las descripciones de las tomas e ImageStitch ensambla la hoja de paneles. Después, introduce el storyboard finalizado en Seedance 2.0 para animarlo y convertirlo en un video con audio sincronizado. Ambos pasos están en un solo flujo de trabajo. Usa [Ejecución parcial](https://docs.comfy.org/es/interface/features/partial-execution) para ejecutar primero el grupo del storyboard, cambia la omisión al grupo de Seedance y luego ejecuta la pasada de animación. ![Vista previa del flujo de trabajo Storyboard to Video de Seedance 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance2_storyboard_to_video-1.webp)

## Ejecutar Storyboard to Video en Cloud

Prueba el flujo de trabajo Storyboard to Video al instante en Comfy Cloud.

## Descargar el flujo de trabajo Storyboard to Video

Descarga el JSON del flujo de trabajo.

## 

​

Seedance 2.0 Mini

Seedance 2.0 Mini es una variante más ligera y rápida de Seedance 2.0 para la generación de video del día a día. Conserva la misma sincronización de audio y video, la consistencia de personajes y el control de cámara que el modelo completo, con un menor costo por ejecución. Hoy, Mini se ofrece en dos flujos de trabajo: texto a video y referencia a video. Ambos están optimizados para iterar rápidamente en narrativas de varias tomas, contenido de marca y creación de cortometrajes.

Seedance 2.0 Mini se encuentra en la misma línea de precios `Seedance 2.0` que el modelo completo. Consulta las [entradas de precios de Seedance 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/pricing#bytedance) para conocer las tarifas actuales.

### 

​

Seedance 2.0 Mini de texto a video

Genera un video cinematográfico a partir de un prompt de texto con controles de cámara por IA y generación de personajes consistente entre escenas. ![Vista previa del flujo de trabajo de texto a video de Seedance 2.0 Mini](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_mini_t2v-1.webp)

## Ejecutar Seedance 2.0 Mini T2V en Cloud

Prueba al instante el flujo de trabajo de texto a video de Mini en Comfy Cloud.

## Descargar flujo de trabajo Seedance 2.0 Mini T2V

Descarga el JSON del flujo de trabajo o busca “Seedance 2.0 Mini” en la biblioteca de plantillas.

### 

​

Seedance 2.0 Mini de referencia a video

Genera un video cinematográfico a partir de dos imágenes de referencia (sujeto + escena) con movimiento de cámara impulsado por IA y generación de personajes consistente. ![Vista previa del flujo de trabajo de referencia a video de Seedance 2.0 Mini](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_mini_r2v-1.webp)

## Ejecutar Seedance 2.0 Mini R2V en Cloud

Prueba al instante el flujo de trabajo de referencia a video de Mini en Comfy Cloud.

## Descargar flujo de trabajo Seedance 2.0 Mini R2V

Descarga el JSON del flujo de trabajo o busca “Seedance 2.0 Mini” en la biblioteca de plantillas.

## Descargar referencia de sujeto

Obtén la imagen de referencia del sujeto de ejemplo.

## Descargar referencia de escena

Obtén la imagen de referencia de escena de ejemplo.

## 

​

Usar retratos de personas reales y retratos generados con IA en ComfyUI para Seedance 2.0

Seedance 2.0 **admite tanto** **retratos de personas reales** (imágenes de personas reales que usas como parecido o como referencia en cámara) **como** **retratos generados con IA** (sujetos ficticios creados por IA, que no representan a una persona real concreta). La ruta que elijas determina si necesitas las comprobaciones de **liveness** (prueba de vida) e identidad de ByteDance.

| **Retrato generado con IA**| **Retrato de persona real**  
---|---|---  
**A qué se refiere**|  El sujeto parece un personaje sintetizado por IA; no debe corresponder a una persona física identificable| Usas imágenes de retrato o de apariencia de una persona real  
**Verificación de identidad**|  Ninguna comprobación adicional| Una verificación de liveness de ByteDance, única (a través de **ByteDance Create Image/Video Asset**)  
**Flujo de trabajo**|  Cualquier flujo de trabajo estándar de Seedance 2.0 (T2V, R2V, FLF2V)| Flujo de trabajo Seedance 2.0 Real Human con el nodo **ByteDance Create Image/Video Asset**  
  
### 

​

Retrato generado con IA

![Referencia de retrato generado con IA en un flujo de trabajo de Seedance 2.0](https://mintcdn.com/dripart/wHjKXKWGGcGAFh8P/images/tutorial/api_nodes/bytedance/seedance2_0/virtual_portrait.png?fit=max&auto=format&n=wHjKXKWGGcGAFh8P&q=85&s=4addbe66cdef1f4025de8bd4f7c733b7) Usa el nodo Seedance 2.0 como cualquier otro generador: sube tu **imagen de personaje generada con IA** (o una referencia equivalente), conéctala y ejecuta. Después del envío, el servicio clasifica el recurso. **Si lo marca como contenido protegido relacionado con personas reales** , el nodo devuelve un error: en ese caso, cambia al flujo de trabajo de **retrato de persona real** que aparece más abajo. Una vez que el backend lo trata como un retrato de IA y la comprobación se supera, úsalo directamente como referencia sin pasos de verificación adicionales.

### 

​

Retrato de persona real

Usa el flujo de trabajo **Real Human** (requiere **ByteDance Create Image/Video Asset**): un parecido real necesita **una** verificación de liveness para disuadir la suplantación y el uso no autorizado del parecido de una persona, y para cumplir con los requisitos cambiantes de transparencia en IA. **Primer uso (verificación requerida)**

  1. Sube imágenes de retrato a través de **ByteDance Create Image/Video Asset**.
  2. Ejecuta el flujo de trabajo: se genera un enlace de verificación.
  3. Abre el enlace en tu teléfono o navegador y finaliza la verificación de liveness (normalmente en menos de ~30 segundos).
  4. Cuando la verificación se completa correctamente, recibes dos IDs: 
     * **Group ID** : la persona verificada; consérvalo cuando vuelvas a subir a la misma persona.
     * **Asset ID** : vinculado a este retrato; conéctalo para la generación de video y reutilízalo en distintas ejecuciones.

**Nueva foto o video de la misma persona (sin repetir la verificación de liveness)**

  1. Sube una foto o un video nuevos de esa persona.
  2. Ingresa el **Group ID** guardado en **ByteDance Create Image/Video Asset**.
  3. El sistema compara los nuevos datos faciales con el registro de verificación original; cuando coinciden, el nuevo recurso se activa automáticamente.



## Seedance 2.0 Real Human

Recorrido completo, flujo de verificación y plantillas del flujo de trabajo Real Human.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/seedance-2-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/seedance-2-0)

[Seedance 2.5 Draft](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5-draft)[Seedance 2 0 Real Human](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-0-real-human)
