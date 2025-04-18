# Order Management API

A RESTful API for restaurant order management system, built as a technical challenge for a backend position.

## Project Overview

This project was generated using [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django/), a framework for jumpstarting production-ready Django projects quickly. The template provides a solid foundation with best practices, security features, and modern development tools pre-configured.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Just](https://just.systems/man/en/introduction.html) - A modern command runner

### Why Just?

Just is used instead of Makefile for several reasons:
- More modern and user-friendly syntax
- Better error messages and debugging capabilities
- Built-in support for command-line arguments
- Cross-platform compatibility
- Simpler and more maintainable configuration

For detailed information about Just, visit the [official documentation](https://just.systems/man/en/introduction.html).

### Installing Just

#### macOS
```bash
brew install just
```

#### Linux
```bash
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
```

#### Windows
```bash
scoop install just
```

## Environment Setup

1. Create the following environment files based on the provided examples:
   ```bash
   cp .envs/.local/.django.example .envs/.local/.django
   cp .envs/.local/.postgres.example .envs/.local/.postgres
   ```

2. Edit these files with your desired configuration.

## Development Tools

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. To set up:

#### Using pip:
```bash
pip install pre-commit
pre-commit install
```

#### Using Homebrew (macOS):
```bash
brew install pre-commit
pre-commit install
```

The hooks include:
- Ruff for linting and formatting
- Django upgrade checks
- Various code quality checks (trailing whitespace, end-of-file, etc.)
- Template linting with djLint

### Ruff

[Ruff](https://github.com/astral-sh/ruff) is used for Python linting and formatting. It's configured in `pyproject.toml` and runs automatically through pre-commit hooks.

## Docker Setup

The project uses Docker and Docker Compose for containerization:

- `docker-compose.local.yml`: Development environment configuration
- `docker-compose.production.yml`: Production environment configuration

This separation allows for:
- Development-specific features (hot-reloading, debugging tools)
- Production optimizations (minimized images, security configurations)
- Environment-specific settings

All development should be done through Docker Compose to ensure consistency across environments. The Python dependencies are managed within the Docker containers, so there's no need to install them locally.

## Available Commands

All commands are run through Just:

```bash
just [command]
```

Available commands:
- `just build` - Build the Docker images
- `just up` - Start the containers
- `just down` - Stop the containers
- `just prune` - Remove containers and volumes
- `just logs` - View container logs
- `just manage` - Run Django management commands
- `just test` - Run pytest tests
- `just test-cov` - Run tests with coverage
- `just type-check` - Run mypy type checking

## CI/CD and Dependencies

- **GitHub Actions**: CI/CD pipeline configuration is located in `.github/workflows/`
- **Dependabot**: Configured in `.github/dependabot.yml` to automatically update dependencies

## Basic Commands

### Setting Up Users

- Create a superuser:
  ```bash
  just manage createsuperuser
  ```

### Running Tests

The project uses pytest for testing. You can run tests in several ways:

```bash
# Run all tests
just test

# Run tests with coverage report
just test-cov

# Run specific test file
just test tests/path/to/test_file.py

# Run tests matching a pattern
just test -k "test_pattern"
```

The coverage report will be generated in the `htmlcov` directory. You can view it by opening `htmlcov/index.html` in your browser.

### Type Checking

The project uses mypy for static type checking. To run type checks:

```bash
just type-check
```

This will check all Python files in the project for type errors and inconsistencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
