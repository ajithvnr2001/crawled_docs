---
url: https://docs.comfy.org/ja/development/api-development/getting-an-api-key/
title: API \u30ad\u30fc\u306e\u53d6\u5f97 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:51.297520+00:00
---

# API キーの取得 - ComfyUI

> Source: https://docs.comfy.org/ja/development/api-development/getting-an-api-key/

## このページの内容

  * API キーの作成
  * API キーの管理
  * API キーの使用



ワークフローの実行

# API キーの取得

ページをコピーページをコピー

Cloud API、Partner Node などにアクセスするための Comfy Platform API キーの作成と管理方法を学びます。

ページをコピーページをコピー

API キーは Comfy Platform サービスにアクセスするための認証情報です。以下の用途に使用できます：

  * [Cloud API](https://docs.comfy.org/ja/development/cloud/overview) — Comfy Cloud のエンドポイントをプログラムから呼び出す
  * [Partner Node API 統合](https://docs.comfy.org/ja/development/comfyui-server/api-key-integration) — ローカルワークフローで有料 API ノードを使用する
  * [MCP 接続](https://docs.comfy.org/ja/agent-tools) — MCP 経由で Comfy に接続する
  * [ComfyUI にローカルログイン](https://docs.comfy.org/ja/interface/user#api-key-%E3%81%A7%E3%81%AE%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3) — メールアドレスの代わりに API キーで認証する



## 

​

API キーの作成

1

https://platform.comfy.org/login にアクセスしてログイン

<https://platform.comfy.org/login> にアクセスし、対応するアカウントでログインしてください。![プラットフォームのログインページにアクセス](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-1.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=c9516c73148a20ac2de9fcd5f56860c9)

2

API キーの一覧で `+ New` をクリックして API キーを作成

API キーの一覧で `+ New` をクリックし、API キーを作成します。![API キーを作成](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-2.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=9e1f6dc2a5a28fbbe5074f4267dd8d14)

3

API キーの名前を入力

![API キーの名前を入力](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-3.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=112f28de30c52898bca15513706c70f2)

  1. （必須）API キーの名前を入力してください。
  2. `Generate` をクリックして作成します。



4

取得した API キーを保存

![API キーを取得](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-4.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=223b5d1941d0d9a2f2644807b08a676f)

API キーは初回作成時のみ表示されるため、作成直後に必ず保存してください。その後は再表示されませんので、安全に保管してください。また、API キーを第三者と共有しないようご注意ください。万一漏洩した場合は、該当のキーを削除し、新しいキーを作成してください。

## 

​

API キーの管理

ログイン後、[platform.comfy.org](https://platform.comfy.org) ですべての API キーを確認および管理できます。

  * **既存のキーを確認** ：各キーの名前と作成日を確認
  * **キーを削除** ：キーが漏洩した場合や不要になった場合はすぐに削除
  * **複数のキーを作成** ：異なるアプリケーションごとに複数の API キーを作成可能



API キーは作成時にのみ表示されます。すぐに安全な場所に保存してください。キーを紛失した場合は、削除して新しいキーを作成してください。

## 

​

API キーの使用

API キーを取得したら、以下の方法で使用できます：

  1. **ComfyUI にローカルログイン** — **設定 → ユーザー** から「Comfy API Key」ログインを選択
  2. **Partner Node API の呼び出し** — ワークフロー送信時に `extra_data.api_key_comfy_org` にキーを含める
  3. **Cloud API の使用** — Cloud API リクエストヘッダーにキーを含める

セキュリティのため、API キーを共有したり、バージョン管理システムにコミットしたりしないでください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/api-development/getting-an-api-key.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/api-development/getting-an-api-key)

[Comfy API：サーバーレスデプロイ前へ](https://docs.comfy.org/ja/development/serverless/overview)[Comfy API v2 の概要次へ](https://docs.comfy.org/ja/api-reference/v2/overview)

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
