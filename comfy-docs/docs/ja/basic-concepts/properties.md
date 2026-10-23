---
url: https://docs.comfy.org/ja/basic-concepts/properties/
title: ComfyUI \u30d7\u30ed\u30d1\u30c6\u30a3\uff1a\u30a6\u30a3\u30b8\u30a7\u30c3\u30c8\u3001\u5165\u529b\u3001\u30c7\u30fc\u30bf\u578b - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:30.988285+00:00
---

# ComfyUI プロパティ：ウィジェット、入力、データ型 - ComfyUI

> Source: https://docs.comfy.org/ja/basic-concepts/properties/

## このページの内容

  * ノードはプロパティのコンテナです
  * データ型



基本概念

# ComfyUI プロパティ：ウィジェット、入力、データ型

ページをコピーページをコピー

ComfyUI のノードプロパティの仕組みを学びます。手動操作用のウィジェット、接続用の入力スロット、ノードグラフを成立させるデータ型を解説します。

ページをコピーページをコピー

## 

​

ノードはプロパティのコンテナです

ノード通常は _**プロパティ**_ を持っています。 _**パラメータ**_ または _**属性**_ とも呼ばれるノードプロパティは、変更可能な変数です。一部のプロパティは、 _**ウィジェット**_ と呼ばれるデータ入力フィールドを使用して、ユーザーが手動で調整できます。他のプロパティは、プロパティの _**入力スロット**_ またはポートに接続された他のノードによって自動的に駆動されます。通常、プロパティはウィジェットから入力へ、またその逆へ変換でき、ユーザーがプロパティ値を手動または自動的に制御できるようになります。 プロパティは多くの形式を取り、多くの異なる種類の情報を保持できます。例えば、**Load Checkpoint** ノードには単一のプロパティがあります：生成モデルチェックポイントファイルへのファイルパスです。**KSampler** ノードには、サンプリング**ステップ数** 、**CFG** スケール、**サンプラー名** などの複数のプロパティがあります。 ![ノードプロパティ](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2121d646aef4f1386f1f09162312785b)

## 

​

データ型

情報は _**データ型**_ と呼ばれる多くの異なる形式で存在できます。例えば、英数字テキストは _**文字列**_ として知られ、整数は _**整数**_ 、小数点を含む数字は _**浮動小数点数**_ または _**浮動小数**_ として知られています。新しいデータ型は常に ComfyUI に追加されています。 ComfyUI は Python スクリプト言語で書かれており、データ型について非常に寛容です。対照的に、ComfyUI 環境は非常に _**強い型付け**_ です。これは、異なるデータ型を混在させることができないことを意味します。例えば、画像出力を整数入力に接続することはできません。これはユーザーにとって大きな利点であり、適切なワークフロー構築をガイドし、プログラムエラーを防ぎます。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/basic-concepts/properties.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/basic-concepts/properties)

[カスタムノード前へ](https://docs.comfy.org/ja/basic-concepts/custom-nodes)[ComfyUI リンク：ノード接続の仕組み次へ](https://docs.comfy.org/ja/basic-concepts/links)

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
