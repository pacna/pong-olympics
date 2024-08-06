## ----------------------------------------------------------------------
## The purpose of this Makefile is to simplify common development tasks.
## ----------------------------------------------------------------------
##
## Usage:
##   - make run          : Starts the application
##   - make install      : Installs all pip dependencies listed in the requirements.txt file
##   - make freeze       : Creates or updates the requirements.txt file with the current pip dependencies
##   - make activate     : Activates the Python virtual environment (venv) 
##   - make venv         : Creates a new virtual environment (venv) for the repository
##   - make test         : Runs tests
##   - make web          : Builds a web folder for deployment to GitHub Pages
##   - make help         : Show available commands and descriptions
##

python = env/bin/python

.PHONY:run
run:
	$(python) main.py

.PHONY:install
install:
	$(python) -m pip install -r requirements.txt 

.PHONY:freeze
freeze:
	$(python) -m pip freeze > requirements.txt

.PHONY:activate
activate:
	echo "Activating env"
	. env/bin/activate

	which $(python)

.PHONY:venv
venv:
	bash venv.sh; \
	make install activate

.PHONY:test
test:
	${python} -m pytest

.PHONY:web
web:
	${python} -m pygbag --build .

.PHONY:help
help:
	@sed -ne '/@sed/!s/##//p' $(MAKEFILE_LIST)