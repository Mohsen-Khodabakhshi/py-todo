from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "username" VARCHAR(64) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "name" VARCHAR(64),
    "avatar" VARCHAR(255),
    "last_login" TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS "idx_user_usernam_9987ab" ON "user" ("username");
CREATE TABLE IF NOT EXISTS "project" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "title" VARCHAR(64) NOT NULL UNIQUE,
    "slug" VARCHAR(64) NOT NULL,
    "order" SMALLINT NOT NULL  DEFAULT 1,
    "owner_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_project_slug_2d2cec" ON "project" ("slug");
CREATE TABLE IF NOT EXISTS "projectuser" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "status" VARCHAR(15) NOT NULL  DEFAULT 'invited',
    "project_id" INT NOT NULL REFERENCES "project" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "projectuser"."status" IS 'INVITED: invited\nACCEPTED_INVITE: accepted_invite\nREJECTED_INVITE: rejected_invite';
CREATE TABLE IF NOT EXISTS "section" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "title" VARCHAR(64) NOT NULL,
    "slug" VARCHAR(64) NOT NULL,
    "order" SMALLINT NOT NULL  DEFAULT 1,
    "project_id" INT NOT NULL REFERENCES "project" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_section_slug_94ee4b" ON "section" ("slug");
CREATE TABLE IF NOT EXISTS "task" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT,
    "slug" VARCHAR(64) NOT NULL,
    "due_date" TIMESTAMPTZ,
    "order" SMALLINT NOT NULL  DEFAULT 1,
    "priority" VARCHAR(8) NOT NULL  DEFAULT 'low',
    "assign_to_id" INT REFERENCES "user" ("id") ON DELETE CASCADE,
    "parent_id" INT REFERENCES "task" ("id") ON DELETE CASCADE,
    "section_id" INT NOT NULL REFERENCES "section" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_task_slug_4e3a6b" ON "task" ("slug");
COMMENT ON COLUMN "task"."priority" IS 'PRIORITY_LOW: low\nPRIORITY_NORMAL: normal\nPRIORITY_HIGH: high\nPRIORITY_CRITICAL: critical';
CREATE TABLE IF NOT EXISTS "comment" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "body" TEXT NOT NULL,
    "task_id" INT NOT NULL REFERENCES "task" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
