---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_dialog/
title: API de di\u00e1logos de ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:50.582084+00:00
---

# API de diálogos de ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_dialog/

## En esta página

Volver arriba

  * Uso básico
    * Diálogo de prompt
    * Diálogo de confirmación
  * Referencia de la API
    * Prompt
    * Confirmar



JavaScript (UI)

# API de diálogos de ComfyUI

Copiar páginaCopiar página

Usa la API de diálogos de ComfyUI para crear diálogos estandarizados de prompt y confirmación en escritorio y web, con ejemplos y referencia completa.

Copiar páginaCopiar página

La API de diálogos proporciona diálogos estandarizados que funcionan de forma consistente tanto en escritorio como en la web. Quienes desarrollan extensiones encontrarán más útiles los métodos prompt y confirm.

## 

​

Uso básico

### 

​

Diálogo de prompt
    
    
    // Mostrar un diálogo de prompt
    app.extensionManager.dialog.prompt({
      title: "User Input",
      message: "Please enter your name:",
      defaultValue: "User"
    }).then(result => {
      if (result !== null) {
        console.log(`Input: ${result}`);
      }
    });
    

### 

​

Diálogo de confirmación
    
    
    // Mostrar un diálogo de confirmación
    app.extensionManager.dialog.confirm({
      title: "Confirm Action",
      message: "Are you sure you want to continue?",
      type: "default"
    }).then(result => {
      console.log(result ? "User confirmed" : "User cancelled");
    });
    

## 

​

Referencia de la API

### 

​

Prompt
    
    
    app.extensionManager.dialog.prompt({
      title: string,             // Título del diálogo
      message: string,           // Mensaje o pregunta a mostrar
      defaultValue?: string      // Valor inicial del campo de entrada (opcional)
    }).then((result: string | null) => {
      // result es el texto introducido, o null si se cancela
    });
    

### 

​

Confirmar
    
    
    app.extensionManager.dialog.confirm({
      title: string,             // Título del diálogo
      message: string,           // Mensaje a mostrar
      type?: "default" | "overwrite" | "delete" | "dirtyClose" | "reinstall", // Tipo de diálogo (opcional)
      itemList?: string[],       // Lista de elementos a mostrar (opcional)
      hint?: string              // Texto de ayuda a mostrar (opcional)
    }).then((result: boolean | null) => {
      // result es true si se confirma, false si se deniega y null si se cancela
    });
    

Para conocer otros diálogos especializados disponibles en ComfyUI, puedes consultar el archivo `dialogService.ts` en el código fuente.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_dialog.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_dialog)

[API de configuraciones](https://docs.comfy.org/es/custom-nodes/js/javascript_settings)[Insignias del panel Acerca de](https://docs.comfy.org/es/custom-nodes/js/javascript_about_panel_badges)
