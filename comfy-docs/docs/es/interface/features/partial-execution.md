---
url: https://docs.comfy.org/es/interface/features/partial-execution/
title: Ejecuci\u00f3n parcial: ejecuta solo parte de tu flujo de trabajo en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:29.233439+00:00
---

# Ejecución parcial: ejecuta solo parte de tu flujo de trabajo en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/interface/features/partial-execution/

## En esta página

Volver arriba

  * ¿Qué es la ejecución parcial?
  * ¿Cómo usar la función de ejecución parcial?
  * Problemas comunes



Componentes de funciones

# Ejecución parcial: ejecuta solo parte de tu flujo de trabajo en ComfyUI

Copiar páginaCopiar página

Ejecuta solo la rama que necesitas: selecciona un nodo de salida y pulsa el triángulo azul del cuadro de herramientas para ejecutar esa ruta.

Copiar páginaCopiar página

![Función de ejecución parcial](https://mintcdn.com/dripart/TKAcLTByYOWti7x2/images/interface/features/partial-execution/partial-execution-icon.jpg?fit=max&auto=format&n=TKAcLTByYOWti7x2&q=85&s=db3858609dd08ed7e0eb044f4cc52506) La función de ejecución parcial se encuentra en el cuadro de herramientas de selección de nodos de ComfyUI. Te permite ejecutar solo una parte de tu flujo de trabajo en lugar de ejecutar todos los nodos. Esta función solo está disponible cuando el nodo seleccionado es un nodo de salida y, cuando está disponible, aparece como un icono de triángulo azul.

## 

​

¿Qué es la ejecución parcial?

La ejecución parcial, como su nombre indica, te permite ejecutar solo una parte de tu flujo de trabajo en lugar de ejecutar todos los nodos del flujo de trabajo. ![Ejecución parcial](https://mintcdn.com/dripart/TKAcLTByYOWti7x2/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?fit=max&auto=format&n=TKAcLTByYOWti7x2&q=85&s=ff5bc603635a642425b52527bce9b2a0) El diagrama anterior compara la ejecución parcial con la ejecución de todo el flujo de trabajo:

  1. Ejecución parcial (izquierda): solo ejecuta la rama del flujo de trabajo desde el nodo inicial hasta el nodo de salida.
  2. Ejecutar flujo de trabajo (derecha): ejecuta todos los nodos del flujo de trabajo.

Esta función te permite ejecutar de forma flexible partes específicas de tu flujo de trabajo, en lugar de ejecutar todo el flujo de trabajo cada vez.

## 

​

¿Cómo usar la función de ejecución parcial?

![Requisitos de la ejecución parcial](https://mintcdn.com/dripart/TKAcLTByYOWti7x2/images/interface/features/partial-execution/requirement.jpg?fit=max&auto=format&n=TKAcLTByYOWti7x2&q=85&s=3f92c45fa7c03f44af25c6b876e83069) Para usar la función de ejecución parcial, el nodo seleccionado actualmente debe ser un nodo de salida, como los nodos de vista previa o de guardado. Cuando el nodo correspondiente cumple con los criterios, después de seleccionarlo, el botón del cuadro de herramientas se mostrará como un icono de triángulo azul. Haz clic en este icono para ejecutar el flujo de trabajo parcial.

## 

​

Problemas comunes

Si la ejecución parcial parece ejecutar todo el gráfico, revisa primero la versión del frontend:

¿Por qué se ejecutan todos los nodos cuando uso esta función?

Asegúrate de que la versión del frontend de tu ComfyUI sea posterior a v1.23.4, o posiblemente se requiera v1.24.x. El error correspondiente se corrigió alrededor de la versión 1.24.x. Actualiza ComfyUI a la última versión para que el frontend cumpla con el requisito.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/features/partial-execution.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/features/partial-execution)

[Subgrafo](https://docs.comfy.org/es/interface/features/subgraph)[Documentación de nodos](https://docs.comfy.org/es/interface/features/node-docs)
