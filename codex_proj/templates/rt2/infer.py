import torch

from model import RT2Minimal


def run_inference() -> int:
    model = RT2Minimal()
    model.eval()
    with torch.no_grad():
        image = torch.randn(1, 3, 64, 64)
        instruction_ids = torch.randint(0, 32000, (1, 24))
        logits = model(image, instruction_ids)
        return int(torch.argmax(logits, dim=1).item())


if __name__ == "__main__":
    print("predicted_action_token", run_inference())
