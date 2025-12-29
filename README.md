### ComfyUI_windows_portable ディレクトリ上でコマンド実行

.\python_embeded\python.exe -m pip uninstall -y diffusers
.\python_embeded\python.exe -m pip install --no-cache-dir git+https://github.com/huggingface/diffusers.git@f7753b1bc8b4b3b97dc7f71d51ccb3a281b17b48
.\python_embeded\python.exe -c "from diffusers import QwenImageLayeredPipeline; print('Success.')"
