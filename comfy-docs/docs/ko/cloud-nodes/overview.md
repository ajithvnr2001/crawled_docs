---
url: https://docs.comfy.org/ko/cloud-nodes/overview/
title: Comfy Cloud \ub178\ub4dc - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:42.764240+00:00
---

# Comfy Cloud 노드 - ComfyUI

> Source: https://docs.comfy.org/ko/cloud-nodes/overview/

## 이 페이지에서

  * 정의
  * 시작하기
  * 사용 가능한 노드
  * 요금
  * 제한 사항
  * 관련 문서



Comfy Cloud 노드

# Comfy Cloud 노드

페이지 복사페이지 복사

로컬 ComfyUI 설치 환경에서 Comfy Cloud의 GPU로 선별된 워크플로를 실행하세요. 구독이 필요하지 않습니다

페이지 복사페이지 복사

Comfy Cloud 노드는 작업을 로컬 머신 대신 Comfy 자체 GPU에서 실행하도록 전송하는 일반적인 ComfyUI 노드입니다. 다른 노드와 마찬가지로 그래프에 추가하면 됩니다. 구독은 필요하지 않습니다. 다른 파트너 노드와 마찬가지로 계정과 크레딧만 있으면 됩니다.

Comfy Cloud 노드는 클라우드에서 오픈소스 모델을 실행합니다. 파트너 노드와 혼동하지 마세요.

## 

​

정의

각 Comfy Cloud 노드는 하나의 고정된 워크플로를 고정된 모델 버전으로 실행하므로, 저장된 그래프는 시간이 지나도 동일한 결과를 계속 생성합니다. 그래프, 프롬프트, 입력 값은 노드가 작업 실행을 위해 전송하는 내용을 제외하면 모두 사용자 컴퓨터에 남아 있습니다.

## 

​

시작하기

Comfy Cloud 노드는 ComfyUI **v0.34.5 이상** 에 포함되어 있습니다. ComfyUI 코어의 일부이므로 별도로 설치할 것이 없습니다.

1

ComfyUI 업데이트

v0.34.5 이상으로 업데이트하세요. 포터블, 데스크톱, 수동 설치 경로는 [ComfyUI 업데이트 방법](https://docs.comfy.org/ko/installation/update_comfyui) 문서를 참조하세요.

2

ComfyUI 재시작

노드는 시작 시에만 등록되므로 재시작할 때까지 나타나지 않습니다.

3

노드 찾기

노드 라이브러리에서 **Comfy Cloud** 를 검색한 다음, 다른 노드와 마찬가지로 그래프에 추가하세요. 모든 노드의 표시 이름에는 `[BETA]` 접미사가 붙어 있습니다.

## 

​

사용 가능한 노드

출시 시점에는 이미지, 비디오, 오디오 분야에 걸쳐 8개의 노드가 제공됩니다:

노드| 유형  
---|---  
Comfy Cloud Flux 2 Text to Image| 이미지  
Comfy Cloud Mage Flow Text to Image| 이미지  
Comfy Cloud Mage Flow Turbo Text to Image| 이미지  
Comfy Cloud Z-Image Turbo Text to Image| 이미지  
Comfy Cloud MiniMax H3 Text to Video| 비디오  
Comfy Cloud MiniMax H3 Image to Video| 비디오  
Comfy Cloud MiniMax H3 First-Last Frame to Video| 비디오  
Comfy Cloud MiniMax Music 3 Text to Audio| 오디오  
  
## 

​

요금

Comfy Cloud 노드는 GPU-초당 크레딧으로 과금되며, 요금은 실행 전에 노드에 표시됩니다. 구독도 월간 최소 요금도 없습니다.

## 

​

제한 사항

  * 아직 자체 LoRA나 checkpoint를 가져와 사용할 수 없습니다. 각 노드는 호스팅된 고정된 가중치 집합을 제공합니다. 직접 업로드는 다음 단계로 계획되어 있으며 이번 릴리스에서는 사용할 수 없습니다.



## 

​

관련 문서

  * [Comfy Cloud 요금](https://comfy.org/pricing)
  * [파트너 노드 개요](https://docs.comfy.org/ko/tutorials/partner-nodes/overview) (별도의 서드파티 API 노드 카탈로그)



이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/cloud-nodes/overview.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/cloud-nodes/overview)

[VOID: ComfyUI에서의 비디오 인페인팅이전](https://docs.comfy.org/ko/tutorials/utility/void-video-inpainting)[파트너 노드다음](https://docs.comfy.org/ko/tutorials/partner-nodes/overview)

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
