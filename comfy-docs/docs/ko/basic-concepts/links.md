---
url: https://docs.comfy.org/ko/basic-concepts/links/
title: ComfyUI \ub9c1\ud06c: \ub178\ub4dc \uc5f0\uacb0 \uc791\ub3d9 \ubc29\uc2dd - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:40.503041+00:00
---

# ComfyUI 링크: 노드 연결 작동 방식 - ComfyUI

> Source: https://docs.comfy.org/ko/basic-concepts/links/

## 이 페이지에서

  * 링크는 노드를 연결합니다
    * 경유점 노드
  * 색상 코드화



기본 개념

# ComfyUI 링크: 노드 연결 작동 방식

페이지 복사페이지 복사

ComfyUI에서 노드를 연결하는 링크의 작동 방식, 링크 표시 스타일 변경 방법, 복잡한 워크플로우를 정리하는 Reroute 노드 사용법을 알아보세요.

페이지 복사페이지 복사

## 

​

링크는 노드를 연결합니다

ComfyUI에서 노드 간에 그려진 선이나 곡선을 _**링크**_ 라고 합니다(또한 _**연결**_ 또는 와이어라고도 함). 이들은 한 노드의 출력에서 다른 노드의 입력으로 데이터를 전달하며, 워크플로의 흐름을 정의합니다. 링크는 여러 가지 시각적 스타일로 표시할 수 있습니다: 곡선, 직각, 직선 또는 아예 숨길 수도 있습니다. ![링크 스타일](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/link_styles.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=1d678959a9c5bd80d68231d5b6fed78d) 링크 스타일을 변경하려면 **설정 메뉴** → **표시(Lite Graph)** → **그래프** → **링크 렌더 모드** 로 이동하세요. ![렌더 모드 설정](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/render_mode.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=25d9de19b526f8ec618a9b5e9ed87ed9) 또한 **캔버스 메뉴** 에서 모든 링크를 일시적으로 숨길 수 있습니다. ![캔버스 메뉴](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/canvas_menu.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=3925615b50749cbd3f7ed8c0b320d5eb)

링크를 표시하는 것은 특히 워크플로를 학습하거나 공유하거나 디버깅할 때 유용합니다. 데이터 흐름을 한눈에 볼 수 있게 해줍니다. 편집할 필요가 없는 완료된 워크플로에서는 링크를 숨기면 시각적 혼잡을 줄일 수 있습니다.

### 

​

경유점 노드

워크플로가 복잡해지면 링크 와이어가 겹치거나 노드 뒤로 지나가 읽기 어려워질 수 있습니다. **경유점** 노드를 사용하면 2D 그래프 공간의 어느 지점으로든 와이어를 수동으로 리디렉션할 수 있어 레이아웃을 깔끔하고 읽기 쉽게 유지할 수 있습니다. ![ComfyUI 경유점 노드](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=d713aae29a8454af5a671d07e0c35ab1) ComfyUI에는 그래프 캔버스 자체에 경유점 기능이 기본 내장되어 있습니다. 새 워크플로에서는 이 기능을 사용하는 것을 권장합니다. ![ComfyUI 기본 경유점](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/native_reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4d0e70a8300bdd79f2d6a623b40306f8)

## 

​

색상 코드화

ComfyUI의 모든 데이터 유형은 고유한 색상을 가집니다. 노드의 입력 및 출력 포트와 이를 연결하는 링크 와이어는 모두 이 색상 체계를 공유합니다. **같은 색상의 포트만 연결할 수 있습니다**. 이는 워크플로 전체에서 타입 안전성을 보장합니다. ![ComfyUI 노드 데이터 유형](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5)

데이터 유형| 색상  
---|---  
확산 모델| 라벤더  
CLIP 모델| 노란색  
VAE 모델| 장미색  
조건화| 주황색  
잠재 이미지| 분홍색  
픽셀 이미지| 파란색  
마스크| 초록색  
숫자 (정수 또는 실수)| 회색  
메시| 밝은 초록색  
  
이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/basic-concepts/links.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/basic-concepts/links)

[ComfyUI 속성: 위젯, 입력, 데이터 유형이전](https://docs.comfy.org/ko/basic-concepts/properties)[ComfyUI 모델: 파일, 폴더, 로더 노드다음](https://docs.comfy.org/ko/basic-concepts/models)

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
