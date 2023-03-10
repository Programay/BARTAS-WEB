# Backend documentation

## BE

### [Fastapi](https://fastapi.tiangolo.com/tutorial/first-steps/)

## DB

### [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

### [Alembic](https://alembic.sqlalchemy.org/en/latest/)

#### DB Basic commands:

- Making migration - `alembic revision --autogenerate -m "<message text>"`
- Apply migration to db `alembic upgrade head`


#### Troubleshooting

After creating a migration, either manually or as `--autogenerate`, you must apply it with `alembic upgrade head`. If you
used `db.create_all()` from a shell, you can use `alembic stamp head` to indicate that the current state of the database
represents the application of all migrations.
