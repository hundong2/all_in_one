import traceback


if __name__ == "__main__":
    try:
        import torch
        import torch.nn as nn

        from dataset import OpenVLADataset
        from model import OpenVLAMinimal

        dataset = OpenVLADataset()
        batch = dataset.sample_batch(2)
        model = OpenVLAMinimal()
        pred = model(batch["image"], batch["token_ids"])
        loss = nn.MSELoss()(pred, batch["action"])
        print("IMPORT_CHECK=PASS")
        print("FORWARD_CHECK=PASS")
        print(f"LOSS={float(loss.item()):.6f}")
    except Exception:
        print("IMPORT_CHECK=FAIL_OR_RUNTIME_ERROR")
        print(traceback.format_exc())
        raise
