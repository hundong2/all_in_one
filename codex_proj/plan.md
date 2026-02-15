# 개발 계획 (Development Plan)

## 프로젝트 비전 (Project Vision)
이 프로젝트는 Android Native를 기반으로 한 혁신적인 모바일 애플리케이션을 개발하는 것을 목표로 합니다. 사용자 친화적이고 안전한 환경을 제공하여, 다양한 기능을 통해 사용자 경험을 극대화합니다.

## 에픽 (Epics) 및 개별 이슈 (Issues)
1. **에픽 1: UI/UX 설계 (UI/UX Design)**
    - **이슈 1.1: 사용자 흐름 정의 (Define User Flows)**
      - 사용자 경험을 개선하기 위한 주요 사용자 흐름을 정의합니다.
    - **이슈 1.2: 와이어프레임 디자인 (Design Wireframes)**
      - 기본적인 와이어프레임을 설계하여 각 스크린의 레이아웃을 결정합니다.
    
2. **에픽 2: 기술 아키텍처 결정 (Technical Architecture Decisions)**
    - **이슈 2.1: WebView 관리 설계 (Design WebView Management)**
      - WebView 구성 및 성능 최적화를 위한 전략을 수립합니다.
    - **이슈 2.2: 데이터베이스 스키마 설계 (Design Database Schema)**
      - 필요한 데이터 베이스 구조를 명확히 정의합니다.
    
3. **에픽 3: 보안 기능 구현 (Implement Security Features)**
    - **이슈 3.1: 사용자 인증 및 권한 관리 (User Authentication and Authorization)**
      - 안전한 사용자 인증 및 데이터 보호를 위한 절차를 설계합니다.

## 로드맵 단계별 맵핑 (Mapping Roadmap Steps)
- **1단계: 요구 사항 수집 (Requirements Gathering)**
  - 사용자 요구 사항을 논의하고 정리합니다.
- **2단계: 프로토타입 디자인 (Prototype Design)**
  - 초기 프로토타입을 설계하여 사용자 피드백을 받습니다.
- **3단계: 개발 및 테스트 (Development and Testing)**
  - 실제 기능을 개발하고 사용자 테스트를 실시하여 품질을 확인합니다.
- **4단계: 배포 (Deployment)**
  - 최종 고객에게 배포하고, 필수 유지 관리 절차를 설정합니다.

## 체크리스트 (Checklist)
- [ ] 사용자 흐름 정의
- [ ] 와이어프레임 디자인
- [ ] WebView 관리 설계
- [ ] 데이터베이스 스키마 정의
- [ ] 사용자 인증 프로세스 구현

---

## AGENTS.md 기반 실행 결과 (2026-02-15)

`NeuroFeed Research Ops` 워크플로우 기준으로 오늘 실행 산출물을 생성함.

- [x] Daily `Execution-Ready Card` 3개 생성 시도 (`VLM`, `Robotics`, `Physical AI`)
- [x] 후보 5편 shortlist + 점수화 (`reports/2026-02-15/scout_shortlist.json`)
- [x] 카드별 요약/novelty/failure modes/repro checklist 작성 (`reports/2026-02-15/daily_pack.json`)
- [x] 템플릿 생성 (`templates/openvla`, `templates/rt2`, `templates/diffusion_policy`)
- [x] 스모크 테스트 실행 + 로그 저장 (`logs/*_smoke.log`)
- [x] Daily Pack JSON 생성 (`reports/2026-02-15/daily_pack.json`)
- [x] KG 관계 업데이트 (`kg/relations.json`)

실행 메모:
- Python 3.11 venv + `torch` 설치 후 스모크 테스트 3/3 `PASS`.
- `requirements.txt`로 의존성 고정 완료.
- `scripts/update_daily_pack_smoke.py --date 2026-02-15`로 PASS/FAIL 및 loss 지표 자동 반영.
