---
url: https://docs.comfy.org/ja/development/run-workflows/overview/
title: \u30ef\u30fc\u30af\u30d5\u30ed\u30fc\u306e\u5b9f\u884c - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:46.608704+00:00
---

# ワークフローの実行 - ComfyUI

> Source: https://docs.comfy.org/ja/development/run-workflows/overview/

## このページの内容

  * まずはこちら: Comfy SDK
  * 何が何に対応するか
  * どのAPIを使うべきか？
  * はじめに
  * 前提条件



ワークフローの実行

# ワークフローの実行

ページをコピーページをコピー

ライブデプロイメントに対して ComfyUI ワークフローを実行する方法、およびどのクライアントがどのデプロイメントで動作するか

ページをコピーページをコピー

ComfyUI を[どこかにデプロイ](https://docs.comfy.org/ja/development/deploy/overview)したら、アプリケーションはそれを対象にワークフローを実行します。ワークフローを送信し、実行を待ち、出力をダウンロードします。このページでは、どのデプロイにどのクライアントを使うべきかを整理します。

## 

​

まずはこちら: Comfy SDK

新規の統合では、公式の **Comfy SDK** （Python と TypeScript）と、それらが呼び出す [Comfy API v2](https://docs.comfy.org/ja/api-reference/v2/overview) を使用してください。同じコードがすべてのデプロイ先で動作し、変わるのはベース URL だけです。

## Comfy SDK

Python または TypeScript でワークフローを送信し、出力をダウンロードするための SDK をインストールします。

## 

​

何が何に対応するか

デプロイメント| Comfy SDK / API v2| 備考  
---|---|---  
**Comfy API デプロイメント**|  はい| APIキーを使用して `COMFY_BASE_URL` を `https://<deployment>.run.comfy.app` に設定します  
**Comfy Cloud**|  はい| デフォルトのベースURL。APIキーと有料サブスクリプションが必要です  
**セルフホスト**|  はい、[API Proxy](https://docs.comfy.org/ja/development/comfyui-server/api-proxy) 経由| ComfyUI と並行して動作する小規模なサービスが v2 API を提供します  
  
セルフホストのインスタンスでは、SDKを完全に使わずに、生の [ComfyUI Server API](https://docs.comfy.org/ja/development/comfyui-server/comms_overview)（REST + WebSocket）を直接利用することもできます。これはキューやノード情報を含むローカル機能のすべてを公開しますが、リリース間での互換性は保証されません。

## 

​

どのAPIを使うべきか？

| Comfy API v2 + SDK| v1 Cloud API| ComfyUI Server API  
---|---|---|---  
**実行場所**|  Comfy API デプロイメント、Comfy Cloud、または API Proxy 経由のセルフホスト| Comfy Cloud のみ| セルフホストのみ  
**互換性**|  バージョン管理されており、v2 内では追加的な変更のみ| 非推奨。予告なく変更される可能性あり| リリース間での保証なし  
**認証**|  Comfy Cloud および Comfy API デプロイメントでは `Authorization: Bearer`。セルフホスト: デフォルトではなし、オプションで静的 bearer トークン| `X-API-Key` ヘッダー（Comfy Cloud アカウント）| なし（ローカル）または Partner Nodes 用の APIキー  
**公式クライアント**|  Python および TypeScript SDK| なし。HTTP 経由で呼び出し| なし。HTTP 経由で呼び出し  
**プロトコル**|  REST + SSE| REST + WebSocket| REST + WebSocket  
**スコープ**|  ワークフローを実行して結果を取得| モデルやアカウントを含む Cloud の全機能| キューやノード情報を含むローカルの全機能  
**最適な用途**|  継続して動作し続けるべき新しい統合| 既存の統合、および v2 がまだカバーしていない Cloud 機能| 完全な制御、自分のインスタンスに対するカスタムツール  
  
いずれも同じワークフロー形式（[APIフォーマット](https://docs.comfy.org/ja/development/api-development/workflow-api-format)）を受け付けるため、ワークフローをローカルで開発・テストし、変更なしで別のデプロイメントに移行できます。

## 

​

はじめに

## Comfy SDKs

Python または TypeScript から、あらゆるデプロイ先に対してワークフローを実行できます。

## セルフホスト用 API プロキシ

自身の ComfyUI の前段で v2 API を提供し、SDK からアクセスできるようにします。

## ワークフロー API フォーマット

API が受け付ける JSON フォーマットでワークフローをエクスポートします。

## ComfyUI サーバー API

セルフホストインスタンスの生の REST および WebSocket API です。

## 

​

前提条件

  * Comfy Cloud、Comfy API デプロイメント、またはパートナーノードを扱うものには [APIキー](https://docs.comfy.org/ja/development/api-development/getting-an-api-key) が必要です。完全にローカルで動かす ComfyUI には不要です。
  * [API形式](https://docs.comfy.org/ja/development/api-development/workflow-api-format) でエクスポートされたワークフロー。



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/run-workflows/overview.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/run-workflows/overview)

[Comfy API と Router のサンプル前へ](https://docs.comfy.org/ja/development/examples)[初めてのワークフローを実行する次へ](https://docs.comfy.org/ja/development/api-development/quickstart)

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
