# Backend documentation

## BE

### [Fastapi](https://fastapi.tiangolo.com/tutorial/first-steps/)

## DB

### [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

### [Alembic](https://alembic.sqlalchemy.org/en/latest/)

## For some cool commands look at [Makefile](../Makefile).

#### Troubleshooting
##### This section can be outdated since we start to use make
After creating a migration, either manually or as `--autogenerate`, you must apply it with `alembic upgrade head`. If you
used `db.create_all()` from a shell, you can use `alembic stamp head` to indicate that the current state of the database
represents the application of all migrations.
