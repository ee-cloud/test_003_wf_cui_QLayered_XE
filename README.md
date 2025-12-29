
## 概要
Qwen-Image-Layeredを実行するためのテスト用ノードとテスト用ワークフローです。
ComfyUI (windows portable) 0.6.0、Diffusers 0.36.0.dev0 で動作確認。
VRAMの消費が少ない代わりに、メモリを約55GB使用するため実行にはご注意ください。
おそらくlow_vramをFalseにすると、VRAMを使用する代わりにメモリは抑えられると思います。（未確認）

## 簡易手順

### ComfyUI_windows_portable ディレクトリ上で、以下のコマンドを実行

.\python_embeded\python.exe -m pip uninstall -y diffusers
.\python_embeded\python.exe -m pip install --no-cache-dir git+https://github.com/huggingface/diffusers.git@f7753b1bc8b4b3b97dc7f71d51ccb3a281b17b48
.\python_embeded\python.exe -c "from diffusers import QwenImageLayeredPipeline; print('Success.')"
