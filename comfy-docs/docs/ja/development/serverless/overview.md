---
url: https://docs.comfy.org/ja/development/serverless/overview/
title: Comfy API\uff1a\u30b5\u30fc\u30d0\u30fc\u30ec\u30b9\u30c7\u30d7\u30ed\u30a4 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:50.786051+00:00
---

# Comfy API：サーバーレスデプロイ - ComfyUI

> Source: https://docs.comfy.org/ja/development/serverless/overview/

## このページの内容

  * プラットフォームの用語
  * ビルドファイル
  * 更新とリリース
  * リージョンと GPU の可用性
  * ワークスペースの制限
  * デプロイの監視と呼び出し
  * デプロイメントの運用
  * 検査とクリーンアップ
  * FAQ
  * 次のステップ



ワークフローの実行

# Comfy API：サーバーレスデプロイ

ページをコピーページをコピー

バージョン管理された ComfyUI 環境を構築し、マネージドエンドポイントとしてデプロイして、API 経由でワークフローを実行します。

ページをコピーページをコピー

Comfy API を使うと、アプリケーションからマネージドエンドポイント経由で ComfyUI ワークフローを実行できます。ワークフローに必要な ComfyUI のバージョン、モデル、カスタムノード、依存関係をパッケージ化すると、Comfy がマネージド GPU 上で実行します。環境を再現可能に保ち、アプリケーションから呼び出せるエンドポイントが必要な場合に使います。

## 

​

プラットフォームの用語

用語| 意味  
---|---  
**ワークスペース**|  メンバー、Build、デプロイ、使用上限を管理するチームアカウントです。  
**Build**|  ComfyUI のバージョン、モデル、カスタムノード、依存関係を含む環境定義です。  
**Build バージョン / リリース**| `linux/nvidia` など、デプロイターゲット向けに用意された番号付きの Build です。  
**デプロイ**|  リリースを実行するエンドポイントです。GPU、リージョン、ワーカー設定を持ちます。  
  
