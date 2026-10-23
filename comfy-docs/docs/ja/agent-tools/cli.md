---
url: https://docs.comfy.org/ja/agent-tools/cli/
title: Comfy CLI\uff1a\u30bf\u30fc\u30df\u30ca\u30eb\u304b\u3089 ComfyUI \u3092\u5b9f\u884c - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:25.694961+00:00
---

# Comfy CLI：ターミナルから ComfyUI を実行 - ComfyUI

> Source: https://docs.comfy.org/ja/agent-tools/cli/

## このページの内容

  * MCPとの連携
  * CLIの機能
  * インストールとセットアップ
  * comfy generate の前提条件
  * 最初の生成
  * 利用可能なモデル
  * 使用例
    * テキストから画像へ
    * 画像編集（参照画像）
    * テキストから動画へ
    * JSONでのスクリプティング
  * comfy generate の先へ
  * エージェントスキル
  * 関連リソース
  * フィードバック



Agent Tools / MCP

# Comfy CLI：ターミナルから ComfyUI を実行

ページをコピーページをコピー

ターミナルからComfyを操作：ローカルComfyUI、パートナー生成呼び出し、Comfy Cloud上の完全なワークフロー。スクリプト、CI、自動化でMCPを補完します。

ページをコピーページをコピー

[comfy-cli](https://github.com/Comfy-Org/comfy-cli) はComfyのコマンドラインツールです。[MCPサーバー](https://docs.comfy.org/ja/agent-tools)と並んで、エージェントや開発者にUI外からComfyを操作するもう一つの方法を提供します。 **ターミナルまたはスクリプトからアクセス** する場合に使用します。バッチジョブ、CIパイプライン、ワークフローの自動化、バンドルされたCLIスキルを介したコーディングエージェントとの連携に最適です。

**エージェント向けクイックリファレンス。** このページは簡略化された概要です。MCPと共に方向性を掴み、一般的な `comfy generate` 呼び出しを実行するのに十分な内容です。完全なCLIドキュメント（ローカルインストール、`comfy setup`、`comfy run`、テンプレート、ワークフロー編集、ノード/モデルの発見など）については、[Comfy CLI はじめに](https://docs.comfy.org/ja/comfy-cli/getting-started)を参照してください。

**`comfy generate` はベータ版です。** フラグ名、モデルエイリアス、出力形式が変更される可能性があります。基礎となるパートナーエンドポイントは安定しています。フィードバックは [comfy-cli GitHub リポジトリ](https://github.com/Comfy-Org/comfy-cli/issues) にお寄せください。

## 

​

MCPとの連携

| Comfy MCP（クラウド）| Comfy CLI  
---|---|---  
**インターフェース**|  MCPクライアント（Claude Code、Claude Desktopなど）とのチャット| ターミナルコマンドとスクリプト  
**最適な用途**|  チャットでの対話的なエージェントワークフロー| 自動化、バッチ実行、CI、シェルパイプライン  
**認証**|  MCPクライアントのOAuth、またはAPIキー（ヘッドレス）| `comfy cloud login`（OAuth）またはAPIキー（CI）  
**出力**|  チャットセッション内に返される| ディスクに保存（`--download`）またはJSON（`--json`）  
  
MCPのセットアップ、インストール、ツール一覧、認証方法については、[Comfy MCP](https://docs.comfy.org/ja/agent-tools/mcp) を参照してください。

## 

​

CLIの機能

  1. **ローカルComfyUI** — インストール、起動、更新、カスタムノードの管理
  2. **パートナー生成** — `comfy generate` で画像・動画・オーディオ・3DパートナーAPIをワンショットで呼び出し
  3. **クラウドワークフロー** — `comfy run`、テンプレート、スロット編集、Comfy Cloudでのジョブ監視



**2つのサーフェス、1つのCLI。** すべてのコマンドは自動的に実行場所を検出します。Comfy Cloud にサインインしている場合、コマンドは **クラウド** にルーティングされます。それ以外の場合は、**ローカル** サーバーに対して実行されます。コールごとに `--where local|cloud` や `COMFY_WHERE` 環境変数で上書きするか、`comfy set-default --where cloud` で永続化できます。

## 

​

インストールとセットアップ

pip

homebrew
    
    
    pip install comfy-cli
    
    
    
    brew tap Comfy-Org/comfy-cli
    brew install comfy-org/comfy-cli/comfy-cli
    

シェルの自動補完を有効にするには、以下のコマンドを実行します：
    
    
    comfy --install-completion
    
    
    
    comfy setup
    

CIやスクリプトでの非対話型インストールには `-y` を渡します。完全な `comfy setup` フラグテーブルについては [Comfy CLI はじめに](https://docs.comfy.org/ja/comfy-cli/getting-started#%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%EF%BC%88%E6%8E%A8%E5%A5%A8%EF%BC%89) を参照してください。 Comfy Cloudにログイン:
    
    
    comfy cloud login
    comfy cloud whoami
    

## 

​

`comfy generate` の前提条件

  * `comfy cloud login` によるアクティブな Comfy Cloud セッション（ブラウザ OAuth）、**または** ヘッドレスや CI での使用のための [Comfy APIキー](https://docs.comfy.org/ja/development/api-development/getting-an-api-key)（`--api-key` / `COMFY_API_KEY`）
  * アカウントに [クレジット](https://docs.comfy.org/ja/interface/credits) があること
  * _オプション:_ [パートナーノードと呼び出しごとの価格をブラウズ](https://docs.comfy.org/ja/tutorials/partner-nodes/pricing)



## 

​

最初の生成
    
    
    comfy generate flux-pro \
        --prompt "a cat on the moon, cinematic lighting" \
        --width 1024 --height 1024 \
        --download cat.png
    

CLIはローカルファイルをアップロードし、ジョブを送信し、完了をポーリングし、結果を保存します。

## 

​

利用可能なモデル

`comfy generate` は画像および動画のパートナーモデルをカバーします。お使いのCLIバージョンで利用可能なモデルを確認:
    
    
    comfy generate list                            # すべてのモデル
    comfy generate list --category text-to-video   # カテゴリでフィルタ
    comfy generate list --partner kling            # パートナーでフィルタ
    comfy generate schema flux-kontext             # 1つのモデルのパラメータ
    

一般的なエイリアス:

カテゴリ| 例  
---|---  
**画像**| `flux-pro`, `flux-ultra`, `flux-kontext`, `nano-banana`, `grok`, `grok-edit`, `ideogram-edit`, `dalle`, `recraft`, `stability`  
**動画**| `seedance`, `kling`, `luma`, `runway`, `pika`, `vidu`, `hailuo`, `moonvalley`, `grok-video`  
  
`comfy generate list` を実行して、お使いの環境の全セットを確認してください。

## 

​

使用例

### 

​

テキストから画像へ
    
    
    comfy generate nano-banana \
        --prompt "a watercolor of a sleeping fox" \
        --download fox.png
    

### 

​

画像編集（参照画像）

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

テキストから動画へ

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

JSONでのスクリプティング
    
    
    comfy generate dalle --prompt "a watercolor whale" --json | jq '.data[0].url'
    

## 

​

`comfy generate` の先へ

ここまではエージェント向けの概要です。完全なガイドでは各コマンドを詳しく説明しています：

  * `comfy run`、`comfy jobs`、`comfy validate`（完全なワークフロー用）
  * `comfy templates` と `comfy workflow` スロット編集
  * `comfy nodes` / `comfy models` の検出
  * `--json` エンベロープと `comfy --json discover`（エージェント向け）

→ [Comfy CLI はじめに](https://docs.comfy.org/ja/comfy-cli/getting-started)（完全なドキュメント）

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

関連リソース

リソース| 用途  
---|---  
[Comfy CLI はじめに](https://docs.comfy.org/ja/comfy-cli/getting-started)| 完全なインストールガイドとコマンドの解説  
[Comfy CLI リファレンス](https://docs.comfy.org/ja/comfy-cli/reference)| コマンド、フラグ、モデルエイリアス  
[Comfy MCP](https://docs.comfy.org/ja/agent-tools/mcp)| MCP経由でエージェントを接続し、チャット駆動の生成を行う  
[GitHub の comfy-cli](https://github.com/Comfy-Org/comfy-cli)| ソースリポジトリ、Issue、最新の動作  
  
## 

​

フィードバック

  * **GitHub** : [comfy-cli issues](https://github.com/Comfy-Org/comfy-cli/issues)
  * **Discord** : [#comfy-mcp-and-cli](https://discord.gg/xWJn6nhE3R)



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/agent-tools/cli.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/agent-tools/cli)

[Comfy MCP：AIエージェントをComfyUIに接続前へ](https://docs.comfy.org/ja/agent-tools/mcp)[Comfy Agent次へ](https://docs.comfy.org/ja/agent-tools/in-app-agent)

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
