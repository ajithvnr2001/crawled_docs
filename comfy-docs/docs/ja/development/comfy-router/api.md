---
url: https://docs.comfy.org/ja/development/comfy-router/api/
title: Comfy Router API \u306e\u6982\u8981 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:54.010827+00:00
---

# Comfy Router API の概要 - ComfyUI

> Source: https://docs.comfy.org/ja/development/comfy-router/api/

## このページの内容

  * ガイド
  * モデル別の例
  * 次へ



Comfy Router

# Comfy Router API の概要

ページをコピーページをコピー

Comfy Router API の仕組み: モデル ID ごとに 1 つのルート。検出、スキーマ、キュー中のリクエスト、エラー、課金に関するガイドを用意しています。

ページをコピーページをコピー

モデルを選択し、そのスキーマを確認して、`POST /v2/models/{provider}/{model}` を呼び出します。ルートと認証はモデル間で変わりません。各モデルは独自のネイティブなリクエストボディを受け取り、独自のネイティブな結果を返します。

## 

​

ガイド

## モデルの検出

カタログを一覧表示し、ページをめくり、1 つのモデルのエントリを読み取ります。

## スキーマと結果

モデルの入力スキーマと出力スキーマを取得し、その結果を読み取ります。

## キュー中のリクエスト

今すぐ実行を送信し、後でポーリング、収集、またはキャンセルします。

## エラーとリトライ

エラーレスポンスを読み取り、二重課金なしでリトライします。

## 課金

何が課金されるか、ポリシー拒否時の課金、使用量の突き合わせについて説明します。

## 

​

モデル別の例

  * [Google Gemini](https://docs.comfy.org/ja/development/comfy-router/models/google/gemini/code)
  * [Nano Banana 2](https://docs.comfy.org/ja/development/comfy-router/models/google/nano-banana-2/code)
  * [Nano Banana 2 Lite](https://docs.comfy.org/ja/development/comfy-router/models/google/nano-banana-2-lite/code)
  * [Nano Banana Pro](https://docs.comfy.org/ja/development/comfy-router/models/google/nano-banana-pro/code)
  * [FLUX 1.1 Pro Ultra](https://docs.comfy.org/ja/development/comfy-router/models/black-forest-labs/flux-1-1-pro-ultra-image/code)
  * [FLUX Kontext](https://docs.comfy.org/ja/development/comfy-router/models/black-forest-labs/flux-1-kontext/code)
  * [FLUX Video Upscale](https://docs.comfy.org/ja/development/comfy-router/models/black-forest-labs/flux-video-upscale/code)
  * [FLUX 3 Video](https://docs.comfy.org/ja/development/comfy-router/models/black-forest-labs/flux-3-video/code)
  * [Ideogram 4](https://docs.comfy.org/ja/development/comfy-router/models/ideogram/ideogram-v4/code)



## 

​

次へ

  * [クイックスタート](https://docs.comfy.org/ja/development/comfy-router/quickstart): インストール、呼び出し、画像の保存。
  * [モデル](https://docs.comfy.org/ja/development/comfy-router/models): カタログをブラウズし、モデル固有のリクエスト例を確認します。
  * [ヘッダー](https://docs.comfy.org/ja/development/comfy-router/headers): 認証、冪等性、リクエスト ID、リトライのペース配分。
  * [API リファレンス](https://docs.comfy.org/ja/development/comfy-router/reference): エンドポイントのパラメータ、スキーマ、レスポンスコード。



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/comfy-router/api.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/comfy-router/api)

[Comfy Router クイックスタート前へ](https://docs.comfy.org/ja/development/comfy-router/quickstart)[Comfy Router モデルを検出する次へ](https://docs.comfy.org/ja/development/comfy-router/discover-models)

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
