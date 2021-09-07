setup:
	sudo apt update && sudo apt upgrade
	sudo apt install -y python3-pip
	sudo apt install -y python-is-python3
	sudo apt install -y nginx
	sudo apt install -y gunicorn
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
	echo 'export PATH="/home/ubuntu/.local/bin:$PATH"' >> /home/ubuntu/.bash_profile
	source /home/ubuntu/.bash_profile
	poetry install
	sudo cp ./conf/upskill.service /etc/systemd/system/upskill.service
	sudo cp ./conf/upskill /etc/nginx/sites-available/upskill
	sudo ln -s /etc/nginx/sites-available/upskill /etc/nginx/sites-enabled
	sudo systemctl start upskill
	sudo systemctl enable upskill
	sudo systemctl restart nginx




create_db:
	poetry run python create_db.py
