---
url: https://docs.comfy.org/ko/get_started/first_generation/
title: AI \uc774\ubbf8\uc9c0 \uc0dd\uc131 \uc2dc\uc791\ud558\uae30 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:38.491424+00:00
---

# AI 이미지 생성 시작하기 - ComfyUI

> Source: https://docs.comfy.org/ko/get_started/first_generation/

## 이 페이지에서

  * 텍스트 기반 이미지 생성이란?
  * ComfyUI 텍스트 기반 이미지 생성 워크플로드 튜토리얼
    * 1\. ComfyUI 실행하기
    * 2\. 기본 텍스트 기반 이미지 생성 워크플로드 로딩하기
    * 3\. 모델 설치
    * 4\. 모델 로드하고 첫 번째 이미지 생성하기
  * 문제 해결
    * 모델 로딩 문제



시작하기

# AI 이미지 생성 시작하기

페이지 복사페이지 복사

ComfyUI로 첫 AI 이미지를 생성해 보세요. 예제 워크플로우 로딩, 모델 설치, 첫 텍스트-이미지 생성을 배워보세요.

페이지 복사페이지 복사

이 가이드는 자신의 기기에서 ComfyUI를 실행하는 **로컬 사용자** 를 대상으로 합니다. 로컬에 아무것도 설치하지 않으려면 공식 클라우드 서비스를 이용해 보세요.

## Comfy Cloud 사용해보기

설정 없이 온라인에서 ComfyUI를 실행하세요. 구글 계정으로 로그인하면 **매달 400 크레딧 무료 제공** 됩니다.

이 가이드는 ComfyUI의 기본 작동 방식을 이해하고 첫 번째 이미지를 완성하는 데 도움을 드립니다. 다음 내용을 다룹니다:

  1. 예제 워크플로드 로딩 
     * ComfyUI 워크플로드 템플릿에서 로딩하기
     * 워크플로드 메타데이터가 포함된 이미지에서 로딩하기
  2. 모델 설치 안내 
     * 자동 모델 설치
     * 수동 모델 설치
  3. 첫 번째 텍스트 기반 이미지 생성 완료



## 

​

텍스트 기반 이미지 생성이란?

