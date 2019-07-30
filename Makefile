show:
	python manage.py showmigrations

mm:
	python manage.py makemigrations

m:
	python manage.py migrate

run:
	python manage.py runserver

deploy:
	git push heroku master

config:
	heroku config:push -a gestao-clientes-rrgaya && heroku config