---
url: https://docs.comfy.org/ja/development/comfy-router/discover-models/
title: Comfy Router \u30e2\u30c7\u30eb\u3092\u691c\u51fa\u3059\u308b - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:54.133177+00:00
---

# Comfy Router モデルを検出する - ComfyUI

> Source: https://docs.comfy.org/ja/development/comfy-router/discover-models/

## このページの内容

  * カタログを検出する
    * ページネーション
  * 1 つのモデルを読み取る
  * 次のステップ



Comfy Router

# Comfy Router モデルを検出する

ページをコピーページをコピー

GET /v2/models で Comfy Router のカタログを一覧表示し、カーソルでページを送り、モデルのエントリを ID で 1 件取得します。

ページをコピーページをコピー

すべての Router モデルは `{provider}/{model}` 形式の ID で指定します。カタログを使ってその ID を見つけ、`POST /v2/models/{provider}/{model}` を呼び出します。

## 

​

カタログを検出する

生成に使用したのと同じ APIキーでモデルを一覧表示します:
    
    
    curl -H "X-API-Key: $COMFY_API_KEY" \
      "https://api.comfy.org/v2/models?limit=50"
    

カタログレスポンスの抜粋:
    
    
    {
      "data": [
        {
          "id": "bfl/flux-2-pro",
          "provider": "bfl",
          "model": "flux-2-pro",
          "billing": { "charges_on_policy_rejection": "no" }
        }
      ],
      "has_more": true,
      "next_cursor": "example-cursor",
      "limit": 50
    }
    

呼び出しパスには `id` を使用します。`billing` オブジェクトには課金に関する事実が含まれており、価格ではありません。これに依存する前に [ポリシー拒否時の課金](https://docs.comfy.org/ja/development/comfy-router/billing#%E3%83%A2%E3%83%87%E3%83%AB%E8%AA%B2%E9%87%91%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E4%BA%8B%E5%AE%9F) をお読みください。

### 

​

ページネーション

  * `has_more` が `true` の場合は、返された `next_cursor` を `cursor` として渡します。前のページが要求より短かった場合でも、`has_more` が `false` になったら停止します。
  * カーソルは不透明な値として扱います。たとえば cURL の `--get --data-urlencode "cursor=$NEXT_CURSOR"` のように値を URL エンコードしてください。オフセットを計算したりカーソルを変更したりしないでください。
  * `limit` のデフォルトは 20 で、上限は 100 です。上限を超える値は上限値に丸められます。ゼロおよびネガティブな値はデフォルトを選択します。レスポンスには実際に使用された limit が報告されます。
  * 無効なカーソルは `400` / `invalid_input` を返します。リストを暗黙的に再起動することはありません。
  * カーソルはカタログの更新をまたいでも有効なままの場合がありますが、走査はスナップショットではありません。現在位置より前に追加されたモデルが、その走査に現れないことがあります。

`503` / `service_unavailable` は一時的なものです。バックオフしながら再試行してください。空のカタログとして扱わないでください。SDK の run メソッドは選択済みのモデルを直接呼び出します。

## 

​

1 つのモデルを読み取る

モデル ID がわかっている場合は、カタログのエントリを直接取得します:
    
    
    curl -H "X-API-Key: $COMFY_API_KEY" \
      https://api.comfy.org/v2/models/bfl/flux-2-pro
    

モデル詳細エンドポイントを使えば、カタログ全体を走査せずに済みます。エントリの完全なフィールドについては [API リファレンス](https://docs.comfy.org/ja/development/comfy-router/reference) を参照してください。

## 

​

次のステップ

  * [スキーマと結果](https://docs.comfy.org/ja/development/comfy-router/schemas): モデルを呼び出す前に、そのモデルの入力と出力のスキーマを確認します。
  * [すべてのモデル](https://docs.comfy.org/ja/development/comfy-router/models): 各モデルで実際に動作するリクエストとともにカタログをブラウズします。



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/comfy-router/discover-models.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/comfy-router/discover-models)

[Comfy Router API の概要前へ](https://docs.comfy.org/ja/development/comfy-router/api)[Comfy Router モデルスキーマと結果次へ](https://docs.comfy.org/ja/development/comfy-router/schemas)

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
