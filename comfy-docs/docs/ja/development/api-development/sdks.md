---
url: https://docs.comfy.org/ja/development/api-development/sdks/
title: Comfy SDK\uff1aComfyUI \u5411\u3051 Python\u30fbTypeScript \u30af\u30e9\u30a4\u30a2\u30f3\u30c8 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:49.659016+00:00
---

# Comfy SDK：ComfyUI 向け Python・TypeScript クライアント - ComfyUI

> Source: https://docs.comfy.org/ja/development/api-development/sdks/

## このページの内容

  * インストール
  * クイックスタート
  * ベースURLの選択
    * Comfy Cloud
    * Comfy API デプロイ
    * ご自身のComfyUI
  * 送信のリトライ: 冪等キー
  * ジョブの実行を監視する
    * events() は subscribe() ではない
  * 出力を生成元のワークフローまで遡る
  * ジョブにラベルを付けて後で見つける
    * HTTP で使う
  * SDK が現在対応している範囲
  * リファレンス
  * フィードバック



ワークフローの実行

# Comfy SDK：ComfyUI 向け Python・TypeScript クライアント

ページをコピーページをコピー

Comfy Cloud、デプロイ環境、または自前の ComfyUI に対して Python または TypeScript から ComfyUI ワークフローを実行し、アセット、ジョブ、ライブイベント、冪等なリトライを扱います。

ページをコピーページをコピー

Comfy API v2 はバージョン管理されています。v2 内の変更は追加的なものに限られ、互換性を損なう変更は v3 で行われます。問題はフィードバックから報告してください。

**1つのパッケージ、2つのサーフェス。** `comfy-sdk`（PyPI）と `@comfyorg/sdk`（npm）は、2つの異なるサービスと通信する2つのクライアントを提供します。メソッド名は両者で重複して登場し（`run`、`submit`、`events`）、それぞれで意味が異なるため、スニペットをコピーする前に、それがどちらのクライアントを構築するものかを確認してください。

