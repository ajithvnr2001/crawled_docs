---
url: https://docs.comfy.org/es/registry/standards/
title: Est\u00e1ndares de calidad y seguridad de nodos del Registro de Comfy - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:39.049681+00:00
---

# Estándares de calidad y seguridad de nodos del Registro de Comfy - ComfyUI

> Source: https://docs.comfy.org/es/registry/standards/

## En esta página

Volver arriba

  * Estándares básicos
    * 1\. Valor para la comunidad
    * 2\. Compatibilidad de nodos
    * 3\. Cumplimiento legal
    * 5\. Requisitos de calidad
    * 6\. Directrices para forks
  * Estándares de seguridad
    * Llamadas a eval/exec
    * Política
    * Justificación
    * subprocess para pip install
    * Política
    * Justificación
    * Ofuscación de código
    * Política
    * Justificación



Package & Publish

# Estándares de calidad y seguridad de nodos del Registro de Comfy

Copiar páginaCopiar página

Estándares de seguridad y calidad para publicar en el Registro

Copiar páginaCopiar página

## 

​

Estándares básicos

### 

​

1\. Valor para la comunidad

Los nodos personalizados deben aportar funcionalidad valiosa a la comunidad de ComfyUI Evita:

  * Autopromoción excesiva
  * Suplantación de identidad o comportamiento engañoso
  * Comportamiento malicioso
  * La autopromoción solo se permite dentro de la sección del menú de configuraciones designada para ello
  * Los menús superiores y laterales deben contener solo funcionalidad útil



### 

​

2\. Compatibilidad de nodos

No interfieras con las operaciones de otros nodos personalizados (instalación, actualizaciones, eliminación)

  * Para dependencias de otros nodos personalizados: 
    * Muestra advertencias claras cuando se use la funcionalidad dependiente
    * Proporciona flujos de trabajo de ejemplo que demuestren los nodos requeridos



### 

​

3\. Cumplimiento legal

Debe cumplir con todas las leyes y regulaciones aplicables

### 

​

5\. Requisitos de calidad

Los nodos deben ser completamente funcionales, estar bien documentados y recibir mantenimiento activo.

### 

​

6\. Directrices para forks

Los nodos derivados (fork) deben:

  * Tener nombres claramente distintos del original
  * Presentar diferencias significativas en funcionalidad o código

A continuación se presentan los estándares que deben cumplirse para publicar nodos personalizados en el registro.

## 

​

Estándares de seguridad

Los nodos personalizados deben ser seguros. Trabajaremos con los nodos personalizados que infrinjan estos estándares para que se reescriban. Si hay alguna funcionalidad importante que debería exponer el núcleo, solicítala en el [repositorio de rfcs](https://github.com/comfy-org/rfcs).

### 

​

Llamadas a eval/exec

#### 

​

Política

El uso de las funciones `eval` y `exec` está prohibido en los nodos personalizados por motivos de seguridad.

#### 

​

Justificación

Estas funciones pueden habilitar la ejecución de código arbitrario, lo que crea posibles vulnerabilidades de ejecución remota de código (RCE) al procesar entradas del usuario. Los flujos de trabajo que contienen nodos que pasan entradas del usuario a `eval` o `exec` podrían aprovecharse para diversos ciberataques, entre ellos:

  * Registro de pulsaciones de teclas
  * Ransomware
  * Otra ejecución de código malicioso



### 

​

subprocess para pip install

#### 

​

Política

No se permite la instalación de paquetes en tiempo de ejecución mediante llamadas a subprocess.

#### 

​

Justificación

  * Primer elemento ComfyUI Manager se distribuye con ComfyUI y permite al usuario instalar dependencias
  * La gestión centralizada de dependencias mejora la seguridad y la experiencia del usuario
  * Ayuda a prevenir posibles ataques a la cadena de suministro
  * Elimina la necesidad de recargar ComfyUI varias veces



### 

​

Ofuscación de código

#### 

​

Política

La ofuscación de código está prohibida en los nodos personalizados.

#### 

​

Justificación

El código ofuscado:

  * Es imposible de revisar y probablemente sea malicioso



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/standards.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/standards)

[Reclamar mi nodo](https://docs.comfy.org/es/registry/claim-my-node)[CI/CD](https://docs.comfy.org/es/registry/cicd)
