---
url: https://docs.comfy.org/ja/development/comfy-router/billing/
title: Comfy Router \u306e\u8ab2\u91d1 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:54.880493+00:00
---

# Comfy Router の課金 - ComfyUI

> Source: https://docs.comfy.org/ja/development/comfy-router/billing/

## このページの内容

  * モデル課金に関する事実
  * 請求の照合
  * 次のステップ



Comfy Router

# Comfy Router の課金

ページをコピーページをコピー

Comfy Router がモデル呼び出しに対してどのように課金するか、カタログのポリシー拒否時の課金フィールドの意味、および使用量を照合する方法について説明します。

ページをコピーページをコピー

課金が発生するのは、プロバイダーが Comfy に課金したときです。同じルールが同期呼び出しと[キュー中](https://docs.comfy.org/ja/development/comfy-router/queue#%E5%86%AA%E7%AD%89%E6%80%A7%E3%81%A8%E8%AA%B2%E9%87%91)の呼び出しにも適用され、結果を再送する同一キーの[再試行](https://docs.comfy.org/ja/development/comfy-router/errors#%E5%86%8D%E8%A9%A6%E8%A1%8C%E3%81%AE%E7%B5%90%E6%9E%9C)に二重の課金は発生しません。

## 

​

モデル課金に関する事実

`GET /v2/models` とモデル詳細レスポンスには `billing.charges_on_policy_rejection` が含まれます。これはポリシー拒否についてのものであり、すべての失敗や価格見積もりを示すものではありません。

値| 意味  
---|---  
`yes`| ポリシー拒否に対して課金されます。  
`no`| ポリシー拒否に対して課金されません。  
`unknown`| まだ挙動が確認されていません。課金される可能性があるものとして扱ってください。  
  
これらの文字列は明示的に比較してください。`"no"` は Python と JavaScript では真（truthy）と評価されます。認識できない値はすべて `unknown` として扱ってください。クレジット不足で拒否されたリクエストは `insufficient_credits` を報告します。

## 

​

請求の照合

プロバイダーのペイロードには独自のコストや使用量の数値が含まれることがありますが、それらは Comfy の請求額ではありません。`X-Comfy-Credits-Used` は一部のモデルと成功したレスポンスでのみ利用できます。同じ `Idempotency-Key` のリクエストで Router が結果を再送する場合、元のヘッダーとともに `Idempotent-Replayed: true` が返されます。課金は一度だけなので、再送されたヘッダーを再度合算しないでください。ヘッダーがないことは無料を意味しません。照合には[ワークスペースの使用量と請求書](https://platform.comfy.org)を使用し、請求を調査する際はリクエスト ID を保管してください。

## 

​

次のステップ

  * [制限事項](https://docs.comfy.org/ja/development/comfy-router/limitations#comfy-%E3%81%AE%E8%AA%B2%E9%87%91%E3%81%A8%E4%BD%BF%E7%94%A8%E9%87%8F): Router が課金について報告する内容と、報告しない内容。
  * [エラーと再試行](https://docs.comfy.org/ja/development/comfy-router/errors): 二重に課金される呼び出しを作らずに再試行します。



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/comfy-router/billing.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/comfy-router/billing)

[Comfy Router のエラーとリトライ前へ](https://docs.comfy.org/ja/development/comfy-router/errors)[Comfy Router ヘッダー次へ](https://docs.comfy.org/ja/development/comfy-router/headers)

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
