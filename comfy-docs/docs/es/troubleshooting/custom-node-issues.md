---
url: https://docs.comfy.org/es/troubleshooting/custom-node-issues/
title: Soluci\u00f3n de problemas de nodos personalizados - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T14:55:29.024783+00:00
---

# Solución de problemas de nodos personalizados - ComfyUI

> Source: https://docs.comfy.org/es/troubleshooting/custom-node-issues/

## En esta página

Volver arriba

  * ¿Cómo desactivar todos los nodos personalizados?
  * ¿Qué es la búsqueda binaria?
  * Dos métodos de solución de problemas
  * Usar la búsqueda binaria para solucionar problemas
    * 1\. Solucionar problemas de las extensiones frontend de los nodos personalizados
    * 2\. Solución general de problemas de nodos personalizados
  * Cómo solucionar el problema
    * Opción 1: Actualizar el nodo
    * Opción 2: Reemplazar el nodo
    * Opción 3: Reportar el problema
    * Opción 4: Eliminar o deshabilitar el nodo
  * Reportar problemas
    * Para problemas específicos de nodos personalizados
    * Para problemas del núcleo de ComfyUI
    * Para problemas de la aplicación de escritorio
    * Para problemas del frontend



Troubleshooting

# Solución de problemas de nodos personalizados

Copiar páginaCopiar página

Soluciona problemas de nodos personalizados en ComfyUI: desactívalos todos con —disable-all-custom-nodes y aísla, corrige o elimina el nodo dañado.

Copiar páginaCopiar página

Este es el enfoque general para solucionar problemas de nodos personalizados:

## 

​

¿Cómo desactivar todos los nodos personalizados?

  * Usuarios de Desktop

  * Instalación manual

  * Portable




Inicia Comfy Desktop con los nodos personalizados desactivados desde el menú de configuraciones![Menú de configuraciones - Desactivar nodos personalizados](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/desktop-diable-custom-node.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=81e3ec0e178c9d0852ae4d97efc1232f)o ejecuta el servidor manualmente:
    
    
    cd path/to/your/comfyui
    python main.py --disable-all-custom-nodes
    
    
    
    cd ComfyUI
    python main.py --disable-all-custom-nodes
    

  * Modificar el archivo `.bat`

  * Desde la línea de comandos




Abre la carpeta donde se encuentra la versión portable y busca el archivo `run_nvidia_gpu.bat` o `run_cpu.bat`![Modificar archivo .bat](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/Portable-disable-custom-nodes.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e5e98abac0f8b4525791042bc4727f3b)

  1. Copia el archivo `run_nvidia_gpu.bat` o `run_cpu.bat` y renómbralo a `run_nvidia_gpu_disable_custom_nodes.bat`
  2. Abre el archivo copiado con el Bloc de notas
  3. Agrega el parámetro `--disable-all-custom-nodes` al archivo, o copia los siguientes parámetros en un archivo `.txt` y renombra el archivo a `run_nvidia_gpu_disable_custom_nodes.bat`


    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --disable-all-custom-nodes  --windows-standalone-build
    pause
    

  4. Guarda el archivo y ciérralo
  5. Haz doble clic en el archivo para ejecutarlo. Si todo es normal, deberías ver que ComfyUI se inicia con los nodos personalizados desactivados



![Solución de problemas de ComfyUI](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/portable-disable-custom-nodes-cml-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=168ab7a2fa8c72a324b13e7aa0605721)

  1. Entra en la carpeta donde se encuentra la versión portable
  2. Abre la terminal con clic derecho en el menú → Abrir terminal ![Solución de problemas de ComfyUI](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/portable-disable-custom-nodes-cml-2.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e94076e9febdd73b763aa4ad31eff68b)
  3. Asegúrate de que el nombre de la carpeta sea el directorio actual de la versión portable
  4. Introduce el siguiente comando para iniciar ComfyUI mediante el python portable y desactivar los nodos personalizados


    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --disable-all-custom-nodes
    

**Resultados:**

  * ✅ **El problema desaparece** : Un nodo personalizado está causando el problema → Continúa al paso 2
  * ❌ **El problema persiste** : No es un problema de nodos personalizados → Reporta el problema



## 

​

¿Qué es la búsqueda binaria?

En este documento presentamos el enfoque de búsqueda binaria para solucionar problemas con nodos personalizados, que consiste en revisar la mitad de los nodos personalizados a la vez hasta localizar el nodo que causa el problema. Consulta el siguiente diagrama de flujo para ver el procedimiento específico: habilita la mitad de los nodos deshabilitados cada vez y comprueba si el problema aparece, hasta identificar qué nodo personalizado lo está causando.

