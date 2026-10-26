---
url: https://docs.comfy.org/es/interface/user/
title: Gesti\u00f3n de cuenta - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:30.594964+00:00
---

# Gestión de cuenta - ComfyUI

> Source: https://docs.comfy.org/es/interface/user/

## En esta página

Volver arriba

  * Requisitos de la versión de ComfyUI
  * Requisitos de red
  * Cómo iniciar sesión
  * Métodos de inicio de sesión
  * Estado después de iniciar sesión
  * Preguntas frecuentes



Cuenta y créditos

# Gestión de cuenta

Copiar páginaCopiar página

Inicia sesión en ComfyUI desde Configuraciones → Usuario con correo, Google, GitHub o clave API; luego Plan y créditos aparecen en Espacio de trabajo.

Copiar páginaCopiar página

Las configuraciones descritas en esta página se encuentran en el **menú de configuraciones dentro de la aplicación de ComfyUI**. Puedes abrirlo navegando a **Configuraciones** (icono de engranaje) o usando el atajo de teclado `Ctrl + ,`, y luego seleccionar la categoría correspondiente para ver y configurar estas opciones.

Los Nodos asociados y la facturación de Comfy Cloud necesitan una cuenta de ComfyUI con sesión iniciada. Inicia sesión desde **Configuraciones → Usuario** (dentro del grupo **General**). Después de iniciar sesión, aparece **Configuraciones → Espacio de trabajo → Plan y créditos** para consultar el saldo y recargar créditos; consulta [Plan y créditos](https://docs.comfy.org/es/interface/credits). Actualmente, admitimos los siguientes métodos de inicio de sesión:

  * Inicio de sesión con correo electrónico
  * Inicio de sesión con Google
  * Inicio de sesión con GitHub
  * Inicio de sesión con Clave API (para autorización de sitios que no están en la lista blanca)

Proporcionaremos los requisitos y las explicaciones correspondientes al inicio de sesión en este documento.

## 

​

Requisitos de la versión de ComfyUI

Es posible que necesites al menos [ComfyUI v0.3.0](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.3.30) para usar el sistema de cuentas. Asegúrate de que la versión del frontend correspondiente sea al menos `1.17.11`. A veces el frontend puede fallar al instalarse y volver a una versión anterior, así que revisa si la versión del frontend es mayor que `1.17.11` en `Settings` -> `About`. En algunas regiones, las restricciones de red pueden impedir el acceso normal a la API de inicio de sesión, provocando tiempos de espera agotados o fallos. ANTES de iniciar sesión, **asegúrate de que tu entorno de red no restrinja el acceso a la API correspondiente** y verifica que puedes acceder a sitios como Google o GitHub.

Como todavía estamos en una etapa de actualizaciones iterativas rápidas, las funciones relacionadas pueden cambiar. Si no hay circunstancias especiales, intenta actualizar a la última versión para obtener soporte de las funciones correspondientes.

## 

​

Requisitos de red

Para iniciar sesión en la cuenta de ComfyUI, debes estar en un entorno de red seguro:

  * Solo se permite el acceso desde `127.0.0.1` o `localhost`.
  * No se admite el uso del parámetro `--listen` para acceder al nodo asociado a través de una red local.
  * Si usas un certificado que no sea SSL o un sitio que no comience por `https`, es posible que no puedas iniciar sesión correctamente.
  * Es posible que no puedas iniciar sesión en un sitio que no esté en nuestra lista blanca (pero ahora puedes iniciar sesión con una Clave API).
  * Asegúrate de poder conectarte a nuestro servicio con normalidad (algunas regiones pueden requerir un proxy).



## 

​

Cómo iniciar sesión

Inicia sesión desde **Configuraciones → Usuario** : ![Interfaz de usuario de ComfyUI](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/user.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4aacfc636460e073d16ef1fdaccb0888)

## 

​

Métodos de inicio de sesión

![Formulario de inicio de sesión con correo, Google, GitHub y clave API](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=70d1bb2128baed57bcd3d87d0744eb46) Si es tu primer inicio de sesión, primero crea una cuenta.

## Iniciar sesión con una Clave API

Para sitios que no están en la lista blanca o entornos de LAN, puedes usar el inicio de sesión con Clave API. Consulta la guía detallada en la documentación de inicio de sesión de la cuenta.

## 

​

Estado después de iniciar sesión

Después de iniciar sesión, el menú superior muestra el control de tu cuenta. Desde allí puedes volver a abrir el panel de usuario, cerrar sesión y, en Cloud, abrir **Gestionar plan** (el mismo panel **Plan y créditos** que en **Configuraciones → Espacio de trabajo → Plan y créditos**). ![Cuenta de usuario con la sesión iniciada](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/setting/user-logged.jpg?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=82fd894f75b3cdcf9c6e029bdab62b7c) ![Menú de usuario con la sesión iniciada](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/setting/menu-user-logged.jpg?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=949118faed113120dd12b35bb4536075)

## 

​

Preguntas frecuentes

¿Existe alguna restricción de dispositivos para iniciar sesión?

No restringimos los dispositivos de inicio de sesión. Puedes iniciar sesión en tu cuenta desde cualquier dispositivo, pero ten en cuenta que otros dispositivos podrían acceder a la información de tu cuenta, así que no inicies sesión en tu cuenta en dispositivos públicos.

¿Cómo iniciar sesión en un entorno de LAN?

Actualmente, en un entorno de LAN solo se admite el inicio de sesión con Clave API. Si accedes a los servicios de ComfyUI a través de una LAN, usa una Clave API para iniciar sesión.

¿Por qué no puedo iniciar sesión en algunos sitios web?

Nuestro servicio de inicio de sesión tiene una lista blanca, por lo que es posible que no puedas iniciar sesión en el ComfyUI desplegado en algunos servidores. En ese caso, puedes resolverlo usando el inicio de sesión con Clave API.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/user.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/user)

[Acerca de](https://docs.comfy.org/es/interface/settings/about)[Créditos](https://docs.comfy.org/es/interface/credits)
