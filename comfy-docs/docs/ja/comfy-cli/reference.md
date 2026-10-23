---
url: https://docs.comfy.org/ja/comfy-cli/reference/
title: Comfy CLI \u30b3\u30de\u30f3\u30c9\u30ea\u30d5\u30a1\u30ec\u30f3\u30b9 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:56.646367+00:00
---

# Comfy CLI コマンドリファレンス - ComfyUI

> Source: https://docs.comfy.org/ja/comfy-cli/reference/

## このページの内容

  * CLI
  * Generate（パートナーノード）— Beta
    * list
    * schema
    * refresh
    * upload
    * resume
    * モデルエイリアス（一部抜粋）
  * ノード
    * deps-in-workflow
    * disable
    * enable
    * fix
    * install
    * install-deps
    * reinstall
    * restore-dependencies
    * restore-snapshot
    * save-snapshot
    * show
    * simple-show
    * uninstall
    * update
  * モデル
    * download
    * list
    * remove



Comfy CLI

# Comfy CLI コマンドリファレンス

ページをコピーページをコピー

Comfy CLI の完全リファレンス。インストールコマンド、ノード管理、モデルダウンロードなど、ターミナルから ComfyUI をセットアップ・管理する方法をカバーします。

ページをコピーページをコピー

# 

​

CLI

## 

​

Generate（パートナーノード）— Beta

