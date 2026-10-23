---
url: https://docs.comfy.org/ja/get_started/cloud/
title: Comfy Cloud - RTX 6000 Pro \u3092\u642d\u8f09\u3057\u305f\u516c\u5f0f ComfyUI \u30af\u30e9\u30a6\u30c9\u30d7\u30e9\u30c3\u30c8\u30d5\u30a9\u30fc\u30e0 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:21.201186+00:00
---

# Comfy Cloud - RTX 6000 Pro を搭載した公式 ComfyUI クラウドプラットフォーム - ComfyUI

> Source: https://docs.comfy.org/ja/get_started/cloud/

## このページの内容

  * Comfy Cloud とは？
    * 主な機能
  * クラウド版 vs ローカル版
  * 料金とサブスクリプション
  * Comfy Cloud ファイアウォールのホワイトリスト
  * ComfyUI Cloud の使い方
  * フィードバック
    * Comfy Cloudの停止/終了方法
  * よくある質問
  * 次のステップ



はじめに

# Comfy Cloud - RTX 6000 Pro を搭載した公式 ComfyUI クラウドプラットフォーム

ページをコピーページをコピー

Comfy Cloud を使用して ComfyUI ワークフローをオンラインで実行。NVIDIA RTX 6000 Pro GPU を搭載した公式クラウドプラットフォームです。ローカルインストールは不要です。

ページをコピーページをコピー

## Comfy Cloud にアクセス

こちらをクリックして ComfyUI Cloud に直接アクセスしてください

## 

​

Comfy Cloud とは？

ComfyUI Cloud は、ローカルバージョンと同じ機能を備えた ComfyUI のクラウドバージョンです。すべてプリインストールされており、すぐに使用できます。

### 

​

主な機能

## 設定不要

インストールは不要です。すべてのモデルとカスタムノードがプリインストールされており、すぐに使用できます

## 強力な GPU

自前のハードウェアがなくても、強力なサーバー GPU でワークフローを高速実行できます

## 常に最新

最新の ComfyUI リリースと機能に自動的に更新されます

## どこからでもアクセス

インターネット接続のある任意のデバイスから ComfyUI を使用できます。ローカルインストールは不要です

## チームでの共同作業

チームワークスペースを作成して、チームメンバーと共同作業できます。サブスクリプション プラン、クレジット、ワークフローを共有できます。

## 

​

クラウド版 vs ローカル版

