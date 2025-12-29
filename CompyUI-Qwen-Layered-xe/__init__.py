from .qwen_nodes import QwenLayeredLoader, QwenLayeredInference, QwenPPTXExport

NODE_CLASS_MAPPINGS = {
    "QwenLayeredLoader": QwenLayeredLoader,
    "QwenLayeredInference": QwenLayeredInference,
    "QwenPPTXExport": QwenPPTXExport
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QwenLayeredLoader": "Qwen Layered Model Loader",
    "QwenLayeredInference": "Qwen Layered Decomposition",
    "QwenPPTXExport": "Export Layers to PPTX"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
