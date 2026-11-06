---
url: https://docs.comfy.org/es/built-in-nodes/PatinaPBRMapsNode/
title: Mapas de material PBR Patina - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:54.154624+00:00
---

# Mapas de material PBR Patina - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PatinaPBRMapsNode/

3d

# Mapas de material PBR Patina - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Deriva un conjunto de mapas de material PBR a partir de una imagen de textura existente: color base, normal, rugosidad, metalicidad y altura.

Copiar páginaCopiar página

Deriva un conjunto de mapas de material PBR a partir de una imagen de textura existente: color base, normal, rugosidad, metalicidad y altura. Habilita solo los mapas que necesites, ya que cada mapa habilitado aumenta el costo. Úsalo para completar una textura que aún no tiene mapas de material, o para reconstruir un único mapa dañado.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`image`| La fotografía o renderizado del que se derivarán los mapas PBR.| IMAGE| Sí| -  
`basecolor`| Generar el mapa de color base (albedo). Predeterminado: True.| BOOLEAN| Sí| true  
false  
`normal`| Generar el mapa de normal. Predeterminado: True.| BOOLEAN| Sí| true  
false  
`roughness`| Generar el mapa de rugosidad. Predeterminado: False.| BOOLEAN| Sí| true  
false  
`metalness`| Generar el mapa de metalicidad. Predeterminado: False.| BOOLEAN| Sí| true  
false  
`height`| Generar el mapa de altura (desplazamiento). Predeterminado: False.| BOOLEAN| Sí| true  
false  
`seed`| Semilla para una eliminación de ruido reproducible. Predeterminado: 42.| INT| Sí| 0 a 2147483646  
`safety_checker`| Ejecutar la comprobación de seguridad de contenido del proveedor en la solicitud. Configuración avanzada. Predeterminado: False.| BOOLEAN| Sí| true  
false  
`auto_downscale`| Reducir automáticamente la escala de una imagen de entrada cuyo lado más largo supere los 2048 píxeles, el límite de entrada del modelo, preservando la relación de aspecto; las imágenes más pequeñas se dejan tal como están. Deshabilítalo para generar un error con imágenes sobredimensionadas en su lugar. Configuración avanzada. Predeterminado: True.| BOOLEAN| No| true  
false  
  
**Restricciones y comportamiento:**

  * Se debe habilitar al menos un mapa; de lo contrario, la ejecución falla.
  * La imagen de entrada está limitada a 2048 píxeles en su lado más largo; o dejas que `auto_downscale` la reduzca, o la ejecución falla con una imagen sobredimensionada.
  * Cada mapa deshabilitado sigue devolviendo una salida, pero como una imagen de marcador de posición de 1x1, así que conecta únicamente las salidas que realmente hayas generado.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`basecolor`| El mapa de color base (albedo) generado, o un marcador de posición de 1x1 cuando ese mapa está deshabilitado.| IMAGE  
`normal`| El mapa de normal generado, o un marcador de posición de 1x1 cuando ese mapa está deshabilitado.| IMAGE  
`roughness`| El mapa de rugosidad generado, o un marcador de posición de 1x1 cuando ese mapa está deshabilitado.| IMAGE  
`metalness`| El mapa de metalicidad generado, o un marcador de posición de 1x1 cuando ese mapa está deshabilitado.| IMAGE  
`height`| El mapa de altura (desplazamiento) generado, o un marcador de posición de 1x1 cuando ese mapa está deshabilitado.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaPBRMapsNode/es.md)

* * *

**Source fingerprint (SHA-256):** `813c5bb3336c5ca54a9ca9ee95e84e7f27791170650248d0169acee39c4b3ce1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PatinaPBRMapsNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PatinaPBRMapsNode)

[Material de pátina](https://docs.comfy.org/es/built-in-nodes/PatinaMaterialNode)[TencentHyNode](https://docs.comfy.org/es/built-in-nodes/TencentHyNode)