텍스트 기반 이미지 생성은 텍스트 설명을 바탕으로 이미지를 생성하는 기본적인 AI 드로잉 기능입니다. AI 아트 생성에서 가장 많이 사용되는 기능 중 하나입니다. 이 과정을 생각해보면, 당신의 요구사항(긍정적 및 부정적 프롬프트)을 아티스트(드로잉 모델)에게 전달하고, 아티스트는 당신이 원하는 것을 만들어냅니다. 텍스트 기반 이미지 생성에 대한 자세한 설명은 [텍스트 기반 이미지 생성](https://docs.comfy.org/ko/tutorials/basic/text-to-image) 챕터에서 다룹니다.

## 

​

ComfyUI 텍스트 기반 이미지 생성 워크플로드 튜토리얼

### 

​

1\. ComfyUI 실행하기

[설치 가이드](https://docs.comfy.org/ko/installation/system_requirements)를 따라 ComfyUI를 시작하고 성공적으로 ComfyUI 인터페이스에 진입했는지 확인하세요. 또는 [Comfy Cloud](https://docs.comfy.org/ko/get_started/cloud)를 이용하면 설치 없이 ComfyUI를 바로 사용할 수 있습니다. ![ComfyUI 인터페이스](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/desktop/comfyui-interface.jpg?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=5fc5c0932897a4ab0076db79fec7b4ea) ComfyUI를 설치하지 않았다면, 기기에 맞는 버전을 선택해 설치해주세요.

Comfy 데스크톱

Comfy Desktop은 **Windows** , **macOS(Apple Silicon)** , **Linux**(AppImage 및 `.deb`)에서 독립형 설치를 지원합니다.

  * 소스는 [GitHub](https://github.com/Comfy-Org/Comfy-Desktop)에 있습니다



Desktop 설치는 기본적으로 ComfyUI **안정 릴리스** 를 따릅니다. 항상 최신 커밋을 쓰려면 휴대용 버전이나 수동 git 설치를 사용하거나, 인스턴스 업데이트 채널을 **Latest on GitHub** 로 바꾸세요.

아래에서 시스템과 하드웨어에 맞는 설치를 선택할 수 있습니다

  * Windows

  * macOS (애플 실리콘)

  * Linux




## Comfy Desktop (Windows) 설치 가이드

**Windows** 10 이상에 적합합니다. NVIDIA 또는 AMD GPU를 권장합니다.

## Comfy Desktop (macOS) 설치 가이드

**애플 실리콘** 을 탑재한 macOS에 적합합니다.

## Comfy Desktop (Linux) 설치 가이드

AppImage 또는 `.deb`를 설치하거나 소스에서 빌드해 실행하세요.

ComfyUI 휴대용 (Windows)

휴대용 버전은 독립적인 임베디드 파이썬 환경을 통합한 ComfyUI 버전으로, 휴대용 버전을 사용하면 최신 기능을 경험할 수 있습니다. 현재 **Windows** 시스템만 지원합니다.

## ComfyUI 휴대용 (Windows) 설치 가이드

**Windows** ComfyUI 버전이 **Nvidia GPU** 또는 **CPU 전용** 으로 실행되며, 항상 최신 커밋을 사용하고 완벽히 휴대 가능합니다.

수동 설치

## ComfyUI 수동 설치 가이드

모든 시스템 유형 및 GPU 유형(Nvidia, AMD, Intel, 애플 실리콘, Ascend NPU, Cambricon MLU)을 지원합니다.

### 

​

2\. 기본 텍스트 기반 이미지 생성 워크플로드 로딩하기

ComfyUI는 보통 실행 시 기본 텍스트 기반 이미지 생성 워크플로드를 자동으로 로드합니다. 하지만 다양한 방법으로 워크플로드를 로드해 ComfyUI의 기본 작동 방식을 익힐 수 있습니다:

  * 메타데이터가 포함된 이미지에서 로딩하기

  * workflow.json에서 로딩하기




ComfyUI가 생성한 모든 이미지는 워크플로드 정보를 포함한 메타데이터를 가지고 있습니다. 다음과 같은 방법으로 워크플로드를 로드할 수 있습니다:

  * ComfyUI가 생성한 이미지를 인터페이스로 드래그 앤 드롭하기
  * 메뉴 **워크플로드** -> **열기** 를 사용해 이미지를 열기

이 예제 이미지를 사용해 워크플로드를 로드해보세요: ![ComfyUI-텍스트 기반 이미지 생성 워크플로드](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/text-to-image-workflow.png)

ComfyUI 워크플로드는 JSON 형식으로 저장될 수 있습니다. 메뉴 **워크플로드** -> **내보내기** 를 사용해 워크플로드를 내보낼 수 있습니다.이 예제 워크플로드를 다운로드해 로드해보세요:[text-to-image.json 다운로드](https://github.com/Comfy-Org/docs/blob/main/public/text-to-image.json)다운로드 후 메뉴 **워크플로드** -> **열기** 를 사용해 JSON 파일을 로드하세요.

### 

​

3\. 모델 설치

대부분의 ComfyUI 설치에는 기본 모델이 포함되어 있지 않습니다. 워크플로드를 로드한 후 [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) 모델이 설치되지 않았다면, 다음과 같은 알림이 나타납니다: 먼저 ComfyUI는 일부 모델이 누락되었음을 경고합니다: ![모델 누락 경고](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/missing_model_warning_1.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=0587d7f045f981756c232644569b3b59) 경고를 클릭해 어떤 모델이 누락되었는지와 다운로드 링크를 확인하세요: ![모델 누락 세부정보](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/missing_model_warning_2.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=bf61da1c5711d935b7d49dd7e236f275) 기본적으로 모델은 `<ComfyUI 설치 위치>/ComfyUI/models/` 아래에 저장되며, `checkpoints`, `embeddings`, `vae`, `lora`, `upscale_model` 등 하위 폴더로 구분됩니다. ComfyUI는 시작할 때 이러한 폴더들과 `extra_model_paths.yaml`에 설정된 경로에서 모델을 감지합니다.

  * Comfy 데스크톱 (모델 폴더 찾기)

  * ComfyUI 포터블 (모델 폴더 찾기)




데스크톱 앱 상단의 캡슐 메뉴를 클릭하고 **Storage** 탭을 열어 모델 디렉터리를 확인하세요. 캡슐 메뉴는 데스크톱 앱에만 있으며 브라우저에서 실행하는 ComfyUI에는 없습니다. 디렉터리 옆의 폴더 아이콘을 클릭하면 파일 관리자에서 열 수 있습니다.![Comfy 데스크톱 캡슐 메뉴: 모델 디렉터리 설정을 표시하는 Storage 탭](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)

포터블 버전의 경우 모델 폴더는 보통 다음 위치에 있습니다:`ComfyUI_windows_portable/ComfyUI/models/`

다음과 같은 방법으로 모델을 설치할 수 있습니다:

  * 자동 다운로드

  * 수동 설치




**다운로드** 버튼을 클릭하면 ComfyUI가 다운로드를 실행하며, 사용 중인 버전에 따라 다른 동작을 수행합니다.

  * Comfy 데스크톱

  * ComfyUI 포터블




데스크톱 버전은 모델 다운로드를 자동으로 완료하고 `<ComfyUI 설치 위치>/ComfyUI/models/checkpoints` 디렉토리에 저장합니다. 설치가 완료될 때까지 기다리거나 사이드바의 모델 패널에서 설치 진행 상황을 확인할 수 있습니다.![모델 다운로드 진행 상태](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/desktop_download_status.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=a1573451803b46539fca14c1b1ef4dd2)

자동 다운로드는 일반적으로 **Hugging Face** 에서 모델을 가져옵니다. 네트워크가 Hugging Face에 안정적으로 연결될 수 있는지 확인하세요.만약 다운로드가 **시작되지 않거나 오랜 시간 동안 진행되지 않는다면** , 누락된 모델 세부정보에서 모델 링크를 복사하거나 아래의 수동 설치 섹션을 참고해 직접 설치하세요.

브라우저가 파일 다운로드를 실행합니다. 다운로드가 완료된 후 `<ComfyUI 설치 위치>/ComfyUI_windows_portable/ComfyUI/models/checkpoints` 디렉토리에 파일을 저장하세요.

[v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) 페이지를 방문해 다음 안내를 따르세요:![Hugging Face 모델 다운로드](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=15c2560c44e7e4276b6a351809f7bf9f)다운로드한 파일을 다음 위치에 저장하세요:

  * Comfy 데스크톱

  * ComfyUI 포터블




`<ComfyUI 설치 위치>/ComfyUI/models/checkpoints`에 저장하세요![Comfy 데스크톱 모델 저장 위치](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=275add7233b1f048455cff0f162847b9)

`ComfyUI_windows_portable/ComfyUI/models/checkpoints`에 저장하세요![ComfyUI 포터블 모델 저장 위치](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=48976b87bcfdba962b119d901c43b286)

저장 후 ComfyUI를 새로 고침하거나 재시작하세요.

### 

​

4\. 모델 로드하고 첫 번째 이미지 생성하기

모델을 설치하거나 업데이트한 후, 키보드에서 **`R`**을 눌러 객체 정의를 새로 고치고 노드의 모델 목록을 업데이트하세요(예: **Load Checkpoint** 의 드롭다운). 이후 아래 단계를 따라 진행하세요: ![워크플로드 실행](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/run_workflow.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=d8cb64b219e93cfd903723255d5e7d11)

  1. **Load Checkpoint** 노드에서 **v1-5-pruned-emaonly-fp16.safetensors** 가 선택되었는지 확인하세요
  2. **실행** 을 클릭하거나 **Ctrl + Enter** 를 눌러 생성하세요

결과는 **Save Image** 노드에 나타납니다. 마우스 오른쪽 버튼을 클릭해 로컬에 저장하세요. ![ComfyUI 첫 번째 이미지 생성 결과](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/result.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=dd253cd626d72716f52322245c5526cc) 자세한 텍스트 기반 이미지 생성 지침은 종합 가이드를 참조하세요:

## ComfyUI 텍스트 기반 이미지 생성 워크플로드 가이드

자세한 텍스트 기반 이미지 생성 워크플로드 지침은 여기를 클릭하세요

## 

​

문제 해결

### 

​

모델 로딩 문제

**Load Checkpoint** 노드에 모델이 표시되지 않거나 “null”이라고 나오는 경우, 모델 설치 위치를 확인하고 ComfyUI를 새로 고치거나 재시작해보세요.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/get_started/first_generation.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/get_started/first_generation)

[ComfyUI Manager 문제 해결이전](https://docs.comfy.org/ko/manager/troubleshooting)[ComfyUI 에이전트 도구: MCP, CLI, 내장 에이전트다음](https://docs.comfy.org/ko/agent-tools)

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
