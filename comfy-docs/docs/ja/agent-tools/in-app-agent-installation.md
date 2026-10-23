---
url: https://docs.comfy.org/ja/agent-tools/in-app-agent-installation/
title: Comfy Agent \u3092\u306f\u3058\u3081\u308b - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:26.999061+00:00
---

# Comfy Agent をはじめる - ComfyUI

> Source: https://docs.comfy.org/ja/agent-tools/in-app-agent-installation/

## このページの内容

  * セットアップを選択
  * 最初の画像を作成する
    * Agent を開く
    * ワークフローを構築する
    * 画像を生成する
    * 変更を加える
  * トラブルシューティング
    * Agent ボタンが表示されない
    * Agent が想定したワークフローを編集できない
    * Agent が入力を求める
    * クラウドでローカルの会話が見つからない
  * 次のステップ



Agent Tools / MCP

# Comfy Agent をはじめる

ページをコピーページをコピー

Comfy Cloud または Comfy Desktop で Comfy Agent を開きます。

ページをコピーページをコピー

## 

​

セットアップを選択

Comfy アカウントが必要です。

  * **Comfy Cloud:** Comfy Agent は一般提供されています。ローカルへのインストールは不要で、ウェイトリストも必要ありません。[Cloud にログイン](https://cloud.comfy.org)。
  * **Comfy Desktop:** ローカル ComfyUI 向けの Comfy Agent は近日公開です。通知を受け取るには[ウェイトリストに参加してください](https://links.comfy.org/agentalpha)。



## 

​

最初の画像を作成する

### 

​

Agent を開く

空のワークフローを開き、タブバーの右端、アバターの隣にある **Agent** を選択します。プロンプトが表示されたら、同意通知を読んで承認します。Agent パネルの **Choose a workflow** を使用して、空のワークフローを選択します。

### 

​

ワークフローを構築する

次のメッセージを送信します：

> ニュートラルグレーの背景に赤いスニーカーを配置するテキストから画像へのワークフローを構築してください。利用可能なモデルを使用し、Save Image ノードを含めてください。ワークフローのエラーを確認してください。ただし、まだ実行しないでください。

Agent はキャンバス上にワークフローを構築し、プロンプトとモデル設定を入力し、ノードの接続と必須の入力を確認します。**Save Image** ノードで終わる、接続されたワークフローが表示されるはずです。 Agent が不足しているモデルまたはファイルを報告した場合は、それを用意するか、お使いのインストールで利用可能な代替を依頼してください。続行する前に、ワークフローを再度確認するよう依頼してください。

### 

​

画像を生成する

メッセージボックスの横にある **Run permissions** を開き、**Ask** を選択し、設定を変更した場合は **Save changes** を選択します。 「このワークフローを実行して」と送信します。Agent が承認を求めたら、**Run** を選択します。その実行を開始したくない場合は、代わりに **Cancel** を選択します。 生成が完了すると、Agent は会話内に出力を返します。画像は **Save Image** ノードにも表示されます。そこにある画像を右クリックすると、コンピューターに保存できます。

### 

​

変更を加える

「背景を白に変更し、モデルとその他の設定はそのままにしてください」と送信します。Agent は既存のワークフローを更新します。再度実行して結果を比較するよう依頼してください。

## 

​

トラブルシューティング

### 

​

Agent ボタンが表示されない

Comfy アカウントにログインしてください。Comfy Desktop では、[アプリケーションを更新](https://docs.comfy.org/ja/installation/update_comfyui)して再起動してください。それでもボタンが表示されない場合は、[サポート](https://docs.comfy.org/ja/support/contact-support)でアカウントの Agent アクセスを確認してください。

### 

​

Agent が想定したワークフローを編集できない

Agent パネルで目的のワークフローを選択し、メッセージを再送信してください。[編集するワークフローの選択](https://docs.comfy.org/ja/agent-tools/in-app-agent#%E7%B7%A8%E9%9B%86%E3%81%99%E3%82%8B%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC%E3%82%92%E9%81%B8%E6%8A%9E)を参照してください。

### 

​

Agent が入力を求める

**Attach a file** を選択するか、要求されたファイルをメッセージボックスにドラッグしてから、Agent に続行するよう依頼してください。

### 

​

クラウドでローカルの会話が見つからない

ローカルとクラウドの履歴は別々に管理されています。[データとプライバシー](https://docs.comfy.org/ja/agent-tools/in-app-agent-data-privacy#%E3%83%81%E3%83%A3%E3%83%83%E3%83%88%E5%B1%A5%E6%AD%B4%E3%81%A8%E5%90%8C%E6%9C%9F)を参照してください。

## 

​

次のステップ

## 既存のワークフローを編集する

プロンプト、モデル、処理ステップを変更します。

## 再利用可能なスキルを保存する

今後のリクエストのために指示を記憶します。

メッセージ、ファイル、会話がどこに保存されるかについては、[データとプライバシー](https://docs.comfy.org/ja/agent-tools/in-app-agent-data-privacy)を参照してください。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/agent-tools/in-app-agent-installation.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/agent-tools/in-app-agent-installation)

[Comfy Agent前へ](https://docs.comfy.org/ja/agent-tools/in-app-agent)[Comfy Agent スキル次へ](https://docs.comfy.org/ja/agent-tools/in-app-agent-skills)

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
