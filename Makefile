# Variables
ENV_FILE = .env
DOCKER_COMPOSE = docker-compose.yml

DEFAULT_ADMIN_USERNAME = admin
DEFAULT_ADMIN_EMAIL = "admin@admin.pl"
DEFAULT_ADMIN_PASSWORD = "admin"

# Commands
.PHONY: build
build:
	@echo "\033[0;32m ## BUILDING ## \033[0m"
	docker compose -f $(DOCKER_COMPOSE) build

.PHONY: run
run:
	@echo "\033[0;32m ## APP RUN ## \033[0m"
	docker compose -f $(DOCKER_COMPOSE) up -d
	@echo "\033[0;32m ## Success. App is now running ## \033[0m"
	@echo "\033[0;34m FE http://localhost:$$(grep ^FE_PORT= .env | cut -d '=' -f2)\033[0m"
	@echo "\033[0;34m BE http://localhost:$$(grep ^BE_PORT= .env | cut -d '=' -f2)/redoc\033[0m"

.PHONY: stop
stop:
	docker compose -f $(DOCKER_COMPOSE) stop

.PHONY: logs
logs:
	docker compose -f $(DOCKER_COMPOSE) logs -f

.PHONY: shell-be
shell-be:
	docker compose -f $(DOCKER_COMPOSE) run --rm backend sh

.PHONY: shell-fe
shell-fe:
	docker compose -f $(DOCKER_COMPOSE) run --rm frontend sh

.PHONY: clean
clean:
	docker compose -f $(DOCKER_COMPOSE) down -v

.PHONY: setup
setup:
	pre-commit install
	@make build
	@make run
	@make migrate

# # Migration
.PHONY: makemigrations
makemigrations:
	docker compose -f $(DOCKER_COMPOSE) run --rm backend sh -c "alembic revision --autogenerate -m 'message'"

.PHONY: migrate
migrate:
	@echo "\033[0;32m ## DB MIGRATE ## \033[0m"
	docker compose -f $(DOCKER_COMPOSE) run --rm backend sh -c "alembic upgrade head"

# # Add user
# # Example: make create_admin EMAIL=your.email@here NAME=your_username PASSWORD=your_password
.PHONY: create_admin
create_admin:
	@if [ "$$(grep ^DEBUG $(ENV_FILE) | cut -d '=' -f2)" = "true" ]; then \
		echo -e "\033[0;32m## Adding user\n\tusername: $${NAME:-$(DEFAULT_ADMIN_USERNAME)}\temail: $${EMAIL:-$(DEFAULT_ADMIN_EMAIL)}\tpassword: $${PASSWORD:-$(DEFAULT_ADMIN_PASSWORD)} ##\033[0m\n\n";		export POSTGRES_USER=$$(grep ^POSTGRES_USER $(ENV_FILE) | cut -d '=' -f2); \
        export POSTGRES_DB=$$(grep ^POSTGRES_DB $(ENV_FILE) | cut -d '=' -f2); \
        docker compose exec -e POSTGRES_USER=$${POSTGRES_USER} -e POSTGRES_DB=$${POSTGRES_DB} db psql --username=$${POSTGRES_USER} $${POSTGRES_DB} -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"; \
        docker compose exec -e POSTGRES_USER=$${POSTGRES_USER} -e POSTGRES_DB=$${POSTGRES_DB} db psql --username=$${POSTGRES_USER} $${POSTGRES_DB} -c "CREATE EXTENSION IF NOT EXISTS \"pgcrypto\";"; \
        docker compose exec -e POSTGRES_USER=$${POSTGRES_USER} -e POSTGRES_DB=$${POSTGRES_DB} db psql --username=$${POSTGRES_USER} $${POSTGRES_DB} -c "INSERT INTO users (uuid, username, email, password, is_active, is_staff, \"table\") VALUES (uuid_generate_v4(), '$${NAME:-$(DEFAULT_ADMIN_USERNAME)}', '$${EMAIL:-$(DEFAULT_ADMIN_EMAIL)}', crypt('$${PASSWORD:-$(DEFAULT_ADMIN_PASSWORD)}', gen_salt('bf')), true, false, '');"; \
		docker compose restart backend; \
	else \
		echo -e "\033[0;33mDEBUG mode is not enabled. Aborting.\033[0m"; \
	fi
