SHELL = /bin/bash

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

install:		## setup venv and install py dependencies
	( \
		python3 -m venv .venv; \
       	source .venv/bin/activate; \
       	python -m pip install -r requirements.txt; \
    )
