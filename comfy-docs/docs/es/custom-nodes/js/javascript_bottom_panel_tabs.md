---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_bottom_panel_tabs/
title: Pesta\u00f1as del panel inferior - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.170022+00:00
---

# Pestañas del panel inferior - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_bottom_panel_tabs/

## En esta página

Volver arriba

  * Uso básico
  * Configuración de pestañas
  * Elementos interactivos
  * Uso de componentes de React
  * Registro independiente



JavaScript (UI)

# Pestañas del panel inferior

Copiar páginaCopiar página

Añade pestañas personalizadas al panel inferior de ComfyUI con la API de pestañas del panel inferior, incluidos elementos interactivos, componentes de React y registro independiente.

Copiar páginaCopiar página

La API de pestañas del panel inferior permite a las extensiones añadir pestañas personalizadas al panel inferior de la interfaz de ComfyUI. Resulta útil para añadir funciones como registros, herramientas de depuración o paneles personalizados.

## 

​

Uso básico
    
    
    app.registerExtension({
      name: "MyExtension",
      bottomPanelTabs: [
        {
          id: "customTab",
          title: "Custom Tab",
          type: "custom",
          render: (el) => {
            el.innerHTML = '<div>This is my custom tab content</div>';
          }
        }
      ]
    });
    

## 

​

Configuración de pestañas

Cada pestaña requiere un `id`, un `title` y un `type`, además de una función de renderizado:
    
    
    {
      id: string,              // Identificador único de la pestaña
      title: string,           // Título que se muestra en la pestaña
      type: string,            // Tipo de pestaña (normalmente "custom")
      icon?: string,           // Clase del icono (opcional)
      render: (element) => void // Función que rellena el contenido de la pestaña
    }
    

La función `render` recibe un elemento DOM en el que debes insertar el contenido de tu pestaña.

## 

​

Elementos interactivos

Puedes añadir elementos interactivos como botones:
    
    
    app.registerExtension({
      name: "InteractiveTabExample",
      bottomPanelTabs: [
        {
          id: "controlsTab",
          title: "Controls",
          type: "custom",
          render: (el) => {
            el.innerHTML = `
              <div style="padding: 10px;">
                <button id="runBtn">Run Workflow</button>
              </div>
            `;
            
            // Añadir detectores de eventos
            el.querySelector('#runBtn').addEventListener('click', () => {
              app.queuePrompt();
            });
          }
        }
      ]
    });
    

## 

​

Uso de componentes de React

Puedes montar componentes de React en las pestañas del panel inferior:
    
    
    // Importar las dependencias de React en tu extensión
    import React from "react";
    import ReactDOM from "react-dom/client";
    
    // Componente de React simple
    function TabContent() {
      const [count, setCount] = React.useState(0);
      
      return (
        <div style={{ padding: "10px" }}>
          <h3>React Component</h3>
          <p>Count: {count}</p>
          <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
      );
    }
    
    // Registrar la extensión con contenido de React
    app.registerExtension({
      name: "ReactTabExample",
      bottomPanelTabs: [
        {
          id: "reactTab",
          title: "React Tab",
          type: "custom",
          render: (el) => {
            const container = document.createElement("div");
            container.id = "react-tab-container";
            el.appendChild(container);
            
            // Montar el componente de React
            ReactDOM.createRoot(container).render(
              <React.StrictMode>
                <TabContent />
              </React.StrictMode>
            );
          }
        }
      ]
    });
    

## 

​

Registro independiente

También puedes registrar pestañas fuera de `registerExtension`:
    
    
    app.extensionManager.registerBottomPanelTab({
      id: "standAloneTab",
      title: "Stand-Alone Tab",
      type: "custom",
      render: (el) => {
        el.innerHTML = '<div>This tab was registered independently</div>';
      }
    });
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_bottom_panel_tabs.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_bottom_panel_tabs)

[Insignias del panel Acerca de](https://docs.comfy.org/es/custom-nodes/js/javascript_about_panel_badges)[Pestañas de la barra lateral](https://docs.comfy.org/es/custom-nodes/js/javascript_sidebar_tabs)
