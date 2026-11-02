---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_toast/
title: API de Toast de ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.438409+00:00
---

# API de Toast de ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_toast/

## En esta página

Volver arriba

  * Uso básico
    * Toast simple
    * Tipos de toast
    * Helper de alerta
  * Referencia de la API
    * Mensaje de toast
    * Helper de alerta
    * Métodos adicionales



JavaScript (UI)

# API de Toast de ComfyUI

Copiar páginaCopiar página

Usa la API de Toast de ComfyUI para mostrar notificaciones no bloqueantes. Cubre los tipos de toast (éxito, advertencia, error), el helper alert y la referencia completa de la API.

Copiar páginaCopiar página

La API de Toast permite mostrar mensajes de notificación no bloqueantes a los usuarios. Resultan útiles para dar retroalimentación sin interrumpir el flujo de trabajo.

## 

​

Uso básico

### 

​

Toast simple
    
    
    // Mostrar un toast informativo simple
    app.extensionManager.toast.add({
      severity: "info",
      summary: "Information",
      detail: "Operation completed successfully",
      life: 3000
    });
    

### 

​

Tipos de toast
    
    
    // Toast de éxito
    app.extensionManager.toast.add({
      severity: "success",
      summary: "Success",
      detail: "Data saved successfully",
      life: 3000
    });
    
    // Toast de advertencia
    app.extensionManager.toast.add({
      severity: "warn",
      summary: "Warning",
      detail: "This action may cause problems",
      life: 5000
    });
    
    // Toast de error
    app.extensionManager.toast.add({
      severity: "error",
      summary: "Error",
      detail: "Failed to process request",
      life: 5000
    });
    

### 

​

Helper de alerta
    
    
    // Atajo para crear un toast de alerta
    app.extensionManager.toast.addAlert("This is an important message");
    

## 

​

Referencia de la API

### 

​

Mensaje de toast
    
    
    app.extensionManager.toast.add({
      severity?: "success" | "info" | "warn" | "error" | "secondary" | "contrast", // Nivel de severidad del mensaje (predeterminado: "info")
      summary?: string,         // Título corto del toast
      detail?: any,             // Contenido detallado del mensaje
      closable?: boolean,       // Indica si el usuario puede cerrar el toast (predeterminado: true)
      life?: number,            // Duración en milisegundos antes del cierre automático
      group?: string,           // Identificador de grupo para gestionar toasts relacionados
      styleClass?: any,         // Clase de estilo del mensaje
      contentStyleClass?: any   // Clase de estilo del contenido
    });
    

### 

​

Helper de alerta
    
    
    app.extensionManager.toast.addAlert(message: string);
    

### 

​

Métodos adicionales
    
    
    // Eliminar un toast específico
    app.extensionManager.toast.remove(toastMessage);
    
    // Eliminar todos los toasts
    app.extensionManager.toast.removeAll();
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_toast.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_toast)

[API de diálogos](https://docs.comfy.org/es/custom-nodes/js/javascript_dialog)[Insignias del panel Acerca de](https://docs.comfy.org/es/custom-nodes/js/javascript_about_panel_badges)
