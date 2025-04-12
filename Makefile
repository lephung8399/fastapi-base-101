# Các biến
DOCKER_COMPOSE = docker compose
DOCKER_COMPOSE_FILE = docker/docker-compose.yml
APP_NAME = fastapi
DB_NAME = fastapi-db

# Màu sắc cho output
GREEN = \033[0;32m
RED = \033[0;31m
YELLOW = \033[0;33m
NC = \033[0m # No Color

# Các lệnh Docker cơ bản
.PHONY: build
build:
	@echo "$(GREEN)Building docker images...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) build

.PHONY: up
start:
	@echo "$(GREEN)Starting containers...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up -d

.PHONY: down
stop:
	@echo "$(RED)Stopping containers...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down

.PHONY: restart
restart: stop start

# Logs
.PHONY: logs
logs:
	@echo "$(YELLOW)Showing logs...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) logs -f

.PHONY: logs-api
logs-api:
	@echo "$(YELLOW)Showing API logs...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) logs -f $(APP_NAME)

.PHONY: logs-db
logs-db:
	@echo "$(YELLOW)Showing database logs...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) logs -f $(DB_NAME)

# Database migrations
.PHONY: migrations
migrations:
	@echo "$(GREEN)Creating database migrations...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec $(APP_NAME) alembic revision --autogenerate -m "$(m)"

.PHONY: migrate
migrate:
	@echo "$(GREEN)Running database migrations...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec $(APP_NAME) alembic upgrade head

.PHONY: rollback
rollback:
	@echo "$(YELLOW)Rolling back last migration...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec $(APP_NAME) alembic downgrade -1

# Tests
.PHONY: test
test:
	@echo "$(GREEN)Running tests...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec $(APP_NAME) pytest

.PHONY: test-cov
test-cov:
	@echo "$(GREEN)Running tests with coverage...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec $(APP_NAME) pytest --cov=app

# Shell access
.PHONY: shell
shell:
	@echo "$(GREEN)Opening shell in API container...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec $(APP_NAME) /bin/bash

.PHONY: db-shell
db-shell:
	@echo "$(GREEN)Opening MySQL shell...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) exec $(DB_NAME) mysql -u root -p

# Cleaning
.PHONY: clean
clean:
	@echo "$(RED)Cleaning up containers, volumes, and images...$(NC)"
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down -v
	docker system prune -f

# Help
.PHONY: help
help:
	@echo "$(YELLOW)Available commands:$(NC)"
	@echo "$(GREEN)build$(NC)      - Build docker images"
	@echo "$(GREEN)up$(NC)         - Start containers"
	@echo "$(GREEN)down$(NC)       - Stop containers"
	@echo "$(GREEN)restart$(NC)    - Restart containers"
	@echo "$(GREEN)logs$(NC)       - View all logs"
	@echo "$(GREEN)logs-api$(NC)   - View API logs"
	@echo "$(GREEN)logs-db$(NC)    - View database logs"
	@echo "$(GREEN)migrations$(NC)  - Create new migration (use with m='message')"
	@echo "$(GREEN)migrate$(NC)    - Run migrations"
	@echo "$(GREEN)rollback$(NC)   - Rollback last migration"
	@echo "$(GREEN)test$(NC)       - Run tests"
	@echo "$(GREEN)test-cov$(NC)   - Run tests with coverage"
	@echo "$(GREEN)shell$(NC)      - Open shell in API container"
	@echo "$(GREEN)db-shell$(NC)   - Open MySQL shell"
	@echo "$(GREEN)clean$(NC)      - Clean up containers, volumes, and images"

# Default command
.DEFAULT_GOAL := help
