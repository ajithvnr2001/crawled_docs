---
url: https://docs.comfy.org/es/interface/shortcuts/
title: Atajos de teclado y rat\u00f3n - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:30.518549+00:00
---

# Atajos de teclado y ratón - ComfyUI

> Source: https://docs.comfy.org/es/interface/shortcuts/

## En esta página

Volver arriba

  * Buscar y editar un atajo
  * Preajustes de combinaciones de teclas



Configuraciones de ComfyUI

# Atajos de teclado y ratón

Copiar páginaCopiar página

Atajos de teclado y ratón de ComfyUI: la lista predeterminada completa y cómo reasignar comandos y guardar tus propias combinaciones.

Copiar páginaCopiar página

Las configuraciones descritas en esta página se encuentran en el **menú de configuraciones dentro de la aplicación de ComfyUI**. Puedes abrirlo navegando a **Configuraciones** (icono de engranaje) o usando el atajo de teclado `Ctrl + ,`, y luego seleccionar la categoría correspondiente para ver y configurar estas opciones.

ComfyUI incluye un conjunto predeterminado de atajos de teclado, y cada comando se puede reasignar. Abre **Configuraciones (icono de engranaje)** > **Combinación de teclas** para ver y cambiar los atajos. ![Configuraciones de atajos de ComfyUI](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/setting/keybinding.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=3b36de580ec995fdd0ec7cc64e3b670c)

## 

​

Buscar y editar un atajo

El panel lista cada comando con su combinación de teclas actual. La caja de búsqueda en la parte superior reduce la lista, y al hacer clic en el encabezado **Comando** esta se ordena alfabéticamente. La columna **Fuente** indica el nombre de la extensión o el paquete de nodos personalizado que proporciona un comando; los comandos que provienen del propio ComfyUI la dejan vacía. Selecciona el icono de edición en una fila para grabar una nueva combinación de teclas. Un menú de fila puede reiniciar ese comando a su valor predeterminado o eliminar sus combinaciones de teclas. Cuando un comando tiene más de una combinación de teclas, la fila se expande y cada combinación obtiene sus propios botones de editar y eliminar. **Restablecer todo** en la parte inferior del panel borra cada personalización después de un aviso de confirmación.

## 

​

Preajustes de combinaciones de teclas

Tus cambios pertenecen a un preajuste con nombre, y el selector de preajustes en la parte superior del panel te permite cambiar entre ellos. El **Preajuste predeterminado** contiene los atajos integrados. Al seleccionarlo, se restauran esos atajos y se descartan los cambios sin guardar de tu sesión actual. Los preajustes que guardaste anteriormente permanecen en el disco.

  * El nombre de un preajuste muestra un `*` mientras tenga cambios sin guardar. En un preajuste guardado, selecciona **Guardar cambios** para almacenarlos. El Preajuste predeterminado no tiene botón Guardar cambios, por lo que sus cambios se guardan mediante **Guardar como nuevo preajuste**.
  * El botón … (más) junto al selector de preajustes contiene **Guardar como nuevo preajuste** (oculto mientras el Preajuste predeterminado no tenga cambios), **Restablecer a predeterminado** , **Eliminar preajuste** (deshabilitado para el Preajuste predeterminado), **Importar preajuste** y **Exportar preajuste**.
  * **Importar preajuste** lee un archivo de preajuste exportado desde ComfyUI, de modo que un conjunto de atajos puede moverse entre instalaciones o entregarse a otro usuario. **Exportar preajuste** escribe el preajuste actual en un archivo JSON.
  * Si cambias de preajuste mientras hay cambios sin guardar, se te pedirá que los guardes primero, o que los descartes y continúes.

Los preajustes se almacenan como archivos JSON en el directorio de usuario de ComfyUI, dentro de `keybindings/`. A continuación se muestra la lista predeterminada actual de atajos.

  * Windows/Linux

  * MacOS




