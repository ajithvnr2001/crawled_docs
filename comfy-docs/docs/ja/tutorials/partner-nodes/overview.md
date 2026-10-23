---
url: https://docs.comfy.org/ja/tutorials/partner-nodes/overview/
title: \u30d1\u30fc\u30c8\u30ca\u30fc \u30ce\u30fc\u30c9 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:34.087648+00:00
---

# パートナー ノード - ComfyUI

> Source: https://docs.comfy.org/ja/tutorials/partner-nodes/overview/

## このページの内容

  * パートナー ノードとは？
  * Partner Nodes を使用するための前提条件
    * 1\. ComfyUI のバージョン要件
    * 2\. アカウントおよびクレジット要件
    * 3\. ネットワーク環境要件
    * 4\. 対応するノードの使用方法
  * 非ホワイトリスト登録サイトでの ComfyUI アカウント API キーによるログイン
  * 有料モデルのパートナー ノードを呼び出すための ComfyUI アカウント API キー統合の利用
  * パートナー ノードの利点
  * 料金体系
  * モデルプロバイダー
  * オープンソースおよびオプトインについて
  * パートナー ノードを完全に無効化する方法
  * 利用例
  * よくある質問



パートナーノード

# パートナー ノード

ページをコピーページをコピー

Partner Nodes は ComfyUI 内の API リクエストを通じて OpenAI、Kling、Luma などのクローズドソースモデルを呼び出します。概要、クレジット、使い方を解説。

ページをコピーページをコピー

パートナー ノードは、API リクエストを介してクローズドソースのモデルを呼び出す ComfyUI の新しい方法であり、複雑な API キー設定を必要とせずに、ComfyUI ユーザーが外部の最先端 AI モデルにアクセスできるようにします。

## 

​

パートナー ノードとは？

パートナー ノードは、外部 API サービスに接続する特殊なノードのセットであり、ComfyUI のワークフロー内で直接、クローズドソースまたはサードパーティがホストする AI モデルを使用できるようにします。これらのノードは、ComfyUI コアのオープンソースという性質を維持しつつ、外部モデルの機能をシームレスに統合することを目的として設計されています。

## 

​

Partner Nodes を使用するための前提条件

Partner Nodes を使用するには、以下の要件を満たす必要があります。

### 

​

1\. ComfyUI のバージョン要件

今後、より多くの API 機能を追加する予定であるため、ComfyUI を最新版に更新してください。これに伴い、対応するノードも随時更新されますので、常に ComfyUI を最新状態に保つようお願いします。

`nightly` バージョン（最新のコードコミット）と `release` バージョン（安定版）の違いにご注意ください。当社では、`release` バージョンがタイムリーに更新されない可能性があるため、`nightly` バージョンの利用を推奨しています。  
これは、開発版と安定版の違いを意味します。当社は現在も急速なイテレーションを続けており、本ドキュメントが即時に更新されない場合がありますので、バージョンの差異には十分ご留意ください。

### 

​

2\. アカウントおよびクレジット要件

