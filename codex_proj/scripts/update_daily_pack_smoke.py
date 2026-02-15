import json
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_smoke_log(log_path: Path) -> tuple[str, float | None]:
    if not log_path.exists():
        return "FAIL", None

    text = log_path.read_text(encoding="utf-8", errors="ignore")
    has_import_pass = "IMPORT_CHECK=PASS" in text
    has_forward_pass = "FORWARD_CHECK=PASS" in text

    loss = None
    for line in text.splitlines():
        if line.startswith("LOSS="):
            try:
                loss = float(line.split("=", 1)[1].strip())
            except ValueError:
                loss = None

    status = "PASS" if has_import_pass and has_forward_pass and loss is not None else "FAIL"
    return status, loss


def main() -> None:
    parser = argparse.ArgumentParser(description="Update smoke_status in daily_pack.json from smoke logs.")
    parser.add_argument("--date", required=True, help="Report date in YYYY-MM-DD format.")
    args = parser.parse_args()

    daily_pack = ROOT / "reports" / args.date / "daily_pack.json"
    data = json.loads(daily_pack.read_text(encoding="utf-8"))

    for card in data.get("cards", []):
        log_path = ROOT / card["smoke_log_path"]
        status, loss = parse_smoke_log(log_path)
        card["smoke_status"] = status

        if status == "PASS":
            card.pop("failure_analysis", None)
            card["smoke_metrics"] = {"loss": loss}
        else:
            card.pop("smoke_metrics", None)

    daily_pack.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