Atajo| Comando  
---|---  
Ctrl + Enter| Poner en cola el prompt  
Ctrl + Shift + Enter| Poner en cola el prompt (al frente)  
Ctrl + Alt + Enter| Interrumpir  
Ctrl + Z / Ctrl + Y| Deshacer/Rehacer  
Ctrl + S| Guardar flujo de trabajo  
Ctrl + O| Cargar flujo de trabajo  
Ctrl + A| Seleccionar todos los nodos  
Alt + C| Contraer/Expandir nodos seleccionados  
Ctrl + M| Silenciar/Activar sonido de nodos seleccionados  
Ctrl + B| Evitar/No evitar nodos seleccionados  
Supr  
Retroceso| Eliminar nodos seleccionados  
Retroceso| Limpiar flujo de trabajo  
Espacio| Mover el lienzo al mantenerlo presionado y desplazar el cursor  
Ctrl + Clic  
Shift + Clic| Agregar a la selección el nodo en el que hagas clic  
Ctrl + C/Ctrl + V| Copiar y pegar nodos seleccionados (sin mantener las conexiones a las salidas de nodos no seleccionados)  
Ctrl + C/Ctrl + Shift + V| Copiar y pegar nodos seleccionados (manteniendo las conexiones desde las salidas de nodos no seleccionados a las entradas de los nodos pegados)  
Shift + Arrastrar| Mover varios nodos seleccionados al mismo tiempo  
Ctrl + G| Agregar un marco a los nodos seleccionados  
Ctrl + ,| Mostrar diálogo de configuración  
Alt + =| Acercar (lienzo)  
Alt + -| Alejar (lienzo)  
.| Ajustar vista a los nodos seleccionados  
P| Anclar/Desanclar elementos seleccionados  
Q| Alternar barra lateral de la cola  
W| Alternar barra lateral del flujo de trabajo  
N| Alternar barra lateral de biblioteca de nodos  
M| Alternar barra lateral de biblioteca de modelos  
Ctrl + `| Alternar panel inferior de registro  
F| Alternar modo de enfoque (pantalla completa)  
R| Actualizar definiciones de nodos  
Doble clic con el botón izquierdo| Búsqueda rápida de nodos para agregar  
  
Atajo| Comando  
---|---  
Cmd ⌘ + Enter| Indicador de cola  
Cmd ⌘ + Shift + Enter| Indicador de cola (al frente)  
Cmd ⌘ + Alt + Enter| Interrumpir  
Cmd ⌘ + Z/Cmd ⌘ + Y| Deshacer/Rehacer  
Cmd ⌘ + S| Guardar flujo de trabajo  
Cmd ⌘ + O| Cargar flujo de trabajo  
Cmd ⌘ + A| Seleccionar todos los nodos  
Opt ⌥ + C| Contraer/Expandir nodos seleccionados  
Cmd ⌘ + M| Silenciar/Activar sonido de nodos seleccionados  
Cmd ⌘ + B| Evitar/No evitar nodos seleccionados  
Delete  
Backspace| Eliminar nodos seleccionados  
Backspace| Limpiar flujo de trabajo  
Space| Mover el lienzo al mantener presionado y mover el cursor  
Cmd ⌘ + Click  
Shift + Click| Agregar el nodo clicado a la selección  
Cmd ⌘ + C / Cmd ⌘ + V| Copiar y pegar nodos seleccionados (sin mantener conexiones con las salidas de nodos no seleccionados)  
Cmd ⌘ + C / Cmd ⌘ + Shift + V| Copiar y pegar nodos seleccionados (manteniendo las conexiones desde las salidas de nodos no seleccionados hacia las entradas de los nodos pegados)  
Shift + Drag| Mover varios nodos seleccionados al mismo tiempo  
Cmd ⌘ + G| Agregar marco a los nodos seleccionados  
Cmd ⌘ + ,| Mostrar diálogo de configuración  
Opt ⌥ + =| Acercar (lienzo)  
Opt ⌥ + -| Alejar (lienzo)  
.| Ajustar vista a los nodos seleccionados  
P| Anclar/Desanclar elementos seleccionados  
Q| Alternar barra lateral de la cola  
W| Alternar barra lateral del flujo de trabajo  
N| Alternar barra lateral de biblioteca de nodos  
M| Alternar barra lateral de biblioteca de modelos  
Cmd ⌘ + `| Alternar panel inferior de registro  
F| Alternar modo de enfoque (pantalla completa)  
R| Actualizar definiciones de nodos  
Double-Click LMB| Búsqueda rápida de nodos para agregar  
  
¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/shortcuts.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/shortcuts)

[Editor de Máscara](https://docs.comfy.org/es/interface/settings/mask-editor)[Extensión](https://docs.comfy.org/es/interface/settings/extension)
