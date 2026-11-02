---
url: https://docs.comfy.org/es/custom-nodes/backend/snippets/
title: Ejemplos comentados - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.071531+00:00
---

# Ejemplos comentados - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/backend/snippets/

## En esta página

Volver arriba

  * Imágenes y máscaras
    * Cargar una imagen
    * Guardar un lote de imágenes
    * Invertir una máscara
    * Convertir una máscara a la forma de Image
    * Usar máscaras como capas de transparencia
  * Ruido
    * Crear variaciones de ruido



Python (backend)

# Ejemplos comentados

Copiar páginaCopiar página

Ejemplos de código comentados para nodos personalizados de ComfyUI: cargar y guardar imágenes, invertir máscaras, convertir formas de máscara, usar máscaras como capas de transparencia y crear ruido.

Copiar páginaCopiar página

Una colección creciente de fragmentos de código de ejemplo…

## 

​

Imágenes y máscaras

### 

​

Cargar una imagen

Cargar una imagen en un lote de tamaño 1 (basado en el código fuente de `LoadImage` en `nodes.py`)
    
    
    i = Image.open(image_path)
    i = ImageOps.exif_transpose(i)
    if i.mode == 'I':
        i = i.point(lambda i: i * (1 / 255))
    image = i.convert("RGB")
    image = np.array(image).astype(np.float32) / 255.0
    image = torch.from_numpy(image)[None,]
    

### 

​

Guardar un lote de imágenes

Guardar un lote de imágenes (basado en el código fuente de `SaveImage` en `nodes.py`)
    
    
    for (batch_number, image) in enumerate(images):
        i = 255. * image.cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        filepath = # alguna ruta que tenga en cuenta el número de lote
        img.save(filepath)
    

### 

​

Invertir una máscara

Invertir una máscara es un proceso sencillo. Como las máscaras están normalizadas al rango [0,1]:
    
    
    mask = 1.0 - mask
    

### 

​

Convertir una máscara a la forma de Image
    
    
    # Queremos [B,H,W,C] con C = 1
    if len(mask.shape)==2: # tenemos [H,W], así que insertamos B y C como dimensión 1
        mask = mask[None,:,:,None]
    elif len(mask.shape)==3 and mask.shape[2]==1: # tenemos [H,W,C]
        mask = mask[None,:,:,:]
    elif len(mask.shape)==3:                      # tenemos [B,H,W]
        mask = mask[:,:,:,None]
    

### 

​

Usar máscaras como capas de transparencia

Cuando se usan para tareas como inpainting o segmentación, los valores de MASK terminan redondeándose al entero más cercano para que sean binarios: 0 indica las regiones que se deben ignorar y 1 las regiones objetivo. Sin embargo, esto no ocurre hasta que la MASK se pasa a esos nodos. Esta flexibilidad te permite usar las MASK como lo harías en fotografía digital, es decir, como una capa de transparencia:
    
    
    # Invertir la máscara de vuelta a la capa de transparencia original
    mask = 1.0 - mask
    
    # Añadir una dimensión singleton a `C` (canales)
    mask = mask.unsqueeze(-1)
    
    # Concatenar ("cat") a lo largo de la dimensión `C`
    rgba_image = torch.cat((rgb_image, mask), dim=-1)
    

## 

​

Ruido

### 

​

Crear variaciones de ruido

Aquí tienes un ejemplo de creación de un objeto de ruido que mezcla el ruido de dos fuentes. Se podría usar para crear ligeras variaciones de ruido variando `weight2`.
    
    
    class Noise_MixedNoise:
        def __init__(self, nosie1, noise2, weight2):
            self.noise1  = noise1
            self.noise2  = noise2
            self.weight2 = weight2
    
        @property
        def seed(self): return self.noise1.seed
    
        def generate_noise(self, input_latent:torch.Tensor) -> torch.Tensor:
            noise1 = self.noise1.generate_noise(input_latent)
            noise2 = self.noise2.generate_noise(input_latent)
            return noise1 * (1.0-self.weight2) + noise2 * (self.weight2)
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/backend/snippets.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/backend/snippets)

[Tensores](https://docs.comfy.org/es/custom-nodes/backend/tensors)[Inversión del modelo de ejecución](https://docs.comfy.org/es/development/comfyui-server/execution_model_inversion_guide)
