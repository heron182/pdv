# Ponto de Venda API

A GraphQL API where you can:
    
- create a new PDV
- Search a PDV by document(CNPJ)
- Given a [lat, long] coordinate, return the nearest PDV in your area.


### Production Deploy

The application should work in any Docker network environment(Docker-Swarm, Kubernetes, etc) as long as the follow environment variables are injected during runtime:

- MONGODB_URI(required) - MongoDB connection string in the form "mongodb://username:password@hostname:port/database"
- SECRET_KEY(required) - Used in Flask session management
- FLASK_ENV(optional) - Defaults to "production"
- FLASK_APP(optional) - Defaults do "pdv"
- FLASK_DEBUG(optional) - Defaults to 0
- LOG_LEVEL(optional) - Default to "INFO"

### Local Development:

- [Python 3.6 +](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/)

**Start webserver:**

    ~/pdv: docker-compose up

GraphiQL and documentation should be available at http://localhost:8000/graphql

**Running tests:**

    ~/pdv: docker-compose run api pytest

**Load tests:**

    ~/pdv: docker-compose run api flask load_fixtures

**Linting:**

    ~/pdv: docker-compose run api flake8

**Auto Format:**

    ~/pdv: docker-compose run api black .

**Sort Imports:**

    ~/pdv: docker-compose run isort