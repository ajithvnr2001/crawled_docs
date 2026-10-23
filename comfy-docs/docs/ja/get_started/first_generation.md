---
url: https://docs.comfy.org/ja/get_started/first_generation/
title: AI\u753b\u50cf\u751f\u6210\u306e\u59cb\u3081\u65b9 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:21.791891+00:00
---

# AI画像生成の始め方 - ComfyUI

> Source: https://docs.comfy.org/ja/get_started/first_generation/

## このページの内容

  * テキストから画像への生成（Text-to-Image）について
  * ComfyUIにおけるText-to-Imageワークフローチュートリアル
    * 1\. ComfyUIの起動
    * 2\. デフォルトのText-to-Imageワークフローの読み込み
    * 3\. モデルのインストール
    * 4\. モデルの読み込みと初めての画像生成
  * トラブルシューティング
    * モデルの読み込みに関する問題



はじめに

# AI画像生成の始め方

ページをコピーページをコピー

ComfyUI で最初の AI 画像を生成しましょう。サンプルワークフローの読み込み、モデルのインストール、初めてのテキストから画像への生成を解説します。

ページをコピーページをコピー

このガイドは、ご自身のデバイスにComfyUIをインストールして利用する**ローカルユーザー** 向けの内容です。ローカルインストールを行いたくない場合は、公式のクラウドサービスをご利用いただけます。

## Comfy Cloudを試す

インストール不要でComfyUIをクラウド上で実行できます。Googleアカウントでログインすると、**毎月400クレジット** が無料で付与されます。

本ガイドでは、ComfyUIの基本操作を理解し、初めての画像生成を完了することを目的としています。以下をカバーします：

  1. 例として提供されるワークフローの読み込み 
     * ComfyUIのワークフローテンプレートからの読み込み
     * ワークフロー情報を含むメタデータ付き画像からの読み込み
  2. モデルのインストールに関するガイダンス 
     * 自動モデルインストール
     * 手動モデルインストール
  3. 最初のテキストから画像への生成（Text-to-Image）の実行



## 

​

テキストから画像への生成（Text-to-Image）について