[Comfy Cloud](https://docs.comfy.org/ja/development/deploy/cloud) でサポートされるワークフローは、Build やデプロイを作成せずに実行できます。

## Comfy API クイックスタート

エージェントから始めるか、環境やワークフローを用意する別の方法を選んでください。

デスクトップのスナップショットとワークフロー JSON のインポートについては、[Build Sources](https://docs.comfy.org/ja/development/serverless/build-sources) を参照してください。

## 

​

ビルドファイル

`comfy-build.yaml` は Build 定義と最後に確認したリモートの状態を保存します。CLI はその状態を使って、リモートの Build が変更されたかどうかを検出します。このファイルはプロジェクトと一緒に管理してください。環境を記述するものであり、モデルファイルは含みません。 変更をプッシュする前に、ローカルの Build がインストール済みの内容やリモートのバージョンとどう違うかを確認します：
    
    
    comfy build status
    

## 

​

更新とリリース

ローカルのインストールを変更した後は、Build 定義を更新します：
    
    
    comfy build update --yes
    

既存の Build から別のリリースを作成するには、サポートされているターゲットを確認して 1 つ選択します：
    
    
    comfy build refs build-targets
    comfy build release create --target linux/nvidia --watch
    

1 つのリリースのビルドログを追うには：
    
    
    comfy build release logs rel_123456 --target linux/nvidia --follow
    

## 

​

リージョンと GPU の可用性

リージョンのキャパシティは変化するため、デプロイ先を選ぶ際はプラットフォームのカタログを確認してください。結果は `--region <region>` でフィルタします:
    
    
    comfy deploy refs compute --region <region>
    

デプロイ時に各リージョンでどの GPU クラスが利用可能かについては、カタログがソースオブトゥルースとなります。

## 

​

ワークスペースの制限

ワークスペースの使用量とプランの上限については、[制限](https://platform.comfy.org/profile/limits)を参照してください。`--max` はデプロイメントごとのワーカー上限内に収めてください。

## 

​

デプロイの監視と呼び出し

`--min` と `--max` オプションはワーカーの下限と上限を設定します。デプロイのヘルス、リリースの最新性、サービングのアクティビティを追跡するには、`comfy deploy status --watch` を実行します。 [Comfy SDK](https://docs.comfy.org/ja/development/api-development/sdks) を使用してエンドポイントを呼び出すこともできます。`COMFY_BASE_URL` にデプロイの URL を設定し、APIキーを指定します。詳細は[ベース URL の選択](https://docs.comfy.org/ja/development/api-development/sdks#%E3%83%99%E3%83%BC%E3%82%B9url%E3%81%AE%E9%81%B8%E6%8A%9E)を参照してください。

## 

​

デプロイメントの運用
    
    
    # ワーカーの下限と上限を変更する
    comfy deploy scale --deployment dep_123456 --min 2 --max 5
    
    # デプロイメントの記録を保持したまま一時停止または再開する
    comfy deploy stop --deployment dep_123456
    comfy deploy start --deployment dep_123456
    

## 

​

検査とクリーンアップ
    
    
    # ビルドの状態
    comfy build ls
    comfy build show --id bld_123456
    comfy build release ls
    comfy build release show rel_123456
    
    # デプロイメントの状態
    comfy deploy ls --workspace --status ready
    comfy deploy logs --deployment dep_123456
    comfy deploy events --deployment dep_123456
    

デプロイメントの削除とビルドの削除は、それぞれ別個の不可逆的な操作です。`comfy deploy delete --yes` または `comfy build delete --id bld_123456 --yes` を使用する前に、対象を確認してください。

## 

​

FAQ

1 つの Build を複数のワークフローから作成できますか？

はい。Builder では、1 つ以上のワークフローをアップロードして、そのモデルとカスタムノードをあらかじめ選択できます。実行する予定のすべてのワークフローが必要とする依存関係を含めてから、各 API フォーマットのワークフローをデプロイ済みのエンドポイントに送信します。各デプロイメントは 1 つの GPU タイプを使用します。異なる GPU タイプでワークフローを実行するには、同じ Build のデプロイメントを別々に作成します。

デプロイしていない Build の保存に料金はかかりますか？

いいえ。Build とそのリリースは、アカウントに無料で保存されます。デプロイするまで、Build のストレージ使用量に対して課金されることはありません。ストレージの課金はデプロイメントから始まります：

  * リリースをデプロイすると、そのモデルはデプロイメントのワーカー間で共有されるネットワークストレージに配置されます。このストレージはデプロイ後は読み取り専用となり、そのリージョンにその Build のデプロイメントが存在する限り、`comfy deploy stop` でデプロイメントが一時停止している間も含めて、GB 月単位で課金されます。
  * 各ワーカーには固定 50 GB のコンテナディスクも割り当てられます。これはエフェメラルであり、ワーカーのコンピュートコストの一部として、ワーカーの実行中のみ課金されます。
  * デプロイメントを削除すると、そのコンピュートが解放されます。配置されたネットワークストレージは、そのリージョンでそれを使用している最後のデプロイメントが削除された直後にクリーンアップされ、その課金も終了します。

現在のストレージ料金については、[Comfy 料金ページ](https://www.comfy.org/pricing)をご覧ください。コンピュートカタログ（`comfy deploy refs compute`）とデプロイダイアログにも、デプロイメントに適用される料金が表示されます。

アクティブワーカーはどのように課金され、時間単価はいくらですか？

`--min` は**アクティブワーカー** の数を設定します。アクティブワーカーとは、常に実行し続けるワーカーであり、リクエストがコールドスタートを待つことはありません。アクティブワーカーは、ジョブを処理しているかどうかに関係なく、実行している間ずっと秒単位で課金されます。`--min` を超えて `--max` までのワーカーは**フレックスワーカー** です。フレックスワーカーは、起動した瞬間（起動とモデルの読み込みを含む）からジョブの処理を経て、スケールダウンする前の短いアイドルウィンドウ（現在は 30 秒）まで、秒単位で課金されます。フレックスワーカーがスケールダウンされると、コストはかかりません。`--min 0` の場合、デプロイメント全体がゼロにスケールし、アイドル中はコンピュートの課金が発生しませんが、最初のリクエストでコールドスタートが発生します。課金は、実際のワーカーの秒単位の使用量に、実行中のワーカー数を掛けて計測されます。ワークスペースのクレジットが不足すると、デプロイメントは自動的に停止されます。現在のワーカーあたりの GPU 料金については、[Comfy 料金ページ](https://www.comfy.org/pricing)をご覧ください。料金はワーカー時間あたりで提示され、秒単位で課金されます。リージョンごとの GPU の可用性はコンピュートカタログから取得できます。現在のリストを確認するには `comfy deploy refs compute` を実行してください。

デプロイメントは複数のリクエストをどのように処理しますか？

デプロイメントは、リクエストをワーカー間で自動的に分散し、設定された `--min` と `--max` の範囲内でスケールします。すぐに実行できないリクエストはキューに入り、ワーカーのキャパシティが空き次第処理されます。

プロビジョニングに時間がかかる場合はどうすればよいですか？

デプロイメントの状態を確認し、次にそのログとイベントを調べて原因を特定します：
    
    
    comfy deploy status --deployment <deployment-id> --watch
    comfy deploy logs --deployment <deployment-id>
    comfy deploy events --deployment <deployment-id>
    

選択した GPU またはリージョンにキャパシティがない場合は、後で再試行するか、`comfy deploy refs compute` を実行して利用可能なリージョンと GPU のペアを選択してください。サポートを依頼する際は、Build、リリース、デプロイメントの ID を添えてください。

デプロイメントを削除するとどうなりますか？

デプロイメントを削除すると、そのエンドポイントが削除され、コンピュートが解放されます。Build やそのリリースは削除されません。あるリージョンでその Build を使用する最後のデプロイメントを削除すると、配置されたネットワークストレージはクリーンアップされ、その後まもなくストレージの課金が終了します。Build の削除は別の操作です：`comfy build delete --id <build-id> --yes`。

## 

​

次のステップ

## Comfy SDKs

Python または TypeScript のアプリから使用して、ワークフローを送信し、入力、進行状況、出力を処理します。

## Comfy API v2

HTTP API を直接呼び出す場合や、そのリクエストとレスポンスの形式を確認する場合に、任意の言語から使用します。

## ワークフロー API 形式

API リクエスト用のワークフロー JSON を準備するときや、その入力と出力をトラブルシューティングするときに使用します。

## Comfy CLI リファレンス

ターミナルから Build、リリース、デプロイメント、ワークフローのコマンドを自動化するために使用します。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/serverless/overview.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/serverless/overview)

[セルフホスト ComfyUI 用の API プロキシ前へ](https://docs.comfy.org/ja/development/comfyui-server/api-proxy)[API キーの取得次へ](https://docs.comfy.org/ja/development/api-development/getting-an-api-key)

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
