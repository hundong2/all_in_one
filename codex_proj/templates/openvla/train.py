import torch
import torch.nn as nn
import torch.optim as optim

from dataset import OpenVLADataset
from model import OpenVLAMinimal


def train_step(batch_size: int = 4) -> float:
    dataset = OpenVLADataset()
    model = OpenVLAMinimal()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    batch = dataset.sample_batch(batch_size)
    pred = model(batch["image"], batch["token_ids"])
    loss = criterion(pred, batch["action"])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return float(loss.item())


if __name__ == "__main__":
    print(f"train_loss={train_step():.6f}")
