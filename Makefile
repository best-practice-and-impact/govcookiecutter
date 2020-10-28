.PHONY: docs example example_with_options help prepare_example_folder requirements requirements-dev

.DEFAULT_GOAL := help

## Install the minimum Python requirements to run the cookiecutter
requirements:
	python3 -m pip install -U pip setuptools
	python3 -m pip install -r requirements.txt

## Install the Python requirements for contributors, and install pre-commit hooks
requirements-dev:
	python3 -m pip install -U pip setuptools
	python3 -m pip install -r requirements-dev.txt
	pre-commit install

## Compile the Sphinx documentation in HTML format in the `docs/_build` folder from a clean build
docs: requirements-dev
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

## Create an `example` folder, if it doesn't exist. Otherwise delete any subfolders and their contents within it
prepare_example_folder:
	if [ ! -d "./example" ]; then mkdir ./example; fi
	find ./example -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;

## Test build the cookiecutter template with all default options selected
example: prepare_example_folder requirements
	python3 -m cookiecutter . -o ./example --no-input

## Test build the cookiecutter template but allow the user to input options
example_with_options: prepare_example_folder requirements
	python3 -m cookiecutter . -o ./example

## Get help on all make commands; referenced from https://github.com/drivendata/cookiecutter-data-science
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
