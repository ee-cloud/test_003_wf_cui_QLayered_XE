# ComfyUI-QLayered-XE (Test)

Qwen-Image-LayeredをComfyUIで実行するためのカスタムノードおよびテスト用ワークフローです。

## 概要
画像をレイヤーごとに分解し、背景透過処理やPPTX形式での出力を目的としています。
非常に実験的なモデルのため、環境構築には特定の手順が必要です。

## 動作確認環境
- **ComfyUI**: Windows Portable版 v0.6.0
- **Diffusers**: 0.36.0.dev0 (Git開発版)
- **VRAM**: 16GB (RTX 4060 Ti) での動作を確認

## 注意事項
- **メモリ消費**: デフォルト（low_vram: True）では、VRAM消費を抑える代わりにメインメモリ（RAM）を**約55GB**使用します。
- **最適化**: `low_vram` を `False` に設定すると、VRAMを優先的に使用する代わりにRAM消費を抑えられる可能性があります。

## 簡易セットアップ手順
ComfyUIのルートディレクトリ（`ComfyUI_windows_portable`）にあるターミナル等で、以下のコマンドを順に実行してください。

```bash
# 既存のdiffusersをアンインストール
.\python_embeded\python.exe -m pip uninstall -y diffusers

# Qwen-Image-Layered対応の特定コミットをインストール
.\python_embeded\python.exe -m pip install --no-cache-dir git+https://github.com/huggingface/diffusers.git@f7753b1bc8b4b3b97dc7f71d51ccb3a281b17b48

# 正常にインストールされたかの確認
.\python_embeded\python.exe -c "from diffusers import QwenImageLayeredPipeline; print('Success.')"
```

- ・.\ComfyUI_windows_portable\ComfyUI\custom_nodes\ ディレクトリ内に，CompyUI-Qwen-Layered-xe ディレクトリを入れる。
- ・ComfyUI等を更新して再起動する。
- ・workflow.jsonを読み込む。
- ・画像ファイルを読込み，プロンプト等を設定して実行する。
