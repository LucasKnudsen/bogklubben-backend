# ──────────────────────────────────────────────────────────────────────────────
# Makefile for AWS CDK + Local Development
# ──────────────────────────────────────────────────────────────────────────────

# Use bash so multi-line rules share state
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eo pipefail -c

# Default goal
.DEFAULT_GOAL := help

# ————————————————— Variables ——————————————————————————————————————————————————

# ————————————————— Phony Targets ——————————————————————————————————————————————
.PHONY: help up serve start reset

help:       ## Show this help text
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*?## "} {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

up:         ## docker-compose up (detached)
	docker-compose up -d

serve:     ## run Uvicorn on src.api.main
	uvicorn src.api.main:app --host 127.0.0.1 --port 8080 --reload

start:      ## equivalent to `make up` then `make serve`
	$(MAKE) up
	$(MAKE) serve

reset:		## stops
	docker-compose down