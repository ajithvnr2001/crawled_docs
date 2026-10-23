---
url: https://docs.comfy.org/ja/basic-concepts/dependencies/
title: \u4f9d\u5b58\u95a2\u4fc2 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:32.682538+00:00
---

# 依存関係 - ComfyUI

> Source: https://docs.comfy.org/ja/basic-concepts/dependencies/

## このページの内容

  * ワークフローファイルは他のファイルに依存します
  * アセット
  * カスタムノード
  * Python 依存関係
    * ComfyUI の依存関係
    * カスタムノードの依存関係
    * 依存関係の競合
  * モデル
  * ソフトウェア



基本概念

# 依存関係

ページをコピーページをコピー

ComfyUI ワークフローの実行に必要な依存関係（メディアアセット、カスタムノード、Python パッケージ、モデル）について解説します。

ページをコピーページをコピー

## 

​

ワークフローファイルは他のファイルに依存します

私たちはよくコミュニティから様々なワークフローファイルを入手しますが、読み込んだ後にワークフローが直接実行できないことが頻繁にあります。これは、ワークフローファイルがワークフロー自体だけでなく、メディアアセットの入力、モデル、カスタムノード、関連する Python 依存関係など、他のファイルにも依存しているためです。 ComfyUI のワークフローは、すべての関連する依存関係が満たされた場合にのみ正常に実行できます。 ComfyUI のワークフロー依存関係は主に以下のカテゴリに分類されます：

  * アセット（オーディオ、ビデオ、画像、その他の入力を含むメディアファイル）
  * カスタムノード
  * Python 依存関係
  * モデル（Stable Diffusion モデルなど）



## 

​

アセット

AI モデルは _**アセット**_ の一例です。メディア制作において、アセットとは入力データを提供する某种のメディアファイルのことです。例えば、ビデオ編集プログラムはディスクに保存された映画ファイルを操作します。編集プログラムのプロジェクトファイルは、これらの映画ファイルアセットへのリンクを保持し、元の映画ファイルを変更しない非破壊編集を可能にします。 ComfyUI も同じように動作します。ワークフローは、必要なすべてのアセットが見つかり、ロードされた場合にのみ実行できます。生成 AI モデル、画像、映画、サウンドなどは、ワークフローが依存する可能性のあるアセットの例です。したがって、これらは _**依存アセット**_ または _**アセット依存関係**_ として知られています。

## 

​

カスタムノード

カスタムノードは、その機能を拡張する ComfyUI の重要なコンポーネントです。これらはコミュニティによって作成され、ワークフローに新しい機能を追加するためにインストールできます。

## 

​

Python 依存関係

ComfyUI は Python ベースのプロジェクトです。私たちは ComfyUI を実行するためにスタンドアロンの Python 環境を構築しており、すべての関連依存関係はこの孤立した Python 環境にインストールされます。

### 

​

ComfyUI の依存関係

