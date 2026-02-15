import torch

from model import DiffusionPolicyMinimal


def run_inference() -> torch.Tensor:
    model = DiffusionPolicyMinimal()
    model.eval()
    with torch.no_grad():
        state = torch.randn(1, 8, 24)
        noisy_action = torch.randn(1, 8, 7)
        timestep = torch.tensor([[100.0]])
        denoised = model(state, noisy_action, timestep)
        return denoised


if __name__ == "__main__":
    out = run_inference()
    print("denoised_shape", tuple(out.shape))
