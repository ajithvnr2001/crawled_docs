---
url: https://docs.comfy.org/es/comfy-cli/troubleshooting/
title: Gu\u00eda de soluci\u00f3n de problemas de Comfy CLI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:49.374852+00:00
---

# Guía de solución de problemas de Comfy CLI - ComfyUI

> Source: https://docs.comfy.org/es/comfy-cli/troubleshooting/

## En esta página

Volver arriba

  * Requisitos
  * Instalar ComfyUI en un entorno virtual
  * Instalar la compilación de PyTorch que corresponde a tu GPU
  * Configurar Comfy Cloud sin navegador
  * Obtener más ayuda



Comfy CLI

# Guía de solución de problemas de Comfy CLI

Copiar páginaCopiar página

Resuelve problemas comunes de Comfy CLI: git faltante, requisitos de Python y entorno virtual, autenticación de Comfy Cloud sin interfaz y bibliotecas de GPU.

Copiar páginaCopiar página

La mayoría de los fallos de Comfy CLI se deben a un requisito faltante o a un paso de configuración que se omitió. Revisa los puntos a continuación antes de reportar un problema.

## 

​

Requisitos

Comfy CLI necesita [git](https://git-scm.com/downloads) instalado en tu sistema. Instálalo primero, para que `comfy install` y `comfy update` puedan clonar ComfyUI y sus nodos personalizados.

## 

​

Instalar ComfyUI en un entorno virtual

`comfy install` instala ComfyUI en el entorno de Python activo, que debe ser Python 3.10 o superior. Crea y activa un entorno virtual antes de ejecutarlo:
    
    
    python3 -m venv comfy-env
    source comfy-env/bin/activate
    comfy install
    

## 

​

Instalar la compilación de PyTorch que corresponde a tu GPU

`comfy install` pregunta qué GPU tienes e instala la compilación de PyTorch correspondiente. Responde al prompt o pasa un flag de GPU para que el comando se ejecute sin intervención:

Plataforma| Qué instala `comfy install`| Qué necesitas todavía  
---|---|---  
NVIDIA| PyTorch con runtime de CUDA (wheel de pip)| Controlador de GPU actual (no el CUDA Toolkit completo)  
AMD Linux| wheels de PyTorch para ROCm| Controlador y stack de AMD compatibles con ROCm para esos wheels  
AMD Windows| `torch-directml`| GPU AMD compatible (DirectML; no ROCm)  
Apple silicon| wheels nocturnas de PyTorch (índice de CPU; Metal/MPS)| macOS en Apple silicon  
Intel Arc| wheels de PyTorch para XPU| GPU Intel Arc compatible / stack de XPU  
CPU| wheels de PyTorch para CPU| No se requiere GPU dedicada  
      
    
    comfy install --nvidia
    

Pasa `--skip-torch-or-directml` si instalas PyTorch por tu cuenta. `comfy env` muestra el entorno de Python y el espacio de trabajo que usa ComfyUI.

## 

​

Configurar Comfy Cloud sin navegador

`comfy setup` inicia sesión a través de tu navegador, así que no puede completarse en CI, un devcontainer ni un servidor sin interfaz gráfica. Pasa una clave API y ejecuta en modo no interactivo:
    
    
    comfy setup --where cloud --api-key comfyui-... --non-interactive
    

## 

​

Obtener más ayuda

  * [Empezar con Comfy CLI](https://docs.comfy.org/es/comfy-cli/getting-started) cubre la instalación, el enrutamiento y la generación.
  * [Referencia de comandos de Comfy CLI](https://docs.comfy.org/es/comfy-cli/reference) enumera todos los comandos y flags.
  * Reporta un bug de CLI reproducible en el [repositorio de comfy-cli](https://github.com/Comfy-Org/comfy-cli/issues).



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/comfy-cli/troubleshooting.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/comfy-cli/troubleshooting)

[Referencia de comandos](https://docs.comfy.org/es/comfy-cli/reference)[Workflow JSON](https://docs.comfy.org/es/specs/workflow_json)
