# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gtourdia <@student.42mulhouse.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#                                                      #+#    #+#              #
#    06/03/2026            Call me maybe v1.2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# export HF_HOME=/home/gtourdia/sgoinfre/42_call_me_maybe/.llm
# export UV_CACHE_DIR=/home/gtourdia/sgoinfre/42_call_me_maybe/.uv_cache


# PROJECT CONFIGURATION
AUTHOR=gtourdia
PROJECT_NAME=Call_Me_Maybe
PROJECT_START_DATE=2026-03-06
GITHUB=https://github.com/sousampere/

# COLORS
YELLOW=\033[0;33m
CYAN=\033[0;36m
GREEN=\033[0;32m
RESET=\033[0m

# MAIN VARIABLES
INTERPRETER			=	python
DEFAULT_INPUT		=	data/input/function_calling_tests.json
DEFAULT_OUTPUT		=	data/output/function_calling_result.json


install:
	@echo "$(YELLOW)╔════════════════════════════════════════════════════════════════╗"
	@echo "$(YELLOW)║                                                                ║"
	@echo "$(YELLOW)║  44  44    2222    $(GREEN)Made with ♥ by $(AUTHOR) $(YELLOW)                    ║"
	@echo "$(YELLOW)║  44  44   22  22   Project: $(CYAN)$(PROJECT_NAME) $(YELLOW)                     ║"
	@echo "$(YELLOW)║  444444      22    Started in: $(CYAN)$(PROJECT_START_DATE) $(YELLOW)                     ║"
	@echo "$(YELLOW)║      44     22     Github: $(CYAN)$(GITHUB) $(YELLOW)     ║"
	@echo "$(YELLOW)║      44   222222                                               ║"
	@echo "$(YELLOW)║                                                                ║"
	@echo "$(YELLOW)╚════════════════════════════════════════════════════════════════╝"
	@echo
	@echo "$(CYAN)[Installation]$(RESET) ➡️  Synchronizing uv"
	uv sync

sync:
	uv sync

run:
	uv run python -m src

visualize:
	uv run python -m src -v

help:
	uv run python -m src --help

debug:
	uv run python -m pdb -m src

clean:
	rm -rf .mypy_cache

lint:
	uv run python -m flake8 src
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run python -m flake8 src
	mypy . --strict