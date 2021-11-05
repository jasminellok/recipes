# Using the PostgreSQL Database through Docker

To simplify installing, configuring, and running a postgres database we will use the Docker container system. To manage database changes we will use Flyway (which will also be run from Docker).

## Installing Docker

Follow the [offical guide](https://docs.docker.com/get-docker) and check that it works by running the default hello-world image.

## Running PostgreSQL in Docker

### Set Up PostgreSQL Image and DB Directory

Get the offical image: `docker pull postgres`

Create a directory so we can persist data between start/stop of containers: `mkdir -p $HOME/docker/db/postgres`

### Start the PostgreSQL Container

`docker run --rm --name pg-docker -e POSTGRES_PASSWORD=password -p 5432:5432 -v $HOME/docker/db/postgres:/var/lib/postgresql/data  postgres`

Sending an interrupt signal (CTRL-C) will shutdown the container and database.

### Connect to the Database (only if you want to manually look around the data)

`psql -h localhost -U postgres -d postgres`

## Running Flyway

You will need to manually create the recipe_book database before running flyway.

In the postgres CLI: `CREATE DATABASE recipe_book;`

### Set Up Flyway Image

Get the official image: `docker pull flyway/flyway`

### Apply Database Migrations

Find the IP address of your postgres container: `docker container inspect pg-docker`

Start a flyway container and run the migrate command (use the IP address from before): `docker run --rm -v $HOME/devprojects/Recipe-Book/db:/flyway/sql flyway/flyway -url=jdbc:postgresql://172.17.0.2:5432/recipe_book -user=postgres -password=password migrate`



