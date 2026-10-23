---
url: https://docs.comfy.org/ja/development/api-development/sdks-design/
title: \u8a2d\u8a08\u30ce\u30fc\u30c8 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:52.035439+00:00
---

# 設計ノート - ComfyUI

> Source: https://docs.comfy.org/ja/development/api-development/sdks-design/

## このページの内容

  * なぜ新しい API なのか
  * 既存のエンドポイントをラップしない理由
  * まずポーリング、進捗はストリームで
  * 既存APIとの関係
  * 最初のバージョンの範囲
  * ローカルプロキシ
  * なぜPythonとTypeScriptが最初なのか
  * 私たちがあなたに求めていること



ワークフローの実行

# 設計ノート

ページをコピーページをコピー

Comfy API v2が存在する理由、既存のComfyUI APIとの関係、そして今後の予定について

ページをコピーページをコピー

[Comfy SDKs](https://docs.comfy.org/ja/development/api-development/sdks)と、それらが呼び出す[Comfy API v2](https://docs.comfy.org/ja/api-reference/v2/overview)の背景です。SDKを使用するにあたり、この背景知識は必要ありません。新しいAPIと既存APIのどちらを基盤に構築するかを検討している場合は、お読みください。

## 

​

なぜ新しい API なのか

既に HTTP 経由で `/prompt` と `/history` を呼び出して ComfyUI を操作できます。これらのエンドポイントは ComfyUI の Web UI を支えるために存在しており、それらを基に構築することは、あなたに約束されていない内部実装に依存することを意味します。v2 API は、それらが提供できない 3 つのものを追加します。 **確約。** v2 はバージョン管理され、ドキュメント化され、サポートされています。v2 内での変更は追加的なものです。破壊的な変更は v3 としてリリースされます。ComfyUI の新しいリリースによってあなたの統合が壊れることはありません。 **移植性。** ローカルの ComfyUI に対しても、Comfy Cloud に対しても、後で提供する他の何に対しても、同じ動作を実現します。同じコードで、異なるベース URL です。 **本番環境に耐える形状。** 永続的なジョブ ID、冪等な送信、型付きエラー、正規化された出力、そして真のバックプレッシャーを備え、すべての統合が `prompt_id` と `/history` の上にこれら 5 つを再発明する必要はありません。

## 

​

既存のエンドポイントをラップしない理由

それらは、一度に1つのワークフローを実行する単一のComfyUIインスタンスを前提としており、その前提が`prompt_id`、`/history`、およびWebSocketプロトコルに組み込まれているためです。 v2 APIはその前提を持ちません。同時に多数のワークフローが実行され、それぞれが永続的なジョブIDで識別されることが、例外ではなくデフォルトのケースです。

## 

​

まずポーリング、進捗はストリームで

v2 のすべての機能は、通常の GET リクエストで利用できます。`GET /api/v2/jobs/{id}` は、現在のステータス、最新の進捗スナップショット、およびこれまでにコミットされたすべての出力を返します。これはジョブの正規のビューであり、ジョブの `expires_at` まで利用可能です。 `GET /api/v2/jobs/{id}/events` の SSE ストリームは、両 SDK で `job.events()` として公開されており、その上に構築されたライブ拡張機能です。プログレスバーを駆動するために使用してください。真実のソースとして使用しないでください。イベント ID はなく、再開カーソルもなく、切断されていた間に送信されたフレームは失われます。 正規の方法がストリームやウェブフックではなくポーリングである理由は 2 つあります。

  * ワークフローは長時間実行される可能性があります。3 秒間接続が途切れても、結果を失うことは決してないはずです。
  * ウェブフックは、公開アドレスを持つサービスには適しています。ポートで待ち受けていない個人のデスクトップ上の Blender プラグインには機能せず、また機能すべきでもありません。

実際の効果として、すべてのステップが再開可能です。プロセスがジョブの途中でクラッシュした場合、1 時間後に戻ってきても、`GET /api/v2/jobs/{id}` にはステータスと出力がまだあります。他のトランスポートは、それに適したケースのために後で追加される可能性があります。この方法はどこでも機能します。

## 

​

既存APIとの関係

非推奨となるものはありません。`/prompt`、`/history`、`/ws`、およびその他のAPIは引き続き動作し、[Cloud API](https://docs.comfy.org/ja/development/cloud/overview)も動作し続けます。現在動作している統合は、これによって壊れることはありません。この2つは共存します。

| Comfy API v2| 既存API  
---|---|---  
**互換性**|  バージョン管理されている。v2内では追加変更のみ| リリース間の互換性は保証されない  
**並行処理モデル**|  複数のジョブを同時実行でき、それぞれに永続的なIDがある| 1つのインスタンスにつき、同時に1つのワークフロー  
**実行対象**|  Comfy Cloudとセルフホスト型ComfyUI、同一のコントラクト| Cloud APIとComfyUIサーバーAPIは異なる  
**公式クライアント**|  PythonおよびTypeScript SDK| なし  
**最適な用途**|  新規の統合| すでに動作している統合  
  
## 

​

最初のバージョンの範囲

ひとつのことをきちんと実現する: ワークフローを実行し、結果を取得する。入力をアップロードし、API形式のグラフを送信し、実行を監視し、出力を取得する。 これが意図的に設定された全体の範囲です。保存されたワークフロー、モデルライブラリ管理、ノードのイントロスペクション、名前付きワークフローパラメータはまだここにはありません。ComfyUIが展開されるあらゆる方法で確実にサポートできる小さな範囲を提供するほうが、一部の方法でしか機能しない大きな範囲を提供するよりも望ましいと考えています。ここから成長していきます。

## 

​

ローカルプロキシ

セルフホスト型ComfyUIは、インスタンスと並行して実行され、v2コントラクトを提供する[comfy-api-proxy](https://github.com/Comfy-Org/comfy-api-proxy)を介してv2で通信します。プロキシはオープンソースです。設定方法は[API Proxy ガイド](https://docs.comfy.org/ja/development/comfyui-server/api-proxy)を参照してください。

## 

​

なぜPythonとTypeScriptが最初なのか

それは、すでにComfyUIをスケール環境で運用している人々に尋ねたところ、需要があったのがこの2言語だったからです。両SDKは同じ文書化されたHTTPコントラクトに基づいているため、どの言語でも今すぐAPIを利用できます。他の言語のファーストパーティSDKをご希望の場合は、[当Discord](https://discord.com/invite/comfyorg) の `#developer-platform` チャンネルでお知らせください。

## 

​

私たちがあなたに求めていること

SDK と API へのフィードバックをお待ちしています。使いにくい点、見つけられなかった情報、回避策が必要だったことをお知らせください。[フィードバック](https://docs.comfy.org/ja/development/api-development/sdks#%E3%83%95%E3%82%A3%E3%83%BC%E3%83%89%E3%83%90%E3%83%83%E3%82%AF)を参照してください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/api-development/sdks-design.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/api-development/sdks-design)

[Request cancellation前へ](https://docs.comfy.org/ja/api-reference/v2/jobs/request-cancellation)[ワークフロー API 形式次へ](https://docs.comfy.org/ja/development/api-development/workflow-api-format)

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
