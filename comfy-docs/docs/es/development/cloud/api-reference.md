---
url: https://docs.comfy.org/es/development/cloud/api-reference/
title: Referencia de la API de Cloud - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:53.146547+00:00
---

# Referencia de la API de Cloud - ComfyUI

> Source: https://docs.comfy.org/es/development/cloud/api-reference/

## En esta página

Volver arriba

  * Configuración
  * Información de objetos
  * Subir entradas
    * Subir directamente (multipart)
    * Subir una máscara
  * Ejecutar flujos de trabajo
    * Enviar flujo de trabajo
    * Usar nodos asociados
    * Modificar las entradas del flujo de trabajo
  * Comprobar el estado de la tarea
  * WebSocket para el progreso en tiempo real
    * Tipos de mensajes de WebSocket
    * Mensajes binarios (vistas previas de imagen)
  * Descargar las salidas
  * Ejemplo completo de extremo a extremo
  * Gestión de la cola
    * Obtener el estado de la cola
    * Cancelar una tarea
    * Interrumpir la ejecución actual
  * Manejo de errores
    * Errores HTTP
    * Errores de ejecución



v1 Cloud API (deprecated)

# Referencia de la API de Cloud

Copiar páginaCopiar página

Referencia completa de la API de Comfy Cloud con ejemplos de código

Copiar páginaCopiar página

