---
url: https://docs.comfy.org/ko/agent-tools/in-app-agent-data-privacy/
title: Comfy Agent \ub370\uc774\ud130 \ubc0f \uac1c\uc778\uc815\ubcf4 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:40.772208+00:00
---

# Comfy Agent 데이터 및 개인정보 - ComfyUI

> Source: https://docs.comfy.org/ko/agent-tools/in-app-agent-data-privacy/

## 이 페이지에서

  * 간단히 요약
  * Agent가 사용하는 정보
  * 클라우드 및 로컬 데이터 흐름
  * 채팅 기록 및 동기화
  * 스킬 및 가이드
  * 보존 및 삭제



Agent Tools / MCP

# Comfy Agent 데이터 및 개인정보

페이지 복사페이지 복사

Comfy Agent가 요청에 응답하기 위해 사용하는 정보와 로컬 및 Cloud 사용의 차이를 이해합니다.

페이지 복사페이지 복사

## 

​

간단히 요약

Comfy Agent는 메시지, 선택한 워크플로, 선택한 노드, 첨부 파일을 사용합니다. 로컬 ComfyUI 설치 환경에서 작업할 때 채팅 기록은 해당 컴퓨터에 저장됩니다. 메시지와 응답에 필요한 정보는 Comfy의 온라인 서비스를 통해 전송됩니다.

## 

​

Agent가 사용하는 정보

데이터| 활용 방식  
---|---  
메시지| Agent가 수행하려는 작업을 알려줍니다.  
선택한 워크플로 및 노드| 설명하거나 변경하려는 워크플로와 노드를 표시합니다.  
이미지 첨부 파일| Agent가 이미지를 검사하고 워크플로에서 사용할 수 있게 합니다.  
비디오 또는 오디오 첨부 파일| Agent가 미디어 속성을 읽고 콘텐츠를 추출하거나 변환할 수 있게 합니다.  
워크플로 및 실행 오류| Agent가 실패한 워크플로를 설명하고 수정하도록 돕습니다.  
개인 스킬| 재사용 가능한 지침을 제공합니다.  
  
[개인정보 보호정책](https://www.comfy.org/privacy-policy?utm_source=docs)과 [이용약관](https://www.comfy.org/terms-of-service?utm_source=docs)이 Comfy 사용에 적용됩니다.

## 

​

클라우드 및 로컬 데이터 흐름

Comfy Agent 사용 위치| 발생하는 일  
---|---  
**Comfy Cloud**|  Comfy Cloud는 대화, 워크플로, 에셋을 저장합니다. 메시지는 Comfy의 온라인 서비스에서 처리되며, 워크플로는 클라우드 GPU에서 실행됩니다.  
**Desktop의 로컬 ComfyUI**|  로컬 설치는 채팅 기록, 워크플로, 파일을 저장합니다. 메시지와 관련 워크플로 정보는 Comfy의 온라인 서비스에서 처리됩니다. 로컬 워크플로 노드는 사용자의 하드웨어에서 실행되고, 파트너 노드는 해당 온라인 제공업체를 사용합니다.  
  
## 

​

채팅 기록 및 동기화

Cloud Agent와의 대화는 Comfy Cloud에 저장됩니다. 로컬 Agent와의 대화는 ComfyUI를 실행하는 컴퓨터에 저장됩니다. 두 기록은 동기화되지 않습니다. 이는 어떤 애플리케이션 창에서 여는지가 아니라 Cloud를 사용하는지 로컬 설치를 사용하는지에 따라 달라집니다.

## 

​

스킬 및 가이드

개인 스킬에는 Agent를 위해 사용자가 만든 지침이 포함됩니다. 이는 계정에 저장되며, 요청이 해당 스킬과 일치하거나 스킬 이름을 지정할 때 사용됩니다. 내장 Agent 가이드와 외부 코딩 에이전트용 스킬은 개인 Agent 스킬과 별개입니다.

## 

​

보존 및 삭제

보존에 대한 세부 정보는 [개인정보 보호정책](https://www.comfy.org/privacy-policy?utm_source=docs)과 [데이터 보존](https://docs.comfy.org/ko/support/data-retention)을 참조하세요. 계정 또는 데이터 삭제 요청은 [support@comfy.org](mailto:support@comfy.org)로 문의하세요.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/agent-tools/in-app-agent-data-privacy.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/agent-tools/in-app-agent-data-privacy)

[Comfy Agent 스킬이전](https://docs.comfy.org/ko/agent-tools/in-app-agent-skills)[코딩 에이전트용 Comfy Skills다음](https://docs.comfy.org/ko/agent-tools/skills)

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
