---
url: https://docs.comfy.org/es/interface/nodes-2/
title: ComfyUI Nodes 2.0 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:30.012936+00:00
---

# ComfyUI Nodes 2.0 - ComfyUI

> Source: https://docs.comfy.org/es/interface/nodes-2/

## En esta página

Volver arriba

  * ¿Por qué este cambio?
  * Estado actual y problemas conocidos
  * Cómo probarlo
    * Activa Nodes 2.0
    * Qué probar
  * Cómo compartir comentarios
  * Volver a la versión anterior



Lienzo

# ComfyUI Nodes 2.0

Copiar páginaCopiar página

Nodes 2.0 traslada el renderizado de nodos de ComfyUI de LiteGraph Canvas a un sistema basado en Vue para iterar más rápido: qué cambió y cómo activarlo.

Copiar páginaCopiar página

Nodes 2.0 ya está disponible en Comfy Desktop y en las versiones portable y estable. Esta actualización traslada el sistema de nodos del renderizado con LiteGraph.js Canvas a una arquitectura basada en Vue, lo que permite iterar más rápido y tener interacciones más ricas.

## 

​

¿Por qué este cambio?

El sistema anterior de renderizado en lienzo se había convertido en un cuello de botella para el desarrollo. Incluso los cambios pequeños en la interfaz a menudo requerían modificaciones profundas y podían tardar días en implementarse. Esto reducía la capacidad de responder a la retroalimentación de la comunidad y dificultaba la personalización de nodos para los desarrolladores. El nuevo sistema basado en Vue permite:

  * **Desarrollo de funciones más rápido** \- Los cambios de interfaz se pueden implementar con mayor rapidez
  * **Interacciones más ricas** \- Widgets dinámicos, nodos expandibles y mejores componentes
  * **Una base más flexible** \- Mejor soporte para futuras herramientas y para la personalización



## 

​

Estado actual y problemas conocidos

Estamos trabajando activamente en mejoras y queremos ser transparentes sobre las limitaciones actuales:

Área| Estado  
---|---  
**Rendimiento**|  Todavía estamos optimizando para alcanzar el rendimiento del lienzo. Algunos escenarios pueden comportarse de forma distinta.  
**Compatibilidad**|  Algunos nodos personalizados pueden requerir actualizaciones para ser totalmente compatibles.  
**Casos límite**|  Con niveles de zoom extremos o en flujos de trabajo muy grandes, pueden aparecer problemas visuales menores.  
  
Estamos recopilando comentarios para priorizar las mejoras. El sistema de renderizado LiteGraph.js sigue disponible y puedes alternar entre ambos sistemas en cualquier momento.

## 

​

Cómo probarlo

### 

​

Activa Nodes 2.0

  1. Visita [cloud.comfy.org](https://cloud.comfy.org) o actualiza a la última versión de Comfy Desktop, portable o estable
  2. Haz clic en **Pruébalo** en el banner superior cuando inicies ComfyUI



### 

​

Qué probar

Usa Nodes 2.0 en tus flujos de trabajo diarios y comparte tus comentarios con nosotros:

  * **Interacciones básicas** \- Arrastrar, redimensionar, seleccionar
  * **Flujos de trabajo diarios** \- Ejecución, parámetros, nodos personalizados
  * **Rendimiento** \- Especialmente con flujos de trabajo complejos



## 

​

Cómo compartir comentarios

¿Encontraste problemas o tienes sugerencias para mejorar las interacciones?

  * **Centro de ayuda** \- [Centro de ayuda de ComfyUI](https://support.comfy.org)
  * **Problemas en GitHub** \- [Crea un issue en ComfyUI_frontend](https://github.com/Comfy-Org/ComfyUI_frontend/issues)



Incluir los pasos para reproducir el problema, capturas de pantalla e información del sistema es muy útil al reportar problemas.

## 

​

Volver a la versión anterior

Si encuentras problemas:

  1. Haz clic en el **logo de ComfyUI** para abrir el menú
  2. Desactiva **Nodes 2.0** para volver a la interfaz anterior

![Ubicación del interruptor de Nodes 2.0 en el menú de ComfyUI](https://mintcdn.com/dripart/qbw4z6UfFGJ-L3Cc/images/interface/nodes_2.0.jpg?fit=max&auto=format&n=qbw4z6UfFGJ-L3Cc&q=85&s=859a3a5b4faefd96adb24044ced72f72) Tus comentarios nos ayudan a priorizar las mejoras. ¡Activa Nodes 2.0 en las configuraciones y empieza a explorar el nuevo diseño de nodos!

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/nodes-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/nodes-2)

[Controles del lienzo](https://docs.comfy.org/es/interface/canvas-controls)[Panel inferior](https://docs.comfy.org/es/interface/bottom-panel)
