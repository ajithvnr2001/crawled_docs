---
url: https://docs.comfy.org/ko/tutorials/partner-nodes/overview/
title: \ud30c\ud2b8\ub108 \ub178\ub4dc - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:44.108478+00:00
---

# 파트너 노드 - ComfyUI

> Source: https://docs.comfy.org/ko/tutorials/partner-nodes/overview/

## 이 페이지에서

  * 파트너 노드란 무엇인가요?
  * 파트너 노드 사용을 위한 사전 요구사항
    * 1\. ComfyUI 버전 요구사항
    * 2\. 계정 및 크레딧 요구사항
    * 3\. 네트워크 환경 요구사항
    * 4\. 해당 노드 사용하기
  * 화이트리스트에 등록되지 않은 웹사이트에서 ComfyUI 계정 API 키로 로그인하기
  * ComfyUI 계정 API 키 통합을 이용해 유료 모델 파트너 노드 호출하기
  * 파트너 노드의 장점
  * 가격 정책
  * 모델 공급자
  * 오픈소스 및 옵트인에 대하여
  * 파트너 노드를 완전히 비활성화하는 방법
  * 활용 사례
  * FAQ



파트너 노드

# 파트너 노드

페이지 복사페이지 복사

Partner Nodes는 ComfyUI 내부의 API 요청을 통해 OpenAI, Kling, Luma 등 폐쇄형 모델을 호출합니다. 정의, 크레딧, 사용 방법을 다룹니다.

페이지 복사페이지 복사

파트너 노드는 ComfyUI가 API 요청을 통해 폐쇄형 모델을 호출하는 새로운 방식으로, 복잡한 API 키 설정 없이 ComfyUI 사용자들이 외부의 최신 AI 모델에 접근할 수 있도록 제공합니다.

## 

​

파트너 노드란 무엇인가요?

파트너 노드는 외부 API 서비스와 연결되는 특수한 노드 세트로, 폐쇄형 또는 타사에서 호스팅하는 AI 모델을 바로 ComfyUI 워크플로우에서 사용할 수 있게 해줍니다. 이러한 노드들은 외부 모델의 기능을 원활하게 통합하면서도 ComfyUI 핵심의 오픈소스 성격을 유지하도록 설계되었습니다.

## 

​

파트너 노드 사용을 위한 사전 요구사항

파트너 노드를 사용하려면 다음의 요구사항을 충족해야 합니다:

### 

​

1\. ComfyUI 버전 요구사항

ComfyUI를 최신 버전으로 업데이트해 주세요. 향후 더 많은 API 지원이 추가될 수 있으며, 이에 맞춰 해당 노드도 업데이트될 예정이므로 항상 ComfyUI를 최신 상태로 유지해 주시기 바랍니다.

야간 빌드와 릴리스 버전 간의 차이점을 유의해 주세요. 릴리스 버전은 적시에 업데이트되지 않을 수 있으므로, `야간 빌드` 버전(최신 코드 커밋)을 사용하는 것을 권장합니다.  
이는 개발 버전과 안정화 버전을 의미하며, 저희가 여전히 빠르게 반복 개발 중이므로 본 문서는 신속하게 업데이트되지 않을 수 있습니다. 따라서 버전 차이에 유의해 주시기 바랍니다.

### 

​

2\. 계정 및 크레딧 요구사항

