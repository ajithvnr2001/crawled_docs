---
url: https://docs.comfy.org/es/development/comfy-router/headers/
title: Encabezados de Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:54.159433+00:00
---

# Encabezados de Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/headers/

## En esta página

Volver arriba

  * Encabezados de la solicitud
  * Encabezados de respuesta
  * Códigos de estado con dos significados
  * Próximos pasos



Referencia

# Encabezados de Comfy Router

Copiar páginaCopiar página

Encabezados de solicitud y respuesta de Comfy Router para cada modelo: autenticación, idempotencia, IDs de solicitud, límites de reintento y gasto.

Copiar páginaCopiar página

Todos los modelos de Router usan `POST /v2/models/{provider}/{model}` con su propio cuerpo JSON. Esta página cubre los encabezados compartidos entre modelos; la [referencia de API](https://docs.comfy.org/es/development/comfy-router/reference) enumera el contrato generado. Los SDK de Comfy (`comfy-sdk` para Python, `@comfyorg/sdk` para TypeScript) gestionan la autenticación y generan claves de idempotencia. Exponen metadatos de respuesta seleccionados como se describe a continuación. Los clientes HTTP directos deben enviar y leer los encabezados por su cuenta.

## 

​

Encabezados de la solicitud

​

X-API-Key

string

Una clave API de Comfy, `comfyui-...`, creada en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router). Usa el acceso a modelos y el saldo de créditos de tu espacio de trabajo. También puedes enviarla como `Authorization: Bearer comfyui-...`; si ambos encabezados están presentes, gana `X-API-Key`.

​

Authorization

string

`Bearer <token>`. Un valor `comfyui-` es una clave API. Cualquier otro valor se trata como un JWT de Comfy Cloud.

​

Idempotency-Key

string

