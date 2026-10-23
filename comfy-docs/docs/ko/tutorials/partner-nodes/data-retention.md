---
url: https://docs.comfy.org/ko/tutorials/partner-nodes/data-retention/
title: \ud30c\ud2b8\ub108 \ub178\ub4dc \ub370\uc774\ud130 \ubcf4\uc874 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:42.678318+00:00
---

# 파트너 노드 데이터 보존 - ComfyUI

> Source: https://docs.comfy.org/ko/tutorials/partner-nodes/data-retention/

## 이 페이지에서

  * 저장되는 항목
  * 파일 보존 기간
  * 삭제 후 발생하는 상황
  * 파일을 더 오래 보관하기
  * 참조



파트너 노드

# 파트너 노드 데이터 보존

페이지 복사페이지 복사

Comfy가 파트너 노드 입력과 출력을 저장하고 삭제하는 방법과 미디어 파일이 보존되는 기간을 설명합니다.

페이지 복사페이지 복사

모든 파트너 노드 요청은 플랫폼에 저장되는 데이터를 생성합니다. 입력(이미지, 비디오, 3D 에셋, 오디오)과 모델이 생성한 출력이 여기에 해당합니다. 이 페이지에서는 각 데이터 유형이 보존되는 기간을 설명합니다. 각 공급자가 이 데이터를 기본적으로 어디에서 처리하는지는 [모델 공급자](https://docs.comfy.org/ko/tutorials/partner-nodes/model-providers)에서 확인할 수 있습니다.

## 

​

저장되는 항목

파트너 노드를 실행하면 두 종류의 파일이 저장됩니다.

  * **입력 파일** : 노드에 제공하는 참조 이미지, 오디오 및 기타 미디어. 입력은 계정의 스토리지 공간에 업로드됩니다.
  * **출력 파일** : 노드가 생성하는 이미지, 비디오, 오디오 및 기타 미디어. 출력은 Comfy 관리 스토리지에 기록되며 다운로드 URL로 제공됩니다.

입력 및 출력 파일은 모두 Comfy 관리 클라우드 스토리지 버킷에 저장됩니다.

## 

​

파일 보존 기간

모든 파트너 노드 미디어 파일은 생성된 후 **24시간** 이 지나면 자동으로 삭제됩니다. 삭제는 입력 및 출력 파일 모두에 적용됩니다.

파일 유형| 삭제 시점  
---|---  
입력 파일| 24시간  
출력 파일| 24시간  
  
24시간 삭제 기간은 플랫폼 기본값이며 모든 파트너 노드 호출에 적용됩니다. 파일을 더 오래 보관해야 하는 경우 만료되기 이전에 자체 스토리지로 다운로드하세요.

## 

​

삭제 후 발생하는 상황

파일이 삭제되면 해당 다운로드 URL은 오류를 반환합니다. 삭제된 파일은 복구할 수 없으며, 다시 필요할 경우 동일한 미디어를 다시 업로드하거나 재생성해야 합니다. 입력 파일을 삭제하면 계정 스토리지에서 해당 파일 기록도 제거되므로 이후 호출에서 해당 입력을 재사용할 수 없습니다.

## 

​

파일을 더 오래 보관하기

워크플로에서 입력 파일을 24시간 이상 계속 사용할 수 있어야 하는 경우, 각 작업 이전에 파일을 다시 업로드하세요. 장기 실행 파이프라인의 경우 해당 파일이 필요한 호출 직전에 다시 업로드하세요. 보관하려는 출력이 있다면 24시간 이내에 자체 스토리지로 다운로드하세요.

## 

​

참조

항목| 값  
---|---  
입력 파일 보존 기간| 24시간  
출력 파일 보존 기간| 24시간  
  
Comfy가 고객 데이터를 처리하는 방법에 대한 일반 정보는 [데이터 보존](https://docs.comfy.org/ko/support/data-retention)을 참조하세요.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/tutorials/partner-nodes/data-retention.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/tutorials/partner-nodes/data-retention)

[파트너 노드에 관한 FAQ이전](https://docs.comfy.org/ko/tutorials/partner-nodes/faq)[모델 공급자다음](https://docs.comfy.org/ko/tutorials/partner-nodes/model-providers)

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
