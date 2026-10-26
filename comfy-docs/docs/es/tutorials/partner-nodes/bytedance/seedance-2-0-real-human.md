---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-0-real-human/
title: Seedance 2.0 Real Human: generaci\u00f3n de video verificada de personas reales - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.917776+00:00
---

# Seedance 2.0 Real Human: generación de video verificada de personas reales - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-0-real-human/

## En esta página

Volver arriba

  * En qué destaca Seedance 2.0 Real Human
  * Guía en video
  * Cómo funciona la verificación en ComfyUI
    * Primera ejecución (verificación requerida)
    * Capturas del flujo de verificación
    * Subidas posteriores (sin verificación)
    * Saltar la verificación con un Group ID existente
  * Flujos de trabajo disponibles
    * Seedance 2.0 Real Human de referencia a video
    * Seedance 2.0 Real Human de primer y último fotograma a video



ByteDance

# Seedance 2.0 Real Human: generación de video verificada de personas reales

Copiar páginaCopiar página

Genera videos de personas reales en Seedance 2.0 con identidad consistente y audio sincronizado, tras una verificación de vitalidad única en ComfyUI.

Copiar páginaCopiar página

![Portada de Seedance 2.0 Real Human](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/cover.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=0301d3247b19cc498f8306ce0c0885eb) **Seedance 2.0 Real Human** está disponible directamente dentro de ComfyUI. Puedes subir un retrato mediante un flujo de trabajo de ComfyUI, completar una verificación única y luego generar videos con esa persona real, con una identidad consistente y expresiones faciales auténticas: todo sin salir de ComfyUI. Con el soporte de Real Human en ComfyUI, ya no estás limitado a personajes virtuales. La controlabilidad de Seedance 2.0 y su sincronización nativa de audio y video ahora se extienden a personas reales, manteniendo la identidad y la actuación a lo largo de todo el clip con los mismos flujos de trabajo basados en nodos que ya usas para otras generaciones de Seedance 2.0.

## 

​

En qué destaca Seedance 2.0 Real Human

  * **Personas reales, control cinematográfico** : Dirige movimientos de cámara, iluminación y cambios de escena mientras mantienes al sujeto creíble
  * **Consistencia de identidad** : Los rasgos faciales y la apariencia general se mantienen estables a través del movimiento, los movimientos de cámara y las transiciones
  * **Sincronización nativa de audio y video** : El video y el audio (diálogo, ambiente, música) se generan juntos, con un lip-sync y unas expresiones más confiables
  * **Dirección con múltiples referencias** : Combina texto con hasta **9 imágenes** , **3 videos** y **3 clips de audio** para fijar el aspecto, el movimiento y el ritmo



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

Guía en video

Mira el recorrido completo que cubre la verificación y ambos flujos de trabajo de Seedance 2.0 Real Human de principio a fin en ComfyUI.

## 

​

Cómo funciona la verificación en ComfyUI

La verificación es obligatoria antes de que cualquier persona real pueda aparecer en una generación de Seedance 2.0. Evita la suplantación de identidad y el uso no autorizado de la imagen de alguien, y la gestiona ByteDance, que cumple con las nuevas normativas de transparencia de la IA. Todo el flujo se controla desde ComfyUI mediante el nodo **ByteDance Create Image/Video Asset** : solo tienes que salir de ComfyUI brevemente para completar la comprobación de vitalidad en tu teléfono o navegador. ![Nodos ByteDance Create Image/Video Asset usados para generar el Group ID y el Asset ID](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/create_asset_nodes.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=b92f7e56d392659839f060c4cccef19a)

### 

​

Primera ejecución (verificación requerida)

  1. En ComfyUI, agrega el nodo **ByteDance Create Image/Video Asset** a tu flujo de trabajo y sube una imagen de retrato
  2. Ejecuta el flujo de trabajo: ComfyUI devuelve un enlace de verificación de ByteDance
  3. Abre el enlace en tu teléfono o navegador y completa la comprobación de vitalidad (menos de 1 minuto)
  4. Cuando la verificación se complete correctamente, vuelve a ComfyUI: la salida del nodo ahora contiene el asset verificado



#### 

​

Capturas del flujo de verificación