## 

​

Dos métodos de solución de problemas

En este documento, clasificamos los nodos personalizados en dos tipos para la solución de problemas: ![Tipos de nodos personalizados](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/custom_node_type.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=de35f5f9b582df8a3825b1103e8500fa)

  * A: Nodos personalizados con extensiones de frontend
  * B: Nodos personalizados normales

Primero, conozcamos los problemas y causas potenciales de los distintos tipos de nodos personalizados:

  * Nodos personalizados con extensiones de frontend

  * Nodos personalizados normales




En el caso de los nodos personalizados, podemos priorizar la solución de problemas de aquellos con extensiones de frontend, ya que son los que más problemas causan. Sus principales conflictos surgen de incompatibilidades con las actualizaciones de la versión del frontend de ComfyUI.Los problemas comunes incluyen:

  * Flujos de trabajo que no se ejecutan
  * Algunos nodos no pueden mostrar imágenes de vista previa (como el nodo Guardar Imagen)
  * Elementos de la interfaz desalineados
  * No se puede acceder al frontend de ComfyUI
  * Interfaz completamente rota o pantalla en blanco
  * No se puede comunicar normalmente con el backend de ComfyUI
  * Las conexiones entre nodos no funcionan correctamente
  * Y más

Causas comunes de estos problemas:

  * Modificaciones en el frontend durante las actualizaciones a las que los nodos personalizados aún no se han adaptado
  * Usuarios que actualizan ComfyUI sin actualizar al mismo tiempo los nodos personalizados, aunque los autores ya hayan publicado versiones compatibles
  * Autores que dejan de dar mantenimiento, lo que provoca incompatibilidad entre las extensiones de los nodos personalizados y el frontend de ComfyUI



Si el problema no lo causan las extensiones de frontend de los nodos personalizados, a menudo está relacionado con las dependencias. Los problemas comunes incluyen:

  * Errores de “Failed to import” en la consola o los registros
  * Nodos faltantes que siguen apareciendo como faltantes después de instalarlos y reiniciar
  * ComfyUI se bloquea o no logra iniciar
  * Y más

Causas comunes de estos errores:

  * Nodos personalizados que requieren wheels adicionales como ComfyUI-Nunchaku
  * Nodos personalizados que usan versiones estrictas de dependencias (por ejemplo, `torch==2.4.1`) mientras otros plugins usan versiones diferentes (por ejemplo, `torch>=2.4.2`), lo que genera conflictos después de la instalación
  * Problemas de red que impiden que las dependencias se instalen correctamente

Cuando los problemas involucran interdependencias y versiones del entorno de Python, la solución de problemas se vuelve más compleja y requiere conocimientos de gestión de entornos de Python, incluido cómo instalar y desinstalar dependencias

## 

​

Usar la búsqueda binaria para solucionar problemas

Entre estos dos tipos distintos de problemas de nodos personalizados, los conflictos entre las extensiones frontend de los nodos personalizados y ComfyUI son los más comunes. Vamos a priorizar la solución de problemas de estos nodos primero. Este es el enfoque general para solucionar problemas:

### 

​

1\. Solucionar problemas de las extensiones frontend de los nodos personalizados

1

Desactivar todas las extensiones frontend de terceros

![Desactivar todas las extensiones frontend de los plugins](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/disable_3rd_party.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ae3bfc32cbe98dce9fdce7874cdf6516)Después de iniciar ComfyUI, busca el menú `Extensions` en las configuraciones y sigue los pasos que se muestran en la imagen para desactivar todas las extensiones de terceros

Si no puedes entrar al frontend de ComfyUI, simplemente salta la sección de solución de problemas de extensiones frontend y continúa con el Enfoque general para solucionar problemas de nodos personalizados

2

Reiniciar ComfyUI

Después de desactivar las extensiones frontend por primera vez, se recomienda reiniciar ComfyUI para asegurarte de que todas las extensiones frontend estén correctamente desactivadas

  * Si el problema desaparece, entonces fue causado por las extensiones frontend de nodos personalizados, y podemos continuar con la solución de problemas mediante búsqueda binaria
  * Si el problema persiste, entonces no fue causado por las extensiones frontend: consulta los otros enfoques de solución de problemas en este documento.



3

Usar la búsqueda binaria para localizar los nodos problemáticos

