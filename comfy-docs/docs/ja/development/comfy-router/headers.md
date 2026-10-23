---
url: https://docs.comfy.org/ja/development/comfy-router/headers/
title: Comfy Router \u30d8\u30c3\u30c0\u30fc - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:55.030343+00:00
---

# Comfy Router ヘッダー - ComfyUI

> Source: https://docs.comfy.org/ja/development/comfy-router/headers/

## このページの内容

  * リクエストヘッダー
  * レスポンスヘッダー
  * 2つの意味を持つステータスコード
  * 次のステップ



Comfy Router

# Comfy Router ヘッダー

ページをコピーページをコピー

Comfy Router に送信できるリクエストヘッダーと、すべてのモデルで返されるレスポンスヘッダーについて説明します。認証、冪等性、リクエスト ID、エラーバケット、リトライのペーシング、支出上限を取り扱います。

ページをコピーページをコピー

すべての Router モデルは、それぞれ独自の JSON ボディを持つ `POST /v2/models/{provider}/{model}` を使用します。このページでは、モデル間で共通のヘッダーについて説明します。[API リファレンス](https://docs.comfy.org/ja/development/comfy-router/reference)には生成済みのコントラクトが記載されています。 Comfy SDK（Python 用の `comfy-sdk`、TypeScript 用の `@comfyorg/sdk`）は認証を処理し、冪等性キーを生成します。以下で説明するように、選択済みのレスポンスメタデータを公開します。生の HTTP クライアントは、ヘッダーを自身で送信し、読み取る必要があります。

## 

​

リクエストヘッダー

​

X-API-Key

string

[Comfy ワークスペース](https://platform.comfy.org/profile/api-keys?onboarding=router)で作成した Comfy APIキー（`comfyui-...`）です。ワークスペースのモデルアクセスとクレジット残高を使用します。`Authorization: Bearer comfyui-...` として送信することもできます。両方のヘッダーが存在する場合は `X-API-Key` が優先されます。

​

Authorization

string

`Bearer <token>`。`comfyui-` で始まる値はAPIキーです。それ以外の値は Comfy Cloud の JWT として扱われます。

​

Idempotency-Key

string

1つの論理的な生成を識別します。呼び出しの前にUUIDを生成して保存し、変更していないリクエストの再試行時にそれを再利用します。このキーは最大24時間のあいだ、結果を再生したり、受け付けた処理を収集したりできます。SDK はキーを生成しますが、独自のキーを指定することもできます（Python では `idempotency_key=`、TypeScript では `idempotencyKey`）。競合、有効期限、再生できない結果については、[再試行の結果](https://docs.comfy.org/ja/development/comfy-router/errors#%E5%86%8D%E8%A9%A6%E8%A1%8C%E3%81%AE%E7%B5%90%E6%9E%9C)を参照してください。

​

Content-Type

string

`application/json`。モデル固有のJSON入力を送信します。フィールドと検証要件はモデルによって異なります。[Router API の使用](https://docs.comfy.org/ja/development/comfy-router/api)を参照してください。

​

If-None-Match

string

`GET /v2/models/{provider}/{model}/openapi.json` でのみ使用します。以前の `200` で受け取った `ETag` を送信します。それがまだ一致する場合、応答は同じ `ETag` を持つボディなしの `304` になります。モデルのスキーマはプロセスの存続期間中キャッシュし、呼び出しのたびに読み直すのではなく、この方法で再検証してください。

## 

​

レスポンスヘッダー

​

X-Comfy-Request-Id

string

必須

この HTTP リクエストを識別します。サポートに問い合わせる際はこれを含めてください。TypeScript では `requestId` として公開され、Python ではエラー時に `request_id` として公開されます。

​

X-Comfy-Error-Type

string

機械可読なエラーカテゴリ。`422` の場合は、検証ボディに `detail[]` があり `error_type` がないため、このヘッダーを使用します。HTTP ステータスと結合して、どう処理するかを判断してください。不明な値は制御フローでは `internal_error` として扱い、診断用にはそのまま保持してください。

​

Idempotent-Replayed

boolean

Router がモデルを再実行せずに保存済みの結果を返す場合に存在し、`true` になります。新規実行時には存在しません。 キュー投入ルートでは、再生された `201` は 2 回目の実行をキューに入れず、元のリクエストハンドルを返します。

​

Retry-After

integer

再試行する前に待機する秒数。`409` / `concurrency_limit_exceeded` または `504` / `deadline_exceeded` の場合は、待機後に同じリクエストと同じキーで再試行してください。`429` / `rate_limited` の場合は、レート制限がいつリセットされるかを示します。 キューに入れたリクエストのステータス読み取りとその `202` 結果読み取りでは、再度ポーリングする価値があるタイミングについての Router のヒントです。

​

X-Committed-Spend-Limit

integer

まだ実行中の呼び出しに対して確定したパートナー支出の上限（USD セント）。強制する spend gate は、許可されたレスポンスとその `429` 拒否の両方でこれを返すことがあります。gate が強制していない場合、または別の制御がリクエストを拒否した場合は存在しません。

​

X-Committed-Spend-Current

integer

現在実行中の呼び出しに対して確定している USD セント。許可されたレスポンスには自身の呼び出しが含まれ、`429` には拒否された呼び出しは含まれません。`X-Committed-Spend-Limit` とともに送信されます。

​

X-Committed-Spend-Remaining

integer

確定支出の上限を下回って残っている USD セント。要求された呼び出しのコストが残量を超える場合、拒否時でも正の値になることがあります。

​

ETag

string

`GET /v2/models/{provider}/{model}/openapi.json` に対して。これを保存し、キャッシュされたスキーマを再検証するために `If-None-Match` として送り返してください。

​

Cache-Control

string

スキーマルートに対しては `private, must-revalidate`。レスポンスをプライベートキャッシュに保持し、古いコピーを `ETag` で再検証してください。

## 

​

2つの意味を持つステータスコード

3つのステータスが2つのバケットで共有されており、それらを見分けるのがこのヘッダーです:

ステータス| `X-Comfy-Error-Type`| 対処方法  
---|---|---  
`409`| `concurrency_limit_exceeded`| このキーに対するオリジナルの呼び出しがまだ実行中です。`Retry-After` を待ってから、同じキーを再送してください。  
`409`| `invalid_input`| 競合の内容を確認してください。リクエストを変更した場合は、オリジナルのリクエストに戻してください。消費済みでリプレイ不能なキーは結果を復元できません。新規の、課金される可能性がある生成を意図する場合にのみ、新しいキーを使用してください。  
`429`| `concurrency_limit_exceeded`| 実行中の呼び出しが多すぎるか、コミット済み支出の上限(`X-Committed-Spend-*` ヘッダーを参照)に達しています。自身の呼び出しのいずれかが完了すると解除されます。  
`429`| `rate_limited`| 再試行する前に `Retry-After` を待ってください。  
`504`| `deadline_exceeded`| Router 自体の10分間の制限です。`Retry-After` がある場合は、同じキーを再送して実行中の生成結果を回収してください。  
`504`| `provider_timeout`| パートナーがタイムアウトしました。[再試行と課金のガイダンス](https://docs.comfy.org/ja/development/comfy-router/errors#%E5%86%8D%E8%A9%A6%E8%A1%8C%E3%81%AE%E7%B5%90%E6%9E%9C)に従ってください。課金されないことの保証として扱わないでください。  
  
## 

​

次のステップ

  * [クイックスタート](https://docs.comfy.org/ja/development/comfy-router/quickstart): リクエストを送信して結果を読み取ります。
  * [Comfy Router API の使用](https://docs.comfy.org/ja/development/comfy-router/api): モデルの検出、スキーマ、エラー、リトライ、課金について。
  * [API リファレンス](https://docs.comfy.org/ja/development/comfy-router/reference): これらのヘッダーが定義されている生成済みコントラクト。
  * [制限事項](https://docs.comfy.org/ja/development/comfy-router/limitations): Router が現時点で行わないこと、および代わりに使用すべきもの。



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/comfy-router/headers.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/comfy-router/headers)

[Comfy Router の課金前へ](https://docs.comfy.org/ja/development/comfy-router/billing)[Comfy Router API リファレンス次へ](https://docs.comfy.org/ja/development/comfy-router/reference)

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
