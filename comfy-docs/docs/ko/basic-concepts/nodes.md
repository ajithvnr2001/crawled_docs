---
url: https://docs.comfy.org/ko/basic-concepts/nodes/
title: ComfyUI \ub178\ub4dc: \uc720\ud615, \uc785\ub825, \ucd9c\ub825 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:40.357863+00:00
---

# ComfyUI 노드: 유형, 입력, 출력 - ComfyUI

> Source: https://docs.comfy.org/ko/basic-concepts/nodes/

## 이 페이지에서

  * 노드는 작업을 수행합니다
  * 다양한 노드 상태
  * 노드 간 연결
    * 노드 연결 및 연결 해제
  * 노드의 외관
    * 노드 배지
  * 노드 컨텍스트 메뉴
    * 노드 컨텍스트 메뉴
    * 모드
    * 입력/출력 컨텍스트 메뉴
  * 노드 선택 도구상자
  * 서브그래프
  * 커스텀 노드
    * ComfyUI 매니저



기본 개념

# ComfyUI 노드: 유형, 입력, 출력

페이지 복사페이지 복사

노드는 ComfyUI의 기본 구성 요소입니다. 링크로 연결하는 독립적인 Comfy Core 또는 커스텀 모듈로 복잡한 워크플로를 구성합니다.

페이지 복사페이지 복사

