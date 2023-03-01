from typing import Any

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


class Mutation:
    gql: gql
    variables: dict[str, Any]
    endpoint: str = ''

    def __init__(self, query, variables, endpoint) -> None:
        self.gql = query
        self.variables = variables
        self.endpoint = endpoint

    async def execute(self, token) -> None:
        transport = AIOHTTPTransport(url=self.endpoint, headers={'Authorization': token})
        async with Client(
                transport=transport,
                fetch_schema_from_transport=False,
        ) as session:
            result = await session.execute(self.gql, variable_values=self.variables)
            return result
