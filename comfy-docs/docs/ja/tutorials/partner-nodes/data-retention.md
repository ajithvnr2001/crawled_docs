---
url: https://docs.comfy.org/ja/tutorials/partner-nodes/data-retention/
title: \u30d1\u30fc\u30c8\u30ca\u30fc\u30ce\u30fc\u30c9\u306e\u30c7\u30fc\u30bf\u4fdd\u6301 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:35.860610+00:00
---

# パートナーノードのデータ保持 - ComfyUI

> Source: https://docs.comfy.org/ja/tutorials/partner-nodes/data-retention/

## このページの内容

  * 保存されるもの
  * ファイルの保持期間
  * 削除後の動作
  * ファイルを長く保持するには
  * 参考



パートナーノード

# パートナーノードのデータ保持

ページをコピーページをコピー

Comfyがパートナーノードの入力と出力を保存・削除する方法と、メディアファイルの保持期間についての説明です。

ページをコピーページをコピー

すべてのパートナーノードのリクエストは、当プラットフォームに保存されるデータ（画像、動画、3Dアセット、オーディオなどの入力、およびモデルによって生成される出力）を生成します。このページでは、各データの種類が保持される期間について説明します。各プロバイダーがこのデータをデフォルトでどこで処理するかは、[モデルプロバイダー](https://docs.comfy.org/ja/tutorials/partner-nodes/model-providers) で確認できます。

## 

​

保存されるもの

パートナーノードを実行すると、2種類のファイルが保存されます。

  * **入力ファイル** : ノードに提供する参照画像、オーディオ、その他のメディアです。入力はアカウントのストレージ領域にアップロードされます。
  * **出力ファイル** : ノードが生成する画像、動画、オーディオ、その他のメディアです。出力はComfy管理のストレージに書き込まれ、ダウンロードURLとして返されます。

入力ファイルと出力ファイルはどちらも、Comfy管理のクラウドストレージバケットに保存されます。

## 

​

ファイルの保持期間

すべてのパートナーノードのメディアファイルは、作成されてから**24時間** 後に自動的に削除されます。削除は入力ファイルと出力ファイルの両方に適用されます。

ファイルの種類| 削除時期  
---|---  
入力ファイル| 24時間  
出力ファイル| 24時間  
  
24時間の削除ウィンドウはプラットフォームのデフォルトであり、すべてのパートナーノード呼び出しに適用されます。ファイルをより長く保持する必要がある場合は、有効期限が切れる前に自分のストレージにダウンロードしてください。

## 

​

削除後の動作

ファイルが削除されると、そのダウンロードURLはエラーを返します。削除されたファイルは復元できません。再度必要になった場合は、同じメディアを再アップロードするか、再生成する必要があります。 入力ファイルを削除すると、アカウントのストレージから対応するファイルのレコードも削除されるため、その入力を後続の呼び出しで再利用することはできません。

## 

​

ファイルを長く保持するには

ワークフローで入力ファイルを24時間以上利用可能な状態に保つ必要がある場合は、各ジョブの前にファイルを再アップロードしてください。長時間実行されるパイプラインの場合は、そのファイルを必要とする呼び出しの直前に再アップロードしてください。 保持したい出力は、24時間のウィンドウ内に自分のストレージへダウンロードしてください。

## 

​

参考

項目| 値  
---|---  
入力ファイルの保持期間| 24時間  
出力ファイルの保持期間| 24時間  
  
Comfyが顧客データをどのように扱うかについての一般情報は、[データ保持](https://docs.comfy.org/ja/support/data-retention)を参照してください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/tutorials/partner-nodes/data-retention.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/tutorials/partner-nodes/data-retention)

[パートナー ノードに関するよくある質問前へ](https://docs.comfy.org/ja/tutorials/partner-nodes/faq)[モデルプロバイダー次へ](https://docs.comfy.org/ja/tutorials/partner-nodes/model-providers)

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
