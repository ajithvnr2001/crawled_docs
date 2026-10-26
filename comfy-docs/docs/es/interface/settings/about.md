---
url: https://docs.comfy.org/es/interface/settings/about/
title: P\u00e1gina Acerca de ComfyUI: insignias de versi\u00f3n e informaci\u00f3n del sistema - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:30.336436+00:00
---

# Página Acerca de ComfyUI: insignias de versión e información del sistema - ComfyUI

> Source: https://docs.comfy.org/es/interface/settings/about/

## En esta página

Volver arriba

  * Insignias de información de versión
  * Insignias de nodos personalizados
  * Información del sistema
  * Guía para desarrolladores de extensiones



Configuraciones de ComfyUI

# Página Acerca de ComfyUI: insignias de versión e información del sistema

Copiar páginaCopiar página

Dónde ver las insignias de versión, de nodos personalizados y la información del sistema en ComfyUI, y cómo las extensiones añaden insignias.

Copiar páginaCopiar página

Las configuraciones descritas en esta página se encuentran en el **menú de configuraciones dentro de la aplicación de ComfyUI**. Puedes abrirlo navegando a **Configuraciones** (icono de engranaje) o usando el atajo de teclado `Ctrl + ,`, y luego seleccionar la categoría correspondiente para ver y configurar estas opciones.

La página Acerca de es un panel informativo dentro del sistema de ajustes de ComfyUI, que muestra la información de versión de la aplicación, enlaces relacionados y estadísticas del sistema. Estos datos nos resultan útiles cuando envías comentarios o informas de un problema. ![acerca de](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/setting/settings-about.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=36423b9d7d78b257e2d34d37b91b8a22)

### 

​

Insignias de información de versión

La página Acerca de muestra la siguiente información de versión principal:

  * **Versión de ComfyUI** : muestra el número de versión del backend de ComfyUI, con enlace al repositorio oficial de GitHub
  * **Versión de ComfyUI_frontend** : muestra el número de versión de la interfaz (frontend), con enlace al repositorio del frontend en GitHub
  * **Comunidad de Discord** : ofrece un enlace al servidor de Discord de ComfyOrg
  * **Sitio web oficial** : enlaza al sitio web oficial de ComfyOrg



Como la información de versión que aparece aquí corresponde sobre todo a versiones estables, si usas la versión nightly no verás el hash del commit correspondiente. Si usas la versión nightly, puedes ejecutar el comando `git log` en el directorio principal de ComfyUI para consultar el hash del commit y otra información. Otro problema habitual es que distintos paquetes de dependencias fallen y se reviertan durante las actualizaciones.

### 

​

Insignias de nodos personalizados

Si tienes nodos personalizados instalados, la página Acerca de también mostrará insignias adicionales que aportan esos nodos. Cada nodo personalizado registra sus insignias mediante la propiedad `aboutPageBadges`.

### 

​

Información del sistema

En la parte inferior de la página se muestran estadísticas detalladas del sistema, entre ellas:

  * Información de la configuración de hardware
  * Información del entorno de software
  * Datos de rendimiento del sistema



## 

​

Guía para desarrolladores de extensiones

Los desarrolladores de extensiones pueden agregar insignias personalizadas a la página Acerca de añadiendo la propiedad `aboutPageBadges` a la configuración de su extensión:
    
    
    app.registerExtension({
      name: 'MyExtension',
      aboutPageBadges: [
        {
          label: 'My Extension v1.0.0',
          url: 'https://github.com/myuser/myextension',
          icon: 'pi pi-github'
        }
      ]
    })
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/settings/about.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/settings/about)

[Extensión](https://docs.comfy.org/es/interface/settings/extension)[Usuario](https://docs.comfy.org/es/interface/user)
