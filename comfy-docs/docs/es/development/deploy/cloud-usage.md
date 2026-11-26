---
url: https://docs.comfy.org/es/development/deploy/cloud-usage/
title: Uso y l\u00edmites - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-26T17:36:33.787625+00:00
---

# Uso y límites - ComfyUI

> Source: https://docs.comfy.org/es/development/deploy/cloud-usage/

## En esta página

Volver arriba

  * Créditos y uso
  * Límites de concurrencia
  * Límites de ejecución y de cola
  * Facturación de despliegues
    * ¿Se me cobra por almacenar Builds que no están desplegados?
    * ¿Cómo se facturan los workers always-warm?
  * Integraciones existentes de v1
  * Próximos pasos



Comfy Cloud

# Uso y límites

Copiar páginaCopiar página

Créditos de Comfy Cloud, tareas simultáneas, límites de ejecución y facturación de GPU y almacenamiento de modelos en implementaciones personalizadas de Build.

Copiar páginaCopiar página

Los flujos de trabajo enviados a través de la API de Comfy Cloud usan los mismos créditos y límites de concurrencia que el resto de flujos de trabajo de Cloud.

## Créditos y uso

Las solicitudes a la API se descuentan de la misma asignación mensual de créditos que la interfaz web de Comfy Cloud. No existe un grupo de créditos independiente para la API. Los créditos incluidos en cada plan, las opciones de recarga y los límites de tiempo de ejecución por flujo de trabajo se aplican a las tareas de la API igual que a las tareas de la interfaz web. Consulta la [página de precios](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) para conocer los montos mensuales de créditos y las opciones de recarga. Puedes comprar recargas desde el panel de tu cuenta.

## Límites de concurrencia

Puedes enviar varios flujos de trabajo sin esperar a que terminen las tareas anteriores. Las tareas se ejecutan en paralelo hasta el límite de tu nivel de suscripción:

Plan| Flujos de trabajo simultáneos  
---|---  
Estándar| 1  
Creador| 3  
Pro| 5  
  
Los planes de Equipo ejecutan más flujos de trabajo simultáneos por miembro que Pro. Consulta [platform.comfy.org](https://platform.comfy.org) para ver la concurrencia de tu cuenta. Las tareas adicionales quedan en cola y se ejecutan a medida que se liberan espacios. Si la cola está llena, los SDK reintentan dentro de un presupuesto limitado antes de lanzar `QueueFull`. En los planes de Equipo y Empresa, la concurrencia es por miembro: cada persona del espacio de trabajo tiene su propio límite de concurrencia, así que las tareas en ejecución de un miembro nunca bloquean las de otro.

Ejecutar más de una tarea a la vez solo se admite a través de la API. La interfaz de Comfy Cloud ejecuta un flujo de trabajo a la vez por persona, y los flujos de trabajo en cola en el editor se ejecutan en orden. Consulta los [planes de precios](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) para ver los detalles de la suscripción.

## Límites de ejecución y de cola

Cada flujo de trabajo de Comfy Cloud tiene un tiempo máximo de ejecución. Una tarea que supere el límite se cancela automáticamente:

Plan| Tiempo máximo de ejecución  
---|---  
Estándar| 30 minutos  
Creador| 30 minutos  
Pro| 1 hora  
  
Puedes tener hasta 100 flujos de trabajo en cola a la vez. Para aumentar el límite de concurrencia de Equipo, [contacta con soporte](https://support.comfy.org/).

## Facturación de despliegues

Un [despliegue](https://docs.comfy.org/es/development/serverless/overview) de un Build personalizado factura tiempo de GPU para sus workers y almacenamiento para sus modelos, con cargo a Comfy Credits.

### ¿Se me cobra por almacenar Builds que no están desplegados?

No. Los Builds y sus versiones se almacenan sin cargo. La facturación del almacenamiento comienza cuando despliegas:

  * Cuando despliegas una versión, Comfy Cloud copia sus modelos a un almacenamiento en red que comparten los workers del despliegue. Comfy Cloud factura ese almacenamiento por GB al mes mientras exista un despliegue del Build en esa región, incluso mientras el despliegue está detenido. Los modelos que una tarea usa de tu [biblioteca del espacio de trabajo](https://docs.comfy.org/es/development/deploy/cloud-custom-builds#agregar-tu-propio-lora-o-modelo) no se copian ahí: el worker los descarga para la tarea. 
    * Los modelos que [agregas a un despliegue](https://docs.comfy.org/es/development/serverless/overview#a%C3%B1adir-un-modelo-a-un-despliegue-en-ejecuci%C3%B3n) también se copian ahí y cuentan para ese almacenamiento.
  * El disco local de cada worker no genera ningún cargo adicional aparte de la tarifa de GPU.
  * Eliminar un despliegue libera su cómputo. La facturación del almacenamiento en red termina cuando eliminas el último despliegue que lo usa.

Para consultar las tarifas de almacenamiento y de GPU, abre [**Limits**](https://platform.comfy.org/settings/limits) en la Developer Platform y revisa **Deployment pricing**. El panel **Estimated cost** del diálogo de despliegue también muestra el tiempo de GPU y el almacenamiento de modelos de un despliegue.

### ¿Cómo se facturan los workers always-warm?

Los [workers always-warm](https://docs.comfy.org/es/development/serverless/overview#escalar-los-workers) (`--min` en comfy-cli) facturan tiempo de GPU mientras estén en ejecución, procesen o no tareas. Los workers por encima de ese número, hasta **Max workers** (`--max`), arrancan cuando llegan tareas. Facturan tiempo de GPU desde el momento en que arrancan, durante sus tareas, y por el tiempo inactivo posterior a su última tarea antes de liberarse. De forma predeterminada, un worker permanece activo 3 minutos después de su última tarea. Puedes configurar ese tiempo, entre 30 segundos y 20 minutos, en **Keep worker up after a job** al crear el despliegue en la Developer Platform. Con `0` workers always-warm, la facturación de GPU se detiene en cuanto termina ese tiempo inactivo y todos los workers se liberan. La siguiente tarea espera mientras arranca una GPU. Si tu espacio de trabajo se queda sin créditos, sus despliegues se detienen. Para consultar las tarifas de GPU, abre [**Limits**](https://platform.comfy.org/settings/limits) en la Developer Platform y revisa **Deployment pricing**. Las tarifas son por worker, por cada hora en ejecución.

## Integraciones existentes de v1

La [API de Cloud v1](https://docs.comfy.org/es/development/cloud/overview), que está obsoleta, también funciona con Comfy Cloud. Úsala para integraciones existentes o para capacidades de Cloud que aún no están disponibles en [Comfy API v2](https://docs.comfy.org/es/api-reference/v2/overview). Encontrarás ejemplos ejecutables en la [Referencia de la API de Cloud](https://docs.comfy.org/es/development/cloud/api-reference), que también está obsoleta.

## Próximos pasos

## Implementa en Comfy Cloud

Configura el SDK y ejecuta tu primer flujo de trabajo en Cloud.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/deploy/cloud-usage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/deploy/cloud-usage)

[Desplegar en Comfy Cloud](https://docs.comfy.org/es/development/deploy/cloud)[Builds personalizados](https://docs.comfy.org/es/development/deploy/cloud-custom-builds)
