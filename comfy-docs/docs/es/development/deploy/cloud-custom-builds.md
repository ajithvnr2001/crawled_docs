---
url: https://docs.comfy.org/es/development/deploy/cloud-custom-builds/
title: Agregar Builds personalizados a Comfy Cloud - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-19T16:26:08.793636+00:00
---

# Agregar Builds personalizados a Comfy Cloud - ComfyUI

> Source: https://docs.comfy.org/es/development/deploy/cloud-custom-builds/

## En esta página

Volver arriba

  * Requisitos previos
  * Crear una Build desde tu flujo de trabajo
    * Publicar la Build
    * Desplegar y ejecutar tu flujo de trabajo
  * Agregar tu propio LoRA o modelo
    * Subir el modelo
    * Usar el modelo en tu flujo de trabajo
    * Cambiar o eliminar un modelo de la biblioteca
  * Detener o eliminar tu despliegue
  * Próximos pasos



Comfy Cloud

# Agregar Builds personalizados a Comfy Cloud

Copiar páginaCopiar página

Ejecuta un flujo de trabajo con Nodos Personalizados en Comfy Cloud: crea un Build, ejecuta su despliegue desde el editor, sube un LoRA y elimina el despliegue.

Copiar páginaCopiar página

Un Build empaqueta tus Nodos Personalizados, tus Nodos Personalizados privados, tus LoRAs y otros modelos, y las Dependencias de Python para que tus Flujos de trabajo puedan ejecutarse en Comfy Cloud. Inicias el Build desde el editor de Comfy Cloud, lo creas y lo despliegas en la Developer Platform, y después ejecutas tu flujo de trabajo en él desde el editor. Un despliegue de tu Build también te da workers de GPU que atienden únicamente tus flujos de trabajo, incluso cuando Comfy Cloud ya admite todos los nodos que contienen.

Para usar tu propio LoRA u otro modelo con nodos que Comfy Cloud ya admite, no necesitas un Build. En su lugar, sube el modelo a tu **Biblioteca de modelos**. Consulta Agrega tu propio LoRA o modelo.

### Requisitos previos

Antes de crear un Build, asegúrate de tener lo siguiente:

  * **Un flujo de trabajo guardado en Comfy Cloud**
  * **Una suscripción activa o un saldo de créditos de Comfy superior a cero**



Crear o mantener un Build no tiene costo. Un despliegue consume tiempo de GPU mientras haya una GPU activa para él. También consume almacenamiento mientras el despliegue exista, incluso mientras esté detenido o no haya ninguna GPU activa. El cuadro de diálogo de despliegue muestra el costo estimado antes de que confirmes. Para dejar de pagar, elimina el despliegue. Consulta Detén o elimina tu despliegue.

## Crear una Build desde tu flujo de trabajo

Si tu flujo de trabajo usa Nodos Personalizados que Comfy Cloud no admite, Comfy Cloud muestra un diálogo al abrirlo. El diálogo enumera los paquetes de Nodos Personalizados faltantes (grupos de Nodos Personalizados) y los modelos, como las LoRA. Para ejecutar el flujo de trabajo, crea una Build con ellos. Cuando eliges tu flujo de trabajo guardado, la Developer Platform encuentra sus Nodos Personalizados y sus modelos, y los selecciona por ti.

1

Abrir la Developer Platform

