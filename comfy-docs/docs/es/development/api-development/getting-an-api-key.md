---
url: https://docs.comfy.org/es/development/api-development/getting-an-api-key/
title: Obtener una clave API - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:52.334447+00:00
---

# Obtener una clave API - ComfyUI

> Source: https://docs.comfy.org/es/development/api-development/getting-an-api-key/

## En esta página

Volver arriba

  * Crear una clave API
  * Administrar tus claves API
  * Usar tu clave API



Desarrollar con Comfy

# Obtener una clave API

Copiar páginaCopiar página

Aprende a crear y administrar tu clave API de Comfy Platform para acceder a las API de Cloud, los Nodos asociados y más.

Copiar páginaCopiar página

Una clave API es tu credencial para acceder a los servicios de Comfy Platform, incluidos:

  * [API de Cloud](https://docs.comfy.org/es/development/cloud/overview): llama a los endpoints de Comfy Cloud de forma programática
  * [Integración de la API de Nodos asociados](https://docs.comfy.org/es/development/comfyui-server/api-key-integration): usa Nodos asociados de pago en tus flujos de trabajo locales
  * [Herramientas de agente / MCP](https://docs.comfy.org/es/agent-tools): conéctate a Comfy mediante MCP
  * [Iniciar sesión en ComfyUI de forma local](https://docs.comfy.org/es/account/login#iniciar-sesi%C3%B3n-con-una-clave-api): autentícate con una clave API en lugar de con tu correo electrónico



## 

​

Crear una clave API

1

Visita la Comfy Platform e inicia sesión

Visita la [página de inicio de sesión de Comfy Platform](https://platform.comfy.org/login) e inicia sesión con la cuenta correspondiente![Visita la página de inicio de sesión de Platform](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-1.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=c9516c73148a20ac2de9fcd5f56860c9)

2

Haz clic en `+ New` en API Keys para crear una clave API

Haz clic en `+ New` en API Keys para crear una clave API![Crear clave API](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-2.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=9e1f6dc2a5a28fbbe5074f4267dd8d14)

3

Ingresa el nombre de la clave API

![Ingresa el nombre de la clave API](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-3.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=112f28de30c52898bca15513706c70f2)

  1. (Requerido) Ingresa el nombre de la clave API,
  2. Haz clic en `Generate` para crearla



4

Guarda la clave API obtenida

![Obtener clave API](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-4.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=223b5d1941d0d9a2f2644807b08a676f)

Dado que la clave API solo es visible en el momento de su primera creación, guárdala inmediatamente después de crearla. No se podrá ver más adelante, así que consérvala en un lugar seguro. Ten en cuenta que no debes compartir tu clave API con otras personas. Si se filtra, puedes eliminarla y crear una nueva.

## 

​

Administrar tus claves API

Puedes ver y administrar todas tus claves API en [platform.comfy.org](https://platform.comfy.org) después de iniciar sesión.

  * **Ver claves existentes** : consulta el nombre y la fecha de creación de cada clave
  * **Eliminar una clave** : si una clave está comprometida o ya no la necesitas, elimínala de inmediato
  * **Crear claves adicionales** : puedes tener varias claves API para distintas aplicaciones



Las claves API solo se muestran una vez al crearlas. Guárdala de inmediato en un lugar seguro. Si pierdes una clave, elimínala y crea una nueva.

## 

​

Usar tu clave API

Una vez que tengas una clave API, puedes:

  1. **Iniciar sesión en ComfyUI de forma local** : ve a **Configuraciones → Usuario** y selecciona el inicio de sesión “Comfy API Key”
  2. **Llamar a las API de Nodos asociados** : incluye la clave en `extra_data.api_key_comfy_org` al enviar flujos de trabajo
  3. **Usar la API de Cloud** : incluye la clave en los encabezados de las solicitudes a los endpoints de la API de Cloud

Por seguridad, nunca compartas tu clave API ni la envíes a un sistema de control de versiones.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/api-development/getting-an-api-key.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/api-development/getting-an-api-key)

[Descripción general para desarrolladores](https://docs.comfy.org/es/development/overview)[Ejemplos](https://docs.comfy.org/es/development/examples)
