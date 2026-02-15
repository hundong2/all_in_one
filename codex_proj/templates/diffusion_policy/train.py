import torch
import torch.nn as nn
import torch.optim as optim

from dataset import DiffusionPolicyDataset
from model import DiffusionPolicyMinimal


def train_step(batch_size: int = 4) -> float:
    dataset = DiffusionPolicyDataset()
    model = DiffusionPolicyMinimal()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    batch = dataset.sample_batch(batch_size)
    pred_noise = model(batch["state"], batch["action"] + batch["noise"], batch["timestep"])
    loss = criterion(pred_noise, batch["noise"])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return float(loss.item())


if __name__ == "__main__":
    print(f"train_loss={train_step():.6f}")
