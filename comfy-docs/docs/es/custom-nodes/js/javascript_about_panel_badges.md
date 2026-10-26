---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_about_panel_badges/
title: Insignias del panel Acerca de - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:50.513741+00:00
---

# Insignias del panel Acerca de - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_about_panel_badges/

## En esta página

Volver arriba

  * Uso básico
  * Configuración de las insignias
  * Opciones de iconos
  * Ejemplo



JavaScript (UI)

# Insignias del panel Acerca de

Copiar páginaCopiar página

Agrega insignias personalizadas con etiquetas, URL e iconos al panel Acerca de de ComfyUI mediante la API About Panel Badges.

Copiar páginaCopiar página

La API About Panel Badges permite que las extensiones agreguen insignias personalizadas a la página Acerca de de ComfyUI. Estas insignias pueden mostrar información sobre tu extensión y contener enlaces a la documentación, al código fuente u otros recursos.

## 

​

Uso básico
    
    
    app.registerExtension({
      name: "MyExtension",
      aboutPageBadges: [
        {
          label: "Documentation",
          url: "https://example.com/docs",
          icon: "pi pi-file"
        },
        {
          label: "GitHub",
          url: "https://github.com/username/repo",
          icon: "pi pi-github"
        }
      ]
    });
    

## 

​

Configuración de las insignias

Cada insignia requiere todas estas propiedades:
    
    
    {
      label: string,           // Texto que se muestra en la insignia
      url: string,             // URL que se abre al hacer clic en la insignia
      icon: string             // Clase de icono (por ejemplo, un icono de PrimeVue)
    }
    

## 

​

Opciones de iconos

Los iconos de las insignias usan el conjunto de iconos de PrimeVue. Estos son algunos de los iconos más usados:

  * Documentación: `pi pi-file` o `pi pi-book`
  * GitHub: `pi pi-github`
  * Enlace externo: `pi pi-external-link`
  * Información: `pi pi-info-circle`
  * Descargar: `pi pi-download`
  * Sitio web: `pi pi-globe`
  * Discord: `pi pi-discord`

Para ver la lista completa de iconos disponibles, consulta la [documentación de iconos de PrimeVue](https://primevue.org/icons/).

## 

​

Ejemplo
    
    
    app.registerExtension({
      name: "BadgeExample",
      aboutPageBadges: [
        {
          label: "Website",
          url: "https://example.com",
          icon: "pi pi-home"
        },
        {
          label: "Donate",
          url: "https://example.com/donate",
          icon: "pi pi-heart"
        },
        {
          label: "Documentation",
          url: "https://example.com/docs",
          icon: "pi pi-book"
        }
      ]
    });
    

Las insignias aparecen en el panel Acerca de del diálogo de Configuraciones, al que puedes acceder con el icono de engranaje en la esquina superior derecha de la interfaz de ComfyUI.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_about_panel_badges.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_about_panel_badges)

[API de diálogos](https://docs.comfy.org/es/custom-nodes/js/javascript_dialog)[Pestañas de la barra lateral](https://docs.comfy.org/es/custom-nodes/js/javascript_sidebar_tabs)
