---
url: https://docs.comfy.org/es/development/comfyui-server/api-proxy/
title: Proxy de API para ComfyUI autoalojado - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:27.635722+00:00
---

# Proxy de API para ComfyUI autoalojado - ComfyUI

> Source: https://docs.comfy.org/es/development/comfyui-server/api-proxy/

## En esta página

Volver arriba

  * Instalar y ejecutar
  * Apuntar el SDK al proxy
  * Autenticación
  * Próximos pasos



Ejecutar flujos de trabajo

# Proxy de API para ComfyUI autoalojado

Copiar páginaCopiar página

Sirve la Comfy API v2 delante de tu propio ComfyUI para que los SDK oficiales ejecuten flujos de trabajo

Copiar páginaCopiar página

Los [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks) hablan [Comfy API v2](https://docs.comfy.org/es/api-reference/v2/overview). Un ComfyUI autoalojado sirve la v2 mediante [comfy-api-proxy](https://github.com/Comfy-Org/comfy-api-proxy), un pequeño servicio de código abierto que se ejecuta junto a tu instancia.

## 

​

Instalar y ejecutar
    
    
    pip install comfy-api-proxy
    comfy-api-proxy
    

De forma predeterminada, hace de proxy del ComfyUI en `127.0.0.1:8188` y sirve la API v2 en `127.0.0.1:8189`. Usa `--comfyui` y `--port` para cambiar cualquiera de los dos. Ejecútalo con `--comfyui-base-dir /path/to/ComfyUI` si además quieres subir archivos de modelo a tu instalación.

## 

​

Apuntar el SDK al proxy

Establece la URL base y crea el cliente como de costumbre:
    
    
    export COMFY_BASE_URL="http://127.0.0.1:8189"
    

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    client = Comfy()
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    const client = new Comfy();
    

Todo lo que aparece en la [guía del SDK](https://docs.comfy.org/es/development/api-development/sdks) funciona igual con el proxy que con Comfy Cloud.

## 

​

Autenticación

La autenticación no es requerida de forma predeterminada. Si el proxy está configurado con un token de portador estático, pasa ese token como la clave API del SDK: `Comfy(api_key="...")`.

El proxy se enlaza solo a loopback de forma predeterminada. Si lo expones más allá de loopback, por ejemplo frente a un ComfyUI en una GPU alquilada, configura un token de portador o coloca un proxy inverso con autenticación delante de él.

## 

​

Próximos pasos

  * [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks): la guía del cliente
  * [Referencia de Comfy API v2](https://docs.comfy.org/es/api-reference/v2/overview): el contrato HTTP que sirve el proxy
  * [Opciones de autoalojamiento](https://docs.comfy.org/es/development/deploy/self-hosting): dónde ejecutar el ComfyUI detrás del proxy
  * [Notas de diseño](https://docs.comfy.org/es/development/api-development/sdks-design#el-proxy-local): por qué existe el proxy



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfyui-server/api-proxy.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfyui-server/api-proxy)

[SDK](https://docs.comfy.org/es/development/api-development/sdks)[Formato de API de flujos de trabajo](https://docs.comfy.org/es/development/api-development/workflow-api-format)
