import traceback


if __name__ == "__main__":
    try:
        import torch
        import torch.nn as nn

        from dataset import DiffusionPolicyDataset
        from model import DiffusionPolicyMinimal

        dataset = DiffusionPolicyDataset()
        batch = dataset.sample_batch(2)
        model = DiffusionPolicyMinimal()
        pred_noise = model(batch["state"], batch["action"] + batch["noise"], batch["timestep"])
        loss = nn.MSELoss()(pred_noise, batch["noise"])
        print("IMPORT_CHECK=PASS")
        print("FORWARD_CHECK=PASS")
        print(f"LOSS={float(loss.item()):.6f}")
    except Exception:
        print("IMPORT_CHECK=FAIL_OR_RUNTIME_ERROR")
        print(traceback.format_exc())
        raise