ComfyUI에서 노드는 작업을 수행하는 기본적인 구성 요소입니다. 각 노드는 독립적으로 구축된 모듈로, **Comfy Core** 노드든 **커스텀 노드** 든 고유한 기능을 갖추고 있습니다. 노드들은 링크를 통해 서로 연결되어 마치 레고 블록을 조립하듯 복잡한 기능을 구축할 수 있게 해줍니다. 다양한 노드들의 조합은 ComfyUI의 무한한 가능성을 만들어냅니다. ![Comfy Core K-Sampler 노드](https://mintcdn.com/dripart/7m9lukFrTCZs7Mhj/images/comfy_core/sampling/k_sampler.png?fit=max&auto=format&n=7m9lukFrTCZs7Mhj&q=85&s=5bb2412a6e137d0a0b630b14845944e1) 예를 들어, K-Sampler 노드를 보면 여러 개의 입력과 출력이 있고, 다양한 파라미터 설정도 포함되어 있습니다. 이 파라미터들은 노드 실행의 논리를 결정합니다. 각 노드 뒤에는 잘 작성된 파이썬 로직이 있어 직접 코드를 작성하지 않아도 원하는 기능을 구현할 수 있습니다.

ComfyUI는 현재 활발히 개발 중이므로 여기서 설명된 일부 내용이 오래되었을 수 있습니다. 변경된 사항을 발견하시면 언제든지 [문서 업데이트에 도움을 주세요](https://github.com/Comfy-Org/docs).

## 

​

노드는 작업을 수행합니다

컴퓨터 과학에서 _**노드**_ 란 정보를 담는 컨테이너로, 보통 어떤 작업을 수행하기 위한 프로그램된 명령어를 포함합니다. 노드는 거의 단독으로 존재하지 않으며, 대부분 네트워크 그래프 내 다른 노드들과 연결됩니다. ComfyUI에서 노드는 서로 연결된 상자 형태로 시각화됩니다. ComfyUI 노드는 보통 _**함수 연산자**_ 입니다. 즉, 특정 데이터를 처리해 어떤 함수를 수행한다는 의미입니다. 함수란 입력 데이터를 받아 어떤 작업을 수행하고 출력 데이터를 생성하는 과정입니다. 다시 말해, 노드는 이미지 생성과 같은 작업을 완성하는 데 기여하는 일을 합니다. 따라서 ComfyUI 노드는 거의 항상 최소 한 개의 입력 또는 출력을 가지며, 보통 여러 개의 입력과 출력을 가집니다.

## 

​

다양한 노드 상태

![노드 상태](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=150ab91575a7c9300b7ed20d8026e499) ComfyUI에서는 노드가 여러 가지 상태를 가집니다. 다음은 일반적인 노드 상태들입니다:

  1. **정상 상태** : 기본 상태
  2. **실행 중 상태** : 실행 중 상태로, 워크플로를 시작한 후 노드가 실행될 때 표시됩니다.
  3. **오류 상태** : 노드 오류로, 워크플로를 실행한 후 노드의 입력에 문제가 있으면 나타나며, 오류가 발생한 입력 노드는 빨간색으로 표시됩니다. 문제 있는 입력을 수정해야만 워크플로가 정상적으로 실행됩니다.
  4. **누락 상태** : 보통 워크플로를 가져온 후 나타나며, 두 가지 경우가 있습니다: 
     * Comfy Core 기본 노드 누락: ComfyUI가 업데이트되었지만 사용자가 이전 버전을 사용하는 경우입니다. 이 문제를 해결하려면 ComfyUI를 업데이트해야 합니다.
     * 커스텀 노드 누락: 워크플로가 제3자 개발자의 커스텀 노드를 사용하는데, 로컬 ComfyUI 버전에 해당 커스텀 노드가 설치되지 않은 경우입니다. [ComfyUI 매니저](https://docs.comfy.org/ko/manager/overview)를 이용해 찾아 설치하거나, [커스텀 노드 설치 방법](https://docs.comfy.org/ko/installation/install_custom_node)을 참고해 다른 방법을 사용할 수 있습니다.



## 

​

노드 간 연결

ComfyUI에서 노드는 [링크](https://docs.comfy.org/ko/basic-concepts/links)를 통해 연결되며, 동일한 유형의 데이터가 서로 다른 처리 장치 간에 흐르면서 최종 결과를 얻게 됩니다. ![ComfyUI 노드 링크](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=40a62b27aa2f44cb97eae917c8c1f8da) 각 노드는 일부 입력을 받고, 자체 모듈을 통해 처리한 후 해당 출력으로 변환합니다. 서로 다른 노드 간의 연결은 데이터 유형 요구사항을 충족해야 합니다. ComfyUI에서는 노드 데이터 유형을 구분하기 위해 서로 다른 색상을 사용합니다. 아래는 몇 가지 기본 데이터 유형입니다: ![ComfyUI 노드 데이터 유형](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5)

데이터 유형| 색상  
---|---  
확산 모델| 라벤더  
CLIP 모델| 노랑  
VAE 모델| 로즈  
컨디셔닝| 주황  
잠재 이미지| 분홍  
픽셀 이미지| 파랑  
마스크| 초록  
숫자 (정수 또는 실수)| 연두  
메쉬| 밝은 초록  
  
ComfyUI가 발전하면서 더 많은 데이터 유형으로 확장할 수도 있습니다.

### 

​

노드 연결 및 연결 해제

![ComfyUI 노드 연결](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/link_nodes.gif?s=06359a20664f48e43763696313a063f9) **연결** : 한 노드의 출력 포인트에서 다른 노드의 같은 색상 입력 포인트로 드래그하여 연결합니다. **연결 해제** : 입력 포인트를 클릭한 후 마우스 왼쪽 버튼을 드래그해 연결을 해제하거나, 링크의 중간 메뉴를 통해 연결을 취소합니다.

## 

​

노드의 외관

![노드 외관](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e7ed881cf2c91cc9c48892dd491cae7b) 다양한 스타일 설정을 제공해 노드의 외관을 맞춤화할 수 있습니다:

  * 스타일 수정
  * 노드 제목을 더블클릭해 노드 이름을 수정
  * 어느 모서리든 드래그해 노드 크기를 조정



### 

​

노드 배지

![노드 배지](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1e22b62c50745c547e2b99c5f13df990) 다양한 노드 배지 표시 기능을 제공하며, 예를 들면 다음과 같습니다:

  * 노드 ID
  * 노드 소스

현재 **Comfy Core 노드** 는 여우 아이콘을 사용해 표시되고, 커스텀 노드는 이름을 사용합니다. 이를 통해 어떤 노드 패키지에서 온 노드인지 빠르게 이해할 수 있습니다. 메뉴에서 해당 표시를 설정할 수 있습니다: ![배지 설정](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f63c9698836a1debc6a1bed84d77fdf2)

## 

​

노드 컨텍스트 메뉴

노드 컨텍스트 메뉴는 크게 두 가지로 나뉩니다:

  * 노드 자체의 컨텍스트 메뉴
  * 입력/출력의 컨텍스트 메뉴



### 

​

노드 컨텍스트 메뉴

노드를 우클릭하면 해당 노드의 컨텍스트 메뉴를 확장할 수 있습니다: ![노드 컨텍스트 메뉴](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d7d99664537a4f2b09aaf0acc228da4f) 노드의 우클릭 컨텍스트 메뉴에서는 다음을 수행할 수 있습니다:

  * 노드의 색상 스타일 조정
  * 제목 수정
  * 노드 복제, 복사, 삭제
  * 노드 모드 설정

이 메뉴에서 외관 관련 설정 외에도 중요한 메뉴 작업은 다음과 같습니다:

  * **모드** : 노드의 모드 설정: 항상, 절대, 바이패스



#### 

​

모드

모드에 대해 알아보면 현재 제공되는 것은: 항상, 절대, 이벤트 발생 시, 트리거 발생 시 - 네 가지 모드가 있지만 실제로 효과적인 것은 **항상** 과 **절대** 뿐입니다. **이벤트 발생 시** 와 **트리거 발생 시** 는 아직 이 기능을 완벽히 구현하지 않았기 때문에 효과적이지 않습니다. 또한 **바이패스** 는 하나의 모드로 이해할 수 있습니다. 가능한 모드에 대한 설명은 다음과 같습니다:

  * **항상** : 기본 노드 모드. 노드가 처음 실행되거나 마지막 실행 이후 입력이 변경되면 언제든 실행됩니다.
  * **절대** : 어떠한 경우에도 노드가 실행되지 않으며, 마치 삭제된 것과 같습니다. 이후 노드는 이 노드로부터 어떤 데이터도 읽거나 받을 수 없습니다.
  * **바이패스** : 어떠한 경우에도 노드가 실행되지 않지만, 이후 노드는 이 노드가 처리하지 않은 데이터를 얻으려고 시도할 수 있습니다.

다음은 `절대`와 `바이패스` 모드의 비교입니다: ![절대 vs 바이패스 모드](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/node/never_vs_bypass.jpg?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=9adb00fa408eb3f09805030cd7a731c2) 이 비교 예시에서 볼 수 있듯이, 두 워크플로우 모두 동시에 두 개의 LoRA 모델을 적용하는데, 차이점은 하나의 `LoRA 로드` 노드는 `절대` 모드로 설정된 반면 다른 하나는 `바이패스` 모드로 설정되었습니다.

  * `절대` 모드로 설정된 노드는 이후 노드들이 입력 데이터를 전혀 받지 못해 오류를 보이게 됩니다.
  * `바이패스` 모드로 설정된 노드는 이후 노드들이 처리되지 않은 데이터를 계속 받을 수 있으므로, 첫 번째 `LoRA 로드` 노드의 출력 데이터를 로드해 이후 워크플로우가 정상적으로 진행됩니다.



### 

​

입력/출력 컨텍스트 메뉴

이 컨텍스트 메뉴는 주로 해당 입력/출력의 데이터 유형과 관련이 있습니다: ![노드 입력/출력 컨텍스트 메뉴](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2daf16654cdd151a6b9ace6ef9d9e530) 노드의 입력/출력을 드래그할 때 연결이 생겼지만 다른 노드의 입력이나 출력에 연결하지 않았다면, 마우스를 놓으면 입력/출력의 컨텍스트 메뉴가 나타나며, 관련 유형의 노드를 빠르게 추가할 수 있습니다. 설정에서 노드 제안 수를 조정할 수 있습니다: ![노드 제안 수](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7a063583df5825a8cc24dc13a1723761)

## 

​

노드 선택 도구상자

**노드 선택 도구상자** 는 노드에 대한 빠른 작업을 제공하는 플로팅 도구입니다. 노드를 선택하면 선택된 노드 위에 떠 있게 되며, 이 도구상자를 통해 다음을 수행할 수 있습니다:

  * 노드의 색상 변경
  * 노드를 빠르게 바이패스 모드로 설정(실행 중에 실행 안 함)
  * 노드 잠금
  * 노드 삭제

물론 이러한 기능들은 해당 노드의 우클릭 메뉴에서도 찾을 수 있습니다. 노드 선택 도구상자는 단순히 바로가기 기능을 제공할 뿐입니다. 이 기능을 비활성화하려면 설정에서 끌 수 있습니다. ![노드 선택 도구상자 비활성화](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=60747b0e83640a2f7a4f1bc66e63a89c)

## 

​

서브그래프

선택한 노드들을 하나의 재사용 가능한 서브그래프 노드로 묶어 복잡한 그래프를 정리하고, 동일한 구조를 여러 워크플로에서 재사용할 수 있습니다.

## 서브그래프

서브그래프 블루프린트를 만들고, 편집하고, 중첩하고, 노드 라이브러리에 게시하는 방법을 알아보세요.

## 

​

커스텀 노드

ComfyUI는 기본 설치에 많은 **Comfy Core** 노드를 포함하고 있습니다. 커뮤니티는 전문적인 워크플로우를 위한 [**커스텀 노드**](https://registry.comfy.org) 카탈로그도 유지하고 있습니다. 커스텀 노드 설치 방법—**ComfyUI 매니저** , Git 복제, ZIP 다운로드, 의존성, 안전 팁—에 대한 전체 요약은 [커스텀 노드 설치 방법](https://docs.comfy.org/ko/installation/install_custom_node)을 참조하세요.

### 

​

ComfyUI 매니저

매일의 커스텀 노드 작업에 **ComfyUI 매니저** 를 사용하세요: 레지스트리에서 검색하고 설치, 패키지 업데이트 또는 비활성화, 가져온 워크플로우에서 누락된 노드 탐지, 확장과 함께 모델 및 스냅샷 관리까지 가능합니다. 데스크탑 빌드에는 기본적으로 활성화되어 있으며, 휴대용 및 수동 설치는 먼저 활성화해야 할 수 있습니다.

## ComfyUI 매니저

개요, Manager 활성화 및 노드 설치 워크플로우

이 페이지가 도움이 되었나요?

예아니오

[수정 제안](https://github.com/comfy-org/docs/edit/main/ko/basic-concepts/nodes.mdx)[문제 보고](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ko/basic-concepts/nodes)

[ComfyUI 워크플로우: 노드, 링크, 비주얼 프로그래밍이전](https://docs.comfy.org/ko/basic-concepts/workflow)[커스텀 노드다음](https://docs.comfy.org/ko/basic-concepts/custom-nodes)

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
