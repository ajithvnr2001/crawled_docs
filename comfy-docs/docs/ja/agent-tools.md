---
url: https://docs.comfy.org/ja/agent-tools/
title: ComfyUI \u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u30c4\u30fc\u30eb\uff1aMCP\u3001CLI\u3001\u5185\u8535\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:22.348528+00:00
---

# ComfyUI エージェントツール：MCP、CLI、内蔵エージェント - ComfyUI

> Source: https://docs.comfy.org/ja/agent-tools/

## このページの内容

  * どれを使うべき？
  * MCP とは？



Agent Tools / MCP

# ComfyUI エージェントツール：MCP、CLI、内蔵エージェント

ページをコピーページをコピー

Comfy MCP、Comfy CLI、Comfy Agent を通じて、AI エージェントとともに ComfyUI を使用します。

ページをコピーページをコピー

## Comfy MCP

あらゆる AI エージェントを、Comfy Cloud または自分のマシン上の ComfyUI に接続できます。**ここから始めましょう。**

## Comfy Agent

ComfyUI に組み込まれたアシスタントで、ワークフローの構築、編集、実行を行えます。**Cloud では一般提供中。** ローカル（Comfy Desktop）は近日公開。

## Comfy CLI

ターミナルで使える ComfyUI。ComfyUI のインストールとアップデート、モデルとノードの管理、スクリプト、CI、バッチジョブからの生成が可能です。

* * *

## 

​

どれを使うべき？

| Comfy MCP  
クラウド接続| Comfy MCP  
ローカル接続| Comfy Agent  
---|---|---|---  
**説明**|  自分のエージェントで Comfy Cloud のワークフローを実行します。| 自分のエージェントでローカルの ComfyUI を操作します。| ComfyUI 内でエージェントとチャットし、選択済みのワークフローを理解、構築、編集、実行します。  
**最適な用途**|  ローカルに ComfyUI をセットアップしたくない初心者。  
ワークフローを共有したい人。| ローカルに ComfyUI を導入している人。  
プライベートなカスタムノードを持っている人。  
ローカルファイルシステムを操作する必要がある人。| キャンバスを見ながらワークフローを構築・編集したい人。  
**必要条件**|  自分のエージェント。  
有効な Comfy Cloud サブスクリプション。| 自分のエージェント。  
ローカルの ComfyUI セットアップ。| Comfy アカウント。Cloud ではウェイトリストなし。Comfy Desktop は近日公開。  
**GPU**|  クラウド GPU（ハードウェア要件なし）| ローカル GPU| 現時点ではクラウド GPU。Comfy Desktop 対応の提供開始後はローカルハードウェア。  
**モデル**|  Comfy Cloud のモデル。  
独自モデルのインポートが可能です。| 自分のマシンにダウンロードしたローカルモデル。| 現時点ではクラウドモデル。Comfy Desktop 対応の提供開始後はローカルモデル。  
**カスタムノード**|  Comfy Cloud でサポートされているカスタムノード。| 任意のカスタムノードをインストールできます。| 現時点では Cloud でサポートされているノード。Comfy Desktop 対応の提供開始後は任意のローカルノード。  
  
MCP の 2 つの列は**同じ製品であり、同じページ** です。[Comfy MCP](https://docs.comfy.org/ja/agent-tools/mcp) を参照して選択してください。両方を同時に接続することもできます。

* * *

## 

​

MCP とは？

**Model Context Protocol (MCP)** は、AI アシスタントが標準化されたインターフェースを通じて外部ツールやサービスと連携できるようにするオープンスタンダードです。AI エージェントがサービスごとに独自の API 形式を把握する必要はなく、MCP はツールを統一された方法で公開します。 MCP サーバーを Claude Desktop、Claude Code、Cursor、Amp に接続すると、AI アシスタントは次のことができるようになります。

  * テキストの説明から**画像を生成**
  * テキストや画像から**動画を作成**
  * テキストや画像から**3D モデルを生成**
  * AI モデルを使って**オーディオや音楽を生成**
  * タスクに適したツールを見つけるために**モデルやテンプレートを検索**

……これらすべてを自然言語の対話を通じて行え、API 呼び出しを手動で書く必要はありません。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/agent-tools/index.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/agent-tools)

[AI画像生成の始め方前へ](https://docs.comfy.org/ja/get_started/first_generation)[Comfy MCP：AIエージェントをComfyUIに接続次へ](https://docs.comfy.org/ja/agent-tools/mcp)

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
