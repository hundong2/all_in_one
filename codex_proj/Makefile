SHELL := /bin/bash

DATE ?= 2026-02-15
PORT ?= 8000
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(PYTHON) -m pip
PID_FILE := .run.pid
SERVE_PID_FILE := .serve.pid

KNOWN_GOALS := help run stop status serve venv install smoke pack clean
EXTRA_GOALS := $(filter-out $(KNOWN_GOALS),$(MAKECMDGOALS))
ifneq ($(strip $(EXTRA_GOALS)),)
PORT := $(firstword $(EXTRA_GOALS))
endif

.DEFAULT_GOAL := help

.PHONY: help run stop status serve venv install smoke pack clean

help: ## Show available commands
	@echo "NeuroFeed Research Ops Make Commands"
	@echo ""
	@echo "Usage:"
	@echo "  make run DATE=$(DATE)"
	@echo "  make serve PORT=$(PORT)"
	@echo "  make serve 5575"
	@echo "  make stop"
	@echo "  make status"
	@echo "  make help"
	@echo ""
	@awk 'BEGIN {FS = ":.*## "}; /^[a-zA-Z_-]+:.*## / {printf "  %-10s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

run: ## Run full local pipeline (venv -> install -> smoke -> daily pack update)
	@set -euo pipefail; \
	if [[ -f "$(PID_FILE)" ]]; then \
	  pid="$$(cat "$(PID_FILE)")"; \
	  if kill -0 "$$pid" 2>/dev/null; then \
	    echo "A run is already in progress (PID=$$pid)."; \
	    exit 1; \
	  fi; \
	  rm -f "$(PID_FILE)"; \
	fi; \
	echo $$$$ > "$(PID_FILE)"; \
	trap 'rm -f "$(PID_FILE)"' EXIT; \
	$(MAKE) install; \
	$(MAKE) smoke DATE="$(DATE)"; \
	$(MAKE) pack DATE="$(DATE)"; \
	echo "Run completed for DATE=$(DATE)"

stop: ## Stop active run/serve processes
	@set -euo pipefail; \
	stopped=0; \
	if [[ ! -f "$(PID_FILE)" ]]; then \
	  echo "No active run."; \
	else \
	  pid="$$(cat "$(PID_FILE)")"; \
	  if kill -0 "$$pid" 2>/dev/null; then \
	    kill "$$pid"; \
	    echo "Stopped run process PID=$$pid"; \
	    stopped=1; \
	  else \
	    echo "Run PID file exists but process is not running (PID=$$pid)."; \
	  fi; \
	  rm -f "$(PID_FILE)"; \
	fi; \
	if [[ ! -f "$(SERVE_PID_FILE)" ]]; then \
	  echo "No active server."; \
	else \
	  spid="$$(cat "$(SERVE_PID_FILE)")"; \
	  if kill -0 "$$spid" 2>/dev/null; then \
	    kill "$$spid"; \
	    echo "Stopped server process PID=$$spid"; \
	    stopped=1; \
	  else \
	    echo "Server PID file exists but process is not running (PID=$$spid)."; \
	  fi; \
	  rm -f "$(SERVE_PID_FILE)"; \
	fi; \
	if [[ "$$stopped" -eq 0 ]]; then echo "Nothing to stop."; fi

status: ## Show run/server status
	@set -euo pipefail; \
	run_state="IDLE"; \
	serve_state="IDLE"; \
	if [[ -f "$(PID_FILE)" ]]; then \
	  pid="$$(cat "$(PID_FILE)")"; \
	  if kill -0 "$$pid" 2>/dev/null; then \
	    run_state="RUNNING(pid=$$pid)"; \
	  else \
	    run_state="STALE(pid=$$pid)"; \
	  fi; \
	fi; \
	if [[ -f "$(SERVE_PID_FILE)" ]]; then \
	  spid="$$(cat "$(SERVE_PID_FILE)")"; \
	  if kill -0 "$$spid" 2>/dev/null; then \
	    serve_state="RUNNING(pid=$$spid,port=$(PORT))"; \
	  else \
	    serve_state="STALE(pid=$$spid)"; \
	  fi; \
	fi; \
	echo "RUN: $$run_state"; \
	echo "SERVE: $$serve_state"

serve: ## Start local server (default port 8000, or: make serve 5575)
	@set -euo pipefail; \
	if [[ -f "$(SERVE_PID_FILE)" ]]; then \
	  spid="$$(cat "$(SERVE_PID_FILE)")"; \
	  if kill -0 "$$spid" 2>/dev/null; then \
	    echo "Server already running (PID=$$spid)"; \
	    exit 0; \
	  fi; \
	  rm -f "$(SERVE_PID_FILE)"; \
	fi; \
	mkdir -p logs; \
	nohup python3 -m http.server "$(PORT)" > logs/serve.log 2>&1 & \
	echo $$! > "$(SERVE_PID_FILE)"; \
	sleep 1; \
	spid="$$(cat "$(SERVE_PID_FILE)")"; \
	if kill -0 "$$spid" 2>/dev/null; then \
	  echo "Server started on http://localhost:$(PORT) (PID=$$spid)"; \
	else \
	  echo "Failed to start server on port $(PORT)."; \
	  echo "Recent logs:"; \
	  tail -n 20 logs/serve.log || true; \
	  rm -f "$(SERVE_PID_FILE)"; \
	  exit 1; \
	fi

venv: ## Create local virtual environment if missing
	@if [[ ! -x "$(PYTHON)" ]]; then \
	  echo "Creating venv at $(VENV)"; \
	  python3 -m venv "$(VENV)"; \
	fi
	@$(PYTHON) -m ensurepip --upgrade >/dev/null 2>&1 || true

install: venv ## Install dependencies into local venv
	@$(PIP) install --disable-pip-version-check -r requirements.txt

smoke: ## Run all smoke tests and capture logs
	@set -euo pipefail; \
	mkdir -p logs; \
	$(PYTHON) templates/openvla/smoke_test.py > logs/openvla_smoke.log 2>&1; \
	$(PYTHON) templates/rt2/smoke_test.py > logs/rt2_smoke.log 2>&1; \
	$(PYTHON) templates/diffusion_policy/smoke_test.py > logs/diffusion_policy_smoke.log 2>&1; \
	echo "Smoke tests completed."

pack: ## Update daily_pack smoke_status from logs
	@set -euo pipefail; \
	if [[ ! -f "reports/$(DATE)/daily_pack.json" ]]; then \
	  echo "Missing reports/$(DATE)/daily_pack.json"; \
	  echo "Use DATE=<yyyy-mm-dd> that exists in reports/"; \
	  exit 1; \
	fi; \
	python3 scripts/update_daily_pack_smoke.py --date "$(DATE)"; \
	echo "Daily pack updated: reports/$(DATE)/daily_pack.json"

clean: ## Remove local runtime artifacts
	@rm -f "$(PID_FILE)" "$(SERVE_PID_FILE)"

$(EXTRA_GOALS):
	@:
