---
url: https://docs.comfy.org/es/tutorials/partner-nodes/faq/
title: Preguntas frecuentes sobre los nodos asociados - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:48.499472+00:00
---

# Preguntas frecuentes sobre los nodos asociados - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/faq/

Nodos asociados

# Preguntas frecuentes sobre los nodos asociados

Copiar páginaCopiar página

Preguntas frecuentes sobre los nodos asociados de ComfyUI: créditos y facturación, inicio de sesión, moderación de contenido y eliminación de cuentas.

Copiar páginaCopiar página

Este artículo responde preguntas comunes sobre el uso de los nodos asociados.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/faq.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/faq)

[Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits)[Retención de datos](https://docs.comfy.org/es/tutorials/partner-nodes/data-retention)
