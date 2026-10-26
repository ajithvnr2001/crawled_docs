---
url: https://docs.comfy.org/es/installation/install_custom_node/
title: C\u00f3mo instalar nodos personalizados en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:04.037749+00:00
---

# Cómo instalar nodos personalizados en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/installation/install_custom_node/

## En esta página

Volver arriba

  * ¿Qué son los nodos personalizados?
  * Método 1: ComfyUI Manager (recomendado)
  * Método 2: Instalación manual usando Git
  * Método 3: Instalación por descarga de ZIP
  * Recursos para nodos personalizados



Instalar nodos personalizados

# Cómo instalar nodos personalizados en ComfyUI

Copiar páginaCopiar página

Instala nodos personalizados en ComfyUI con ComfyUI Manager, git clone o una descarga ZIP, e instala sus dependencias de Python de forma segura.

Copiar páginaCopiar página

## 

​

¿Qué son los nodos personalizados?

Los nodos personalizados son extensiones para ComfyUI que añaden nuevas funcionalidades como procesamiento avanzado de imágenes, ajuste fino de aprendizaje automático, ajustes de color y más. Estos nodos desarrollados por la comunidad pueden expandir significativamente las capacidades principales de ComfyUI.

Antes de instalar nodos personalizados, es importante revisarlos cuidadosamente. Dado que ComfyUI es un proyecto de código abierto, los complementos maliciosos podrían potencialmente explotar los nodos personalizados:

  1. Instala nodos personalizados solo de autores de confianza y de aquellos comúnmente usados por la comunidad
  2. Comprende la funcionalidad del complemento antes de instalarlo y evita fuentes desconocidas para garantizar la seguridad del sistema
  3. Evita instalar complementos oscuros o sospechosos: los complementos no verificados pueden plantear riesgos de seguridad que podrían comprometer el sistema



Todas las instalaciones de nodos personalizados requieren completar estos dos pasos:

  1. Clonar el código del nodo en el directorio `ComfyUI/custom_nodes`
  2. Instalar las dependencias de Python requeridas

Esta guía compara tres métodos de instalación. **ComfyUI Manager** está integrado en las versiones actuales de ComfyUI para la mayoría de las configuraciones. Comienza por la [descripción general de ComfyUI Manager](https://docs.comfy.org/es/manager/overview) para saber qué hace y cómo habilitarlo. Usa **Git clone** o **ZIP** cuando un nodo no esté en el registro o necesites una revisión específica.

Método| Ventajas| Desventajas  
---|---|---  
**ComfyUI Manager** (recomendado)| 1\. Instalación automatizada  
2\. Gestión de dependencias  
3\. Interfaz gráfica| No se pueden buscar directamente nodos que no estén registrados en el registro  
**Git Clone**|  Permite instalar nodos que no estén registrados en el registro| 1\. Requiere conocimientos de Git  
2\. Gestión manual de dependencias  
3\. Riesgos de instalación  
**Descarga de ZIP del repositorio**|  1\. No requiere Git  
2\. Control manual| 1\. Gestión manual de dependencias  
2\. Sin control de versiones  
3\. Riesgos de instalación  
  
Consejo: Antes de instalar nodos personalizados, revisa el archivo README del complemento para comprender los métodos de instalación, el uso y los requisitos, como modelos específicos, versiones de dependencias y soluciones a problemas comunes.

## 

​

Método 1: ComfyUI Manager (recomendado)

Necesitas tener ComfyUI Manager disponible en tu entorno antes de usar este método. Si falta o está deshabilitado, consulta la [descripción general de ComfyUI Manager](https://docs.comfy.org/es/manager/overview) y la [guía de instalación](https://docs.comfy.org/es/manager/install).

ComfyUI Manager ofrece dos versiones de interfaz para administrar nodos personalizados. Elige la guía que coincida con tu interfaz:

## Nueva interfaz (predeterminada para Desktop)

La nueva interfaz de administración de nodos, habilitada de forma predeterminada para usuarios de Desktop.

## Interfaz clásica

La interfaz clásica de Manager para instalar nodos personalizados.

## 

​

Método 2: Instalación manual usando Git

Adecuado para nodos nuevos que no se encuentran en ComfyUI Manager o cuando se necesitan versiones específicas. Requiere tener [Git](https://git-scm.com/) instalado en tu sistema.

1

Obtén la URL del repositorio

Haz clic en el botón “Code” en GitHub y copia el enlace HTTPS

2

Navega al directorio custom_nodes
    
    
    cd /path/to/ComfyUI/custom_nodes
    

3

Clona el repositorio
    
    
    git clone [repository URL]
    

4

Instala las dependencias

Las dependencias deben instalarse en tu entorno de ComfyUI. Ten cuidado de no mezclarlas con tu entorno del sistema para evitar contaminación

  * Windows Portable

  * Instalación manual




Para la versión portable de Windows, instala las dependencias en el entorno de Python Integrado
    
    
    python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\[node directory]\requirements.txt
    

Instala las dependencias en tu entorno de ComfyUI
    
    
    cd [node directory]
    pip install -r requirements.txt
    

5

Reinicia ComfyUI y actualiza el navegador

Reinicia ComfyUI y actualiza tu navegador. Revisa los registros de inicio para detectar errores de `import failed`

## 

​

Método 3: Instalación por descarga de ZIP

Adecuado para usuarios que no pueden usar Git o ComfyUI Manager

No recomendamos este método de instalación, ya que se pierde la capacidad de control de versiones

1

Haz clic en `Code` → `Download ZIP` en GitHub

Haz clic en `Code` → `Download ZIP` en la página de GitHub![Haz clic en Code → Download ZIP en GitHub](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=442d68eaf9a445b1d3d62f046e9f7b69)

2

Extrae el archivo ZIP

Extrae el archivo ZIP descargado

3

Copia la carpeta extraída al directorio `ComfyUI/custom_nodes/`

Copia la carpeta extraída al directorio `ComfyUI/custom_nodes/`

4

Instala las dependencias manualmente (igual que el paso 4 del método Git)

Reinicia ComfyUI y actualiza el navegador

5

Verifica que la instalación se haya realizado correctamente

Revisa ComfyUI Manager después de reiniciar para confirmar que el complemento se instaló correctamente y que no hay errores de `import failed`

## 

​

Recursos para nodos personalizados

En ComfyUI, además de la funcionalidad básica de extensión de nodos, los nodos personalizados también pueden incluir los siguientes recursos adicionales:

  * [Documentación de nodos](https://docs.comfy.org/es/custom-nodes/help_page): Esta función es compatible con todos los nodos personalizados y básicos. Puedes usarla para consultar la documentación de los nodos, entender el propósito y el uso de los nodos, y contribuir con documentación mediante PRs al autor.
  * [Plantillas de flujos de trabajo para nodos personalizados](https://docs.comfy.org/es/custom-nodes/workflow_templates): Plantillas de flujos de trabajo proporcionadas por los autores de nodos como flujos de trabajo de ejemplo, que se pueden explorar y cargar desde las plantillas de ComfyUI.
  * [Soporte multi-idioma](https://docs.comfy.org/es/custom-nodes/i18n)

Si eres desarrollador de nodos personalizados, puedes agregar estos recursos para que tu nodo personalizado sea más fácil de usar.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/install_custom_node.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/install_custom_node)

[Actualizar ComfyUI](https://docs.comfy.org/es/installation/update_comfyui)[Descripción general](https://docs.comfy.org/es/manager/overview)
