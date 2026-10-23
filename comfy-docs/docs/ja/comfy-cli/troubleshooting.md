---
url: https://docs.comfy.org/ja/comfy-cli/troubleshooting/
title: Comfy CLI \u30c8\u30e9\u30d6\u30eb\u30b7\u30e5\u30fc\u30c6\u30a3\u30f3\u30b0\u30ac\u30a4\u30c9 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:56.715588+00:00
---

# Comfy CLI トラブルシューティングガイド - ComfyUI

> Source: https://docs.comfy.org/ja/comfy-cli/troubleshooting/

## このページの内容

  * 前提条件
  * 仮想環境に ComfyUI をインストールする
  * GPU に合った PyTorch ビルドをインストールする
  * ブラウザなしで Comfy Cloud を設定する
  * さらにサポートが必要な場合



Comfy CLI

# Comfy CLI トラブルシューティングガイド

ページをコピーページをコピー

Comfy CLI でよくあるセットアップの問題を解決します：git の不足、Python と仮想環境の要件、ブラウザなしでの Comfy Cloud 認証、GPU ライブラリのインストール。

ページをコピーページをコピー

Comfy CLI のほとんどの問題は、前提条件の不足かセットアップ手順の抜けが原因です。問題を報告する前に、以下を順に確認してください。

## 

​

前提条件

Comfy CLI を使用するには、システムに [git](https://git-scm.com/downloads) がインストールされている必要があります。先に git をインストールすると、`comfy install` と `comfy update` が ComfyUI とカスタムノードをクローンできます。

## 

​

仮想環境に ComfyUI をインストールする

`comfy install` は有効な Python 環境に ComfyUI をインストールします。Python 3.10 以降が必要です。先に仮想環境を作成して有効化してください：
    
    
    python3 -m venv comfy-env
    source comfy-env/bin/activate
    comfy install
    

## 

​

GPU に合った PyTorch ビルドをインストールする

`comfy install` は使用する GPU を尋ね、それに合った PyTorch ビルドをインストールします。プロンプトに答えるか、フラグで GPU を指定して無人で実行してください：

プラットフォーム| `comfy install` がインストールするもの| 別途必要なもの  
---|---|---  
NVIDIA| CUDA runtime 付き PyTorch（pip ホイール）| 最新の GPU ドライバ（フルの CUDA Toolkit は不要）  
AMD Linux| ROCm PyTorch ホイール| それらのホイールに対応する ROCm 対応 AMD ドライバ／スタック  
AMD Windows| `torch-directml`| 互換 AMD GPU（DirectML。ROCm ではない）  
Apple silicon| PyTorch nightly ホイール（CPU インデックス；Metal/MPS）| Apple silicon 上の macOS  
Intel Arc| PyTorch XPU ホイール| 互換 Intel Arc GPU / XPU スタック  
CPU| CPU 向け PyTorch ホイール| 独立 GPU は不要  
      
    
    comfy install --nvidia
    

PyTorch を自分でインストールする場合は `--skip-torch-or-directml` を指定してください。`comfy env` は ComfyUI が使用する Python 環境とワークスペースを表示します。

## 

​

ブラウザなしで Comfy Cloud を設定する

`comfy setup` はブラウザ経由でサインインするため、CI、devcontainer、ヘッドレスサーバーでは完了できません。代わりに API キーを渡し、非対話モードで実行してください：
    
    
    comfy setup --where cloud --api-key comfyui-... --non-interactive
    

## 

​

さらにサポートが必要な場合

  * [Comfy CLI をはじめよう](https://docs.comfy.org/ja/comfy-cli/getting-started) では、インストール、ルーティング、生成を説明しています。
  * [Comfy CLI コマンドリファレンス](https://docs.comfy.org/ja/comfy-cli/reference) にはすべてのコマンドとフラグが掲載されています。
  * 再現可能な CLI の不具合は [comfy-cli リポジトリ](https://github.com/Comfy-Org/comfy-cli/issues) で報告してください。



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/comfy-cli/troubleshooting.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/comfy-cli/troubleshooting)

[Comfy CLI コマンドリファレンス前へ](https://docs.comfy.org/ja/comfy-cli/reference)[ワークフロー JSON次へ](https://docs.comfy.org/ja/specs/workflow_json)

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
