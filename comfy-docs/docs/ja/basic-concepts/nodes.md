---
url: https://docs.comfy.org/ja/basic-concepts/nodes/
title: ComfyUI \u30ce\u30fc\u30c9\uff1a\u7a2e\u985e\u3001\u5165\u529b\u3001\u51fa\u529b - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:29.712983+00:00
---

# ComfyUI ノード：種類、入力、出力 - ComfyUI

> Source: https://docs.comfy.org/ja/basic-concepts/nodes/

## このページの内容

  * ノードは操作を実行する
  * 異なるノードの状態
  * ノード間の接続
    * ノードの接続と切断
  * ノードの外観
    * ノードバッジ
  * ノードのコンテキストメニュー
    * ノードのコンテキストメニュー
    * モード
    * 入力/出力のコンテキストメニュー
  * ノード選択ツールボックス
  * サブグラフ
  * カスタムノード
    * ComfyUI Manager



基本概念

# ComfyUI ノード：種類、入力、出力

ページをコピーページをコピー

ノードは ComfyUI の基本構成要素です。リンクで接続する独立した Comfy Core またはカスタムモジュールで、複雑なワークフローを組み立てます。

ページをコピーページをコピー

ComfyUI において、ノードはタスクを実行するための基本的な構成要素です。各ノードは**Comfy Core** ノードであれ**カスタムノード** であれ、それぞれが独立して構築されたモジュールであり、独自の機能を持っています。ノードはリンクを通じて相互に接続され、レゴブロックを組み立てるように複雑な機能を構築することができます。 異なるノードの組み合わせが、ComfyUI の無限の可能性を生み出します。 ![Comfy Core K-Sampler ノード](https://mintcdn.com/dripart/7m9lukFrTCZs7Mhj/images/comfy_core/sampling/k_sampler.png?fit=max&auto=format&n=7m9lukFrTCZs7Mhj&q=85&s=5bb2412a6e137d0a0b630b14845944e1) 例えば、K-Sampler ノードでは、複数の入力と出力があり、複数のパラメータ設定も含まれていることがわかります。これらのパラメータがノード実行のロジックを決定します。各ノードの背後には適切に記述された Python ロジックがあり、コードを自分で書かなくても対応する機能を実現できます。

ComfyUI は活発に開発中であるため、ここでの一部の詳細は古くなっている可能性があります。変更点に気づかれた場合は、[ドキュメントの更新にご協力ください](https://github.com/Comfy-Org/docs)。

## 

​

ノードは操作を実行する

コンピュータサイエンスにおいて、 _**ノード**_ は情報のコンテナであり、通常は何らかのタスクを実行するためのプログラムされた命令を含みます。ノードが孤立して存在することはほとんどなく、ネットワーク化されたグラフ内で他のノードと接続されていることがほとんどです。ComfyUI では、ノードは互いに接続されたボックスの視覚的な形を取ります。 ComfyUI ノードは通常 _**関数演算子**_ です。これは、何らかのデータを操作して関数を実行することを意味します。関数は入力データを受け取り、それに対して何らかの操作を実行し、出力データを生成するプロセスです。つまり、ノードは何らかの作業を行い、画像生成などのタスクの完了に貢献します。したがって、ComfyUI ノードはほとんど常に少なくとも 1 つの入力または出力を持ち、通常は複数の入力と出力を持ちます。

## 

​

異なるノードの状態

![ノードの状態](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=150ab91575a7c9300b7ed20d8026e499) ComfyUI では、ノードには複数の状態があります。以下にいくつかの一般的なノードの状態を示します：

  1. **通常状態 (Normal State)** : デフォルトの状態
  2. **実行中状態 (Running State)** : 実行中の状態。通常、ワークフローの実行を開始した後、ノードが実行されているときに表示されます
  3. **エラー状態 (Error State)** : ノードエラー。通常、ワークフロー実行後にノードの入力に問題がある場合に表示され、エラーのある入力ノードが赤色でマークされます。ワークフローが正しく実行されるように、問題のある入力を修正する必要があります
  4. **欠落状態 (Missing State)** : この状態は通常、ワークフローをインポートした後に表示され、2 つの可能性があります： 
     * Comfy Core ネイティブノードの欠落：これは通常、ComfyUI が更新されたが、古いバージョンの ComfyUI を使用しているために発生します。この問題を解決するには ComfyUI を更新する必要があります
     * カスタムノードの欠落：ワークフローがサードパーティ製作者によって開発されたカスタムノードを使用していますが、ローカルの ComfyUI バージョンにこれらのカスタムノードがインストールされていません。[ComfyUI Manager](https://docs.comfy.org/ja/manager/overview) を使用して欠落ノードを見つけてインストールできます。または [カスタムノードのインストール方法](https://docs.comfy.org/ja/installation/install_custom_node) でその他の方法もご確認ください



## 

​

ノード間の接続

ComfyUI では、ノードは[リンク](https://docs.comfy.org/ja/basic-concepts/links)を通じて接続され、同じタイプのデータが異なる処理ユニット間を流れて最終結果を達成できます。 ![ComfyUI ノードリンク](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=40a62b27aa2f44cb97eae917c8c1f8da) 各ノードは何らかの入力を受け取り、そのモジュールを通じて処理し、対応する出力に変換します。異なるノード間の接続はデータタイプの要件に準拠する必要があります。ComfyUI では、異なる色を使用してノードのデータタイプを区別します。以下にいくつかの基本的なデータタイプを示します： ![ComfyUI ノードデータタイプ](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5)

データタイプ| 色  
---|---  
拡散モデル (diffusion model)| ラベンダー  
CLIP モデル| 黄色  
VAE モデル| ローズ  
条件付け (conditioning)| オレンジ  
潜在画像 (latent image)| ピンク  
ピクセル画像 (pixel image)| 青色  
マスク (mask)| 緑色  
数値 (整数または浮動小数点数)| 薄緑色  
メッシュ (mesh)| 鮮緑色  
  
ComfyUI の進化に伴い、より多くのシナリオのニーズに応えるために、より多くのデータタイプに拡張する可能性があります。

### 

​

ノードの接続と切断

![ComfyUI ノード接続](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/link_nodes.gif?s=06359a20664f48e43763696313a063f9) **接続** : 1 つのノードの出力ポイントから、別のノードの同じ色の入力にドラッグして接続します **切断** : 入力エンドポイントをクリックしてマウスの左ボタンをドラッグして切断するか、リンクの中点メニューを通じて接続をキャンセルします

## 

​

ノードの外観

![ノードの外観](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e7ed881cf2c91cc9c48892dd491cae7b) ノードの外観をカスタマイズするためのさまざまなスタイル設定を提供しています：

  * スタイルの変更
  * ノードタイトルをダブルクリックしてノード名を変更
  * 任意の角をドラッグしてノードのサイズを変更



### 

​

ノードバッジ

![ノードバッジ](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1e22b62c50745c547e2b99c5f13df990) 複数のノードバッジ表示機能を提供しています。例えば：

  * ノード ID
  * ノードソース

現在、**Comfy Core ノード** はキツネのアイコンを使用して表示され、カスタムノードはその名前を使用します。これにより、ノードがどのノードパッケージから来たかをすばやく理解できます。 メニューで対応する表示を設定できます： ![バッジ設定](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f63c9698836a1debc6a1bed84d77fdf2)

## 

​

ノードのコンテキストメニュー

ノードのコンテキストメニューは主に 2 つのタイプに分かれています：

  * ノード自体のコンテキストメニュー
  * 入力/出力のコンテキストメニュー



### 

​

ノードのコンテキストメニュー

ノードを右クリックすることで、対応するノードのコンテキストメニューを展開できます： ![ノードのコンテキストメニュー](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d7d99664537a4f2b09aaf0acc228da4f) ノードの右クリックコンテキストメニューでは、以下が可能です：

  * ノードのカラースタイルを調整
  * タイトルを変更
  * ノードをクローン、コピー、または削除
  * ノードのモードを設定

このメニューでは、外観関連の設定に加えて、以下のメニュー操作が重要です：

  * **モード (Mode)** : ノードのモードを設定：Always、Never、Bypass



#### 

​

モード

モードについては、現在提供されているものが：Always、Never、On Event、On Trigger - の 4 つのモードであることに気づくかもしれませんが、実際には**Always** と**Never** のみが有効です。**On Event** と**On Trigger** は、この機能を完全に実装していないため、現在は無効です。さらに、**Bypass** もモードとして理解できます。以下に利用可能なモードの説明を示します：

  * **Always** : デフォルトのノードモード。ノードは、初めて実行される場合、または最後の実行以降に入力のいずれかが変更された場合に実行されます
  * **Never** : ノードはいかなる状況下でも実行されず、削除されたかのように動作します。後続のノードはそこからデータを読み取ったり受け取ったりできません
  * **Bypass** : ノードはいかなる状況下でも実行されませんが、後続のノードはこのノードによって処理されていないデータを取得しようとすることができます

以下は`Never`モードと`Bypass`モードの比較です： ![Never モードと Bypass モード](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/node/never_vs_bypass.jpg?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=9adb00fa408eb3f09805030cd7a731c2) この比較例では、両方のワークフローが同時に 2 つの LoRA モデルを適用していることがわかります。違いは、一方の`Load LoRA`ノードが`Never`モードに設定され、もう一方が`Bypass`モードに設定されていることです。

  * `Never`モードに設定されたノードは、後続のノードが入力データを受け取らないため、エラーを表示します
  * `Bypass`モードに設定されたノードは、後続のノードが未処理のデータを受け取ることができるため、最初の`Load LoRA`ノードからの出力データを読み込み、後続のワークフローが正常に実行され続けます



### 

​

入力/出力のコンテキストメニュー

このコンテキストメニューは、対応する入力/出力のデータタイプと主に関連しています： ![ノード入力/出力のコンテキストメニュー](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2daf16654cdd151a6b9ace6ef9d9e530) ノードの入力/出力をドラッグする際、接続が表示されますが、他のノードの入力または出力に接続していない場合、マウスを離すと入力/出力のコンテキストメニューがポップアップ表示され、関連するタイプのノードをすばやく追加するために使用されます。 設定でノードの提案数を調整できます： ![ノード提案数](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7a063583df5825a8cc24dc13a1723761)

## 

​

ノード選択ツールボックス

**ノード選択ツールボックス (Node Selection Toolbox)** は、ノードのクイック操作を提供するフローティングツールです。ノードを選択すると、選択されたノードの上にホバーします。このツールボックスを通じて、以下が可能です：

  * ノードの色を変更
  * ノードを Bypass モードにすばやく設定（実行時に実行しない）
  * ノードをロック
  * ノードを削除

もちろん、これらの機能は対応するノードの右クリックメニューでも見つけることができます。ノード選択ツールボックスはショートカット操作を提供するだけです。この機能を無効にしたい場合は、設定でオフにできます。 ![ノード選択ツールボックスを無効化](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=60747b0e83640a2f7a4f1bc66e63a89c)

## 

​

サブグラフ

選択したノード群をひとつの再利用可能なサブグラフノードにまとめることができます。複雑なキャンバスを整理したり、同じ構造を複数のワークフローで使い回すのに便利です。

## サブグラフ

サブグラフの作成・編集、ネスト、ノードライブラリへのブループリント公開について

## 

​

カスタムノード

ComfyUI には基本インストールに多数の **Comfy Core** ノードが含まれています。コミュニティは [カスタムノードのカタログ](https://registry.comfy.org) でさまざまな用途向けの拡張ノードを公開しています。 カスタムノードのインストール方法（**ComfyUI Manager** 、Git クローン、ZIP ダウンロード、依存関係の処理、安全に関するヒントなど）の概要については、[カスタムノードのインストール方法](https://docs.comfy.org/ja/installation/install_custom_node) を参照してください。

### 

​

ComfyUI Manager

日常的なカスタムノード管理には **ComfyUI Manager** が便利です。レジストリからの検索・インストール、パッケージの更新や無効化、インポートしたワークフローの欠落ノード検出、モデルやスナップショットの管理などが行えます。デスクトップ版は通常デフォルトで有効になっています。ポータブル版や手動インストール環境では、先に有効化する手順が必要な場合があります。

## ComfyUI Manager

機能概要・有効化手順・ノードインストールのワークフロー

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/basic-concepts/nodes.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/basic-concepts/nodes)

[ComfyUI ワークフロー：ノード、リンク、ビジュアルプログラミング前へ](https://docs.comfy.org/ja/basic-concepts/workflow)[カスタムノード次へ](https://docs.comfy.org/ja/basic-concepts/custom-nodes)

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
