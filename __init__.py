
from .nodes.comfy_nodes import EasyControlLoadFlux, EasyControlLoadLora, EasyControlLoadMultiLora, EasyControlGenerate


# 注册节点
NODE_CLASS_MAPPINGS = {
    "EasyControlLoadFlux": EasyControlLoadFlux,
    "EasyControlLoadLora": EasyControlLoadLora,
    "EasyControlLoadMultiLora": EasyControlLoadMultiLora,
    "EasyControlGenerate": EasyControlGenerate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EasyControlLoadFlux": "Load EasyControl Flux Model",
    "EasyControlLoadLora": "Load EasyControl Lora",
    "EasyControlLoadMultiLora": "Load Multiple EasyControl Loras",
    "EasyControlGenerate": "EasyControl Generate",
} 
WEB_DIRECTORY = "./web"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', "WEB_DIRECTORY"]