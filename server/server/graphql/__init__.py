from ariadne import make_executable_schema, snake_case_fallback_resolvers
from ariadne import load_schema_from_path
from ariadne.asgi import GraphQL
from pathlib import Path

from server.config import DEBUG
from server.graphql.resolvers import query, mutation

schema_file = Path(__file__).parent / "schema.graphql"

type_defs = load_schema_from_path(str(schema_file))

schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

graphql_app = GraphQL(schema, debug=DEBUG)
