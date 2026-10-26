---
url: https://docs.comfy.org/es/comfy-cli/getting-started/
title: Empezar con Comfy CLI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:48.947581+00:00
---

# Empezar con Comfy CLI - ComfyUI

> Source: https://docs.comfy.org/es/comfy-cli/getting-started/

## En esta página

Volver arriba

  * Descripción general
  * Instalar la CLI
  * Configuración rápida (recomendado)
  * Instalar ComfyUI (local)
  * Ejecutar ComfyUI (local)
  * Comfy Cloud
  * Generar con nodos asociados
    * Requisitos previos
    * Primera generación
    * Modelos comunes
    * Descubrir modelos
    * Edición de imágenes con referencias
    * Generación de video (tareas asíncronas)
    * Salida JSON para scripts
  * Ejecutar flujos de trabajo
  * Comenzar desde una plantilla
  * Editar flujos de trabajo en su lugar
  * Descubrir nodos y modelos
  * Subir y descargar archivos
  * Administrar nodos personalizados
  * Administrar modelos (local)
  * Salida JSON para scripts y agentes
  * Habilidades de agente
  * Contribuir
  * Analítica



Comfy CLI

# Empezar con Comfy CLI

Copiar páginaCopiar página

Instala comfy-cli, configura el enrutamiento local o en la nube, genera con Nodos asociados y ejecuta flujos de trabajo desde la terminal.

Copiar páginaCopiar página

## 

​

Descripción general

