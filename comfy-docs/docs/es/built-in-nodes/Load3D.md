---
url: https://docs.comfy.org/es/built-in-nodes/Load3D/
title: Cargar 3D y animaci\u00f3n - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:04.551562+00:00
---

# Cargar 3D y animación - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Load3D/

3D

# Cargar 3D y animación - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Aquí tienes la traducción al español de la documentación del nodo Load3D, siguiendo todas las reglas establecidas:

Copiar páginaCopiar página

Aquí tienes la traducción al español de la documentación del nodo Load3D, siguiendo todas las reglas establecidas: El nodo Load3D es un nodo principal para cargar y procesar archivos de modelos 3D. Al cargar el nodo, este recupera automáticamente los recursos 3D disponibles de `ComfyUI/input/3d/`. También puedes subir archivos 3D compatibles para previsualizarlos usando la función de carga. **Formatos compatibles** Actualmente, este nodo admite múltiples formatos de archivo 3D, incluyendo `.gltf`, `.glb`, `.obj`, `.fbx` y `.stl`. **Preferencias de nodos 3D** Algunas preferencias relacionadas con los nodos 3D se pueden configurar en el menú de ajustes de ComfyUI. Consulta la siguiente documentación para las configuraciones correspondientes: [Menú de Ajustes](https://docs.comfy.org/interface/settings/3d) Además de las salidas regulares del nodo, Load3D tiene muchas configuraciones relacionadas con la vista 3D en el menú del lienzo.

## 

​

Entradas

Nombre del Parámetro| Descripción| Tipo| Por Defecto| Rango  
---|---|---|---|---  
model_file| Ruta del archivo de modelo 3D, admite carga, por defecto lee archivos de modelo de `ComfyUI/input/3d/`| Selección de Archivo| -| Formatos compatibles  
width| Ancho de renderizado del lienzo| INT| 1024| 1-4096  
height| Alto de renderizado del lienzo| INT| 1024| 1-4096  
  
## 

​

Salidas

Nombre del Parámetro| Descripción| Tipo de Dato  
---|---|---  
image| Imagen renderizada del lienzo| IMAGE  
mask| Máscara que contiene la posición actual del modelo| MASK  
mesh_path| Ruta del archivo del modelo| STRING  
normal| Mapa de normales| IMAGE  
lineart| Salida de imagen de arte lineal, el `edge_threshold` correspondiente se puede ajustar en el menú del modelo del lienzo| IMAGE  
camera_info| Información de la cámara| LOAD3D_CAMERA  
recording_video| Video grabado (solo cuando existe una grabación)| VIDEO  
  
Vista previa de todas las salidas: ![Demostración de operación de vista](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/load3d_outputs.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=9f5a50adc39a7614a8f83ee709f1fbda)

## 

​

Descripción del Área del Lienzo

El área del Lienzo del nodo Load3D contiene numerosas operaciones de vista, incluyendo:

  * Configuraciones de vista previa (cuadrícula, color de fondo, vista previa)
  * Control de cámara: Controlar FOV, tipo de cámara
  * Intensidad de iluminación global: Ajustar la intensidad de la luz
  * Grabación de video: Grabar y exportar videos
  * Exportación de modelo: Compatible con formatos `GLB`, `OBJ`, `STL`
  * Y más

![Interfaz de usuario del nodo Load 3D](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/load3d_ui.jpg?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=ee504a68a45a19e68bf27635cf5d1436)

  1. Contiene múltiples menús y menús ocultos del nodo Load 3D
  2. Menú para `redimensionar la ventana de vista previa` y `grabación de video del lienzo`
  3. Eje de operación de la vista 3D
  4. Miniatura de vista previa
  5. Configuraciones de tamaño de vista previa, escala la visualización de la vista previa estableciendo dimensiones y luego redimensionando la ventana



### 

​

1\. Operaciones de Vista

Tu navegador no soporta la reproducción de video.Operaciones de control de vista:

  * Clic izquierdo + arrastrar: Rotar la vista
  * Clic derecho + arrastrar: Desplazar la vista
  * Rueda del medio o clic central + arrastrar: Acercar/Alejar
  * Eje de coordenadas: Cambiar vistas



### 

​

2\. Funciones del Menú Izquierdo

![Menú](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=8d906a62632bc4a4eae4e76aada77862) En el lienzo, algunas configuraciones están ocultas en el menú. Haz clic en el botón de menú para expandir diferentes menús

  *     1. Escena: Contiene cuadrícula de ventana de vista previa, color de fondo, configuraciones de vista previa
  *     2. Modelo: Modo de renderizado del modelo, texturas de materiales, configuración de dirección hacia arriba
  *     3. Cámara: Cambiar entre vistas ortográfica y perspectiva, y establecer el tamaño del ángulo de perspectiva
  *     4. Luz: Intensidad de iluminación global de la escena
  *     5. Exportar: Exportar modelo a otros formatos (GLB, OBJ, STL)



#### 

​

Escena

![menú de escena](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_scene.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=ecbfa96b458f8a1799d447557a49bd6e) El menú Escena proporciona algunas funciones básicas de configuración de la escena

  1. Mostrar/Ocultar cuadrícula
  2. Establecer color de fondo
  3. Haz clic para subir una imagen de fondo
  4. Ocultar la vista previa



#### 

​

Modelo

![Menú_Escena](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_model.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=755a3f4e1aec5042b9893b37c6d987e8) El menú Modelo proporciona algunas funciones relacionadas con el modelo

  1. **Dirección hacia arriba** : Determinar qué eje es la dirección hacia arriba para el modelo
  2. **Modo de material** : Cambiar los modos de renderizado del modelo - Original, Normal, Malla, Arte Lineal



#### 

​

Cámara

![menú_modelo_cámara](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_camera.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=575bff41361272230d0928595da65d16) Este menú proporciona el cambio entre vistas ortográfica y perspectiva, y la configuración del tamaño del ángulo de perspectiva

  1. **Cámara** : Cambiar rápidamente entre vistas ortográfica y perspectiva
  2. **FOV** : Ajustar el ángulo FOV



#### 

​

Luz

![menú_modelo_cámara](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_light.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=d242f04c2061d2458ffc8a5906d7747b) A través de este menú, puedes ajustar rápidamente la intensidad de iluminación global de la escena

#### 

​

Exportar

![menú_exportar](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Load3D/menu_export.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=a6df9da61ff0168f4d403ff20f087c7e) Este menú proporciona la capacidad de convertir y exportar rápidamente formatos de modelo

### 

​

3\. Funciones del Menú Derecho

Tu navegador no soporta la reproducción de video.El menú derecho tiene dos funciones principales:

  1. **Restablecer proporción de vista** : Después de hacer clic en el botón, la vista ajustará la proporción del área de renderizado del lienzo según el ancho y alto establecidos
  2. **Grabación de video** : Permite grabar las operaciones actuales de la vista 3D como video, permite la importación, y se puede emitir como `recording_video` a nodos posteriores



> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3D/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Load3D.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Load3D)

[Obtener componentes 3D](https://docs.comfy.org/es/built-in-nodes/Get3DComponents)[Cargar 3D (Avanzado)](https://docs.comfy.org/es/built-in-nodes/Load3DAdvanced)
