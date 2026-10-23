---
url: https://docs.comfy.org/ja/development/api-development/quickstart/
title: \u521d\u3081\u3066\u306e\u30ef\u30fc\u30af\u30d5\u30ed\u30fc\u3092\u5b9f\u884c\u3059\u308b - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:47.166669+00:00
---

# 初めてのワークフローを実行する - ComfyUI

> Source: https://docs.comfy.org/ja/development/api-development/quickstart/

## このページの内容

  * 始める前に
  * 1\. サンプルをダウンロードする
  * 2\. SDKをインストールしてキーを設定する
  * 3\. 実行して結果を確認する
    * リクエストが失敗した場合
  * 4\. 独自の生成ワークフローを実行する



ワークフローの実行

# 初めてのワークフローを実行する

ページをコピーページをコピー

Comfy Cloud でサンプルワークフローを実行し、Python または TypeScript でその出力をダウンロードします。

ページをコピーページをコピー

コードから完全なワークフローを実行し、その出力を `first-result.png` として保存します。このサンプルでは、2 つの組み込みノードを使って **512 × 512 の単色の青い画像** を作成します。モデル、入力画像、カスタムノードを必要とせずに、認証、ワークフローの実行、出力のダウンロードを検証します。 ホストされたモデルを直接呼び出して画像を生成する場合は、[Comfy Router クイックスタート](https://docs.comfy.org/ja/development/comfy-router/quickstart)から始めてください。 このサンプルは Comfy Cloud 上で実行されます。Comfy API のデプロイやセルフホスティングなど、その他のホスティングオプションについては、[ComfyUI のデプロイ](https://docs.comfy.org/ja/development/deploy/overview)を参照してください。

## 

​

始める前に

  * [Comfy APIキー](https://docs.comfy.org/ja/development/api-development/getting-an-api-key)を用意します。
  * [有料のComfy Cloudサブスクリプション](https://docs.comfy.org/ja/development/deploy/cloud)が必要です。CloudのワークフローAPIアクセスは無料プランには含まれていません。
  * Python 3.10以降、またはTypeScriptの例を実行する場合はNode.js 22.18以降が必要です。

このガイドでは、SDKのデフォルトの接続先であるComfy Cloudを使用します。以前に `COMFY_BASE_URL` を設定している場合は、Cloudを使用するために設定を解除してください。既存のComfy APIデプロイメントやセルフホストインスタンスを使用する場合は、[ベースURLの選択](https://docs.comfy.org/ja/development/api-development/sdks#%E3%83%99%E3%83%BC%E3%82%B9url%E3%81%AE%E9%81%B8%E6%8A%9E)を参照してください。

## 

​

1\. サンプルをダウンロードする

例用のフォルダーを作成します。そのフォルダーに [workflow_api.json](https://docs.comfy.org/files/api-first-result/workflow_api.json) と、使用する言語のスクリプトをダウンロードしてください:

  * [Python: first_workflow.py](https://docs.comfy.org/files/api-first-result/first_workflow.py)
  * [TypeScript: first_workflow.mts](https://docs.comfy.org/files/api-first-result/first_workflow.mts)

ワークフローはすでに API 形式になっています。ノード `"1"` が青い画像を作成し、ノード `"2"` がそれを保存します。スクリプトはその SaveImage ノードから正確に出力を読み取るため、ノード ID を探したり編集したりする必要はありません。

## 

​

2\. SDKをインストールしてキーを設定する

ファイルを保存したフォルダーでターミナルを開きます。

Python

TypeScript
    
    
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install comfy-sdk
    
    
    
    npm init -y
    npm install @comfyorg/sdk
    

Windowsでは、PowerShellで `.venv\Scripts\Activate.ps1` を使ってPython環境を有効化します。 同じターミナルでキーを設定します:

macOS / Linux

Windows PowerShell
    
    
    export COMFY_API_KEY="comfyui-your-key"
    
    
    
    $env:COMFY_API_KEY = "comfyui-your-key"
    

APIキーはサーバー環境に保管してください。ブラウザーコードに含めたり、ソース管理にコミットしたりしないでください。

## 

​

3\. 実行して結果を確認する

Python

TypeScript
    
    
    python first_workflow.py
    
    
    
    node first_workflow.mts
    

スクリプトはワークフローを送信し、完了を待って、画像をダウンロードします。`Saved` に続いてパスが出力されたら、その場所にある `first-result.png` を開いてください。青一色の正方形が表示されるはずです。サンプルをもう一度実行すると、そのローカルファイルは置き換えられます。

これはワークフローの接続確認です。生成モデルは使用しません。同じ送信、待機、ダウンロードの手順は、独自の生成ワークフローでもそのまま使えます。

### 

​

リクエストが失敗した場合

  * **キーが不足している、または認証エラー:** スクリプトを実行しているターミナルで `COMFY_API_KEY` が設定されており、有効なキーが含まれていることを確認してください。
  * **アクセスまたはクレジットのエラー:** 再試行する前に、Cloud サブスクリプションと利用可能なクレジットを確認してください。
  * **ワークフローファイルが見つからない:** `workflow_api.json` をダウンロードしたスクリプトの隣に置いてください。
  * **予期しないエンドポイント:** `COMFY_BASE_URL` を確認してください。この Cloud の例では設定を解除してください。

エラーの処理とジョブの進捗については、[SDK ガイド](https://docs.comfy.org/ja/development/api-development/sdks)を参照してください。

## 

​

4\. 独自の生成ワークフローを実行する

ComfyUI エディタでワークフローを構築または選択し、そこで正常に実行してから、[API フォーマットでエクスポート](https://docs.comfy.org/ja/development/api-development/workflow-api-format)します。`workflow_api.json` をエクスポートしたファイルに置き換え、Python では `get_outputs("2")`、TypeScript では `getOutputs("2")` を、ワークフローの SaveImage ノード ID を使用するように更新します。対象の環境に、ワークフローが使用するモデルとカスタムノードが揃っていることを確認してください。 独自のモデルとカスタムノードでワークフローをホストするには、[Comfy API クイックスタート](https://docs.comfy.org/ja/development/serverless/quickstart)に従ってください。ワークフローの入力を変更する、ファイルをアップロードする、または進行状況を監視するには、[Comfy SDKs](https://docs.comfy.org/ja/development/api-development/sdks) に続けてください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/api-development/quickstart.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/api-development/quickstart)

[ワークフローの実行前へ](https://docs.comfy.org/ja/development/run-workflows/overview)[Comfy SDK：ComfyUI 向け Python・TypeScript クライアント次へ](https://docs.comfy.org/ja/development/api-development/sdks)

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
