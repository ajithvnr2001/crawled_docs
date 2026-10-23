---
url: https://docs.comfy.org/ko/basic-concepts/models/
title: ComfyUI \ubaa8\ub378: \ud30c\uc77c, \ud3f4\ub354, \ub85c\ub354 \ub178\ub4dc - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:40.964650+00:00
---

# ComfyUI 모델: 파일, 폴더, 로더 노드 - ComfyUI

> Source: https://docs.comfy.org/ko/basic-concepts/models/

## 이 페이지에서

  * 모델의 기본 개념
    * ComfyUI에서 지원하는 모델
  * ComfyUI에서 모델 사용하기
    * 대용량 다운로드를 예상하세요
  * 메인 체크포인트 외에도
  * 모델 제거하기
  * 추가 모델 경로 추가하기
    * 구성 파일 열기
    * 예제 구조
    * 추가 커스텀 노드 경로 추가하기
  * 일반적인 문제
  * 좀 더 자세한 배경 정보가 필요하신가요?



기본 개념

# ComfyUI 모델: 파일, 폴더, 로더 노드

페이지 복사페이지 복사

모델 파일이 ComfyUI 워크플로우에 어떻게 맞춰지는지: 어디에 저장되고, 어떻게 로드하며, 일반적인 해결 방법은 무엇인지.

페이지 복사페이지 복사

## 

​

모델의 기본 개념

ComfyUI에서 **모델** 이란 실제로 워크플로를 실행하는 가중치 파일을 말합니다. 여기에는 **체크포인트** , **VAE** , **LoRA** , **ControlNet** , 업스케일러 등이 포함됩니다. 앱 설치 파일은 작으며, 이러한 파일들은 기본적으로 포함되어 있지 않습니다. 보통 **웹에서 다운로드** 한 후 `ComfyUI/models/` 아래에 배치하거나(또는 템플릿의 안내를 따르세요) 캔버스에서 올바른 **로더 노드** 를 선택하면 됩니다(이 노드들은 이름이 **Load** 로 시작하는 경우가 많습니다).

### 

​

