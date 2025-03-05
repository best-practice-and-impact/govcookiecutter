@echo off


IF /I "%1"=="" GOTO .DEFAULT_GOAL
IF /I "%1"=="install" GOTO install
IF /I "%1"=="install_dev" GOTO install_dev
IF /I "%1"=="prepare_docs_folder" GOTO prepare_docs_folder
IF /I "%1"=="docs" GOTO docs
IF /I "%1"=="docs_check_external_links" GOTO docs_check_external_links
IF /I "%1"=="coverage" GOTO coverage
IF /I "%1"=="coverage_html" GOTO coverage_html
IF /I "%1"=="coverage_xml" GOTO coverage_xml
IF /I "%1"=="help" GOTO help
GOTO error

:.DEFAULT_GOAL
	GOTO help

:install_dev
	python -m pip install -U pip setuptools
	python -m pip install -e .[dev]
	pre-commit install
	GOTO :EOF

:install
	python -m pip install -U pip setuptools
	python -m pip install -e .
	GOTO :EOF

:prepare_docs_folder
	IF exist "./docs/_build" ( rmdir /s /q "./docs/_build/" )
	mkdir ".\docs\_build"
	GOTO :EOF

:docs
	CALL make.bat prepare_docs_folder
	CALL make.bat install_dev
	sphinx-build -b html ./docs ./docs/_build
	GOTO :EOF

:docs_check_external_links
	CALL make.bat prepare_docs_folder
	CALL make.bat install_dev
	sphinx-build -b linkcheck ./docs ./docs/_build
	GOTO :EOF

:coverage
	CALL make.bat install_dev
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
	ECHO make: Use one of the following commands: install, install_dev, docs, docs_check_external_links, coverage, coverage_html, coverage_xml.
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
