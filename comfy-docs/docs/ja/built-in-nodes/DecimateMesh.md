---
url: https://docs.comfy.org/ja/built-in-nodes/DecimateMesh/
title: DecimateMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:38.455769+00:00
---

# DecimateMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/ja/built-in-nodes/DecimateMesh/

Mesh

# DecimateMesh - ComfyUI Built-in Node Documentation

ページをコピーページをコピー

3Dメッシュを、アクティブな計算デバイス上で計算を実行する QEM（二次誤差尺度）簡略化を用いて、目標面数まで簡略化します。

ページをコピーページをコピー

3Dメッシュを、アクティブな計算デバイス上で計算を実行する QEM（二次誤差尺度）簡略化を用いて、目標面数まで簡略化します。`"midpoint"` 配置モードは cumesh-faithful のプリセットで、髪の毛などの細い特徴を保持しながら最高品質を提供します。一方、`"qem"` は、オプションのラインおよび特徴エッジ制御を用いて、頂点を QEM 最適位置に配置します。出力メッシュは溶接された状態を維持します。

## 

​

入力

### 

​

共通入力

パラメータ| 説明| データ型| 必須| 範囲  
---|---|---|---|---  
`mesh`| 簡略化する3Dメッシュです。| MESH| はい| -  
`target_face_count`| 目標最大面数。0 で無効になります。（デフォルト: 200000）| INT| はい| 0 〜 50000000  
`placement_mode`| midpoint: cumesh-faithful（推奨）。qem: QEM 最適配置。（デフォルト: `"midpoint"`）| DYNAMIC_COMBO| はい| `"midpoint"`  
`"qem"`  
  
### 

​

Midpoint 入力

`"midpoint"` 配置モードでは追加のサブパラメータは公開されません。デフォルトの midpoint 配置プリセットを使用します。

### 

​

QEM 入力

以下のサブパラメータは、`placement_mode` が `"qem"` に設定されている場合にのみインターフェースに表示されます。

パラメータ| 説明| データ型| 必須| 範囲  
---|---|---|---|---  
`line_quadric_weight`| エッジごとのライン二次形式の重み。鋭い尾根/谷を保持します。0 = オフ。（デフォルト: 0.0）| FLOAT| いいえ| 0.0 〜 100.0  
`feature_edge_quadric_weight`| 二面角の特徴エッジ（折り目）に対する追加の二次形式重み。0 = オフ。（デフォルト: 0.0）| FLOAT| いいえ| 0.0 〜 1000.0  
`feature_edge_min_dihedral_deg`| エッジを特徴エッジとしてカウントするための最小二面角（度）。（デフォルト: 30.0）| FLOAT| いいえ| 0.0 〜 180.0  
`clamp_v_to_edge`| QEM 最適位置を、折りたたまれたエッジセグメント上に投影します。（デフォルト: true）| BOOLEAN| いいえ| `true`  
`false`  
  
注: `target_face_count` が 0 の場合、またはメッシュの面数がすでにターゲット以下である場合、間引きはスキップされます。このノードは自身に面数削減の概要を表示します。例: `faces: 1.23M → 200K (-84%)`。

## 

​

出力

出力名| 説明| データ型  
---|---|---  
`mesh`| 面数が削減された簡略化済みメッシュ。接続性は溶接された状態を維持します。| MESH  
  
> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/ja.md)

* * *

**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`

このページは役に立ちましたか？

はいいいえ

[編集を提案](https://github.com/comfy-org/docs/edit/main/ja/built-in-nodes/DecimateMesh.mdx)[問題を報告](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/ja/built-in-nodes/DecimateMesh)

[ComfyUI 組み込みノード前へ](https://docs.comfy.org/ja/built-in-nodes/overview)[FillHoles - ComfyUI Built-in Node Documentation次へ](https://docs.comfy.org/ja/built-in-nodes/FillHoles)

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
