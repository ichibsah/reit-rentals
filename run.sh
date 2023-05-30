#! /usr/bin/bash

#docker build -t anasse . 
#docker run -it -d -p 8090:80 -v /home/ibrahim/sandbox/meryem/logs:/var/log/nginx:rw --name meryem meryem 
#docker run -it -d -p 8090:80 --restart always -v /home/ibrahim/sandbox/anasse/website:/www -v /home/ibrahim/sandbox/anasse/logs:/var/log/nginx:rw --name anasse anasse 
#docker run -it meryem 
#docker run -it node
#docker exec -it meryem sh
git add .
git commit -am "$(date)"
#git push

# flask run

python3 -m venv ./.venv/ --upgrade

. ./.venv/bin/activate

#pip freeze > ./requirements.txt

python3 manage.py runserver 0.0.0.0:8000