Usa el método mencionado al inicio de este documento para solucionar el problema, habilitando la mitad de los nodos personalizados a la vez hasta que encuentres el nodo problemático![Habilitar extensiones frontend](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/enable_extensions.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=9ba859462bdd883cdecd0ab8df40ad62)Consulta la imagen para habilitar la mitad de las extensiones frontend. Ten en cuenta que si los nombres de las extensiones son similares, probablemente provienen de las extensiones frontend del mismo nodo personalizado

4

Acciones de seguimiento

Si encuentras el nodo personalizado problemático, consulta la sección de corrección de problemas de este documento para resolver los problemas del nodo personalizado

Con este método, no necesitas reiniciar ComfyUI varias veces: basta con recargar ComfyUI después de habilitar o deshabilitar las extensiones frontend de los nodos personalizados. Además, tu alcance de solución de problemas se limita a los nodos con extensiones frontend, lo que reduce enormemente el rango de búsqueda.

### 

​

2\. Solución general de problemas de nodos personalizados

1

Usar la búsqueda binaria para localizar nodos personalizados

Para el método de localización por búsqueda binaria, además de la búsqueda manual, también contamos con una búsqueda binaria automatizada usando comfy-cli, como se detalla a continuación:

  * Usar Comfy CLI (RECOMENDADO)

  * Búsqueda binaria manual




