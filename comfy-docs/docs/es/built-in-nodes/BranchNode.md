---
url: https://docs.comfy.org/es/built-in-nodes/BranchNode/
title: BranchNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:32.303293+00:00
---

# BranchNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BranchNode/

Lógica

# BranchNode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Branch selecciona una de varias entradas conectadas por nombre y la pasa a la salida.

Copiar páginaCopiar página

Branch selecciona una de varias entradas conectadas por nombre y la pasa a la salida. Funciona como un conmutador perezoso: solo se evalúa la rama seleccionada, por lo que las demás ramas pueden permanecer sin conectar o contener salidas que no desea calcular. Cada nueva conexión agrega otra entrada de rama, las entradas se pueden renombrar haciendo doble clic sobre ellas, y la rama activa se elige desde el selector `branch`.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`autogrow`| Las ramas conectadas. Cada conexión agrega una nueva entrada de rama, hasta 32; todas las ramas deben usar el mismo tipo de datos, que se convierte en el tipo de salida.| AUTOGROW| Sí| 1 a 32 ramas  
`branch`| Nombre de la rama que se pasa a la salida. Las opciones son los nombres de las entradas de rama conectadas, y una entrada se puede renombrar haciendo doble clic sobre ella.| STRING| Sí| Nombres de las ramas conectadas  
`branch_names`| Lista interna de los nombres de las ramas conectadas, mantenida sincronizada por el frontend. Asocia el nombre seleccionado con su rama y no está destinada a editarse manualmente.| ARRAY| Sí| -  
  
**Nota:** Solo se solicita la rama seleccionada, por lo que las demás ramas no se evalúan. El nodo genera un error cuando el nombre seleccionado no está conectado.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El valor de la rama seleccionada, pasado sin cambios.| MATCH_TYPE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BranchNode/es.md)

* * *

**Source fingerprint (SHA-256):** `2b4dca360c1b459a9f05eb54fedb7cdea6842fb0c606ee6f937ed00f715ee23a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BranchNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BranchNode)

[Interruptor](https://docs.comfy.org/es/built-in-nodes/ComfySwitchNode)[Finalizar bucle](https://docs.comfy.org/es/built-in-nodes/EndLoop)
