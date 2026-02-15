import torch
import torch.nn as nn


class RT2Minimal(nn.Module):
    def __init__(self, vocab_size: int = 32000, hidden_dim: int = 128, action_vocab_size: int = 256):
        super().__init__()
        self.vision = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(64, hidden_dim),
        )
        self.text = nn.Embedding(vocab_size, hidden_dim)
        self.decoder = nn.Linear(hidden_dim * 2, action_vocab_size)

    def forward(self, image: torch.Tensor, instruction_ids: torch.Tensor) -> torch.Tensor:
        v = self.vision(image)
        t = self.text(instruction_ids).mean(dim=1)
        return self.decoder(torch.cat([v, t], dim=1))
