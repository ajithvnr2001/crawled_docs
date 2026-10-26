---
url: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-virtual-try-on/
title: Kling Virtual Try-On en ComfyUI: viste a una persona con cualquier prenda - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.266815+00:00
---

# Kling Virtual Try-On en ComfyUI: viste a una persona con cualquier prenda - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-virtual-try-on/

## En esta página

Volver arriba

  * Flujos de trabajo disponibles
    * Kling Virtual Try-On
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Controles del nodo
  * Consejos
  * Empezar



Kling

# Kling Virtual Try-On en ComfyUI: viste a una persona con cualquier prenda

Copiar páginaCopiar página

Viste a una persona con cualquier prenda con el nodo asociado Kling Virtual Try-On en ComfyUI y conserva rostro y pose en un solo flujo de trabajo de API en la nube.

Copiar páginaCopiar página

**Kling Virtual Try-On** es un nodo asociado de ComfyUI que coloca una prenda de vestir sobre una persona en una foto. Conectas dos imágenes, una foto de una persona y una foto de la prenda, y el nodo devuelve a la misma persona vistiendo la prenda con el rostro y el cuerpo intactos. Acepta fotos de producto, flat lays, fotos de maniquí y fotos con modelo. En ComfyUI, el modelo se ejecuta mediante el nodo asociado **Kling Virtual Try-On**. Es un nodo de API en la nube: necesita una cuenta de Comfy con créditos y no descarga ningún modelo local. Ingresas dos imágenes y obtienes una imagen, junto con una comparación lado a lado. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer la tarifa por ejecución. El resultado coincide con el tamaño de la imagen de la persona, con un límite de 2048 píxeles en el lado más largo. Las imágenes más grandes se reducen antes de la ejecución.

## 

​

Flujos de trabajo disponibles

### 

​

Kling Virtual Try-On

Viste a una persona con una prenda y compara el resultado con la imagen original de la persona. La plantilla carga una foto de la persona y una foto de la prenda, ejecuta la prueba virtual a plena fidelidad de 2048px y muestra una vista `ImageCompare` de la persona de entrada y del resultado. ![Vista previa del flujo de trabajo de Kling Virtual Try-On](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_vto-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling: Virtual Try On” en la Biblioteca de plantillas

**Recursos de entrada**

## model_colorful_outfit.png

Carga la imagen en el nodo `LoadImage` de la persona que alimenta el nodo Kling Virtual Try-On

## green_floral_dress.png

Carga la imagen en el nodo `LoadImage` de la prenda que alimenta el nodo Kling Virtual Try-On

### 

​

Resumen del flujo de trabajo

La plantilla usa cinco nodos funcionales, además de un `MarkdownNote` que enumera los recursos de entrada:

  * **LoadImage** (persona): proporciona la foto de la persona
  * **LoadImage** (prenda): proporciona la prenda que se va a poner
  * **KlingTryOnNode** : el nodo principal que combina las dos imágenes
  * **SaveImageAdvanced** e **ImageCompare** : guardan el resultado y lo muestran junto a la imagen de la persona



### 

​

Pasos para ejecutar

  1. **Carga la foto de la persona** : sube o selecciona una foto de una sola persona en el nodo **LoadImage** de la persona
  2. **Carga la prenda** : sube o selecciona la ropa en el nodo **LoadImage** de la prenda
  3. **Configura`keep_pose`**: déjalo activado para mantener la pose, o desactívalo para que la pose se adapte y lograr una mejor presentación
  4. **Haz clic en Queue** o presiona `Ctrl+Enter` para generar



## 

​

Controles del nodo

Control| Valores| Efecto  
---|---|---  
`person_image`| una imagen| Foto de una sola persona, idealmente de frente o en vista de tres cuartos. Las imágenes con un lado de más de 2048px se reducen de escala primero  
`garment_image`| una imagen| La prenda que se va a poner: foto de producto, flat lay, maniquí o foto con modelo. Una foto con modelo puede arrastrar el resto de ese conjunto. Solo prendas de vestir; no se admiten zapatos, bolsos ni accesorios  
`keep_pose`| activado (predeterminado), desactivado| Avanzado. Desactívalo para que la pose pueda cambiar y presente mejor el conjunto  
`seed`| entero| Controla si el nodo se vuelve a ejecutar. Los resultados no son deterministas sin importar la semilla  
  
## 

​

Consejos

  * **Usa una foto de persona limpia y de frente**. El nodo funciona mejor cuando el sujeto mira a la cámara o está girado aproximadamente tres cuartos hacia ella.
  * **Solo ropa**. Los zapatos, bolsos y accesorios no son compatibles; conecta la prenda en sí.
  * **Una foto de la prenda sobre un modelo aporta más que la prenda en sí**. Cuando la imagen de la prenda es una toma sobre modelo, el resto del conjunto puede aparecer, lo que ayuda cuando quieres un conjunto completo.
  * **El resultado conserva el tamaño de la imagen de la persona**. La salida tiene la misma forma que la foto de la persona, con un límite de 2048 píxeles en el lado más largo.
  * **Espera variación entre ejecuciones**. La semilla no fija el resultado; las mismas configuraciones pueden producir una toma diferente.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Kling: Virtual Try On`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/kling/kling-virtual-try-on.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/kling/kling-virtual-try-on)

[Kling 3 0](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-3-0)[Kling Motion Control](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-motion-control)
