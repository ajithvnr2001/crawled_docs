---
url: https://docs.comfy.org/es/custom-nodes/js/primevue-removal-migration/
title: Migraci\u00f3n tras eliminar PrimeVue en extensiones del frontend - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:40.557019+00:00
---

# Migración tras eliminar PrimeVue en extensiones del frontend - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/primevue-removal-migration/

## En esta página

Volver arriba

  * Extensiones que renderizan componentes de PrimeVue
  * Extensiones que leen variables --p-*
  * Información sobre herramientas
  * Nombres de variables obsoletos



Migration Guides

# Migración tras eliminar PrimeVue en extensiones del frontend

Copiar páginaCopiar página

Reemplaza $primevue, componentes de PrimeVue, variables CSS —p-* y selectores de tooltip tras retirar PrimeVue del frontend de ComfyUI.

Copiar páginaCopiar página

El frontend de ComfyUI ya no instala PrimeVue. La aplicación host no llama a `app.use(PrimeVue)`, así que las extensiones pierden tres cosas en las que podrían haberse apoyado:

  * la propiedad global `$primevue` en la aplicación Vue host;
  * la hoja de estilos del tema de PrimeVue, por lo que los componentes de PrimeVue que una extensión renderiza dentro de la aplicación host se muestran sin estilos; y
  * todas las variables CSS globales `--p-*`, como `--p-primary-color`, `--p-surface-*`, `--p-text-color`, `--p-content-background` y `--p-form-field-border-color`.



## 

​

Extensiones que renderizan componentes de PrimeVue

No dependas de la instancia de PrimeVue de la aplicación anfitriona. Reemplaza los componentes de PrimeVue con tu propio marcado, o crea tu propia aplicación Vue para tu UI e instala PrimeVue y su tema en esa aplicación.

## 

​

Extensiones que leen variables `--p-*`

Reemplázalas con las variables de tema del sistema de diseño, que siguen el tema claro u oscuro activo y la paleta de colores activa:

Variable de PrimeVue| Variable de tema  
---|---  
`--p-primary-color`| `--primary`  
`--p-text-color`| `--foreground`  
`--p-text-muted-color`| `--muted-foreground`  
`--p-content-background`| `--background`  
`--p-surface-*` (paneles, áreas elevadas)| `--secondary`  
`--p-content-border-color`, `--p-form-field-border-color`| `--border`  
  
## 

​

Información sobre herramientas

La directiva global `v-tooltip` ya no existe, y la información sobre herramientas ya no renderiza el DOM de PrimeVue:

  * `.p-tooltip` y `.p-tooltip-text`
  * el atributo `data-pd-tooltip`
  * las propiedades de elemento `$_ptooltip*`

Ahora, una información sobre herramientas abierta renderiza un solo elemento con `data-slot="tooltip-content"`, colocado en un portal al final de `document.body`. Solo existe mientras la información sobre herramientas está abierta. Las extensiones que oculten la información sobre herramientas durante su propia UI deben apuntar a `[data-slot="tooltip-content"]` en lugar de `.p-tooltip`. Las variables CSS `--node-component-tooltip*` también se eliminaron de la hoja de estilos del sistema de diseño. En su lugar, usa las variables del tema: `--background`, `--foreground` y `--border`. Los nombres anteriores `--base-background`, `--base-foreground` y `--border-default` están obsoletos; consulta Nombres de variables obsoletos.

## 

​

Nombres de variables obsoletos

Versiones anteriores de estas notas apuntaban a nombres antiguos del sistema de diseño. Todavía se resuelven, pero están obsoletos y se eliminarán en una versión futura. Cambia ahora a la variable de tema:

Nombre obsoleto| Variable de tema  
---|---  
`--base-background`| `--background`  
`--base-foreground`| `--foreground`  
`--border-default`| `--border`  
`--primary-background`| `--primary`  
`--secondary-background`| `--secondary`  
`--component-node-background`| `--node`  
  
PrimeIcons todavía se carga, así que las clases de icono `pi pi-*` existentes siguen funcionando, pero se están retirando gradualmente. No agregues nuevos usos.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/primevue-removal-migration.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/primevue-removal-migration)

[Migración de geometría de nodos](https://docs.comfy.org/es/custom-nodes/js/node-geometry-migration)[Reemplazo de nodos](https://docs.comfy.org/es/custom-nodes/backend/node-replacement)
