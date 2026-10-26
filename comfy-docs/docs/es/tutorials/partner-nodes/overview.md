---
url: https://docs.comfy.org/es/tutorials/partner-nodes/overview/
title: Nodos asociados - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:53.677480+00:00
---

# Nodos asociados - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/overview/

## En esta página

Volver arriba

  * ¿Qué son los Nodos asociados?
  * Requisitos previos para usar los Nodos asociados
    * 1\. Requisitos de versión de ComfyUI
    * 2\. Requisitos de cuenta y créditos
    * 3\. Requisitos del entorno de red
    * 4\. Usar los nodos correspondientes
  * Iniciar sesión con la Clave API de la cuenta de ComfyUI en sitios web que no están en la lista blanca
  * Usar la integración de claves API de la cuenta de ComfyUI para llamar a nodos asociados de modelos de pago
  * Ventajas de los Nodos asociados
  * Precios
  * Proveedores de modelos
  * Acerca del código abierto y la participación voluntaria
  * Cómo desactivar por completo los nodos asociados
  * Casos de uso
  * Preguntas frecuentes



Nodos asociados

# Nodos asociados

Copiar páginaCopiar página

Los Nodos asociados llaman a modelos de código cerrado como OpenAI, Kling y Luma mediante solicitudes API dentro de ComfyUI: qué son, créditos y cómo usarlos.

Copiar páginaCopiar página

Los Nodos asociados son la nueva forma de ComfyUI de llamar a modelos de código cerrado mediante solicitudes a la API, y le dan acceso a los usuarios de ComfyUI a modelos de IA externos de última generación sin necesidad de una configuración compleja de claves API.

## 

​

¿Qué son los Nodos asociados?

Los Nodos asociados son un conjunto de nodos especiales que se conectan a servicios de API externos, lo que te permite usar modelos de IA de código cerrado o alojados por terceros directamente en tus flujos de trabajo de ComfyUI. Estos nodos están diseñados para integrar sin problemas las capacidades de los modelos externos mientras se mantiene la naturaleza de código abierto del núcleo de ComfyUI.

## 

​

Requisitos previos para usar los Nodos asociados

Para usar los Nodos asociados, se deben cumplir los siguientes requisitos:

### 

​

1\. Requisitos de versión de ComfyUI

Actualiza tu ComfyUI a la última versión, ya que es posible que agreguemos más compatibilidad con API en el futuro y los nodos correspondientes se actualicen, así que mantén tu ComfyUI actualizado.

Ten en cuenta la diferencia entre las versiones nocturna y de lanzamiento. Recomendamos usar la versión `nightly` (que es la confirmación de código más reciente), ya que es posible que la versión de lanzamiento no se actualice de manera oportuna. Esto se refiere a la versión de desarrollo y a la versión estable, y como todavía estamos iterando rápidamente, es posible que este documento no se actualice con prontitud, así que presta atención a las diferencias entre versiones.

### 

​

2\. Requisitos de cuenta y créditos

