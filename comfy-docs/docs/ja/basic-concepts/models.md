---
url: https://docs.comfy.org/ja/basic-concepts/models/
title: ComfyUI \u30e2\u30c7\u30eb\uff1a\u30d5\u30a1\u30a4\u30eb\u3001\u30d5\u30a9\u30eb\u30c0\u3001\u30ed\u30fc\u30c0\u30fc\u30ce\u30fc\u30c9 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:31.714450+00:00
---

# ComfyUI モデル：ファイル、フォルダ、ローダーノード - ComfyUI

> Source: https://docs.comfy.org/ja/basic-concepts/models/

## このページの内容

  * モデルをひと言で言うと
    * ComfyUI でサポートされているモデル
  * ComfyUI でモデルを使う
    * 大きなダウンロードを見込んでおく
  * メインチェックポイント以外のモデル
  * モデルのアンインストール
  * 外部モデルパスの追加
    * 設定ファイルの開き方
    * 設定例
    * 追加のカスタムノードパスの登録
  * よくある問題
  * もう少し背景を知りたい方へ



基本概念

# ComfyUI モデル：ファイル、フォルダ、ローダーノード

ページをコピーページをコピー

ComfyUI のモデルファイル：配置場所、ノードでの使い方、よくある問題。

ページをコピーページをコピー

## 

​

モデルをひと言で言うと

ComfyUI において、**モデル** とはワークフローを実際に動かす**重みファイル** のことです。**チェックポイント** 、**VAE** 、**LoRA** 、**ControlNet** 、アップスケーラーなどが該当します。アプリ本体は軽量で、これらのファイルはデフォルトでは含まれていません。通常はウェブからダウンロードし、`ComfyUI/models/` 以下に配置します（またはテンプレートのプロンプトに従います）。その後、キャンバス上の適切な**ローダーノード** （名前が **Load** から始まることが多い）でファイルを選択します。

### 

​

