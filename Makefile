dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build

pro:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build

down:
	docker-compose down
migrate:
	docker-compose exec web python manage.py migrate
makemigrations:
	docker-compose exec web python manage.py makemigrations
web bash:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml exec web bash