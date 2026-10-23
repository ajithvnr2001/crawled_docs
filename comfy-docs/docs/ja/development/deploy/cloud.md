---
url: https://docs.comfy.org/ja/development/deploy/cloud/
title: Comfy Cloud \u30af\u30a4\u30c3\u30af\u30b9\u30bf\u30fc\u30c8 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:45.161719+00:00
---

# Comfy Cloud クイックスタート - ComfyUI

> Source: https://docs.comfy.org/ja/development/deploy/cloud/

## このページの内容

  * クイックスタート
  * 次のステップ



Comfy で開発する

# Comfy Cloud クイックスタート

ページをコピーページをコピー

有料のサブスクリプション、APIキー、Comfy SDK を使って、Comfy Cloud 上で API 形式のワークフローを実行します。

ページをコピーページをコピー

Comfy Cloud は、フルマネージドで常時利用可能な ComfyUI 環境です。ブラウザでワークフローを構築することも、SDK から実行することもできます。作成が必要な Build やデプロイメントはありません。

Comfy Cloud を初めて使う場合は、[Comfy Cloud の紹介](https://docs.comfy.org/ja/get_started/cloud) から始めてください。このクイックスタートでは、アプリからワークフローを実行する方法を説明します。

## 

​

クイックスタート

有料のサブスクリプション、[APIキー](https://docs.comfy.org/ja/development/api-development/getting-an-api-key)、API 形式のワークフローが必要です。[Comfy SDK](https://docs.comfy.org/ja/development/api-development/sdks) はデフォルトで Cloud をターゲットにします。

1

APIキーを作成

[platform.comfy.org](https://platform.comfy.org) で APIキーを作成します。詳細は [APIキーの取得](https://docs.comfy.org/ja/development/api-development/getting-an-api-key) を参照してください。

2

SDKをインストール

Python

TypeScript
    
    
    pip install comfy-sdk
    
    
    
    npm i @comfyorg/sdk
    

3

ワークフローをAPI形式でエクスポート

クラウドエディタで、テスト済みのワークフローを `File → Export Workflow (API)` で `workflow_api.json` として保存します。詳細は [ワークフローAPI形式](https://docs.comfy.org/ja/development/api-development/workflow-api-format) を参照してください。

4

実行する

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    client = Comfy(api_key="comfyui-...")  # Comfy Cloud がデフォルトのターゲットです
    
    wf = client.workflows.from_file("workflow_api.json")
    
    job = client.run(wf)
    for output in job.get_outputs("9"):
        output.to_file(output.name)
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    const client = new Comfy({ apiKey: "comfyui-..." }); // Comfy Cloud がデフォルトのターゲットです
    
    const wf = await client.workflows.fromFile("workflow_api.json");
    
    const job = await client.run(wf);
    await job.getOutputs("9")[0].toFile("out.png");
    

`"9"` は出力ノードのIDです。入力、進捗、エラー処理については [SDKガイド](https://docs.comfy.org/ja/development/api-development/sdks) を参照してください。

同じ SDK のコードで、[Comfy API デプロイメント](https://docs.comfy.org/ja/development/serverless/quickstart) と [セルフホストの ComfyUI](https://docs.comfy.org/ja/development/deploy/self-hosting) をターゲットにすることもできます。詳しくは [ワークフローの実行](https://docs.comfy.org/ja/development/run-workflows/overview) を参照してください。

## 

​

次のステップ

## 使用量と制限

Cloud のクレジットと同時実行ジョブの仕組みを確認します。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/deploy/cloud.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/deploy/cloud)

[ComfyUI のデプロイ前へ](https://docs.comfy.org/ja/development/deploy/overview)[Comfy API と Router のサンプル次へ](https://docs.comfy.org/ja/development/examples)

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
