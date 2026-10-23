---
url: https://docs.comfy.org/ja/basic-concepts/links/
title: ComfyUI \u30ea\u30f3\u30af\uff1a\u30ce\u30fc\u30c9\u63a5\u7d9a\u306e\u4ed5\u7d44\u307f - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:32.143968+00:00
---

# ComfyUI リンク：ノード接続の仕組み - ComfyUI

> Source: https://docs.comfy.org/ja/basic-concepts/links/

## このページの内容

  * ノードを接続するリンク
    * リルートノード
  * 色分け



基本概念

# ComfyUI リンク：ノード接続の仕組み

ページをコピーページをコピー

ComfyUI でノードをつなぐリンクの仕組み、リンクの表示スタイルの変更方法、複雑なワークフローを整理する Reroute ノードの使い方を解説します。

ページをコピーページをコピー

## 

​

ノードを接続するリンク

ComfyUI では、ノード間に引かれる線や曲線は _**リンク**_ と呼ばれます（ _**接続**_ やワイヤーとも呼ばれます）。これらは、あるノードの出力から別のノードの入力へデータを運び、ワークフローの流れを定義します。 リンクは、曲線、直角、直線、または完全に非表示など、いくつかの視覚的スタイルで表示できます。 ![リンクスタイル](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/link_styles.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=1d678959a9c5bd80d68231d5b6fed78d) リンクスタイルを変更するには、**設定メニュー** → **表示 (Lite Graph)** → **グラフ** → **リンクレンダーモード** に移動します。 ![レンダリングモード設定](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/render_mode.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=25d9de19b526f8ec618a9b5e9ed87ed9) **キャンバスメニュー** からすべてのリンクを一時的に非表示にすることもできます。 ![キャンバスメニュー](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/canvas_menu.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=3925615b50749cbd3f7ed8c0b320d5eb)

リンクを表示することは、学習、共有、またはワークフローのデバッグ時に特に便利です。一目でデータの流れを確認できます。編集を意図していない完成したワークフローでは、リンクを非表示にすることで視覚的な煩雑さを減らせます。

### 

​

リルートノード

ワークフローが複雑になると、リンクワイヤーが重なったりノードの背後を通ったりして、読みづらくなることがあります。**リルート** ノードを使用すると、グラフの 2D 空間内の任意のポイントを経由してワイヤーを手動で迂回させることができ、レイアウトを整理し、可読性を保つことができます。 ![ComfyUI リルートノード](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=d713aae29a8454af5a671d07e0c35ab1) ComfyUI には、グラフキャンバスに組み込みのネイティブなリルート機能もあります。新しいワークフローでは、この機能の使用をお勧めします。 ![ComfyUI ネイティブリルート](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/native_reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4d0e70a8300bdd79f2d6a623b40306f8)

## 

​

色分け

ComfyUI のすべてのデータタイプには固有の色があります。ノードの入力ポート、出力ポート、およびそれらを接続するリンクワイヤーは、すべてこの配色を共有しています。**同じ色のポート同士のみ接続できます** 。これにより、ワークフロー全体で型の安全性が確保されます。 ![ComfyUI ノードデータタイプ](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5)

データタイプ| 色  
---|---  
拡散モデル| ラベンダー  
CLIP モデル| 黄色  
VAE モデル| ローズ  
条件付け| オレンジ  
潜在画像| ピンク  
ピクセル画像| 青  
マスク| 緑  
数値（整数または浮動小数点数）| グレー  
メッシュ| 鮮緑  
  
このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/basic-concepts/links.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/basic-concepts/links)

[ComfyUI プロパティ：ウィジェット、入力、データ型前へ](https://docs.comfy.org/ja/basic-concepts/properties)[ComfyUI モデル：ファイル、フォルダ、ローダーノード次へ](https://docs.comfy.org/ja/basic-concepts/models)

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
