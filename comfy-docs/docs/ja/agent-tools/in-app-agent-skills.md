---
url: https://docs.comfy.org/ja/agent-tools/in-app-agent-skills/
title: Comfy Agent \u30b9\u30ad\u30eb - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:27.550457+00:00
---

# Comfy Agent スキル - ComfyUI

> Source: https://docs.comfy.org/ja/agent-tools/in-app-agent-skills/

## このページの内容

  * 個人スキルとは？
  * チャットでスキルを作成する
  * スキルを使用する
  * スキルを更新または削除する
  * 既存のスキルファイルを保存する
  * 公開スキルを使用する
  * 組み込みガイダンスとコーディングエージェントスキル



Agent Tools / MCP

# Comfy Agent スキル

ページをコピーページをコピー

個人スキルと公開スキルを使って、Comfy Agent に作業で再利用できる指示を与えます。

ページをコピーページをコピー

## 

​

個人スキルとは？

個人スキルとは、Comfy Agent 向けの再利用可能な指示のまとまりです。名前、いつ使うかを示す 1 行の説明、そして指示そのものが含まれます。 個人スキルは、「正方形の画像を作成する」「白い背景を使う」「実行前にノードの接続を確認する」といった指示を繰り返すために使用します。 個人スキルはアカウントに保存されます。Agent は、スキルの説明がリクエストと一致したとき、または名前で指定したときにそのスキルを読み込みます。

## 

​

チャットでスキルを作成する

保存する内容、名前、使用するタイミングを Agent に伝えます:

> これを product-shot というスキルとして保存して: 製品画像を依頼したときは、正方形の 1024 × 1024 キャンバス、ニュートラルグレーの背景、Save Image ノードを使用すること。実行前にワークフローを検証すること。

Agent は今後のメッセージのためにスキルを保存します。新規または更新されたスキルは、次のメッセージから有効になります。

## 

​

スキルを使用する

名前でスキルを依頼します:

> 私の product-shot スキルを使って、赤いスニーカーのスタジオ写真ワークフローを作成して。

Agent は、リクエストが説明と一致した場合にスキルを自動的に選択することもできます。

## 

​

スキルを更新または削除する

同じスキル名で指示を置き換えます:

> 私の product-shot スキルを更新して、白い背景と 1536 × 1536 のキャンバスを使用するようにして。

名前でスキルを削除します:

> 私の product-shot スキルを削除して。

## 

​

既存のスキルファイルを保存する

`SKILL.md` ファイルの内容をチャットに貼り付け、個人スキルとして保存するよう Agent に依頼します。Agent はファイルの先頭にあるヘッダーから名前と説明を読み取ります。保存されたスキルは次のメッセージから利用できます。

## 

​

公開スキルを使用する

公開スキルは、あなたが作成したものに限らず誰でも使用できる共有スキルです。名前で公開スキルを依頼するか、やりたいことを説明すると、Agent はあなたの個人スキルと同じようにそれを使用します:

> ニュートラルグレーの背景に赤いスニーカー用の product-shot 公開スキルを使用して。

## 

​

組み込みガイダンスとコーディングエージェントスキル

Comfy Agent には、ワークフローを構築しモデルを選択するためのガイダンスが含まれています。個人スキルと公開スキルは、そのガイダンスに加えて、繰り返し行うタスク向けの指示を追加します。 [コーディングエージェント向けスキル](https://docs.comfy.org/ja/agent-tools/skills)は、Claude Code などのツールに別途インストールします。そこでインストールしても、Comfy Agent には追加されません。 API キー、パスワード、アクセストークンはスキルの指示に含めないでください。データの取り扱いについては、[データとプライバシー](https://docs.comfy.org/ja/agent-tools/in-app-agent-data-privacy#%E3%82%B9%E3%82%AD%E3%83%AB%E3%81%A8%E3%82%AC%E3%82%A4%E3%83%80%E3%83%B3%E3%82%B9)を参照してください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/agent-tools/in-app-agent-skills.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/agent-tools/in-app-agent-skills)

[Comfy Agent をはじめる前へ](https://docs.comfy.org/ja/agent-tools/in-app-agent-installation)[Comfy Agent のデータとプライバシー次へ](https://docs.comfy.org/ja/agent-tools/in-app-agent-data-privacy)

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