En el diálogo, haz clic en **Create on Platform**. La Developer Platform se abre en una pestaña nueva, en su página **Deploy**.![Diálogo de Comfy Cloud para un flujo de trabajo con Nodos Personalizados que Comfy Cloud no tiene, donde se enumeran los Nodos faltantes encima del enlace Leer la documentación, el botón Crea con tu agente y el botón Create on Platform](https://mintcdn.com/dripart/oPsov_e3HUhk_xUX/images/development/deploy/run-on-custom-deployment.png?fit=max&auto=format&n=oPsov_e3HUhk_xUX&q=85&s=da981d7d6d591244e63f7c3e91979419)

Para crear una Build sin el diálogo, haz clic en el menú de la nube a la izquierda de **Run**. De forma predeterminada, está configurado en **Comfy Cloud**.

  * Si tu espacio de trabajo aún no tiene implementaciones, selecciona **Create a custom deployment** y luego haz clic en **Create on Platform**.
  * Si ya tiene implementaciones, selecciona **Manage deployments**. ![Menú Run on abierto junto al botón Run, con Comfy Cloud marcado, el mensaje This workspace has no deployments yet y Create a custom deployment debajo](https://mintcdn.com/dripart/oPsov_e3HUhk_xUX/images/development/deploy/run-on.png?fit=max&auto=format&n=oPsov_e3HUhk_xUX&q=85&s=3ed4851ed8cf0355d60d208bc64650c4)



2

Iniciar una Build nueva

En la página **Deploy** , haz clic en **New build**. Si aún no tienes ninguna Build, haz clic en **Start from scratch** en su lugar.

3

Elegir tu flujo de trabajo

  1. Haz clic en **Pick from Comfy Cloud**.
  2. Selecciona tu flujo de trabajo y luego haz clic en **Add 1 workflow**.

También puedes arrastrar el archivo `.json` del flujo de trabajo, o una imagen `.png` hecha con él, al área para soltar archivos.![Página de nueva Build de la Developer Platform en su primer paso, con el área para soltar archivos, el botón Pick from Comfy Cloud, el nombre del flujo de trabajo elegido con una marca de verificación, la lista Suggested defaults y los botones Customise build y Build with defaults](https://mintcdn.com/dripart/jxn4ma9PhGXye-0C/images/development/deploy/missing-nodes.png?fit=max&auto=format&n=jxn4ma9PhGXye-0C&q=85&s=2b2c2fb604fd942aae8db27dbd749dfe)El paso se completa cuando el nombre de tu flujo de trabajo aparece debajo del área para soltar archivos con una marca de verificación y la lista **Suggested defaults** muestra los **Custom nodes** de la Build.

4

Crear la Build con los valores predeterminados sugeridos

Haz clic en **Build with defaults…**. Se abre el diálogo **Choose build targets**.Si **Build with defaults…** no está disponible, una línea debajo del botón explica por qué. Cuando esa línea dice _Add the missing models and custom nodes on their steps first._ , agrega lo que falta:

  1. Haz clic en **Customise build**.
  2. Haz clic en **Next** hasta que un paso enumere los Nodos Personalizados o los modelos faltantes.
  3. En cada uno, haz clic en **Use suggestion** o en **Upload**.



Para cambiar lo que incluye la Build, haz clic en **Customise build** y recorre los pasos. Dos pasos determinan el contenido de la Build:

  * **Which custom nodes does the build need?**
    * elige los Nodos Personalizados.
  * **Which models ship inside the build?**
    * elige qué modelos incluye la Build. Un modelo que la Build no incluye se descarga la primera vez que un trabajo lo usa.



### Publicar la Build

Publicar convierte tu Build en una versión numerada, como `v1`, que puedes implementar ahora y más tarde. Publicar es gratis.

  1. En el diálogo **Choose build targets** , deja seleccionado **Serverless build**. Es el objetivo que se ejecuta en Comfy Cloud.
  2. Haz clic en **Publish**.

La página de tu Build se abre con la nueva versión. La fila **Serverless build** muestra el progreso de la Build. Por lo general, la Build tarda de 10 a 15 minutos en completarse, y puedes abandonar la página y volver. Cuando la Build termina, la fila **Serverless build** muestra un botón **Deploy**. Para volver a la versión más tarde:

  1. En la barra lateral de la Developer Platform, haz clic en **Deploy**.
  2. En la sección **Builds** , haz clic en tu Build.
  3. En **Versions** , haz clic en la última versión.



¿Qué pasa si la Build falla?

Algunos Nodos Personalizados fallan durante la compilación. Cuando eso ocurre, la fila **Serverless build** de la página de tu Build muestra **Build failed**.

  1. Abre **Logs** en la fila para leer qué falló.
  2. Haz clic en **Edit build** y cambia la Build, por ejemplo quitando el Nodo Personalizado que falló.
  3. Publica la Build de nuevo.

El botón **Debug with your agent** de la fila abre un prompt que describe el fallo. Cópialo en un agente de programación para reparar la Build.

### Desplegar y ejecutar tu flujo de trabajo

Un despliegue es tu Build ejecutándose en las GPU en la nube de Comfy Cloud. Despliega el Build y luego cambia el editor de Comfy Cloud al despliegue para ejecutar tu flujo de trabajo.

  1. En la fila **Serverless build** , haz clic en **Deploy**. Se abre el diálogo **Deploy v1 of** _el nombre de tu Build_.
  2. Selecciona una GPU. Cada GPU muestra su VRAM (memoria de GPU) y su precio por hora.
  3. Si el diálogo muestra **Ready for the Cloud editor** , deja esa opción seleccionada. Está activada de forma predeterminada.
  4. Deja las demás configuraciones con sus valores predeterminados. Con **Always-warm workers** en `0`, el despliegue apaga sus GPU cuando no llegan tareas. De forma predeterminada, **Keep worker up after a job** mantiene una GPU encendida durante 3 minutos después de la última tarea, y ese tiempo de inactividad se factura a la tarifa de la GPU.
  5. Revisa el panel **Estimated cost**. Muestra el tiempo de GPU por hora y el almacenamiento del modelo por mes.
  6. Haz clic en **Create deployment**. Se abre la página del despliegue. Espera hasta que el estado debajo del nombre del despliegue indique **Ready**.
  7. En el editor de Comfy Cloud, haz clic en el menú de la nube a la izquierda de **Run**. En **Run on** , selecciona tu despliegue. El editor se recarga y tus pestañas permanecen abiertas. ![Menú Run on abierto junto al botón Run, con una marca de verificación junto al despliegue seleccionado](https://mintcdn.com/dripart/oPsov_e3HUhk_xUX/images/development/deploy/selected-deployment.jpg?fit=max&auto=format&n=oPsov_e3HUhk_xUX&q=85&s=805ead9743e23cd00c44c686b3073bc4)
  8. Abre tu flujo de trabajo y haz clic en **Run**. Tu primera tarea puede esperar mientras el despliegue inicia una GPU.

Este navegador sigue ejecutando tus flujos de trabajo en el despliegue hasta que selecciones otro. Para volver, selecciona **Comfy Cloud** en el mismo menú. Si un flujo de trabajo tiene cambios sin guardar, se abre el diálogo **Save your workflows before switching?**. Haz clic en **Save and switch** o en **Switch without saving**.

## Agregar tu propio LoRA o modelo

La **Biblioteca de modelos** contiene los modelos que sube tu espacio de trabajo. Un modelo que subes funciona en Comfy Cloud y en tus despliegues. Antes de subir un modelo, asegúrate de cumplir estos requisitos:

  * **Un plan Pro, Creator, Team o Empresa activo** : tu espacio de trabajo necesita uno para subir un modelo.
  * **Un archivo`.safetensors` de 2 GB o menos**: coloca los modelos base más grandes, como SDXL o Flux, en el Build.



Algunos despliegues creados antes de que existieran los modelos de la biblioteca no pueden cargarlos. Para usar modelos de la biblioteca, crea un nuevo despliegue. En un despliegue antiguo, un trabajo puede fallar con `Library model "<file name>" is unavailable on this deployment. Retry the job. If it still fails, contact support with the job ID.`

### Subir el modelo

Puedes subir el modelo en el editor de Comfy Cloud o en la Developer Platform. Elige la pestaña del lugar donde estés trabajando.

  * Editor de Comfy Cloud

  * Developer Platform




  1. En el menú de la nube a la izquierda de **Run** , asegúrate de que **Comfy Cloud** esté seleccionado en **Run on**. En un despliegue, la **Biblioteca de modelos** no tiene botón **Import**.
  2. En la **barra lateral izquierda** , haz clic en **Biblioteca de modelos** y luego en **Importar**.
  3. Haz clic en **Choose a file** o arrastra un archivo `.safetensors` al cuadro de diálogo.
  4. En **What type of model is this?** , deja **LoRA** si es un LoRA o selecciona el tipo que corresponda al archivo.
  5. Haz clic en **Upload**. Cuando el diálogo muestre _Model successfully imported._ , haz clic en **Finalizar**. ![Cuadro de diálogo Importar un modelo con my_style_lora_9e2417.safetensors \(97.37 MB\) seleccionado, What type of model is this? establecido en LoRA, y los botones Back y Upload](https://mintcdn.com/dripart/A-FVGUweJXUuD_Sl/images/development/serverless/library-models-editor-import.png?fit=max&auto=format&n=A-FVGUweJXUuD_Sl&q=85&s=472fb8f96344cdeca95a18dd901c48e5)

Para importar un modelo desde un enlace de Civitai o Hugging Face en su lugar:

  1. En el cuadro de diálogo **Importar** , pega el enlace del modelo en **Pega el enlace aquí**.
  2. Haz clic en **Continuar**.
  3. En **What type of model is this?** , selecciona el tipo de modelo.
  4. Haz clic en **Importar**.

Una importación desde enlace en otro formato, como `.ckpt`, entra en la **Biblioteca de modelos** , pero no funciona en un despliegue.

  1. En el paso **Which models ship inside the build?** de un Build, haz clic en **Upload Models**.
  2. Selecciona **Workspace library**.
  3. Arrastra un archivo `.safetensors` al área de carga o haz clic en el área para explorar.
  4. En **Tipo de modelo** , deja **LoRA** si es un LoRA o selecciona el tipo que corresponda al archivo.
  5. Haz clic en **Upload**. ![Cuadro de diálogo Upload Models en el paso Which models ship inside the build? de un Build, con las pestañas Public, Private y Workspace library, Workspace library seleccionada, la zona de carga, Tipo de modelo establecido en LoRA, una línea que indica que el archivo está en la biblioteca de tu espacio de trabajo, y los botones Cancelar y Upload](https://mintcdn.com/dripart/A-FVGUweJXUuD_Sl/images/development/serverless/library-models-platform-upload.png?fit=max&auto=format&n=A-FVGUweJXUuD_Sl&q=85&s=3dd2998d080ef5e98d7e7c52c2c00465)



### Usar el modelo en tu flujo de trabajo

Una vez subido el modelo, puedes usarlo en Comfy Cloud o en tu despliegue.

  1. En el menú de la nube a la izquierda de **Run** , selecciona dónde ejecutar: **Comfy Cloud** o tu despliegue.
  2. Agrega un nodo `Load LoRA (Model and CLIP)` o abre un flujo de trabajo que ya tenga uno.
  3. En la lista `lora_name` del nodo, selecciona tu archivo.
  4. Haz clic en **Run**.

![Flujo de trabajo con nodos Load Checkpoint y Load LoRA \(Model and CLIP\), el LoRA subido seleccionado en lora_name, y la fila superior del Panel de Cola mostrando Descargando my_style_lora_9e2417.safetensors 0 B de 97.37 MB](https://mintcdn.com/dripart/A-FVGUweJXUuD_Sl/images/development/serverless/library-models-editor-downloading.png?fit=max&auto=format&n=A-FVGUweJXUuD_Sl&q=85&s=7e7bb638ea4aa1f7599ca742dbcbcf09)

En un despliegue, la primera ejecución descarga el modelo y la fila del trabajo en la cola muestra `Downloading <file name>`. Los trabajos posteriores en la misma GPU en ejecución omiten la descarga. Una GPU que el despliegue inicie más adelante descarga el modelo otra vez. Para omitir la descarga, agrega el modelo al Build.

Sigue estas reglas para que un trabajo encuentre tu modelo:

  * **Elige el tipo correcto.** Un nodo de carga solo lista modelos de su tipo. Un nodo `Load LoRA (Model and CLIP)` lista los modelos subidos como LoRA.
  * **Usa un nombre de archivo nuevo.** Si tu Build ya tiene un modelo con el mismo nombre, un trabajo en tu despliegue usa el archivo del Build, no el que subiste.
  * **Usa el modelo base correcto.** Un LoRA debe coincidir con el modelo base que carga tu flujo de trabajo.
  * **Usa un nodo de carga que exista en Comfy Cloud.** Si el nodo de carga proviene de un nodo personalizado que Comfy Cloud no tiene, agrega el modelo al Build.



### Cambiar o eliminar un modelo de la biblioteca

Cuando hay un despliegue seleccionado en **Run on** , la **Biblioteca de modelos** solo lista los modelos del Build. Para cambiar o eliminar un modelo que subiste, primero vuelve a Comfy Cloud y luego, en la **barra lateral izquierda** , haz clic en **Biblioteca de modelos**. Para cambiar el tipo de modelo:

  1. Pasa el cursor sobre la tarjeta del modelo y haz clic en **Información del modelo**.
  2. Selecciona un nuevo **Tipo de modelo**.



Eliminar un modelo lo quita de la **Biblioteca de modelos** de forma permanente. Un trabajo que todavía use el archivo falla con un error `Value not in list` en el nodo de carga.

Para eliminar el modelo:

  1. Pasa el cursor sobre la tarjeta del modelo, haz clic en **More** y luego en **Eliminar**.
  2. En **Delete this model?** , haz clic en **Eliminar**.



## Detener o eliminar tu despliegue

Un despliegue consume almacenamiento hasta que lo elimines, incluso mientras está detenido. Detén un despliegue para conservarlo más adelante sin ejecutar tareas. Elimínalo para dejar de pagar por él. Para abrir la página del despliegue:

  1. En la **barra lateral de Developer Platform** , haz clic en **Deploy**.
  2. En la sección **Deployments** , haz clic en el nombre del despliegue.

![Sección Deployments de la página Deploy, con el nombre de cada despliegue en la columna de la izquierda y su estado en la columna Status](https://mintcdn.com/dripart/oPsov_e3HUhk_xUX/images/development/deploy/deployments.jpg?fit=max&auto=format&n=oPsov_e3HUhk_xUX&q=85&s=deff6c47fd097f0e0ffe25a781b44c62) Para detener el despliegue:

  1. Haz clic en **Stop**.
  2. En el cuadro de diálogo **Stop deployment** , haz clic en **Stop**.

El estado muestra **Stopping** y luego **Stopped**. Para volver a ejecutar el despliegue:

  * Haz clic en **Start**.



Eliminar quita el despliegue y su historial de forma permanente. Tu Build y sus versiones se conservan, así que puedes volver a desplegar más adelante.

Para eliminar el despliegue:

  1. En un despliegue detenido, haz clic en **Delete**. En un despliegue en ejecución, abre el menú **More actions** y luego selecciona **Delete**.
  2. En el cuadro de diálogo **Delete deployment** , haz clic en **Delete**.

La próxima vez que abras el editor en este navegador, el editor ejecutará tus flujos de trabajo en Comfy Cloud.

## Próximos pasos

## Modelos de la biblioteca en solicitudes de API

Sube un modelo desde una terminal y selecciónalo en cada solicitud con `lora_name`.

## Inicio rápido de Comfy API

Llama a tu implementación desde tu propio código como un endpoint de autoescalado.

## Uso y límites

Consulta cómo funcionan los créditos de Comfy Cloud y los límites de tareas simultáneas.

## Formato de API de flujo de trabajo

Exporta un flujo de trabajo en el formato que envían las solicitudes de API.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/deploy/cloud-custom-builds.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/deploy/cloud-custom-builds)

[Uso y límites](https://docs.comfy.org/es/development/deploy/cloud-usage)[Opciones de alojamiento](https://docs.comfy.org/es/development/deploy/self-hosting)
