setup:
	sudo apt update && sudo apt upgrade
	sudo apt install python3-pip
	sudo apt install nginx
	sudo apt install gunicorn
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
	git clone git@github.com:patryklomza/devops-upskill.git
	cd devops-upskill
	poetry install
	cp ./conf/upskill.service etc/systemd/system/upskill.service
	cp ./conf/upskill /etc/nginx/sites-available/upskill
	sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
	sudo systemctl start myproject
	sudo systemctl enable myproject
	sudo systemctl restart nginx




create_db:
	poetry run python create_db.py
