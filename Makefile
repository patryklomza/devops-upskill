setup:
	sudo apt update && sudo apt upgrade
	sudo apt install python3-pip
	sudo apt install python-is-python3
	sudo apt install nginx
	sudo apt install gunicorn
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
	poetry install
	cp ./conf/upskill.service etc/systemd/system/upskill.service
	cp ./conf/upskill /etc/nginx/sites-available/upskill
	sudo ln -s /etc/nginx/sites-available/upskill /etc/nginx/sites-enabled
	sudo systemctl start upskill
	sudo systemctl enable upskill
	sudo systemctl restart nginx




create_db:
	poetry run python create_db.py
