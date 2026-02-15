import torch
import torch.nn as nn
import torch.optim as optim

from dataset import RT2Dataset
from model import RT2Minimal


def train_step(batch_size: int = 4) -> float:
    dataset = RT2Dataset()
    model = RT2Minimal()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()

    batch = dataset.sample_batch(batch_size)
    logits = model(batch["image"], batch["instruction_ids"])
    loss = criterion(logits, batch["action_token"])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return float(loss.item())


if __name__ == "__main__":
    print(f"train_loss={train_step():.6f}")