ComfyUI でサポートされているモデル

  * **組み込み／ファーストパーティのサポートは意図的に限定されていますが** 、ComfyUI とオープンソースエコシステムの発展に伴い随時拡充されています。モデルが正式サポートされると、通常は**[ワークフローテンプレートライブラリ](https://docs.comfy.org/ja/interface/features/template)** に期待されるグラフとモデルの組み合わせを示す新しいエントリが追加されます。
  * **すべてのチェックポイントや重みファイルがそのまま動作するわけではありません。** **ネイティブサポートされているモデルとその一般的な付属ウェイトについては** 、ComfyUI を最新の状態に **[保ち](https://docs.comfy.org/ja/installation/update_comfyui)** 、ファイルが誤った場所にあると決めつける前に、**[テンプレートライブラリ](https://docs.comfy.org/ja/interface/features/template)** に対応するワークフローが存在するか確認してください。
  * **多くのモデルはコミュニティのカスタムノードで利用可能になります。** パス、ローダーノード、グラフの構成はこのページの一般的な `ComfyUI/models/` ガイダンスとは異なる場合があります。**必ず各プロジェクトの README やドキュメントに従ってください** 。ComfyUI は高い拡張性を持つため、実装は作者によって異なります。インストールとトラブルシューティングについては、[カスタムノードのインストール方法](https://docs.comfy.org/ja/installation/install_custom_node) を参照してください。



## 

​

ComfyUI でモデルを使う

  1. **ファイルを正しい場所に配置する。** [Hugging Face](https://huggingface.co)、[Civitai](https://civitai.green)、[GitHub](https://github.com) などのコミュニティサイトからダウンロードし、`ComfyUI/models/` 以下のモデルタイプに対応するサブフォルダ（例：`checkpoints`、`loras`、`vae`）に配置します。
  2. **対応するローダーノードを追加する。** モデルタイプ（チェックポイント、LoRA、VAE など）に合ったローダーを選びます。ノードリストではタイトルが **Load** で始まることが多いです。
  3. **ファイルを選択する。** そのローダーノードのドロップダウンで選びます。
  4. **ローダーノードをグラフの残りのノードに接続する。** ComfyUI の実行中に手動でファイルをコピーした場合は、リストを更新するためにアプリを**再起動** してください（または必要に応じて更新してください）。



### 

​

大きなダウンロードを見込んでおく

生成モデル 1 つは多くの場合**数ギガバイト** に達します。ダウンロードや同期の際はディスク容量と時間を十分に確保してください。

## 

​

メインチェックポイント以外のモデル

メインの拡散チェックポイントは多くのことをこなしますが、多くのワークフローではさらに**小さなヘルパーモデル** を追加します。例えば：

  * **LoRA** : スタイル、キャラクター、概念に合わせてチューニングされた軽量アドオン
  * **ControlNet** : エッジ、深度、ポーズなどによる追加ガイダンス
  * **Inpainting** : 既存画像内の領域の塗りつぶしや置き換え

![補助モデル](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=0f49a29f61c23ccd32ec5a15207b8f9c)

## 

​

モデルのアンインストール

UI にはまだ「アンインストール」ボタンがありません。モデルを削除するには、配置した `ComfyUI/models/` 以下のフォルダからそのファイル（複数の場合はすべて）を**手動で削除** してください。

## 

​

外部モデルパスの追加

`ComfyUI/models` ディレクトリの外部でモデルファイルを管理したい場合、以下のような理由が考えられます。

  * 複数の ComfyUI インスタンスを運用しており、ディスク容量の節約のためにモデルファイルを共有したい
  * WebUI などの異なる種類の GUI アプリケーションを併用しており、それらで共通のモデルファイルを使いたい
  * モデルファイルが認識されない、または見つからない

このため、`extra_model_paths.yaml` 設定ファイルを用いて、追加のモデル検索パスを指定する方法を提供しています。

### 

​

設定ファイルの開き方

  * ポータブル版／手動インストール版

  * Comfy Desktop




[ポータブル版](https://docs.comfy.org/ja/installation/comfyui_portable_windows) や [手動インストール版](https://docs.comfy.org/ja/installation/manual_install) の ComfyUI の場合、ComfyUI のルートディレクトリに `extra_model_paths.yaml.example` という名前のサンプルファイルが含まれています。
    
    
    ComfyUI/extra_model_paths.yaml.example
    

このファイルをコピーし、名前を `extra_model_paths.yaml` に変更して使用します。ファイルは必ず ComfyUI のルートディレクトリ（`ComfyUI/extra_model_paths.yaml`）に保存してください。  
また、このサンプル設定ファイルは [こちら](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example) からも参照できます。

[Comfy Desktop](https://docs.comfy.org/ja/installation/desktop/windows) アプリケーションをご利用の場合、デスクトップアプリ上部のカプセルメニューをクリックし、**Storage** タブを開いてモデルディレクトリを追加します。カプセルメニューはデスクトップアプリにのみ存在し、ブラウザーで実行している ComfyUI にはありません![Comfy Desktop カプセルメニュー: モデルディレクトリ設定を表示する Storage タブ](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)または、直接以下のパスから開くことも可能です：

  * Windows

  * macOS



    
    
    C:\Users\YourUsername\AppData\Roaming\ComfyUI\extra_models_config.yaml
    
    
    
    ~/Library/Application Support/ComfyUI/extra_models_config.yaml
    

この設定ファイルは、上記の場所に常に保存しておく必要があります。他の場所へ移動しないでください。

該当ファイルが存在しない場合は、任意のテキストエディタで新規作成してください。

### 

​

設定例

たとえば、以下の構造でモデルファイルを格納している場合：
    
    
    📁 YOUR_PATH/
      ├── 📁models/
      |   ├── 📁 loras/
      |   │   └── xxxxx.safetensors
      |   ├── 📁 checkpoints/
      |   │   └── xxxxx.safetensors
      |   ├── 📁 vae/
      |   │   └── xxxxx.safetensors
      |   └── 📁 controlnet/
      |       └── xxxxx.safetensors
    

このパスを ComfyUI が認識できるよう、`extra_model_paths.yaml` を次のように設定できます：
    
    
    my_custom_config:
        base_path: YOUR_PATH
        loras: models/loras/
        checkpoints: models/checkpoints/
        vae: models/vae/
        controlnet: models/controlnet/
    

あるいは以下のようにも設定可能です：
    
    
    my_custom_config:
        base_path: YOUR_PATH/models/
        loras: loras
        checkpoints: checkpoints
        vae: vae
        controlnet: controlnet
    

デスクトップ版では、インストール時に自動生成されたパス設定を上書きせず、既存の設定ファイルに新しい設定を追加してください。誤った編集を行った場合に備えて、変更前に該当ファイルのバックアップを必ず取得してください。

そのほかの設定オプションについては、デフォルトの [extra_model_paths.yaml.example](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example) をご参照ください。設定を保存した後は、**ComfyUI を再起動** する必要があります。 以下は、元の設定ファイルのサンプルです：
    
    
    # このファイルを extra_model_paths.yaml に名前を変更すると、ComfyUI が読み込みます
    
    
    # a1111 UI 向け設定
    # 必要なのは、base_path をご自身のインストール先に変更することだけです
    a111:
        base_path: path/to/stable-diffusion-webui/
    
        checkpoints: models/Stable-diffusion
        configs: models/Stable-diffusion
        vae: models/VAE
        loras: |
             models/Lora
             models/LyCORIS
        upscale_models: |
                      models/ESRGAN
                      models/RealESRGAN
                      models/SwinIR
        embeddings: embeddings
        hypernetworks: models/hypernetworks
        controlnet: models/ControlNet
    
    # ComfyUI 向け設定
    # base_path には、既存の ComfyUI インストール先、またはすべてのモデル・LoRA などを一元管理する中央フォルダのパスを指定してください
    
    #comfyui:
    #     base_path: path/to/comfyui/
    #     # is_default を true に設定すると、これらのフォルダが優先的にリスト表示され、ダウンロード先などデフォルトのディレクトリとして使用されます
    #     #is_default: true
    #     checkpoints: models/checkpoints/
    #     clip: models/clip/
    #     clip_vision: models/clip_vision/
    #     configs: models/configs/
    #     controlnet: models/controlnet/
    #     diffusion_models: |
    #                  models/diffusion_models
    #                  models/unet
    #     embeddings: models/embeddings/
    #     loras: models/loras/
    #     upscale_models: models/upscale_models/
    #     vae: models/vae/
    
    # その他の UI 向け設定
    #other_ui:
    #    base_path: path/to/ui
    #    checkpoints: models/checkpoints
    #    gligen: models/gligen
    #    custom_nodes: path/custom_nodes
    
    

たとえば、WebUI が `D:\stable-diffusion-webui\` にインストールされている場合、対応する設定を次のように変更できます：
    
    
    a111:
        base_path: D:\stable-diffusion-webui\
        checkpoints: models/Stable-diffusion
        configs: models/Stable-diffusion
        vae: models/VAE
        loras: |
             models/Lora
             models/LyCORIS
        upscale_models: |
                      models/ESRGAN
                      models/RealESRGAN
                      models/SwinIR
        embeddings: embeddings
        hypernetworks: models/hypernetworks
        controlnet: models/ControlNet
    

### 

​

追加のカスタムノードパスの登録

外部モデルの追加に加え、ComfyUI のデフォルトパスに含まれていないカスタムノードのパスも登録できます。

この設定は、カスタムノードのデフォルトインストールパスを変更するものではありません。ComfyUI 起動時に追加の検索パスとして認識されるようになります。ただし、実行環境の完全性を保つため、対応する環境においてカスタムノードの依存関係を引き続き正しくインストールする必要があります。

以下は、macOS 向けの簡単な設定例です。実際の環境に合わせて適宜修正し、対応する設定ファイルに追加してください。変更後は、**ComfyUI を再起動** することで設定が有効になります：
    
    
    my_custom_nodes:
      custom_nodes: /Users/your_username/Documents/extra_custom_nodes
    

## 

​

よくある問題

ComfyUI は GGUF モデルをサポートしていますか？

ComfyUI はネイティブに GGUF 形式をサポートしていません。サポートを追加するには [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) などのコミュニティカスタムノードが必要です。

モデルが見つからないのはなぜですか？

モデルをインストールしたが ComfyUI で見つからない場合は、次の手順を試してください：

  * モデルが正しい場所にあるか確認します：
    * デフォルトのパスは `ComfyUI/models/` です（例：`checkpoints`、`loras`、`vae`）
    * **Comfy Desktop** の場合：デスクトップアプリ上部のカプセルメニューをクリックし、**Storage** タブを開いてモデルディレクトリを確認します。カプセルメニューはデスクトップアプリにのみ存在し、ブラウザーで実行している ComfyUI にはありません
![Comfy Desktop capsule menu: Storage tab showing model directory settings](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)
  * `r` キーを押してノード定義を更新し、ComfyUI がモデルを検出できるようにします
  * ComfyUI を再起動します
  * ローダーノードで正しいモデルが選択されていることを確認します



## 

​

もう少し背景を知りたい方へ

ここでいう「モデル」とは？

ここでの**モデル** とは、ネットワークが学習した内容をエンコードしたデータファイルのことです。テキストやノイズなどの入力から画像などの出力を生成するのに十分な情報を含んでいます。画像ワークフローでの一般的な例としては、**拡散** チェックポイント、**CLIP** などのテキスト／画像エンコーダ、RealESRGAN などの**アップスケーラー** があります。

ベースモデルとコミュニティバリアント

研究機関やオープンソースプロジェクトの大型**ベース** モデルは汎用目的のものです。コミュニティはこれらを特定のスタイル向けに**ファインチューニング** したり、マージして新しいチェックポイントや LoRA を作成します。それらはより良い出力を出したり、少し軽量に動作したり、新しい挙動を追加したりします。Civitai や Hugging Face でお気に入りのチェックポイントを選ぶのと同じ考え方です。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/basic-concepts/models.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/basic-concepts/models)

[ComfyUI リンク：ノード接続の仕組み前へ](https://docs.comfy.org/ja/basic-concepts/links)[依存関係次へ](https://docs.comfy.org/ja/basic-concepts/dependencies)

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
