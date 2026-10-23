---
url: https://docs.comfy.org/ja/development/comfy-router/schemas/
title: Comfy Router \u30e2\u30c7\u30eb\u30b9\u30ad\u30fc\u30de\u3068\u7d50\u679c - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:54.235159+00:00
---

# Comfy Router モデルスキーマと結果 - ComfyUI

> Source: https://docs.comfy.org/ja/development/comfy-router/schemas/

## このページの内容

  * 入力スキーマと出力スキーマを読み取る
    * スキーマをキャッシュする
  * 検証とフォールバックスキーマ
  * 結果を読み取る
  * 次のステップ



Comfy Router

# Comfy Router モデルスキーマと結果

ページをコピーページをコピー

Router モデルの OpenAPI 入力スキーマと出力スキーマを取得し、ETag でキャッシュし、モデルのネイティブな結果形状を読み取ります。

ページをコピーページをコピー

各 Router モデルは独自のネイティブなリクエストボディを受け付け、独自のネイティブな結果を返します。両方を知るには、モデルのスキーマを読み取ります。

## 

​

入力スキーマと出力スキーマを読み取る

各モデルは単体の OpenAPI ドキュメントを公開しています。
    
    
    curl --dump-header schema-headers.txt \
      -H "X-API-Key: $COMFY_API_KEY" \
      https://api.comfy.org/v2/models/bfl/flux-2-pro/openapi.json
    

モデルのオペレーション内では、`requestBody` が入力を記述し、出力スキーマが作成されている場合は `200` レスポンスが出力を記述します。入力の検証と出力のドキュメント化は別物です。Router は入力スキーマに対して検証を行いますが、返されたプロバイダーの結果をその出力スキーマに対して検証することはありません。 出力のメディアタイプとそのフィールドも確認してください。作成されていない出力は `*/*` を使用することがあり、一部のモデルは JSON ではなくバイナリデータを返します。

### 

​

スキーマをキャッシュする

スキーマとその `ETag` を保存します。後でスキーマを取得する際に、その ETag を `If-None-Match` に渡します。`304` にはボディがありません。キャッシュしたドキュメントを保持してください。`200` は置き換え用のドキュメントと ETag を提供します。
    
    
    curl -H "X-API-Key: $COMFY_API_KEY" \
      -H 'If-None-Match: "previous-etag-value"' \
      https://api.comfy.org/v2/models/bfl/flux-2-pro/openapi.json
    

スキーマルートは `Cache-Control: private, must-revalidate` を使用します。認証済みのレスポンスは共有キャッシュに保存しないでください。この ETag/304 の動作はスキーマエンドポイントにのみ適用されます。

## 

​

検証とフォールバックスキーマ

作成済みの入力スキーマは、プロバイダーの呼び出し前に `422` と `detail[]` 配列で無効なフィールドを拒否します。`loc` のフィールドパスを読み取ってください。詳しくは[検証エラー](https://docs.comfy.org/ja/development/comfy-router/errors#%E6%A4%9C%E8%A8%BC%E3%82%A8%E3%83%A9%E3%83%BC)を参照してください。 一部のスキーマは任意の JSON オブジェクトを受け付け、`x-comfy-input-schema-authored: false` を設定します。Router はそれらのリクエストをモデル固有の検証なしで転送するため、プロバイダーがそれらを拒否する可能性があります。

## 

​

結果を読み取る

Router は各モデルのターミナルな結果形状を返します。共通の画像、ビデオ、テキストのエンベロープはありません。BFL の画像出力は `result.sample` を使用し、他のモデルは URL リストやインラインバイトを返すことがあります。 一部のアセット URL は Comfy によって再ホストされますが、それ以外はプロバイダーの URL やインラインバイトのままです。[結果アセット](https://docs.comfy.org/ja/development/comfy-router/reference#%E7%B5%90%E6%9E%9C%E3%82%A2%E3%82%BB%E3%83%83%E3%83%88)を確認し、有効期限が切れるアセットは速やかにダウンロードしてください。リプレイでは URL は更新されません。

## 

​

次のステップ

  * [キュー中のリクエスト](https://docs.comfy.org/ja/development/comfy-router/queue): 実行を送信し、後で結果を収集します。
  * [エラーと再試行](https://docs.comfy.org/ja/development/comfy-router/errors): 二重に支払うことなく失敗を処理します。



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/comfy-router/schemas.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/comfy-router/schemas)

[Comfy Router モデルを検出する前へ](https://docs.comfy.org/ja/development/comfy-router/discover-models)[Comfy Router リクエストのキューイング次へ](https://docs.comfy.org/ja/development/comfy-router/queue)

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
