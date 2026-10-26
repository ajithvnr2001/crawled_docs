---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bria/product-compositing/
title: Bria Product Holding y Virtual Try-On en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.110829+00:00
---

# Bria Product Holding y Virtual Try-On en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bria/product-compositing/

## En esta página

Volver arriba

  * Flujos de trabajo disponibles
    * Product Holding
    * Virtual Try-On
  * Controles del nodo
  * Consejos para el prompt
  * Empezar



Bria

# Bria Product Holding y Virtual Try-On en ComfyUI

Copiar páginaCopiar página

Pon un producto en las manos de una persona o vístela con una prenda usando los nodos asociados Bria Product Holding y Virtual Try-On de ComfyUI.

Copiar páginaCopiar página

**Bria Product Holding** toma una foto de una persona y de una a tres fotos de un producto, y luego renderiza a la persona sosteniendo ese producto. **Bria Virtual Try-On** hace lo mismo con prendas y accesorios: cada artículo reemplaza al artículo equivalente que la persona ya lleva puesto y se ajusta al cuerpo. Ambos nodos conservan el rostro, la pose y el fondo de la persona. La escena se vuelve a renderizar a aproximadamente un megapíxel, así que una foto tomada con el teléfono y una imagen del producto bastan para crear una imagen de estilo de vida o una vista de catálogo sin necesidad de una sesión de fotos. Son nodos API en la nube: necesitan una cuenta de Comfy con créditos, no descargan ningún archivo de modelo en local y devuelven una imagen que guardas con un nodo Save Image.

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

Product Holding

Coloca un producto en las manos de la persona que aparece en la foto. El nodo empieza con una conexión de producto; el botón más del nodo añade conexiones para hasta tres imágenes del mismo producto, como el propio producto, su embalaje, otro ángulo o un artículo complementario. ![Vista previa del flujo de trabajo Bria: Product Holding](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_product_holding-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Product Holding” en la Biblioteca de plantillas

**Materiales de entrada**

## bria_holding_person.png

Carga en la entrada `person_image`

## bria_holding_product.png

Carga en la entrada `product_images`

### 

​

Virtual Try-On

Viste a la persona con una prenda o un accesorio tomado de una foto de producto independiente. Cada artículo conectado reemplaza el artículo correspondiente que lleva puesto la persona, y dos prendas se combinan en un solo conjunto por capas, así que una prenda de la parte superior y una falda pueden ir en la misma ejecución en lugar de en dos. ![Vista previa del flujo de trabajo Bria: Virtual Try-On](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_virtual_try_on-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Virtual Try-On” en la Biblioteca de plantillas

**Materiales de entrada**

## bria_tryon_man.png

Carga en la entrada `person_image`

## bria_tryon_shirt.png

Carga en la entrada `garment_images`

Una prenda fotografiada en una percha o extendida sobre una superficie funciona igual de bien que una llevada por un modelo.

## 

​

Controles del nodo

Control| Valores| Se aplica a| Efecto  
---|---|---|---  
`person_image`| una imagen| ambos nodos| La foto sobre la que se coloca el producto o la prenda. Se conservan el rostro, la pose y el fondo  
`product_images`| 1 a 3 imágenes| Product Holding| Imágenes de un producto. Una entrada por lotes cuenta una vez por imagen y las áreas transparentes se tratan como blancas  
`garment_images`| 1 a 3 imágenes| Virtual Try-On| Prendas o accesorios que se llevan juntos, y cada uno reemplaza la prenda correspondiente  
`instruction`| texto, opcional| ambos nodos| Indicaciones adicionales a las de Bria, como `hold the bag in one hand` o `roll the sleeves up`  
`aspect_ratio`| `auto`, `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`| ambos nodos| `auto` mantiene el encuadre de la foto de la persona. Una relación fija devuelve de 0.6 a 1 megapíxel, por ejemplo 768x1024 en 3:4  
`seed`| entero, fijo de forma predeterminada| ambos nodos| Cámbiala para explorar variaciones de las mismas entradas  
`moderation`| `true`, `false`| ambos nodos| Activa el control de moderación de la salida visual  
  
## 

​

Consejos para el prompt

  * **Empieza con las manos vacías.** Una foto de una persona con las manos visibles y vacías le da al modelo espacio para colocar el producto. Un puño cerrado o una mano ocupada suele dar un resultado poco natural.
  * **Mantén las fotos del producto consistentes.** Funcionan mejor de una a tres imágenes del mismo producto: el frente, el empaque y un ángulo alternativo. Mezclar dos productos diferentes divide el render.
  * **Deja`instruction` vacío al principio.** La dirección integrada resuelve la mayoría de los casos. Añade una línea solo para una pose o un rostro específicos, como `hold the bag in one hand` o `face the label to the camera`.
  * **Usa una foto de una prenda, no un atuendo completo.** Una foto en percha o una vista cenital de la prenda individual es lo que se ajusta al cuerpo. Un look completo en una sola imagen suele sustituir más de lo previsto.
  * **Combina prendas en capas en una sola ejecución.** Dos prendas conectadas se convierten en un solo atuendo, lo que mantiene la iluminación y el ajuste uniformes entre las piezas.
  * **Mantén`aspect_ratio` en `auto` para una edición que coincida.** Conserva el encuadre de la foto original, así que el ANTES y el DESPUÉS quedan alineados.



## 

​

Empezar

  1. Actualizar ComfyUI a la última versión
  2. Ir a la Biblioteca de plantillas y buscar `Bria`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bria/product-compositing.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bria/product-compositing)

[Beeble Switchx](https://docs.comfy.org/es/tutorials/partner-nodes/beeble/beeble-switchx)[Edición de imágenes](https://docs.comfy.org/es/tutorials/partner-nodes/bria/image-editing)
