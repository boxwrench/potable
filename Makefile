.PHONY: help validate export stats eval new-record scaffold clean

PYTHON ?= python3
DATA_DIR ?= data/raw
EVAL_DIR ?= data/eval
EXPORT_FILE ?= data/exports/potable_train.jsonl

help: ## Show available targets
	@echo.
	@echo   Potable Dataset Toolchain
	@echo   -------------------------
	@echo.
	@echo   make validate       Validate all records in $(DATA_DIR)
	@echo   make stats          Print coverage report
	@echo   make export         Export approved records to JSONL
	@echo   make export-all     Export all records (any status) to JSONL
	@echo   make eval           Run golden eval set
	@echo   make new-record     Scaffold a new blank record (interactive)
	@echo   make scaffold S=... Batch scaffold from seeds file S
	@echo   make clean          Remove export artifacts
	@echo.

validate: ## Validate all records
	$(PYTHON) scripts/validate.py --path $(DATA_DIR)

stats: ## Print coverage report
	$(PYTHON) scripts/stats.py --path $(DATA_DIR)

export: ## Export approved records to JSONL
	$(PYTHON) scripts/export.py --path $(DATA_DIR) --output $(EXPORT_FILE)

export-all: ## Export all records regardless of status
	$(PYTHON) scripts/export.py --path $(DATA_DIR) --output $(EXPORT_FILE) --status any

eval: ## Run golden eval scoring
	$(PYTHON) scripts/eval.py --path $(EVAL_DIR) -v

new-record: ## Scaffold a new blank record (interactive)
	$(PYTHON) scripts/new_record.py --path $(DATA_DIR)

scaffold: ## Batch scaffold from seeds file (usage: make scaffold S=path/to/seeds.txt)
	$(PYTHON) scripts/batch_scaffold.py $(S) --path $(DATA_DIR)

clean: ## Remove export artifacts
	rm -f $(EXPORT_FILE)
