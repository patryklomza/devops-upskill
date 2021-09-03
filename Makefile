setup:
	sudo apt update && sudo apt upgrade
	sudo apt install python3-pip
	sudo apt install nginx
	sudo apt install gunicorn
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
	git clone git@github.com:patryklomza/devops-upskill.git
	poetry install

