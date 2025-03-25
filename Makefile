# Variables
ENV_FILE = .env
DOCKER_COMPOSE = docker-compose.yml

DEFAULT_ADMIN_USERNAME = admin
DEFAULT_ADMIN_EMAIL = "admin@admin.pl"
DEFAULT_ADMIN_PASSWORD = "admin"

# Commands
.PHONY: build
build:
	docker compose -f $(DOCKER_COMPOSE) build --no-cache

.PHONY: run
run:
	docker compose -f $(DOCKER_COMPOSE) up -d

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
	echo "\n\t\t## Success app is now running ##\n"


# # Migration
.PHONY: makemigrations
makemigrations:
	docker compose -f $(DOCKER_COMPOSE) run --rm backend sh -c "alembic revision --autogenerate -m 'message'"

.PHONY: migrate
migrate:
	docker compose -f $(DOCKER_COMPOSE) run --rm backend sh -c "alembic upgrade head"

.PHONY: roll_migration
roll_migration:
	docker compose -f $(DOCKER_COMPOSE) run --rm backend sh -c "alembic downgrade -1"

# # Add user
# # Example: make add_admin EMAIL=your.email@here NAME=your_username PASSWORD=your_password
.PHONY: add_admin
add_admin:
	@if [ "$$(grep ^DEBUG $(ENV_FILE) | cut -d '=' -f2)" = "true" ]; then \
		echo "## Adding user\n\tusername: $${NAME:-$(DEFAULT_ADMIN_USERNAME)}\temail: $${EMAIL:-$(DEFAULT_ADMIN_EMAIL)}\tpassowrd: $${PASSWORD:-$(DEFAULT_ADMIN_PASSWORD)} ##\n\n"; \
		export POSTGRES_USER=$$(grep ^POSTGRES_USER $(ENV_FILE) | cut -d '=' -f2); \
        export POSTGRES_DB=$$(grep ^POSTGRES_DB $(ENV_FILE) | cut -d '=' -f2); \
        docker compose exec -e POSTGRES_USER=$${POSTGRES_USER} -e POSTGRES_DB=$${POSTGRES_DB} db psql --username=$${POSTGRES_USER} $${POSTGRES_DB} -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"; \
        docker compose exec -e POSTGRES_USER=$${POSTGRES_USER} -e POSTGRES_DB=$${POSTGRES_DB} db psql --username=$${POSTGRES_USER} $${POSTGRES_DB} -c "CREATE EXTENSION IF NOT EXISTS \"pgcrypto\";"; \
        docker compose exec -e POSTGRES_USER=$${POSTGRES_USER} -e POSTGRES_DB=$${POSTGRES_DB} db psql --username=$${POSTGRES_USER} $${POSTGRES_DB} -c "INSERT INTO users (uuid, username, email, password, is_active, is_staff, \"table\") VALUES (uuid_generate_v4(), '$${NAME:-$(DEFAULT_ADMIN_USERNAME)}', '$${EMAIL:-$(DEFAULT_ADMIN_EMAIL)}', crypt('$${PASSWORD:-$(DEFAULT_ADMIN_PASSWORD)}', gen_salt('bf')), true, false, '');"; \
		docker compose restart backend; \
	else \
		echo "DEBUG mode is not enabled. Aborting."; \
	fi
