dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
pro:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build
down:
	docker-compose down
web bash:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml exec web bash
	