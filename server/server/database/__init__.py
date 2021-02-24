from __future__ import annotations
import asyncpg
import uuid

create_new_tables = True
populate = True


async def initialize_database():
    conn = await asyncpg.connect("postgresql://nois:nois@localhost:5432/nois")
    if create_new_tables:
        await conn.execute(
            """
            DROP TABLE messages CASCADE;
            DROP TABLE threads CASCADE;
            DROP TABLE users CASCADE;
        """
        )
        await conn.execute(
            """
            CREATE TABLE users(
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP
            );
            CREATE TABLE threads(
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP,
                title TEXT,
                user_id INTEGER REFERENCES users 
            );
            CREATE TABLE messages(
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP,
                recording_uuid UUID,
                user_id INTEGER REFERENCES users,
                thread_id INTEGER REFERENCES threads
            );
        """
        )
    if populate:
        await conn.executemany(
            """
            INSERT INTO users (created_at) VALUES (NOW()) RETURNING id;
        """,
            [(), ()],
        )
        first_user, second_user = await conn.fetch("SELECT id FROM users;")
        await conn.execute(
            """
            INSERT INTO threads (title, user_id) VALUES($1, $2);
        """,
            "Huoh tätä koronaa",
            first_user["id"],
        )
        await conn.execute(
            """
            INSERT INTO threads (title, user_id) VALUES($1, $2);
        """,
            "Ebin juttu kävi kampis",
            first_user["id"],
        )
        await conn.execute(
            """
            INSERT INTO threads (title, user_id) VALUES($1, $2);
        """,
            "Tämmöne pääsykoecase tänää",
            second_user["id"],
        )
        threads = await conn.fetch("SELECT id FROM threads;")

        for thread in threads:
            await conn.executemany(
                """
                INSERT INTO messages (recording_uuid, thread_id, user_id)
                VALUES($1, $2, $3);
            """,
                [
                    (uuid.uuid4(), thread["id"], first_user["id"]),
                    (uuid.uuid4(), thread["id"], second_user["id"]),
                    (uuid.uuid4(), thread["id"], first_user["id"]),
                ],
            )
