DOCKER_COMPOSE=docker-compose
PYTHON=python3
MANAGE=manage.py
SERVICE=web

# ------------------------------
# Docker commands
# ------------------------------

up:  ## Build and start the Docker container
	$(DOCKER_COMPOSE) up --build -d

down:  ## Stop and remove the Docker container
	$(DOCKER_COMPOSE) down

logs:  ## Show container logs
	$(DOCKER_COMPOSE) logs -f $(SERVICE)

restart: down up  ## Restart the container

# ------------------------------
# Django management commands
# ------------------------------

migrate:  ## Run Django migrations
	$(DOCKER_COMPOSE) exec $(SERVICE) $(PYTHON) $(MANAGE) migrate

makemigrations:  ## Create Django migrations
	$(DOCKER_COMPOSE) exec $(SERVICE) $(PYTHON) $(MANAGE) makemigrations

flush:  ## Clear the database
	$(DOCKER_COMPOSE) exec $(SERVICE) $(PYTHON) $(MANAGE) flush --no-input
