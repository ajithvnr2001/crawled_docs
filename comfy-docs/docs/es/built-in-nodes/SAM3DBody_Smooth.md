---
url: https://docs.comfy.org/es/built-in-nodes/SAM3DBody_Smooth/
title: Suavizar datos de pose corporal SAM3D - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:25.656029+00:00
---

# Suavizar datos de pose corporal SAM3D - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SAM3DBody_Smooth/

Detección

# Suavizar datos de pose corporal SAM3D - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Smooth SAM3D Body Pose Data reduce el jitter entre fotogramas en una secuencia de poses corporales 3D al promediar el movimiento a lo largo del tiempo.

Copiar páginaCopiar página

Smooth SAM3D Body Pose Data reduce el jitter entre fotogramas en una secuencia de poses corporales 3D al promediar el movimiento a lo largo del tiempo. Los datos de cámara y apariencia se suavizan por completo, mientras que la geometría de la malla se suaviza menos cuando el sujeto rota rápidamente, de modo que los giros rápidos no se aplanan.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`mhr_pose_data`| La secuencia de datos de pose MHR que se va a suavizar, que contiene parámetros del modelo, parámetros de forma, parámetros de expresión, disposición de puntos clave MHR70 y datos de malla relacionados.| MHR_POSE_DATA| Sí| —  
`intensidad`| Fuerza de suavizado. 0 = sin procesar, 1 = suavizado. (predeterminado: 1.0)| FLOAT| Sí| 0.0 a 1.0 (paso 0.05)  
`método`| gaussian: promedio ponderado simétrico, el mejor suavizador de propósito general.  
savgol: ajuste polinomial deslizante, conserva picos pronunciados. (predeterminado: “savgol”)| COMBO| Sí| ”gaussian"  
"savgol”  
`ventana`| Ventana temporal en fotogramas (valores impares). (predeterminado: 7)| INT| Sí| 1 a 51 (valores impares, paso 2)  
`rotation_threshold_degrees`| Desactiva el suavizado para esta tasa de rotación de la raíz (grados/fotograma) para conservar giros rápidos. 30° se adapta a la mayoría del contenido; los valores bajos podrían desactivar el suavizado en jitter ordinario y afectar silenciosamente la calidad. 0 = desactivar. (predeterminado: 30.0)| FLOAT| Sí| 0.0 a 90.0 (paso 1.0)  
  
Nota: Cuando `strength` es 0.0 o menor, o `window` es 1 o menor, el nodo devuelve los datos de entrada sin cambios. La entrada debe contener al menos 2 fotogramas y datos de puntos clave; de lo contrario, el nodo devuelve los datos de entrada sin cambios. Cuando `rotation_threshold_degrees` es 0.0, el mecanismo de reducción del suavizado basado en rotación se desactiva.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`mhr_pose_data`| La secuencia de datos de pose MHR suavizada con jitter entre fotogramas reducido.| MHR_POSE_DATA  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/es.md)

* * *

**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SAM3DBody_Smooth.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SAM3DBody_Smooth)

[Renderizar pose corporal 3D](https://docs.comfy.org/es/built-in-nodes/SAM3DBody_Render)[Dibujar puntos clave SDPose](https://docs.comfy.org/es/built-in-nodes/SDPoseDrawKeypoints)