Identifica una generación lógica. Genera y guarda un UUID antes de la llamada y luego reutilízalo para los reintentos de la solicitud sin cambios. La clave puede reproducir un resultado o recopilar el trabajo aceptado durante un máximo de 24 horas. Los SDK generan claves y te permiten usar las tuyas (`idempotency_key=` en Python, `idempotencyKey` en TypeScript). Consulta [resultados de reintento](https://docs.comfy.org/es/development/comfy-router/errors#resultados-de-reintento) para conflictos, caducidad y resultados no reproducibles.

​

Content-Type

string

`application/json`. Envía la entrada JSON nativa del modelo. Los campos y los requisitos de validación varían según el modelo; consulta [Uso de la API del Router](https://docs.comfy.org/es/development/comfy-router/api).

​

If-None-Match

string

Solo en `GET /v2/models/{provider}/{model}/openapi.json`. Envía el `ETag` que tienes de un `200` anterior; cuando aún coincide, la respuesta es un `304` sin cuerpo con el mismo `ETag`. Guarda en caché el esquema de un modelo durante la vida de tu proceso y revalídalo de esta forma en lugar de volver a leerlo antes de cada llamada.

## 

​

Encabezados de respuesta

​

X-Comfy-Request-Id

string

requerido

Identifica esta solicitud HTTP. Inclúyelo cuando contactes a soporte. TypeScript lo expone como `requestId`; Python expone `request_id` en los errores.

​

X-Comfy-Error-Type

string

La categoría de error legible por máquina. En un `422`, usa este encabezado porque el cuerpo de validación tiene `detail[]` y no tiene `error_type`. Combínalo con el estado HTTP para decidir qué hacer. Trata un valor desconocido como `internal_error` para el flujo de control y consérvalo para el diagnóstico.

​

Idempotent-Replayed

boolean

Presente y `true` cuando Router entrega un resultado almacenado en lugar de ejecutar el modelo otra vez. No está presente en una ejecución nueva. En la ruta de envío en cola, un `201` reproducido devuelve el identificador de la solicitud original en lugar de encolar una segunda ejecución.

​

Retry-After

integer

Segundos que debes esperar antes de reintentar. En `409` / `concurrency_limit_exceeded` o `504` / `deadline_exceeded`, reintenta la misma solicitud y la misma clave después de la espera. En `429` / `rate_limited`, indica cuándo se restablece el límite de tasa. En la lectura del estado de una solicitud en cola y en la lectura de su resultado `202`, es la sugerencia de Router sobre cuándo vale la pena volver a consultar.

​

X-Committed-Spend-Limit

integer

El límite máximo del gasto de socio comprometido en llamadas que aún se están ejecutando, en centavos de USD. Una compuerta de gasto con aplicación activa puede devolverlo en las respuestas admitidas y en sus rechazos `429`. No está presente cuando la compuerta no está aplicando el límite o cuando otro control rechazó la solicitud.

​

X-Committed-Spend-Current

integer

Centavos de USD comprometidos actualmente en llamadas en curso. Una respuesta admitida incluye su propia llamada; un `429` excluye la llamada rechazada. Se envía junto con `X-Committed-Spend-Limit`.

​

X-Committed-Spend-Remaining

integer

Centavos de USD que quedan por debajo del límite de gasto comprometido. Puede ser positivo en un rechazo cuando la llamada solicitada cuesta más que la cantidad restante.

​

ETag

string

En `GET /v2/models/{provider}/{model}/openapi.json`. Guárdalo y envíalo de vuelta como `If-None-Match` para revalidar un esquema en caché.

​

Cache-Control

string

En la ruta del esquema: `private, must-revalidate`. Mantén la respuesta en una caché privada y revalida las copias obsoletas con el `ETag`.

## 

​

Códigos de estado con dos significados

Tres estados se comparten entre dos categorías, y el encabezado es lo que permite distinguirlos:

Estado| `X-Comfy-Error-Type`| Qué hacer  
---|---|---  
`409`| `concurrency_limit_exceeded`| La llamada original para esta clave sigue en ejecución. Espera `Retry-After` y vuelve a enviar la misma clave.  
`409`| `invalid_input`| Inspecciona el conflicto. Restaura la solicitud original si la cambiaste. Una clave consumida y no reutilizable no puede recuperar el resultado; usa una clave nueva solo si pretendes realizar una generación nueva, potencialmente facturable.  
`429`| `concurrency_limit_exceeded`| Demasiadas llamadas en curso, o se alcanzó el límite de gasto comprometido (consulta los encabezados `X-Committed-Spend-*`). Se libera cuando finaliza una de tus propias llamadas.  
`429`| `rate_limited`| Espera `Retry-After` antes de reintentar.  
`504`| `deadline_exceeded`| Límite propio del router de 10 minutos. Con `Retry-After`, vuelve a enviar la misma clave para recuperar la generación en curso.  
`504`| `provider_timeout`| El Socio agotó el tiempo de espera. Sigue la [orientación sobre reintentos y facturación](https://docs.comfy.org/es/development/comfy-router/errors#resultados-de-reintento); no lo interpretes como una garantía de que no se cobrará.  
  
## 

​

Próximos pasos

  * [Quickstart](https://docs.comfy.org/es/development/comfy-router/quickstart): envía una solicitud y lee el resultado.
  * [Usar la API de Comfy Router](https://docs.comfy.org/es/development/comfy-router/api): descubrimiento de modelos, esquemas, errores, reintentos y facturación.
  * [Referencia de la API](https://docs.comfy.org/es/development/comfy-router/reference): el contrato generado en el que se definen estos encabezados.
  * [Limitaciones](https://docs.comfy.org/es/development/comfy-router/limitations): qué no hace Router hoy y qué usar en su lugar.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/headers.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/headers)

[Referencia de la API](https://docs.comfy.org/es/development/comfy-router/reference)[Capacidades y límites](https://docs.comfy.org/es/development/comfy-router/limitations)
