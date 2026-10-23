---
url: https://docs.comfy.org/ko/get_started/cloud/
title: Comfy Cloud - RTX 6000 Pro\ub85c \uad6c\ub3d9\ub418\ub294 \uacf5\uc2dd ComfyUI \ud074\ub77c\uc6b0\ub4dc \ud50c\ub7ab\ud3fc - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:39.353549+00:00
---

# Comfy Cloud - RTX 6000 Pro로 구동되는 공식 ComfyUI 클라우드 플랫폼 - ComfyUI

> Source: https://docs.comfy.org/ko/get_started/cloud/

## 이 페이지에서

  * Comfy Cloud란?
    * 주요 특징
  * 클라우드 vs 로컬
  * 가격 및 구독
  * Comfy Cloud 방화벽 화이트리스트
  * ComfyUI Cloud 사용 방법
  * 피드백
    * Comfy Cloud 중지/종료 방법
  * 자주 묻는 질문
  * 다음 단계



시작하기

# Comfy Cloud - RTX 6000 Pro로 구동되는 공식 ComfyUI 클라우드 플랫폼

페이지 복사페이지 복사

NVIDIA RTX 6000 Pro GPU를 탑재한 공식 클라우드 플랫폼인 Comfy Cloud를 통해 온라인에서 ComfyUI 워크플로우를 실행해 보세요. 로컬 설치가 필요 없습니다.

페이지 복사페이지 복사

## Comfy Cloud에 접속하기

여기를 클릭하여 ComfyUI Cloud에 바로 접속하세요

## 

​

Comfy Cloud란?

ComfyUI Cloud는 로컬 버전과 동일한 기능을 갖춘 ComfyUI의 클라우드 버전입니다. 모든 것이 사전 설치되어 즉시 사용할 수 있습니다.

### 

​

주요 특징

## 설정 없음

설치가 필요 없습니다. 모든 모델과 커스텀 노드가 사전 설치되어 바로 사용 가능합니다.

## 강력한 GPU

자체 하드웨어 없이 강력한 서버 GPU에서 워크플로를 빠르게 실행할 수 있습니다.

## 항상 최신 상태

최신 ComfyUI 릴리스와 기능으로 자동 업데이트됩니다.

## 어디서나 접속 가능

인터넷 연결만 있으면 어떤 디바이스에서든 ComfyUI를 사용할 수 있습니다. 로컬 설치가 필요 없습니다.

## 팀 협업

팀 워크스페이스를 만들어 팀 멤버와 협업하세요. 구독 플랜, 크레딧, 워크플로를 공유할 수 있습니다.

## 

​

클라우드 vs 로컬