テキストから画像への生成（Text-to-Image）は、テキストによる説明に基づいて画像を生成するAI描画の基本機能であり、AIアート生成において最も一般的に使用される機能の一つです。これは、要件（ポジティブプロンプトおよびネガティブプロンプト）を「画家（描画モデル）」に伝える作業と捉えることができます。その「画家」が、あなたの指示通りに画像を作成します。Text-to-Imageの詳細な解説については、[Text to Image](https://docs.comfy.org/ja/tutorials/basic/text-to-image)章で取り上げます。

## 

​

ComfyUIにおけるText-to-Imageワークフローチュートリアル

### 

​

1\. ComfyUIの起動

ComfyUIを起動し、正常にComfyUIのインターフェースにアクセスできることを確認してください。そのためには、まず[インストールガイド](https://docs.comfy.org/ja/installation/system_requirements)に従ってセットアップを完了しておく必要があります。あるいは、インストール不要でComfyUIを利用できる[Comfy Cloud](https://docs.comfy.org/ja/get_started/cloud)もご利用いただけます。 ![ComfyUIインターフェース](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/desktop/comfyui-interface.jpg?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=5fc5c0932897a4ab0076db79fec7b4ea) まだComfyUIをインストールしていない場合は、お使いのデバイスに合ったバージョンを選んでインストールしてください。

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

2\. デフォルトのText-to-Imageワークフローの読み込み

ComfyUIは通常、起動時にデフォルトのText-to-Imageワークフローを自動的に読み込みます。ただし、ComfyUIの基本操作に慣れるために、以下の異なる方法でワークフローを読み込んでみることもおすすめします：

  * メタデータ付き画像から読み込む

  * workflow.jsonファイルから読み込む




ComfyUIで生成されたすべての画像には、ワークフロー情報が含まれるメタデータが埋め込まれています。このメタデータを利用してワークフローを読み込むことができます：

  * ComfyUIで生成された画像をインターフェースにドラッグ＆ドロップする
  * メニューの **Workflows** → **Open** を使って画像を開く

以下のサンプル画像を使ってワークフローの読み込みを試してみてください： ![ComfyUI - Text to Imageワークフロー](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/text-to-image-workflow.png)

ComfyUIのワークフローはJSON形式で保存できます。ワークフローを完成させた後は、メニューの **Workflows** → **Export** を使ってエクスポートし、JSONファイルとして保存できます。以下のボタンをクリックして、GitHubからサンプルのworkflow.jsonファイルをダウンロードしてみてください：[text-to-image.jsonをダウンロード](https://github.com/Comfy-Org/docs/blob/main/public/text-to-image.json)ダウンロードが完了したら、メニューの **Workflows** → **Open** を使ってこのJSONファイルを読み込みます。

### 

​

3\. モデルのインストール

ほとんどのComfyUIインストールでは、初期状態でベースモデルは含まれていません。ワークフローを読み込んだ後、[v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) モデルがインストールされていない場合、次のようなメッセージが表示されます： まず、ComfyUIからモデルが不足しているという警告が表示されます： ![不足しているモデルの警告](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/missing_model_warning_1.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=0587d7f045f981756c232644569b3b59) 警告をクリックすると、不足しているモデルとダウンロードリンクが表示されます： ![不足しているモデルの詳細](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/missing_model_warning_2.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=bf61da1c5711d935b7d49dd7e236f275) デフォルトでは、モデルは `<あなたのComfyUIインストール先>/ComfyUI/models/` ディレクトリ内に保存され、`checkpoints`、`embeddings`、`vae`、`lora`、`upscale_model` などのサブディレクトリに分類されます。ComfyUIは起動時にこれらのディレクトリおよび `extra_model_paths.yaml` で設定されたパス内のモデルを検出します。

  * Comfyデスクトップ版（モデルフォルダーの探し方）

  * ComfyUIポータブル版（モデルフォルダーの探し方）




デスクトップアプリ上部のカプセルメニューをクリックし、**Storage** タブを開いてモデルディレクトリを確認します。カプセルメニューはデスクトップアプリにのみ存在し、ブラウザーで実行している ComfyUI にはありません。ディレクトリ横のフォルダーアイコンをクリックすると、ファイルマネージャーで開けます。![Comfy Desktop カプセルメニュー: モデルディレクトリ設定を表示する Storage タブ](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)

ポータブル版の場合、モデルフォルダーは通常次の場所にあります：`ComfyUI_windows_portable/ComfyUI/models/`

モデルのインストール方法は以下の通りです：

  * 自動ダウンロード

  * 手動インストール




**Download** ボタンをクリックすると、ComfyUIがダウンロードを実行します。使用中のバージョンによって動作が異なります。

  * Comfyデスクトップ版

  * ComfyUIポータブル版




デスクトップ版では、モデルのダウンロードが自動的に完了し、`<あなたのComfyUIインストール先>/ComfyUI/models/checkpoints` ディレクトリに保存されます。  
インストールが完了するまで待つか、サイドバーのモデルパネルで進捗状況を確認できます。![モデルダウンロードの進捗](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/desktop_download_status.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=a1573451803b46539fca14c1b1ef4dd2)

自動ダウンロードは通常 **Hugging Face** からモデルを取得します。Hugging Face に安定してアクセスできるネットワーク環境になっているか確認してください。ダウンロードが**開始されない** 、または**長時間進捗が見られない** 場合は、不足モデル詳細に表示されているリンクをコピーするか、このページの **手動インストール** を使ってモデルを手動で配置してください。

ブラウザがファイルのダウンロードを実行します。ダウンロード完了後、ファイルを `<あなたのComfyUIインストール先>/ComfyUI_windows_portable/ComfyUI/models/checkpoints` ディレクトリに保存してください。

[v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) のページにアクセスし、以下の手順に従ってダウンロードしてください：![Hugging Faceでのモデルダウンロード](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=15c2560c44e7e4276b6a351809f7bf9f)ダウンロードしたファイルを以下の場所に保存します：

  * Comfyデスクトップ版

  * ComfyUIポータブル版




`<あなたのComfyUIインストール先>/ComfyUI/models/checkpoints` に保存します![Comfyデスクトップ版のモデル保存先](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=275add7233b1f048455cff0f162847b9)

`ComfyUI_windows_portable/ComfyUI/models/checkpoints` に保存します![ComfyUIポータブル版のモデル保存先](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=48976b87bcfdba962b119d901c43b286)

保存後に、ComfyUIを再読み込みまたは再起動してください。

### 

​

4\. モデルの読み込みと初めての画像生成

モデルをインストールまたは更新した後は、キーボードの **`R`** キーを押してオブジェクト定義を更新し、ノード側のモデル一覧（例：**Load Checkpoint** のドロップダウン）をリフレッシュできます。そのうえで、次の手順に進みます： ![ワークフローの実行](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/run_workflow.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=d8cb64b219e93cfd903723255d5e7d11)

  1. **Load Checkpoint** ノードで、**v1-5-pruned-emaonly-fp16.safetensors** が選択されていることを確認します
  2. `Run`ボタンをクリックするか、`Ctrl + Enter`キーを押して生成を開始します

結果は**Save Image** ノードに表示されます。右クリックしてローカルに保存できます。 ![ComfyUIによる初めての画像生成結果](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/result.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=dd253cd626d72716f52322245c5526cc) テキストから画像への生成の詳細な手順については、以下の包括的なガイドをご覧ください：

## ComfyUI Text-to-Imageワークフローガイド

詳細なText-to-Imageワークフロー手順はこちらをクリック

## 

​

トラブルシューティング

### 

​

モデルの読み込みに関する問題

`Load Checkpoint`ノードにモデルが表示されない、または「null」と表示される場合は、モデルのインストール先が正しいか確認し、ComfyUIを再読み込みまたは再起動してみてください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/get_started/first_generation.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/get_started/first_generation)

[ComfyUI Manager トラブルシューティング前へ](https://docs.comfy.org/ja/manager/troubleshooting)[ComfyUI エージェントツール：MCP、CLI、内蔵エージェント次へ](https://docs.comfy.org/ja/agent-tools)

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
