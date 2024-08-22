shell:
	docker compose exec app python manage.py shell
m1:
	docker compose run app python manage.py makemigrations

m2:
	docker compose run app python manage.py migrate

cs:
	docker compose run app python manage.py collectstatic --clear --verbosity 3

build:
	docker compose up --build --remove-orphans -d

builds:
	docker compose up --build -d

stop:
	docker compose stop

down:
	docker compose down -v

logApp:
	 docker compose logs -f app

logDb:
	 docker compose logs -f postgres

logNginx:
	 docker compose logs -f nginx


PHONY: m1 m2 cs build builds logApp logDb logApp logNginx stop down