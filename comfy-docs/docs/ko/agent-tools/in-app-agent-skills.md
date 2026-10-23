---
url: https://docs.comfy.org/ko/agent-tools/in-app-agent-skills/
title: Comfy Agent \uc2a4\ud0ac - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:39.999449+00:00
---

# Comfy Agent 스킬 - ComfyUI

> Source: https://docs.comfy.org/ko/agent-tools/in-app-agent-skills/

## 이 페이지에서

  * 개인 스킬이란 무엇인가요?
  * 채팅에서 스킬 생성하기
  * 스킬 사용하기
  * 스킬 업데이트 또는 삭제하기
  * 기존 스킬 파일 저장하기
  * 공개 스킬 사용하기
  * 내장 가이드와 코딩 에이전트 스킬



Agent Tools / MCP

# Comfy Agent 스킬

페이지 복사페이지 복사

개인 및 공개 스킬을 사용해 Comfy Agent에 작업에 재사용할 수 있는 지침을 제공하세요.

페이지 복사페이지 복사

## 

​

개인 스킬이란 무엇인가요?

개인 스킬은 Comfy Agent를 위한 재사용 가능한 지침 세트입니다. 이름, 언제 사용할지에 대한 한 줄 설명, 그리고 지침 자체로 구성됩니다. 개인 스킬을 사용해 “정사각형 이미지 만들기”, “흰색 배경 사용”, “실행 전에 노드 연결 확인” 같은 지침을 반복할 수 있습니다. 개인 스킬은 계정에 저장됩니다. Agent는 스킬의 설명이 요청과 일치하거나 이름으로 요청할 때 해당 스킬을 불러옵니다.

## 

​

채팅에서 스킬 생성하기

무엇을 저장할지, 무엇이라고 부를지, 언제 사용해야 하는지 Agent에게 알려주세요:

> product-shot이라는 스킬로 저장해 주세요: 제품 이미지를 요청하면 정사각형 1024 × 1024 캔버스, 중립적인 회색 배경, Save Image 노드를 사용하세요. 실행하기 전에 워크플로를 검증하세요.

Agent는 이후 메시지를 위해 스킬을 저장합니다. 새로 만들거나 업데이트한 스킬은 다음 메시지부터 적용됩니다.

## 

​

스킬 사용하기

이름으로 스킬을 요청하세요:

> 내 product-shot 스킬을 사용해 빨간색 스니커즈의 스튜디오 사진 워크플로를 만들어 주세요.

요청이 스킬의 설명과 일치하면 Agent가 자동으로 스킬을 선택할 수도 있습니다.

## 

​

스킬 업데이트 또는 삭제하기

같은 스킬 이름을 사용해 지침을 교체하세요:

> 내 product-shot 스킬을 흰색 배경과 1536 × 1536 캔버스를 사용하도록 업데이트해 주세요.

이름으로 스킬을 삭제하세요:

> 내 product-shot 스킬을 삭제해 주세요.

## 

​

기존 스킬 파일 저장하기

`SKILL.md` 파일의 내용을 채팅에 붙여넣고 Agent에게 개인 스킬로 저장해 달라고 요청하세요. Agent는 파일 상단의 헤더에서 이름과 설명을 읽습니다. 저장된 스킬은 다음 메시지부터 사용할 수 있습니다.

## 

​

공개 스킬 사용하기

공개 스킬은 여러분이 만든 스킬뿐 아니라 누구나 사용할 수 있는 공유 스킬입니다. 이름으로 공개 스킬을 요청하거나 하고 싶은 일을 설명하면, Agent는 여러분의 스킬을 사용할 때와 같은 방식으로 해당 스킬을 사용합니다:

> 중립적인 회색 배경에 빨간색 스니커즈를 위해 product-shot 공개 스킬을 사용해 주세요.

## 

​

내장 가이드와 코딩 에이전트 스킬

Comfy Agent에는 워크플로를 만들고 모델을 선택하기 위한 가이드가 포함되어 있습니다. 개인 및 공개 스킬은 이 가이드 위에 반복되는 작업을 위한 지침을 추가합니다. [코딩 에이전트용 스킬](https://docs.comfy.org/ko/agent-tools/skills)은 Claude Code 같은 도구에 별도로 설치됩니다. 그곳에 설치해도 Comfy Agent에는 추가되지 않습니다. 스킬 지침에 API 키, 비밀번호, 액세스 토큰을 넣지 마세요. 데이터 처리에 대해서는 [데이터 및 개인정보](https://docs.comfy.org/ko/agent-tools/in-app-agent-data-privacy#%EC%8A%A4%ED%82%AC-%EB%B0%8F-%EA%B0%80%EC%9D%B4%EB%93%9C)를 참고하세요.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/agent-tools/in-app-agent-skills.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/agent-tools/in-app-agent-skills)

[Comfy Agent 시작하기이전](https://docs.comfy.org/ko/agent-tools/in-app-agent-installation)[Comfy Agent 데이터 및 개인정보다음](https://docs.comfy.org/ko/agent-tools/in-app-agent-data-privacy)

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
