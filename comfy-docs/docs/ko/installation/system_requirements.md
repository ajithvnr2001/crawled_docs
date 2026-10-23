---
url: https://docs.comfy.org/ko/installation/system_requirements/
title: \uc2dc\uc2a4\ud15c \uc694\uad6c\uc0ac\ud56d - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:43.848424+00:00
---

# 시스템 요구사항 - ComfyUI

> Source: https://docs.comfy.org/ko/installation/system_requirements/

## 이 페이지에서

  * 지원되는 운영체제
  * Python 버전
  * 브라우저 요구사항
  * 지원되는 하드웨어
  * 의존성
  * 자주 묻는 질문



로컬 (자체 호스팅)

# 시스템 요구사항

페이지 복사페이지 복사

ComfyUI 설치 및 실행을 위한 하드웨어 및 소프트웨어 요구 사항.

페이지 복사페이지 복사

이 가이드에서는 ComfyUI를 설치하기 위한 시스템 요구사항을 소개합니다. ComfyUI는 수시로 업데이트되기 때문에 이 문서가 최신 상태로 유지되지 않을 수 있습니다. 관련 지침은 [ComfyUI](https://github.com/Comfy-Org/ComfyUI)를 참조해 주세요. 어떤 버전의 ComfyUI를 사용하든, ComfyUI는 별도의 Python 환경에서 실행됩니다.

### 

​

지원되는 운영체제

현재 다음과 같은 운영체제를 지원합니다:

  * Windows
  * Linux
  * macOS (M 시리즈와 같은 Apple Silicon 지원)

각 운영체제 및 설정에 맞는 설치 지침은 아래 링크를 참조하세요.

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

Python 버전

  * **Python 3.13** 은 매우 잘 지원되며 권장됩니다.
  * Python 3.14도 작동하지만 일부 커스텀 노드에서 문제가 발생할 수 있습니다. 자유 스레딩 변형은 작동하지만 일부 의존성이 GIL을 활성화하므로 완전히 지원되지 않습니다.
  * Python 3.12는 3.13에서 일부 커스텀 노드 의존성 문제를 겪을 경우 좋은 대안입니다.



### 

​

브라우저 요구사항

최상의 경험을 위해 **Google Chrome 버전 143 이상** 을 사용하세요. 이전 버전의 Chrome(142 이하)에서는 ComfyUI에서 시각적 오류와 성능 문제가 발생하는 것으로 알려져 있습니다.

### 

​

지원되는 하드웨어

  * **NVIDIA GPU** \- CUDA 13.0과 함께 안정적인 PyTorch 설치: `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130`
  * **AMD GPU (Linux)** \- ROCm 7.2 안정판 또는 최신 테스트 버전(nightly)
  * **AMD GPU (Windows)** \- AMD 멀티 아키텍처 PyTorch 패키지를 통한 ROCm 10.0. RDNA 2, RDNA 3, RDNA 3.5, RDNA 4를 지원하며 별도의 HIP SDK 설치가 필요하지 않습니다
  * **Intel GPU** \- Arc 시리즈, 기본 PyTorch torch.xpu 지원
  * **Apple Silicon** \- M1/M2/M3/M4 시리즈, Metal 가속 지원
  * **Ascend NPU** \- torch_npu 확장을 통해
  * **Cambricon MLU** \- torch_mlu 확장을 통해
  * **Iluvatar Corex** \- PyTorch용 Iluvatar 확장을 통해
  * **CPU** \- `--cpu` 파라미터 사용(느리지만 가능)

자세한 설치 단계는 [ComfyUI Windows 및 Linux 수동 설치 섹션](https://github.com/Comfy-Org/ComfyUI?tab=readme-ov-file#manual-install-windows-linux)을 참조해 주세요.

PyTorch 2.7 이상도 지원되지만, 더 새로운 버전을 사용하는 것을 강력히 권장합니다. Nvidia 20 시리즈 이상 GPU에서는 cu130 이상 버전의 PyTorch가 필요합니다. 일부 기능과 최적화는 최신 버전에서만 작동할 수 있습니다. 일반적으로 PyTorch의 최신 메이저 버전과 최신 CUDA 버전을 사용하는 것이 좋습니다. 단, 출시된 지 2주 미만인 경우는 제외됩니다.현재 Windows 포터블 빌드에는 Python 3.13과 PyTorch CUDA 13.0이 포함되어 있습니다. 만약 시작되지 않는다면 NVIDIA 드라이버를 업데이트해 주세요.

### 

​

의존성

  * PyTorch 설치(하드웨어에 맞는 버전)
  * ComfyUI의 requirements.txt에 있는 모든 의존성 설치: `pip install -r requirements.txt`



## 수동 설치

자세한 설치 단계는 수동 설치 섹션을 참조해 주세요.

## 

​

자주 묻는 질문

ComfyUI가 MLX(Apple의 머신러닝 프레임워크)를 지원하나요?

ComfyUI는 MLX를 직접 사용하지 않습니다. Apple Silicon(M1/M2/M3/M4) Mac에서 ComfyUI는 PyTorch의 **MPS(Metal Performance Shaders)** 백엔드를 사용하여 Apple의 Metal 그래픽스 프레임워크로 GPU 가속을 활용합니다.MLX는 Apple Silicon을 위해 설계된 별도의 머신러닝 배열 프레임워크입니다. ComfyUI의 PyTorch 기반 아키텍처는 MPS를 대신 사용합니다.Mac에서 MPS가 정상 작동하는지 확인하려면:
    
    
    python -c "import torch; print(torch.backends.mps.is_available())"
    

**Docker:** ComfyUI는 공식 Docker 이미지를 제공하지 않습니다. 컨테이너에서 ComfyUI를 실행하려면 [Docker Hub](https://hub.docker.com/search?q=comfyui)의 커뮤니티 유지보수 이미지를 사용할 수 있습니다. 이 이미지들은 **Comfy-Org가 공식적으로 유지보수하지 않으며** , ComfyUI 팀의 지원도 받지 않습니다. 사용에 따른 책임은 사용자에게 있습니다.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/installation/system_requirements.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/installation/system_requirements)

[ComfyUI 공식 문서이전](https://docs.comfy.org/ko)[Comfy Desktop 개요다음](https://docs.comfy.org/ko/installation/desktop/overview)

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
