## ----------------------------------------------------------------------
## The purpose of this Makefile is to simplify common development tasks.
## ----------------------------------------------------------------------
##

.PHONY:run
run: ## run the app
 ##
	python main.py

.PHONY:install
install: ## install pip dependencies (do this after creating a venv)
 ##
	pip install -r requirements.txt 

.PHONY:activate
activate: ## activate venv
 ##
	echo "Activating env"
	. env/bin/activate

	which python

.PHONY:venv
venv: ## creating a new venv for the repo
 ##
	echo "Removing env"
	rm -r env

	echo "Creating env"
	python3 -m venv env

.PHONY:help
help: ## Show this help
##
	@sed -ne '/@sed/!s/##//p' $(MAKEFILE_LIST)