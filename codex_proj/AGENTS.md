# NeuroFeed Research Ops - AGENTS.md

## 처음 1일 운영 체크리스트
1. 오늘 목표 생성: Daily `Execution-Ready Card` 3개 (`VLM`, `Robotics`, `Physical AI`)
2. 수집/선별: 후보 5편 shortlist + 점수화(참신성/재현성/리소스 비용)
3. 압축: 카드별 기여 3줄, SOTA delta, failure modes 3개 이상 추출
4. 실행 템플릿: minimal training loop, dataset stub, inference example 생성
5. `Smoke Test`: import, single batch forward, loss 로그 기록
6. 산출물 저장: `reports/YYYY-MM-DD/`, `templates/<paper_slug>/`, `logs/`
7. `Daily Pack` 완료: JSON 3장 + action items(최대 3개)

한 줄 운영 원칙:
- `Execution-Ready Card`가 아니면 완료로 간주하지 않는다.

## Global Objectives
- Daily: Produce 3 `Execution-Ready Card`s (VLM/Robotics/Physical AI).
- Each card must include: summary, novelty, failure modes, minimal runnable template, `Smoke Test` result.

## Standard Workflow (MUST FOLLOW)
1) Scout -> shortlist 5 papers (score by novelty, reproducibility, resource cost).
2) Compression -> extract:
   - 3-line contribution
   - Key method diagram (textual)
   - SOTA delta
   - Failure modes (>=3)
   - Repro checklist
3) Execution -> generate:
   - Minimal training loop (PyTorch)
   - Dataset interface stub
   - Inference example
   - Optional: ROS2/MuJoCo/Isaac config if applicable
4) Validator -> run `Smoke Test`:
   - import check
   - single batch forward pass
   - log loss value
   - capture stdout/stderr
5) Synthesizer -> output:
   - Daily Pack JSON (3 cards)
   - Update knowledge graph relations
   - Action items (<=3)

## File Conventions
- reports/YYYY-MM-DD/
- templates/<paper_slug>/
- logs/<paper_slug>_smoke.log
- kg/relations.json

## Quality Gates
- If `Smoke Test` fails -> provide 3 root causes + 2 next steps.
- No card without runnable template stub.
- Keep mobile summary <= 600 words.

## Cost Control
- Cache embeddings.
- Prefer minimal context windows.
