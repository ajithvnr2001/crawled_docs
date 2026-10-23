---
url: https://docs.comfy.org/ja/agent-tools/in-app-agent-data-privacy/
title: Comfy Agent \u306e\u30c7\u30fc\u30bf\u3068\u30d7\u30e9\u30a4\u30d0\u30b7\u30fc - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:28.081923+00:00
---

# Comfy Agent のデータとプライバシー - ComfyUI

> Source: https://docs.comfy.org/ja/agent-tools/in-app-agent-data-privacy/

## このページの内容

  * 要点
  * Agent が使用するもの
  * クラウドとローカルのデータフロー
  * チャット履歴と同期
  * スキルとガイダンス
  * 保持と削除



Agent Tools / MCP

# Comfy Agent のデータとプライバシー

ページをコピーページをコピー

Comfy Agent がリクエストへの応答に何を使用するのか、またローカル利用とクラウド利用でどう異なるのかを理解します。

ページをコピーページをコピー

## 

​

要点

Comfy Agent は、あなたのメッセージ、選択済みのワークフロー、選択済みのノード、添付ファイルを使用します。ローカルの ComfyUI インストールで作業している場合、チャット履歴はそのマシンに保存されます。あなたのメッセージと、それに応答するために必要な情報は、Comfy のオンラインサービスを通じて送信されます。

## 

​

Agent が使用するもの

データ| どのように役立つか  
---|---  
あなたのメッセージ| Agent に何をしたいのかを伝えます。  
選択済みのワークフローとノード| 説明または変更したいワークフローとノードを示します。  
画像の添付ファイル| Agent が画像を検査し、ワークフロー内で使用できるようにします。  
ビデオまたはオーディオの添付ファイル| Agent がメディアのプロパティを読み取り、コンテンツを抽出または変換できるようにします。  
ワークフローと実行のエラー| Agent が失敗したワークフローを説明し、修正するのに役立ちます。  
個人スキル| 再利用可能な指示を提供します。  
  
[プライバシーポリシー](https://www.comfy.org/privacy-policy?utm_source=docs) と [利用規約](https://www.comfy.org/terms-of-service?utm_source=docs) が、Comfy の利用に適用されます。

## 

​

クラウドとローカルのデータフロー

Comfy Agent を使用する場所| 何が起こるか  
---|---  
**Comfy Cloud**|  Comfy Cloud は会話、ワークフロー、アセットを保存します。あなたのメッセージは Comfy のオンラインサービスによって処理され、ワークフローはクラウド GPU 上で実行されます。  
**デスクトップ版のローカル ComfyUI**|  ローカルインストールはチャット履歴、ワークフロー、ファイルを保存します。あなたのメッセージと関連するワークフロー情報は Comfy のオンラインサービスによって処理されます。ローカルのワークフローノードはあなたのハードウェア上で実行され、パートナーノードはそれぞれのオンラインプロバイダーを使用します。  
  
## 

​

チャット履歴と同期

クラウド Agent との会話は Comfy Cloud に保存されます。ローカル Agent との会話は、ComfyUI を実行しているマシンに保存されます。この 2 つの履歴は同期されません。これは、どのアプリケーションウィンドウで開いたかではなく、クラウドとローカルインストールのどちらを使用しているかによって決まります。

## 

​

スキルとガイダンス

個人スキルには、あなたが Agent 用に作成した指示が含まれます。これらはあなたのアカウントに保存され、あなたのリクエストがそれらに一致したとき、またはそれらの名前を指定したときに使用されます。 組み込みの Agent ガイダンス、および外部コーディングエージェント向けのスキルは、あなたの個人 Agent スキルとは別です。

## 

​

保持と削除

保持の詳細については、[プライバシーポリシー](https://www.comfy.org/privacy-policy?utm_source=docs) と [データ保持](https://docs.comfy.org/ja/support/data-retention) を参照してください。 アカウントまたはデータの削除をリクエストする場合は、[support@comfy.org](mailto:support@comfy.org) までお問い合わせください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/agent-tools/in-app-agent-data-privacy.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/agent-tools/in-app-agent-data-privacy)

[Comfy Agent スキル前へ](https://docs.comfy.org/ja/agent-tools/in-app-agent-skills)[コーディングエージェント向け Comfy Skills次へ](https://docs.comfy.org/ja/agent-tools/skills)

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