Usar Comfy CLI requiere algo de experiencia con la línea de comandos. Si no te sientes cómodo con ella, usa la búsqueda binaria manual en su lugar.Si tienes [Comfy CLI](https://docs.comfy.org/es/comfy-cli/getting-started) instalado, puedes usar la herramienta automatizada de bisección para encontrar el nodo problemático:
    
    
    # Inicia una sesión de bisección
    comfy-cli node bisect start
    
    # Sigue las indicaciones:
    # - Prueba ComfyUI con el conjunto actual de nodos habilitados
    # - Márcalo como 'good' si el problema desaparece: comfy-cli node bisect good
    # - Márcalo como 'bad' si el problema persiste: comfy-cli node bisect bad
    # - Repite hasta identificar el nodo problemático
    
    # Reinicia cuando termines
    comfy-cli node bisect reset
    

La herramienta de bisección activa y desactiva nodos automáticamente y te guía por el proceso.

Antes de comenzar, **crea una copia de seguridad** de tu carpeta custom_nodes por si algo sale mal.

Si prefieres hacer el proceso manualmente o no tienes Comfy CLI instalado, sigue los pasos a continuación:

1

Crear carpetas temporales

Antes de comenzar, entra en la carpeta `<YOUR_COMFYUI_FOLDER>\ComfyUI\`

  * Windows

  * macOS/Linux

  * Cloud/Colab




  * **Haz una copia de seguridad de todos los nodos personalizados** : Copia y renombra `custom_nodes` a `custom_nodes_backup`
  * **Crea una carpeta temporal** : Crea una carpeta llamada `custom_nodes_temp`

O usa la siguiente línea de comandos para hacer la copia de seguridad:
    
    
    # Crear la copia de seguridad y la carpeta temporal
    mkdir "%USERPROFILE%\custom_nodes_backup"
    mkdir "%USERPROFILE%\custom_nodes_temp"
    
    # Copiar todo el contenido
    xcopy "custom_nodes\*" "%USERPROFILE%\custom_nodes_backup\" /E /H /Y
    

Respalda manualmente la carpeta custom_nodes O usa la siguiente línea de comandos para hacer el respaldo:
    
    
    # Crear respaldo y carpeta temporal
    mkdir ~/custom_nodes_backup
    mkdir ~/custom_nodes_temp
    
    # Respaldar todo el contenido
    cp -r custom_nodes/* ~/custom_nodes_backup/
    
    
    
    # Crea una carpeta de respaldo y una temporal
    mkdir /content/custom_nodes_backup
    mkdir /content/custom_nodes_temp
    
    # Respalda todo el contenido
    cp -r /content/ComfyUI/custom_nodes/* /content/custom_nodes_backup/
    

2

Enumera todos los nodos personalizados

  * Windows

  * macOS/Linux

  * Cloud/Colab




Como Windows tiene una interfaz visual, puedes saltarte este paso a menos que solo uses la línea de comandos
    
    
    dir custom_nodes
    
    
    
    ls custom_nodes/
    
    
    
    ls /content/ComfyUI/custom_nodes/
    

3

Divide los nodos por la mitad

Supongamos que tienes 8 nodos personalizados. Mueve la primera mitad al almacenamiento temporal:

  * Windows

  * macOS/Linux

  * Cloud/Colab



    
    
    # Mueve la primera mitad (nodos 1-4) a temp
    move "custom_nodes\node1" "%USERPROFILE%\custom_nodes_temp\"
    move "custom_nodes\node2" "%USERPROFILE%\custom_nodes_temp\"
    move "custom_nodes\node3" "%USERPROFILE%\custom_nodes_temp\"
    move "custom_nodes\node4" "%USERPROFILE%\custom_nodes_temp\"
    
    
    
    # Mueve la primera mitad (nodos 1-4) a temp
    mv custom_nodes/node1 ~/custom_nodes_temp/
    mv custom_nodes/node2 ~/custom_nodes_temp/
    mv custom_nodes/node3 ~/custom_nodes_temp/
    mv custom_nodes/node4 ~/custom_nodes_temp/
    
    
    
    # Mueve la primera mitad (nodos 1-4) a temp
    mv /content/ComfyUI/custom_nodes/node1 /content/custom_nodes_temp/
    mv /content/ComfyUI/custom_nodes/node2 /content/custom_nodes_temp/
    mv /content/ComfyUI/custom_nodes/node3 /content/custom_nodes_temp/
    mv /content/ComfyUI/custom_nodes/node4 /content/custom_nodes_temp/
    

4

Prueba ComfyUI

Inicia ComfyUI con normalidad
    
    
    python main.py
    

5

Interpreta los resultados

  * **El problema persiste** : El problema está en los nodos restantes (5-8)
  * **El problema desaparece** : El problema estaba en los nodos movidos (1-4)



6

Acota el problema

  * Si el problema persiste: mueve la mitad de los nodos restantes (por ejemplo, los nodos 7-8) a temp
  * Si el problema desapareció: mueve la mitad de los nodos de temp (por ejemplo, los nodos 3-4) de vuelta a custom_nodes



7

Repite hasta encontrar el único nodo problemático

  * Repite hasta encontrar el único nodo problemático



## 

​

Cómo solucionar el problema

Una vez que hayas identificado el nodo personalizado problemático:

### 

​

Opción 1: Actualizar el nodo

  1. Comprueba si hay una actualización disponible en ComfyUI Manager
  2. Actualiza el nodo y vuelve a probar



### 

​

Opción 2: Reemplazar el nodo

  1. Busca nodos personalizados alternativos con una funcionalidad similar
  2. Consulta el [ComfyUI Registry](https://registry.comfy.org) para encontrar alternativas



### 

​

Opción 3: Reportar el problema

Contacta con el desarrollador del nodo personalizado:

  1. Encuentra el repositorio de GitHub del nodo
  2. Crea una incidencia con: 
     * Tu versión de ComfyUI
     * Mensajes de error y registros
     * Pasos para reproducir el problema
     * Tu sistema operativo



### 

​

Opción 4: Eliminar o deshabilitar el nodo

Si no hay una solución disponible y no necesitas esa funcionalidad:

  1. Elimina el nodo problemático de `custom_nodes/` o deshabilítalo en la interfaz de ComfyUI Manager
  2. Reinicia ComfyUI



## 

​

Reportar problemas

Si el problema no lo causan los nodos personalizados, consulta la [descripción general de solución de problemas](https://docs.comfy.org/es/troubleshooting/overview) para ver otros problemas comunes.

### 

​

Para problemas específicos de nodos personalizados

Contacta al desarrollador del nodo personalizado:

  * Busca el repositorio de GitHub del nodo
  * Crea un reporte de problema con tu versión de ComfyUI, los mensajes de error, los pasos para reproducirlo y tu sistema operativo
  * Revisa la documentación del nodo y su página de Issues para comprobar si hay problemas conocidos



### 

​

Para problemas del núcleo de ComfyUI

  * **GitHub** : [Problemas de ComfyUI](https://github.com/Comfy-Org/ComfyUI/issues)
  * **Foro** : [Foro oficial de ComfyUI](https://forum.comfy.org/)



### 

​

Para problemas de la aplicación de escritorio

  * **GitHub** : [Problemas de Comfy Desktop](https://github.com/Comfy-Org/Comfy-Desktop/issues)



### 

​

Para problemas del frontend

  * **GitHub** : [Problemas del frontend de ComfyUI](https://github.com/Comfy-Org/ComfyUI_frontend/issues)



Para problemas generales de instalación, modelos o rendimiento, consulta las páginas de [descripción general de solución de problemas](https://docs.comfy.org/es/troubleshooting/overview) y [problemas de modelos](https://docs.comfy.org/es/troubleshooting/model-issues).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/troubleshooting/custom-node-issues.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/troubleshooting/custom-node-issues)

[Problemas de modelos](https://docs.comfy.org/es/troubleshooting/model-issues)[Contribuir](https://docs.comfy.org/es/community/contributing)
