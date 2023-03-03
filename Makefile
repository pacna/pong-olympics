run:
	python main.py

install:
	pip install -r requirements.txt 

freeze:
	pip freeze > requirements.txt

venv:
	echo "Removing env"
	rm -r env

	sleep 1s

	echo "Creating env"
	python3 -m venv env

	sleep 1s

	echo "Activate env"
# using . as alternative to "source"
	. env/bin/activate

	which python