dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
pro:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build
devdown:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down
prodown:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
web bash:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml exec web bash
	