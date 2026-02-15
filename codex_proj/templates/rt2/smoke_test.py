import traceback


if __name__ == "__main__":
    try:
        import torch
        import torch.nn as nn

        from dataset import RT2Dataset
        from model import RT2Minimal

        dataset = RT2Dataset()
        batch = dataset.sample_batch(2)
        model = RT2Minimal()
        logits = model(batch["image"], batch["instruction_ids"])
        loss = nn.CrossEntropyLoss()(logits, batch["action_token"])
        print("IMPORT_CHECK=PASS")
        print("FORWARD_CHECK=PASS")
        print(f"LOSS={float(loss.item()):.6f}")
    except Exception:
        print("IMPORT_CHECK=FAIL_OR_RUNTIME_ERROR")
        print(traceback.format_exc())
        raise
