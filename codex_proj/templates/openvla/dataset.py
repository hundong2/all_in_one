from dataclasses import dataclass
from typing import Dict


@dataclass
class OpenVLABatch:
    image: "torch.Tensor"
    token_ids: "torch.Tensor"
    action: "torch.Tensor"


class OpenVLADataset:
    """Dataset interface stub for OpenVLA-like multimodal training."""

    def __init__(self, image_size: int = 32, vocab_size: int = 1000, action_dim: int = 7):
        self.image_size = image_size
        self.vocab_size = vocab_size
        self.action_dim = action_dim

    def sample_batch(self, batch_size: int) -> Dict[str, "torch.Tensor"]:
        import torch

        return {
            "image": torch.randn(batch_size, 3, self.image_size, self.image_size),
            "token_ids": torch.randint(0, self.vocab_size, (batch_size, 16)),
            "action": torch.randn(batch_size, self.action_dim),
        }