[Comfy 계정](https://docs.comfy.org/ko/interface/user)으로 ComfyUI에 로그인되어 있어야 하며, [크레딧](https://docs.comfy.org/ko/interface/credits) 잔액이 0보다 많아야 합니다. `설정` -> `사용자`를 통해 로그인하세요: ![ComfyUI 사용자 인터페이스](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/user.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4aacfc636460e073d16ef1fdaccb0888) `설정` -> `크레딧`으로 이동하여 크레딧을 구매하세요: ![크레딧 인터페이스](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/setting/purchase-1.jpg?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=d4371030bb5549d08feb37abd8ae19fb) 계정 및 크레딧 관련 자세한 내용은 다음 문서를 참조해 주세요:

  * [Comfy 계정](https://docs.comfy.org/ko/interface/user): 설정 메뉴에서 `사용자` 섹션을 찾아 로그인하세요.
  * [크레딧](https://docs.comfy.org/ko/interface/credits): 로그인 후 설정 인터페이스에 크레딧 메뉴가 표시되며, 여기서 크레딧을 구매할 수 있습니다. 저희는 선불 방식을 사용하므로 예상치 못한 요금 청구는 없습니다.



### 

​

3\. 네트워크 환경 요구사항

API 접근을 위해서는 현재 요청이 안전한 네트워크 환경을 기반으로 해야 합니다. API 접근을 위한 현재 요구사항은 다음과 같습니다:

  * 로컬 네트워크는 `127.0.0.1` 또는 `localhost`로부터만 접속을 허용하며, 직접 로그인 기능을 사용할 수 있습니다.
  * 만약 로컬 네트워크나 화이트리스트에 등록되지 않은 웹사이트에서 접근하려는 경우, API Key를 사용해 로그인해 주세요. [API Key로 로그인하기](https://docs.comfy.org/ko/interface/user#api-%ED%82%A4%EB%A1%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%95%98%EA%B8%B0)를 참고해 주세요.
  * 당사의 API 서비스에 정상적으로 접근할 수 있어야 합니다(일부 지역에서는 프록시 서비스를 이용해야 할 수도 있습니다).
  * 요청의 보안을 확보하기 위해 `https` 환경에서 접근해야 합니다.



비안전한 환경에서 접근하면 큰 위험이 따르며, 다음과 같은 결과를 초래할 수 있습니다:

  1. 인증 정보가 도난당해 계정 정보가 유출될 수 있습니다.
  2. 악의적으로 계정이 사용되어 금전적 손실이 발생할 수 있습니다.

향후 이 제한을 해제하더라도, 비안전한 네트워크 요청을 통해 API 서비스에 접근하는 것은 매우 위험하므로 절대 권장하지 않습니다.

### 

​

4\. 해당 노드 사용하기

**워크플로우에 추가** : 다른 노드와 마찬가지로 파트너 노드를 워크플로우에 추가하세요. **실행** : 매개변수를 설정한 후 워크플로우를 실행하세요. ![파트너 노드](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/tutorial/api_nodes/sidebar.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=5adc8f697864ac7d890722dddbb8260c)

## 

​

화이트리스트에 등록되지 않은 웹사이트에서 ComfyUI 계정 API 키로 로그인하기

현재 우리는 ComfyUI 계정에 로그인할 수 있는 웹사이트를 제한하기 위해 화이트리스트를 설정했습니다. 만약 일부 화이트리스트에 등록되지 않은 웹사이트에서 ComfyUI 계정에 로그인해야 한다면, 계정 관리 섹션을 참고해 API 키를 이용한 로그인 방법을 알아보세요. 이 경우 해당 웹사이트가 우리의 화이트리스트에 반드시 등록되어 있을 필요는 없습니다.

## 계정 관리

ComfyUI 계정 API 키로 로그인하는 방법 알아보기

![Comfy API 키 로그인 선택](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdb8d99a4bd52a6cc1de1b3453e8cfda)

## 

​

ComfyUI 계정 API 키 통합을 이용해 유료 모델 파트너 노드 호출하기

현재 우리는 ComfyUI API 키 통합을 통해 유료 모델 파트너 노드를 호출하는 서비스에 접근할 수 있도록 지원하고 있습니다. API 키 통합 섹션을 참고해 유료 모델 파트너 노드를 호출하는 방법을 알아보세요.

**중요:** 여기서 다루는 API 키는 귀하의 **ComfyUI 계정 API 키**(워크플로우에서 유료 파트너 노드에 접근하는 데 사용됨)입니다. 이는 개발자가 커스텀 노드를 레지스트리에 게시하는 데 사용하는 **레지스트리 게시 API 키** 와는 **다릅니다**. 커스텀 노드를 게시하려면 [노드 게시](https://docs.comfy.org/ko/registry/publishing)를 참조하세요.

## API 키 통합

API 키 통합 섹션을 참고해 유료 모델 파트너 노드를 호출하는 방법 알아보기

## 

​

파트너 노드의 장점

파트너 노드는 ComfyUI 사용자들에게 다음과 같은 중요한 장점을 제공합니다:

  * **폐쇄형 모델 접근** : 직접 배포할 필요 없이 최신 AI 모델을 사용할 수 있습니다
  * **원활한 통합** : 파트너 노드는 다른 ComfyUI 노드와 완벽히 호환되며, 이를 조합해 복잡한 워크플로우를 만들 수 있습니다
  * **간편한 경험** : API 키를 관리하거나 복잡한 API 요청을 처리할 필요가 없습니다
  * **비용 통제** : 선불 시스템 덕분에 예상치 못한 비용 없이 지출을 완벽히 관리할 수 있습니다



## 

​

가격 정책

## 파트너 노드 가격 정책

해당 파트너 가격 정책 페이지를 참고하세요

## 

​

모델 공급자

## 모델 공급자

파트너 노드에 사용되는 모델 공급자의 검증 상태, 상업용 라이선스, 데이터 상주 위치를 확인하세요

## 

​

오픈소스 및 옵트인에 대하여

**파트너 노드는 완전히 선택적** 이라는 점에 유의하세요. ComfyUI는 언제나 완전히 오픈소스이며, 지역 사용자에게 무료로 제공됩니다. 파트너 노드는 ‘옵트인’ 기능으로 설계되어, 외부 SOTA(최신) 모델에 접근하고자 하는 사용자들에게 편의를 제공합니다.

## 

​

파트너 노드를 완전히 비활성화하는 방법

ComfyUI에서 모든 파트너 노드를 비활성화하려면 `--disable-partner-nodes` 실행 인자를 추가하면 됩니다. 프런트엔드가 인터넷과 통신하지 못하게 하려면 대신 `--offline`을 사용하세요. **수동 설치용:**
    
    
    python main.py --disable-partner-nodes
    

**휴대용 사용자용 (윈도우):** `run_xxx.bat` 파일을 업데이트하세요:
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build --disable-partner-nodes
    pause
    

## 

​

활용 사례

파트너 노드의 강력한 응용 사례 중 하나는 외부 모델의 출력을 로컬 노드와 결합하는 것입니다. 예를 들어:

  * GPT-Image-1을 사용해 기본 이미지를 생성한 후, 로컬 `wan` 노드로 이를 동영상으로 변환하기
  * 외부에서 생성된 이미지를 로컬 업스케일링이나 스타일 전송 노드와 결합하기
  * 폐쇄형 모델과 오픈소스 모델의 장점을 모두 활용한 하이브리드 워크플로우 만들기

이러한 유연성 덕분에 ComfyUI는 다양한 AI 기능을 통합한 진정한 범용 생성 AI 인터페이스가 되었으며, 더 많은 가능성을 열어줍니다.

## 

​

FAQ

왜 파트너 노드를 찾을 수 없나요?

ComfyUI를 최신 버전으로 업데이트해 주세요(최신 커밋 또는 최신 [데스크톱 버전](https://www.comfy.org/download)). 향후 더 많은 API 지원을 추가하고 해당 노드도 업데이트될 예정이니, ComfyUI를 항상 최신 상태로 유지해 주세요.

최신 테스트 버전(nightly)과 릴리즈 버전을 구분해야 한다는 점에 유의해 주세요. 경우에 따라 최신 `릴리즈` 버전이 `최신 테스트 버전(nightly)`보다 제때 업데이트되지 않을 수 있습니다. 아직 빠르게 반복 개발 중이므로, 해당 노드를 찾을 수 없는 경우 반드시 최신 버전을 사용해 주세요.

왜 파트너 노드를 사용하거나 로그인할 수 없나요?

API 접근을 위해서는 현재 요청이 안전한 네트워크 환경을 기반으로 해야 합니다. 현재 API 접근 요구사항은 다음과 같습니다:

  * 로컬 네트워크는 `127.0.0.1` 또는 `localhost`에서만 접속을 허용하므로, LAN 환경에서 `--listen` 매개변수로 시작된 ComfyUI 서비스에서는 파트너 노드를 사용할 수 없습니다.
  * 당사 API 서비스에 정상적으로 접근 가능해야 합니다(일부 지역에서는 프록시 서비스가 필요할 수 있음).
  * 계정에 충분한 [크레딧](https://docs.comfy.org/ko/interface/credits)이 있어야 합니다.



로그인 후에도 왜 파트너 노드를 사용할 수 없거나 계속해서 로그인을 요구하나요?

  * 현재 `127.0.0.1` 또는 `localhost` 접속만 지원됩니다.
  * 계정에 충분한 크레딧이 있는지 확인해 주세요.



파트너 노드는 무료로 사용할 수 있나요?

파트너 노드는 폐쇄형 모델에 대한 API 호출에 크레딧이 필요하므로, 무료 사용을 지원하지 않습니다.

크레딧을 어떻게 구매하나요?

다음 문서를 참고해 주세요:

  1. [Comfy 계정](https://docs.comfy.org/ko/interface/user): 설정 메뉴에서 `사용자` 섹션을 찾아 로그인하세요.
  2. [크레딧](https://docs.comfy.org/ko/interface/credits): 로그인 후 설정 인터페이스에 크레딧 메뉴가 표시됩니다. `설정` → `크레딧`에서 크레딧을 구매할 수 있습니다. 선불 방식을 사용하므로 예상치 못한 요금 청구는 없습니다.
  3. Stripe를 통해 결제를 완료하세요.
  4. 크레딧이 업데이트되었는지 확인하세요. 그렇지 않은 경우 페이지를 다시 시작하거나 새로고침해 보세요.



미사용 크레딧은 환불받을 수 있나요?

현재 크레딧에 대한 환불은 지원되지 않습니다. 기술적 문제로 인해 미사용 잔액이 발생했다고 판단되는 경우, [지원팀에 문의](mailto:support@comfy.org)해 주세요.

크레딧이 마이너스로 갈 수 있나요?

크레딧은 마이너스 잔액이나 신용 한도로 사용하도록 설계되지 않았습니다. 그러나 경합 조건으로 인해 파트너 노드가 실행 전에 항상 비용을 보고하지 않는 경우, 한 번의 실행으로 남은 잔액보다 더 많은 크레딧을 소모해 일시적으로 마이너스 잔액이 될 수 있습니다. 잔액이 마이너스인 경우, 충전해 양수 잔액을 복원할 때까지 파트너 노드를 실행할 수 없습니다. API 호출 전에 충분한 크레딧이 있는지 확인해 주세요.

사용량과 지출 내역은 어디서 확인할 수 있나요?

로그인 후 [크레딧](https://docs.comfy.org/ko/interface/credits) 메뉴를 방문해 해당 크레딧을 확인해 주세요.

내 API 키를 사용할 수 있나요?

현재 파트너 노드는 아직 테스트 단계이며 이 기능을 지원하지 않지만, 추가하는 것을 고려하고 있습니다.

크레딧은 만료되나요?

예, 만료 기간은 크레딧 종류에 따라 다릅니다:

  * **월간 크레딧** : 청구 주기 종료 시 만료
  * **충전형 크레딧** : 구매일로부터 1년 후 만료



크레딧을 이전하거나 공유할 수 있나요?

아니요, 귀하의 크레딧은 다른 사용자에게 이전할 수 없으며 현재 로그인된 계정에만 한정됩니다. 다만, 로그인 가능한 기기 수에는 제한이 없습니다.

동일한 계정을 여러 기기에서 사용할 수 있나요?

로그인 가능한 기기 수에는 제한이 없으므로, 원하는 곳에서 계정을 사용할 수 있습니다.

내 계정이나 정보를 삭제해 달라고 요청하려면 어떻게 하나요?

[support@comfy.org](mailto:support@comfy.org)로 이메일을 보내주시면 귀하의 정보를 삭제해 드립니다.

파트너 노드에 콘텐츠 심사가 있나요?

파트너 노드는 사용자의 입력(프롬프트, 이미지 등)을 타사 제공업체에 전송하여 처리합니다. 해당 제공업체는 자체 콘텐츠 심사 정책을 적용합니다. 파트너 노드에 NSFW 또는 기타 금지된 콘텐츠를 제출하지 마십시오.

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/tutorials/partner-nodes/overview.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/tutorials/partner-nodes/overview)

[Comfy Cloud 노드이전](https://docs.comfy.org/ko/cloud-nodes/overview)[Partner Node 가격다음](https://docs.comfy.org/ko/tutorials/partner-nodes/pricing)

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
