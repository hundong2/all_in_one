from typing import Dict


class DiffusionPolicyDataset:
    """Dataset interface stub for state-action trajectory chunks."""

    def __init__(self, state_dim: int = 24, action_dim: int = 7, horizon: int = 8):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.horizon = horizon

    def sample_batch(self, batch_size: int = 4) -> Dict[str, "torch.Tensor"]:
        import torch

        return {
            "state": torch.randn(batch_size, self.horizon, self.state_dim),
            "action": torch.randn(batch_size, self.horizon, self.action_dim),
            "noise": torch.randn(batch_size, self.horizon, self.action_dim),
            "timestep": torch.randint(0, 1000, (batch_size, 1)).float(),
        }
