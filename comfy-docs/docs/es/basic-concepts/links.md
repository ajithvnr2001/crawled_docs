---
url: https://docs.comfy.org/es/basic-concepts/links/
title: Enlaces de ComfyUI: c\u00f3mo funcionan las conexiones entre nodos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:29.607886+00:00
---

# Enlaces de ComfyUI: cómo funcionan las conexiones entre nodos - ComfyUI

> Source: https://docs.comfy.org/es/basic-concepts/links/

## En esta página

Volver arriba

  * Los enlaces conectan nodos
    * Nodo Reroute
  * Codificación por colores



Conceptos básicos

# Enlaces de ComfyUI: cómo funcionan las conexiones entre nodos

Copiar páginaCopiar página

Aprende cómo los enlaces conectan nodos en ComfyUI, cómo cambiar su estilo de dibujo y cómo el nodo Reroute mantiene legible el flujo.

Copiar páginaCopiar página

## 

​

Los enlaces conectan nodos

En ComfyUI, las líneas o curvas que se dibujan entre los nodos se llaman _**enlaces**_ (también conocidos como _**conexiones**_ o cables). Transportan datos desde la salida de un nodo hasta la entrada de otro nodo, definiendo el flujo de tu flujo de trabajo. Los enlaces se pueden mostrar con varios estilos visuales: curvas, ángulos rectos, líneas rectas u ocultos por completo. ![Estilos de enlace](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/link_styles.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=1d678959a9c5bd80d68231d5b6fed78d) Para cambiar el estilo de los enlaces, ve a **Menú de configuración** → **Display (Lite Graph)** → **Gráfico** → **Modo de renderizado de enlace**. ![Ajuste del modo de renderizado](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/render_mode.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=25d9de19b526f8ec618a9b5e9ed87ed9) También puedes ocultar temporalmente todos los enlaces desde el **Menú del lienzo**. ![Menú del lienzo](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/canvas_menu.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=3925615b50749cbd3f7ed8c0b320d5eb)

Mostrar los enlaces es especialmente útil cuando aprendes, compartes o depuras un flujo de trabajo. Hacen visible el flujo de datos de un vistazo. Para flujos de trabajo finalizados que no están pensados para editarse, ocultar los enlaces puede reducir el desorden visual.

### 

​

Nodo Reroute

Cuando un flujo de trabajo se vuelve complejo, los cables de los enlaces pueden superponerse o pasar por detrás de los nodos, lo que dificulta la lectura. El nodo **Reroute** te permite redirigir manualmente un cable a través de cualquier punto del espacio 2D del gráfico, manteniendo la disposición limpia y legible. ![Nodo Reroute de ComfyUI](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=d713aae29a8454af5a671d07e0c35ab1) ComfyUI también tiene una función nativa de reenrutado integrada en el lienzo del gráfico. Recomendamos usarla para los flujos de trabajo nuevos. ![Reenrutado nativo de ComfyUI](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/native_reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4d0e70a8300bdd79f2d6a623b40306f8)

## 

​

Codificación por colores

Cada tipo de dato en ComfyUI tiene un color distinto. Los puertos de entrada y salida de los nodos, así como los cables de enlace que los conectan, comparten este mismo esquema de colores. **Solo puedes conectar puertos del mismo color**. Esto garantiza la seguridad de tipos en todo tu flujo de trabajo. ![Tipos de datos de los nodos de ComfyUI](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5)

Tipo de dato| Color  
---|---  
Modelo de difusión| Lavanda  
Modelo CLIP| Amarillo  
Modelo VAE| Rosa  
Acondicionamiento| Naranja  
Imagen latente| Rosado  
Imagen de píxeles| Azul  
Máscara| Verde  
Número (entero o flotante)| Gris  
Malla| Verde brillante  
  
¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/basic-concepts/links.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/basic-concepts/links)

[Propiedades](https://docs.comfy.org/es/basic-concepts/properties)[Modelos](https://docs.comfy.org/es/basic-concepts/models)