ComfyUI에서 지원하는 모델

  * **내장/1차 지원 범위는 의도적으로 제한되어 있지만** , ComfyUI와 오픈소스 생태계가 발전함에 따라 점차 늘어납니다. 모델이 일급 지원을 받으면 보통 **[워크플로 템플릿 라이브러리](https://docs.comfy.org/ko/interface/features/template)**에 새로운 항목이 추가되며, 예상되는 그래프와 모델 조합이 표시됩니다.
  * **모든 체크포인트나 가중치 파일이 바로 사용 가능한 것은 아닙니다.** 기본적으로 지원되는 모델과 함께 쓰이는 일반적인 가중치 파일의 경우, ComfyUI를 **[최신 상태로 유지](https://docs.comfy.org/ko/installation/update_comfyui)**하고 해당 워크플로가 **[템플릿 라이브러리](https://docs.comfy.org/ko/interface/features/template)**에 있는지 확인하기 전까지는 파일이 잘못된 위치에 있다고 가정하지 마세요.
  * **그 밖의 많은 모델은 커뮤니티의 커스텀 노드를 통해 활성화됩니다.** 경로, 로더 노드, 그래프 레이아웃은 이 페이지의 일반적인 `ComfyUI/models/` 안내와 다를 수 있으므로 **각 프로젝트의 README나 문서를 반드시 따르세요**. ComfyUI는 매우 확장성이 뛰어나므로 구현 방식은 작성자마다 다릅니다. 설치 및 문제 해결 방법은 [커스텀 노드 설치 방법](https://docs.comfy.org/ko/installation/install_custom_node)을 참조하세요.



## 

​

ComfyUI에서 모델 사용하기

  1. **파일을 올바른 위치에 가져오기** : [Hugging Face](https://huggingface.co), [Civitai](https://civitai.green) 또는 [GitHub](https://github.com)의 프로젝트 페이지와 같은 커뮤니티 사이트에서 다운로드한 후, `ComfyUI/models/` 아래의 해당 유형 하위 폴더(예: `checkpoints`, `loras`, `vae`)에 넣으세요.
  2. **적합한 로더 노드 추가하기** : 해당 모델 유형(체크포인트, LoRA, VAE 등)에 맞는 로더를 선택하세요. 노드 목록에서 제목은 종종 **Load** 로 시작합니다.
  3. **로더 노드에서 파일 선택하기** : 해당 로더 노드의 드롭다운 메뉴에서 파일을 선택하세요.
  4. **로더 노드를 나머지 그래프에 연결하기** : ComfyUI가 열려 있는 동안 직접 파일을 복사했다면 앱을 **재시작** 하거나 필요에 따라 새로 고침하여 목록이 업데이트되도록 하세요.



### 

​

대용량 다운로드를 예상하세요

단일 생성 모델은 종종 **수 기가바이트** 에 달합니다. 다운로드하거나 동기화할 때 디스크 공간과 시간을 충분히 준비하세요.

## 

​

메인 체크포인트 외에도

메인 디퓨전 체크포인트는 많은 일을 하지만, 많은 워크플로에서는 **작은 보조 모델** 을 추가하기도 합니다. 예를 들면:

  * **LoRA** : 스타일, 캐릭터, 또는 컨셉에 맞게 조정된 경량 추가물
  * **ControlNet** : 에지, 깊이, 자세 등에서 추가 가이드 제공
  * **인페인팅** : 기존 이미지 내부의 영역을 채우거나 교체

![보조 모델](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=0f49a29f61c23ccd32ec5a15207b8f9c)

## 

​

모델 제거하기

현재 UI에는 ‘제거’ 버튼이 없습니다. 모델을 삭제하려면, `ComfyUI/models/` 폴더에서 해당 모델이 저장된 파일(또는 여러 파일)을 **삭제** 하세요.

## 

​

추가 모델 경로 추가하기

`ComfyUI/models` 외부에서 모델 파일을 관리하고 싶다면 다음과 같은 이유가 있을 수 있습니다:

  * 여러 개의 ComfyUI 인스턴스를 사용하고 있으며 디스크 공간을 절약하기 위해 모델 파일을 공유하고 싶습니다.
  * 서로 다른 유형의 GUI 프로그램(예: WebUI)을 사용하고 있으며 동일한 모델 파일을 사용하고 싶습니다.
  * 모델 파일이 인식되지 않거나 찾을 수 없습니다.

우리는 `extra_model_paths.yaml` 구성 파일을 통해 추가 모델 검색 경로를 추가할 수 있는 방법을 제공합니다.

### 

​

구성 파일 열기

  * 휴대용/수동 설치

  * Comfy 데스크톱




[휴대용](https://docs.comfy.org/ko/installation/comfyui_portable_windows) 및 [수동](https://docs.comfy.org/ko/installation/manual_install) 버전의 ComfyUI에서는 ComfyUI 루트 디렉터리에 `extra_model_paths.yaml.example`라는 예제 파일을 찾을 수 있습니다:
    
    
    ComfyUI/extra_model_paths.yaml.example
    

이를 복사하여 `extra_model_paths.yaml`로 이름을 변경해 사용하세요. 이 파일은 ComfyUI의 루트 디렉터리인 `ComfyUI/extra_model_paths.yaml`에 유지하십시오. 또한, 구성 예제 파일은 [여기](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example)에서도 확인할 수 있습니다.

[Comfy 데스크톱](https://docs.comfy.org/ko/installation/desktop/windows) 애플리케이션을 사용하는 경우, 데스크톱 앱 상단의 캡슐 메뉴를 클릭하고 **Storage** 탭을 열어 모델 디렉터리를 추가하세요. 캡슐 메뉴는 데스크톱 앱에만 있으며 브라우저에서 실행하는 ComfyUI에는 없습니다![Comfy 데스크톱 캡슐 메뉴: 모델 디렉터리 설정을 표시하는 Storage 탭](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)또는 다음 경로에서 직접 열 수도 있습니다:

  * Windows

  * macOS



    
    
    C:\Users\YourUsername\AppData\Roaming\ComfyUI\extra_models_config.yaml
    
    
    
    ~/Library/Application Support/ComfyUI/extra_models_config.yaml
    

해당 파일을 동일한 디렉터리에 유지해야 하며, 다른 곳으로 이동해서는 안 됩니다.

파일이 존재하지 않는 경우, 아무 텍스트 편집기로 직접 생성할 수 있습니다.

### 

​

예제 구조

다음과 같은 모델 경로를 ComfyUI에 추가하고 싶다고 가정해 보겠습니다:
    
    
    📁 YOUR_PATH/
      ├── 📁models/
      |   ├── 📁 loras/
      |   │   └── xxxxx.safetensors
      |   ├── 📁 checkpoints/
      |   │   └── xxxxx.safetensors
      |   ├── 📁 vae/
      |   │   └── xxxxx.safetensors
      |   └── 📁 controlnet/
      |       └── xxxxx.safetensors
    

그러면 `extra_model_paths.yaml` 파일을 아래와 같이 설정하여 ComfyUI가 기기의 모델 경로를 인식하도록 할 수 있습니다:
    
    
    my_custom_config:
        base_path: YOUR_PATH
        loras: models/loras/
        checkpoints: models/checkpoints/
        vae: models/vae/
        controlnet: models/controlnet/
    

또는
    
    
    my_custom_config:
        base_path: YOUR_PATH/models/
        loras: loras
        checkpoints: checkpoints
        vae: vae
        controlnet: controlnet
    

데스크톱 버전의 경우, 설치 시 생성된 경로 설정을 덮어쓰지 않고 기존 구성 경로에 설정을 추가하십시오. 수정 전에 해당 파일을 백업해 두어 실수했을 때 복구할 수 있도록 하십시오.

또는 기본 제공되는 [extra_model_paths.yaml.example](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example)를 참고해 더 많은 구성 옵션을 확인할 수 있습니다. 저장 후에는 **ComfyUI를 다시 시작** 해야 변경 사항이 적용됩니다. 아래는 원본 구성 예제입니다:
    
    
    #이름을 extra_model_paths.yaml로 변경하면 ComfyUI가 로드합니다
    
    
    #a1111 ui용 구성
    #base_path만 귀하의 설치 경로로 변경하면 됩니다
    a111:
        base_path: path/to/stable-diffusion-webui/
    
        checkpoints: models/Stable-diffusion
        configs: models/Stable-diffusion
        vae: models/VAE
        loras: |
             models/Lora
             models/LyCORIS
        upscale_models: |
                      models/ESRGAN
                      models/RealESRGAN
                      models/SwinIR
        embeddings: embeddings
        hypernetworks: models/hypernetworks
        controlnet: models/ControlNet
    
    #comfyui용 구성
    #귀하의 base_path는 기존 ComfyUI 설치 경로이거나 모든 모델, Lora 등을 저장하는 중앙 폴더여야 합니다.
    
    #comfyui:
    #     base_path: path/to/comfyui/
    #     # is_default를 사용해 해당 폴더를 먼저 나열하고 다운로드 등 기본 디렉터리로 지정할 수 있습니다
    #     #is_default: true
    #     checkpoints: models/checkpoints/
    #     clip: models/clip/
    #     clip_vision: models/clip_vision/
    #     configs: models/configs/
    #     controlnet: models/controlnet/
    #     diffusion_models: |
    #                  models/diffusion_models
    #                  models/unet
    #     embeddings: models/embeddings/
    #     loras: models/loras/
    #     upscale_models: models/upscale_models/
    #     vae: models/vae/
    
    #other_ui:
    #    base_path: path/to/ui
    #    checkpoints: models/checkpoints
    #    gligen: models/gligen
    #    custom_nodes: path/custom_nodes
    
    

예를 들어, 귀하의 WebUI가 `D:\stable-diffusion-webui\`에 위치한다면, 해당 구성은 아래와 같이 수정할 수 있습니다:
    
    
    a111:
        base_path: D:\stable-diffusion-webui\
        checkpoints: models/Stable-diffusion
        configs: models/Stable-diffusion
        vae: models/VAE
        loras: |
             models/Lora
             models/LyCORIS
        upscale_models: |
                      models/ESRGAN
                      models/RealESRGAN
                      models/SwinIR
        embeddings: embeddings
        hypernetworks: models/hypernetworks
        controlnet: models/ControlNet
    

### 

​

추가 커스텀 노드 경로 추가하기

외부 모델을 추가하는 것 외에도, ComfyUI의 기본 경로에 없는 커스텀 노드 경로를 추가할 수도 있습니다.

이렇게 하면 커스텀 노드의 기본 설치 경로는 변경되지 않으며, ComfyUI를 시작할 때 추가 경로 검색이 이루어집니다. 여전히 해당 환경에서 커스텀 노드 종속성을 설치해 실행 환경의 무결성을 보장해야 합니다.

아래는 간단한 구성 예제입니다(맥OS), 실제 상황에 맞게 수정해 해당 구성 파일에 추가하고 저장한 후 ComfyUI를 다시 시작해 변경 사항이 적용되도록 하십시오:
    
    
    my_custom_nodes:
      custom_nodes: /Users/your_username/Documents/extra_custom_nodes
    

## 

​

일반적인 문제

ComfyUI는 GGUF 형식 모델을 지원하나요?

ComfyUI는 기본적으로 GGUF 형식 모델을 지원하지 않습니다. GGUF 모델을 사용하려면 [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)와 같은 커뮤니티 커스텀 노드를 설치해야 합니다.

왜 내 모델을 찾을 수 없나요?

모델을 설치했는데 ComfyUI에서 찾을 수 없다면 다음 단계를 시도해 보세요:

  * 모델이 올바른 위치에 있는지 확인하세요:
    * 기본 경로는 `ComfyUI/models/`입니다 (예: `checkpoints`, `loras`, `vae`)
    * **Comfy 데스크톱** : 데스크톱 앱 상단의 캡슐 메뉴를 클릭하고 **Storage** 탭을 열어 모델 디렉터리를 확인하세요. 캡슐 메뉴는 데스크톱 앱에만 있으며 브라우저에서 실행하는 ComfyUI에는 없습니다.
![Comfy Desktop capsule menu: Storage tab showing model directory settings](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)
  * `r` 키를 눌러 노드 정의를 새로 고쳐 ComfyUI가 모델을 인식하도록 하세요.
  * ComfyUI를 재시작하세요.
  * 로더 노드에서 올바른 모델이 선택되었는지 확인하세요.



## 

​

좀 더 자세한 배경 정보가 필요하신가요?

여기서 '모델'이란 무엇을 의미하나요?

여기서 **모델** 이란 네트워크가 학습한 내용을 담은 데이터 파일을 말합니다. 입력값(텍스트 및 노이즈 등)을 출력값(이미지 등)으로 변환할 수 있을 정도로 충분한 정보를 포함하고 있습니다. 이미지 워크플로에서 흔히 사용되는 예는 **디퓨전** 체크포인트, **CLIP** 과 같은 텍스트/이미지 인코더, 그리고 RealESRGAN과 같은 **업스케일러** 입니다.

베이스 모델과 커뮤니티 변형

연구실과 오픈소스 프로젝트에서 제공하는 큰 **베이스 모델** 은 범용적으로 사용됩니다. 커뮤니티에서는 이를 **파인튜닝** 하거나 새로운 체크포인트와 LoRA로 합쳐 특정 스타일에 더 잘 맞거나, 조금 더 가볍게 작동하거나, 새로운 동작을 추가하기도 합니다. 마치 Civitai나 Hugging Face에서 좋아하는 체크포인트를 고르는 것과 같은 원리입니다.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/basic-concepts/models.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/basic-concepts/models)

[ComfyUI 링크: 노드 연결 작동 방식이전](https://docs.comfy.org/ko/basic-concepts/links)[종속성다음](https://docs.comfy.org/ko/basic-concepts/dependencies)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

리소스

[설치](https://docs.comfy.org/ko/installation/system_requirements)[튜토리얼](https://docs.comfy.org/ko/tutorials/basic/text-to-image)[개발](https://docs.comfy.org/ko/development/overview)

제품

[기능](https://www.comfy.org/?utm_source=docs)[갤러리](https://www.comfy.org/gallery?utm_source=docs)[다운로드](https://www.comfy.org/download?utm_source=docs)

회사 정보

[소개](https://www.comfy.org/about?utm_source=docs)[채용](https://www.comfy.org/careers?utm_source=docs)[이용약관](https://www.comfy.org/terms-of-service?utm_source=docs)[개인정보 처리방침](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