Debes haber iniciado sesión en tu ComfyUI con una [cuenta de Comfy](https://docs.comfy.org/es/interface/user) y tener un saldo de [créditos](https://docs.comfy.org/es/interface/credits) mayor que 0. Inicia sesión mediante `Settings` -> `User`: ![ComfyUI User Interface](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/user.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4aacfc636460e073d16ef1fdaccb0888) Ve a `Settings` -> `Credits` para comprar créditos ![Credits Interface](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/setting/purchase-1.jpg?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=d4371030bb5549d08feb37abd8ae19fb) Consulta la documentación correspondiente sobre la cuenta y los créditos para asegurar este requisito:

  * [Cuenta de Comfy](https://docs.comfy.org/es/interface/user): busca la sección `User` en el menú de configuraciones para iniciar sesión.
  * [Créditos](https://docs.comfy.org/es/interface/credits): después de iniciar sesión, la interfaz de configuraciones mostrará un menú de créditos donde puedes comprar créditos. Usamos un sistema de prepago, así que no habrá cargos inesperados.



### 

​

3\. Requisitos del entorno de red

El acceso a la API requiere que tus solicitudes actuales se realicen en un entorno de red seguro. Los requisitos actuales para el acceso a la API son los siguientes:

  * La red local solo permite el acceso desde `127.0.0.1` o `localhost`, y puedes usar directamente la función de inicio de sesión.
  * Si accedes desde una red de área local o un sitio web que no esté en la lista de permitidos, inicia sesión con una Clave API. Consulta [Iniciar sesión con una Clave API](https://docs.comfy.org/es/account/login#iniciar-sesi%C3%B3n-con-una-clave-api).
  * Deberías poder acceder normalmente a nuestro servicio de API (en algunas regiones, es posible que necesites usar un servicio de proxy).
  * El acceso debe realizarse en un entorno `https` para garantizar la seguridad de las solicitudes.



Acceder en un contexto no seguro conlleva riesgos importantes, lo que puede provocar las siguientes consecuencias:

  1. La autenticación puede ser robada, lo que ocasiona la filtración de la información de tu cuenta.
  2. Tu cuenta puede ser utilizada de forma maliciosa, lo que resulta en pérdidas financieras.

Incluso si en el futuro abrimos esta restricción, recomendamos encarecidamente no acceder a los servicios de API mediante solicitudes de red no seguras debido a los altos riesgos que implica.

### 

​

4\. Usar los nodos correspondientes

**Agregar al flujo de trabajo** : agrega el Nodo asociado a tu flujo de trabajo tal como lo harías con otros nodos. **Ejecutar** : configura los parámetros y luego ejecuta el flujo de trabajo. ![Partner Nodes](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/tutorial/api_nodes/sidebar.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=5adc8f697864ac7d890722dddbb8260c)

## 

​

Iniciar sesión con la Clave API de la cuenta de ComfyUI en sitios web que no están en la lista blanca

Actualmente, contamos con una lista blanca que restringe los sitios web donde puedes iniciar sesión en tu cuenta de ComfyUI. Si necesitas iniciar sesión en tu cuenta de ComfyUI en sitios web que no están en la lista blanca, consulta la sección de administración de cuentas para obtener información sobre cómo iniciar sesión con una Clave API. En este caso, el sitio web correspondiente no necesita estar en nuestra lista blanca.

## Administración de cuentas

Aprende a iniciar sesión con la Clave API de la cuenta de ComfyUI

![Seleccionar el inicio de sesión con la Clave API de Comfy](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdb8d99a4bd52a6cc1de1b3453e8cfda)

## 

​

Usar la integración de claves API de la cuenta de ComfyUI para llamar a nodos asociados de modelos de pago

Actualmente, admitimos el acceso a nuestros servicios mediante la integración de claves API de ComfyUI para llamar a nodos asociados de modelos de pago. Consulta la sección Integración de claves API para obtener información sobre cómo usar la integración de claves API para llamar a nodos asociados de modelos de pago.

**Importante:** La clave API que se trata aquí es tu **Clave API de la cuenta de ComfyUI** (se usa para acceder a los nodos asociados de pago en los flujos de trabajo). **NO** es la misma que la **Clave API de publicación en el registro** que usan los desarrolladores para publicar nodos personalizados en el registro. Si deseas publicar nodos personalizados, consulta [Publicar nodos](https://docs.comfy.org/es/registry/publishing).

## Integración de claves API

Consulta la sección Integración de claves API para obtener información sobre cómo usar la integración de claves API para llamar a nodos asociados de modelos de pago

## 

​

Ventajas de los Nodos asociados

Los Nodos asociados ofrecen varias ventajas importantes para los usuarios de ComfyUI:

  * **Acceso a modelos de código cerrado** : Usa modelos de IA de última generación sin tener que desplegarlos tú mismo
  * **Integración perfecta** : Los nodos asociados son totalmente compatibles con otros nodos de ComfyUI y puedes combinarlos para crear flujos de trabajo complejos
  * **Experiencia simplificada** : No necesitas administrar claves de API ni gestionar solicitudes de API complejas
  * **Costos controlados** : El sistema de prepago te garantiza un control total sobre tu gasto, sin cargos inesperados



## 

​

Precios

## Precios de los Nodos asociados

Consulta la página de precios para ver los precios correspondientes de los Nodos asociados

## 

​

Proveedores de modelos

## Proveedores de modelos

Consulta el estado de verificación, las licencias comerciales y la residencia de datos de los proveedores de modelos que hay detrás de los Nodos asociados

## 

​

Acerca del código abierto y la participación voluntaria

Es importante tener en cuenta que **los nodos asociados son completamente opcionales**. ComfyUI siempre seguirá siendo totalmente de código abierto y gratis para los usuarios locales. Los nodos asociados están diseñados como una función “opt-in”, que brinda comodidad a quienes desean acceder a modelos externos SOTA (de última generación).

## 

​

Cómo desactivar por completo los nodos asociados

Puedes añadir el argumento de inicio `--disable-partner-nodes` para desactivar todos los Nodos asociados en ComfyUI. Usa `--offline` en su lugar si además quieres impedir que el frontend se comunique con internet. **Para instalación manual:**
    
    
    python main.py --disable-partner-nodes
    

**Para usuarios de la versión portable (Windows):** Actualiza tu archivo `run_xxx.bat`:
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build --disable-partner-nodes
    pause
    

## 

​

Casos de uso

Una aplicación potente de los Nodos asociados es combinar la salida de modelos externos con nodos locales. Por ejemplo:

  * Usar GPT-Image-1 para generar una imagen base y luego transformarla en video con un nodo `wan` local
  * Combinar imágenes generadas externamente con nodos locales de ampliación o transferencia de estilo
  * Crear flujos de trabajo híbridos que aprovechen las ventajas tanto de los modelos de código cerrado como de los de código abierto

Esta flexibilidad hace de ComfyUI una interfaz de IA generativa verdaderamente universal, que integra diversas capacidades de IA en un flujo de trabajo unificado y abre más posibilidades.

## 

​

Preguntas frecuentes

¿Por qué no encuentro los Nodos asociados?

Actualiza tu ComfyUI a la última versión (el último commit o la última [versión de escritorio](https://www.comfy.org/download)). Es posible que agreguemos más compatibilidad con API en el futuro y se actualicen los nodos correspondientes, así que mantén tu ComfyUI actualizado.

Ten en cuenta que debes distinguir entre la versión nocturna y la versión de lanzamiento. En algunos casos, la última versión `release` puede no actualizarse a tiempo en comparación con la versión `nightly`. Como todavía estamos iterando rápidamente, asegúrate de usar la última versión cuando no encuentres el nodo correspondiente.

¿Por qué no puedo usar / iniciar sesión en los Nodos asociados?

El acceso a la API requiere que tu solicitud actual se base en un entorno de red seguro. Los requisitos actuales para acceder a la API son los siguientes:

  * La red local solo permite el acceso desde `127.0.0.1` o `localhost`, lo que puede significar que no puedas usar los Nodos asociados en un servicio de ComfyUI iniciado con el parámetro `--listen` en un entorno de LAN.
  * Poder acceder a nuestro servicio de API normalmente (es posible que se requiera un servicio de proxy en algunas regiones).
  * Tu cuenta no tiene suficientes [créditos](https://docs.comfy.org/es/interface/credits).



¿Por qué no puedo usar un Nodo asociado incluso después de iniciar sesión, o por qué me sigue pidiendo que inicie sesión mientras lo uso?

  * Actualmente, solo se admite el acceso desde `127.0.0.1` o `localhost`.
  * Asegúrate de que tu cuenta tenga suficientes créditos.



¿Se pueden usar los Nodos asociados de forma gratuita?

Los Nodos asociados requieren créditos para las llamadas a la API de modelos de código cerrado, por lo que no admiten el uso gratuito.

¿Cómo comprar créditos?

Consulta la siguiente documentación:

  1. [Cuenta de Comfy](https://docs.comfy.org/es/interface/user): busca la sección `User` en el menú de configuraciones para iniciar sesión.
  2. [Créditos](https://docs.comfy.org/es/interface/credits): después de iniciar sesión, la interfaz de configuraciones mostrará el menú de créditos. Puedes comprar créditos en `Settings` → `Credits`. Usamos un sistema de prepago, por lo que no habrá cargos inesperados.
  3. Completa el pago a través de Stripe.
  4. Comprueba si los créditos se han actualizado. Si no es así, intenta reiniciar o actualizar la página.



¿Se pueden reembolsar los créditos no utilizados?

Actualmente, no admitimos reembolsos de créditos. Si crees que hay un error que resulte en un saldo sin usar debido a problemas técnicos, por favor [contacta con soporte](mailto:support@comfy.org).

¿Los créditos pueden quedar en negativo?

Los créditos no están pensados para usarse como un saldo negativo ni como una línea de crédito. Sin embargo, debido a condiciones de carrera en las que los nodos asociados no siempre informan los costos antes de la ejecución, una sola ejecución puede consumir más créditos que tu saldo restante y dar como resultado temporalmente un saldo negativo después de completarse. Cuando tu saldo sea negativo, no podrás ejecutar Nodos asociados hasta que recargues y restaures un saldo positivo. Asegúrate de tener suficientes créditos antes de realizar llamadas a la API.

¿Dónde puedo consultar el uso y los gastos?

Visita el menú [Créditos](https://docs.comfy.org/es/interface/credits) después de iniciar sesión para consultar los créditos correspondientes.

¿Es posible usar mi propia clave API?

Actualmente, los Nodos asociados todavía están en fase de pruebas y aún no admiten esta función, pero hemos considerado agregarla.

¿Expiran los créditos?

Sí, la expiración depende del tipo de créditos:

  * **Créditos mensuales** : expiran al final de tu período de facturación
  * **Créditos de recarga** : expiran 1 año a partir de la fecha de compra



¿Se pueden transferir o compartir los créditos?

No, tus créditos no se pueden transferir a otros usuarios y están limitados a la cuenta con la sesión iniciada actualmente, pero no restringimos la cantidad de dispositivos que pueden iniciar sesión.

¿Puedo usar la misma cuenta en diferentes dispositivos?

No limitamos la cantidad de dispositivos que pueden iniciar sesión; puedes usar tu cuenta donde quieras.

¿Cómo puedo solicitar que se elimine mi cuenta o mi información?

Envía una solicitud por correo electrónico a [support@comfy.org](mailto:support@comfy.org) y eliminaremos tu información.

¿Existe moderación de contenido para los Nodos asociados?

Los Nodos asociados envían tus entradas (prompts, imágenes y otro contenido) a proveedores externos para su procesamiento. Estos proveedores aplican sus propias políticas de moderación de contenido. No envíes contenido NSFW ni otro contenido prohibido a los Nodos API.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/overview)

[Descripción general](https://docs.comfy.org/es/cloud-nodes/overview)[Precios](https://docs.comfy.org/es/tutorials/partner-nodes/pricing)
