# abusquets-northwind

To execute any command
```bash
docker-compose exec api bash
```


# Users

## Create admin User
```bash
python manage.py {user_email} {name}
```

# Migrations


```bash
alembic init -t async migrations
```

## Create the initial migration or add a migration
```bash
alembic revision --autogenerate -m "init"

```

```bash

alembic revision --autogenerate -m 'add northwind models'

```

## Apply the migrations to the database:

```bash
alembic upgrade head

```

# Populate

```bash
docker-compose up
```

```bash
docker-compose exec api alembic upgrade head
docker-compose exec postgres bash -c 'export PGPASSWORD=northwind && psql -U northwind northwind < /data/northwind_data.sql'
```

```bash
docker-compose exec api python manage.py {user_email} {name}
```
