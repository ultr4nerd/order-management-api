export COMPOSE_FILE := "compose.local.yaml"

# Default command to list all available commands.
default:
    @just --list

# install-hooks: Install pre-commit hooks
install-hooks:
    @pre-commit install

# build: Build python image.
build:
    @echo "Building python image..."
    @docker compose build

# up: Start up containers.
up:
    @echo "Starting up containers..."
    @docker compose up -d --remove-orphans

# down: Stop containers.
down:
    @echo "Stopping containers..."
    @docker compose down

# prune: Remove containers and their volumes.
prune *args:
    @echo "Killing containers and removing volumes..."
    @docker compose down -v {{args}}

# logs: View container logs
logs *args:
    @docker compose logs -f {{args}}

# manage: Executes `manage.py` command.
manage +args:
    @docker compose run --rm django python ./manage.py {{args}}

# test: Run pytest tests
test *args:
    @docker compose run --rm django pytest {{args}}

# test-cov: Run tests with coverage
test-cov *args:
    @docker compose run --rm django coverage run -m pytest {{args}}
    @docker compose run --rm django coverage html
    @echo "Coverage report generated at htmlcov/index.html"

# type-check: Run mypy type checking
type-check:
    @docker compose run --rm django mypy order_management_api

# ruff: Run ruff with given arguments
ruff *args:
    @docker compose run --rm django ruff {{args}}

# lint: Lint all files in the project without making any changes
lint:
    @just ruff check .

# lint-fix: Lint all files in the project and automatically fix any fixable issues
lint-fix:
    @just ruff check --fix .

# format: Automatically format the code
format:
    @just ruff format .

# sort-imports: Sort imports and format the code
sort-imports:
    @just ruff check --select I --fix
    @just ruff format .
