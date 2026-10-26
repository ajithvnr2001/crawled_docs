---
url: https://docs.comfy.org/es/agent-tools/cli/
title: Comfy CLI: ejecuta ComfyUI desde la terminal - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:22.045854+00:00
---

# Comfy CLI: ejecuta ComfyUI desde la terminal - ComfyUI

> Source: https://docs.comfy.org/es/agent-tools/cli/

## En esta página

Volver arriba

  * Cómo encaja con MCP
  * Qué hace el CLI
  * Instalar y configurar
  * Requisitos previos para comfy generate
  * Tu primera generación
  * Modelos disponibles
  * Ejemplos de uso
    * Texto a imagen
    * Edición de imagen (imagen de referencia)
    * Texto a video
    * Scripts con JSON
  * Más allá de comfy generate
  * Habilidades del agente
  * Recursos relacionados
  * Retroalimentación



# Comfy CLI: ejecuta ComfyUI desde la terminal

Copiar páginaCopiar página

Controla Comfy desde la terminal: ComfyUI local, llamadas de generación de socios y flujos de trabajo completos en Comfy Cloud. Complementa MCP para scripts, CI y automatización.

Copiar páginaCopiar página

[comfy-cli](https://github.com/Comfy-Org/comfy-cli) es la herramienta de línea de comandos de Comfy. Junto con los [servidores MCP](https://docs.comfy.org/es/agent-tools), ofrece a los agentes y a los desarrolladores otra forma de controlar Comfy desde fuera de la interfaz. Úsala para el **acceso desde terminal o scripts** : tareas por lotes, pipelines de CI, automatización de flujos de trabajo y uso combinado con agentes de programación mediante las habilidades incluidas en la CLI.

**Referencia rápida para agentes.** Esta página es un resumen breve: lo suficiente para orientarte junto con MCP y ejecutar las llamadas habituales de `comfy generate`. Para la **documentación completa de la CLI** (instalación local, `comfy setup`, `comfy run`, plantillas, edición de flujos de trabajo, descubrimiento de nodos y modelos, y más), consulta [Primeros pasos con Comfy CLI](https://docs.comfy.org/es/comfy-cli/getting-started).

**`comfy generate` está en beta.** Los nombres de los flags, los alias de modelos y los formatos de salida pueden cambiar. Los endpoints de los socios subyacentes son estables. Envía tu retroalimentación en el [repositorio de GitHub de comfy-cli](https://github.com/Comfy-Org/comfy-cli/issues).

## 

​

Cómo encaja con MCP

| Comfy MCP (cloud)| Comfy CLI  
---|---|---  
**Interfaz**|  Chat con un cliente MCP (Claude Code, Claude Desktop, …)| Comandos de terminal y scripts  
**Ideal para**|  Flujos de trabajo interactivos con agentes en el chat| Automatización, ejecuciones por lote, CI, canalizaciones de shell  
**Autenticación**|  OAuth en clientes MCP, o clave API (sin interfaz)| `comfy cloud login` (OAuth) o clave API (CI)  
**Salida**|  Devuelta en la sesión de chat| Guardada en disco (`--download`) o en JSON (`--json`)  
  
Para la configuración de MCP, la instalación, las listas de herramientas y los métodos de autenticación, consulta [Comfy MCP](https://docs.comfy.org/es/agent-tools/mcp).

## 

​

Qué hace el CLI

  1. **ComfyUI local** : instala, inicia, actualiza y administra nodos personalizados
  2. **Generación con socios** : `comfy generate` para llamadas puntuales a la API de socios de imagen, video, audio y 3D
  3. **Flujos de trabajo en la nube** : `comfy run`, plantillas, edición de slots y seguimiento de tareas en Comfy Cloud



**Dos superficies, una CLI.** Cada comando detecta automáticamente dónde ejecutarse. Si tienes la sesión iniciada en Comfy Cloud, los comandos se dirigen a la **nube** ; de lo contrario, se ejecutan en tu **servidor** local. Puedes sobrescribirlo en cada llamada con `--where local|cloud`, la variable de entorno `COMFY_WHERE`, o persistirlo con `comfy set-default --where cloud`.

## 

​

Instalar y configurar

pip

homebrew
    
    
    pip install comfy-cli
    
    
    
    brew tap Comfy-Org/comfy-cli
    brew install comfy-org/comfy-cli/comfy-cli
    

Para obtener sugerencias de autocompletado en la shell:
    
    
    comfy --install-completion
    
    
    
    comfy setup
    

Pasa `-y` para instalaciones no interactivas en CI o scripts. Consulta [Primeros pasos con Comfy CLI](https://docs.comfy.org/es/comfy-cli/getting-started#configuraci%C3%B3n-r%C3%A1pida-recomendado) para ver la tabla completa de flags de `comfy setup`. Inicia sesión en Comfy Cloud:
    
    
    comfy cloud login
    comfy cloud whoami
    

## 

​

Requisitos previos para `comfy generate`

  * Una sesión de Comfy Cloud activa mediante `comfy cloud login` (OAuth en el navegador), **o** una [Clave API de Comfy](https://docs.comfy.org/es/development/api-development/getting-an-api-key) (`--api-key` / `COMFY_API_KEY`) para uso sin interfaz o en CI
  * [Créditos](https://docs.comfy.org/es/interface/credits) en tu cuenta
  * _Opcional:_ [Explora los nodos asociados y el precio por llamada](https://docs.comfy.org/es/tutorials/partner-nodes/pricing)



## 

​

Tu primera generación
    
    
    comfy generate flux-pro \
        --prompt "a cat on the moon, cinematic lighting" \
        --width 1024 --height 1024 \
        --download cat.png
    

La CLI sube los archivos locales, envía la tarea, consulta su estado hasta que finaliza y guarda los resultados.

## 

​

Modelos disponibles

`comfy generate` abarca modelos de socios para imagen y video. Descubre qué hay disponible en tu versión de la CLI:
    
    
    comfy generate list                            # todos los modelos
    comfy generate list --category text-to-video   # filtrar por categoría
    comfy generate list --partner kling            # filtrar por socio
    comfy generate schema flux-kontext             # parámetros de un modelo
    

Los alias comunes incluyen:

Categoría| Ejemplos  
---|---  
**Imagen**| `flux-pro`, `flux-ultra`, `flux-kontext`, `nano-banana`, `grok`, `grok-edit`, `ideogram-edit`, `dalle`, `recraft`, `stability`  
**Video**| `seedance`, `kling`, `luma`, `runway`, `pika`, `vidu`, `hailuo`, `moonvalley`, `grok-video`  
  
Ejecuta `comfy generate list` para ver el conjunto completo en tu entorno.

## 

​

Ejemplos de uso

### 

​

Texto a imagen
    
    
    comfy generate nano-banana \
        --prompt "a watercolor of a sleeping fox" \
        --download fox.png
    

### 

​

Edición de imagen (imagen de referencia)

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

Texto a video

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

Scripts con JSON
    
    
    comfy generate dalle --prompt "a watercolor whale" --json | jq '.data[0].url'
    

## 

​

Más allá de `comfy generate`

Todo lo anterior es el resumen enfocado en agentes. La guía completa recorre cada comando en profundidad:

  * `comfy run`, `comfy jobs` y `comfy validate` para flujos de trabajo completos
  * `comfy templates` y la edición de slots de `comfy workflow`
  * Descubrimiento con `comfy nodes` / `comfy models`
  * Sobres `--json` y `comfy --json discover` para agentes

→ [Primeros pasos de Comfy CLI](https://docs.comfy.org/es/comfy-cli/getting-started) (documentación completa)

## 

​

Habilidades del agente

Instala en Claude Code, Cursor y cualquier herramienta compatible con AGENTS.md las habilidades del agente incluidas con Comfy, para que tu agente de programación pueda controlar la CLI directamente:
    
    
    comfy skills install
    comfy skills list      # comfy, comfy-fragments, comfy-debug, comfy-relay, comfy-director
    comfy skills status    # qué está instalado y dónde
    

Estas son **habilidades CLI incluidas** que se instalan con `comfy skills install`. Son independientes del repositorio [Comfy Skills](https://github.com/Comfy-Org/comfy-skills/), que aloja el plugin **comfy-cloud** de Claude Code para [Comfy Cloud MCP](https://docs.comfy.org/es/agent-tools/mcp).

## 

​

Recursos relacionados

Recurso| Para qué sirve  
---|---  
[Primeros pasos con Comfy CLI](https://docs.comfy.org/es/comfy-cli/getting-started)| Guía de instalación **completa** y recorrido por los comandos  
[Referencia de Comfy CLI](https://docs.comfy.org/es/comfy-cli/reference)| Comandos, flags y alias de modelos  
[Comfy MCP](https://docs.comfy.org/es/agent-tools/mcp)| Conecta agentes mediante MCP para generar desde el chat  
[comfy-cli en GitHub](https://github.com/Comfy-Org/comfy-cli)| Repositorio fuente, problemas y el comportamiento más reciente  
  
## 

​

Retroalimentación

  * **GitHub** : [problemas de comfy-cli](https://github.com/Comfy-Org/comfy-cli/issues)
  * **Discord** : [#comfy-mcp-and-cli](https://discord.gg/xWJn6nhE3R)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/agent-tools/cli.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/agent-tools/cli)

[Comfy MCP](https://docs.comfy.org/es/agent-tools/mcp)[Descripción general](https://docs.comfy.org/es/agent-tools/in-app-agent)
