---
url: https://docs.comfy.org/ja/comfy-cli/getting-started/
title: Comfy CLI \u3092\u306f\u3058\u3081\u3088\u3046 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:56.225140+00:00
---

# Comfy CLI をはじめよう - ComfyUI

> Source: https://docs.comfy.org/ja/comfy-cli/getting-started/

## このページの内容

  * 概要
  * CLIのインストール
  * クイックセットアップ（推奨）
  * ComfyUI（ローカル）のインストール
  * ComfyUIを実行する（ローカル）
  * Comfy Cloud
  * パートナーノードで生成
    * 前提条件
    * 初めての生成
    * よく使われるモデル
    * モデルを見つける
    * 参照画像を使った画像編集
    * 動画生成（非同期ジョブ）
    * スクリプト用のJSON出力
  * ワークフローの実行（comfy run）
  * テンプレートから始める
  * ワークフローのその場編集
  * ノードとモデルを発見する
  * ファイルのアップロードとダウンロード
  * カスタムノードの管理
  * モデルの管理（ローカル）
  * スクリプトとエージェント向けのJSON出力
  * エージェントスキル
  * コントリビューション
  * 分析



Comfy CLI

# Comfy CLI をはじめよう

ページをコピーページをコピー

comfy-cli をインストールし、ローカルまたはクラウドのルーティングを設定し、パートナーノードを使用して生成し、ターミナルからワークフローを実行します。

ページをコピーページをコピー

## 

​

概要

