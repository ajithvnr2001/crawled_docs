---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_settings/
title: API de configuraciones - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:51.152341+00:00
---

# API de configuraciones - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_settings/

## En esta página

Volver arriba

  * Funcionamiento básico
    * Agregar una configuración
    * Leer una configuración
    * Reaccionar a los cambios
    * Escribir una configuración
    * Configuración adicional
  * Tipos
    * Booleano
    * Texto
    * Número
    * Control deslizante
    * Combo
    * Color
    * Imagen
    * Oculto
  * Otros
    * Categorías
    * Tooltips



JavaScript (UI)

# API de configuraciones

Copiar páginaCopiar página

Agrega, lee, escribe y reacciona a las configuraciones de extensiones de ComfyUI con app.registerExtension: tipos booleano, texto, número, slider, combo, color e imagen.

Copiar páginaCopiar página

Puedes proporcionar a ComfyUI un objeto de configuraciones que aparecerá cuando el usuario abra el panel de configuraciones de ComfyUI.

## 

​

Funcionamiento básico

### 

​

Agregar una configuración
    
    
    import { app } from "../../scripts/app.js";
    
    app.registerExtension({
        name: "My Extension",
        settings: [
            {
                id: "example.boolean",
                name: "Example boolean setting",
                type: "boolean",
                defaultValue: false,
            },
        ],
    });
    

El `id` debe ser único en todas las extensiones y se usará para obtener los valores. Si no proporcionas una categoría, el `id` se dividirá por `.` para determinar dónde aparece en el panel de configuraciones.

  * Si tu `id` no contiene ningún `.`, aparecerá en la categoría “Other” y tu `id` se usará como encabezado de sección.
  * Si tu `id` contiene al menos un `.`, la parte más a la izquierda se usará como categoría de la configuración y la segunda parte se usará como encabezado de sección. Las demás partes se ignoran.



### 

​

Leer una configuración
    
    
    import { app } from "../../scripts/app.js";
    
    if (app.extensionManager.setting.get('example.boolean')) {
        console.log("Setting is enabled.");
    } else {
        console.log("Setting is disabled.");
    }
    

### 

​

Reaccionar a los cambios

El controlador de eventos `onChange()` se llamará en cuanto el usuario cambie la configuración en el panel de configuraciones. También se llamará cuando se registre la extensión, en cada carga de página.
    
    
    {
        id: "example.boolean",
        name: "Example boolean setting",
        type: "boolean",
        defaultValue: false,
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Escribir una configuración
    
    
    import { app } from "../../scripts/app.js";
    
    try {
        await app.extensionManager.setting.set("example.boolean", true);
    } catch (error) {
        console.error(`Error changing setting: ${error}`);
    }
    

### 

​

Configuración adicional

Cada tipo de configuración muestra un componente de formulario del frontend de ComfyUI. Puedes pasar props adicionales a ese componente en un campo `attrs`. Las props que admite cada tipo se indican en Tipos. Por ejemplo, esto limita una entrada de número a un rango y un paso:
    
    
    {
        id: "example.number",
        name: "Example number setting",
        type: "number",
        defaultValue: 0,
        attrs: {
            min: 0,
            max: 100,
            step: 5,
        },
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

Si tu extensión pasaba props de PrimeVue como `showButtons`, `maxFractionDigits`, `editable` o `filter`, consulta la [migración por la eliminación de PrimeVue](https://docs.comfy.org/es/custom-nodes/js/primevue-removal-migration). El panel de configuración ya no usa componentes de PrimeVue, así que esas props no tienen efecto.

## 

​

Tipos

### 

​

Booleano

Muestra un interruptor de activado/desactivado.
    
    
    {
        id: "example.boolean",
        name: "Example boolean setting",
        type: "boolean",
        defaultValue: false,
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Texto

Es texto de forma libre.
    
    
    {
        id: "example.text",
        name: "Example text setting",
        type: "text",
        defaultValue: "Foo",
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Número

Sirve para introducir números. La entrada siempre muestra botones de incremento y decremento. Los `attrs` admitidos son `min`, `max`, `step` y `formatOptions`. `formatOptions` acepta [`Intl.NumberFormatOptions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#options), así que `maximumFractionDigits` controla cuántos decimales se muestran.
    
    
    {
        id: "example.number",
        name: "Example number setting",
        type: "number",
        defaultValue: 42,
        attrs: {
            step: 0.1,
            formatOptions: { maximumFractionDigits: 1 },
        },
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Control deslizante

Permite al usuario introducir un número directamente o mediante un control deslizante. Los `attrs` admitidos son `min`, `max` y `step`. No se admiten rangos.
    
    
    {
        id: "example.slider",
        name: "Example slider setting",
        type: "slider",
        attrs: {
            min: -10,
            max: 10,
            step: 0.5,
        },
        defaultValue: 0,
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Combo

Permite al usuario elegir de una lista desplegable de valores. Puedes proporcionar las opciones como una cadena simple o como un objeto con los campos `text` y `value`. Si solo proporcionas una cadena simple, se usará tanto como texto como valor. Puedes permitir que el usuario busque en la lista aportando el atributo `searchable: true`. No se admiten grupos ni la entrada de texto libre.
    
    
    {
        id: "example.combo",
        name: "Example combo setting",
        type: "combo",
        defaultValue: "first",
        options: [
            { text: "My first option", value: "first" },
            "My second option",
        ],
        attrs: {
            searchable: true,
        },
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Color

Permite al usuario seleccionar un color desde un selector de color o escribir una referencia hexadecimal. Ten en cuenta que el formato requiere seis dígitos hexadecimales completos (u ocho, con alfa). La forma abreviada de tres dígitos no funciona.
    
    
    {
        id: "example.color",
        name: "Example color setting",
        type: "color",
        defaultValue: "ff0000",
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Imagen

Permite al usuario subir una imagen. La configuración se guarda como [data URL](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data).
    
    
    {
        id: "example.image",
        name: "Example image setting",
        type: "image",
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Oculto

Las configuraciones ocultas no se muestran en el panel de configuraciones, pero puedes leerlas y escribir en ellas desde tu código.
    
    
    {
        id: "example.hidden",
        name: "Example hidden setting",
        type: "hidden",
    }
    

## 

​

Otros

### 

​

Categorías

Puedes especificar la categorización de tu ajuste de forma independiente al `id`. Esto significa que puedes cambiar la categorización y el nombre sin cambiar el `id` y perder los valores que los usuarios ya hayan establecido.
    
    
    {
        id: "example.boolean",
        name: "Example boolean setting",
        type: "boolean",
        defaultValue: false,
        category: ["Category name", "Section heading", "Setting label"],
    }
    

### 

​

Tooltips

Puedes añadir ayuda contextual adicional con el campo `tooltip`. Esto añade un pequeño icono ℹ︎ después del nombre del campo que mostrará el texto de ayuda cuando el usuario pase el cursor sobre él.
    
    
    {
        id: "example.boolean",
        name: "Example boolean setting",
        type: "boolean",
        defaultValue: false,
        tooltip: "This is some helpful information",
    }
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_settings.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_settings)

[Objetos de Comfy](https://docs.comfy.org/es/custom-nodes/js/javascript_objects_and_hijacking)[API de diálogos](https://docs.comfy.org/es/custom-nodes/js/javascript_dialog)
