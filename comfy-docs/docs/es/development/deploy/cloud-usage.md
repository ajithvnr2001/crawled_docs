---
url: https://docs.comfy.org/es/development/deploy/cloud-usage/
title: Uso y l\u00edmites - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:27.573425+00:00
---

# Uso y límites - ComfyUI

> Source: https://docs.comfy.org/es/development/deploy/cloud-usage/

## En esta página

Volver arriba

  * Créditos y uso
  * Tareas simultáneas
  * Límites de ejecución y de cola
  * Integraciones existentes de v1
  * Próximos pasos



Comfy Cloud

# Uso y límites

Copiar páginaCopiar página

Conoce los créditos de Comfy Cloud, las tareas simultáneas y los límites al ejecutar flujos de trabajo desde el SDK.

Copiar páginaCopiar página

Los flujos de trabajo enviados a través de la API de Comfy Cloud usan los mismos créditos y límites de simultaneidad que el resto de flujos de trabajo de Cloud.

## 

​

Créditos y uso

Las solicitudes a la API consumen la misma asignación mensual de créditos que la interfaz web de Comfy Cloud. No hay un grupo de créditos independiente para la API. Los créditos incluidos en cada plan, las opciones de recarga y los límites de tiempo de ejecución por flujo de trabajo se aplican a las tareas de la API igual que a las tareas de la interfaz. Consulta la [página de precios](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) para ver los importes mensuales de créditos y las opciones de recarga. Puedes comprar recargas desde el panel de tu cuenta.

## 

​

Tareas simultáneas

Puedes enviar varios flujos de trabajo sin esperar a que terminen las tareas anteriores. Las tareas se ejecutan en paralelo hasta el límite de tu plan de suscripción:

Plan| Flujos de trabajo simultáneos  
---|---  
Standard| 1  
Creator| 3  
Pro| 5  
  
Los planes de equipo ejecutan más flujos de trabajo simultáneos por miembro que Pro. Consulta [platform.comfy.org](https://platform.comfy.org) para ver la simultaneidad de tu cuenta. Las tareas adicionales quedan en cola y se ejecutan a medida que se liberan espacios. Si la cola está llena, los SDK reintentan dentro de un presupuesto limitado antes de generar el error `QueueFull`. En los planes Team y Enterprise, la simultaneidad es por miembro: cada persona del espacio de trabajo tiene su propio límite de simultaneidad, así que las tareas en ejecución de un miembro nunca bloquean las de otro.

La ejecución de más de una tarea a la vez solo se admite a través de la API. La interfaz de Comfy Cloud ejecuta un flujo de trabajo a la vez por persona, y los flujos de trabajo en cola en el editor se ejecutan en orden. Consulta los [planes de precios](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) para ver los detalles de la suscripción.

## 

​

Límites de ejecución y de cola

Cada flujo de trabajo de Cloud tiene un tiempo máximo de ejecución. Una tarea que supera ese límite se cancela automáticamente:

Plan| Tiempo máximo de ejecución  
---|---  
Standard| 30 minutos  
Creator| 30 minutos  
Pro| 1 hora  
  
Puedes tener hasta 100 flujos de trabajo en cola a la vez. Para aumentar el límite de simultaneidad de un plan de equipo, [contacta con soporte](https://support.comfy.org/).

## 

​

Integraciones existentes de v1

La [API de Cloud v1](https://docs.comfy.org/es/development/cloud/overview), que está obsoleta, también funciona con Comfy Cloud. Úsala para integraciones existentes o para capacidades de Cloud que aún no están disponibles en [Comfy API v2](https://docs.comfy.org/es/api-reference/v2/overview). Hay ejemplos ejecutables en la [Referencia de la API de Cloud](https://docs.comfy.org/es/development/cloud/api-reference), también obsoleta.

## 

​

Próximos pasos

## Inicio rápido de Comfy Cloud

Configura el SDK y ejecuta tu primer flujo de trabajo de Cloud.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/deploy/cloud-usage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/deploy/cloud-usage)

[Inicio rápido](https://docs.comfy.org/es/development/deploy/cloud)[Opciones de alojamiento](https://docs.comfy.org/es/development/deploy/self-hosting)