`comfy-cli` は、Comfy のインストールと管理を効率化し、ローカルまたはクラウド上で ComfyUI エコシステム全体にスクリプト可能な単一コマンドでアクセスできる[コマンドラインツール](https://github.com/Comfy-Org/comfy-cli)です。 主な機能は3つです。

  1. **ローカルの ComfyUI インストールを管理** — ComfyUI とカスタムノードのインストール、起動、更新、スナップショット、bisect を行います。
  2. **ホスト型パートナーノードにアクセス** — Seedance、Nano Banana（Gemini）、Grok、Flux、Ideogram、DALL·E、Recraft、Stability、Kling、Luma、Runway、Pika、Vidu、Hailuo、Moonvalley などのプロバイダーから画像、動画、音声、3D を単一コマンドで生成します。
  3. **Comfy Cloud で完全なワークフローを実行** — ワークフローグラフの送信、厳選されたテンプレートギャラリーのブラウズ、スロット編集によるワークフローの編集、ジョブの完了までの監視を、ローカル GPU なしで行います。



**2つのサーフェス、1つのCLI。** すべてのコマンドは自動的に実行場所を検出します。Comfy Cloud にサインインしている場合、コマンドは **クラウド** にルーティングされます。それ以外の場合は、**ローカル** サーバーに対して実行されます。コールごとに `--where local|cloud` や `COMFY_WHERE` 環境変数で上書きするか、`comfy set-default --where cloud` で永続化できます。

## 

​

CLIのインストール

pip

homebrew
    
    
    pip install comfy-cli
    
    
    
    brew tap Comfy-Org/comfy-cli
    brew install comfy-org/comfy-cli/comfy-cli
    

シェルの自動補完を有効にするには、以下のコマンドを実行します：
    
    
    comfy --install-completion
    

## 

​

クイックセットアップ（推奨）

最新バージョンでの新機能: ルーティング、認証、エージェントスキルを1つのステップで処理する対話型ウィザードが追加されました。
    
    
    comfy setup
    

このウィザードでは、ルーティング先（ローカルまたはクラウド）の選択、**ブラウザ経由のサインイン（OAuth）** 、プロジェクトディレクトリの選択、そしてオプションでエージェントスキルのインストールを順に行います。推奨される方法です。ブラウザのサインインを自動で開くため、キーをコピーする必要はありません。
    
    
    comfy setup --where cloud
    

**非対話型（CIのみ）。** ブラウザOAuthには対話型セッションが必要です。CI、devcontainers、スクリプト化されたインストールなどブラウザが利用できない環境では、代わりにAPIキーを渡してください:
    
    
    comfy setup --where cloud --api-key comfyui-... --non-interactive
    

フラグ| 目的  
---|---  
`--where local|cloud`| ルーティング先。プロンプトをスキップ  
`--project-dir`| ワークフロー、入力、出力用のディレクトリ  
`--api-key`|  _(オプション)_ ヘッドレス/CI用のComfy Cloud APIキー。`--where cloud` を暗黙的に指定  
`-y, --non-interactive`| プロンプトなし。すべての設定をフラグで指定  
`--skip-skills`| エージェントスキルをインストールしない  
`--skip-verify`| 接続確認をスキップ  
  
## 

​

ComfyUI（ローカル）のインストール

Python 3.10 以上のバージョンで仮想環境を作成します。

conda

venv
    
    
    conda create -n comfy-env python=3.11
    conda activate comfy-env
    
    
    
    python3 -m venv comfy-env
    source comfy-env/bin/activate
    

ComfyUI のインストール
    
    
    comfy install
    

`comfy install` は使用する GPU を尋ね、それに合った PyTorch ビルドをインストールします。プロンプトに答えるか、フラグで GPU を指定して無人インストールできます：

プラットフォーム| `comfy install` がインストールするもの| 別途必要なもの  
---|---|---  
NVIDIA| CUDA runtime 付き PyTorch（pip ホイール）| 最新の GPU ドライバ（フルの CUDA Toolkit は不要）  
AMD Linux| ROCm PyTorch ホイール| それらのホイールに対応する ROCm 対応 AMD ドライバ／スタック  
AMD Windows| `torch-directml`| 互換 AMD GPU（DirectML。ROCm ではない）  
Apple silicon| PyTorch nightly ホイール（CPU インデックス；Metal/MPS）| Apple silicon 上の macOS  
Intel Arc| PyTorch XPU ホイール| 互換 Intel Arc GPU / XPU スタック  
CPU| CPU 向け PyTorch ホイール| 独立 GPU は不要  
  
## 

​

ComfyUIを実行する（ローカル）
    
    
    comfy launch
    

バックグラウンドで実行し、後で停止する：
    
    
    comfy launch --background
    comfy stop
    

どのワークスペースが選択済みで、何がインストール済みかを確認する：
    
    
    comfy which
    comfy env
    

## 

​

Comfy Cloud

Run workflows and partner nodes on Comfy’s hosted GPUs. No local install required.
    
    
    comfy cloud login          # browser OAuth + PKCE
    comfy cloud whoami         # show sign-in status, auth method, base URL
    comfy cloud logout         # clear the local session
    

Once signed in, commands auto-route to cloud. **Browser OAuth is the recommended path.** No keys to manage, and the CLI handles token refresh for you. To point at a custom environment (for example a PR preview) before signing in:
    
    
    comfy cloud set-base-url https://my-preview.comfy.org
    

**API key is optional.** You only need an API key for headless or CI use where a browser sign-in is not possible. It is a fallback, not the default:
    
    
    export COMFY_API_KEY=comfyui-...   # or pass --api-key per call
    

**Session lifetime.** Cloud session tokens are short-lived (~1h). The CLI auto-refreshes them on demand. If a command reports `cloud_unauthorized`, run `comfy cloud login` again.

## 

​

パートナーノードで生成

**`comfy generate` はベータ版です。** フラグ名、モデルエイリアス、出力形式が変更される可能性があります。基礎となるパートナーエンドポイントは安定しています。フィードバックは [comfy-cli GitHub リポジトリ](https://github.com/Comfy-Org/comfy-cli/issues) にお寄せください。

ターミナルまたはスクリプトから Comfy の[パートナーノード](https://docs.comfy.org/ja/tutorials/partner-nodes/overview)を呼び出す最も高速な方法です。ComfyUI ワークフローと同じホストされたエンドポイントを使用しますが、単一の CLI 呼び出しとして実行します。完全な ComfyUI グラフが不要なバッチジョブ、クイック実験、自動化に最適です。

### 

​

前提条件

  * `comfy cloud login` によるアクティブな Comfy Cloud セッション（ブラウザ OAuth）、**または** ヘッドレスや CI での使用のための [Comfy APIキー](https://docs.comfy.org/ja/development/api-development/getting-an-api-key)（`--api-key` / `COMFY_API_KEY`）
  * アカウントに [クレジット](https://docs.comfy.org/ja/interface/credits) があること
  * _オプション:_ [パートナーノードと呼び出しごとの価格をブラウズ](https://docs.comfy.org/ja/tutorials/partner-nodes/pricing)



### 

​

初めての生成
    
    
    comfy generate flux-pro \
        --prompt "a cat on the moon, cinematic lighting" \
        --width 1024 --height 1024 \
        --download cat.png
    

CLIはローカルファイルをアップロードし、ジョブを送信し、完了をポーリングし、結果を保存します。

モデルの実際のパラメータを事前に確認しましょう。フラグ名はモデルごとに異なります（例：`flux-ultra` は `--width`/`--height`、`seedance` は `--ratio`/`--resolution`/`--duration`）。スクリプト化する前に必ず確認してください：
    
    
    comfy generate schema flux-ultra
    

### 

​

よく使われるモデル

**Nano Banana（Google Gemini）：テキストから画像へと編集：**
    
    
    comfy generate nano-banana \
        --prompt "a watercolor of a sleeping fox" \
        --download fox.png
    
    # 画像編集：
    comfy generate nano-banana \
        --prompt "add a top hat" \
        --image ./cat.png \
        --download edited.png
    
    # モデルバリアントの指定：
    comfy generate nano-banana \
        --prompt "neon city skyline" \
        --model gemini-3-pro-image-preview \
        --download city.png
    

**FLUX 1.1 Pro Ultra：高解像度テキストから画像へ：**
    
    
    comfy generate flux-ultra \
        --prompt "a purple Victorian house in San Francisco, golden hour" \
        --width 896 --height 1152 --seed 11 \
        --download house.png
    

**Seedance（ByteDance）：テキストから動画へと画像から動画へ、最大1080p / 12秒：**
    
    
    # テキストから動画へ：
    comfy generate seedance \
        --prompt "a hummingbird hovering over a flower" \
        --resolution 1080p --duration 5 \
        --download hummingbird.mp4
    
    # 画像から動画へ（ローカル画像をアニメーション化、自動アップロード）：
    comfy generate seedance \
        --model seedance-1-0-pro-250528 \
        --image ./painting.png \
        --ratio 3:4 --resolution 1080p --duration 5 \
        --prompt "the painting gently comes alive, a soft breeze stirs the trees" \
        --download animated.mp4
    

**Grok（xAI）：画像とビデオ：**
    
    
    comfy generate grok --prompt "a cyberpunk street market at night" --download street.png
    comfy generate grok-edit --prompt "swap the umbrella for a parasol" --image ./photo.jpg --download out.png
    comfy generate grok-video --prompt "a paper plane gliding through a cathedral" --download flight.mp4
    

### 

​

モデルを見つける
    
    
    comfy generate list                            # すべてのモデル
    comfy generate list --category text-to-video   # カテゴリでフィルタ
    comfy generate list --partner kling            # パートナーでフィルタ
    comfy generate schema flux-kontext             # モデルのパラメータを表示
    

### 

​

参照画像を使った画像編集

ローカルファイルパスを渡します。CLIは、Comfyのストレージエンドポイントを介してアップロードするか、必要に応じてbase64エンコードします。
    
    
    comfy generate nano-banana \
        --prompt "add a top hat" \
        --image ./cat.png \
        --download edited.png
    
    comfy generate flux-kontext \
        --prompt "add a top hat and a monocle" \
        --input_image ./photo.jpg \
        --download out.png
    
    comfy generate ideogram-edit \
        --image cat.png --mask mask.png \
        --prompt "add sunglasses" \
        --rendering_speed TURBO \
        --download edited.png
    

1回アップロードして、複数の呼び出しで再利用するには：
    
    
    comfy generate upload ./photo.jpg     # prints a signed URL
    

アップロードされた参照アセットは**24時間** 後に自動削除されます。これらは署名付きURLを使用してComfy管理のGCSに保存されます。長時間実行されるパイプラインの場合は、各ジョブの前に再アップロードしてください。詳細については[リファレンス](https://docs.comfy.org/ja/comfy-cli/reference#upload)を参照してください。

### 

​

動画生成（非同期ジョブ）

ビデオジョブは非同期です。CLIはデフォルトでブロッキングしてポーリングします：
    
    
    comfy generate seedance \
        --prompt "a hummingbird hovering over a flower" \
        --resolution 1080p --duration 5 \
        --download hummingbird.mp4
    
    comfy generate kling \
        --prompt "a paper boat drifting on a river at dusk" \
        --duration 5 \
        --download boat.mp4
    

`--async` で即座に戻り、後で再開します：
    
    
    comfy generate luma --prompt "neon koi swimming through clouds" --aspect_ratio 16:9 --async
    # ジョブIDが表示されます。後で再開：
    comfy generate resume luma <job_id> --download out.mp4
    

### 

​

スクリプト用のJSON出力

パイプライン統合用に生の API レスポンスを出力：
    
    
    comfy generate dalle --prompt "a watercolor whale" --json | jq '.data[0].url'
    

コマンド、フラグ、モデルエイリアスの全リストについては[リファレンス](https://docs.comfy.org/ja/comfy-cli/reference)を参照してください。

## 

​

ワークフローの実行（`comfy run`）

単独のパートナー呼び出しを超えて、`comfy run` は完全な ComfyUI ワークフローグラフを送信します。API形式とエクスポートされたUI形式の両方のJSON（UIワークフローはクライアント側でAPI形式に変換されます）を受け付け、他のコマンドと同様にローカルまたはクラウドにルーティングします。デフォルトでは**非同期** で動作します。バックグラウンドのウォッチャーが進捗を追跡しつつ、ミリ秒単位で `prompt_id` を返します。ブロックして待機するには `--wait` を指定します。
    
    
    # 送信：即座に prompt_id を返す
    RES=$(comfy --json run --workflow my_workflow.json)
    PROMPT_ID=$(echo "$RES" | jq -r .data.prompt_id)
    
    # ターミナル状態になるまで監視し、出力を収集
    comfy --json jobs watch "$PROMPT_ID" | comfy download
    

単一のブロッキング呼び出しを希望しますか？ `--wait` を使用します：
    
    
    comfy run --workflow my_workflow.json --wait | comfy download
    

ジョブの追跡と管理：
    
    
    comfy jobs ls                 # ローカルの非同期送信 + サーバーのキュー/履歴
    comfy jobs status <prompt_id> # 1つのジョブ
    comfy jobs wait <id1> <id2>   # 全てがターミナル状態に達するまでブロック
    comfy jobs cancel <prompt_id> # べき等
    

送信前に検証しましょう。不明なノード、不足しているモデル、誤った配線を、クラウド計算を消費する前に発見します：
    
    
    comfy validate --workflow my_workflow.json
    

## 

​

テンプレートから始める

厳選された `Comfy-Org/workflow_templates` ギャラリーは、特定のタスクに対して既知の優れたワークフローを入手する最速の方法です。ゼロから構築する必要はありません。
    
    
    comfy templates ls --type image --tag "Text to Image"   # ブラウズ
    comfy templates show <name>                              # 完全なメタデータ
    comfy templates fetch <name> --out my.json               # ワークフローJSONを取得
    

ダウンロードされたJSONはフロントエンド形式です。`comfy run --where cloud` は送信時に自動的にAPI形式に変換します。

## 

​

ワークフローのその場編集

`comfy workflow` は、フロントエンド形式のワークフロー内でエージェントが調整可能なスロットを公開し、それらを上書きできるようにします。手動の JSON 編集は不要です。
    
    
    comfy workflow slots my.json                 # アドレス可能なスロットを一覧表示
    comfy workflow set-slot my.json 6.text="a fox in the snow"
    comfy workflow vary my.json \
        --slot positive.text='["a cat","a dog","a fox"]' \
        --out-dir ./variants                     # N個のバリエーションを生成
    

Comfy Cloud に保存されたワークフロー:
    
    
    comfy workflow list                          # 保存されたワークフローの一覧
    comfy workflow get <id> --out my.json
    comfy workflow save my.json --name "My Flow"
    comfy workflow delete <id>
    

複雑なマルチステップパイプラインでは、小さな再利用可能な断片を組み合わせて1つのグラフにします:
    
    
    comfy workflow compose blueprints/my_pipeline.yaml -o workflows/my_pipeline.json
    comfy workflow decompose my.json             # 逆: ワークフローを断片に分解
    

## 

​

ノードとモデルを発見する

解決済みのバックエンドで利用可能なすべてを詳細に確認します。 **ノード:**
    
    
    comfy nodes search "checkpoint"              # あいまい検索
    comfy nodes show KSampler                    # 完全なスキーマ：入力、出力、デフォルト値
    comfy nodes ls --produces IMAGE --limit 10   # 出力タイプでフィルタ
    comfy nodes ls --api-only                    # パートナーAPIノードのみ
    

**モデル:**
    
    
    comfy models list-folders                    # すべてのモデルフォルダー
    comfy models search --text "wan2.2" --type lora
    comfy models show wan2.2_vae.safetensors     # 完全なメタデータ
    

## 

​

ファイルのアップロードとダウンロード
    
    
    comfy upload photo.png video.mp4             # → サーバー入力ディレクトリ
    comfy download <prompt_id>                   # → ./outputs/
    

**慣用的なパイプ:**
    
    
     comfy run --workflow flux.json --wait | comfy download
    

`comfy download` は、パイプされた標準入力から prompt_id と出力URLを自動的に読み取ります。手動でキーを抽出したり、`jq` を使う必要はありません。

## 

​

カスタムノードの管理
    
    
    comfy node install <NODE_NAME>
    

このツールはカスタムノードのインストールに `cm-cli` を使用します。詳細は [ComfyUI Manager cm-cli ドキュメント](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/docs/en/cm-cli.md) を参照してください。

## 

​

モデルの管理（ローカル）

モデルを簡単にダウンロード：
    
    
    comfy model download --url <url> --relative-path models/checkpoints
    

## 

​

スクリプトとエージェント向けのJSON出力

すべてのコマンドは `--json` を受け付け、同一のエンベロープ形状を出力します。これにより、CLIは完全にスクリプト可能でエージェントフレンドリーになります。
    
    
    {
      "ok": true,
      "command": "...",
      "version": "1.11.1",
      "where": "local | cloud | null",
      "data": { },
      "error": null
    }
    

`error` が存在する場合は、`hint` を読み、それに従って行動します。
    
    
    comfy --json run --workflow my.json | jq '.error.hint'
    

エージェント向けのインターフェースは完全に自己記述的です。コマンドツリー全体、出力スキーマ、エラーコードをダンプします。
    
    
    comfy --json discover
    

## 

​

エージェントスキル

インストール済みのComfyエージェントスキルをClaude Code、Cursor、およびAGENTS.md対応ツールにインストールすると、コーディングエージェントがCLIを直接操作できるようになります：
    
    
    comfy skills install
    comfy skills list      # comfy, comfy-fragments, comfy-debug, comfy-relay, comfy-director
    comfy skills status    # what's installed where
    

これらは `comfy skills install` でインストールされる**バンドル済みCLIスキル** です。[Comfy Skills](https://github.com/Comfy-Org/comfy-skills/) リポジトリ（[Comfy Cloud MCP](https://docs.comfy.org/ja/agent-tools/mcp) 用の **comfy-cloud** Claude Codeプラグインをホスト）とは別のものです。

## 

​

コントリビューション

コントリビューションを歓迎します。[comfy-cli GitHub リポジトリ](https://github.com/Comfy-Org/comfy-cli/issues)でイシューを開くか、プルリクエストを送信してください。詳細は[開発ガイド](https://github.com/Comfy-Org/comfy-cli/blob/main/CONTRIBUTING.md)を参照してください。

## 

​

分析

使用状況の追跡はCLIの改善に役立ちます。以下のコマンドで無効にします：
    
    
    comfy tracking disable
    

追跡を再度有効にする：
    
    
    comfy tracking enable
    

また、`DO_NOT_TRACK` または `COMFY_NO_TELEMETRY` 環境変数を設定して、完全にオプトアウトすることもできます。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/comfy-cli/getting-started.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/comfy-cli/getting-started)

[Comfy Router で Chat Completions を使用する前へ](https://docs.comfy.org/ja/development/comfy-router/models/openrouter/chat-completions/code)[Comfy CLI コマンドリファレンス次へ](https://docs.comfy.org/ja/comfy-cli/reference)

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
