---
url: https://docs.comfy.org/ko/agent-tools/in-app-agent-installation/
title: Comfy Agent \uc2dc\uc791\ud558\uae30 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:40.428324+00:00
---

# Comfy Agent 시작하기 - ComfyUI

> Source: https://docs.comfy.org/ko/agent-tools/in-app-agent-installation/

## 이 페이지에서

  * 설정 선택
  * 첫 이미지 만들기
    * 에이전트 열기
    * 워크플로 만들기
    * 이미지 생성하기
    * 변경 적용하기
  * 문제 해결
    * Agent 버튼이 누락됨
    * Agent가 예상한 워크플로를 편집할 수 없음
    * Agent가 입력을 요청함
    * 클라우드에서 로컬 대화를 찾을 수 없음
  * 다음 단계



Agent Tools / MCP

# Comfy Agent 시작하기

페이지 복사페이지 복사

Comfy Cloud 또는 Comfy Desktop에서 Comfy Agent를 여세요.

페이지 복사페이지 복사

## 

​

설정 선택

Comfy 계정이 필요합니다.

  * **Comfy Cloud:** Comfy Agent가 정식 제공됩니다. [클라우드에 로그인](https://cloud.comfy.org)하세요. 로컬 설치가 필요하지 않으며 웨이팅 리스트도 필요하지 않습니다.
  * **Comfy Desktop:** 로컬 ComfyUI용 Comfy Agent가 곧 출시 예정입니다. 알림을 받으려면 [웨이팅 리스트에 참여하기](https://links.comfy.org/agentalpha)하세요.



## 

​

첫 이미지 만들기

### 

​

에이전트 열기

빈 워크플로를 연 다음, 탭 표시줄 오른쪽 끝 아바타 옆에서 **Agent** 를 선택합니다. 동의 안내가 표시되면 내용을 확인하고 동의합니다. 에이전트 패널에서 **워크플로 선택** 을 사용해 빈 워크플로를 선택합니다.

### 

​

워크플로 만들기

다음 메시지를 보내세요.

> 중립적인 회색 배경에 빨간색 스니커즈를 위한 텍스트 기반 이미지 생성 워크플로를 만들어 주세요. 사용 가능한 모델을 사용하고 이미지 저장 노드를 포함해 주세요. 워크플로에 오류가 있는지 확인하되, 아직 실행하지는 마세요.

에이전트가 캔버스에 워크플로를 만들고 프롬프트와 모델 설정을 채운 뒤, 노드 연결과 필수 입력을 확인합니다. **이미지 저장** 노드로 끝나는 연결된 워크플로가 표시되어야 합니다. 에이전트가 누락된 모델이나 파일을 보고하면, 해당 항목을 제공하거나 현재 설치 환경에서 사용할 수 있는 대안을 요청하세요. 계속하기 전에 워크플로를 다시 확인해 달라고 요청하세요.

### 

​

이미지 생성하기

메시지 상자 옆의 **실행 권한** 을 열고 **묻기** 를 선택한 다음, 설정을 변경했다면 **변경 사항 저장** 을 선택합니다. “이 워크플로를 실행해 주세요.”라고 보냅니다. 에이전트가 승인을 요청하면 **실행** 을 선택합니다. 해당 실행을 시작하지 않으려면 대신 **취소** 를 선택합니다. 생성이 끝나면 에이전트가 대화에서 출력을 반환합니다. 이미지는 **이미지 저장** 노드에도 표시됩니다. 그곳에서 이미지를 마우스 오른쪽 버튼으로 클릭하면 컴퓨터에 저장할 수 있습니다.

### 

​

변경 적용하기

“배경을 흰색으로 바꾸고 모델과 기타 설정은 그대로 유지해 주세요.”라고 보냅니다. 에이전트가 기존 워크플로를 업데이트합니다. 결과를 비교하려면 다시 실행해 달라고 요청하세요.

## 

​

문제 해결

### 

​

Agent 버튼이 누락됨

Comfy 계정에 로그인하세요. Comfy Desktop에서는 [애플리케이션을 업데이트](https://docs.comfy.org/ko/installation/update_comfyui)하고 재시작하세요. 그래도 버튼이 누락되어 있다면 [지원팀](https://docs.comfy.org/ko/support/contact-support)을 통해 계정의 Agent 접근 권한을 확인하세요.

### 

​

Agent가 예상한 워크플로를 편집할 수 없음

Agent 패널에서 원하는 워크플로를 선택한 다음 메시지를 다시 보내세요. [편집할 워크플로 선택](https://docs.comfy.org/ko/agent-tools/in-app-agent#%ED%8E%B8%EC%A7%91%ED%95%A0-%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C-%EC%84%A0%ED%83%9D)을 참조하세요.

### 

​

Agent가 입력을 요청함

**파일 첨부** 를 선택하거나 요청된 파일을 메시지 상자로 끌어다 놓은 다음, Agent에게 계속하도록 요청하세요.

### 

​

클라우드에서 로컬 대화를 찾을 수 없음

로컬 기록과 클라우드 기록은 별도로 관리됩니다. [데이터 및 개인정보 보호](https://docs.comfy.org/ko/agent-tools/in-app-agent-data-privacy#%EC%B1%84%ED%8C%85-%EA%B8%B0%EB%A1%9D-%EB%B0%8F-%EB%8F%99%EA%B8%B0%ED%99%94)를 참조하세요.

## 

​

다음 단계

## 기존 워크플로 편집

프롬프트, 모델 또는 처리 단계를 변경합니다.

## 재사용 가능한 스킬 저장

향후 요청에 사용할 지침을 기억해 둡니다.

메시지, 파일, 대화가 어디에 저장되는지 알아보려면 [데이터 및 개인정보 보호](https://docs.comfy.org/ko/agent-tools/in-app-agent-data-privacy)를 참조하세요.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/agent-tools/in-app-agent-installation.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/agent-tools/in-app-agent-installation)

[Comfy Agent이전](https://docs.comfy.org/ko/agent-tools/in-app-agent)[Comfy Agent 스킬다음](https://docs.comfy.org/ko/agent-tools/in-app-agent-skills)

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
