---
url: https://docs.comfy.org/ja/tutorials/partner-nodes/faq/
title: \u30d1\u30fc\u30c8\u30ca\u30fc \u30ce\u30fc\u30c9\u306b\u95a2\u3059\u308b\u3088\u304f\u3042\u308b\u8cea\u554f - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:35.765195+00:00
---

# パートナー ノードに関するよくある質問 - ComfyUI

> Source: https://docs.comfy.org/ja/tutorials/partner-nodes/faq/

パートナーノード

# パートナー ノードに関するよくある質問

ページをコピーページをコピー

ComfyUI パートナーノードに関するよくある質問：クレジットと請求、ログイン要件、コンテンツモデレーション、アカウント削除について解説します。

ページをコピーページをコピー

この記事では、パートナー ノードの使用に関する一般的な質問について説明します。

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

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/tutorials/partner-nodes/faq.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/tutorials/partner-nodes/faq)

[同時実行制限前へ](https://docs.comfy.org/ja/tutorials/partner-nodes/concurrency-limits)[パートナーノードのデータ保持次へ](https://docs.comfy.org/ja/tutorials/partner-nodes/data-retention)

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
