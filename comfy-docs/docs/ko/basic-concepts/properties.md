---
url: https://docs.comfy.org/ko/basic-concepts/properties/
title: ComfyUI \uc18d\uc131: \uc704\uc82f, \uc785\ub825, \ub370\uc774\ud130 \uc720\ud615 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:40.605748+00:00
---

# ComfyUI 속성: 위젯, 입력, 데이터 유형 - ComfyUI

> Source: https://docs.comfy.org/ko/basic-concepts/properties/

## 이 페이지에서

  * 노드는 속성의 컨테이너입니다
  * 데이터 유형



기본 개념

# ComfyUI 속성: 위젯, 입력, 데이터 유형

페이지 복사페이지 복사

ComfyUI 노드 속성이 동작하는 방식을 알아봅니다. 수동 조작용 위젯, 연결용 입력 슬롯, 그래프를 유효하게 유지하는 데이터 유형을 다룹니다.

페이지 복사페이지 복사

## 

​

노드는 속성의 컨테이너입니다

노드에는 보통 _**속성**_ 이 있습니다. _**매개변수**_ 또는 _**특성**_ 이라고도 하는 노드 속성은 변경할 수 있는 변수입니다. 일부 속성은 사용자가 _**위젯**_ 이라는 데이터 입력 필드를 이용해 직접 조정할 수 있습니다. 다른 속성들은 해당 속성의 _**입력 슬롯**_ 이나 포트에 연결된 다른 노드들에 의해 자동으로 제어될 수 있습니다. 일반적으로 속성은 위젯에서 입력으로 변환하거나 그 반대로 변환할 수 있어, 사용자가 속성 값을 수동 또는 자동으로 제어할 수 있습니다. 속성은 다양한 형태를 취할 수 있으며 여러 가지 종류의 정보를 담을 수 있습니다. 예를 들어, **체크포인트 로드** 노드에는 하나의 속성이 있습니다: 생성 모델 체크포인트 파일의 파일 경로입니다. **KSampler** 노드에는 샘플링 **단계** 수, **CFG** 스케일, **sampler_name** 등 여러 속성이 있습니다. ![노드 속성](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2121d646aef4f1386f1f09162312785b)

## 

​

데이터 유형

정보는 _**데이터 유형**_ 이라 불리는 다양한 형태를 가질 수 있습니다. 예를 들어, 영숫자 텍스트는 _**문자열**_ 로 알려져 있고, 정수는 _**정수**_ 이며, 소수점이 포함된 숫자는 _**부동소수점**_ 또는 _**float**_ 라고 합니다. 새로운 데이터 유형은 항상 ComfyUI에 추가되고 있습니다. ComfyUI는 파이썬 스크립팅 언어로 작성되었으며, 파이썬은 데이터 유형에 대해 매우 관대합니다. 반면 ComfyUI 환경은 매우 _**강한 타입**_ 입니다. 이는 서로 다른 데이터 유형을 혼동할 수 없다는 것을 의미합니다. 예를 들어 이미지 출력을 정수 입력에 연결할 수 없습니다. 이는 사용자에게 큰 장점으로 작용하며, 올바른 워크플로우 구성을 안내하고 프로그램 오류를 방지합니다.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/basic-concepts/properties.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/basic-concepts/properties)

[커스텀 노드이전](https://docs.comfy.org/ko/basic-concepts/custom-nodes)[ComfyUI 링크: 노드 연결 작동 방식다음](https://docs.comfy.org/ko/basic-concepts/links)

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
