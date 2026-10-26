---
url: https://docs.comfy.org/es/agent-tools/in-app-agent-installation/
title: Empezar con Comfy Agent - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:22.127848+00:00
---

# Empezar con Comfy Agent - ComfyUI

> Source: https://docs.comfy.org/es/agent-tools/in-app-agent-installation/

## En esta página

Volver arriba

  * Elige tu configuración
  * Crear tu primera imagen
    * Abrir el Agente
    * Crear un flujo de trabajo
    * Generar la imagen
    * Hacer un cambio
  * Solución de problemas
    * Falta el botón del Agente
    * El Agente no puede editar el flujo de trabajo que esperaba
    * El Agente solicita una entrada
    * No encuentro una conversación local en Cloud
  * Próximos pasos



Comfy Agent

# Empezar con Comfy Agent

Copiar páginaCopiar página

Abre Comfy Agent en Comfy Cloud o Comfy Desktop.

Copiar páginaCopiar página

## 

​

Elige tu configuración

Necesitas una cuenta de Comfy.

  * **Comfy Cloud:** Comfy Agent está disponible de forma general. [Inicia sesión en Cloud](https://cloud.comfy.org). No necesitas instalación local ni unirte a una lista de espera.
  * **Comfy Desktop:** Comfy Agent para ComfyUI local llegará próximamente. [Únete a la lista de espera](https://links.comfy.org/agentalpha) para recibir una notificación.



## 

​

Crear tu primera imagen

### 

​

Abrir el Agente

Abre un flujo de trabajo en blanco y luego selecciona **Agent** en el extremo derecho de la barra de pestañas, junto a tu avatar. Lee y acepta el aviso de consentimiento si se te solicita. Usa **Elige un flujo de trabajo** en el panel del Agente para seleccionar el flujo de trabajo en blanco.

### 

​

Crear un flujo de trabajo

Envía este mensaje:

> Crea un flujo de trabajo de texto a imagen para un tenis rojo sobre un fondo gris neutro. Usa un modelo disponible e incluye un nodo **Save Image**. Revisa el flujo de trabajo en busca de errores, pero no lo ejecutes todavía.

El Agente construye el flujo de trabajo en el lienzo, completa el prompt y la configuración del modelo, y revisa las conexiones entre nodos y las entradas requeridas. Deberías ver un flujo de trabajo conectado que termina en un nodo **Save Image**. Si el Agente informa que falta un modelo o un archivo, proporciónalo o pide una alternativa disponible en tu instalación. Pídele que revise el flujo de trabajo nuevamente antes de continuar.

### 

​

Generar la imagen

Abre **Permisos de ejecución** junto a la caja de mensaje, elige **Preguntar** y selecciona **Guardar cambios** si cambiaste la configuración. Envía “Ejecuta este flujo de trabajo.” Cuando el Agente solicite aprobación, selecciona **Run**. Selecciona **Cancelar** en su lugar si no quieres iniciar esa ejecución. Cuando termine la generación, el Agente devuelve el resultado en la conversación. La imagen también aparece en el nodo **Save Image**. Haz clic derecho sobre la imagen allí para guardarla en tu computadora.

### 

​

Hacer un cambio

Envía “Cambia el fondo a blanco y conserva el modelo y las demás configuraciones.” El Agente actualiza el flujo de trabajo existente. Pídele que lo ejecute de nuevo para comparar el resultado.

## 

​

Solución de problemas

### 

​

Falta el botón del Agente

Inicia sesión en tu cuenta de Comfy. En Comfy Desktop, [actualiza la aplicación](https://docs.comfy.org/es/installation/update_comfyui) y reiníciala. Si el botón sigue faltando, consulta el acceso al Agente de tu cuenta con [soporte](https://docs.comfy.org/es/support/contact-support).

### 

​

El Agente no puede editar el flujo de trabajo que esperaba

Elige el flujo de trabajo deseado en el panel del Agente y vuelve a enviar tu mensaje. Consulta [Elegir qué flujo de trabajo editar](https://docs.comfy.org/es/agent-tools/in-app-agent#elegir-qu%C3%A9-flujo-de-trabajo-editar).

### 

​

El Agente solicita una entrada

Selecciona **Attach a file** o arrastra el archivo solicitado al cuadro de mensaje y luego pide al Agente que continúe.

### 

​

No encuentro una conversación local en Cloud

El historial local y el de Cloud están separados. Consulta [Datos y privacidad](https://docs.comfy.org/es/agent-tools/in-app-agent-data-privacy#historial-de-chat-y-sincronizaci%C3%B3n).

## 

​

Próximos pasos

## Editar un flujo de trabajo existente

Cambia los prompts, los modelos o los pasos de procesamiento.

## Guardar una habilidad reutilizable

Recuerda instrucciones para futuras solicitudes.

Consulta [Datos y privacidad](https://docs.comfy.org/es/agent-tools/in-app-agent-data-privacy) para obtener información sobre dónde se almacenan los mensajes, los archivos y las conversaciones.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/agent-tools/in-app-agent-installation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/agent-tools/in-app-agent-installation)

[Descripción general](https://docs.comfy.org/es/agent-tools/in-app-agent)[Habilidades del Agente](https://docs.comfy.org/es/agent-tools/in-app-agent-skills)
