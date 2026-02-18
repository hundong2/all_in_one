# Codex Team 기능 및 사용 방법 (공식 문서 기반)

## 실행 명령 (Makefile)
프로젝트 루트에서 아래 명령으로 한 번에 실행할 수 있습니다.

```bash
make help
make run
make run DATE=2026-02-15
make serve
make serve 5575
make status
make stop
```

- `make run`: venv 준비 -> 의존성 설치 -> smoke test 3종 실행 -> daily_pack smoke 상태 업데이트
- `make serve`: 로컬 정적 서버 실행 (기본 포트 `8000`)
- `make serve 5575`: 포트 `5575`로 로컬 서버 실행
- `make stop`: 실행 중인 `make run`/`make serve` 프로세스 중지
- `make status`: 현재 `run`/`serve` 상태 확인

## 빠른 시작 (처음 3분)
1. 이 레포 루트에 `AGENTS.md`가 있는지 확인합니다.
2. 로컬 스킬이 있는지 확인합니다.
   - `.agents/skills/openai-docs/SKILL.md`
3. Codex에 아래처럼 바로 요청합니다.
   - `AGENTS.md 워크플로우대로 오늘 Execution-Ready Card 3개와 Daily Pack 생성해줘`
   - `openai-docs skill로 OpenAI API 변경점 확인해줘`

한 줄 요약:
- 팀처럼 운영하려면 `AGENTS.md`(규칙) + `.agents/skills`(반복작업 모듈) + 목표형 프롬프트(실행 지시)를 같이 사용합니다.
- 결과물 용어는 `Execution-Ready Card`, `Daily Pack`, `Smoke Test`로 통일합니다.

## 1) Claude Code식 Team 기능이 있나?
결론: Claude Code의 고정된 "Team" 명칭/기능과 1:1로 동일한 공식 기능은 확인되지 않습니다.

대신 OpenAI 공식 문서 기준으로는 아래 조합이 팀형 자동화에 해당합니다.
1. 여러 작업을 병렬로 위임/실행 (Codex cloud)
2. 저장소 규칙 파일 `AGENTS.md`로 에이전트 행동 정의
3. `Skills`로 반복 작업 절차를 모듈화

참고 링크:
- Introducing Codex: https://openai.com/index/introducing-codex/
- AGENTS.md guide: https://developers.openai.com/codex/config/
- Skills guide: https://developers.openai.com/codex/skills/

## 2) 공식 문서 핵심 내용 요약
- Codex는 여러 작업을 병렬로 수행하는 에이전트형 워크플로우를 지원합니다. (Introducing Codex)
- Codex는 작업 시 `AGENTS.md`를 읽어 프로젝트별 지침을 따릅니다. (config 문서)
- `AGENTS.md`는 상위 디렉터리까지 계층적으로 탐색되어 적용됩니다. (config 문서)
- Skills는 재사용 가능한 `SKILL.md` 단위 지침이며, 호출 시 필요 파일만 로드됩니다. (skills 문서)
- 프로젝트 로컬 스킬은 `<repo>/.agents/skills/`에 두면 해당 레포에서만 적용됩니다. (skills 문서)

## 3) 이 레포에서 Team처럼 운영하는 방법
1. 루트에 `AGENTS.md`를 두고 역할/워크플로우/품질게이트를 정의합니다.
2. 반복 작업(예: 논문 스카우팅, 압축, 템플릿 생성)을 스킬로 분리합니다.
3. Codex에게 "AGENTS.md 절차대로 Execution-Ready Card 3개 + Daily Pack 생성"처럼 목표형 요청을 주면, Codex가 규칙 기반으로 단계 실행합니다.
4. 병렬 가능한 작업(수집, 요약, 템플릿 생성, 검증)은 동시에 실행되도록 지시합니다.

## 4) 현재 적용 상태
- 공식 스킬 `openai-docs`를 이 레포 로컬 경로에 설치 완료:
  - `.agents/skills/openai-docs`

## 5) 레포 로컬 스킬 사용법
1. 스킬 설치 경로 확인
   - `.agents/skills/<skill-name>/SKILL.md`
2. Codex 프롬프트에서 스킬 이름을 직접 언급
   - 예: `openai-docs skill로 API 변경사항 확인해줘`
3. Codex는 해당 스킬의 `SKILL.md` 지침을 읽고 작업을 수행

## 6) 설치 명령(재실행용)
아래 명령으로 같은 방식으로 레포 로컬 설치가 가능합니다.

```bash
python3 /Users/donghun2/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo openai/skills \
  --path skills/.curated/openai-docs \
  --dest /Users/donghun2/workspace/all_in_one/codex_proj/.agents/skills
```

## 7) 문서 확인 시점
- 이 README는 2026-02-15 기준 공식 페이지 내용을 바탕으로 정리되었습니다.
