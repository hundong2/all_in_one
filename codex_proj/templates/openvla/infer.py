import torch

from model import OpenVLAMinimal


def run_inference() -> torch.Tensor:
    model = OpenVLAMinimal()
    model.eval()
    with torch.no_grad():
        image = torch.randn(1, 3, 32, 32)
        token_ids = torch.randint(0, 1000, (1, 16))
        return model(image, token_ids)


if __name__ == "__main__":
    out = run_inference()
    print("action_pred_shape", tuple(out.shape))