サーフェス| 機能| アクセス方法| ベースURL| 認証  
---|---|---|---|---  
**[Comfy Router](https://docs.comfy.org/ja/development/comfy-router/quickstart)**|  パートナーモデル（FLUX、Veo、Gemini、Kling）をそのプロバイダー自身のリクエストボディで呼び出し、ネイティブのレスポンスを返します| Python: `Comfy()` の `client.models`。TypeScript: モジュールレベルの `comfy` 名前空間の `comfy.models`| `https://api.comfy.org`、ルート `/v2/models/{provider}/{model}`| `COMFY_API_KEY`、または `comfy.config({ credentials })`  
**[Comfy Cloud と Comfy API v2](https://docs.comfy.org/ja/development/api-development/sdks)**|  API形式の ComfyUI ワークフローをエンドツーエンドで実行します: アセットのアップロード、グラフの送信、ジョブの追跡、出力のダウンロード| `Comfy(api_key=...)` / `new Comfy({ apiKey })`、続いて `client.workflows`、`client.assets`、`client.jobs`| デフォルトでは `https://cloud.comfy.org`、または `COMFY_BASE_URL` が指定するもの| コンストラクターの `api_key` / `apiKey`  
  
どちらのサーフェスも他方をラップしておらず、[あなたの Comfy ワークスペース](https://platform.comfy.org/profile/api-keys)で作成した1つの APIキーが両方で機能します。

2つの言語では Router サーフェスの公開の仕方が異なります。Python では `Comfy()` が両方を担います。Router には `client.models.run(...)`、Cloud には `client.workflows` / `client.assets` / `client.jobs` です。TypeScript ではこれらは意図的に似た名前を持つ別々のエクスポートです。`comfy`（小文字、モジュールレベルの名前空間）が `comfy.models` を持ち、一方 `Comfy`（クラス）は Cloud クライアントであり `.models` を持ちません。

このページでは2行目、つまりComfy CloudとComfy API v2クライアントについて説明します。モデルルーターについては、[Comfy Routerクイックスタート](https://docs.comfy.org/ja/development/comfy-router/quickstart)から始めてください。 Comfy SDKを使用すると、アプリケーションでComfyUIワークフローを実行し、結果を受け取ることができます。ワークフローを送信すると、ComfyUIがそれを実行し、出力をダウンロードできます。同じコードが、Comfy Cloudまたは自分でホストするComfyUIインスタンスに対して実行されます。変更されるのはベースURLのみです。ただし、ジョブのラベルは Comfy API デプロイでのみ使え、ジョブ一覧は Comfy Cloud ではまだ提供されていません。 SDKは、[Comfy API v2](https://docs.comfy.org/ja/api-reference/v2/overview)のクライアントです。これは、長期的にサポートする予定のバージョン管理されたHTTP APIです。ComfyUIの新しいリリースでも、それに基づいて構築された統合が壊れることはありません。 この方法で人々が構築するもの:

  * BlenderやKritaなど、別のアプリケーション内でコンテンツを生成するプラグイン
  * ユーザーに代わって生成を実行するコンシューマー向けアプリ
  * バッチパイプライン。たとえば、ビデオの全フレームに1つのワークフローを実行するなど
  * 同時に多くのワークフローを処理する必要があるバックエンドサービス



これらのSDKは、ComfyUIを**外部から** 操作します。**ComfyUIの内部で** 実行されるカスタムノードやフロントエンド拡張機能を記述している場合は、代わりに[カスタムノードの開発](https://docs.comfy.org/ja/custom-nodes/overview)を参照してください。これらは別のAPIセットです。

## 

​

インストール

Python

TypeScript
    
    
    pip install comfy-sdk
    
    
    
    npm i @comfyorg/sdk
    

Python 3.10 以降。Node 22 以降。

**現在のリリース: 0.5.0。** PyPI の [`comfy-sdk`](https://pypi.org/project/comfy-sdk/) と npm の [`@comfyorg/sdk`](https://www.npmjs.com/package/@comfyorg/sdk) は同時にリリースされ、バージョン番号を共有します。最新版をインストールする（`pip install comfy-sdk`、`npm install @comfyorg/sdk`）か、正確なピン留めではなく範囲を指定してください。この 2 つのエコシステムではその書き方が異なります。`comfy-sdk>=0.5` は下限であり、それ以降のマイナーバージョンも受け入れます。一方 `@comfyorg/sdk@^0.5` は `0.5.x` に対する npm の互換範囲で、`0.6.0` には到達しないため、新しいマイナーバージョンがリリースされたときはキャレット範囲を引き上げる必要があります。npm 側でも以降のマイナーバージョンを追跡したい場合は `@comfyorg/sdk@>=0.5.0` を使用してください。この注記が古くなっている場合は、レジストリのページが正式な情報です。

## 

​

クイックスタート

入力画像をアップロードし、ワークフローを実行して、結果をディスクに書き込みます。

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    # Comfy Cloud
    client = Comfy(api_key="comfyui-...")
    
    wf = client.workflows.from_file("workflow_api.json")
    
    asset = client.assets.from_file("photo.png")
    wf.set_input("10", "image", asset)
    
    job = client.run(wf)
    for output in job.get_outputs("9"):
        output.to_file(output.name)
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    // Comfy Cloud
    const client = new Comfy({ apiKey: "comfyui-..." });
    
    const wf = await client.workflows.fromFile("workflow_api.json");
    
    const asset = client.assets.fromFile("photo.png");
    wf.setInput("10", "image", asset);
    
    const job = await client.run(wf);
    await job.getOutputs("9")[0].toFile("out.png");
    

`workflow_api.json` は、[API 形式](https://docs.comfy.org/ja/development/api-development/workflow-api-format)で保存されたワークフローです。`"10"` と `"9"` はそのファイル内のノード ID です。入力画像が送り込まれるノードと、結果を取得したい出力ノードを指します。 アセットハンドルは遅延評価されます。`photo.png` はローカルでハッシュ化され、サーバーがそのバイトをまだ保持していない場合にのみアップロードされます。そのため、同じ入力を使用して再実行してもコストはかかりません。 `run()` はジョブを送信し、ターミナル状態に達するまで待機します。実行中に他の作業を行うには、代わりに `submit()` を使用し、イベントストリームを監視してください。 代わりに自分の ComfyUI に対して実行するには、`COMFY_BASE_URL` を設定してキーを削除します。以下を参照してください。

## 

​

ベースURLの選択

接続先| Base URL| APIキー  
---|---|---  
**Comfy Cloud**| `https://cloud.comfy.org` (デフォルト)| 必須  
**Comfy API デプロイ**| `https://<deployment>.run.comfy.app`| 必須  
**ご自身のComfyUI**| `http://127.0.0.1:8189` (ローカルプロキシ)| デフォルトでは不要。オプションの静的ベアラートークン  
  
ベースURLはコンストラクタ引数ではなく、`COMFY_BASE_URL`環境変数から取得されます:
    
    
    export COMFY_BASE_URL="https://<deployment>.run.comfy.app"  # Comfy API デプロイ
    export COMFY_BASE_URL="http://127.0.0.1:8189"               # セルフホストプロキシ
    

この変数はクライアントが構築されるたびに読み取られ、`http(s)` URLである必要があります。未設定または空白の場合はComfy Cloudを意味します。したがって、クライアント自体はどこでも同じです:

Python

TypeScript
    
    
    client = Comfy(api_key="comfyui-...")
    
    
    
    const client = new Comfy({ apiKey: "comfyui-..." });
    

初期ビルドからアップグレードしますか? `Comfy("<url>", "<key>")`は、`COMFY_BASE_URL`を設定した`Comfy(api_key="<key>")`になりました。`api_key`はキーワード専用引数なので、以前の位置引数での呼び出しは、URLをキーとして静かに読み取るのではなく、`TypeError`を発生させます。

### 

​

Comfy Cloud

そのまま動作します。[APIキー](https://docs.comfy.org/ja/development/api-development/getting-an-api-key)を作成し、クライアントに渡します。

APIアクセスには有料のComfy Cloudサブスクリプションが必要です。無料プランには含まれません。同時に実行できるジョブ数はプランによって異なります。[並列実行](https://docs.comfy.org/ja/development/deploy/cloud-usage#%E5%90%8C%E6%99%82%E5%AE%9F%E8%A1%8C%E3%82%B8%E3%83%A7%E3%83%96)をご覧ください。

### 

​

Comfy API デプロイ

[開発者プラットフォーム](https://platform.comfy.org)を通じてデプロイしたワークフローには、専用のエンドポイントが割り当てられます。`COMFY_BASE_URL`をそのエンドポイントに指定し、Comfy Cloudとまったく同じようにAPIキーを使用します。このガイドのすべてが同じように機能します。ただし、ジョブのラベルとジョブ一覧は Comfy Cloud ではまだサポートされていません。 Comfy APIデプロイは、そのBuildに含まれるモデルとカスタムノードを使用して複数のワークフローを実行できます。各ジョブについて、`get_workflow()`は`format: "api"`を持ち、実行されたグラフを`.graph`プロパティに含むワークフローレスポンスを返します。

### 

​

ご自身のComfyUI

セルフホスト環境では、v2 API は ComfyUI と一緒に動作する小規模なオープンソースサービス [comfy-api-proxy](https://github.com/Comfy-Org/comfy-api-proxy) によって提供されます。インストールして実行し、`COMFY_BASE_URL="http://127.0.0.1:8189"`を設定します:
    
    
    pip install comfy-api-proxy
    comfy-api-proxy
    export COMFY_BASE_URL="http://127.0.0.1:8189"
    

設定と認証については、[セルフホスト ComfyUI 用 API プロキシ](https://docs.comfy.org/ja/development/comfyui-server/api-proxy)を参照してください。

## 

​

送信のリトライ: 冪等キー

`submit()` と `run()` は送信のたびに `Idempotency-Key` を送り、そのキーに対する Comfy API v2 の契約は **複製時に拒否であり、記録して再生するものではない** 。送信をリトライループで包む前にこれを読んでほしい。

  * **呼び出しごとに新しいキーが発行される。** 同じワークフローで `submit()` を2回呼ぶと、2回の送信、2つのジョブ、2回の課金になる。`submit()` を素朴に `for attempt in range(3)` で囲むのはリトライではなく二重請求だ。
  * **再利用されたキーは拒否され、再生されない。** リトライを冪等にするには独自の `idempotency_key`（TypeScript では `idempotencyKey`）を渡すが、同じキーでの2回目のリクエストは最初のジョブを返す代わりに `422 idempotency_key_reuse` で失敗する。SDK は `IdempotencyKeyReuse` を送出する。これは通常の「冪等リトライ」の意味とは正反対なので、明示的に処理すること。
  * **復旧とはジョブを探しに行くことであり、再送信ではない。** `IdempotencyKeyReuse` では、最初の試行がジョブを作成している可能性が高い。`client.jobs.get(job_id)` で取得する。この検索にはすでに保存した id が必要なので、送信が戻り、失敗前に id を永続化していた場合にのみ復旧できる。id が記録される前に接続が切れた場合、検索するものがなく、自動復旧もない。以下の例は、確保されたキーで再送信するのではなく、手動処理のために再送出する。
  * **送信が明確に失敗したとき、キーは解放される。** 検証エラー、クレジット不足による拒否、キュー満杯による拒否はジョブを作成せずキーを解放するので、そのキーで再送信しても問題ない。 _曖昧な_ 失敗（読み取りタイムアウト、リクエスト途中での接続断）の後は、キーは確保されたままになる。再送信するのではなく、ジョブを探すこと。
  * **キーは24時間後に期限切れになる** また、空でなく、印刷可能な ASCII であり、長さの制限内でなければならない。無効なキーはリクエストが行われる前に `ValueError` を送出するので、明示的な `""` が暗黙的に発行されたキーにフォールバックすることはない。

したがって、複数回実行しても安全なリトライは、試行をまたいで2つのものを持ち運ぶ必要がある。キーは、サーバーがリトライと新しい送信を区別できるようにするため。ジョブID は、確保されたキーがすでに作成したジョブを見つけられるようにするためだ。

Python

TypeScript
    
    
    import uuid
    from comfy_sdk import IdempotencyKeyReuse
    
    # どちらの値も、そのリクエストがあなたにとって何を意味するかでキー付けした
    # 自分のストアに属する。`key` は最初の試行で一度だけ発行され、`job_id` は送信が
    # 戻り次第記入される。
    state = load_submission_state()  # {"key": ..., "job_id": ...} or {}
    key = state.get("key") or str(uuid.uuid4())
    save_submission_state(key=key)
    
    try:
        job = client.submit(wf, idempotency_key=key)
        save_submission_state(key=key, job_id=job.id)
    except IdempotencyKeyReuse:
        # このキーでの以前の試行がすでに送信に到達しているため、ジョブが
        # 存在する可能性がある。再送信しないこと。探しに行く。
        job_id = state.get("job_id")
        if job_id is None:
            raise  # 検索するために記録されたものがない。これは人間の対応が必要
        job = client.jobs.get(job_id)
    
    
    
    import { IdempotencyKeyReuse } from "@comfyorg/sdk";
    
    // どちらの値も、そのリクエストがあなたにとって何を意味するかでキー付けした
    // 自分のストアに属する。`key` は最初の試行で一度だけ発行され、`jobId` は送信が
    // 戻り次第記入される。
    const state = await loadSubmissionState(); // { key?, jobId? }
    const key = state.key ?? crypto.randomUUID();
    await saveSubmissionState({ key });
    
    let job;
    try {
      job = await client.submit(wf, { idempotencyKey: key });
      await saveSubmissionState({ key, jobId: job.id });
    } catch (err) {
      // このキーでの以前の試行がすでに送信に到達しているため、ジョブが
      // 存在する可能性がある。再送信しないこと。探しに行く。
      if (!(err instanceof IdempotencyKeyReuse) || !state.jobId) throw err;
      job = await client.jobs.get(state.jobId);
    }
    

`client.jobs.get(job_id)` は SDK の復元パスであり、id を必要とする。だからこそ、送信が戻った瞬間に id を記録することが、これを復旧可能にしている。`POST /api/v2/jobs` におけるキー契約の全体については [Comfy API v2](https://docs.comfy.org/ja/api-reference/v2/overview) を参照。

Comfy Router の `Idempotency-Key` は **異なる** 動作をする。Router ではキーは使い捨てトークンではなく再生ハンドルである。同じキーでキュー中の送信を再送すると、2つ目をキューに入れる代わりにオリジナルのリクエストを返す。[キューの冪等性と課金](https://docs.comfy.org/ja/development/comfy-router/queue#%E5%86%AA%E7%AD%89%E6%80%A7%E3%81%A8%E8%AA%B2%E9%87%91) と [Router のリトライ結果](https://docs.comfy.org/ja/development/comfy-router/errors#%E5%86%8D%E8%A9%A6%E8%A1%8C%E3%81%AE%E7%B5%90%E6%9E%9C) を参照。2つのサーフェスはヘッダー名を共有しているだけで、契約は共有していない。

## 

​

ジョブの実行を監視する

`job.events()` は、ジョブの状態のライブストリームを提供します。ノードとステップの進捗、プレビューフレーム、各出力がコミットされた瞬間のデータを取得できます。接続が切断された場合は、自動的に再接続されます。

Python

TypeScript
    
    
    from comfy_sdk import Progress, Preview, OutputReady, StatusChange
    
    job = client.submit(wf)
    
    for event in job.events():
        match event:
            case Progress() as p:
                print(f"{p.value:.0%} {p.message}")
            case Preview() as pv:
                image = pv.to_pil()
            case OutputReady() as o:
                o.output.to_file(f"partial/{o.output.name}")
            case StatusChange(status="succeeded"):
                break
    
    result = job.result()
    
    
    
    const job = await client.submit(wf);
    
    // ラベルは必須です。switch 内の単独の `break` は、ループではなく
    // switch を抜けてしまいます。
    eventLoop: for await (const event of job.events()) {
      switch (event.kind) {
        case "progress":
          console.log(event.value);
          break;
        case "outputReady":
          await event.output.toFile(`${event.output.name}`);
          break;
        case "statusChange":
          if (event.status === "succeeded") break eventLoop;
      }
    }
    

`Preview.to_pil()` にはオプションの Pillow extra が必要です: `pip install "comfy-sdk[pil]"`。 `result()` は、完了したジョブを返します。実行に失敗した場合は、ノードレベルの詳細情報を含む `JobFailed` を送出します。完全なイベントカタログについては、お使いの言語の SDK README を参照してください。

### 

​

`events()` は `subscribe()` ではない

似た名前のものが 2 つのサーフェスにまたがって 3 つ存在し、このページで扱うのはそのうちの 1 つだけです。

呼び出し| サーフェス| 得られるもの  
---|---|---  
`job.events()`| Comfy Cloud（このページ）| 1 つのワークフロージョブのライブ SSE ストリーム: `Progress`、`Preview`、`OutputReady`、`StatusChange`。自動再接続し、ポーリングにフォールバックします。  
`handle.events()`（TypeScript）/ `handle.iter_events()`（Python）| [Comfy Router のキュー配信](https://docs.comfy.org/ja/development/comfy-router/queue)| 1 つの Router リクエストに対するキューの監視: ステータスとキュー位置。ステータスルートをポーリングします。ストリームは存在せず、進捗イベントやプレビューイベントもありません。  
`comfy.models.subscribe(...)`| [Comfy Router のキュー配信](https://docs.comfy.org/ja/development/comfy-router/queue)| イテレータではありません。送信、ポーリング、収集を 1 回の呼び出しで行い、`on_queue_update` / `onQueueUpdate` コールバックを備え、結果を返します。  
  
Comfy Cloud クライアントに `subscribe()` はなく、どこにも `job.subscribe()` はありません。`subscribe` に相当する Cloud の機能は `run()` です。送信し、終了状態を待ちます。 ストリームはライブフィードであり、再生可能なログではありません。進捗を表示するためのものであり、結果の取得に依存するためのものではありません。ジョブのポーリングこそが信頼できる情報源であり、`run()`、`wait()`、`result()` は自動的にポーリングにフォールバックします。理由については、[設計ノート](https://docs.comfy.org/ja/development/api-development/sdks-design#%E3%81%BE%E3%81%9A%E3%83%9D%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0%E3%80%81%E9%80%B2%E6%8D%97%E3%81%AF%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%A0%E3%81%A7) を参照してください。

## 

​

出力を生成元のワークフローまで遡る

出力には、それを生成したジョブのIDが保持されています。そのため、サイドテーブルを保持しなくても、ファイルから逆方向に遡ることができます。

Python

TypeScript
    
    
    output = job.outputs[0]
    output.job_id          # the job that produced this file
    
    
    
    const output = job.outputs[0];
    output.jobId; // the job that produced this file
    

同じIDは、単体で取得したアセットにも付いています。後で見つけたファイルでも、そのジョブまで遡れます。アップロードしたアセットには生成元のジョブがないため、この値は`None`（TypeScriptでは`undefined`）になります。 ジョブから、その背後にあるワークフローを取得できます。これは、このプロセス内で送信したものではなく、IDで再水和されたジョブでも機能します。

Python

TypeScript
    
    
    wf = job.get_workflow()
    
    if wf.format == "save":
        ...  # the workflow as authored, canvas layout and Note nodes intact
    else:
        ...  # the executed API-format graph
    
    
    
    const wf = await job.getWorkflow();
    
    if (wf.format === "save") {
      // the workflow as authored, canvas layout and Note nodes intact
    } else {
      // the executed API-format graph
    }
    

**常に`format`で分岐してください。** 返ってくる形状は、ジョブがどのように送信されたかによって決まり、リクエストごとに制御できるものではありません。

`format`| 取得できるもの| ケース  
---|---|---  
`save`| ジョブが実行されたバージョンの作成時ワークフロー。キャンバスレイアウトとNoteなどのエディタ専用ノードを含みます| Comfy Cloudエディタから送信されたジョブ。ワークフローバージョンが固定されています  
`api`| 実行されたグラフ。エディタ専用の構成要素は除去され、Get/Setノードは展開されています| その他すべて（今日これらのSDKを通じて送信されるすべてのジョブを含みます）  
  
SDKを通じて送信したジョブは常に`api`を返します。v2送信にはバージョン固定フィールドがまだないためです。この動作は将来変更されます。判別子が用意されているのは、コード側の変更が不要になるようにするためです。

## 

​

ジョブにラベルを付けて後で見つける

ラベルは、ジョブを送信するときに付けるキーと値の組です。たとえば `client: acme` や `project: spring` です。ラベルを使うと、ジョブがどのクライアントやプロジェクトのために実行されたかを記録できます。そうすれば、ジョブ ID の対応表を自前で持たなくても、1 つのクライアントのジョブを一覧できます。ラベルとジョブ一覧には、現在の SDK リリース（インストールのバージョン注記に記載されているもの）が必要です。 ラベルは Comfy API デプロイに送信したジョブで使えます。そのため、ベースURLの選択で示したとおり、`COMFY_BASE_URL` をデプロイのアドレスに設定してください。Comfy Cloud は現時点ではラベルを受け付けず、ジョブ一覧には `501` とコード `not_implemented` を返します。セルフホストの comfy-api-proxy もラベルを保持しません。proxy 独自の `metadata` フィールドは 1 つのテキスト文字列なので、ラベルのマップを拒否します。proxy のジョブ一覧はラベルによる絞り込みを無視するため、そこではラベルを指定した SDK の一覧呼び出しはジョブを 1 件も返さず、HTTP で同じフィルターを送るとすべてのジョブが返ります。 制限:

  * 1 つのジョブに付けられるラベルは最大 16 個です。
  * キーは 1〜40 文字で、使える文字は英字、数字、`_`、`-`、`.` です。
  * 値は最大 256 バイト（UTF-8）の文字列です。
  * ラベルはジョブの送信時に設定され、後から変更できません。

制限に違反した送信は `422`、コード `metadata_invalid` で失敗し、ジョブは作成されません。エラーメッセージには、違反したキーが示されます。ラベルが 16 個を超える場合は、その数が示されます。SDK 自体は制限を確認しません。サーバーのコードとメッセージを含むエラーを送出します。

ワークスペース内でジョブを閲覧できる人は誰でも、そのラベルも閲覧できます。シークレットや個人データをラベルに入れないでください。

送信時に `metadata` を渡します。ジョブを読み戻すと、ラベルが付いています。

Python

TypeScript
    
    
    job = client.submit(wf, metadata={"client": "acme", "project": "spring"})
    job.metadata  # {"client": "acme", "project": "spring"}
    
    
    
    const job = await client.submit(wf, {
      metadata: { client: "acme", project: "spring" },
    });
    job.metadata; // { client: "acme", project: "spring" }
    

ラベルなしで送信したジョブの `metadata` は空です。 1 つのクライアントのジョブを見つけるには、ラベルで絞り込んでジョブを一覧します。一覧に含まれるのは、ベースURLのデプロイに送信したジョブだけです。結果は新しい順に返り、反復するにつれて SDK が次のページを取得します。

Python

TypeScript
    
    
    for job in client.list_jobs(metadata={"client": "acme"}):
        print(job.id, job.status)
    
    
    
    for await (const job of client.listJobs({ metadata: { client: "acme" } })) {
      console.log(job.id, job.status);
    }
    

一度に絞り込めるラベルは最大 3 個で、ジョブはそのすべてに完全一致する必要があります。一覧の項目には出力が含まれません。ジョブの出力を取得するには、`client.jobs.get(job.id)` で ID からジョブを読み取ってください。

### 

​

HTTP で使う

`POST /api/v2/jobs` の本文で `metadata` を送ります。
    
    
    curl -X POST "https://<deployment>.run.comfy.app/api/v2/jobs" \
      -H "Authorization: Bearer $COMFY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "workflow": { ... },
        "metadata": { "client": "acme", "project": "spring" }
      }'
    

`GET /api/v2/jobs` は、ラベルごとに 1 つの `metadata[<key>]=<value>` クエリパラメーターで絞り込みます。`-g` フラグを付けると、curl は角かっこをパターンとして解釈しません。
    
    
    curl -g "https://<deployment>.run.comfy.app/api/v2/jobs?metadata[client]=acme" \
      -H "Authorization: Bearer $COMFY_API_KEY"
    

レスポンスには 1 ページ分のジョブと、続きのページがある場合は `next_cursor` が含まれます。次のページを取得するには、それを `cursor` として、同じ `metadata[...]` フィルターと一緒に渡します。フィルターなしで送ったカーソルは、絞り込まれていないジョブを返します。ページサイズは `limit` で設定します（最大 500）。
    
    
    {
      "jobs": [
        {
          "id": "6f1c2b9e-...",
          "status": "succeeded",
          "metadata": { "client": "acme", "project": "spring" }
        }
      ],
      "next_cursor": "eyJ..."
    }
    

ラベルの絞り込みが 3 個を超える場合や、キーの規則に違反するキーを指定した場合は、`400`、コード `invalid_metadata_filter` で失敗します。ジョブと一覧のすべてのフィールドについては、[Comfy API v2 リファレンス](https://docs.comfy.org/ja/api-reference/v2/overview)を参照してください。

## 

​

SDK が現在対応している範囲

最初のバージョンは、1つのことをきちんと行います。ワークフローを実行して結果を取得することです。

  * **アセット:** ファイル、バイト、ストリーム、または URL から入力ハンドルを作成します。ハンドルは遅延評価され、コンテンツアドレス方式のため、同じ入力で再実行しても再アップロードされません。
  * **送信:** API 形式のグラフを送信します。送信は冪等であり、キューが満杯の場合も、限られた予算内で自動的に再試行されます。
  * **実行:** `wait()` でポーリングするか、`events()` でリアルタイムの進捗を追跡します。
  * **出力:** ディスクに書き込む、メモリにバッファリングする、バイト範囲を取得する、または短期間有効なダウンロード URL を取得します。`getDownloadUrl()` は、APIキーなしで誰でも読み取れる署名付き URL を返し、有効期間はおよそ 6 時間です。保存する前に [出力 URL とその有効期間](https://docs.comfy.org/ja/api-reference/v2/overview#%E5%87%BA%E5%8A%9Burl%E3%81%A8%E3%81%9D%E3%81%AE%E6%9C%89%E5%8A%B9%E6%9C%9F%E9%96%93) を読んでください。後で出力を表示し続けるには、バイトを再ホストするか、必要に応じて URL を再発行します。
  * **トレーサビリティ:** すべての出力には、それを生成したジョブの ID が含まれ、ジョブからその背後にあるワークフローを取得することもできます。
  * **アセットの削除:** アップロードしたアセットを、ハンドルまたは ID で削除します。
  * **エラー:** 生のステータスコードではなく、`JobFailed`、`Unauthorized`、`InsufficientCredits`、`QueueFull` などの型付き例外。
  * **キャンセル:** 実行中のジョブをキャンセルできます。TypeScript では、任意の呼び出しで `AbortSignal` も受け付けます。

Python には、同期 `Comfy` クライアントと、同じインターフェースを持つ `AsyncComfy` クライアントの両方が用意されています。TypeScript は非同期のみです。 このバージョンには含まれないもの: 保存したワークフローの管理、モデルライブラリ、ノードのイントロスペクション、名前付きワークフローパラメータ。[設計ノート](https://docs.comfy.org/ja/development/api-development/sdks-design#%E6%9C%80%E5%88%9D%E3%81%AE%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%81%AE%E7%AF%84%E5%9B%B2) では、なぜ API サーフェスがこのように小さく始まるのかを説明しています。

## 

​

リファレンス

SDK の README は、各言語の完全なリファレンスです。認証、アセット、エラー、および低レベルのエスケープハッチを含みます。

## Python SDK

`comfy-sdk` を PyPI で公開。同期・非同期クライアント。

## TypeScript SDK

`@comfyorg/sdk` を npm で公開。型付き・非同期、低レベルクライアントを備えています。

## Comfy API v2 リファレンス

両方のSDKの基盤となるHTTP API。任意の言語から直接使用できます。

## 設計ノート

このAPIが存在する理由、既存のComfyUI APIとの関係、今後の予定。

## Comfy Router

同じパッケージのもう一つのサーフェス: Flux、Veo、Gemini などのパートナーモデルに対して `comfy.models.run` を実行します。

## 

​

フィードバック

SDK と API へのフィードバックをお待ちしています。使いにくい点、見つけられなかった情報、回避策が必要だったことをお知らせください。 扱いにくい点、期待していたのに見つからなかったもの、回避策で対応せざるを得なかったことを報告してください。[私たちのDiscord](https://discord.com/invite/comfyorg)の`#developer-platform`チャンネルがその報告の場所です。 別の言語のファーストパーティ SDK が必要な場合は、そこでその旨をお伝えください。両方の SDK は同じ文書化された HTTP 契約に基づいているため、今日の時点であらゆる言語が API と通信できますが、どこに需要があるのかを把握したいと考えています。

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/api-development/sdks.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/api-development/sdks)

[初めてのワークフローを実行する前へ](https://docs.comfy.org/ja/development/api-development/quickstart)[セルフホスト ComfyUI 用の API プロキシ次へ](https://docs.comfy.org/ja/development/comfyui-server/api-proxy)

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
