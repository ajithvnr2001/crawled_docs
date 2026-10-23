---
url: https://docs.comfy.org/ja/basic-concepts/workflow/
title: ComfyUI \u30ef\u30fc\u30af\u30d5\u30ed\u30fc\uff1a\u30ce\u30fc\u30c9\u3001\u30ea\u30f3\u30af\u3001\u30d3\u30b8\u30e5\u30a2\u30eb\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:28.700620+00:00
---

# ComfyUI ワークフロー：ノード、リンク、ビジュアルプログラミング - ComfyUI

> Source: https://docs.comfy.org/ja/basic-concepts/workflow/

## このページの内容

  * ワークフローとは？
  * ノードはステップです
  * リンクはノード間でデータを渡す
  * プロパティが各ステップを制御します
  * ワークフローの実行
  * テンプレートからはじめる
  * ワークフローの保存と共有
  * 背景について



基本概念

# ComfyUI ワークフロー：ノード、リンク、ビジュアルプログラミング

ページをコピーページをコピー

ComfyUI におけるワークフローとは、接続されたノードのグラフで、画像・動画・音声・3D を生成できます。ノード、リンク、JSON での保存方法を解説します。

ページをコピーページをコピー

## 

​

ワークフローとは？

ワークフローとは、ComfyUI に何かの作成方法を指示する一連のステップです。 ワークフローをレシピのように考えることができます：

  * レシピがワークフローです。
  * レシピの各手順がノードです。
  * 材料には、プロンプト、画像、モデルが含まれます。
  * 結果は、生成済みの画像、ビデオ、オーディオ、またはその他の出力です。

たとえば、シンプルな画像ワークフローでは、次のような手順になります：

  1. モデルを読み込む。
  2. テキストプロンプトを読み取る。
  3. 画像を生成する。
  4. 画像を保存する。

ComfyUI は、これらのステップをキャンバス上のボックスとして表示します。 ![シンプルな ComfyUI ワークフロー](https://mintcdn.com/dripart/7m9lukFrTCZs7Mhj/images/simple_workflow.jpg?fit=max&auto=format&n=7m9lukFrTCZs7Mhj&q=85&s=b3f3e488389463fbddef9a9e45c50eac)

## 

​

ノードはステップです

ノードは、特定の1つのジョブを実行します。ファイルを読み込むノードもあれば、データを変更するノードもあり、結果を生成または保存するノードもあります。 例：

  * **Load Checkpoint** ノードは、AIモデルを読み込みます。
  * **CLIP Text Encode** ノードは、プロンプトをモデルへの指示に変換します。
  * **KSampler** ノードは、モデルとその指示から画像を生成します。
  * **Save Image** ノードは、結果をコンピュータに保存します。

ノードをさまざまな方法で組み合わせて、異なるワークフローを作成できます。ノードを使用するためにコードを書く必要はありません。 ノードの詳細については、[ノード](https://docs.comfy.org/ja/basic-concepts/nodes) で学べます。

## 

​

リンクはノード間でデータを渡す

ノードは、あるノードから別のノードへデータを渡すことで連携します。リンクは、あるノードの出力を別のノードの入力に接続します。 例えば、**チェックポイントを読み込む** ノードで読み込んだモデルは、**KSampler** ノードに渡すことができます。テキストエンコードノードで作成されたテキスト指示も、サンプラーに渡すことができます。 接続できるのは、互換性のあるデータ型のみです。例えば、画像出力を数値を想定した入力に直接接続することはできません。 リンクの詳細を学ぶには、[リンク](https://docs.comfy.org/ja/basic-concepts/links)をご覧ください。

## 

​

プロパティが各ステップを制御します

ノードにはプロパティが含まれています。プロパティは、ノードの動作を制御する設定です。 たとえば、サンプラーノードには以下のようなプロパティがあります：

  * ステップ数
  * ガイダンススケール
  * サンプリング方法
  * 画像サイズ

通常、ノード上で直接プロパティを設定できます。一部のプロパティは、別のノードから値を受け取ることもできます。 プロパティの詳細については、[プロパティ](https://docs.comfy.org/ja/basic-concepts/properties) をご覧ください。

## 

​

ワークフローの実行

ワークフローを実行すると、ComfyUI は必須ノードを実行し、リンクを通じてデータを渡します。ワークフローは最終出力を生成するまで続行されます。 ノードが不足している、エラーが発生している、または必要なデータを受信できない場合、ComfyUI はワークフローを完了できません。問題を発見して修正できるように、ノードにはマークが付けられます。

## 

​

テンプレートからはじめる

はじめるには、**ワークフロー** → **ワークフローテンプレートをブラウズ** を選択し、組み込みのワークフローテンプレートを開きます。テンプレートには、実行して編集できる完全な例が用意されています。 テンプレートは、ComfyUI に含まれるコアノードを使用します。また、必要なモデルがあれば、そのダウンロードを促します。 コミュニティは、さらに多くの機能を追加するカスタムノードを多数作成しています。詳細は[カスタムノード](https://docs.comfy.org/ja/basic-concepts/custom-nodes)で学ぶことができます。

## 

​

ワークフローの保存と共有

ワークフローをJSONファイルとして保存し、生成済みメディアとは独立して共有できます。 組み込みの保存ノードで出力を保存すると、ComfyUIはワークフローを出力ファイル内にも保存できます。その後、ファイルをキャンバスにドラッグして戻すことで、ワークフローを復元できます。 埋め込みデータ、対応ファイル形式、プログラムによるアクセスの詳細については、[ワークフローメタデータ](https://docs.comfy.org/ja/development/api-development/workflow-metadata)を参照してください。

## 

​

背景について

技術的には、ワークフローはノードグラフです。ノードはグラフ内のポイントであり、リンクはデータがノード間をどのように移動するかを示します。 これはビジュアルプログラミングとも呼ばれます。コードを書く代わりに、視覚的なブロックを配置して接続することでプログラムを作成するからです。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/basic-concepts/workflow.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/basic-concepts/workflow)

[コーディングエージェント向け Comfy Skills前へ](https://docs.comfy.org/ja/agent-tools/skills)[ComfyUI ノード：種類、入力、出力次へ](https://docs.comfy.org/ja/basic-concepts/nodes)

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
