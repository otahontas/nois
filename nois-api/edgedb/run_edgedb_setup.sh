# Tear down previous docker-composed containers if there, restart new one
docker-compose up -d

# Set up database
cat initialize_db.edgeql  | edgedb -H localhost -u edgedb

# Set up schema

# Populate db with data
