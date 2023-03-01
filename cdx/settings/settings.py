import cdx.graphql.mutation as mu
from gql import gql
import cdx.config.config as c


async def request(operation, params, query, token):
    m = mu.Mutation(query, variables=params,
                    endpoint=(c.endpoint() + '?operationName=' + operation))
    return await m.execute(token)


class Settings:
    def __init__(self, token):
        self.token = token

    async def enable_lc(self):
        query = gql(
            """
            mutation EditLeaderSettings($input: EditLeaderSettingsInput!) {
              editLeaderSettings(input: $input) {
                hasSucceeded
              }
            }
            """
        )

        params = {"input": {"isLeadershipCornerEnabled": True}}
        operation = 'EditLeaderSettings'
        return await request(operation, params, query, self.token)

    async def enable_storyline(self):
        query = gql(
            """
            mutation EditStorylineSettings($input: EditStorylineSettingsInput!) {
              editStorylineSettings(input: $input) {
                hasSucceeded
              }
            }
            """
        )

        params = {"input": {"isStorylineEnabled": True}}
        operation = 'EditStorylineSettings'
        return await request(operation, params, query, self.token)

    async def enable_stories(self):
        query = gql(
            """
            mutation EditStoriesSettings($input: EditStoriesSettingsInput!) {
              editStoriesSettings(input: $input) {
                hasSucceeded
              }
            }
            """
        )

        params = {"input": {"storiesEnabledStatus": "ENABLED", "isStoriesEnabled": True}}
        operation = 'EditStoriesSettings'
        return await request(operation, params, query, self.token)
