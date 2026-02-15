import torch
import torch.nn as nn


class DiffusionPolicyMinimal(nn.Module):
    def __init__(self, state_dim: int = 24, action_dim: int = 7, hidden_dim: int = 128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim + action_dim + 1, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, state: torch.Tensor, noisy_action: torch.Tensor, timestep: torch.Tensor) -> torch.Tensor:
        bsz, horizon, _ = state.shape
        t = timestep.unsqueeze(1).expand(bsz, horizon, 1) / 1000.0
        x = torch.cat([state, noisy_action, t], dim=-1)
        return self.net(x)