ComfyUI には、公式クラウドバージョンである [Comfy Cloud](https://comfy.org/cloud) と、オープンソースのセルフホストバージョンの両方があります。強力な GPU をお持ちの場合、ComfyUI をローカルで実行するのは素晴らしい選択肢です。一方、クラウドバージョンはすぐに使用できるオンラインサービスです。URL を開くだけで、インストールや設定は不要です。

カテゴリ| Comfy Cloud| セルフホスト（ローカル ComfyUI）  
---|---|---  
**コスト**|  無料プランと有料サブスクリプション| 無料  
**GPU**|  強力な Blackwell RTX 6000 Pro| 自前の GPU を用意  
**技術知識**|  技術知識は不要です。| デスクトップ版とポータブル版で簡単に始められますが、カスタムノードのインストールやローカルインストールの問題をトラブルシューティングする必要があります。  
**カスタムノード**|  プリインストール済みのカスタムノードを使用でき、互換性の問題を心配する必要はありません。| 任意のカスタムノードをインストールできますが、自分で管理する必要があります。  
**モデル**|  プリインストール済みのモデルを使用します。Civitai と Hugging Face からモデルをインポートできます。| 任意のモデルを使用できますが、まずダウンロードする必要があります。  
**主な違い**| [Workspaces](https://docs.comfy.org/ja/cloud/workspace) でチームのオンボーディングが容易| オフラインで動作し、無限にカスタマイズ可能  
**はじめる**| [ComfyUI Cloud を実行](https://comfy.org/cloud)| [ComfyUI をローカルにインストール](https://docs.comfy.org/ja/installation/system_requirements)  
  
## 

​

料金とサブスクリプション

## 料金を確認

Comfy Cloud の料金とサブスクリプションオプションを表示

## 

​

Comfy Cloud ファイアウォールのホワイトリスト

TCP 443 で、以下の宛先へのアウトバウンド HTTPS および WebSocket 通信を許可してください：

  * **アプリ：** `cloud.comfy.org`, `api.comfy.org`, `cdn.comfy.org`
  * **アップロードと出力：** `comfy-hub-assets.comfy.org`, `storage.googleapis.com`
  * **サインイン：** `dreamboothy.firebaseapp.com`, `identitytoolkit.googleapis.com`, `securetoken.googleapis.com`, `apis.google.com`, `challenges.cloudflare.com`
  * **その他の機能：** `registry.comfy.org`, `*.algolia.net`, `media.comfy.org`



## 

​

ComfyUI Cloud の使い方

ComfyUI Cloud の使用は、ローカルの ComfyUI を使用するのと基本的に同じです。ComfyUI を初めて使用する場合は、以下のクイックヒントを参考にしてください。

1

テンプレートを選択

左サイドバーのテンプレートアイコンをクリックして、利用可能なワークフローを閲覧してください。![ワークフローテンプレートを開く](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a32875bb4e6d1c92ea4f893831aff925)

2

実行したいワークフローを選択

実行したいテンプレートをクリックしてください。![ワークフローテンプレートを選択](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b16043c4ad9372834eb7fe49c1180eee)

3

テンプレートの入力を更新

  1. 読み込まれたワークフローでは、クラウドバージョンですべてのモデルがプリインストールされているため、すべてのテンプレートは読み込み後すぐに実行準備が整います。
  2. 更新が必要な場合は、画像入力またはテキストプロンプトを提供するだけです。`Load Image` ノードまたは `CLIP Text Encode` ノードを確認してください。 ![入力を確認](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=56ca79d24c79e666146c927263c96e99)



4

ワークフローを実行

すべて正しければ、「Run」アイコンをクリックするか、ショートカット「Ctrl + Enter」を使用してワークフローを実行してください。![ワークフローを実行](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=546f1e0003941deba2006a36d8f9ed34)

5

出力を確認

実行をクリックすると、サービスはワークフロー用にマシンの割り当てを開始します。キューパネルで該当するワークフローの実行ステータスを確認できます。![キューを確認](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=4ac366407cf13fa84e55ef7948cff36e)

6

コンテンツをローカルに保存

ワークフローの実行が完了した後、生成されたコンテンツをローカルに保存できます。アセットの種類に応じて、保存方法は以下の通りです。

  * 画像を保存

  * 動画を保存

  * 音声を保存

  * 3D アセットを保存




キューパネルまたは画像保存ノードで、生成された画像を右クリックし、「Save image」を選択して画像をローカルに保存してください。![画像アセットを保存](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a15e70a3649537fb8c6adc50689dfbe7)

キューパネルまたは動画保存ノードで：

  1. ブラウザプレーヤーコンポーネントの 3 つの点をクリックしてメニューを開きます
  2. 「Download」を選択して動画をローカルに保存してください。 ![動画アセットを保存](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=2c987025c1c25e954a3065775ef5223d)



キューパネルまたは音声保存ノードで：

  1. ブラウザプレーヤーコンポーネントの 3 つの点をクリックしてメニューを開きます
  2. 「Download」を選択して音声ファイルをローカルに保存してください。 ![音声アセットを保存](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8d876d9c3b89b2ae9f1e84ba8b3e9887)



3D ブラウザノードメニューで、「Export」オプションを選択し、保存したいフォーマットを選択すると、3D ファイルがローカルに保存されます。![3D アセットを保存](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5e121107826658a3e1725b8d9840d94b)

## 

​

フィードバック

ご意見、ご提案、または問題がございましたら、「フィードバック」アイコンをクリックするだけです。これにより、フィードバックが直接送信されます。 ![フィードバック](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f1306e3587e441fc9964ffc0f9e4cc73)

### 

​

Comfy Cloudの停止/終了方法

クラウドセッションは GPU が動作している間のみ課金されます。ブラウザのタブを閉じるとセッションは自動的に停止します。通常のブラウザタブと同じように、いつでも閉じて大丈夫です。

## 

​

よくある質問

## FAQ を表示

料金、機能、制限など、Comfy Cloud に関するよくある質問と回答を表示

## 

​

次のステップ

## Cloud API

Cloud API を介してワークフローをプログラム的に実行

## チュートリアル

ComfyUI ワークフローを学ぶためのチュートリアルを探索

## サポート

Discord コミュニティに参加してサポートを受ける

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/get_started/cloud.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/get_started/cloud)

[ComfyUI の更新方法前へ](https://docs.comfy.org/ja/installation/update_comfyui)[ComfyUI でのカスタムノードのインストール方法次へ](https://docs.comfy.org/ja/installation/install_custom_node)

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