**Obsoleto:** La API de Cloud v1 está obsoleta en favor de [Comfy API v2](https://docs.comfy.org/es/api-reference/v2/overview). Los endpoints, los formatos de solicitud y respuesta, y el comportamiento pueden modificarse sin previo aviso. Algunos endpoints se mantienen por compatibilidad con ComfyUI local, pero pueden tener una semántica distinta (por ejemplo, campos ignorados).

Esta página ofrece ejemplos completos de las operaciones más habituales de la API de Comfy Cloud.

**Suscripción requerida:** Ejecutar flujos de trabajo mediante la API requiere una suscripción activa a Comfy Cloud. Consulta los [planes de precios](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) para más detalles.

## 

​

Configuración

Todos los ejemplos usan estas importaciones y esta configuración comunes:

curl

TypeScript

Python
    
    
    export COMFY_CLOUD_API_KEY="your-api-key"
    export BASE_URL="https://cloud.comfy.org"
    
    
    
    import { readFile, writeFile } from "fs/promises";
    
    const BASE_URL = "https://cloud.comfy.org";
    const API_KEY = process.env.COMFY_CLOUD_API_KEY!;
    
    function getHeaders(): HeadersInit {
      return {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json",
      };
    }
    
    
    
    import os
    import requests
    import json
    import time
    import asyncio
    import aiohttp
    
    BASE_URL = "https://cloud.comfy.org"
    API_KEY = os.environ["COMFY_CLOUD_API_KEY"]
    
    def get_headers():
        return {
            "X-API-Key": API_KEY,
            "Content-Type": "application/json"
        }
    

* * *

## 

​

Información de objetos

Recupera las definiciones de nodos disponibles. Esto es útil para entender qué nodos están disponibles y sus especificaciones de entrada y salida.

curl

TypeScript

Python
    
    
    curl -X GET "$BASE_URL/api/object_info" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY"
    
    
    
    async function getObjectInfo(): Promise<Record<string, any>> {
      const response = await fetch(`${BASE_URL}/api/object_info`, {
        headers: getHeaders(),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    }
    
    const objectInfo = await getObjectInfo();
    console.log(`Available nodes: ${Object.keys(objectInfo).length}`);
    
    const ksampler = objectInfo["KSampler"] ?? {};
    console.log(`KSampler inputs: ${Object.keys(ksampler.input?.required ?? {})}`);
    
    
    
    def get_object_info():
        """Obtiene todas las definiciones de nodos disponibles desde la nube."""
        response = requests.get(
            f"{BASE_URL}/api/object_info",
            headers=get_headers()
        )
        response.raise_for_status()
        return response.json()
    
    # Obtiene todos los nodos
    object_info = get_object_info()
    print(f"Available nodes: {len(object_info)}")
    
    # Obtiene la definición de un nodo específico
    ksampler = object_info.get("KSampler", {})
    inputs = list(ksampler.get('input', {}).get('required', {}).keys())
    print(f"KSampler inputs: {inputs}")
    

* * *

## 

​

Subir entradas

Sube imágenes, máscaras u otros archivos para usarlos en flujos de trabajo.

### 

​

Subir directamente (multipart)

curl

TypeScript

Python
    
    
    curl -X POST "$BASE_URL/api/upload/image" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY" \
      -F "image=@my_image.png" \
      -F "type=input" \
      -F "overwrite=true"
    
    
    
    async function uploadInput(
      filePath: string,
      inputType: string = "input"
    ): Promise<{ name: string; subfolder: string }> {
      const file = await readFile(filePath);
      const formData = new FormData();
      formData.append("image", new Blob([file]), filePath.split("/").pop());
      formData.append("type", inputType);
      formData.append("overwrite", "true");
    
      const response = await fetch(`${BASE_URL}/api/upload/image`, {
        method: "POST",
        headers: { "X-API-Key": API_KEY },
        body: formData,
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    }
    
    const result = await uploadInput("my_image.png");
    console.log(`Uploaded: ${result.name} to ${result.subfolder}`);
    
    
    
    def upload_input(file_path: str, input_type: str = "input") -> dict:
        """Sube un archivo directamente a la nube.
        
        Argumentos:
            file_path: Ruta al archivo que se va a subir
            input_type: "input" para imágenes, "temp" para archivos temporales
            
        Devuelve:
            Respuesta de subida con el nombre de archivo y la subcarpeta
        """
        with open(file_path, "rb") as f:
            files = {"image": f}
            data = {"type": input_type, "overwrite": "true"}
            
            response = requests.post(
                f"{BASE_URL}/api/upload/image",
                headers={"X-API-Key": API_KEY},  # Sin Content-Type para multipart
                files=files,
                data=data
            )
        response.raise_for_status()
        return response.json()
    
    # Subir una imagen
    result = upload_input("my_image.png")
    print(f"Uploaded: {result['name']} to {result['subfolder']}")
    

### 

​

Subir una máscara

La API acepta el parámetro `subfolder` por compatibilidad, pero el almacenamiento en la nube lo ignora. Todos los archivos se guardan en un espacio de nombres plano con direccionamiento por contenido.

curl

TypeScript

Python
    
    
    curl -X POST "$BASE_URL/api/upload/mask" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY" \
      -F "image=@mask.png" \
      -F "type=input" \
      -F "subfolder=clipspace" \
      -F 'original_ref={"filename":"my_image.png","subfolder":"","type":"input"}'
    
    
    
    async function uploadMask(
      filePath: string,
      originalRef: { filename: string; subfolder: string; type: string }
    ): Promise<{ name: string; subfolder: string }> {
      const file = await readFile(filePath);
      const formData = new FormData();
      formData.append("image", new Blob([file]), filePath.split("/").pop());
      formData.append("type", "input");
      formData.append("subfolder", "clipspace");
      formData.append("original_ref", JSON.stringify(originalRef));
    
      const response = await fetch(`${BASE_URL}/api/upload/mask`, {
        method: "POST",
        headers: { "X-API-Key": API_KEY },
        body: formData,
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    }
    
    const maskResult = await uploadMask("mask.png", {
      filename: "my_image.png",
      subfolder: "",
      type: "input",
    });
    console.log(`Uploaded mask: ${maskResult.name}`);
    
    
    
    def upload_mask(file_path: str, original_ref: dict) -> dict:
        """Sube una máscara asociada a una imagen original.
        
        Argumentos:
            file_path: Ruta al archivo de máscara
            original_ref: Referencia a la imagen original {"filename": "...", "subfolder": "...", "type": "..."}
        """
        with open(file_path, "rb") as f:
            files = {"image": f}
            data = {
                "type": "input",
                "subfolder": "clipspace",
                "original_ref": json.dumps(original_ref)
            }
            
            response = requests.post(
                f"{BASE_URL}/api/upload/mask",
                headers={"X-API-Key": API_KEY},
                files=files,
                data=data
            )
        response.raise_for_status()
        return response.json()
    

* * *

## 

​

Ejecutar flujos de trabajo

Envía un flujo de trabajo para ejecutarlo.

**Envíos simultáneos admitidos:** Según tu nivel de suscripción, puedes enviar varios flujos de trabajo sin esperar a que terminen las tareas anteriores. Las tareas se ejecutan en paralelo hasta el límite de tu nivel. Las tareas adicionales se ponen en cola automáticamente. Consulta [Tareas simultáneas](https://docs.comfy.org/es/development/deploy/cloud-usage#tareas-simult%C3%A1neas) para ver los detalles y los límites de simultaneidad.

### 

​

Enviar flujo de trabajo

curl

TypeScript

Python
    
    
    curl -X POST "$BASE_URL/api/prompt" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"prompt": '"$(cat workflow_api.json)"'}'
    
    
    
    async function submitWorkflow(workflow: Record<string, any>): Promise<string> {
      const response = await fetch(`${BASE_URL}/api/prompt`, {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify({ prompt: workflow }),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const result = await response.json();
    
      if (result.error) {
        throw new Error(`Workflow error: ${result.error}`);
      }
      return result.prompt_id;
    }
    
    const workflow = JSON.parse(await readFile("workflow_api.json", "utf-8"));
    const promptId = await submitWorkflow(workflow);
    console.log(`Submitted job: ${promptId}`);
    
    
    
    def submit_workflow(workflow: dict) -> str:
        """Envía un flujo de trabajo y devuelve el prompt_id (ID de trabajo).
        
        Argumentos:
            workflow: flujo de trabajo de ComfyUI en formato API
            
        Devuelve:
            prompt_id para hacer seguimiento de la tarea
        """
        response = requests.post(
            f"{BASE_URL}/api/prompt",
            headers=get_headers(),
            json={"prompt": workflow}
        )
        response.raise_for_status()
        result = response.json()
        
        if "error" in result:
            raise ValueError(f"Workflow error: {result['error']}")
        
        return result["prompt_id"]
    
    # Cargar y enviar un flujo de trabajo
    with open("workflow_api.json") as f:
        workflow = json.load(f)
    
    prompt_id = submit_workflow(workflow)
    print(f"Submitted job: {prompt_id}")
    

### 

​

Usar nodos asociados

Si tu flujo de trabajo contiene [nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview) (nodos que llaman a servicios de IA externos como Flux Pro, Ideogram, etc.), debes incluir tu [clave API de Comfy](https://docs.comfy.org/es/development/api-development/getting-an-api-key) en el campo `extra_data` de la carga útil de la solicitud.

El frontend de ComfyUI incluye automáticamente tu clave API en `extra_data` cuando ejecutas flujos de trabajo en el navegador. Esta sección solo es relevante cuando llamas a la API directamente.

curl

TypeScript

Python
    
    
    curl -X POST "$BASE_URL/api/prompt" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "prompt": '"$(cat workflow_api.json)"',
        "extra_data": {
          "api_key_comfy_org": "your-comfy-api-key"
        }
      }'
    
    
    
    async function submitWorkflowWithPartnerNodes(
      workflow: Record<string, any>,
      apiKey: string
    ): Promise<string> {
      const response = await fetch(`${BASE_URL}/api/prompt`, {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify({
          prompt: workflow,
          extra_data: {
            api_key_comfy_org: apiKey,
          },
        }),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const result = await response.json();
      return result.prompt_id;
    }
    
    // Úsalo cuando el flujo de trabajo contenga nodos asociados (p. ej., Flux Pro, Ideogram, etc.)
    const promptId = await submitWorkflowWithPartnerNodes(workflow, API_KEY);
    
    
    
    def submit_workflow_with_partner_nodes(workflow: dict, api_key: str) -> str:
        """Envía un flujo de trabajo que usa nodos asociados.
        
        Argumentos:
            workflow: flujo de trabajo de ComfyUI en formato API
            api_key: tu clave API de platform.comfy.org
            
        Devuelve:
            prompt_id para hacer seguimiento de la tarea
        """
        response = requests.post(
            f"{BASE_URL}/api/prompt",
            headers=get_headers(),
            json={
                "prompt": workflow,
                "extra_data": {
                    "api_key_comfy_org": api_key
                }
            }
        )
        response.raise_for_status()
        return response.json()["prompt_id"]
    
    # Úsalo cuando el flujo de trabajo contenga nodos asociados
    prompt_id = submit_workflow_with_partner_nodes(workflow, API_KEY)
    

Genera tu clave API en [platform.comfy.org](https://platform.comfy.org/login). Es la misma clave que se usa para la autenticación de la API de Comfy Cloud (encabezado `X-API-Key`). Consulta [Obtener una clave API](https://docs.comfy.org/es/development/api-development/getting-an-api-key) para ver las instrucciones paso a paso.

### 

​

Modificar las entradas del flujo de trabajo

TypeScript

Python
    
    
    function setWorkflowInput(
      workflow: Record<string, any>,
      nodeId: string,
      inputName: string,
      value: any
    ): Record<string, any> {
      if (workflow[nodeId]) {
        workflow[nodeId].inputs[inputName] = value;
      }
      return workflow;
    }
    
    // Ejemplo: establecer la semilla y el prompt
    let workflow = JSON.parse(await readFile("workflow_api.json", "utf-8"));
    workflow = setWorkflowInput(workflow, "3", "seed", 12345);
    workflow = setWorkflowInput(workflow, "6", "text", "a beautiful landscape");
    
    
    
    def set_workflow_input(workflow: dict, node_id: str, input_name: str, value) -> dict:
        """Modifica el valor de una entrada del flujo de trabajo.
        
        Argumentos:
            workflow: el diccionario del flujo de trabajo
            node_id: ID del nodo que se va a modificar
            input_name: nombre del campo de entrada
            value: valor nuevo
            
        Devuelve:
            flujo de trabajo modificado
        """
        if node_id in workflow:
            workflow[node_id]["inputs"][input_name] = value
        return workflow
    
    # Ejemplo: establecer la semilla y el prompt
    workflow = set_workflow_input(workflow, "3", "seed", 12345)
    workflow = set_workflow_input(workflow, "6", "text", "a beautiful landscape")
    

* * *

## 

​

Comprobar el estado de la tarea

Consulta periódicamente hasta que la tarea finalice. **Valores del estado de la tarea:** La API devuelve uno de los siguientes valores de estado:

Estado| Descripción  
---|---  
`success`| La tarea finalizó correctamente. Estado terminal  
`error`| La tarea falló. Estado terminal  
`non_retryable_error`| La tarea falló y reintentar no ayudará. Estado terminal  
`lost`| La tarea desapareció antes de poder finalizar. Estado terminal  
`cancelled`| La tarea se canceló. Estado terminal  
  
Esos cinco son los estados terminales. Todo lo demás significa que la tarea aún está en curso, incluidos `submitted`, `queued_waiting`, `preparing`, `executing` y estados de transición como `cancel_requested`. Consulta periódicamente hasta que veas un valor terminal en lugar de buscar coincidencias con los nombres de los estados en curso.

curl

TypeScript

Python
    
    
    # Consulta periódicamente la finalización de la tarea
    curl -X GET "$BASE_URL/api/job/{prompt_id}/status" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY"
    
    # Ejemplos de respuesta:
    # {"status": "queued_waiting"}       - La tarea está en cola
    # {"status": "executing"}            - La tarea se está ejecutando actualmente
    # {"status": "success"}              - La tarea finalizó correctamente
    # {"status": "error"}                - La tarea encontró un error
    # {"status": "non_retryable_error"}  - La tarea falló, reintentar no ayudará
    # {"status": "lost"}                 - La tarea desapareció antes de finalizar
    # {"status": "cancelled"}            - La tarea se canceló
    
    
    
    interface JobStatus {
      status: string;
    }
    
    async function getJobStatus(promptId: string): Promise<JobStatus> {
      const response = await fetch(`${BASE_URL}/api/job/${promptId}/status`, {
        headers: getHeaders(),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    }
    
    async function pollForCompletion(
      promptId: string,
      timeout: number = 300,
      pollInterval: number = 2000
    ): Promise<void> {
      const startTime = Date.now();
    
      while (Date.now() - startTime < timeout * 1000) {
        const { status } = await getJobStatus(promptId);
    
        if (status === "success") {
          return;
        } else if (
          ["error", "non_retryable_error", "lost", "cancelled"].includes(status)
        ) {
          throw new Error(`Job failed with status: ${status}`);
        }
    
        await new Promise((resolve) => setTimeout(resolve, pollInterval));
      }
    
      throw new Error(`Job ${promptId} did not complete within ${timeout}s`);
    }
    
    await pollForCompletion(promptId);
    console.log("Job completed!");
    
    
    
    def get_job_status(prompt_id: str) -> str:
        """Obtiene el estado actual de una tarea."""
        response = requests.get(
            f"{BASE_URL}/api/job/{prompt_id}/status",
            headers=get_headers()
        )
        response.raise_for_status()
        return response.json()["status"]
    
    def poll_for_completion(prompt_id: str, timeout: int = 300, poll_interval: float = 2.0) -> None:
        """Consulta periódicamente hasta que la tarea se complete o se agote el tiempo de espera."""
        start_time = time.time()
    
        while time.time() - start_time < timeout:
            status = get_job_status(prompt_id)
    
            if status == "success":
                return
            elif status in ("error", "non_retryable_error", "lost", "cancelled"):
                raise RuntimeError(f"Job failed with status: {status}")
    
            time.sleep(poll_interval)
    
        raise TimeoutError(f"Job {prompt_id} did not complete within {timeout}s")
    
    poll_for_completion(prompt_id)
    print("Job completed!")
    

* * *

## 

​

WebSocket para el progreso en tiempo real

Conéctate al WebSocket para recibir actualizaciones de ejecución en tiempo real.

El parámetro `clientId` se ignora actualmente: todas las conexiones de un mismo usuario reciben los mismos mensajes. Pasa un `clientId` único para mantener la compatibilidad a futuro.

TypeScript

Python
    
    
    async function listenForCompletion(
      promptId: string,
      timeout: number = 300000
    ): Promise<Record<string, any>> {
      const wsUrl = `wss://cloud.comfy.org/ws?clientId=${crypto.randomUUID()}&token=${API_KEY}`;
      const outputs: Record<string, any> = {};
    
      return new Promise((resolve, reject) => {
        const ws = new WebSocket(wsUrl);
        const timer = setTimeout(() => {
          ws.close();
          reject(new Error(`Job did not complete within ${timeout / 1000}s`));
        }, timeout);
    
        ws.onmessage = (event) => {
          // Los frames binarios llevan imágenes de vista previa, no JSON.
          if (typeof event.data !== "string") return;
    
          const data = JSON.parse(event.data);
          const msgType = data.type;
          const msgData = data.data ?? {};
    
          // Filtrar a nuestra tarea
          if (msgData.prompt_id !== promptId) return;
    
          if (msgType === "executing") {
            const node = msgData.node;
            if (node) {
              console.log(`Executing node: ${node}`);
            } else {
              console.log("Execution complete");
            }
          } else if (msgType === "progress") {
            console.log(`Progress: ${msgData.value}/${msgData.max}`);
          } else if (msgType === "executed" && msgData.output) {
            outputs[msgData.node] = msgData.output;
          } else if (msgType === "execution_success") {
            console.log("Job completed successfully!");
            clearTimeout(timer);
            ws.close();
            resolve(outputs);
          } else if (msgType === "execution_error") {
            const errorMsg = msgData.exception_message ?? "Unknown error";
            clearTimeout(timer);
            ws.close();
            reject(new Error(`Execution error: ${errorMsg}`));
          }
        };
    
        ws.onerror = (err) => {
          clearTimeout(timer);
          reject(err);
        };
      });
    }
    
    // Espera la finalización y recopila las salidas
    const outputs = await listenForCompletion(promptId);
    
    
    
    import asyncio
    import aiohttp
    import json
    import uuid
    
    async def listen_for_completion(prompt_id: str, timeout: float = 300.0) -> dict:
        """Conéctate al WebSocket y escucha la finalización de la tarea.
    
        Devuelve:
            Las salidas finales de la tarea
        """
        ws_url = BASE_URL.replace("https://", "wss://")
        client_id = str(uuid.uuid4())
        ws_url = f"{ws_url}/ws?clientId={client_id}&token={API_KEY}"
    
        outputs = {}
    
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(ws_url) as ws:
                async def receive_messages():
                    async for msg in ws:
                        if msg.type == aiohttp.WSMsgType.TEXT:
                            data = json.loads(msg.data)
                            msg_type = data.get("type")
                            msg_data = data.get("data", {})
    
                            # Filtrar a nuestra tarea
                            if msg_data.get("prompt_id") != prompt_id:
                                continue
    
                            if msg_type == "executing":
                                node = msg_data.get("node")
                                if node:
                                    print(f"Executing node: {node}")
    
                            elif msg_type == "progress":
                                value = msg_data.get("value", 0)
                                max_val = msg_data.get("max", 100)
                                print(f"Progress: {value}/{max_val}")
    
                            elif msg_type == "executed":
                                node_id = msg_data.get("node")
                                output = msg_data.get("output", {})
                                if output:
                                    outputs[node_id] = output
    
                            elif msg_type == "execution_success":
                                print("Job completed successfully!")
                                return outputs
    
                            elif msg_type == "execution_error":
                                error_msg = msg_data.get("exception_message", "Unknown error")
                                raise RuntimeError(f"Execution error: {error_msg}")
    
                        elif msg.type == aiohttp.WSMsgType.ERROR:
                            raise RuntimeError(f"WebSocket error: {ws.exception()}")
    
                try:
                    return await asyncio.wait_for(receive_messages(), timeout=timeout)
                except asyncio.TimeoutError:
                    raise TimeoutError(f"Job did not complete within {timeout}s")
    
    # Espera la finalización y recopila las salidas
    outputs = await listen_for_completion(prompt_id)
    

### 

​

Tipos de mensajes de WebSocket

Los mensajes se envían como tramas de texto JSON, a menos que se indique lo contrario.

Tipo| Descripción  
---|---  
`status`| Actualización del estado de la cola con el conteo `queue_remaining`  
`notification`| Mensaje de estado claro para el usuario (el campo `value` contiene texto como “Executing workflow…”)  
`execution_start`| La ejecución del flujo de trabajo ha comenzado  
`executing`| Un nodo específico se está ejecutando ahora (el ID del nodo va en el campo `node`)  
`progress`| Progreso de los pasos dentro de un nodo (`value`/`max` para los pasos de muestreo)  
`progress_state`| Estado de progreso extendido con metadatos del nodo (objeto `nodes` anidado)  
`executed`| El nodo se completó con salidas (imágenes, video, etc. en el campo `output`)  
`execution_cached`| Nodos omitidos porque sus salidas están en caché (array `nodes`)  
`execution_success`| Todo el flujo de trabajo se completó correctamente  
`execution_error`| El flujo de trabajo falló (incluye `exception_type`, `exception_message`, `traceback`)  
`execution_interrupted`| El usuario canceló el flujo de trabajo  
  
#### 

​

Mensajes binarios (vistas previas de imagen)

Durante la generación de imágenes, ComfyUI envía **tramas binarias de WebSocket** que contienen vistas previas de imagen. Son datos binarios sin procesar (no JSON):

Tipo binario| Valor| Descripción  
---|---|---  
`PREVIEW_IMAGE`| `1`| Vista previa en curso durante el muestreo de difusión  
`TEXT`| `3`| Salida de texto de los nodos (texto de progreso)  
`PREVIEW_IMAGE_WITH_METADATA`| `4`| Vista previa de imagen con metadatos de contexto del nodo  
  
**Formatos de las tramas binarias** (todos los enteros son big-endian):

  * PREVIEW_IMAGE (1)

  * TEXT (3)

  * PREVIEW_WITH_METADATA (4)




Desplazamiento| Tamaño| Campo| Descripción  
---|---|---|---  
0| 4 bytes| `type`| `0x00000001`  
4| 4 bytes| `image_type`| Código de formato (1=JPEG, 2=PNG)  
8| variable| `image_data`| Bytes de imagen sin procesar  
  
Desplazamiento| Tamaño| Campo| Descripción  
---|---|---|---  
0| 4 bytes| `type`| `0x00000003`  
4| 4 bytes| `node_id_len`| Longitud de la cadena node_id  
8| N bytes| `node_id`| ID del nodo codificado en UTF-8  
8+N| variable| `text`| Texto de progreso codificado en UTF-8  
  
Desplazamiento| Tamaño| Campo| Descripción  
---|---|---|---  
0| 4 bytes| `type`| `0x00000004`  
4| 4 bytes| `metadata_len`| Longitud del JSON de metadatos  
8| N bytes| `metadata`| JSON en UTF-8 (ver abajo)  
8+N| variable| `image_data`| Bytes JPEG/PNG sin procesar  
  
**Estructura del JSON de metadatos:**
    
    
    {
      "node_id": "3",
      "display_node_id": "3",
      "real_node_id": "3",
      "prompt_id": "abc-123",
      "parent_node_id": null
    }
    

Consulta la [especificación OpenAPI](https://docs.comfy.org/es/development/cloud/openapi) para ver las definiciones completas del esquema de cada tipo de mensaje JSON.

* * *

## 

​

Descargar las salidas

Recupera los archivos generados cuando la tarea haya finalizado.

curl

TypeScript

Python
    
    
    # Paso 1: lee el destino 302. No uses -L aquí: seguir la redirección
    # reenviaría tu clave API al host de almacenamiento.
    SIGNED_URL=$(curl -s -o /dev/null -w '%{redirect_url}' \
      "$BASE_URL/api/view?filename=output.png&subfolder=&type=output" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY")
    
    # Paso 2: la URL firmada tiene su propia autorización, así que no envíes encabezados.
    curl -s "$SIGNED_URL" -o output.png
    
    
    
    import { mkdir, writeFile } from "fs/promises";
    
    async function downloadOutput(
      filename: string,
      subfolder: string = "",
      outputType: string = "output"
    ): Promise<ArrayBuffer> {
      const params = new URLSearchParams({ filename, subfolder, type: outputType });
      // Obtén la URL de redirección
      const response = await fetch(`${BASE_URL}/api/view?${params}`, {
        headers: { "X-API-Key": API_KEY },
        redirect: "manual",
      });
      if (response.status !== 302) throw new Error(`HTTP ${response.status}`);
      const signedUrl = response.headers.get("location")!;
    
      // Obtén el archivo desde la URL firmada
      const fileResponse = await fetch(signedUrl);
      if (!fileResponse.ok) throw new Error(`HTTP ${fileResponse.status}`);
      return fileResponse.arrayBuffer();
    }
    
    async function saveOutputs(
      outputs: Record<string, any>,
      outputDir: string = "."
    ): Promise<void> {
      await mkdir(outputDir, { recursive: true });
      for (const nodeOutputs of Object.values(outputs)) {
        for (const key of ["images", "video", "audio"]) {
          for (const fileInfo of (nodeOutputs as any)[key] ?? []) {
            const data = await downloadOutput(
              fileInfo.filename,
              fileInfo.subfolder ?? "",
              fileInfo.type ?? "output"
            );
            const path = `${outputDir}/${fileInfo.filename}`;
            await writeFile(path, Buffer.from(data));
            console.log(`Saved: ${path}`);
          }
        }
      }
    }
    
    // Descarga todas las salidas
    await saveOutputs(outputs, "./my_outputs");
    
    
    
    def download_output(filename: str, subfolder: str = "", output_type: str = "output") -> bytes:
        """Descarga un archivo de salida.
    
        Argumentos:
            filename: Nombre del archivo
            subfolder: Ruta de la subcarpeta (normalmente vacía)
            output_type: "output" para las salidas finales, "temp" para las vistas previas
    
        Devuelve:
            Bytes del archivo
        """
        params = {
            "filename": filename,
            "subfolder": subfolder,
            "type": output_type
        }
    
        # No sigas la redirección. requests elimina Authorization en una redirección
        # entre hosts, pero mantiene los encabezados personalizados, así que X-API-Key
        # llegaría al host de almacenamiento. La URL firmada tiene su propia autorización.
        response = requests.get(
            f"{BASE_URL}/api/view",
            headers=get_headers(),
            params=params,
            allow_redirects=False
        )
        if response.status_code != 302:
            raise RuntimeError(f"Expected a 302 redirect, got {response.status_code}")
        signed_url = response.headers["Location"]
    
        file_response = requests.get(signed_url)
        file_response.raise_for_status()
        return file_response.content
    
    def save_outputs(outputs: dict, output_dir: str = "."):
        """Guarda todas las salidas de una tarea en el disco.
    
        Argumentos:
            outputs: Diccionario de salidas de la tarea (node_id -> output_data)
            output_dir: Directorio donde se guardan los archivos
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
    
        for node_id, node_outputs in outputs.items():
            for key in ("images", "video", "audio"):
                for file_info in node_outputs.get(key, []):
                    filename = file_info["filename"]
                    subfolder = file_info.get("subfolder", "")
                    output_type = file_info.get("type", "output")
    
                    data = download_output(filename, subfolder, output_type)
    
                    output_path = os.path.join(output_dir, filename)
                    with open(output_path, "wb") as f:
                        f.write(data)
                    print(f"Saved: {output_path}")
    
    # Descarga todas las salidas
    save_outputs(outputs, "./my_outputs")
    

* * *

## 

​

Ejemplo completo de extremo a extremo

Aquí tienes un ejemplo completo que integra todo:

TypeScript

Python
    
    
    import { mkdir, readFile, writeFile } from "fs/promises";
    
    const BASE_URL = "https://cloud.comfy.org";
    const API_KEY = process.env.COMFY_CLOUD_API_KEY!;
    
    function getHeaders(): HeadersInit {
      return { "X-API-Key": API_KEY, "Content-Type": "application/json" };
    }
    
    async function submitWorkflow(workflow: Record<string, any>): Promise<string> {
      const response = await fetch(`${BASE_URL}/api/prompt`, {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify({ prompt: workflow }),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return (await response.json()).prompt_id;
    }
    
    async function waitForCompletion(
      promptId: string,
      timeout: number = 300000
    ): Promise<Record<string, any>> {
      const wsUrl = `wss://cloud.comfy.org/ws?clientId=${crypto.randomUUID()}&token=${API_KEY}`;
      const outputs: Record<string, any> = {};
    
      return new Promise((resolve, reject) => {
        const ws = new WebSocket(wsUrl);
        const timer = setTimeout(() => {
          ws.close();
          reject(new Error("Job timed out"));
        }, timeout);
    
        ws.onmessage = (event) => {
          // Las tramas binarias contienen imágenes de vista previa, no JSON.
          if (typeof event.data !== "string") return;
    
          const data = JSON.parse(event.data);
          if (data.data?.prompt_id !== promptId) return;
    
          const msgType = data.type;
          const msgData = data.data ?? {};
    
          if (msgType === "progress") {
            console.log(`Progress: ${msgData.value}/${msgData.max}`);
          } else if (msgType === "executed" && msgData.output) {
            outputs[msgData.node] = msgData.output;
          } else if (msgType === "execution_success") {
            clearTimeout(timer);
            ws.close();
            resolve(outputs);
          } else if (msgType === "execution_error") {
            clearTimeout(timer);
            ws.close();
            reject(new Error(msgData.exception_message ?? "Unknown error"));
          }
        };
    
        ws.onerror = (err) => {
          clearTimeout(timer);
          reject(err);
        };
      });
    }
    
    async function downloadOutputs(
      outputs: Record<string, any>,
      outputDir: string
    ): Promise<void> {
      await mkdir(outputDir, { recursive: true });
      for (const nodeOutputs of Object.values(outputs)) {
        for (const key of ["images", "video", "audio"]) {
          for (const fileInfo of (nodeOutputs as any)[key] ?? []) {
            const params = new URLSearchParams({
              filename: fileInfo.filename,
              subfolder: fileInfo.subfolder ?? "",
              type: fileInfo.type ?? "output",
            });
            // Obtener la URL de redirección (no seguirla para evitar enviar la autenticación al almacenamiento)
            const response = await fetch(`${BASE_URL}/api/view?${params}`, {
              headers: { "X-API-Key": API_KEY },
              redirect: "manual",
            });
            if (response.status !== 302) throw new Error(`HTTP ${response.status}`);
            const signedUrl = response.headers.get("location")!;
            // Obtener desde la URL firmada sin encabezados de autenticación
            const fileResponse = await fetch(signedUrl);
            if (!fileResponse.ok) throw new Error(`HTTP ${fileResponse.status}`);
    
            const path = `${outputDir}/${fileInfo.filename}`;
            await writeFile(path, Buffer.from(await fileResponse.arrayBuffer()));
            console.log(`Downloaded: ${path}`);
          }
        }
      }
    }
    
    async function main() {
      // 1. Cargar flujo de trabajo
      const workflow = JSON.parse(await readFile("workflow_api.json", "utf-8"));
    
      // 2. Modificar parámetros del flujo de trabajo
      workflow["3"].inputs.seed = 42;
      workflow["6"].inputs.text = "a beautiful sunset over mountains";
    
      // 3. Enviar flujo de trabajo
      const promptId = await submitWorkflow(workflow);
      console.log(`Job submitted: ${promptId}`);
    
      // 4. Esperar la finalización con progreso
      const outputs = await waitForCompletion(promptId);
      console.log(`Job completed! Found ${Object.keys(outputs).length} output nodes`);
    
      // 5. Descargar salidas
      await downloadOutputs(outputs, "./outputs");
      console.log("Done!");
    }
    
    main();
    
    
    
    import os
    import requests
    import json
    import asyncio
    import aiohttp
    import uuid
    
    BASE_URL = "https://cloud.comfy.org"
    API_KEY = os.environ["COMFY_CLOUD_API_KEY"]
    
    def get_headers():
        return {"X-API-Key": API_KEY, "Content-Type": "application/json"}
    
    def upload_image(file_path: str) -> dict:
        """Sube una imagen y devuelve la referencia para usarla en flujos de trabajo."""
        with open(file_path, "rb") as f:
            response = requests.post(
                f"{BASE_URL}/api/upload/image",
                headers={"X-API-Key": API_KEY},
                files={"image": f},
                data={"type": "input", "overwrite": "true"}
            )
        response.raise_for_status()
        return response.json()
    
    def submit_workflow(workflow: dict) -> str:
        """Envía el flujo de trabajo y devuelve prompt_id."""
        response = requests.post(
            f"{BASE_URL}/api/prompt",
            headers=get_headers(),
            json={"prompt": workflow}
        )
        response.raise_for_status()
        return response.json()["prompt_id"]
    
    async def wait_for_completion(prompt_id: str, timeout: float = 300.0) -> dict:
        """Espera a que el trabajo se complete mediante WebSocket."""
        ws_url = BASE_URL.replace("https://", "wss://") + f"/ws?clientId={uuid.uuid4()}&token={API_KEY}"
        outputs = {}
        
        async with aiohttp.ClientSession() as session:
            # receive_timeout limita cada espera de una trama, así que una conexión
            # silenciosa no puede quedarse colgada más allá del plazo
            async with session.ws_connect(ws_url, receive_timeout=timeout) as ws:
                start = asyncio.get_event_loop().time()
                async for msg in ws:
                    if asyncio.get_event_loop().time() - start > timeout:
                        raise TimeoutError("Job timed out")
                    
                    if msg.type != aiohttp.WSMsgType.TEXT:
                        continue
                        
                    data = json.loads(msg.data)
                    if data.get("data", {}).get("prompt_id") != prompt_id:
                        continue
                    
                    msg_type = data.get("type")
                    msg_data = data.get("data", {})
                    
                    if msg_type == "progress":
                        print(f"Progress: {msg_data.get('value')}/{msg_data.get('max')}")
                    elif msg_type == "executed":
                        if output := msg_data.get("output"):
                            outputs[msg_data["node"]] = output
                    elif msg_type == "execution_success":
                        return outputs
                    elif msg_type == "execution_error":
                        raise RuntimeError(msg_data.get("exception_message", "Unknown error"))
        
        return outputs
    
    def download_outputs(outputs: dict, output_dir: str):
        """Descarga todos los archivos de salida."""
        os.makedirs(output_dir, exist_ok=True)
        
        for node_outputs in outputs.values():
            for key in ["images", "video", "audio"]:
                for file_info in node_outputs.get(key, []):
                    params = {
                        "filename": file_info["filename"],
                        "subfolder": file_info.get("subfolder", ""),
                        "type": file_info.get("type", "output")
                    }
                    response = requests.get(f"{BASE_URL}/api/view", headers=get_headers(), params=params)
                    response.raise_for_status()
                    
                    path = os.path.join(output_dir, file_info["filename"])
                    with open(path, "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded: {path}")
    
    async def main():
        # 1. Cargar flujo de trabajo
        with open("workflow_api.json") as f:
            workflow = json.load(f)
        
        # 2. Opcionalmente, subir imágenes de entrada
        # image_ref = upload_image("input.png")
        # workflow["1"]["inputs"]["image"] = image_ref["name"]
        
        # 3. Modificar parámetros del flujo de trabajo
        workflow["3"]["inputs"]["seed"] = 42
        workflow["6"]["inputs"]["text"] = "a beautiful sunset over mountains"
        
        # 4. Enviar flujo de trabajo
        prompt_id = submit_workflow(workflow)
        print(f"Job submitted: {prompt_id}")
        
        # 5. Esperar la finalización con progreso
        outputs = await wait_for_completion(prompt_id)
        print(f"Job completed! Found {len(outputs)} output nodes")
        
        # 6. Descargar salidas
        download_outputs(outputs, "./outputs")
        print("Done!")
    
    if __name__ == "__main__":
        asyncio.run(main())
    

* * *

## 

​

Gestión de la cola

### 

​

Obtener el estado de la cola

curl

TypeScript

Python
    
    
    curl -X GET "$BASE_URL/api/queue" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY"
    
    
    
    async function getQueue(): Promise<{
      queue_running: any[];
      queue_pending: any[];
    }> {
      const response = await fetch(`${BASE_URL}/api/queue`, {
        headers: getHeaders(),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    }
    
    const queue = await getQueue();
    console.log(`Running: ${queue.queue_running.length}`);
    console.log(`Pending: ${queue.queue_pending.length}`);
    
    
    
    def get_queue():
        """Obtiene el estado actual de la cola."""
        response = requests.get(
            f"{BASE_URL}/api/queue",
            headers=get_headers()
        )
        response.raise_for_status()
        return response.json()
    
    queue = get_queue()
    print(f"Running: {len(queue.get('queue_running', []))}")
    print(f"Pending: {len(queue.get('queue_pending', []))}")
    

### 

​

Cancelar una tarea

curl

TypeScript

Python
    
    
    curl -X POST "$BASE_URL/api/queue" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"delete": ["PROMPT_ID_HERE"]}'
    
    
    
    async function cancelJob(promptId: string): Promise<void> {
      const response = await fetch(`${BASE_URL}/api/queue`, {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify({ delete: [promptId] }),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
    }
    
    
    
    def cancel_job(prompt_id: str):
        """Cancela una tarea pendiente o en ejecución."""
        response = requests.post(
            f"{BASE_URL}/api/queue",
            headers=get_headers(),
            json={"delete": [prompt_id]}
        )
        response.raise_for_status()
        return response.json()
    

### 

​

Interrumpir la ejecución actual

curl

TypeScript

Python
    
    
    curl -X POST "$BASE_URL/api/interrupt" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY"
    
    
    
    async function interrupt(): Promise<void> {
      const response = await fetch(`${BASE_URL}/api/interrupt`, {
        method: "POST",
        headers: getHeaders(),
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
    }
    
    
    
    def interrupt():
        """Interrumpe la tarea que se está ejecutando."""
        response = requests.post(
            f"{BASE_URL}/api/interrupt",
            headers=get_headers()
        )
        response.raise_for_status()
    

* * *

## 

​

Manejo de errores

### 

​

Errores HTTP

Los endpoints de la API REST devuelven códigos de estado HTTP estándar:

Estado| Descripción  
---|---  
`400`| Solicitud inválida (flujo de trabajo inválido, campos faltantes)  
`401`| No autorizado (clave API inválida o faltante)  
`402`| Créditos insuficientes  
`429`| Suscripción inactiva  
`500`| Error interno del servidor  
  
### 

​

Errores de ejecución

Durante la ejecución de un flujo de trabajo, los errores llegan mediante el mensaje WebSocket `execution_error`. El campo `exception_type` identifica la categoría del error:

Tipo de excepción| Descripción  
---|---  
`ValidationError`| Flujo de trabajo o entradas inválidos  
`ModelDownloadError`| El modelo requerido no está disponible o la descarga falló  
`ImageDownloadError`| No se pudo descargar la imagen de entrada desde la URL  
`OOMError`| Memoria de GPU agotada  
`InsufficientFundsError`| Saldo de la cuenta demasiado bajo (para Nodos asociados)  
`InactiveSubscriptionError`| Suscripción no activa  
  
¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/cloud/api-reference.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/cloud/api-reference)

[Descripción general](https://docs.comfy.org/es/development/cloud/overview)[Especificación OpenAPI](https://docs.comfy.org/es/development/cloud/openapi)
