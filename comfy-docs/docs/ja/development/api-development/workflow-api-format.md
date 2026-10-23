---
url: https://docs.comfy.org/ja/development/api-development/workflow-api-format/
title: \u30ef\u30fc\u30af\u30d5\u30ed\u30fc API \u5f62\u5f0f - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:52.508504+00:00
---

# ワークフロー API 形式 - ComfyUI

> Source: https://docs.comfy.org/ja/development/api-development/workflow-api-format/

## このページの内容

  * 保存形式 vs API 形式
  * エクスポート方法
  * 形式の変換
  * 関連ページ



ワークフローの実行

# ワークフロー API 形式

ページをコピーページをコピー

ComfyUI ワークフローの API 形式とそのエクスポート方法

ページをコピーページをコピー

ComfyUI ワークフローは、ノードのグラフを記述する JSON オブジェクトです。Cloud API や自身のサーバーを通じてプログラムから ComfyUI を呼び出す場合、ワークフローは**API 形式** で送信する必要があります。これはブラウザで使用される通常の保存形式とは異なる専用の JSON 構造です。 このページでは、両者の違いとワークフローを正しくエクスポートする方法を説明します。

* * *

## 

​

保存形式 vs API 形式

ComfyUI フロントエンドは 2 つの形式でワークフローを保存できます：

| 保存形式| API 形式  
---|---|---  
**メニュー**| `File → Save` または `Ctrl+S`| `File → Export Workflow (API)`  
**ファイル拡張子**| `.json`| `.json`  
**ノードキー**|  ノードタイトルまたはラベル| 数値ノード ID  
**ウィジェット値**|  含む| 含む  
**位置/レイアウトデータ**|  含む (x, y, width)| **含まない**  
**色/グループ**|  含む| **含まない**  
**用途**|  フロントエンドで再読み込み| API 送信用  
**UI に読み込み可能か**|  可| 可（ただしレイアウトなし）  
  
重要な違い：**API 形式は UI メタデータを省略** します（位置、色、グループ、ノードサイズ）。これらはフロントエンドでの視覚的編集にのみ必要なためです。これにより JSON がより小さく、プログラムでの使用に適した形になります。

* * *

## 

​

エクスポート方法

ComfyUI フロントエンドでワークフローを開き、`File → Export Workflow (API)` を選択します：

![API 形式でワークフローを保存](https://mintcdn.com/dripart/ozpqEvCuCvE4rrKe/images/development/export_workflow_api_format.png?fit=max&auto=format&n=ozpqEvCuCvE4rrKe&q=85&s=8a8d872f29df9d6a39326899c06714ed)

ComfyUI フロントエンドから API 形式でワークフローをエクスポート

これにより、API 関連データのみを含む `.json` ファイルがダウンロードされます：
    
    
    {
      "3": {
        "inputs": {
          "seed": 156680208700286,
          "steps": 20,
          "cfg": 8,
          "sampler_name": "euler",
          "scheduler": "normal",
          "denoise": 1,
          "model": [
            "4",
            0
          ],
          "positive": [
            "6",
            0
          ],
          "negative": [
            "7",
            0
          ],
          "latent_image": [
            "5",
            0
          ]
        },
        "class_type": "KSampler",
        "_meta": {
          "title": "KSampler"
        }
      },
      "4": {
        "inputs": {
          "ckpt_name": "v1-5-pruned-emaonly-fp16.safetensors"
        },
        "class_type": "CheckpointLoaderSimple",
        "_meta": {
          "title": "Load Checkpoint"
        }
      },
      "5": {
        "inputs": {
          "width": 512,
          "height": 512,
          "batch_size": 1
        },
        "class_type": "EmptyLatentImage",
        "_meta": {
          "title": "Empty Latent Image"
        }
      },
      "6": {
        "inputs": {
          "text": "beautiful scenery nature glass bottle landscape, , purple galaxy bottle,",
          "clip": [
            "4",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "7": {
        "inputs": {
          "text": "text, watermark",
          "clip": [
            "4",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "8": {
        "inputs": {
          "samples": [
            "3",
            0
          ],
          "vae": [
            "4",
            2
          ]
        },
        "class_type": "VAEDecode",
        "_meta": {
          "title": "VAE Decode"
        }
      },
      "9": {
        "inputs": {
          "filename_prefix": "ComfyUI",
          "images": [
            "8",
            0
          ]
        },
        "class_type": "SaveImage",
        "_meta": {
          "title": "Save Image"
        }
      }
    }
    

* * *

## 

​

形式の変換

保存形式のワークフローを API 形式に変換する最も簡単な方法：

  1. フロントエンドで `File → Load` から `.json` ファイルを開く
  2. `File → Export Workflow (API)` で再エクスポート

自動化が必要な場合は、各ノードの `x`、`y`、`width` フィールドを削除し、ルート JSON から `groups` と `extra` セクションを取り除くスクリプトを作成できます。

* * *

## 

​

関連ページ

  * [Cloud API 概要](https://docs.comfy.org/ja/development/cloud/overview) — Comfy Cloud に API 形式のワークフローを送信
  * [API 例](https://docs.comfy.org/ja/development/comfyui-server/api-examples) — API 形式ワークフローの実例
  * [API Key の取得](https://docs.comfy.org/ja/development/api-development/getting-an-api-key) — Cloud API と Partner Nodes に必要



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/development/api-development/workflow-api-format.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/development/api-development/workflow-api-format)

[設計ノート前へ](https://docs.comfy.org/ja/development/api-development/sdks-design)[ワークフローメタデータ次へ](https://docs.comfy.org/ja/development/api-development/workflow-metadata)

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
