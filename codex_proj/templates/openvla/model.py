import torch
import torch.nn as nn


class OpenVLAMinimal(nn.Module):
    def __init__(self, vocab_size: int = 1000, hidden_dim: int = 128, action_dim: int = 7):
        super().__init__()
        self.vision = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(32, hidden_dim),
        )
        self.text = nn.Embedding(vocab_size, hidden_dim)
        self.head = nn.Sequential(
            nn.ReLU(),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, image: torch.Tensor, token_ids: torch.Tensor) -> torch.Tensor:
        visual = self.vision(image)
        textual = self.text(token_ids).mean(dim=1)
        fused = torch.cat([visual, textual], dim=1)
        return self.head(fused)
