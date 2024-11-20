from abc import ABC, abstractmethod

class LoraResolver(ABC):

    @abstractmethod
    async def resolve_lora(self, lora_name: str):
        """
        Abstract method to resolve and possibly download a Lora model on the fly.
        lora_name: str - the name of the lora model to resolve
        This should ideally return a LoRARequest
        """
        pass