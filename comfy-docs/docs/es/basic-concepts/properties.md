---
url: https://docs.comfy.org/es/basic-concepts/properties/
title: Propiedades de ComfyUI: widgets, entradas y tipos de datos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:30.090614+00:00
---

# Propiedades de ComfyUI: widgets, entradas y tipos de datos - ComfyUI

> Source: https://docs.comfy.org/es/basic-concepts/properties/

## En esta página

Volver arriba

  * Los nodos son contenedores de propiedades
  * Tipos de datos



Conceptos básicos

# Propiedades de ComfyUI: widgets, entradas y tipos de datos

Copiar páginaCopiar página

Aprende cómo funcionan las propiedades de los nodos: widgets de control manual, ranuras de entrada y los tipos de datos que mantienen válido el grafo.

Copiar páginaCopiar página

## 

​

Los nodos son contenedores de propiedades

Los nodos suelen tener _**propiedades**_. También conocidas como _**parámetros**_ o _**atributos**_ , las propiedades de un nodo son variables que se pueden cambiar. Algunas propiedades se pueden ajustar manualmente por el usuario mediante un campo de entrada de datos llamado _**widget**_. Otras propiedades se pueden controlar automáticamente desde otros nodos conectados a la _**ranura de entrada**_ o puerto de la propiedad. Normalmente, una propiedad se puede convertir de widget a entrada y viceversa, lo que permite a los usuarios controlar los valores de las propiedades de forma manual o automática. Las propiedades pueden adoptar muchas formas y contener muchos tipos distintos de información. Por ejemplo, un nodo **Load Checkpoint** tiene una sola propiedad: la ruta del archivo checkpoint del modelo generativo. Un nodo **KSampler** tiene varias propiedades, como el número de **pasos** de muestreo, la escala **CFG** , **sampler_name** , etc. ![propiedades del nodo](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2121d646aef4f1386f1f09162312785b)

## 

​

Tipos de datos

La información puede presentarse de muchas formas distintas, llamadas _**tipos de datos**_. Por ejemplo, el texto alfanumérico se conoce como _**string**_ , un número entero es un _**integer**_ y un número con punto decimal se conoce como número de _**punto flotante**_ o _**float**_. Constantemente se añaden nuevos tipos de datos a ComfyUI. ComfyUI está escrito en el lenguaje de programación Python, que es muy permisivo con los tipos de datos. En cambio, el entorno de ComfyUI está muy _**fuertemente tipado**_. Esto significa que los distintos tipos de datos no se pueden mezclar. Por ejemplo, no podemos conectar una salida de imagen a una entrada de tipo entero. Esto es una gran ventaja para los usuarios, ya que les guía hacia una construcción correcta del flujo de trabajo y evita errores del programa.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/basic-concepts/properties.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/basic-concepts/properties)

[Nodos personalizados](https://docs.comfy.org/es/basic-concepts/custom-nodes)[Enlaces](https://docs.comfy.org/es/basic-concepts/links)
