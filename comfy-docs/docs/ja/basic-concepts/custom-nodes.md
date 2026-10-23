---
url: https://docs.comfy.org/ja/basic-concepts/custom-nodes/
title: \u30ab\u30b9\u30bf\u30e0\u30ce\u30fc\u30c9 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:30.553670+00:00
---

# カスタムノード - ComfyUI

> Source: https://docs.comfy.org/ja/basic-concepts/custom-nodes/

## このページの内容

  * カスタムノードについて
  * カスタムノード管理
    * 1\. カスタムノードのインストール
    * 2\. ノード依存関係のインストール
    * カスタムノードバージョン管理
    * カスタムノードのアンインストール
    * カスタムノードの一時的な無効化
    * カスタムノードの依存関係の競合
  * ComfyUI Manager
    * Manager のインストール
    * 欠落ノードの検出
  * カスタムノードの開発



基本概念

# カスタムノード

ページをコピーページをコピー

ComfyUI のカスタムノード：Comfy Core ノードとの違い、およびインストール、更新、依存関係の有効化、無効化、アンインストール方法。

ページをコピーページをコピー

## 

​

カスタムノードについて

ComfyUI をインストールした後、ComfyUI にはすでに多くのノードが含まれていることに気づくでしょう。これらのネイティブノードは **Comfy Core** ノードと呼ばれ、ComfyUI 公式によってメンテナンスされています。 さらに、ComfyUI コミュニティのさまざまな作者によって作成された数多くの [**カスタムノード**](https://registry.comfy.org) があります。これらのカスタムノードは ComfyUI に広範な機能をもたらし、その機能と能力の境界を大きく拡張します。 このガイドでは、カスタムノードに関連するさまざまな操作について説明します。インストール、更新、無効化、アンインストール、依存関係のインストールなどを含みます。 誰でも ComfyUI 用の独自のカスタム拡張機能を開発し、他の人と共有することができます。多くのコミュニティカスタムノードを [こちら](https://registry.comfy.org) で見つけることができます。独自のカスタムノードを開発したい場合は、以下のセクションを訪れて開始してください：

## カスタムノードの開発を開始

カスタムノードの開発を開始する方法を学ぶ

## 

​

カスタムノード管理

このセクションでは以下について説明します：

  * カスタムノードのインストール
  * ノード依存関係のインストール
  * カスタムノードのバージョン管理
  * カスタムノードのアンインストール
  * カスタムノードの一時的な無効化
  * カスタムノードの依存関係の競合の処理



### 

​

1\. カスタムノードのインストール

現在、ComfyUI は複数の方法でカスタムノードをインストールすることをサポートしています。以下を含みます：

  * ComfyUI Manager 経由でインストール（推奨）
  * Git 経由でインストール
  * 手動インストール

カスタムノードは **ComfyUI Manager** 経由でインストールすることを推奨します。これは ComfyUI カスタムノードエコシステムにおいて非常に重要なツールです。カスタムノード管理（検索、インストール、更新、無効化、アンインストールなど）を簡単にします。ComfyUI Manager でインストールしたいノードを検索し、インストールをクリックするだけです。 ただし、現在すべてのカスタムノードは GitHub に保存されているため、GitHub に正常にアクセスできない地域向けに、このガイドでは異なるカスタムノードインストール方法の詳細な手順を記載しています。 さらに、プラグイン管理には **ComfyUI Manager** の使用を推奨しているため、このツールを使用してプラグインを管理することを推奨します。ソースコードは [こちら](https://github.com/Comfy-Org/ComfyUI-Manager) で見つけることができます。 したがって、このドキュメントでは、カスタムノードインストールの例として ComfyUI Manager のインストールを使用し、関連する紹介セクションでノード管理に如何使用するかを補足します。

  * ComfyUI Manager 経由でインストール

  * Git 経由でインストール

  * 手動インストール




ComfyUI Manager は非常に豊富な機能を持っているため、ComfyUI Manager のインストール章は別のドキュメントで紹介します。以下のリンクを訪れて、ComfyUI Manager を使用してカスタムノードをインストールする方法を学んでください。

## ComfyUI Manager でカスタムノードをインストール

ComfyUI Manager を使用してカスタムノードをインストールする方法を学ぶ

1

Git がインストールされていることを確認

まず、システムに Git がインストールされていることを確認する必要があります。システムターミナルで以下のコマンドを入力して、Git がインストールされているか確認できます：
    
    
    git --version
    

Git がインストールされている場合、以下のような出力が表示されます：![Windows ターミナル](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c0e90164d3a1c8f9ed0f54164b16443b)まだインストールされていない場合は、[git-scm.com](https://git-scm.com/) を訪れて対応するインストールパッケージをダウンロードしてください。Linux ユーザーは [git-scm.com/downloads/linux](https://git-scm.com/downloads/linux) を参照してインストール手順を確認してください。

Comfy Desktop バージョンの場合、以下のように Desktop ターミナルを使用してインストールを完了できます。![Comfy Desktop ターミナル](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/custom_nodes/desktop_terminal.png?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=333c167906d375f684542c19a938d2ff)

2

カスタムノードコードをディレクトリにクローン

Git のインストールを完了した後、カスタムノードのリポジトリアドレスが必要です。ここでは ComfyUI-Manager リポジトリアドレスを例として使用します：
    
    
    https://github.com/Comfy-Org/ComfyUI-Manager
    

GitHub にスムーズにアクセスできない地域の場合、他のコードホスティングサービスウェブサイトを使用して対応するリポジトリをフォークし、そのリポジトリアドレスを使用してノードインストールを完了できます。gitee などがあります。

まず、ComfyUI カスタムノードディレクトリに移動する必要があります。ComfyUI ポータブルバージョンを例として、フォルダの場所が `D:\ComfyUI_windows_portable` の場合、`D:\ComfyUI_windows_portable\ComfyUI\custom_nodes` にカスタムノードフォルダが見つかるはずです。まず、`cd` コマンドを使用して対応するディレクトリに入ります：
    
    
    cd D:\ComfyUI_windows_portable\ComfyUI\custom_nodes
    

次に、`git clone` コマンドを使用してノードインストールを完了します：
    
    
    git clone https://github.com/Comfy-Org/ComfyUI-Manager
    

すべてがスムーズに進めば、以下のような出力が表示されます：![Git 経由でカスタムノードをインストール](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=80409dceca35c9d58c42dde48c4c53a5)これは、カスタムノードコードを正常にクローンしたことを意味します。次に、対応する依存関係をインストールする必要があります。

3

依存関係をインストール

依存関係のインストールについては、ノード依存関係のインストール セクションの説明を参照してください。

手動インストールは推奨されるインストール方法ではありませんが、git を使用してスムーズにインストールできない場合のバックアップオプションとして機能します。

この方法でインストールされたプラグインは、対応する git バージョン履歴情報を失い、後続のバージョン管理が不便になります。

1

カスタムノードコード ZIP パッケージをダウンロード

手動インストールの場合、まず対応するノードコードをダウンロードし、適切なディレクトリに解凍する必要があります。![ノードコードをダウンロード](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=34fa06cf4580152428c5d2b55b192911)対応するカスタムノードリポジトリページを訪れます：

  1. `Code` ボタンをクリック
  2. 次に `Download ZIP` ボタンをクリックして ZIP パッケージをダウンロード
  3. ZIP パッケージを解凍



2

ファイルを ComfyUI カスタムノードディレクトリにコピー

上記の手順で解凍したコードを ComfyUI カスタムノードディレクトリにコピーします。ComfyUI ポータブルバージョンを例として、フォルダの場所が `D:\ComfyUI_windows_portable` の場合、`D:\ComfyUI_windows_portable\ComfyUI\custom_nodes` にカスタムノードフォルダが見つかるはずです。上記の手順で解凍したコードを対応するディレクトリにコピーします。

3

依存関係をインストール

依存関係のインストールについては、ノード依存関係のインストール セクションの説明を参照してください。

### 

​

2\. ノード依存関係のインストール

カスタムノードはすべて関連する依存関係のインストールが必要です。例えば、ComfyUI-Manager の場合、[requirements.txt](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/requirements.txt) ファイルを訪れて依存パッケージの要件を確認できます。 前の手順では、カスタムノードコードをローカルにクローンしただけで、対応する依存関係をインストールしていませんでした。したがって、次に対応する依存関係をインストールする必要があります。

実際、ComfyUI-Manager を使用してプラグインをインストールする場合、ComfyUI Manager は自動的に依存関係のインストールを完了してくれます。プラグインをインストールした後、ComfyUI を再起動するだけです。これが、カスタムノードをインストールするために ComfyUI Manager の使用を強く推奨する理由です。ただし、状況によっては ComfyUI Manager を使用してカスタムノードをスムーズにインストールできない場合もあるため、このより詳細な依存関係インストールガイドを提供しています。

[依存関係](https://docs.comfy.org/ja/basic-concepts/dependencies) 章では、ComfyUI における依存関係に関する関連コンテンツを紹介しました。ComfyUI は **Python** ベースのプロジェクトであり、ComfyUI を実行するための独立した **Python** ランタイム環境を構築しています。すべての関連する依存関係は、この独立した **Python** ランタイム環境にインストールする必要があります。 システムレベルのターミナルで直接 `pip install -r requirements.txt` を実行すると、対応する依存関係がシステムレベルの **Python** 環境にインストールされる可能性があり、ComfyUI の環境で依存関係が仍然として欠落し、対応するカスタムノードが正常に実行できなくなります。 したがって、次に ComfyUI の独立した Python ランタイム環境を使用して依存関係のインストールを完了する必要があります。 異なる ComfyUI バージョンに応じて、対応する依存関係をインストールするために異なる方法を使用します：

  * ComfyUI Portable

  * Comfy Desktop

  * カスタム Python 環境ユーザー




ComfyUI Portable バージョンの場合、`\ComfyUI_windows_portable\python_embeded` ディレクトリにある埋め込み Python を使用します。この Python を使用して依存関係のインストールを完了する必要があります。まず、ポータブルバージョンディレクトリでターミナルを起動するか、ターミナルを起動した後 `cd` コマンドを使用して `\ComfyUI_windows_portable\` ディレクトリに移動します。![ターミナルを起動](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ee4569d27b4ef901c5f67d8f795b448c)ターミナルディレクトリが `\ComfyUI_windows_portable\` であることを確認します。以下は `D:\ComfyUI_windows_portable\` の例です。![ターミナル](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f6da2e8c4eef1016e6fde84ee5527ce0)次に、`python_embeded\python.exe` を使用して依存関係のインストールを完了します：
    
    
    python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Manager\requirements.txt
    

もちろん、ComfyUI-Manager を実際にインストールしたカスタムノードの名前に置き換えることができますが、対応するノードディレクトリに `requirements.txt` ファイルが存在することを確認してください。

Comfy Desktop はインストールプロセス中にすでに ComfyUI-Manager とその依存関係がインストールされているため、このガイドはカスタムノードインストールの例として ComfyUI Manager を使用していますが、実際にはデスクトップバージョンで ComfyUI Manager の依存関係インストールを実行する必要はありません。 予期しない問題がない限り、カスタムノードをインストールするために ComfyUI Manager の使用を推奨します。そうすれば、依存関係を手動でインストールする必要はありません。

![Comfy Desktop ターミナル](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/custom_nodes/desktop_terminal.png?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=333c167906d375f684542c19a938d2ff)次に、以下のコマンドを使用して対応するプラグインの依存関係をインストールします：
    
    
    pip install -r .\custom_nodes\<corresponding_custom_node_name>\requirements.txt
    

以下に示すように、これは ComfyUI-Hunyuan3Dwrapper の依存関係インストールです：![Comfy Desktop 依存関係インストール](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/custom_nodes/install_dependencies.png?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=ab31e7626f27d5a7da7171f985d1b305)

カスタム Python 環境を持つユーザーの場合、`pip install -r requirements.txt` を使用して依存関係のインストールを完了することを推奨します。

### 

​

カスタムノードバージョン管理

カスタムノードのバージョン管理は実際には Git バージョン管理に基づいています。Git を通じてノードバージョンを管理できますが、ComfyUI Manager はすでにこのバージョン管理機能を非常によく統合しています。[@Dr.Lt.Data](https://github.com/ltdrdata) さんに、このような便利なツールをもたらしてくれたことに感謝します。 このセクションでは、これら 2 つの異なるプラグインバージョン管理方法について説明しますが、ZIP パッケージを使用して手動でインストールする場合、対応する git バージョン履歴情報が失われ、バージョン管理を実行できなくなります。

  * ComfyUI Manager でのバージョン管理

  * Git でのバージョン管理




ComfyUI Manager を反復しているため、実際の最新のインターフェースと手順は大幅に変更される可能性があります

1

ノード管理インターフェースに入る

図に示すように対応する操作を実行して、ComfyUI Manager インターフェースに入ります

2

対応するカスタムノードパッケージを見つける

対応するフィルターを使用してインストールされたノードパッケージをフィルタリングし、対応するノード管理を実行できます

3

バージョン切り替えを実行

対応するバージョンに切り替えます。Manager は対応する依存関係の更新とインストールを完了してくれます。通常、バージョンを切り替えた後、変更を有効にするために ComfyUI を再起動する必要があります。

1

コマンドラインを使用してディレクトリに移動

対応するノードが位置するディレクトリフォルダーを見つけます。例：`ComfyUI/custom_nodes/ComfyUI-Manager` `cd` コマンドを使用して対応するフォルダーに入ります：
    
    
    cd <your_installation_directory>/ComfyUI/custom_nodes/ComfyUI-Manager
    

2

Git コマンドを使用してバージョンを表示

以下のコマンドを使用して、利用可能なすべてのタグとリリースを表示できます：
    
    
    git tag
    

これにより、すべてのバージョンタグが一覧表示され、切り替えたいバージョンを選択できます。

3

指定されたバージョンに切り替え

以下のコマンドを使用して、指定されたタグまたはリリースに切り替えます：
    
    
    git checkout <tag_name>
    

`<tag_name>` を切り替えたい特定のバージョンタグに置き換えます。

4

特定のコミットバージョンに切り替え

特定のコミットバージョンに切り替えたい場合、以下のコマンドを使用できます：
    
    
    git checkout <commit_hash>
    

`<commit_hash>` を切り替えたい特定のコミットハッシュに置き換えます。

5

依存関係をインストール

バージョン切り替え後、対応するカスタムノードパッケージの依存関係が変更される可能性があるため、対応するノードの依存関係を再インストールする必要があります。ノード依存関係のインストール セクションの説明を参照して、対応する環境に入りインストールしてください。

### 

​

カスタムノードのアンインストール

更新予定

### 

​

カスタムノードの一時的な無効化

更新予定

### 

​

カスタムノードの依存関係の競合

更新予定

## 

​

ComfyUI Manager

![ComfyUI Manager インターフェース](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936) このツールは現在 [Desktop バージョン](https://docs.comfy.org/ja/installation/desktop/windows) にデフォルトで含まれており、[Portable バージョン](https://docs.comfy.org/ja/installation/comfyui_portable_windows) では、このドキュメントの Manager のインストール セクションのインストール手順を参照する必要があります。

ComfyUI の開発に伴い、ComfyUI Manager は ComfyUI においてますます重要な役割を果たしています。現在、ComfyUI-Manager は正式に Comfy Org 組織に参加し、ComfyUI のコア依存関係の一部となり、元の作者 [Dr.Lt.Data](https://github.com/ltdrdata) によって引き続きメンテナンスされています。詳細については [このブログ投稿](https://blog.comfy.org/p/comfyui-manager-joins-comfy-org) を読むことができます。 将来の反復では、ComfyUI Manager の使用を大幅に最適化するため、このドキュメントに表示されるインターフェースは最新バージョンの ComfyUI Manager と異なる可能性があります。

### 

​

Manager のインストール

ComfyUI サーバーアプリケーションを実行している場合、manager をインストールする必要があります。ComfyUI が実行されている場合は、続行する前に閉じてください。 最初のステップは Git のインストールです。これはソフトウェアバージョン管理のためのコマンドラインアプリケーションです。Git は [github.com](https://github.com) から ComfyUI manager をダウンロードします。[git-scm.com](https://git-scm.com/) から Git をダウンロードしてインストールします。 Git をインストールした後、ComfyUI サーバープログラムディレクトリに移動し、**custom_nodes** とラベル付けされたフォルダーに入ります。コマンドウィンドウまたはターミナルを開きます。コマンドラインが現在のディレクトリパスを **custom_nodes** として表示していることを確認します。以下のコマンドを実行して ComfyUI-Manager リポジトリをクローンします：
    
    
    git clone https://github.com/Comfy-Org/ComfyUI-Manager.git
    

これにより manager がダウンロードされます。技術的には、これは _Git リポジトリのクローン_ と呼ばれます。

### 

​

欠落ノードの検出

manager をインストールした後、manager で欠落ノードを検出できます。 ![ComfyUI Manager インターフェース](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936)

## 

​

カスタムノードの開発

ある程度の開発能力をお持ちの場合は、以下のドキュメントから開始して、カスタムノードの開発を開始する方法を学んでください。

## カスタムノードの開発を開始

カスタムノードの開発を開始する方法を学ぶ

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/basic-concepts/custom-nodes.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/basic-concepts/custom-nodes)

[ComfyUI ノード：種類、入力、出力前へ](https://docs.comfy.org/ja/basic-concepts/nodes)[ComfyUI プロパティ：ウィジェット、入力、データ型次へ](https://docs.comfy.org/ja/basic-concepts/properties)

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
