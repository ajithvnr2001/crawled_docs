---
url: https://docs.comfy.org/es/interface/overview/
title: Resumen de la interfaz - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:29.663581+00:00
---

# Resumen de la interfaz - ComfyUI

> Source: https://docs.comfy.org/es/interface/overview/

## En esta página

Volver arriba

  * Localización
  * Mapa del espacio de trabajo
    * Barra lateral izquierda
    * Panel del lado derecho
    * Lienzo
    * Barra de ejecución
    * Parte inferior y ayuda
  * Componentes de funciones
  * Configuraciones
  * Cuenta y créditos
  * Exclusivo de Cloud



Guía de la interfaz

# Resumen de la interfaz

Copiar páginaCopiar página

Mapa del espacio de trabajo de ComfyUI: regiones, componentes, configuraciones, cuenta y créditos, y exclusivas de Cloud.

Copiar páginaCopiar página

La interfaz visual es la forma en que la mayoría de las personas controlan el [Servidor de ComfyUI](https://docs.comfy.org/es/development/comfyui-server/comms_overview). Usa esta página como un mapa de la interfaz y luego abre las guías enlazadas para cada región y componente. ![Interfaz básica de ComfyUI](https://mintcdn.com/dripart/EeFKEryMLH5667kk/images/interface/overview/comfyui_new_interface.jpg?fit=max&auto=format&n=EeFKEryMLH5667kk&q=85&s=4d18b1d3d8044ca37fc71f7e89d143e7) El [frontend de ComfyUI](https://github.com/Comfy-Org/ComfyUI_frontend) se mantiene como un proyecto propio. Las contribuciones se envían a ese repositorio.

## 

​

Localización

ComfyUI es compatible con inglés, chino, ruso, francés, japonés y coreano. Abre **Configuraciones** y, en `Comfy` → `Locale`, elige tu idioma. ![Soporte de localización de ComfyUI](https://mintcdn.com/dripart/eWfBNjjL5jL2h2ib/images/interface/overview/locale.jpg?fit=max&auto=format&n=eWfBNjjL5jL2h2ib&q=85&s=f7bdc0a03f437ea74bd9c69e3b9bc6d7)

## 

​

Mapa del espacio de trabajo

![Espacio de trabajo de ComfyUI con regiones numeradas del 1 al 6](https://mintcdn.com/dripart/Bf4DeDZgTg4kdJMV/images/interface/overview/comfyui-new-interface-main.png?fit=max&auto=format&n=Bf4DeDZgTg4kdJMV&q=85&s=a9b74b0809cce523bf37bfcefbfd68b5) Los números en la captura de pantalla coinciden con las regiones a continuación:

#| Área| Qué es  
---|---|---  
**1**| **Barra lateral izquierda**|  Recursos, Biblioteca de nodos, Biblioteca de modelos, Flujos de trabajo, Apps y (cuando está habilitado) Historial de trabajos  
**2**| **Lienzo**|  El grafo donde colocas y conectas nodos, además de los controles del lienzo  
**3**| **Panel del lado derecho**|  Parámetros, información del nodo, configuraciones y errores de la selección actual (se abre desde el interruptor de propiedades de la barra superior)  
**4**| **Barra superior**|  Abrir flujos de trabajo, controles de Ejecutar / cola, inicio de sesión y el interruptor del panel de propiedades  
**5**| **Abajo a la izquierda**|  Centro de ayuda, panel inferior (registros / atajos) y Configuraciones  
**6**| **Abajo a la derecha**|  Controles del lienzo: desplazamiento, minimapa, visibilidad de conexiones, zoom, ajustar  
  
### 

​

Barra lateral izquierda

Los íconos de la barra lateral izquierda, de arriba a abajo. **Historial de trabajos** aparece en la parte superior solo cuando `Comfy.Queue.QPOV2` está habilitado: ![Orden de los íconos de la barra lateral izquierda: Historial de trabajos \(cuando está habilitado\), Recursos, Nodos, Modelos, Flujos de trabajo, Apps](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/overview/sidebar_order.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=660e8ca23ca81dbf9a3daf5c8a518f0d)

## Recursos

Medios generados e importados: vista previa, reutilizar, descargar, eliminar

## Biblioteca de nodos

Cuadrícula de Esenciales y lista completa de nodos, favoritos, búsqueda

## Biblioteca de modelos

Modelos detectados en tu carpeta de modelos

## Flujos de trabajo

Flujos de trabajo guardados localmente y archivos recientes

## Apps

Entrada Apps de la barra lateral; consulta también Modo App en Componentes de funciones

## Historial de trabajos

Historial de cola / trabajos cuando QPOV2 está habilitado

### 

​

Panel del lado derecho

## Panel del lado derecho

Parámetros, Información (documentación de nodos), Configuraciones, Errores

### 

​

Lienzo

## Controles del lienzo

Minimapa, conexiones, información del lienzo, zoom, ajustar, modo de enfoque

## Nodos 2.0

Interfaz de los nodos, encabezados y comportamiento de la selección

### 

​

Barra de ejecución

La barra de ejecución flotante se ubica en la parte superior del lienzo y contiene todo lo necesario para iniciar y supervisar una ejecución: conteo de lotes, Run, modo de cola, cancelar y el número de trabajos activos. ![Barra de ejecución: 1 controlador de arrastre, 2 conteo de lotes, 3 Run, 4 modo de cola, 5 cancelar, 6 trabajos activos](https://mintcdn.com/dripart/eWJdujtoaBSEH32O/images/interface/overview/run_bar.png?fit=max&auto=format&n=eWJdujtoaBSEH32O&q=85&s=a667c6a1008fdb6963c8c84fdfe5faa6)

#| Control| Qué hace  
---|---|---  
**1**| **Controlador de arrastre**|  Mueve la barra a cualquier lugar del lienzo. Mientras arrastras, aparece una zona **Acoplar en la parte superior** para fijarla de nuevo al borde superior.  
**2**| **Conteo de lotes**|  Cuántas veces se encola el flujo de trabajo por ejecución (predeterminado `1`). Escribe un valor o usa las flechas arriba y abajo.  
**3**| **Run**|  Encola el flujo de trabajo. Mantén `Shift` para encolarlo al frente de la cola en lugar del final.  
**4**| **Menú de modo de cola**|  Elige cuándo se encola el flujo de trabajo a sí mismo: **Run** (solo cuando haces clic), **Run (On Change)** (se encola de nuevo cada vez que el flujo de trabajo cambia) o **Run (Instant)** (se encola de nuevo en cuanto termina la ejecución actual).  
**5**| **Cancelar**|  Detiene la ejecución que se está ejecutando ahora. Deshabilitado mientras la cola está inactiva.  
**6**| **Trabajos activos**|  Número de trabajos en cola y en ejecución. Haz clic para abrir la cola, haz clic derecho para vaciarla.  
  
### 

​

Parte inferior y ayuda

## Panel inferior

Atajos, registros y (escritorio) terminal de comandos

## Centro de ayuda

Notas de la versión, documentación, soporte, retroalimentación

## 

​

Componentes de funciones

Capacidades de IU reutilizables que no están ligadas a una sola región del chrome del espacio de trabajo.

## Plantillas

Plantillas de flujos de trabajo integradas

## Modo App

IU lineal / estilo aplicación para ejecutar flujos de trabajo

## Subgrafo

Contrae grafos en nodos de subgrafo reutilizables

## Ejecución parcial

Ejecuta solo una parte de un flujo de trabajo

## Documentación de nodos

Ayuda de nodos dentro de la aplicación (también en la pestaña Info de RSP)

## Entradas dinámicas

Entradas dinámicas que crecen a medida que las conectas

## Editor de máscara

Pinta y edita máscaras en el lienzo

## 

​

Configuraciones

## Configuraciones

Diálogo completo de configuraciones por categoría

## 

​

Cuenta y créditos

## Usuario

Configuraciones de cuenta y perfil

## Plan y créditos

Saldo, recarga, actividad de uso y facturas de Cloud

## 

​

Exclusivo de Cloud

## Espacios de trabajo

Espacios de trabajo en equipo en Comfy Cloud

## Compartir flujo de trabajo

Comparte flujos de trabajo desde Cloud

## Importar modelos

Sube tus propios modelos a Cloud

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/overview)

[Dependencias](https://docs.comfy.org/es/basic-concepts/dependencies)[Recursos](https://docs.comfy.org/es/interface/assets)