`comfy-cli` es una [herramienta de línea de comandos](https://github.com/Comfy-Org/comfy-cli) que simplifica la instalación y la administración de Comfy y te da acceso programable con un solo comando a todo el ecosistema de ComfyUI, ya sea de forma local o en la nube. Cumple tres funciones principales:

  1. **Administrar una instalación local de ComfyUI** : instalar, iniciar, actualizar, crear instantáneas y bisecar ComfyUI y los Nodos personalizados.
  2. **Acceder a los Nodos asociados alojados** : generar imágenes, video, audio y 3D con proveedores como Seedance, Nano Banana (Gemini), Grok, Flux, Ideogram, DALL·E, Recraft, Stability, Kling, Luma, Runway, Pika, Vidu, Hailuo, Moonvalley y otros, con un solo comando.
  3. **Ejecutar flujos de trabajo completos en Comfy Cloud** : enviar grafos de flujo de trabajo, explorar la galería de plantillas seleccionadas, editar los slots de los flujos de trabajo y seguir las tareas hasta que terminen, sin necesidad de una GPU local.



**Dos superficies, una CLI.** Cada comando detecta automáticamente dónde ejecutarse. Si tienes la sesión iniciada en Comfy Cloud, los comandos se dirigen a la **nube** ; de lo contrario, se ejecutan en tu **servidor** local. Puedes sobrescribirlo en cada llamada con `--where local|cloud`, la variable de entorno `COMFY_WHERE`, o persistirlo con `comfy set-default --where cloud`.

## 

​

Instalar la CLI

pip

homebrew
    
    
    pip install comfy-cli
    
    
    
    brew tap Comfy-Org/comfy-cli
    brew install comfy-org/comfy-cli/comfy-cli
    

Para obtener sugerencias de autocompletado en la shell:
    
    
    comfy --install-completion
    

## 

​

Configuración rápida (recomendado)

Novedad en las versiones recientes: un único asistente interactivo que se encarga del enrutamiento, la autenticación y las habilidades del agente en un solo paso.
    
    
    comfy setup
    

Te guía para elegir un objetivo de enrutamiento (local o nube), **iniciar sesión a través de tu navegador (OAuth)** , seleccionar un directorio de proyecto e, opcionalmente, instalar las habilidades del agente. Esta es la ruta RECOMENDADA. Abre el inicio de sesión en el navegador por ti, sin claves que copiar.
    
    
    comfy setup --where cloud
    

**No interactivo (solo CI).** El OAuth del navegador necesita una sesión interactiva. Para CI, devcontainers e instalaciones por script en las que no hay navegador disponible, pasa una Clave API en su lugar:
    
    
    comfy setup --where cloud --api-key comfyui-... --non-interactive
    

Flag| Propósito  
---|---  
`--where local|cloud`| Objetivo de enrutamiento; omite la pregunta  
`--project-dir`| Directorio para flujos de trabajo, entradas y salidas  
`--api-key`|  _(Opcional)_ Clave API de Comfy Cloud para entornos sin interfaz/CI; implica `--where cloud`  
`-y, --non-interactive`| Sin preguntas. Controla todo desde los flags  
`--skip-skills`| No Instalar las habilidades del agente  
`--skip-verify`| Saltar la comprobación de conectividad  
  
## 

​

Instalar ComfyUI (local)

Crea un entorno virtual con Python 3.10 o superior.

conda

venv
    
    
    conda create -n comfy-env python=3.11
    conda activate comfy-env
    
    
    
    python3 -m venv comfy-env
    source comfy-env/bin/activate
    

Instala ComfyUI
    
    
    comfy install
    

`comfy install` pregunta qué GPU tienes e instala la compilación de PyTorch correspondiente. Responde a la pregunta o pasa un indicador de GPU para instalaciones desatendidas:

Plataforma| Qué instala `comfy install`| Qué necesitas además  
---|---|---  
NVIDIA| PyTorch con runtime de CUDA (rueda de pip)| Un controlador de GPU actual (no el CUDA Toolkit completo)  
AMD Linux| Ruedas de PyTorch para ROCm| Un controlador o stack de AMD compatible con ROCm para esas ruedas  
AMD Windows| `torch-directml`| Una GPU AMD compatible (DirectML; no ROCm)  
Apple silicon| Ruedas nocturnas de PyTorch (índice de CPU; Metal/MPS)| macOS en Apple silicon  
Intel Arc| Ruedas de PyTorch para XPU| Una GPU Intel Arc o un stack XPU compatible  
CPU| Ruedas de PyTorch para CPU| No se requiere una GPU dedicada  
  
## 

​

Ejecutar ComfyUI (local)
    
    
    comfy launch
    

Ejecútalo en segundo plano y detenlo más tarde:
    
    
    comfy launch --background
    comfy stop
    

Comprueba qué espacio de trabajo está seleccionado y qué está instalado:
    
    
    comfy which
    comfy env
    

## 

​

Comfy Cloud

Ejecuta flujos de trabajo y nodos asociados en las GPUs alojadas de Comfy. No se requiere instalación local.
    
    
    comfy cloud login          # OAuth del navegador + PKCE
    comfy cloud whoami         # muestra el estado de sesión, el método de autenticación y la URL base
    comfy cloud logout         # limpia la sesión local
    

Una vez que inicias sesión, los comandos se enrutan automáticamente a la nube. **OAuth del navegador es el método RECOMENDADO.** No hay claves que administrar y la CLI se encarga de actualizar el token por ti. Para apuntar a un entorno personalizado (por ejemplo, una VISTA PREVIA de un PR) antes de iniciar sesión:
    
    
    comfy cloud set-base-url https://my-preview.comfy.org
    

**La clave API es opcional.** Solo necesitas una clave API para uso sin interfaz o en CI, donde no es posible iniciar sesión desde el navegador. Es una alternativa, no la opción predeterminada:
    
    
    export COMFY_API_KEY=comfyui-...   # o pasa --api-key en cada llamada
    

**Duración de la sesión.** Los tokens de sesión de la nube son de corta duración (~1 h). La CLI los actualiza automáticamente cuando es necesario. Si un comando informa `cloud_unauthorized`, ejecuta `comfy cloud login` de nuevo.

## 

​

Generar con nodos asociados

**`comfy generate` está en beta.** Los nombres de los flags, los alias de modelos y los formatos de salida pueden cambiar. Los endpoints de los socios subyacentes son estables. Envía tu retroalimentación en el [repositorio de GitHub de comfy-cli](https://github.com/Comfy-Org/comfy-cli/issues).

La forma más rápida de llamar a los [nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview) de Comfy desde una terminal o un script. Usa los mismos endpoints alojados que los flujos de trabajo de ComfyUI, pero como llamadas individuales de la CLI. Es ideal para trabajos por lotes, experimentos rápidos y automatización donde un gráfico completo de ComfyUI no es necesario.

### 

​

Requisitos previos

  * Una sesión de Comfy Cloud activa mediante `comfy cloud login` (OAuth en el navegador), **o** una [Clave API de Comfy](https://docs.comfy.org/es/development/api-development/getting-an-api-key) (`--api-key` / `COMFY_API_KEY`) para uso sin interfaz o en CI
  * [Créditos](https://docs.comfy.org/es/interface/credits) en tu cuenta
  * _Opcional:_ [Explora los nodos asociados y el precio por llamada](https://docs.comfy.org/es/tutorials/partner-nodes/pricing)



### 

​

Primera generación
    
    
    comfy generate flux-pro \
        --prompt "a cat on the moon, cinematic lighting" \
        --width 1024 --height 1024 \
        --download cat.png
    

La CLI sube los archivos locales, envía la tarea, consulta su estado hasta que finaliza y guarda los resultados.

Descubre primero los parámetros reales de un modelo. Los nombres de las flags varían según el modelo (por ejemplo, `flux-ultra` acepta `--width`/`--height`; `seedance` acepta `--ratio`/`--resolution`/`--duration`). Verifica siempre antes de crear un script:
    
    
    comfy generate schema flux-ultra
    

### 

​

Modelos comunes

**Nano Banana (Google Gemini): texto a imagen y edición:**
    
    
    comfy generate nano-banana \
        --prompt "a watercolor of a sleeping fox" \
        --download fox.png
    
    # Edición de imagen:
    comfy generate nano-banana \
        --prompt "add a top hat" \
        --image ./cat.png \
        --download edited.png
    
    # Especificar una variante de modelo:
    comfy generate nano-banana \
        --prompt "neon city skyline" \
        --model gemini-3-pro-image-preview \
        --download city.png
    

**FLUX 1.1 Pro Ultra: texto a imagen de alta resolución:**
    
    
    comfy generate flux-ultra \
        --prompt "a purple Victorian house in San Francisco, golden hour" \
        --width 896 --height 1152 --seed 11 \
        --download house.png
    

**Seedance (ByteDance): texto a video e imagen a video, hasta 1080p / 12s:**
    
    
    # Texto a video:
    comfy generate seedance \
        --prompt "a hummingbird hovering over a flower" \
        --resolution 1080p --duration 5 \
        --download hummingbird.mp4
    
    # Imagen a video (anima una imagen local, se sube automáticamente):
    comfy generate seedance \
        --model seedance-1-0-pro-250528 \
        --image ./painting.png \
        --ratio 3:4 --resolution 1080p --duration 5 \
        --prompt "the painting gently comes alive, a soft breeze stirs the trees" \
        --download animated.mp4
    

**Grok (xAI): imágenes y video:**
    
    
    comfy generate grok --prompt "a cyberpunk street market at night" --download street.png
    comfy generate grok-edit --prompt "swap the umbrella for a parasol" --image ./photo.jpg --download out.png
    comfy generate grok-video --prompt "a paper plane gliding through a cathedral" --download flight.mp4
    

### 

​

Descubrir modelos
    
    
    comfy generate list                            # todos los modelos
    comfy generate list --category text-to-video   # filtrar por categoría
    comfy generate list --partner kling            # filtrar por socio
    comfy generate schema flux-kontext             # ver los parámetros de un modelo
    

### 

​

Edición de imágenes con referencias

Pasa rutas de archivos locales. La CLI sube los archivos mediante el endpoint de almacenamiento de Comfy o los codifica en base64 según sea necesario:
    
    
    comfy generate nano-banana \
        --prompt "add a top hat" \
        --image ./cat.png \
        --download edited.png
    
    comfy generate flux-kontext \
        --prompt "add a top hat and a monocle" \
        --input_image ./photo.jpg \
        --download out.png
    
    comfy generate ideogram-edit \
        --image cat.png --mask mask.png \
        --prompt "add sunglasses" \
        --rendering_speed TURBO \
        --download edited.png
    

Para subir una vez y reutilizar en varias llamadas:
    
    
    comfy generate upload ./photo.jpg     # imprime una URL firmada
    

Los recursos de referencia que subes se eliminan automáticamente después de **24 horas**. Se almacenan en GCS administrado por Comfy con URLs firmadas. Para pipelines de larga duración, vuelve a subirlos antes de cada tarea. Consulta la [Referencia](https://docs.comfy.org/es/comfy-cli/reference) para más detalles.

### 

​

Generación de video (tareas asíncronas)

Los trabajos de video son asíncronos. La CLI bloquea y consulta el estado por defecto:
    
    
    comfy generate seedance \
        --prompt "a hummingbird hovering over a flower" \
        --resolution 1080p --duration 5 \
        --download hummingbird.mp4
    
    comfy generate kling \
        --prompt "a paper boat drifting on a river at dusk" \
        --duration 5 \
        --download boat.mp4
    

Regresa de inmediato con `--async` y continúa después:
    
    
    comfy generate luma --prompt "neon koi swimming through clouds" --aspect_ratio 16:9 --async
    # imprime un id de trabajo; continúa con:
    comfy generate resume luma <job_id> --download out.mp4
    

### 

​

Salida JSON para scripts

Emite las respuestas sin procesar de la API para integrarlas en pipelines:
    
    
    comfy generate dalle --prompt "a watercolor whale" --json | jq '.data[0].url'
    

Consulta la [referencia](https://docs.comfy.org/es/comfy-cli/reference) para ver la lista completa de comandos, flags y alias de modelos.

## 

​

Ejecutar flujos de trabajo

Más allá de las llamadas individuales a socios, `comfy run` envía un gráfico de flujo de trabajo completo de ComfyUI. Acepta JSON tanto en formato API como en formato UI exportado (los flujos de trabajo de UI se convierten a formato API en el lado del cliente) y enruta a local o a la nube como cualquier otro comando. Es **asíncrono de forma predeterminada**. Devuelve un `prompt_id` en milisegundos mientras un proceso de vigilancia en segundo plano sigue el progreso. Usa `--wait` si prefieres bloquear.
    
    
    # Envía; devuelve de inmediato un prompt_id
    RES=$(comfy --json run --workflow my_workflow.json)
    PROMPT_ID=$(echo "$RES" | jq -r .data.prompt_id)
    
    # Vigila hasta el estado terminal y luego recopila las salidas
    comfy --json jobs watch "$PROMPT_ID" | comfy download
    

¿Prefieres una sola llamada bloqueante? Usa `--wait`:
    
    
    comfy run --workflow my_workflow.json --wait | comfy download
    

Sigue y administra las tareas:
    
    
    comfy jobs ls                 # envíos asíncronos locales + cola/historial del servidor
    comfy jobs status <prompt_id> # una sola tarea
    comfy jobs wait <id1> <id2>   # bloquea hasta que TODAS lleguen a un estado terminal
    comfy jobs cancel <prompt_id> # idempotente
    

Valida antes de enviar. Detecta nodos desconocidos, modelos faltantes y conexiones incorrectas antes de consumir cómputo en la nube:
    
    
    comfy validate --workflow my_workflow.json
    

## 

​

Comenzar desde una plantilla

La galería curada `Comfy-Org/workflow_templates` es la forma más rápida de obtener un flujo de trabajo que ya funciona para una tarea determinada. No necesitas construirlo desde cero.
    
    
    comfy templates ls --type image --tag "Text to Image"   # explorar
    comfy templates show <name>                              # metadatos completos
    comfy templates fetch <name> --out my.json               # obtén el JSON del flujo de trabajo
    

El JSON descargado está en formato del frontend. `comfy run --where cloud` lo convierte automáticamente a formato API al enviarlo.

## 

​

Editar flujos de trabajo en su lugar

`comfy workflow` expone los slots editables por el agente en cualquier flujo de trabajo en formato frontend y te permite sobrescribirlos. Sin cirugía manual de JSON.
    
    
    comfy workflow slots my.json                 # list addressable slots
    comfy workflow set-slot my.json 6.text="a fox in the snow"
    comfy workflow vary my.json \
        --slot positive.text='["a cat","a dog","a fox"]' \
        --out-dir ./variants                     # fan out N variants
    

Flujos de trabajo guardados en Comfy Cloud:
    
    
    comfy workflow list                          # your saved workflows
    comfy workflow get <id> --out my.json
    comfy workflow save my.json --name "My Flow"
    comfy workflow delete <id>
    

Para canalizaciones complejas de varios pasos, combina fragmentos pequeños y reutilizables en un solo gráfico:
    
    
    comfy workflow compose blueprints/my_pipeline.yaml -o workflows/my_pipeline.json
    comfy workflow decompose my.json             # inverse: project a workflow into a fragment
    

## 

​

Descubrir nodos y modelos

Inspecciona todo lo que esté disponible en el backend resuelto. **Nodos:**
    
    
    comfy nodes search "checkpoint"              # fuzzy search
    comfy nodes show KSampler                    # full schema: inputs, outputs, defaults
    comfy nodes ls --produces IMAGE --limit 10   # filter by output type
    comfy nodes ls --api-only                    # partner-API nodes only
    

**Modelos:**
    
    
    comfy models list-folders                    # every model folder
    comfy models search --text "wan2.2" --type lora
    comfy models show wan2.2_vae.safetensors     # full metadata
    

## 

​

Subir y descargar archivos
    
    
    comfy upload photo.png video.mp4             # → directorio de entrada del servidor
    comfy download <prompt_id>                   # → ./outputs/
    

**La tubería idiomática:**
    
    
     comfy run --workflow flux.json --wait | comfy download
    

`comfy download` lee el prompt_id y las URLs de salida desde el stdin canalizado de forma automática. Sin extracción manual de claves, sin `jq`.

## 

​

Administrar nodos personalizados
    
    
    comfy node install <NODE_NAME>
    

La herramienta usa `cm-cli` para instalar nodos personalizados. Consulta la [documentación de cm-cli de ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/docs/en/cm-cli.md) para más detalles.

## 

​

Administrar modelos (local)

Descarga modelos fácilmente:
    
    
    comfy model download --url <url> --relative-path models/checkpoints
    

## 

​

Salida JSON para scripts y agentes

Todos los comandos aceptan `--json` y emiten la misma estructura de envoltura, lo que hace que la CLI se pueda usar por completo en scripts y sea cómoda para los agentes:
    
    
    {
      "ok": true,
      "command": "...",
      "version": "1.11.1",
      "where": "local | cloud | null",
      "data": { },
      "error": null
    }
    

Cuando `error` está presente, lee el `hint` y actúa en consecuencia:
    
    
    comfy --json run --workflow my.json | jq '.error.hint'
    

La superficie orientada a agentes se describe a sí misma por completo. Vuelca todo el árbol de comandos, los esquemas de salida y los códigos de error:
    
    
    comfy --json discover
    

## 

​

Habilidades de agente

Instala en Claude Code, Cursor y cualquier herramienta compatible con AGENTS.md las habilidades del agente incluidas con Comfy, para que tu agente de programación pueda controlar la CLI directamente:
    
    
    comfy skills install
    comfy skills list      # comfy, comfy-fragments, comfy-debug, comfy-relay, comfy-director
    comfy skills status    # qué está instalado y dónde
    

Estas son **habilidades CLI incluidas** que se instalan con `comfy skills install`. Son independientes del repositorio [Comfy Skills](https://github.com/Comfy-Org/comfy-skills/), que aloja el plugin **comfy-cloud** de Claude Code para [Comfy Cloud MCP](https://docs.comfy.org/es/agent-tools/mcp).

## 

​

Contribuir

Las contribuciones son bienvenidas. Abre un problema o envía un pull request en el [repositorio de GitHub de comfy-cli](https://github.com/Comfy-Org/comfy-cli/issues). Consulta la [Guía para desarrolladores](https://github.com/Comfy-Org/comfy-cli/blob/main/CONTRIBUTING.md) para más detalles.

## 

​

Analítica

El seguimiento de uso ayuda a mejorar la CLI. Desactívalo con:
    
    
    comfy tracking disable
    

Vuelve a activar el seguimiento:
    
    
    comfy tracking enable
    

También puedes optar por desactivarlo de forma definitiva mediante las variables de entorno `DO_NOT_TRACK` o `COMFY_NO_TELEMETRY`.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/comfy-cli/getting-started.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/comfy-cli/getting-started)

[Get workspace usage over time](https://docs.comfy.org/es/api-reference/cloud/billing/get-workspace-usage-over-time)[Referencia de comandos](https://docs.comfy.org/es/comfy-cli/reference)
