---
url: https://docs.comfy.org/es/comfy-cli/reference/
title: Referencia de comandos de Comfy CLI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:49.490077+00:00
---

# Referencia de comandos de Comfy CLI - ComfyUI

> Source: https://docs.comfy.org/es/comfy-cli/reference/

## En esta página

Volver arriba

  * CLI
  * Generar (nodos asociados): Beta
    * list
    * schema
    * refresh
    * upload
    * resume
    * Alias de modelos (seleccionados)
  * Nodos
    * deps-in-workflow
    * disable
    * enable
    * fix
    * install
    * install-deps
    * reinstall
    * restore-dependencies
    * restore-snapshot
    * save-snapshot
    * show
    * simple-show
    * uninstall
    * update
  * Modelos
    * download
    * list
    * remove



Comfy CLI

# Referencia de comandos de Comfy CLI

Copiar páginaCopiar página

Referencia completa de Comfy CLI: comandos de instalación, gestión de nodos y descargas de modelos para configurar y administrar ComfyUI desde la terminal.

Copiar páginaCopiar página

# 

​

CLI

## 

​

Generar (nodos asociados): Beta

**`comfy generate` está en beta.** Los nombres de las opciones, los alias de modelos y los formatos de salida pueden cambiar. Los endpoints de los nodos asociados subyacentes son estables; la interfaz de la CLI todavía está evolucionando. Envía tu retroalimentación en el [repositorio de comfy-cli en GitHub](https://github.com/Comfy-Org/comfy-cli/issues).

**Uso** :
    
    
    $ comfy generate [OPTIONS] <MODEL_OR_ACTION> [--<param> value]...
    

`<MODEL_OR_ACTION>` es una de las siguientes opciones:

  * Un **alias de modelo** (p. ej. `flux-pro`, `ideogram-edit`, `kling`, `dalle`): llama directamente a ese modelo de socio.
  * Una **acción reservada** : `list`, `schema`, `refresh`, `upload`, `resume`.

Cualquier cosa que no esté en el conjunto reservado se trata como un alias de modelo y la solicitud se envía a ese endpoint del socio. **Autenticación** : Configura la variable de entorno `COMFY_API_KEY` o pasa `--api-key <KEY>` en cada llamada. Obtén una clave en [platform.comfy.org](https://platform.comfy.org). **Opciones de nivel de ejecución** (funcionan con cualquier modelo):

  * `--download PATH`: Guarda la imagen/video del resultado en `PATH`.
  * `--async`: Envía y devuelve un ID de trabajo de inmediato en lugar de sondear hasta que termine. Reanúdalo más tarde con `comfy generate resume <model> <job_id>`.
  * `--json`: Emite la respuesta sin procesar de la API como JSON (útil para scripting).
  * `--timeout SECONDS`: Anula el tiempo de espera de sondeo predeterminado de 300 s.
  * `--api-key KEY`: Clave API en línea (anula `COMFY_API_KEY`).

**Ejemplos** :
    
    
    comfy generate flux-pro --prompt "a cat on the moon" --width 1024 --height 1024 --download cat.png
    comfy generate ideogram-edit --image cat.png --mask m.png --prompt "add sunglasses" --rendering_speed TURBO
    comfy generate kling --prompt "a paper boat drifting at dusk" --duration 5 --download boat.mp4
    

### 

​

`list`

Lista los modelos de socios disponibles con sus alias cortos. **Uso** :
    
    
    $ comfy generate list [OPTIONS]
    

**Opciones** :

  * `--partner TEXT` / `-p TEXT`: Filtrar por socio (p. ej. `bfl`, `kling`, `ideogram`, `openai`).
  * `--category TEXT` / `--style TEXT` / `-c TEXT`: Filtrar por categoría (p. ej. `text-to-image`, `image-edit`, `inpaint`, `upscale`, `text-to-video`, `image-to-video`).
  * `--query TEXT` / `-q TEXT`: Coincidencia de subcadena con el id/resumen del modelo.



### 

​

`schema`

Muestra los parámetros de un modelo específico, incluidos los indicadores requeridos/opcionales, los tipos, los valores predeterminados y un ejemplo de invocación. **Uso** :
    
    
    $ comfy generate schema <MODEL>
    

**Ejemplo** :
    
    
    comfy generate schema flux-pro
    comfy generate schema kling-i2v
    

### 

​

`refresh`

Actualiza el catálogo local de modelos en caché a partir de la especificación OpenAPI de la nube. Es útil cuando se agregan nuevos modelos de socios. **Uso** :
    
    
    $ comfy generate refresh
    

### 

​

`upload`

Sube un archivo local (o reubica una URL remota) al almacenamiento de Comfy e imprime la URL firmada. La mayoría de los modelos aceptan rutas de archivo locales directamente; esto es para los casos en que quieres la URL de forma explícita (p. ej., para reutilizar el mismo recurso en varias llamadas). **Uso** :
    
    
    $ comfy generate upload <FILE_OR_URL> [--json]
    

**Ejemplo** :
    
    
    comfy generate upload ./photo.jpg
    comfy generate upload ./photo.jpg --json
    

**Los recursos de referencia se eliminan automáticamente después de 24 horas.** Los archivos subidos (ya sea mediante `comfy generate upload` o de forma implícita cuando pasas una ruta de archivo local a un modelo) se almacenan en un bucket GCS administrado por Comfy (`api-nodes-prod`) y solo son accesibles mediante una URL firmada. Los objetos se eliminan automáticamente **1 día después de la subida** por una regla de ciclo de vida del bucket. Si necesitas que un recurso persista en tareas asíncronas de larga duración, vuelve a subirlo antes de cada tarea, o alójalo tú mismo y pasa la URL directamente.

### 

​

`resume`

Reanuda una tarea asíncrona enviada anteriormente (normalmente una tarea de video enviada con `--async`). Sondea hasta que el resultado esté listo y, opcionalmente, lo descarga. **Uso** :
    
    
    $ comfy generate resume <MODEL> <JOB_ID> [--download PATH] [--json]
    

**Ejemplo** :
    
    
    comfy generate resume luma 7c3f9e2a --download out.mp4
    

### 

​

Alias de modelos (seleccionados)

Los siguientes alias cortos se aceptan como `<MODEL>`. Ejecuta `comfy generate list` para ver el catálogo completo y actualizado. **Populares** :

Alias| Socio| Categoría  
---|---|---  
`nano-banana`| Google (Gemini Flash Image)| text-to-image / image-edit  
`seedance`| ByteDance| text-to-video / image-to-video (async)  
`grok`, `grok-edit`| xAI| text-to-image / image-edit  
`grok-video`| xAI| text-to-video (async)  
  
**Todo lo demás** :

Alias| Socio| Categoría  
---|---|---  
`flux-pro`, `flux-ultra`, `flux-2`| BFL| text-to-image (async)  
`flux-kontext`, `flux-kontext-max`| BFL| image-edit (async)  
`flux-fill`, `flux-expand`, `flux-canny`, `flux-depth`| BFL| inpaint / outpaint / controlnet  
`ideogram`, `ideogram-edit`, `ideogram-remix`, `ideogram-reframe`, `ideogram-bg`| Ideogram| text-to-image / image-edit  
`dalle`, `dalle-edit`| OpenAI| text-to-image / image-edit  
`stability-ultra`, `stability-sd3`, `stability-upscale`, `stability-upscale-creative`, `stability-upscale-fast`| Stability| text-to-image / upscale  
`recraft`, `recraft-vectorize`, `recraft-rmbg`, `recraft-replace-bg`, `recraft-i2i`, `recraft-inpaint`, `recraft-upscale`, `recraft-upscale-creative`| Recraft| text-to-image / image-edit  
`reve`, `reve-edit`| Reve| text-to-image / image-edit  
`runway`| Runway| text-to-image  
`kling`, `kling-i2v`, `kling-extend`, `kling-lipsync`| Kling| text-to-video / image-to-video / video-extend / lipsync (async)  
`luma`, `luma-i2v`| Luma| text-to-video / image-to-video (async)  
`hailuo`| MiniMax| text-to-video (async)  
`runway-i2v`| Runway| image-to-video (async)  
`moonvalley-t2v`, `moonvalley-i2v`| Moonvalley| text-to-video / image-to-video (async)  
`pika`, `pika-i2v`| Pika| text-to-video / image-to-video (async)  
`vidu`, `vidu-i2v`, `vidu-extend`| Vidu| text-to-video / image-to-video / video-extend (async)  
  
## 

​

Nodos

**Uso** :
    
    
    $ comfy node [OPTIONS] COMMAND [ARGS]...
    

**Opciones** :

  * `--install-completion`: Instala el autocompletado para la shell actual.
  * `--show-completion`: Muestra el autocompletado para la shell actual, para copiarlo o personalizar la instalación.
  * `--help`: Muestra este mensaje y sale.

**Comandos** :

  * `deps-in-workflow`
  * `disable`
  * `enable`
  * `fix`
  * `install`
  * `install-deps`
  * `reinstall`
  * `restore-dependencies`
  * `restore-snapshot`
  * `save-snapshot`: Guarda una instantánea del entorno actual de ComfyUI…
  * `show`
  * `simple-show`
  * `uninstall`
  * `update`



### 

​

`deps-in-workflow`

**Uso** :
    
    
    $ deps-in-workflow [OPTIONS]
    

**Opciones** :

  * `--workflow TEXT`: archivo de flujo de trabajo (.json/.png) [requerido]
  * `--output TEXT`: archivo de flujo de trabajo (.json/.png) [requerido]
  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`disable`

**Uso** :
    
    
    $ disable [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: deshabilita los nodos personalizados [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`enable`

**Uso** :
    
    
    $ enable [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: habilita los nodos personalizados [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`fix`

**Uso** :
    
    
    $ fix [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: corrige las dependencias de los nodos personalizados especificados [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`install`

**Uso** :
    
    
    $ install [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: instala los nodos personalizados [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`install-deps`

**Uso** :
    
    
    $ install-deps [OPTIONS]
    

**Opciones** :

  * `--deps TEXT`: archivo de especificación de dependencias (.json)
  * `--workflow TEXT`: archivo de flujo de trabajo (.json/.png)
  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`reinstall`

**Uso** :
    
    
    $ reinstall [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: reinstala los nodos personalizados [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`restore-dependencies`

**Uso** :
    
    
    $ restore-dependencies [OPTIONS]
    

**Opciones** :

  * `--help`: Muestra este mensaje y sale.



### 

​

`restore-snapshot`

**Uso** :
    
    
    $ restore-snapshot [OPTIONS] PATH
    

**Argumentos** :

  * `PATH`: [requerido]

**Opciones** :

  * `--help`: Muestra este mensaje y sale.



### 

​

`save-snapshot`

Guarda una instantánea del entorno actual de ComfyUI **Uso** :
    
    
    $ save-snapshot [OPTIONS]
    

**Opciones** :

  * `--output TEXT`: Especifica la ruta del archivo de salida. (.json/.yaml)
  * `--help`: Muestra este mensaje y sale.



### 

​

`show`

**Uso** :
    
    
    $ show [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: [installed|enabled|not-installed|disabled|all|snapshot|snapshot-list] [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`simple-show`

**Uso** :
    
    
    $ simple-show [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: [installed|enabled|not-installed|disabled|all|snapshot|snapshot-list] [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`uninstall`

**Uso** :
    
    
    $ uninstall [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: desinstala los nodos personalizados [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



### 

​

`update`

**Uso** :
    
    
    $ update [OPTIONS] ARGS...
    

**Argumentos** :

  * `ARGS...`: actualiza los nodos personalizados [requerido]

**Opciones** :

  * `--channel TEXT`: Especifica el modo de operación
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Muestra este mensaje y sale.



## 

​

Modelos

**Uso** :
    
    
    $ comfy model [OPTIONS] COMMAND [ARGS]...
    

**Opciones** :

  * `--install-completion`: Instala el autocompletado para la shell actual.
  * `--show-completion`: Muestra el autocompletado para la shell actual, para copiarlo o personalizar la instalación.
  * `--help`: Muestra este mensaje y sale.

**Comandos** :

  * `download`: Descarga un modelo en una ruta relativa especificada…
  * `list`: Muestra una lista de todos los modelos descargados actualmente…
  * `remove`: Elimina uno o más modelos descargados,…



### 

​

`download`

Descarga un modelo en una ruta relativa especificada si aún no está descargado. **Uso** :
    
    
    $ download [OPTIONS]
    

**Opciones** :

  * `--url TEXT`: La URL desde la cual descargar el modelo [Requerido]
  * `--relative-path TEXT`: La ruta relativa desde el espacio de trabajo actual donde instalar el modelo. [predeterminado: models/checkpoints]
  * `--help`: Muestra este mensaje y sale.



### 

​

`list`

Muestra una lista de todos los modelos descargados actualmente en formato de tabla. **Uso** :
    
    
    $ list [OPTIONS]
    

**Opciones** :

  * `--relative-path TEXT`: La ruta relativa desde el espacio de trabajo actual donde se almacenan los modelos. [predeterminado: models/checkpoints]
  * `--help`: Muestra este mensaje y sale.



### 

​

`remove`

Elimina uno o más modelos descargados, ya sea especificándolos directamente o mediante una selección interactiva. **Uso** :
    
    
    $ remove [OPTIONS]
    

**Opciones** :

  * `--relative-path TEXT`: La ruta relativa desde el espacio de trabajo actual donde se almacenan los modelos. [predeterminado: models/checkpoints]
  * `--model-names TEXT`: Lista de nombres de archivo de modelos a eliminar, separados por espacios
  * `--help`: Muestra este mensaje y sale.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/comfy-cli/reference.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/comfy-cli/reference)

[Empezar](https://docs.comfy.org/es/comfy-cli/getting-started)[Solución de problemas](https://docs.comfy.org/es/comfy-cli/troubleshooting)