**Paso 1: Sube y ejecuta para iniciar la verificación** ![Sube tu retrato y ejecuta para iniciar la verificación de vitalidad](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_1.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=14a4e0268cb71d57374cbaeb4843c1a1) **Paso 2: Obtén el enlace de verificación** ![La ejecución del flujo de trabajo devuelve un enlace de verificación para abrir en el navegador](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_2.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=de061f6735e1212ec97e17e5c2535092) **Paso 3: Completa la comprobación de vitalidad en la página H5** ![Completa la autenticación de identidad en la página de verificación H5](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_3.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=1083f8f57730993cc20dc67dda035c91) **Paso 4: Vuelve a ComfyUI y guarda los IDs (sin créditos adicionales)** ![Tras la verificación, ComfyUI entrega el Asset ID y el Group ID para guardarlos y reutilizarlos](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_4.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=4fe58413a38ea8e0c3d9de961e8bfca4) Cuando la verificación de persona real se completa correctamente, el nodo expone dos IDs que puedes usar en los nodos de video de Seedance 2.0 posteriores:

  * **Group ID** : representa a la persona verificada. Guárdalo para poder reutilizar la misma identidad más tarde sin volver a verificar
  * **Asset ID** : representa esta imagen específica. Conéctalo a un nodo de generación de video de Seedance 2.0 para producir un video de la persona verificada; se puede reutilizar en varios flujos de trabajo



### 

​

Subidas posteriores (sin verificación)

  1. En ComfyUI, sube una foto o un video nuevos de la misma persona con el nodo **ByteDance Create Image/Video Asset**
  2. Introduce el **Group ID** guardado en el nodo
  3. Al ejecutar, ByteDance compara los rasgos faciales con la verificación original
  4. Si coinciden, el nuevo asset se activa automáticamente y se devuelve a ComfyUI, listo para usarse en la generación de video de Seedance 2.0



#### 

​

Saltar la verificación con un Group ID existente

Si ya completaste la verificación una vez, a menudo puedes saltar el paso de vitalidad en las nuevas subidas de la misma persona proporcionando el **Group ID** existente. Si ByteDance reconoce la nueva imagen como la misma persona, la verificación se omite. ![Reutiliza un Group ID existente para saltar la verificación de vitalidad cuando la persona coincide](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_5.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=641a21d96ed9f2b5b8a7aa6d1e88dd0f)

## 

​

Flujos de trabajo disponibles

En ComfyUI hay dos plantillas predefinidas de Seedance 2.0 Real Human. Ambas conectan el nodo **ByteDance Create Image/Video Asset** a un nodo de generación de video de Seedance 2.0 para que la verificación y la generación ocurran en una sola ejecución.

### 

​

Seedance 2.0 Real Human de referencia a video

Usa un retrato verificado (más imágenes, videos o audio de referencia adicionales opcionales) para generar un video de Seedance 2.0 con una identidad coherente de una persona real. ![Vista previa del flujo de trabajo Seedance 2.0 Real Human R2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v_real_human-1.webp)

## Ejecutar Seedance 2.0 Real Human R2V en Cloud

Prueba el flujo de trabajo Seedance 2.0 Real Human Reference-to-Video al instante en Comfy Cloud.

## Flujo de trabajo Seedance 2.0 Real Human R2V

Obtén el archivo del flujo de trabajo Seedance 2.0 Real Human Reference-to-Video.

### 

​

Seedance 2.0 Real Human de primer y último fotograma a video

Proporciona un fotograma inicial y uno final verificados para generar el video entre ambos y conservar la identidad de la persona real. ![Vista previa del flujo de trabajo Seedance 2.0 Real Human FLF2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_flf2v_real_human-1.webp)

## Ejecutar Seedance 2.0 Real Human FLF2V en Cloud

Prueba el flujo de trabajo Seedance 2.0 Real Human First-Last-Frame-to-Video al instante en Comfy Cloud.

## Flujo de trabajo Seedance 2.0 Real Human FLF2V

Obtén el archivo del flujo de trabajo Seedance 2.0 Real Human First-Last-Frame-to-Video.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/seedance-2-0-real-human.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/seedance-2-0-real-human)

[Seedance 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-0)[Vcube](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/vcube)
