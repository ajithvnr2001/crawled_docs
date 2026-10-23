---
url: https://docs.comfy.org/ja/development/comfy-router/quickstart/
title: Comfy Router \u30af\u30a4\u30c3\u30af\u30b9\u30bf\u30fc\u30c8 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:53.772558+00:00
---

# Comfy Router クイックスタート - ComfyUI

> Source: https://docs.comfy.org/ja/development/comfy-router/quickstart/

## このページの内容

  * APIキーを作成する
  * リクエストをキューに入れる
  * 画像から動画と参照から動画
  * 次のステップ



Comfy Router

# Comfy Router クイックスタート

ページをコピーページをコピー

最新のフロンティアメディアモデルを使って、数分で画像とビデオを生成します。

ページをコピーページをコピー

Comfy Router は、`https://api.comfy.org` でホスト型の画像モデルとビデオモデルを利用するための単一の API を提供します。[Comfy ワークスペース](https://platform.comfy.org/profile/api-keys?onboarding=router)で API キーを作成し、公式の [Python および TypeScript SDK](https://docs.comfy.org/ja/development/api-development/sdks) か、通常の HTTP 経由で任意のモデルを呼び出せます。課金は従量制です。各リクエストはワークスペースの残高からクレジットを消費し、サブスクリプションはありません。

**Higgsfield をお使いですか?** ご自身の Higgsfield キーを保存すると、それらの生成は Comfy クレジットではなく Higgsfield アカウントに課金されます。エンドポイントもリクエストボディも同じです。詳細は [Higgsfield を自分のキーで使う](https://docs.comfy.org/ja/development/comfy-router/higgsfield-byok) を参照してください。

**LiteLLM で支出を追跡しますか?** Router は、LiteLLM が読み取るヘッダーに同期実行の USD コストを報告するため、価格表を維持する必要はありません。詳細は [Comfy Router を LiteLLM で使う](https://docs.comfy.org/ja/development/comfy-router/litellm) を参照してください。

1

## APIキーを作成する

[Comfy ワークスペース](https://platform.comfy.org/profile/api-keys?onboarding=router)でキーを作成します。Bash 互換のターミナルで次を設定します:
    
    
    export COMFY_API_KEY="comfyui-..."
    

API キーはサーバー上またはローカル環境に保管してください。これらの例はターミナルまたはサーバー向けであり、ブラウザの JavaScript 向けではありません。Router はリクエストごとにクレジットを課金します。ワークスペースにクレジット残高がない場合、最初の実際の呼び出しは `402` と `error_type: insufficient_credits` を返します。このチェックはボディの検証より前に実行されるため、クレジットのないワークスペースでは無効なリクエストでも `402` が返ることがあります。リクエストボディをデバッグする前に、[ワークスペースの請求](https://platform.comfy.org)でクレジットを追加してください。

2

## リクエストをキューに入れる

使用する言語を選んでサンプルを実行します。生成には数分かかることがあります。

Python

cURL

TypeScript
    
    
    # Python 3.10+
    # インストール: python -m pip install "comfy-sdk>=0.3.0"
    # quickstart.py として保存し、実行: python quickstart.py
    
    import asyncio
    
    from comfy_sdk import AsyncComfy
    
    # AsyncComfy は環境変数から COMFY_API_KEY を読み取ります。
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "byteplus/dreamina-seedance-2-5-260628",
                {
                    "content": [
                        {
                            "text": "A red fox trotting through a snowy pine forest",
                            "type": "text",
                        },
                    ],
                    "duration": 5,
                    "ratio": "16:9",
                    "resolution": "720p",
                },
            )
            print("request_id:", handle.request_id)
    
            # リクエストが完了するまでポーリングし、サーバーが指定する Retry-After だけ待機します。
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            result = await handle.get()
    
        print("result:", result)
    
    asyncio.run(main())
    
    
    
    # 1. リクエストを送信します。201 レスポンスの request_id を保存します。
    curl https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-5-260628/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d '{"content": [{"text": "A red fox trotting through a snowy pine forest", "type": "text"}], "duration": 5, "ratio": "16:9", "resolution": "720p"}'
    
    # 2. ステータスが COMPLETED になるまでポーリングし、毎回 Retry-After の値だけ待機します。
    REQUEST_ID="paste-request-id-from-201-response"
    curl -i "https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-5-260628/requests/$REQUEST_ID/status" \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. モデルの結果を取得します。
    curl "https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-5-260628/requests/$REQUEST_ID" \
      -H "X-API-Key: $COMFY_API_KEY"
    
    
    
    // Node.js 22+
    // インストール: npm install "@comfyorg/sdk@>=0.4.0" --save-dev tsx
    // quickstart.mts として保存し、実行: npx tsx quickstart.mts
    
    import { comfy } from "@comfyorg/sdk";
    
    // Comfy は環境変数から COMFY_API_KEY を読み取ります。
    const handle = await comfy.models.submit(
      "byteplus/dreamina-seedance-2-5-260628",
      {
        content: [
          {
            text: "A red fox trotting through a snowy pine forest",
            type: "text",
          },
        ],
        duration: 5,
        ratio: "16:9",
        resolution: "720p",
      },
    );
    console.log("requestId:", handle.requestId);
    
    // リクエストが完了するまでポーリングし、サーバーが指定する Retry-After だけ待機します。
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    const result = await handle.get();
    
    console.log("result:", result.data);
    

SDK の submit 呼び出しはそれぞれ冪等性キーを作成し、自動リトライでそれを再利用します。cURL の例では `uuidgen` で作成します。利用できない場合は、別の UUID 生成ツールを使用してください。ステータス、キャンセル、結果の取得の詳細については、[キューの配信](https://docs.comfy.org/ja/development/comfy-router/queue) を参照してください。

## 

​

画像から動画と参照から動画

同じ Seedance リクエストが画像、動画、音声の入力を受け取ります。`content` に項目を追加し、それぞれに `role` を設定します。送信する role が Router の実行する操作を決定します。課金は role ではなく `content` 内のメディア種別に従います。動画入力が 1 つでもあるリクエストは動画から動画として課金され、そうでなければ画像が 1 つでもあるリクエストは画像から動画として課金され、テキストのみのリクエストはテキストから動画として課金されます。テキストから動画と画像から動画に同じ料金を課すモデルもあります。

操作| `content` の項目  
---|---  
テキストから動画| `text` 項目を 1 つ  
画像から動画| `text` 項目 1 つと `role: first_frame` の `image_url` 項目  
最初と最後のフレーム| 上記に加えて `role: last_frame` の 2 つ目の `image_url` 項目  
参照から動画| `text` 項目 1 つと `role: reference_image` の `image_url` 項目群、さらに Seedance 2.0 と 2.5 では `role: reference_video` の `video_url` 項目群と `role: reference_audio` の `audio_url` 項目群  
  
画像の `url` には公開 URL か `data:image/<format>;base64,<content>` 文字列を使用できます。送信、ポーリング、収集は上記のクイックスタートとまったく同じです。変わるのはボディだけです。

Image-to-video
    
    
    curl https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-5-260628/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d '{
        "content": [
          {"type": "text", "text": "The fox turns and runs into the trees"},
          {"type": "image_url", "image_url": {"url": "https://example.com/fox.png"}, "role": "first_frame"}
        ],
        "duration": 5,
        "resolution": "720p"
      }'
    

Reference-to-video
    
    
    curl https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-5-260628/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d '{
        "content": [
          {"type": "text", "text": "The character from the reference walks through a neon-lit market"},
          {"type": "image_url", "image_url": {"url": "https://example.com/character.png"}, "role": "reference_image"},
          {"type": "image_url", "image_url": {"url": "https://example.com/outfit.png"}, "role": "reference_image"}
        ],
        "duration": 5,
        "ratio": "16:9",
        "resolution": "720p"
      }'
    

Seedance 2.5 では、最初のフレームと最初と最後のフレームのリクエストは、出力のアスペクト比を最初のフレームから取得します。具体的な比率は `400` で拒否されるため、`ratio` を省略するか `adaptive` を送信してください。リクエストスキーマは Seedance ファミリーで共有されており、モデルが無視する role が含まれることがあるため、各モデルの[入力スキーマ](https://docs.comfy.org/ja/development/comfy-router/models) の `x-comfy-router-input-modalities` フィールドで、そのモデルが受け付ける入力種別を確認してください。たとえば、`reference_video` と `reference_audio` には、そこで `video` または `audio` を列挙しているモデルが必要です。

## 

​

次のステップ

## モデルをブラウズ

利用可能なモデルを確認し、モデル固有のリクエスト例を見つけられます。

## Router API の使用

モデルの検出、スキーマ、キュー中のリクエスト、エラー、課金について学びます。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/comfy-router/quickstart.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/comfy-router/quickstart)

[Comfy API のバージョン：v2 と非推奨の v1 Cloud API前へ](https://docs.comfy.org/ja/development/comfy-api/overview)[Comfy Router API の概要次へ](https://docs.comfy.org/ja/development/comfy-router/api)

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