**`comfy generate` はベータ版です。** フラグ名、モデルエイリアス、出力形式は変更される可能性があります。基盤となるパートナーエンドポイントは安定していますが、CLI のインターフェースは依然として進化中です。フィードバックは [comfy-cli GitHub リポジトリ](https://github.com/Comfy-Org/comfy-cli/issues) にお寄せください。

**使用法** :
    
    
    $ comfy generate [OPTIONS] <MODEL_OR_ACTION> [--<param> value]...
    

`<MODEL_OR_ACTION>` は以下のいずれかです。

  * **モデルエイリアス** （例: `flux-pro`、`ideogram-edit`、`kling`、`dalle`） — 対応するパートナーモデルを直接呼び出します。
  * **予約済みアクション** : `list`、`schema`、`refresh`、`upload`、`resume`。

予約済みのセットに含まれないものは全てモデルエイリアスとして扱われ、リクエストは対応するパートナーエンドポイントへ送信されます。 **認証** : 環境変数 `COMFY_API_KEY` を設定するか、各呼び出しで `--api-key <KEY>` を渡します。キーは [platform.comfy.org](https://platform.comfy.org) で取得してください。 **実行レベルのフラグ** （すべてのモデルで使用可能）:

  * `--download PATH`: 結果の画像/動画を `PATH` に保存します。
  * `--async`: 完了をポーリングする代わりに、ジョブIDを即座に返して非同期実行します。後で `comfy generate resume <model> <job_id>` で再開できます。
  * `--json`: 生のAPIレスポンスをJSONとして出力します（スクリプト用に便利です）。
  * `--timeout SECONDS`: デフォルトの300秒のポーリングタイムアウトを上書きします。
  * `--api-key KEY`: インラインAPIキー（`COMFY_API_KEY` を上書きします）。

**例** :
    
    
    comfy generate flux-pro --prompt "a cat on the moon" --width 1024 --height 1024 --download cat.png
    comfy generate ideogram-edit --image cat.png --mask m.png --prompt "add sunglasses" --rendering_speed TURBO
    comfy generate kling --prompt "a paper boat drifting at dusk" --duration 5 --download boat.mp4
    

### 

​

`list`

利用可能なパートナーモデルを短いエイリアスと共に一覧表示します。 **使用法** :
    
    
    $ comfy generate list [OPTIONS]
    

**オプション** :

  * `--partner TEXT` / `-p TEXT`: パートナーでフィルタ（例: `bfl`、`kling`、`ideogram`、`openai`）。
  * `--category TEXT` / `--style TEXT` / `-c TEXT`: カテゴリでフィルタ（例: `text-to-image`、`image-edit`、`inpaint`、`upscale`、`text-to-video`、`image-to-video`）。
  * `--query TEXT` / `-q TEXT`: モデルID/概要に対する部分文字列検索。



### 

​

`schema`

特定のモデルのパラメータを表示します。必須/任意のフラグ、型、デフォルト値、および実行例を含みます。 **使用法** :
    
    
    $ comfy generate schema <MODEL>
    

**例** :
    
    
    comfy generate schema flux-pro
    comfy generate schema kling-i2v
    

### 

​

`refresh`

ローカルにキャッシュされたモデルカタログをクラウドのOpenAPI仕様から更新します。新しいパートナーモデルが追加されたときに便利です。 **使用法** :
    
    
    $ comfy generate refresh
    

### 

​

`upload`

ローカルファイル（またはリモートURLの再ホスト）をComfyのストレージにアップロードし、署名付きURLを出力します。ほとんどのモデルはローカルファイルパスを直接受け付けますが、これはURLを明示的に取得したい場合に使用します（例: 同じアセットを複数回の呼び出しで再利用する場合）。 **使用法** :
    
    
    $ comfy generate upload <FILE_OR_URL> [--json]
    

**例** :
    
    
    comfy generate upload ./photo.jpg
    comfy generate upload ./photo.jpg --json
    

**参照アセットは24時間後に自動的に削除されます。** アップロードされたファイル（`comfy generate upload` 経由、またはモデルにローカルファイルパスを渡す際の暗黙的なアップロード）は、Comfyが管理するGCSバケット（`api-nodes-prod`）に保存され、署名付きURLでのみアクセス可能です。バケットのライフサイクルルールにより、アップロードから**1日後** にオブジェクトは自動的に削除されます。長時間実行される非同期ジョブの間もアセットを保持する必要がある場合は、各ジョブの前に再アップロードするか、ご自身でホストしてURLを直接渡してください。

### 

​

`resume`

以前に送信した非同期ジョブ（通常は `--async` を指定した動画ジョブ）を再開します。結果が準備できるまでポーリングし、必要に応じてダウンロードします。 **使用法** :
    
    
    $ comfy generate resume <MODEL> <JOB_ID> [--download PATH] [--json]
    

**例** :
    
    
    comfy generate resume luma 7c3f9e2a --download out.mp4
    

### 

​

モデルエイリアス（一部抜粋）

以下の短いエイリアスを `<MODEL>` として使用できます。完全かつ最新のカタログは `comfy generate list` を実行して確認してください。 **人気** :

エイリアス| パートナー| カテゴリ  
---|---|---  
`nano-banana`| Google (Gemini Flash Image)| テキストから画像 / 画像編集  
`seedance`| ByteDance| テキストから動画 / 画像から動画（非同期）  
`grok`、`grok-edit`| xAI| テキストから画像 / 画像編集  
`grok-video`| xAI| テキストから動画（非同期）  
  
**その他** :

エイリアス| パートナー| カテゴリ  
---|---|---  
`flux-pro`、`flux-ultra`、`flux-2`| BFL| テキストから画像（非同期）  
`flux-kontext`、`flux-kontext-max`| BFL| 画像編集（非同期）  
`flux-fill`、`flux-expand`、`flux-canny`、`flux-depth`| BFL| インペイント / アウトペイント / controlnet  
`ideogram`、`ideogram-edit`、`ideogram-remix`、`ideogram-reframe`、`ideogram-bg`| Ideogram| テキストから画像 / 画像編集  
`dalle`、`dalle-edit`| OpenAI| テキストから画像 / 画像編集  
`stability-ultra`、`stability-sd3`、`stability-upscale`、`stability-upscale-creative`、`stability-upscale-fast`| Stability| テキストから画像 / アップスケール  
`recraft`、`recraft-vectorize`、`recraft-rmbg`、`recraft-replace-bg`、`recraft-i2i`、`recraft-inpaint`、`recraft-upscale`、`recraft-upscale-creative`| Recraft| テキストから画像 / 画像編集  
`reve`、`reve-edit`| Reve| テキストから画像 / 画像編集  
`runway`| Runway| テキストから画像  
`kling`、`kling-i2v`、`kling-extend`、`kling-lipsync`| Kling| テキストから動画 / 画像から動画 / 動画延長 / リップシンク（非同期）  
`luma`、`luma-i2v`| Luma| テキストから動画 / 画像から動画（非同期）  
`hailuo`| MiniMax| テキストから動画（非同期）  
`runway-i2v`| Runway| 画像から動画（非同期）  
`moonvalley-t2v`、`moonvalley-i2v`| Moonvalley| テキストから動画 / 画像から動画（非同期）  
`pika`、`pika-i2v`| Pika| テキストから動画 / 画像から動画（非同期）  
`vidu`、`vidu-i2v`、`vidu-extend`| Vidu| テキストから動画 / 画像から動画 / 動画延長（非同期）  
  
## 

​

ノード

**Usage** :
    
    
    $ comfy node [OPTIONS] COMMAND [ARGS]...
    

**Options** :

  * `--install-completion`: Install completion for the current shell.
  * `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
  * `--help`: Show this message and exit.

**Commands** :

  * `deps-in-workflow`
  * `disable`
  * `enable`
  * `fix`
  * `install`
  * `install-deps`
  * `reinstall`
  * `restore-dependencies`
  * `restore-snapshot`
  * `save-snapshot`: Save a snapshot of the current ComfyUI…
  * `show`
  * `simple-show`
  * `uninstall`
  * `update`



### 

​

`deps-in-workflow`

**Usage** :
    
    
    $ deps-in-workflow [OPTIONS]
    

**Options** :

  * `--workflow TEXT`: Workflow file (.json/.png) [required]
  * `--output TEXT`: Workflow file (.json/.png) [required]
  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`disable`

**Usage** :
    
    
    $ disable [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: disable custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`enable`

**Usage** :
    
    
    $ enable [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: enable custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`fix`

**Usage** :
    
    
    $ fix [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: fix dependencies for specified custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`install`

**Usage** :
    
    
    $ install [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: install custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`install-deps`

**Usage** :
    
    
    $ install-deps [OPTIONS]
    

**Options** :

  * `--deps TEXT`: Dependency spec file (.json)
  * `--workflow TEXT`: Workflow file (.json/.png)
  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`reinstall`

**Usage** :
    
    
    $ reinstall [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: reinstall custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`restore-dependencies`

**Usage** :
    
    
    $ restore-dependencies [OPTIONS]
    

**Options** :

  * `--help`: Show this message and exit.



### 

​

`restore-snapshot`

**Usage** :
    
    
    $ restore-snapshot [OPTIONS] PATH
    

**Arguments** :

  * `PATH`: [required]

**Options** :

  * `--help`: Show this message and exit.



### 

​

`save-snapshot`

Save a snapshot of the current ComfyUI environment **Usage** :
    
    
    $ save-snapshot [OPTIONS]
    

**Options** :

  * `--output TEXT`: Specify the output file path. (.json/.yaml)
  * `--help`: Show this message and exit.



### 

​

`show`

**Usage** :
    
    
    $ show [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: [installed|enabled|not-installed|disabled|all|snapshot|snapshot-list] [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`simple-show`

**Usage** :
    
    
    $ simple-show [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: [installed|enabled|not-installed|disabled|all|snapshot|snapshot-list] [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`uninstall`

**Usage** :
    
    
    $ uninstall [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: uninstall custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



### 

​

`update`

**Usage** :
    
    
    $ update [OPTIONS] ARGS...
    

**Arguments** :

  * `ARGS...`: update custom nodes [required]

**Options** :

  * `--channel TEXT`: Specify the operation mode
  * `--mode TEXT`: [remote|local|cache]
  * `--help`: Show this message and exit.



## 

​

モデル

**使用方法** :
    
    
    $ comfy model [OPTIONS] COMMAND [ARGS]...
    

**オプション** :

  * `--install-completion`: 現在のシェルに対してコマンド補完機能をインストールします。
  * `--show-completion`: 現在のシェル向けのコマンド補完スクリプトを表示し、コピーまたはカスタマイズ可能な状態にします。
  * `--help`: このメッセージを表示して終了します。

**コマンド** :

  * `download`: モデルを指定された相対パスにダウンロードします…
  * `list`: 現在ダウンロード済みのすべてのモデルの一覧を表示します…
  * `remove`: 1つ以上のダウンロード済みモデルを削除します…



### 

​

`download`

モデルがまだダウンロードされていない場合、指定された相対パスにダウンロードします。 **使用方法** :
    
    
    $ download [OPTIONS]
    

**オプション** :

  * `--url TEXT`: モデルをダウンロードするための URL [必須]
  * `--relative-path TEXT`: モデルをインストールするための、現在のワークスペースからの相対パス。 [デフォルト: models/checkpoints]
  * `--help`: このメッセージを表示して終了します。



### 

​

`list`

現在ダウンロード済みのすべてのモデルを表形式で一覧表示します。 **使用方法** :
    
    
    $ list [OPTIONS]
    

**オプション** :

  * `--relative-path TEXT`: モデルが格納されている、現在のワークスペースからの相対パス。 [デフォルト: models/checkpoints]
  * `--help`: このメッセージを表示して終了します。



### 

​

`remove`

直接モデル名を指定するか、インタラクティブな選択を通じて、1つ以上のダウンロード済みモデルを削除します。 **使用方法** :
    
    
    $ remove [OPTIONS]
    

**オプション** :

  * `--relative-path TEXT`: モデルが格納されている、現在のワークスペースからの相対パス。 [デフォルト: models/checkpoints]
  * `--model-names TEXT`: 削除対象のモデルファイル名のリスト（スペース区切り）
  * `--help`: このメッセージを表示して終了します。



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/comfy-cli/reference.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/comfy-cli/reference)

[Comfy CLI をはじめよう前へ](https://docs.comfy.org/ja/comfy-cli/getting-started)[Comfy CLI トラブルシューティングガイド次へ](https://docs.comfy.org/ja/comfy-cli/troubleshooting)

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
