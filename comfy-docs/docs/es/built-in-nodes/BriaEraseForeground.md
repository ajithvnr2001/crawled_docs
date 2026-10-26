---
url: https://docs.comfy.org/es/built-in-nodes/BriaEraseForeground/
title: Bria Borrar primer plano - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:32.581749+00:00
---

# Bria Borrar primer plano - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BriaEraseForeground/

Bria

# Bria Borrar primer plano - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo elimina el primer plano de una imagen con Bria y genera un nuevo fondo en su lugar.

Copiar páginaCopiar página

Este nodo elimina el primer plano de una imagen con Bria y genera un nuevo fondo en su lugar. Todo lo que Bria identifica como primer plano se elimina, no solo las personas, y los píxeles no modificados se conservan. El resultado se vuelve a renderizar a un tamaño estándar cercano a 1 megapíxel. Este es un nodo de API de pago que se ejecuta en el servicio de Bria, por lo que tus credenciales de Comfy API se usan en cada ejecución.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen cuyo primer plano se elimina y se reemplaza con un fondo generado. Solo se envían los canales de color; cualquier canal alfa se descarta antes de la carga.| IMAGE| Sí| -  
`moderación`| Configuración de moderación. Selecciona `"false"` para enviar la imagen sin indicadores de moderación, o `"true"` para mostrar las opciones de moderación de contenido que aparecen a continuación. Predeterminado: `"false"`.| DYNAMIC_COMBO| Sí| `"false"`  
`"true"`  
  
### 

​

Entradas de `"false"`

No hay entradas adicionales. La solicitud se envía sin indicadores de moderación de contenido.

### 

​

Entradas de `"true"`

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`visual_input_moderation`| Habilita la moderación de contenido en la imagen de entrada. Predeterminado: false.| BOOLEAN| Sí| true  
false  
`visual_output_moderation`| Habilita la moderación de contenido en la imagen de salida generada. Predeterminado: false.| BOOLEAN| Sí| true  
false  
  
### 

​

Notas

  * La salida se vuelve a renderizar a un tamaño estándar cercano a 1 megapíxel, por lo que la imagen devuelta puede diferir en dimensiones respecto a la entrada.
  * Este nodo es un nodo de API de pago; cada ejecución cuesta aproximadamente 0,0572 USD.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`IMAGE`| La imagen de entrada con su primer plano borrado y un fondo recién generado en su lugar.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseForeground/es.md)

* * *

**Source fingerprint (SHA-256):** `4d8c3c5eed97c648b1191ec41931c97caa17e98a8edd1c054ed63e80cc671b05`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BriaEraseForeground.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BriaEraseForeground)

[Bria Borrar por texto](https://docs.comfy.org/es/built-in-nodes/BriaEraseByText)[Borrador Bria](https://docs.comfy.org/es/built-in-nodes/BriaEraser)
