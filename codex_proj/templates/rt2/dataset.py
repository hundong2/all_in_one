from typing import Dict


class RT2Dataset:
    """Dataset interface stub for RT-2 style vision-language-action finetuning."""

    def __init__(self, vocab_size: int = 32000, action_vocab_size: int = 256):
        self.vocab_size = vocab_size
        self.action_vocab_size = action_vocab_size

    def sample_batch(self, batch_size: int = 4) -> Dict[str, "torch.Tensor"]:
        import torch

        return {
            "image": torch.randn(batch_size, 3, 64, 64),
            "instruction_ids": torch.randint(0, self.vocab_size, (batch_size, 24)),
            "action_token": torch.randint(0, self.action_vocab_size, (batch_size,)),
        }
