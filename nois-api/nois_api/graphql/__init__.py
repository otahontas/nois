from ariadne import make_executable_schema
from ariadne import load_schema_from_path
from ariadne.asgi import GraphQL
from pathlib import Path

from nois_api.config import DEBUG
from nois_api.graphql.resolvers import query, mutation

schema_file = Path(__file__).parent / "schema.graphql"

type_defs = load_schema_from_path(str(schema_file))

schema = make_executable_schema(type_defs, query, mutation)

graphql_app = GraphQL(schema, debug=DEBUG)