[Comfy アカウント](https://docs.comfy.org/ja/interface/user) で ComfyUI にログイン済みであり、かつ [クレジット](https://docs.comfy.org/ja/interface/credits) 残高が 0 より大きい必要があります。 ログインは `設定` → `ユーザー` から行います： ![ComfyUI ユーザーインターフェース](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/user.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4aacfc636460e073d16ef1fdaccb0888) クレジットの購入は `設定` → `クレジット` から行えます： ![クレジットインターフェース](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/setting/purchase-1.jpg?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=d4371030bb5549d08feb37abd8ae19fb) この要件を確認するため、以下の関連ドキュメントをご参照ください：

  * [Comfy アカウント](https://docs.comfy.org/ja/interface/user)：設定メニュー内の `ユーザー` セクションからログインできます。
  * [クレジット](https://docs.comfy.org/ja/interface/credits)：ログイン後に設定インターフェースにクレジットメニューが表示され、そこからクレジットを購入できます。当社は事前支払い方式を採用しているため、予期しない課金は発生しません。



### 

​

3\. ネットワーク環境要件

API へのアクセスには、安全なネットワーク環境下でのリクエストが必要です。現在の API アクセス要件は以下の通りです：

  * ローカルネットワーク（`127.0.0.1` または `localhost`）からのアクセスのみ許可されており、その場合は直接ログイン機能を利用できます。
  * ローカルエリアネットワーク（LAN）やホワイトリストに登録されていないウェブサイトからのアクセスの場合は、API キーによるログインをお使いください。詳しくは [API キーによるログイン](https://docs.comfy.org/ja/interface/user#api-key-%E3%81%A7%E3%81%AE%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3) をご参照ください。
  * 当社の API サービスに正常にアクセスできる必要があります（一部の地域ではプロキシサービスの利用が必要になる場合があります）。
  * 要求の安全性を確保するため、`https` 環境下でのアクセスが必須です。



不安全なコンテキスト（HTTP など）からのアクセスには重大なリスクが伴い、以下のような結果を招く可能性があります：

  1. 認証情報が盗まれ、アカウント情報が漏洩する。
  2. アカウントが悪意ある目的で不正利用され、金銭的損失を被る。

将来的にこの制限を緩和したとしても、極めて高いリスクを伴うため、不安全なネットワーク経由での API サービスへのアクセスは強く推奨しません。

### 

​

4\. 対応するノードの使用方法

**ワークフローへの追加** ：他のノードと同様に、API ノードをワークフローに追加します。  
**実行** ：パラメーターを設定し、ワークフローを実行します。 ![Partner Nodes](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/tutorial/api_nodes/sidebar.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=5adc8f697864ac7d890722dddbb8260c)

## 

​

非ホワイトリスト登録サイトでの ComfyUI アカウント API キーによるログイン

現在、ComfyUI アカウントへのログインが許可されるウェブサイトを制限するためにホワイトリストが設定されています。  
一部の非ホワイトリスト登録サイトで ComfyUI アカウントにログインする必要がある場合は、アカウント管理セクションを参照し、API キーを用いたログイン方法をご確認ください。この場合、対象のウェブサイトが当社のホワイトリストに登録されている必要はありません。

## アカウント管理

ComfyUI アカウント API キーによるログイン方法を学ぶ

![Comfy API キーによるログインを選択](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdb8d99a4bd52a6cc1de1b3453e8cfda)

## 

​

有料モデルのパートナー ノードを呼び出すための ComfyUI アカウント API キー統合の利用

現在、ComfyUI アカウント API キー統合を介して当社のサービスにアクセスし、有料モデルのパートナー ノードを呼び出すことをサポートしています。有料モデルのパートナー ノードを呼び出すために API キー統合を利用する方法については、API キー統合セクションをご参照ください。

**重要:** ここで言及する API キーは、ワークフロー内で有料のパートナー ノードにアクセスするために使用される **ComfyUI アカウント API キー** です。これは、開発者がカスタム ノードをレジストリに公開するために使用する **レジストリ公開用 API キー** とは異なります。カスタム ノードの公開をお考えの場合は、[ノードの公開](https://docs.comfy.org/ja/registry/publishing) をご覧ください。

## API キー統合

有料モデルのパートナー ノードを呼び出すために API キー統合を利用する方法については、API キー統合セクションをご参照ください

## 

​

パートナー ノードの利点

パートナー ノードは、ComfyUI ユーザーにとって以下の重要な利点を提供します：

  * **クローズドソース モデルへのアクセス** : 自身でデプロイすることなく、最先端の AI モデルを利用可能
  * **シームレスな統合** : パートナー ノードは他の ComfyUI ノードと完全に互換性があり、複雑なワークフローを作成するために組み合わせることが可能
  * **簡素化された体験** : API キーの管理や複雑な API リクエストの処理が不要
  * **コストのコントロール** : プレペイド方式により、予期しない課金を防ぎ、支出を完全に管理可能



## 

​

料金体系

## パートナー ノードの料金

対応するパートナー ノードの料金については、料金ページをご参照ください

## 

​

モデルプロバイダー

## モデルプロバイダー

パートナー ノードで使用されるモデル プロバイダーの検証状況、商用ライセンス、データ所在地を確認できます

## 

​

オープンソースおよびオプトインについて

**パートナー ノードは完全に任意の機能である** ことに注意してください。ComfyUI は今後も常に完全にオープンソースであり、ローカルユーザーには無料で提供されます。パートナー ノードは「オプトイン」機能として設計されており、外部の SOTA（State-of-the-Art：最先端）モデルにアクセスしたいユーザーに利便性を提供します。

## 

​

パートナー ノードを完全に無効化する方法

ComfyUI ですべてのパートナー ノードを無効化するには、起動引数 `--disable-partner-nodes` を追加します。フロントエンドのインターネット通信も防止したい場合は、代わりに `--offline` を使用してください。 **手動インストールの場合:**
    
    
    python main.py --disable-partner-nodes
    

**ポータブル版ユーザー（Windows）の場合:** `run_xxx.bat` ファイルを更新してください：
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build --disable-partner-nodes
    pause
    

## 

​

利用例

パートナー ノードの強力な応用例の一つは、外部モデルの出力をローカルのノードと組み合わせることです。例えば：

  * GPT-Image-1 を使用してベース画像を生成し、その後、ローカルの `wan` ノードで動画に変換する
  * 外部で生成された画像とローカルのアップスケーリングやスタイル変換ノードを組み合わせる
  * クローズドソースおよびオープンソースの両方のモデルの長所を活かしたハイブリッドワークフローを作成する

このような柔軟性により、ComfyUI は真に汎用的な生成AIインターフェースとなり、さまざまなAI機能を統一されたワークフローに統合し、さらに多くの可能性を開きます。

## 

​

よくある質問

パートナーノードが見つからないのはなぜですか？

ComfyUIを最新版（最新のコミット、または最新の[デスクトップ版](https://www.comfy.org/download)）に更新してください。今後、より多くのAPI対応を追加する予定であり、それに伴って対応するノードも更新されます。そのため、ComfyUIは常に最新版をご利用ください。

nightly版とrelease版を区別する必要があります。場合によっては、最新の`release`版が`nightly`版と比較して更新が間に合っていないことがあります。現在も急速に開発を進めているため、該当するノードが見つからない場合は、最新版を使用していることを確認してください。

パートナーノードが使用できない／ログインできないのはなぜですか？

APIへのアクセスには、現在のリクエストがセキュアなネットワーク環境に基づいている必要があります。現在のAPIアクセス要件は以下の通りです：

  * ローカルネットワークでは、`127.0.0.1`または`localhost`からのアクセスのみ許可されています。このため、LAN環境で`--listen`パラメータを指定して起動したComfyUIサービス上では、パートナーノードを使用できない可能性があります。
  * 当社のAPIサービスに正常にアクセスできること（一部地域ではプロキシサービスが必要となる場合があります）。
  * アカウントに十分な[クレジット](https://docs.comfy.org/ja/interface/credits)が残っていること。



ログイン済みにもかかわらずパートナーノードが使用できない、または使用中に何度もログインを要求されるのはなぜですか？

  * 現在は`127.0.0.1`または`localhost`からのアクセスのみ対応しています。
  * アカウントに十分なクレジットがあることを確認してください。



パートナーノードは無料で使用できますか？

パートナーノードは、クローズドソースモデルへのAPI呼び出しにクレジットを必要とするため、無料での使用はサポートされていません。

クレジットの購入方法を教えてください

以下のドキュメントをご参照ください：

  1. [Comfyアカウント](https://docs.comfy.org/ja/interface/user)：設定メニュー内の「ユーザー」セクションからログインできます。
  2. [クレジット](https://docs.comfy.org/ja/interface/credits)：ログイン後、設定インターフェースにクレジットメニューが表示されます。「設定」→「クレジット」からクレジットを購入できます。当社はプリペイド方式を採用しており、予期せぬ課金は発生しません。
  3. Stripeを通じて支払いを完了します。
  4. クレジットが更新されたか確認してください。更新されていない場合は、アプリケーションの再起動またはページの再読み込みをお試しください。



未使用のクレジットは返金可能ですか？

現在、クレジットの返金はサポートしていません。  
技術的な問題により、未使用の残高が発生したとお考えの場合は、[サポートチーム](mailto:support@comfy.org)までお問い合わせください。

クレジットがマイナスになることはありますか？

クレジットは負の残高や信用枠として使用することを想定していません。ただし、パートナーノードが実行前にコストを報告しない場合があるため、競合状態（race condition）が発生し、単一の実行で残高を超えるクレジットが消費され、実行完了後に一時的に負の残高になることがあります。残高がマイナスになると、クレジットを追加して正の残高に戻すまでパートナーノードを実行できません。API呼び出しを行う前に、十分なクレジットを確保してください。

使用量および費用はどこで確認できますか？

ログイン後に[クレジット](https://docs.comfy.org/ja/interface/credits)メニューへアクセスし、対応するクレジット情報をご確認ください。

独自のAPIキーを使用できますか？

現在、パートナーノードはテスト段階であり、この機能はまだサポートされていませんが、将来的な実装を検討しています。

クレジットは有効期限がありますか？

はい、有効期限はクレジットの種類によって異なります：

  * **月額クレジット** ：請求期間の終了時に失効します。
  * **チャージクレジット** ：購入日から1年間有効です。



クレジットは譲渡・共有できますか？

いいえ、クレジットは他のユーザーへの譲渡はできず、現在ログイン中のアカウントでのみ使用可能です。ただし、ログイン可能なデバイス数には制限を設けていません。

異なるデバイスで同じアカウントを使用できますか？

ログイン可能なデバイス数には制限を設けていませんので、ご希望の場所でいつでもアカウントをご利用いただけます。

アカウントまたは個人情報の削除を依頼するにはどうすればよいですか？

[support@comfy.org](mailto:support@comfy.org) 宛てにメールにてご依頼ください。その後、お客様の情報を削除いたします。

パートナーノードにコンテンツモデレーションはありますか？

パートナーノードは、あなたの入力（プロンプト、画像、その他のコンテンツ）をサードパーティプロバイダーに送信して処理します。これらのプロバイダーは独自のコンテンツモデレーションポリシーを適用します。パートナーノードにNSFWやその他の禁止コンテンツを送信しないでください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/tutorials/partner-nodes/overview.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/tutorials/partner-nodes/overview)

[Comfy Cloud ノード前へ](https://docs.comfy.org/ja/cloud-nodes/overview)[Partner Node 価格次へ](https://docs.comfy.org/ja/tutorials/partner-nodes/pricing)

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
