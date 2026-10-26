---
url: https://docs.comfy.org/es/development/serverless/build-sources/
title: Otras formas de crear un Build de Comfy API - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:28.056245+00:00
---

# Otras formas de crear un Build de Comfy API - ComfyUI

> Source: https://docs.comfy.org/es/development/serverless/build-sources/

## En esta página

Volver arriba

  * Instantánea de Comfy Desktop
  * JSON del flujo de trabajo
  * Siguientes pasos



API de Comfy

# Otras formas de crear un Build de Comfy API

Copiar páginaCopiar página

Crea un Build de Comfy API desde una instantánea de Comfy Desktop o un JSON de flujo de trabajo guardado.

Copiar páginaCopiar página

¿Ya tienes una instantánea de Desktop o un flujo de trabajo? Usa la ruta correspondiente a continuación para iniciar un Build y luego revisa su contenido antes de publicar el release.

## 

​

Instantánea de Comfy Desktop

Usa una instantánea para trasladar la versión de ComfyUI, los nodos personalizados y los paquetes de Python de una instancia de Desktop a un Build.

  1. En Comfy Desktop, abre el panel **Manage** de la instancia y selecciona **Snapshots**. Elige la instantánea del entorno que quieres compilar y haz clic en su botón **Export**. Si el estado actual no aparece en la lista, crea primero una instantánea manual. Consulta [Pasos para instantáneas de Desktop](https://docs.comfy.org/es/installation/desktop/usage/snapshots#descripci%C3%B3n-general-de-la-pesta%C3%B1a-instant%C3%A1neas).
  2. Abre el [Comfy API Build Wizard](https://platform.comfy.org/?onboarding=comfyapi) e importa el archivo de instantánea.
  3. Revisa el contenido del Build y agrega o corrige los modelos o las dependencias faltantes antes de crear un release.

![Pestaña Snapshots de Comfy Desktop con el botón Export de la instantánea seleccionada resaltado](https://mintcdn.com/dripart/iNsH_dGIhlvCFWxl/images/development/serverless/build-sources-desktop-snapshot.png?fit=max&auto=format&n=iNsH_dGIhlvCFWxl&q=85&s=13e0b54bdf0364f74e2978cc648c94ce)

## 

​

JSON del flujo de trabajo

Usa un archivo de flujo de trabajo guardado para configurar un Build en el Build Wizard:

  1. Abre el [Comfy API Build Wizard](https://platform.comfy.org/?onboarding=comfyapi).
  2. Arrastra el JSON del flujo de trabajo al paso de importación.
  3. Revisa el contenido del Build y agrega o corrige los modelos o las dependencias faltantes antes de crear un release.

![Comfy API Build Wizard con un JSON de flujo de trabajo importado y los pasos de configuración del Build](https://mintcdn.com/dripart/iNsH_dGIhlvCFWxl/images/development/serverless/build-sources-workflow-import.png?fit=max&auto=format&n=iNsH_dGIhlvCFWxl&q=85&s=288be8ba80618d14e16b294b846c5f88) El asistente inspecciona el flujo de trabajo y sugiere configuraciones del Build antes de que continúes.

## 

​

Siguientes pasos

## Comfy API Quickstart

Crea un release, despliégalo y ejecuta un flujo de trabajo con un agente o la CLI.

## Guía de despliegue de Comfy API

Administra los archivos del Build, las actualizaciones, los releases, el escalado, la facturación y la resolución de problemas.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/serverless/build-sources.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/serverless/build-sources)

[Inicio rápido](https://docs.comfy.org/es/development/serverless/quickstart)[Guía de despliegue](https://docs.comfy.org/es/development/serverless/overview)
