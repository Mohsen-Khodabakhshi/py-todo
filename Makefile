.PHONY: init_db
init_db:
	aerich init -t services.database.connection.TORTOISE_ORM
	aerich init-db

.PHONY: db_migrations
db_migrations:
	aerich migrate

.PHONY: db_upgrade
db_upgrade:
	aerich upgrade