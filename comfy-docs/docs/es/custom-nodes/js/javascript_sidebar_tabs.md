---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_sidebar_tabs/
title: Pesta\u00f1as de la barra lateral - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:51.204523+00:00
---

# Pestañas de la barra lateral - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_sidebar_tabs/

## En esta página

Volver arriba

  * Uso básico
  * Configuración de pestañas
  * Opciones de iconos
  * Ejemplo de pestaña con estado
  * Usar componentes de React
  * Actualizaciones dinámicas de contenido



JavaScript (UI)

# Pestañas de la barra lateral

Copiar páginaCopiar página

Domina la API de Comfy Extension y crea pestañas personalizadas en la barra lateral. Explora ejemplos de React y actualizaciones dinámicas. Lee la documentación.

Copiar páginaCopiar página

La API de Sidebar Tabs permite que las extensiones agreguen pestañas personalizadas a la barra lateral de la interfaz de ComfyUI. Esto es útil para agregar funciones que requieren visibilidad persistente y acceso rápido.

## 

​

Uso básico
    
    
    app.extensionManager.registerSidebarTab({
      id: "customSidebar",
      icon: "pi pi-compass",
      title: "Custom Tab",
      tooltip: "My Custom Sidebar Tab",
      type: "custom",
      render: (el) => {
        el.innerHTML = '<div>This is my custom sidebar content</div>';
      }
    });
    

## 

​

Configuración de pestañas

Cada pestaña requiere varias propiedades:
    
    
    {
      id: string,              // Identificador único para la pestaña
      icon: string,            // Clase de icono para el botón de la pestaña
      title: string,           // Texto del título de la pestaña
      tooltip?: string,        // Texto de tooltip al pasar el cursor (opcional)
      type: string,            // Tipo de pestaña (normalmente "custom")
      render: (element) => void // Función que rellena el contenido de la pestaña
    }
    

La función `render` recibe un elemento DOM donde debes insertar el contenido de tu pestaña.

## 

​

Opciones de iconos

Los iconos de las pestañas de la barra lateral pueden usar distintos conjuntos de iconos:

  * Iconos PrimeVue: `pi pi-[icon-name]` (por ejemplo, `pi pi-home`)
  * Iconos Material Design: `mdi mdi-[icon-name]` (por ejemplo, `mdi mdi-robot`)
  * Iconos Font Awesome: `fa-[style] fa-[icon-name]` (por ejemplo, `fa-solid fa-star`)

Asegúrate de que la biblioteca de iconos correspondiente esté cargada antes de usar estos iconos.

## 

​

Ejemplo de pestaña con estado

Puedes crear pestañas que mantengan su estado:
    
    
    app.extensionManager.registerSidebarTab({
      id: "statefulTab",
      icon: "pi pi-list",
      title: "Notes",
      type: "custom",
      render: (el) => {
        // Create elements
        const container = document.createElement('div');
        container.style.padding = '10px';
        
        const notepad = document.createElement('textarea');
        notepad.style.width = '100%';
        notepad.style.height = '200px';
        notepad.style.marginBottom = '10px';
        
        // Load saved content if available
        const savedContent = localStorage.getItem('comfyui-notes');
        if (savedContent) {
          notepad.value = savedContent;
        }
        
        // Auto-save content
        notepad.addEventListener('input', () => {
          localStorage.setItem('comfyui-notes', notepad.value);
        });
        
        // Assemble the UI
        container.appendChild(notepad);
        el.appendChild(container);
      }
    });
    

## 

​

Usar componentes de React

Puedes montar componentes de React en las pestañas de la barra lateral:
    
    
    // Importa las dependencias de React en tu extensión
    import React from "react";
    import ReactDOM from "react-dom/client";
    
    // Registra la pestaña de la barra lateral con contenido de React
    app.extensionManager.registerSidebarTab({
      id: "reactSidebar",
      icon: "mdi mdi-react",
      title: "React Tab",
      type: "custom",
      render: (el) => {
        const container = document.createElement("div");
        container.id = "react-sidebar-container";
        el.appendChild(container);
        
        // Define un componente de React simple
        function SidebarContent() {
          const [count, setCount] = React.useState(0);
          
          return (
            <div style={{ padding: "10px" }}>
              <h3>React Sidebar</h3>
              <p>Count: {count}</p>
              <button onClick={() => setCount(count + 1)}>
                Increment
              </button>
            </div>
          );
        }
        
        // Monta el componente de React
        ReactDOM.createRoot(container).render(
          <React.StrictMode>
            <SidebarContent />
          </React.StrictMode>
        );
      }
    });
    

Para ver un ejemplo real de una aplicación de React integrada como pestaña de la barra lateral, consulta el [proyecto ComfyUI-Copilot en GitHub](https://github.com/AIDC-AI/ComfyUI-Copilot).

## 

​

Actualizaciones dinámicas de contenido

Puedes actualizar el contenido de la barra lateral en respuesta a cambios en el gráfico:
    
    
    app.extensionManager.registerSidebarTab({
      id: "dynamicSidebar",
      icon: "pi pi-chart-line",
      title: "Stats",
      type: "custom",
      render: (el) => {
        const container = document.createElement('div');
        container.style.padding = '10px';
        el.appendChild(container);
        
        // Function to update stats
        function updateStats() {
          const stats = {
            nodes: app.graph._nodes.length,
            connections: Object.keys(app.graph.links).length
          };
          
          container.innerHTML = `
            <h3>Workflow Stats</h3>
            <ul>
              <li>Nodes: ${stats.nodes}</li>
              <li>Connections: ${stats.connections}</li>
            </ul>
          `;
        }
        
        // Initial update
        updateStats();
        
        // Listen for graph changes
        const api = app.api;
        api.addEventListener("graphChanged", updateStats);
        
        // Clean up listeners when tab is destroyed
        return () => {
          api.removeEventListener("graphChanged", updateStats);
        };
      }
    });
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_sidebar_tabs.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_sidebar_tabs)

[Insignias del panel Acerca de](https://docs.comfy.org/es/custom-nodes/js/javascript_about_panel_badges)[Selection Toolbox](https://docs.comfy.org/es/custom-nodes/js/javascript_selection_toolbox)
