---
url: https://docs.comfy.org/es/custom-nodes/js/node-id-migration/
title: Migraci\u00f3n de ID de nodo para extensiones del frontend - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:40.450153+00:00
---

# Migración de ID de nodo para extensiones del frontend - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/node-id-migration/

Migration Guides

# Migración de ID de nodo para extensiones del frontend

Copiar páginaCopiar página

Migra extensiones del frontend de ComfyUI a ID de nodo de cadena con marca y a los centinelas de límite de subgrafo SUBGRAPH_INPUT_ID y SUBGRAPH_OUTPUT_ID.

Copiar páginaCopiar página

El frontend de ComfyUI ahora normaliza los ID de nodo locales al tipo de cadena con marca `NodeId` en los límites internos. Los flujos de trabajo serializados y las cargas útiles de la API todavía pueden contener ID numéricos, pero los ID de nodo en litegraph, como `node.id`, `LLink.origin_id` y `LLink.target_id`, deben tratarse como cadenas después de entrar al frontend. Los ID de enlace (`LLink.id`) y los ID de reenrutamiento siguen siendo números. Quienes escriben extensiones deben evitar las comparaciones numéricas con los ID de nodo. En particular, los centinelas de límite de subgrafo se exponen como ID de cadena con marca:

  * `SUBGRAPH_INPUT_ID` se serializa a partir de `-10`
  * `SUBGRAPH_OUTPUT_ID` se serializa a partir de `-20`

Compara con las cadenas `'-10'` y `'-20'`, o normaliza ambos lados a cadenas antes de comparar valores clásicos.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/node-id-migration.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/node-id-migration)

[Migración del menú contextual](https://docs.comfy.org/es/custom-nodes/js/context-menu-migration)[Migración del registro de enlaces](https://docs.comfy.org/es/custom-nodes/js/link-registration-migration)
