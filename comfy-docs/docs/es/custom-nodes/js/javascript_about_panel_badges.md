---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_about_panel_badges/
title: Insignias del panel Acerca de - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:50.861029+00:00
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
          icon: "icon-[lucide--file]"
        },
        {
          label: "GitHub",
          url: "https://github.com/username/repo",
          icon: "icon-[lucide--github]"
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
      icon: string             // Clase de icono (por ejemplo, "icon-[lucide--github]")
    }
    

## 

​

Opciones de iconos

Los iconos de las insignias usan clases de iconos de [Lucide](https://lucide.dev/icons/) con el formato `icon-[lucide--<icon-name>]`. Estos son algunos de los iconos más usados:

  * Documentación: `icon-[lucide--file]` o `icon-[lucide--book-open]`
  * GitHub: `icon-[lucide--github]`
  * Enlace externo: `icon-[lucide--external-link]`
  * Información: `icon-[lucide--info]`
  * Descargar: `icon-[lucide--download]`
  * Sitio web: `icon-[lucide--globe]`

El frontend genera estas clases al compilarse, así que solo están disponibles los iconos de Lucide que usa el propio frontend. Si un icono no se muestra, elige otro o define tu propia clase de icono en una hoja de estilos que cargue tu extensión. Las clases de PrimeIcons como `pi pi-file` todavía se muestran por ahora, pero se están retirando gradualmente. No las uses en código nuevo. Consulta la [migración por la eliminación de PrimeVue](https://docs.comfy.org/es/custom-nodes/js/primevue-removal-migration).

## 

​

Ejemplo
    
    
    app.registerExtension({
      name: "BadgeExample",
      aboutPageBadges: [
        {
          label: "Website",
          url: "https://example.com",
          icon: "icon-[lucide--globe]"
        },
        {
          label: "Donate",
          url: "https://example.com/donate",
          icon: "icon-[lucide--heart]"
        },
        {
          label: "Documentation",
          url: "https://example.com/docs",
          icon: "icon-[lucide--book-open]"
        }
      ]
    });
    

Las insignias aparecen en el panel Acerca de del diálogo de Configuraciones, al que puedes acceder con el icono de engranaje en la esquina superior derecha de la interfaz de ComfyUI.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_about_panel_badges.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_about_panel_badges)

[API de Toast](https://docs.comfy.org/es/custom-nodes/js/javascript_toast)[Pestañas del panel inferior](https://docs.comfy.org/es/custom-nodes/js/javascript_bottom_panel_tabs)
