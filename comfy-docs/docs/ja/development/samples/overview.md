---
url: https://docs.comfy.org/ja/development/samples/overview/
title: \u30c7\u30e2\u30a2\u30d7\u30ea - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:57.392823+00:00
---

# デモアプリ - ComfyUI

> Source: https://docs.comfy.org/ja/development/samples/overview/

Demo Apps

# デモアプリ

ページをコピーページをコピー

Comfy API で構築された動作するデモアプリから始めましょう。

ページをコピーページをコピー

動作するデモアプリから始めて、ワークフローとインターフェースを自分のプロジェクト向けに調整しましょう。最速で進めたい場合は Comfy Cloud を、独自のモデルやノードが必要な場合は「自分でデプロイ」を選びます。

![画像から画像へのウェブアプリのプレビュー](https://mintcdn.com/dripart/h9CkwK6HVnehRaV4/images/samples/img2img-web-app.svg?fit=max&auto=format&n=h9CkwK6HVnehRaV4&q=85&s=20739845b77b13a7f3b9298e7c497e9f)

## 

​

画像から画像へのウェブアプリ

画像をアップロードし、Comfy ワークフローを実行して、結果を Next.js アプリで表示します。

Comfy Cloud を使用自分でデプロイ

[ワークフローをダウンロード ↗](https://github.com/Comfy-Org/comfy-examples/blob/main/img2img-web-app/workflows/workflow_api.json?raw=1)·[ソースを表示 ↗](https://github.com/Comfy-Org/comfy-examples/tree/main/img2img-web-app)

← デモアプリに戻る

Comfy Cloud

## 

​

Comfy Cloud で画像から画像へのウェブアプリを使用する

Comfy Cloud をマネージドエンドポイントとして使用します。APIキーを作成し、アプリのコピーをデプロイします。

1

**APIキーを作成** Comfy APIキーを作成して保存します。対象となる Comfy Cloud サブスクリプションも必須です。

[APIキーを作成 ↗](https://platform.comfy.org/profile/api-keys)

2

**アプリを Vercel にデプロイ** プロバイダーがあなたのアカウントにこのサンプルのコピーを作成します。

[アプリをデプロイ ↗](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FComfy-Org%2Fcomfy-examples%2Ftree%2Fmain%2Fimg2img-web-app&env=COMFY_BASE_URL%2CCOMFY_API_KEY&envDefaults=%7B%22COMFY_BASE_URL%22%3A%22https%3A%2F%2Fcloud.comfy.org%22%7D)

← デモアプリに戻る

自分でデプロイ

## 

​

画像から画像へのウェブアプリ用に独自のエンドポイントをデプロイする

独自のモデルやカスタムノードが必要な場合は、Comfy API のサーバーレスエンドポイントを作成します。

1

**ワークフローをダウンロード** 専用のデプロイフローでこの API 形式のワークフローを使用します。

[ワークフローをダウンロード ↗](https://github.com/Comfy-Org/comfy-examples/blob/main/img2img-web-app/workflows/workflow_api.json?raw=1)

2

**APIキーを作成** デプロイしたアプリが使用するキーを作成して保存します。

[APIキーを作成 ↗](https://platform.comfy.org/profile/api-keys)

3

**ワークフローを貼り付けてデプロイ** Builds でワークフローを貼り付け、エンドポイントを設定し、その URL を待ちます。

[Builds を開く ↗](https://platform.comfy.org/profile/builds)

4

**エンドポイント URL と APIキーを貼り付け** アプリのデプロイ時に COMFY_BASE_URL と COMFY_API_KEY を設定します。

[アプリをデプロイ ↗](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FComfy-Org%2Fcomfy-examples%2Ftree%2Fmain%2Fimg2img-web-app&env=COMFY_BASE_URL%2CCOMFY_API_KEY)

![スケッチから画像へのアプリのプレビュー](https://mintcdn.com/dripart/h9CkwK6HVnehRaV4/images/samples/sketch-to-image.svg?fit=max&auto=format&n=h9CkwK6HVnehRaV4&q=85&s=f4b31ac4090338aad4196bf1ccf4c1af)

## 

​

スケッチから画像

ガイドを描くかインポートし、そのガイドとプロンプトから画像を生成します。

Comfy Cloud を使用自分でデプロイ

[ワークフローをダウンロード ↗](https://github.com/Comfy-Org/comfy-examples/blob/main/sketch-to-image/workflows/workflow_api.json?raw=1)·[ソースを表示 ↗](https://github.com/Comfy-Org/comfy-examples/tree/main/sketch-to-image)

← デモアプリに戻る

Comfy Cloud

## 

​

Comfy Cloud でスケッチから画像を使用する

Comfy Cloud をマネージドエンドポイントとして使用します。APIキーを作成し、アプリのコピーをデプロイします。

1

**APIキーを作成** Comfy APIキーを作成して保存します。対象となる Comfy Cloud サブスクリプションも必須です。

[APIキーを作成 ↗](https://platform.comfy.org/profile/api-keys)

2

**アプリを Vercel にデプロイ** プロバイダーがあなたのアカウントにこのサンプルのコピーを作成します。

[アプリをデプロイ ↗](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FComfy-Org%2Fcomfy-examples%2Ftree%2Fmain%2Fsketch-to-image&env=COMFY_BASE_URL%2CCOMFY_API_KEY&envDefaults=%7B%22COMFY_BASE_URL%22%3A%22https%3A%2F%2Fcloud.comfy.org%22%7D)

← デモアプリに戻る

自分でデプロイ

## 

​

スケッチから画像用に独自のエンドポイントをデプロイする

独自のモデルやカスタムノードが必要な場合は、Comfy API のサーバーレスエンドポイントを作成します。

1

**ワークフローをダウンロード** 専用のデプロイフローでこの API 形式のワークフローを使用します。

[ワークフローをダウンロード ↗](https://github.com/Comfy-Org/comfy-examples/blob/main/sketch-to-image/workflows/workflow_api.json?raw=1)

2

**APIキーを作成** デプロイしたアプリが使用するキーを作成して保存します。

[APIキーを作成 ↗](https://platform.comfy.org/profile/api-keys)

3

**ワークフローを貼り付けてデプロイ** Builds でワークフローを貼り付け、エンドポイントを設定し、その URL を待ちます。

[Builds を開く ↗](https://platform.comfy.org/profile/builds)

4

**エンドポイント URL と APIキーを貼り付け** アプリのデプロイ時に COMFY_BASE_URL と COMFY_API_KEY を設定します。

[アプリをデプロイ ↗](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FComfy-Org%2Fcomfy-examples%2Ftree%2Fmain%2Fsketch-to-image&env=COMFY_BASE_URL%2CCOMFY_API_KEY)

![Discord 画像ボットのプレビュー](https://mintcdn.com/dripart/h9CkwK6HVnehRaV4/images/samples/discord-image-bot.svg?fit=max&auto=format&n=h9CkwK6HVnehRaV4&q=85&s=785b60d710c773d303743a65333f9455)

## 

​

Discord 画像ボット

Discord サーバーに `/imagine` コマンドを追加し、同梱の Comfy ワークフローを実行します。

Comfy Cloud を使用自分でデプロイ

[ワークフローをダウンロード ↗](https://github.com/Comfy-Org/comfy-discord-image-bot/blob/main/workflows/workflow_api.json?raw=1)·[ソースを表示 ↗](https://github.com/Comfy-Org/comfy-discord-image-bot)

← デモアプリに戻る

Comfy Cloud

## 

​

Comfy Cloud で Discord 画像ボットを使用する

Comfy Cloud をマネージドエンドポイントとして使用します。APIキーを作成し、アプリのコピーをデプロイします。

1

**APIキーを作成** Comfy APIキーを作成して保存します。対象となる Comfy Cloud サブスクリプションも必須です。

[APIキーを作成 ↗](https://platform.comfy.org/profile/api-keys)

2

**アプリを Render にデプロイ** プロバイダーがあなたのアカウントにこのサンプルのコピーを作成します。

[アプリをデプロイ ↗](https://render.com/deploy?repo=https%3A%2F%2Fgithub.com%2FComfy-Org%2Fcomfy-discord-image-bot)

← デモアプリに戻る

自分でデプロイ

## 

​

Discord 画像ボット用に独自のエンドポイントをデプロイする

独自のモデルやカスタムノードが必要な場合は、Comfy API のサーバーレスエンドポイントを作成します。

1

**ワークフローをダウンロード** 専用のデプロイフローでこの API 形式のワークフローを使用します。

[ワークフローをダウンロード ↗](https://github.com/Comfy-Org/comfy-discord-image-bot/blob/main/workflows/workflow_api.json?raw=1)

2

**APIキーを作成** デプロイしたアプリが使用するキーを作成して保存します。

[APIキーを作成 ↗](https://platform.comfy.org/profile/api-keys)

3

**ワークフローを貼り付けてデプロイ** Builds でワークフローを貼り付け、エンドポイントを設定し、その URL を待ちます。

[Builds を開く ↗](https://platform.comfy.org/profile/builds)

4

**エンドポイント URL と APIキーを貼り付け** アプリのデプロイ時に COMFY_BASE_URL と COMFY_API_KEY を設定します。

[アプリをデプロイ ↗](https://render.com/deploy?repo=https%3A%2F%2Fgithub.com%2FComfy-Org%2Fcomfy-discord-image-bot)

どちらの方法でも [Comfy APIキー](https://platform.comfy.org/profile/api-keys) が必要です。「自分でデプロイ」の場合は、ワークフローをダウンロードし、Builds でそれを貼り付けてサーバーレスエンドポイントを設定し、その URL を待ってから、その URL と APIキーを Vercel または Render のデプロイに貼り付けます。

デモアプリを追加したいですか？ [examples リポジトリ](https://github.com/Comfy-Org/comfy-examples) を参照してください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/samples/overview.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/samples/overview)

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
