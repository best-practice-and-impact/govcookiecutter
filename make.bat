@echo off


IF /I "%1"==".DEFAULT_GOAL " GOTO .DEFAULT_GOAL 
IF /I "%1"=="requirements" GOTO requirements
IF /I "%1"=="prepare_docs_folder" GOTO prepare_docs_folder
IF /I "%1"=="docs" GOTO docs
IF /I "%1"=="docs_check_external_links" GOTO docs_check_external_links
IF /I "%1"=="prepare_example_folder" GOTO prepare_example_folder
IF /I "%1"=="example" GOTO example
IF /I "%1"=="example_with_options" GOTO example_with_options
IF /I "%1"=="coverage" GOTO coverage
IF /I "%1"=="coverage_html" GOTO coverage_html
IF /I "%1"=="coverage_xml" GOTO coverage_xml
IF /I "%1"=="help" GOTO help
GOTO error

:.DEFAULT_GOAL 
	CALL make.bat =
	CALL make.bat help
	GOTO :EOF

:requirements
	python -m pip install -U pip setuptools
	python -m pip install -r requirements.txt
	pre-commit install
	GOTO :EOF

:prepare_docs_folder
	if [ ! -d "./docs/_build" ]; then mkdir ./docs/_build; fi
	find ./docs/_build -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;
	GOTO :EOF

:docs
	CALL make.bat prepare_docs_folder
	CALL make.bat requirements
	sphinx-build -b html ./docs ./docs/_build
	GOTO :EOF

:docs_check_external_links
	CALL make.bat prepare_docs_folder
	CALL make.bat requirements
	sphinx-build -b linkcheck ./docs ./docs/_build
	GOTO :EOF

:prepare_example_folder
	if [ ! -d "./example" ]; then mkdir ./example; fi
	find ./example -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;
	GOTO :EOF

:example
	CALL make.bat prepare_example_folder
	CALL make.bat requirements
	python -m cookiecutter . -o ./example --no-input
	GOTO :EOF

:example_with_options
	CALL make.bat prepare_example_folder
	CALL make.bat requirements
	python -m cookiecutter . -o ./example
	GOTO :EOF

:coverage
	CALL make.bat requirements
	coverage run -m pytest
	GOTO :EOF

:coverage_html
	CALL make.bat coverage
	coverage html
	GOTO :EOF

:coverage_xml
	CALL make.bat coverage
	coverage xml
	GOTO :EOF

:help
	@echo "$%tput bold%Available rules:$%tput sgr0%"
	@echo
	@sed -n -e "/^
	h; s/.*//; :doc" -e "H; n; s/^
	t doc" -e "s/:.*//; G; s/\\n
	s/\\n/ /g; p; }" %MAKEFILE_LIST% | LC_ALL='C' sort --ignore-case | awk -F '---' -v ncol=$%tput cols% -v indent=25 -v col_on="$%tput setaf 6%" -v col_off="$%tput sgr0%" '{ printf "%s%*s%s ", col_on, -indent, $$1, col_off; n = split($$2, words, " "); line_length = ncol - indent; for (i = 1; i <= n; i++) { line_length -= length(words[i]) + 1; if (line_length <= 0) { line_length = ncol - indent - length(words[i]) - 1; printf "\n%*s ", -indent, " "; } printf "%s ", words[i]; } printf "\n"; }' | more %shell test $(shell uname% = Darwin && echo '--no-init --raw-control-chars')
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