ComfyUI는 공식 클라우드 버전인 [Comfy Cloud](https://comfy.org/cloud)와 오픈소스 자체 호스팅 버전을 모두 제공합니다. 강력한 GPU를 보유하고 있다면 로컬에서 ComfyUI를 실행하는 것이 좋은 선택입니다. 반면 클라우드 버전은 즉시 사용할 수 있는 온라인 서비스로, URL만 열면 설치나 설정이 필요 없습니다.

카테고리| Comfy Cloud| 자체 호스팅 (로컬 ComfyUI)  
---|---|---  
**비용**|  무료 요금제 및 유료 구독 플랜| 무료  
**GPU**|  강력한 Blackwell RTX 6000 Pro| 직접 GPU 준비 필요  
**기술 지식**|  기술 지식이 필요 없습니다.| 데스크톱 및 포터블 버전으로 쉽게 시작할 수 있지만, 커스텀 노드 설치 및 로컬 설치 문제를 직접 해결해야 합니다.  
**커스텀 노드**|  사전 설치된 커스텀 노드를 사용하며 호환성 문제를 걱정할 필요가 없습니다.| 원하는 커스텀 노드를 설치할 수 있지만 직접 관리해야 합니다.  
**모델**|  사전 설치된 모델을 사용합니다. Civitai와 Hugging Face에서 모델을 가져올 수 있습니다.| 원하는 모델을 사용할 수 있지만 먼저 다운로드해야 합니다.  
**주목할 만한 차이점**| [워크스페이스](https://docs.comfy.org/ko/cloud/workspace)로 팀을 손쉽게 온보딩할 수 있음| 오프라인에서도 작동하며 무한히 커스터마이징 가능  
**시작하기**| [ComfyUI Cloud 실행하기](https://comfy.org/cloud)| [로컬 ComfyUI 설치하기](https://docs.comfy.org/ko/installation/system_requirements)  
  
## 

​

가격 및 구독

## 가격 확인하기

Comfy Cloud의 가격 및 구독 옵션 보기

## 

​

Comfy Cloud 방화벽 화이트리스트

TCP 443을 통해 다음 대상으로의 아웃바운드 HTTPS 및 WebSocket 트래픽을 허용하세요:

  * **앱:** `cloud.comfy.org`, `api.comfy.org`, `cdn.comfy.org`
  * **업로드 및 출력:** `comfy-hub-assets.comfy.org`, `storage.googleapis.com`
  * **로그인:** `dreamboothy.firebaseapp.com`, `identitytoolkit.googleapis.com`, `securetoken.googleapis.com`, `apis.google.com`, `challenges.cloudflare.com`
  * **기타 기능:** `registry.comfy.org`, `*.algolia.net`, `media.comfy.org`



## 

​

ComfyUI Cloud 사용 방법

ComfyUI Cloud를 사용하는 방법은 기본적으로 로컬 ComfyUI를 사용하는 것과 같습니다. ComfyUI를 처음 사용하신다면, 다음의 간단한 팁을 참고해보세요:

1

템플릿 선택하기

왼쪽 사이드바의 템플릿 아이콘을 클릭해 사용 가능한 워크플로우를 둘러보세요.![워크플로우 템플릿 열기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a32875bb4e6d1c92ea4f893831aff925)

2

실행할 워크플로우 선택하기

실행하고자 하는 템플릿을 클릭하세요.![워크플로우 템플릿 선택하기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b16043c4ad9372834eb7fe49c1180eee)

3

템플릿 입력값 업데이트하기

  1. 로드된 워크플로우에서, 클라우드 버전에서는 모든 모델이 사전 설치되어 있으므로 로드 후 바로 실행할 준비가 됩니다.
  2. 업데이트가 필요한 경우 이미지 입력이나 텍스트 프롬프트만 제공하면 됩니다. ‘Load Image’ 노드 또는 ‘CLIP Text Encode’ 노드를 확인하세요. ![입력값 확인하기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=56ca79d24c79e666146c927263c96e99)



4

워크플로우 실행하기

모든 것이 정확하다면, ‘Run’ 아이콘을 클릭하거나 단축키 ‘Ctrl + Enter’를 사용해 워크플로우를 실행하세요.![워크플로우 실행하기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=546f1e0003941deba2006a36d8f9ed34)

5

출력물 보기

실행을 클릭한 후, 저희 서비스는 워크플로우를 위한 머신을 할당하기 시작합니다. 대기열 패널에서 해당 워크플로우의 실행 상태를 확인할 수 있습니다.![대기열 보기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=4ac366407cf13fa84e55ef7948cff36e)

6

내부 콘텐츠 저장하기

워크플로우 실행이 완료된 후, 생성된 콘텐츠를 로컬에 저장할 수 있습니다. 자산 유형에 따라 저장 방법은 다음과 같습니다:

  * 이미지 저장하기

  * 비디오 저장하기

  * 오디오 저장하기

  * 3D 자산 저장하기




대기열 패널 또는 이미지 저장 노드에서 생성된 이미지를 마우스 오른쪽 버튼으로 클릭하고 ‘이미지 저장’을 선택해 로컬에 저장하세요.![이미지 자산 저장하기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a15e70a3649537fb8c6adc50689dfbe7)

대기열 패널 또는 비디오 저장 노드에서:

  1. 브라우저 플레이어 구성 요소의 세 개 점을 클릭해 메뉴를 열고
  2. ‘다운로드’를 선택해 비디오를 로컬에 저장하세요. ![비디오 자산 저장하기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=2c987025c1c25e954a3065775ef5223d)



대기열 패널 또는 오디오 저장 노드에서:

  1. 브라우저 플레이어 구성 요소의 세 개 점을 클릭해 메뉴를 열고
  2. ‘다운로드’를 선택해 오디오 파일을 로컬에 저장하세요. ![오디오 자산 저장하기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8d876d9c3b89b2ae9f1e84ba8b3e9887)



3D 브라우저 노드 메뉴에서 ‘Export’ 옵션을 선택하고 원하는 형식을 고르면 3D 파일이 로컬에 저장됩니다.![3D 자산 저장하기](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5e121107826658a3e1725b8d9840d94b)

## 

​

피드백

생각나는 점, 제안사항 또는 문제가 있다면, 그냥 ‘피드백’ 아이콘을 클릭하세요. 그러면 귀하의 의견이 바로 저희에게 전송됩니다. ![피드백](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f1306e3587e441fc9964ffc0f9e4cc73)

### 

​

Comfy Cloud 중지/종료 방법

클라우드 세션은 GPU가 활성 상태에서 실행 중일 때만 요금이 청구됩니다. 브라우저 탭을 닫으면 세션이 자동으로 중지됩니다. 일반 브라우저 탭처럼 언제든지 닫아도 됩니다.

## 

​

자주 묻는 질문

## FAQ 보기

가격, 기능, 제한사항 등 Comfy Cloud에 대한 자주 묻는 질문과 답변 보기

## 

​

다음 단계

## 클라우드 API

클라우드 API를 통해 프로그래밍 방식으로 워크플로우 실행하기

## 튜토리얼

ComfyUI 워크플로우를 배우는 튜토리얼 살펴보기

## 지원

도움을 받으려면 저희 Discord 커뮤니티에 참여하세요

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/get_started/cloud.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/get_started/cloud)

[ComfyUI 업데이트 방법이전](https://docs.comfy.org/ko/installation/update_comfyui)[ComfyUI에서 커스텀 노드 설치 방법다음](https://docs.comfy.org/ko/installation/install_custom_node)

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
