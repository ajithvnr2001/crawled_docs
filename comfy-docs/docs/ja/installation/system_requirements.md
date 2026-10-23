---
url: https://docs.comfy.org/ja/installation/system_requirements/
title: \u30b7\u30b9\u30c6\u30e0\u8981\u4ef6 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:36.715475+00:00
---

# システム要件 - ComfyUI

> Source: https://docs.comfy.org/ja/installation/system_requirements/

## このページの内容

  * サポートされているオペレーティングシステム
  * Python バージョン
  * ブラウザ要件
  * サポートされているハードウェア
  * 依存関係
  * よくある質問



ローカル (セルフホステッド)

# システム要件

ページをコピーページをコピー

ComfyUIをインストールして実行するためのハードウェアとソフトウェアの要件

ページをコピーページをコピー

このガイドでは、ComfyUI をインストールするためのシステム要件について紹介します。ComfyUI は頻繁に更新されるため、このドキュメントは適時に更新されない場合があります。詳細については、[ComfyUI](https://github.com/Comfy-Org/ComfyUI) の関連説明を参照してください。 どのバージョンの ComfyUI を使用する場合でも、それは独立した Python 環境で実行されます。

### 

​

サポートされているオペレーティングシステム

現在、以下のオペレーティングシステムをサポートしています：

  * Windows
  * Linux
  * macOS（M シリーズなどの Apple Silicon をサポート）

お使いのOSとセットアップに合わせたインストール手順については、以下のリンクをご覧ください。

Comfy デスクトップ版

Comfy Desktop は **Windows** 、**macOS（Apple Silicon）** 、**Linux** （AppImage と `.deb`）でのスタンドアロンインストールに対応しています。

  * ソースは [GitHub](https://github.com/Comfy-Org/Comfy-Desktop) にあります



Desktop インストールはデフォルトで ComfyUI の **安定版** を追跡します。常に最新のコミットが必要な場合は、ポータブル版か手動 git インストールを使うか、インスタンスの更新チャネルを **Latest on GitHub** に切り替えてください。

以下から、お使いのシステムとハードウェアに合ったインストールを選んでください

  * Windows

  * macOS (Apple Silicon)

  * Linux




## Comfy Desktop（Windows）インストールガイド

**Windows** 10 以降向け。NVIDIA または AMD GPU を推奨。

## Comfy Desktop（macOS）インストールガイド

**Apple Silicon** 搭載の macOS 向け

## Comfy Desktop（Linux）インストールガイド

AppImage または `.deb` をインストールするか、ソースからビルドして実行します。

ComfyUI ポータブル版（Windows）

ポータブル版は、独立した埋め込み型 Python 環境を統合した ComfyUI のバージョンです。このバージョンを利用することで、最新の機能をいち早く体験できます。現在は **Windows** システムのみをサポートしています。

## ComfyUI ポータブル版（Windows）インストールガイド

**NVIDIA GPU** または **CPU 専用環境** で動作する **Windows** 向け ComfyUI バージョンをサポート。常に最新のコミットを反映し、完全にポータブルです。

手動インストール

## ComfyUI 手動インストールガイド

すべての OS（Windows/macOS/Linux）および GPU（NVIDIA、AMD、Intel、Apple Silicon、Ascend NPU、Cambricon MLU）に対応しています。

### 

​

Python バージョン

  * **Python 3.13** は非常に良くサポートされており、推奨されます
  * Python 3.14 は動作しますが、一部のカスタムノードで問題が発生する可能性があります。フリースレッド版は動作しますが、一部の依存関係で GIL が有効になるため、完全にサポートされているわけではありません
  * 3.13 で一部のカスタムノードの依存関係に問題がある場合、Python 3.12 は良いフォールバックオプションです



### 

​

ブラウザ要件

最適な体験を得るためには、**Google Chrome バージョン 143 以降** を使用してください。Chrome の以前のバージョン（142 以下）には、ComfyUI で視覚的な不具合やパフォーマンス問題を引き起こす既知の問題があります。

### 

​

サポートされているハードウェア

  * **NVIDIA GPU** \- CUDA 13.0 で安定版 PyTorch をインストールします：`pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130`
  * **AMD GPU (Linux)** \- ROCm 7.2 安定版または nightly 版
  * **AMD GPU (Windows)** \- AMD のマルチアーキテクチャ PyTorch パッケージによる ROCm 10.0。RDNA 2、RDNA 3、RDNA 3.5、RDNA 4 をサポートし、別途 HIP SDK のインストールは不要です
  * **Intel GPU** \- ネイティブ PyTorch torch.xpu サポートを備えた Arc シリーズ
  * **Apple Silicon** \- Metal 加速を備えた M1/M2/M3/M4 シリーズ
  * **Ascend NPU** \- torch_npu 拡張機能経由
  * **Cambricon MLU** \- torch_mlu 拡張機能経由
  * **Iluvatar Corex** \- Iluvatar Extension for PyTorch 経由
  * **CPU** \- `--cpu` パラメータを使用します（低速）

詳細なインストール手順については、[ComfyUI Windows および Linux 手動インストールセクション](https://github.com/Comfy-Org/ComfyUI?tab=readme-ov-file#manual-install-windows-linux) を参照してください。

PyTorch 2.7 以上がサポートされていますが、新しいバージョンの使用を強く推奨します。Nvidia 20 シリーズ以上の GPU では cu130 以上の PyTorch が必要です。一部の機能と最適化は新しいバージョンでのみ動作する可能性があります。通常、最新バージョンの公開から 2 週間以内でない限り、最新メジャーバージョンの PyTorch と最新 CUDA バージョンの使用を推奨します。Windows ポータブル版には現在、Python 3.13 と PyTorch CUDA 13.0 が付属しています。起動しない場合は、Nvidia ドライバーを更新してください。

### 

​

依存関係

  * PyTorch をインストールします（ハードウェアに固有のバージョン）
  * ComfyUI の requirements.txt にあるすべての依存関係をインストールします：`pip install -r requirements.txt`



## 手動インストール

詳細なインストール手順については、手動インストールセクションを参照してください。

## 

​

よくある質問

ComfyUIはMLX（Appleの機械学習フレームワーク）をサポートしていますか？

ComfyUIはMLXを直接使用しません。Apple Silicon（M1/M2/M3/M4）Macでは、PyTorchの **MPS（Metal Performance Shaders）** バックエンドを使用して、AppleのMetalグラフィックスフレームワークによるGPUアクセラレーションを活用します。MLXはApple Silicon向けに設計された独立した機械学習配列フレームワークです。ComfyUIのPyTorchベースのアーキテクチャでは、代わりにMPSを使用しています。お使いのMacでMPSが動作していることを確認するには：
    
    
    python -c "import torch; print(torch.backends.mps.is_available())"
    

**Docker：** ComfyUI は公式の Docker イメージを提供していません。コンテナで ComfyUI を実行したい場合は、[Docker Hub](https://hub.docker.com/search?q=comfyui) にあるコミュニティがメンテナンスするイメージを利用できます。これらのイメージは **Comfy-Org が公式にメンテナンスしているものではなく** 、ComfyUI チームによるサポートもありません。自己責任でご利用ください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/installation/system_requirements.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/installation/system_requirements)

[ComfyUI 公式ドキュメント前へ](https://docs.comfy.org/ja)[Comfy Desktop 概要次へ](https://docs.comfy.org/ja/installation/desktop/overview)

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
