---
url: https://docs.comfy.org/ko/agent-tools/cli/
title: Comfy CLI: \ud130\ubbf8\ub110\uc5d0\uc11c ComfyUI \uc2e4\ud589 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:39.154628+00:00
---

# Comfy CLI: 터미널에서 ComfyUI 실행 - ComfyUI

> Source: https://docs.comfy.org/ko/agent-tools/cli/

## 이 페이지에서

  * MCP와의 연동
  * CLI 기능
  * 설치 및 설정
  * comfy generate 사전 요구 사항
  * 첫 번째 생성
  * 사용 가능한 모델
  * 사용 예시
    * 텍스트 기반 이미지 생성
    * 이미지 편집 (참조 이미지)
    * 텍스트 기반 비디오 생성
    * JSON 스크립팅
  * comfy generate 그 외
  * 에이전트 스킬
  * 관련 자료
  * 피드백



Agent Tools / MCP

# Comfy CLI: 터미널에서 ComfyUI 실행

페이지 복사페이지 복사

터미널에서 Comfy를 구동하세요: 로컬 ComfyUI, 파트너 생성 호출, Comfy Cloud의 전체 워크플로. 스크립트, CI, 자동화에서 MCP를 보완합니다.

페이지 복사페이지 복사

[comfy-cli](https://github.com/Comfy-Org/comfy-cli)는 Comfy의 명령줄 도구입니다. [MCP 서버](https://docs.comfy.org/ko/agent-tools)와 함께 에이전트와 개발자에게 UI 외부에서 Comfy를 조작하는 또 다른 방법을 제공합니다. **터미널 또는 스크립트 접근** 이 필요할 때 사용하세요: 배치 작업, CI 파이프라인, 워크플로 자동화, 번들 CLI 스킬을 통한 코딩 에이전트와의 페어링에 적합합니다.

**에이전트를 위한 빠른 참고 자료.** 이 페이지는 MCP와 함께 사용할 수 있도록 방향을 잡고 일반적인 `comfy generate` 호출을 실행하는 데 충분한 짧은 개요입니다. **전체 CLI 문서**(로컬 설치, `comfy setup`, `comfy run`, 템플릿, 워크플로 편집, 노드/모델 검색 등)는 [Comfy CLI 시작하기](https://docs.comfy.org/ko/comfy-cli/getting-started)를 참조하세요.

**`comfy generate`는 베타 버전입니다.** 플래그명, 모델 별칭 및 출력 형식은 변경될 수 있습니다. 기본 파트너 엔드포인트는 안정적입니다. 피드백은 [comfy-cli GitHub 저장소](https://github.com/Comfy-Org/comfy-cli/issues)에 제출해 주세요.

## 

​

MCP와의 연동

| Comfy MCP(클라우드)| Comfy CLI  
---|---|---  
**인터페이스**|  MCP 클라이언트(Claude Code, Claude Desktop 등)와 채팅| 터미널 명령 및 스크립트  
**최적 사용**|  채팅 내 대화형 에이전트 워크플로| 자동화, 배치 실행, CI, 셸 파이프라인  
**인증**|  MCP 클라이언트의 OAuth 또는 API 키(헤드리스)| `comfy cloud login`(OAuth) 또는 API 키(CI)  
**출력**|  채팅 세션에 반환| 디스크에 저장(`--download`) 또는 JSON(`--json`)  
  
MCP 설정, 설치, 도구 목록 및 인증 방법은 [Comfy MCP](https://docs.comfy.org/ko/agent-tools/mcp)를 참조하세요.

## 

​

CLI 기능

  1. **로컬 ComfyUI** — 설치, 실행, 업데이트, 커스텀 노드 관리
  2. **파트너 생성** — `comfy generate`로 일회성 이미지/비디오/오디오/3D 파트너 API 호출
  3. **클라우드 워크플로** — `comfy run`, 템플릿, 슬롯 편집, Comfy Cloud에서 작업 모니터링



**두 가지 표면, 하나의 CLI.** 모든 명령이 자동으로 실행 위치를 감지합니다. Comfy Cloud에 로그인한 경우 명령은 **클라우드** 로 라우팅되고, 그렇지 않으면 **로컬** 서버에서 실행됩니다. 각 호출 시 `--where local|cloud`로 재정의하거나, `COMFY_WHERE` 환경 변수를 사용하거나, `comfy set-default --where cloud`로 영구 설정할 수 있습니다.

## 

​

설치 및 설정

pip

homebrew
    
    
    pip install comfy-cli
    
    
    
    brew tap Comfy-Org/comfy-cli
    brew install comfy-org/comfy-cli/comfy-cli
    

셸 자동완성 힌트를 얻으려면:
    
    
    comfy --install-completion
    
    
    
    comfy setup
    

CI 또는 스크립트에서 비대화형 설치를 원하면 `-y`를 전달하세요. 전체 `comfy setup` 플래그 표는 [Comfy CLI 시작하기](https://docs.comfy.org/ko/comfy-cli/getting-started#%EB%B9%A0%EB%A5%B8-%EC%84%A4%EC%A0%95-%EA%B6%8C%EC%9E%A5)를 참조하세요. Comfy Cloud에 로그인:
    
    
    comfy cloud login
    comfy cloud whoami
    

## 

​

`comfy generate` 사전 요구 사항

  * `comfy cloud login`(브라우저 OAuth)를 통한 활성 Comfy Cloud 세션, **또는** 헤드리스 또는 CI 사용을 위한 [Comfy API 키](https://docs.comfy.org/ko/development/api-development/getting-an-api-key)(`--api-key` / `COMFY_API_KEY`)
  * 계정의 [크레딧](https://docs.comfy.org/ko/interface/credits)
  * _선택 사항:_ [파트너 노드 및 호출당 가격 찾아보기](https://docs.comfy.org/ko/tutorials/partner-nodes/pricing)



## 

​

첫 번째 생성
    
    
    comfy generate flux-pro \
        --prompt "a cat on the moon, cinematic lighting" \
        --width 1024 --height 1024 \
        --download cat.png
    

CLI는 로컬 파일을 업로드하고, 작업을 제출하며, 완료를 폴링한 후 결과를 저장합니다.

## 

​

사용 가능한 모델

`comfy generate`는 이미지 및 비디오 파트너 모델을 지원합니다. CLI 버전에서 사용 가능한 항목을 확인하세요:
    
    
    comfy generate list                            # 모든 모델
    comfy generate list --category text-to-video   # 카테고리별 필터
    comfy generate list --partner kling            # 파트너별 필터
    comfy generate schema flux-kontext             # 한 모델의 매개변수
    

일반 별칭은 다음과 같습니다:

카테고리| 예시  
---|---  
**이미지**| `flux-pro`, `flux-ultra`, `flux-kontext`, `nano-banana`, `grok`, `grok-edit`, `ideogram-edit`, `dalle`, `recraft`, `stability`  
**비디오**| `seedance`, `kling`, `luma`, `runway`, `pika`, `vidu`, `hailuo`, `moonvalley`, `grok-video`  
  
환경에서 전체 목록을 보려면 `comfy generate list`를 실행하세요.

## 

​

사용 예시

### 

​

텍스트 기반 이미지 생성
    
    
    comfy generate nano-banana \
        --prompt "a watercolor of a sleeping fox" \
        --download fox.png
    

### 

​

이미지 편집 (참조 이미지)

로컬 파일 경로를 전달합니다. CLI는 Comfy의 스토리지 엔드포인트를 통해 업로드하거나 필요에 따라 base64로 인코딩합니다:
    
    
    comfy generate nano-banana \
        --prompt "add a top hat" \
        --image ./cat.png \
        --download edited.png
    
    comfy generate flux-kontext \
        --prompt "add a top hat and a monocle" \
        --input_image ./photo.jpg \
        --download out.png
    
    comfy generate ideogram-edit \
        --image cat.png --mask mask.png \
        --prompt "add sunglasses" \
        --rendering_speed TURBO \
        --download edited.png
    

한 번 업로드하고 여러 호출에서 재사용하려면:
    
    
    comfy generate upload ./photo.jpg     # prints a signed URL
    

업로드된 참조 에셋은 **24시간** 이후 자동으로 삭제됩니다. Comfy 관리 GCS에 서명된 URL로 저장됩니다. 오래 실행되는 파이프라인의 경우 각 작업 이전에 다시 업로드하세요. 자세한 내용은 [참조](https://docs.comfy.org/ko/comfy-cli/reference#upload)를 확인하세요.

### 

​

텍스트 기반 비디오 생성

비디오 작업은 비동기입니다. CLI는 기본적으로 차단 및 폴링합니다:
    
    
    comfy generate seedance \
        --prompt "a hummingbird hovering over a flower" \
        --resolution 1080p --duration 5 \
        --download hummingbird.mp4
    
    comfy generate kling \
        --prompt "a paper boat drifting on a river at dusk" \
        --duration 5 \
        --download boat.mp4
    

`--async`를 사용하면 즉시 반환하고 나중에 다시 시작합니다:
    
    
    comfy generate luma --prompt "neon koi swimming through clouds" --aspect_ratio 16:9 --async
    # prints a job id; resume with:
    comfy generate resume luma <job_id> --download out.mp4
    

### 

​

JSON 스크립팅
    
    
    comfy generate dalle --prompt "a watercolor whale" --json | jq '.data[0].url'
    

## 

​

`comfy generate` 그 외

위의 내용은 에이전트 중심의 요약입니다. 전체 가이드에서는 각 명령을 더 자세히 살펴봅니다:

  * `comfy run`, `comfy jobs`, `comfy validate` — 전체 워크플로
  * `comfy templates` 및 `comfy workflow` 슬롯 편집
  * `comfy nodes` / `comfy models` 검색
  * `--json` 출력 및 에이전트용 `comfy --json discover`

→ [Comfy CLI 시작하기](https://docs.comfy.org/ko/comfy-cli/getting-started) (전체 문서)

## 

​

에이전트 스킬

번들된 Comfy 에이전트 스킬을 Claude Code, Cursor 및 AGENTS.md를 인식하는 모든 도구에 설치하여 코딩 에이전트가 CLI를 직접 사용할 수 있도록 합니다:
    
    
    comfy skills install
    comfy skills list      # comfy, comfy-fragments, comfy-debug, comfy-relay, comfy-director
    comfy skills status    # 설치된 위치 확인
    

이는 `comfy skills install`로 설치되는 **번들된 CLI 스킬** 입니다. [Comfy Cloud MCP](https://docs.comfy.org/ko/agent-tools/mcp)용 **comfy-cloud** Claude Code 플러그인을 호스팅하는 [Comfy Skills](https://github.com/Comfy-Org/comfy-skills/) 저장소와는 별개입니다.

## 

​

관련 자료

자료| 용도  
---|---  
[Comfy CLI 시작하기](https://docs.comfy.org/ko/comfy-cli/getting-started)| **전체** 설치 가이드 및 명령 안내  
[Comfy CLI 참조](https://docs.comfy.org/ko/comfy-cli/reference)| 명령, 플래그, 모델 별칭  
[Comfy MCP](https://docs.comfy.org/ko/agent-tools/mcp)| MCP를 통해 에이전트를 연결하여 채팅 기반 생성  
[GitHub의 comfy-cli](https://github.com/Comfy-Org/comfy-cli)| 소스 저장소, 이슈, 최신 동작  
  
## 

​

피드백

  * **GitHub** : [comfy-cli 이슈](https://github.com/Comfy-Org/comfy-cli/issues)
  * **Discord** : [#comfy-mcp-and-cli](https://discord.gg/xWJn6nhE3R)



이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/agent-tools/cli.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/agent-tools/cli)

[Comfy MCP: AI 에이전트를 ComfyUI에 연결이전](https://docs.comfy.org/ko/agent-tools/mcp)[Comfy Agent다음](https://docs.comfy.org/ko/agent-tools/in-app-agent)

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