ComfyUI の現在の依存関係は、[requirements.txt](https://github.com/Comfy-Org/ComfyUI/blob/master/requirements.txt) ファイルで確認できます：
    
    
    comfyui-frontend-package==1.49.6
    comfyui-workflow-templates==0.11.48
    comfyui-embedded-docs==0.5.10
    torch
    torchsde
    torchvision
    torchaudio
    numpy>=1.25.0
    einops
    transformers>=4.50.3
    tokenizers>=0.13.3
    sentencepiece
    safetensors>=0.4.2
    aiohttp>=3.11.8
    yarl>=1.18.0
    pyyaml
    Pillow
    scipy
    tqdm
    psutil
    alembic
    SQLAlchemy>=2.0.0
    filelock
    av>=17.0.0
    comfy-kitchen==0.2.31
    comfy-aimdo==0.4.15
    requests
    simpleeval>=1.0.0
    blake3
    
    #non essential dependencies:
    kornia>=0.7.1
    spandrel
    pydantic~=2.0
    pydantic-settings~=2.0
    PyOpenGL>=3.1.8
    comfy-angle
    

ComfyUI の進化に伴い、新しい依存関係の追加や不要になった依存関係の削除など、依存関係を適宜調整する場合があります。 したがって、Git を使用して ComfyUI を更新する場合は、最新の更新をプルした後、対応する環境で以下のコマンドを実行する必要があります：
    
    
    pip install -r requirements.txt
    

これにより、ComfyUI の依存関係が適切に動作するように最新の状態に保たれます。特定のパッケージの依存関係バージョンを変更して、特定の依存関係をアップグレードまたはダウングレードすることもできます。 さらに、ComfyUI のフロントエンド [ComfyUI_frontend](https://github.com/Comfy-Org/ComfyUI_frontend) は現在、別のプロジェクトとして維持されています。対応するバージョンが安定した後、`comfyui-frontend-package` 依存関係のバージョンを更新します。別のフロントエンドバージョンに切り替える必要がある場合は、[こちら](https://pypi.org/project/comfyui-frontend-package/#history)でバージョン情報を確認できます。

### 

​

カスタムノードの依存関係

ComfyUI コミュニティの多くの作者の努力のおかげで、異なるカスタムノードを使用することで ComfyUI の機能を拡張し、印象的な創造性を実現できます。 通常、各カスタムノードには独自の依存関係があり、個別の `requirements.txt` ファイルがあります。 [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager) を使用してカスタムノードをインストールする場合、ComfyUI Manager は通常、対応する依存関係を自動的にインストールします。 手動で依存関係をインストールする必要がある場合もあります。現在、すべてのカスタムノードは `ComfyUI/custom_nodes` ディレクトリにインストールされます。 ComfyUI Python 環境で対応するプラグインディレクトリに移動し、`pip install -r requirements.txt` を実行して依存関係をインストールする必要があります。 [Windows ポータブル版](https://docs.comfy.org/ja/installation/comfyui_portable_windows) を使用している場合は、`ComfyUI_windows_portable` ディレクトリで以下のコマンドを使用できます：
    
    
    python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\<custom_node_name>\requirements.txt
    

これにより、対応するノードの依存関係をインストールできます。

### 

​

依存関係の競合

依存関係の競合は、ComfyUI を使用する際の一般的な問題です。カスタムノードをインストールまたは更新した後、以前インストールしたカスタムノードが ComfyUI のノードライブラリに見つからなくなったり、エラーポップアップが表示されたりすることがあります。考えられる理由の 1 つは依存関係の競合です。 依存関係の競合には多くの原因があり得ます。例えば：

  1. カスタムノードのバージョン固定

一部のプラグインは、依存関係ライブラリの正確なバージョンを固定する場合があります（例：`open_clip_torch==2.26.1`）。一方、他のプラグインはより高いバージョンを要求する場合があります（例：`open_clip_torch>=2.29.0`）。これにより、両方のバージョン要件を同時に満たすことが不可能になります。 **解決策** ：固定バージョンの依存関係を範囲制約（例：`open_clip_torch>=2.26.1`）に変更し、依存関係を再インストールすることで、これらの問題を解決できる場合があります。

  2. 環境汚染

カスタムノードの依存関係をインストールする过程中、他のプラグインによってすでにインストールされているライブラリのバージョンを上書きしてしまう可能性があります。例えば、複数のプラグインが `PyTorch` に依存しているが、異なる CUDA バージョンを要求する場合、後からインストールされたプラグインが既存の環境を壊すことがあります。 **解決策** ：

  * Python 仮想環境で特定のバージョンの依存関係を手動でインストールすることで、これらの問題を解決できる場合があります。
  * または、これらの問題を解決するために、異なるプラグインのために異なる Python 仮想環境を作成します。
  * プラグインを 1 つずつインストールし、各プラグインのインストール後に ComfyUI を再起動して、依存関係の競合が発生するか観察してみてください。


  3. カスタムノードの依存関係バージョンが ComfyUI の依存関係バージョンと互換性がない

これらのタイプの依存関係の競合は解決がより困難な場合があり、ComfyUI をアップグレード/ダウングレードするか、カスタムノードの依存関係バージョンを変更して、これらの問題を解決する必要があるかもしれません。 **解決策** ：これらのタイプの依存関係の競合は解決がより困難な場合があり、ComfyUI をアップグレード/ダウングレードするか、カスタムノードの依存関係バージョンを変更して、これらの問題を解決する必要があるかもしれません。

## 

​

モデル

モデルは ComfyUI にとって重要なアセット依存関係です。様々なカスタムノードやワークフローは、Stable Diffusion シリーズ、Flux シリーズ、Ltxv など、特定のモデルを中心に構築されています。 これらのモデルは ComfyUI での創作に不可欠な基盤であるため、使用するモデルが適切に利用可能であることを確認する必要があります。通常、モデルは `ComfyUI/models/` 下の対応するディレクトリに保存されます。もちろん、テンプレートを修正して [extra_model_paths.yaml](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example) を作成し、追加のモデルパスを ComfyUI に認識させることもできます。 これにより、複数の ComfyUI インスタンスが同じモデルライブラリを共有でき、ディスク使用量を削減できます。

## 

​

ソフトウェア

ComfyUI のような高度なアプリケーションには、 _**ソフトウェア依存関係**_ もあります。これらは、アプリケーションの実行に必要なプログラミングコードとデータのライブラリです。カスタムノードはソフトウェア依存関係の例です。さらに根本的なレベルでは、Python プログラミング環境が ComfyUI の究極の依存関係です。特定のバージョンの ComfyUI を実行するには、正しいバージョンの Python が必要です。Python、ComfyUI、カスタムノードの更新はすべて、**ComfyUI Manager** ウィンドウから処理できます。 ![ComfyUI カスタムノードマネージャー](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_dependecies_custom-nodes-manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=835aa06ad002a4231415f525c0a88b7c)

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/basic-concepts/dependencies.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/basic-concepts/dependencies)

[ComfyUI モデル：ファイル、フォルダ、ローダーノード前へ](https://docs.comfy.org/ja/basic-concepts/models)[インターフェース概要次へ](https://docs.comfy.org/ja/interface/overview)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

リソース

[インストール](https://docs.comfy.org/ja/installation/system_requirements)[チュートリアル](https://docs.comfy.org/ja/tutorials/basic/text-to-image)[開発](https://docs.comfy.org/ja/development/overview)

プロダクト

[機能](https://www.comfy.org/?utm_source=docs)[ギャラリー](https://www.comfy.org/gallery?utm_source=docs)[ダウンロード](https://www.comfy.org/download?utm_source=docs)

会社情報

[概要](https://www.comfy.org/about?utm_source=docs)[採用情報](https://www.comfy.org/careers?utm_source=docs)[利用規約](https://www.comfy.org/terms-of-service?utm_source=docs)[プライバシーポリシー](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
