---
url: https://docs.comfy.org/ja/development/comfyui-server/api-proxy/
title: \u30bb\u30eb\u30d5\u30db\u30b9\u30c8 ComfyUI \u7528\u306e API \u30d7\u30ed\u30ad\u30b7 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:50.205821+00:00
---

# セルフホスト ComfyUI 用の API プロキシ - ComfyUI

> Source: https://docs.comfy.org/ja/development/comfyui-server/api-proxy/

## このページの内容

  * インストールと実行
  * SDK の接続先を設定する
  * 認証
  * 次のステップ



ワークフローの実行

# セルフホスト ComfyUI 用の API プロキシ

ページをコピーページをコピー

公式 SDK からワークフローを実行できるよう、自分の ComfyUI の前段で Comfy API v2 を提供する

ページをコピーページをコピー

[Comfy SDK](https://docs.comfy.org/ja/development/api-development/sdks) は [Comfy API v2](https://docs.comfy.org/ja/api-reference/v2/overview) を使用します。セルフホストの ComfyUI は、インスタンスと並行して動作する小規模なオープンソースサービス [comfy-api-proxy](https://github.com/Comfy-Org/comfy-api-proxy) を通じて v2 を提供します。

## 

​

インストールと実行
    
    
    pip install comfy-api-proxy
    comfy-api-proxy
    

デフォルトでは `127.0.0.1:8188` の ComfyUI をプロキシし、`127.0.0.1:8189` で v2 API を提供します。どちらも変更するには `--comfyui` と `--port` を使用します。 インストール先にモデルファイルをアップロードしたい場合は、`--comfyui-base-dir /path/to/ComfyUI` を付けて実行します。

## 

​

SDK の接続先を設定する

ベース URL を設定し、通常どおりクライアントを構築します:
    
    
    export COMFY_BASE_URL="http://127.0.0.1:8189"
    

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    client = Comfy()
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    const client = new Comfy();
    

[SDK ガイド](https://docs.comfy.org/ja/development/api-development/sdks) の内容はすべて、Comfy Cloud に対する場合と同じように、プロキシに対しても動作します。

## 

​

認証

認証はデフォルトでは必須ではありません。プロキシに静的なベアラートークンが設定されている場合は、そのトークンを SDK の APIキーとして渡します: `Comfy(api_key="...")`。

プロキシはデフォルトではループバックにのみバインドします。ループバックを超えて公開する場合、たとえばレンタル GPU 上の ComfyUI の前段に置く場合は、ベアラートークンを設定するか、認証を行うリバースプロキシを前段に配置してください。

## 

​

次のステップ

  * [Comfy SDK](https://docs.comfy.org/ja/development/api-development/sdks): クライアントガイド
  * [Comfy API v2 リファレンス](https://docs.comfy.org/ja/api-reference/v2/overview): プロキシが提供する HTTP コントラクト
  * [セルフホストのオプション](https://docs.comfy.org/ja/development/deploy/self-hosting): その背後で ComfyUI を実行する場所
  * [設計ノート](https://docs.comfy.org/ja/development/api-development/sdks-design#%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%83%97%E3%83%AD%E3%82%AD%E3%82%B7): プロキシが存在する理由



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/comfyui-server/api-proxy.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/comfyui-server/api-proxy)

[Comfy SDK：ComfyUI 向け Python・TypeScript クライアント前へ](https://docs.comfy.org/ja/development/api-development/sdks)[Comfy API：サーバーレスデプロイ次へ](https://docs.comfy.org/ja/development/serverless/overview)

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
