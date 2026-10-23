---
url: https://docs.comfy.org/ja/cloud-nodes/overview/
title: Comfy Cloud \u30ce\u30fc\u30c9 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:33.441536+00:00
---

# Comfy Cloud ノード - ComfyUI

> Source: https://docs.comfy.org/ja/cloud-nodes/overview/

## このページの内容

  * 概要
  * はじめに
  * 利用可能なノード
  * 課金
  * 制限事項
  * 関連リンク



Comfy Cloud ノード

# Comfy Cloud ノード

ページをコピーページをコピー

ローカルにインストールした ComfyUI から、Comfy Cloud の GPU 上でキュレーションされたワークフローを実行できます。サブスクリプションは不要です。

ページをコピーページをコピー

Comfy Cloud ノードは、ローカルマシンではなく Comfy 自身の GPU 上でジョブを実行するために送信する、通常の ComfyUI ノードです。他のノードと同じようにグラフに配置して使用します。サブスクリプションは不要で、他のパートナーノードと同様に、アカウントとクレジットがあれば十分です。

Comfy Cloud ノードはオープンソースモデルをクラウド上で実行します。パートナーノードと混同しないでください。

## 

​

概要

各 Comfy Cloud ノードは、ピン留めされたモデルバージョン上で1つの固定ワークフローを実行するため、保存したグラフは時間が経っても同じ結果を生成し続けます。ノードがジョブの実行のために送信するものを除き、グラフ、プロンプト、入力はお使いのマシン上に保持されます。

## 

​

はじめに

Comfy Cloud ノードは、ComfyUI **v0.34.5 以降** に同梱されています。ComfyUI コアの一部であるため、別途インストールする必要はありません。

1

ComfyUIをアップデート

v0.34.5 以降にアップデートしてください。ポータブル版、デスクトップ版、手動インストールの手順については、[ComfyUIのアップデート方法](https://docs.comfy.org/ja/installation/update_comfyui) を参照してください。

2

ComfyUIを再起動

ノードは起動時にのみ登録されるため、再起動するまで表示されません。

3

ノードを検索

ノードライブラリで **Comfy Cloud** を検索し、他のノードと同様にグラフに組み込みます。すべてのノードの表示名には `[BETA]` のサフィックスが付いています。

## 

​

利用可能なノード

ローンチ時点では、画像、ビデオ、オーディオにわたる8つのノードが用意されています。

ノード| モダリティ  
---|---  
Comfy Cloud Flux 2 Text to Image| 画像  
Comfy Cloud Mage Flow Text to Image| 画像  
Comfy Cloud Mage Flow Turbo Text to Image| 画像  
Comfy Cloud Z-Image Turbo Text to Image| 画像  
Comfy Cloud MiniMax H3 Text to Video| ビデオ  
Comfy Cloud MiniMax H3 Image to Video| ビデオ  
Comfy Cloud MiniMax H3 First-Last Frame to Video| ビデオ  
Comfy Cloud MiniMax Music 3 Text to Audio| オーディオ  
  
## 

​

課金

Comfy Cloud ノードは、GPU 秒ごとにクレジットで課金され、料金は実行前にノードに表示されます。サブスクリプションは不要で、月額の最低料金もありません。

## 

​

制限事項

  * 現時点では、独自の LoRA やチェックポイントの持ち込みには対応していません。各ノードは、ホストされた固定の重みセットを提供します。直接アップロードは次のステップとして計画されていますが、このリリースでは利用できません。



## 

​

関連リンク

  * [Comfy Cloud の料金](https://comfy.org/pricing)
  * [パートナーノードの概要](https://docs.comfy.org/ja/tutorials/partner-nodes/overview)（Comfy Cloud ノードとは別の、サードパーティー製 API ノードカタログ）



このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/cloud-nodes/overview.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/cloud-nodes/overview)

[VOID：ComfyUI ビデオ修復ワークフロー前へ](https://docs.comfy.org/ja/tutorials/utility/void-video-inpainting)[パートナー ノード次へ](https://docs.comfy.org/ja/tutorials/partner-nodes/overview)

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
