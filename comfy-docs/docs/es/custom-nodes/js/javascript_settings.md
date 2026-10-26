---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_settings/
title: API de configuraciones - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:51.118268+00:00
---

# API de configuraciones - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_settings/

## En esta página

Volver arriba

  * Funcionamiento básico
    * Añadir una configuración
    * Leer una configuración
    * Reaccionar a los cambios
    * Escribir una configuración
    * Configuración adicional
  * Tipos
    * Booleano (Boolean)
    * Texto (Text)
    * Número (Number)
    * Slider
    * Combo
    * Color
    * Imagen (Image)
    * Oculto (Hidden)
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

Añadir una configuración
    
    
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

Los tipos de configuración se basan en componentes de [PrimeVue](https://primevue.org/). Las props descritas en la documentación de PrimeVue se pueden definir para las configuraciones de ComfyUI añadiéndolas en un campo `attrs`. Por ejemplo, esto añade botones de incremento y decremento a una entrada numérica:
    
    
    {
        id: "example.number",
        name: "Example number setting",
        type: "number",
        defaultValue: 0,
        attrs: {
            showButtons: true,
        },
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

## 

​

Tipos

### 

​

Booleano (Boolean)

Muestra un interruptor de activado y desactivado. Basado en el [componente ToggleSwitch de PrimeVue](https://primevue.org/toggleswitch/).
    
    
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

Texto (Text)

Es texto libre. Basado en el [componente InputText de PrimeVue](https://primevue.org/inputtext/).
    
    
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

Número (Number)

Sirve para introducir números. Para permitir decimales, establece el atributo `maxFractionDigits` en un número mayor que cero. Basado en el [componente InputNumber de PrimeVue](https://primevue.org/inputnumber/).
    
    
    {
        id: "example.number",
        name: "Example number setting",
        type: "number",
        defaultValue: 42,
        attrs: {
            showButtons: true,
            maxFractionDigits: 1,
        },
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Slider

Permite al usuario introducir un número directamente o mediante un slider. Basado en el [componente Slider de PrimeVue](https://primevue.org/slider/). No se admiten rangos.
    
    
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

Permite al usuario elegir de una lista desplegable de valores. Puedes proporcionar las opciones como una cadena simple o como un objeto con los campos `text` y `value`. Si solo proporcionas una cadena simple, se usará para ambos. Puedes permitir que el usuario introduzca texto libre con el atributo `editable: true`, o que busque con el atributo `filter: true`. Basado en el [componente Select de PrimeVue](https://primevue.org/select/). No se admiten grupos.
    
    
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
            editable: true,
            filter: true,
        },
        onChange: (newVal, oldVal) => {
            console.log(`Setting was changed from ${oldVal} to ${newVal}`);
        },
    }
    

### 

​

Color

Permite al usuario seleccionar un color en un selector de color o escribir una referencia hexadecimal. Ten en cuenta que el formato requiere seis dígitos hexadecimales completos; la forma abreviada de tres dígitos no funciona. Basado en el [componente ColorPicker de PrimeVue](https://primevue.org/colorpicker/).
    
    
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

Imagen (Image)

Permite al usuario subir una imagen. La configuración se guardará como una [URL de datos](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data). Basado en el [componente FileUpload de PrimeVue](https://primevue.org/fileupload/).
    
    
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

Oculto (Hidden)

Las configuraciones ocultas no se muestran en el panel de configuraciones, pero puedes leerlas y escribirlas desde tu código.
    
    
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

Puedes especificar la categorización de tu configuración de forma independiente del `id`. Esto significa que puedes cambiar la categorización y los nombres sin cambiar el `id` y sin perder los valores que los usuarios ya hayan establecido.
    
    
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

Puedes añadir ayuda contextual adicional con el campo `tooltip`. Esto añade un pequeño icono ℹ︎ después del nombre del campo que mostrará el texto de ayuda cuando el usuario pase el cursor por encima.
    
    
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
