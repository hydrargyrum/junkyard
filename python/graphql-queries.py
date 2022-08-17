
import requests

QL_QUERY = """
query FindPerformer($performerName: String!) {
  findPerformers(performer_filter: {
    name: {
      value: $performerName
      modifier: EQUALS
    }
  }) {
    performers {
      id
    }
  }
}
"""

QL_MUTATION = """
mutation AddPerformerScenes($scenes: [ID!], $performer: ID!) {
  bulkSceneUpdate(input: {
    ids: $scenes
    performer_ids: {
      ids: [$performer]
      mode: SET
    }
  }) {
    id
    path
    performers {
      id
      name
    }
  }
}
"""

GQL_URL = "http://localhost:9999/graphql"

session = requests.Session()
session.headers["ApiKey"] = "REDACTED"

# perform a query (read-only)
response = session.post(
    GQL_URL,
    json={
        "query": QL_QUERY,
        "variables": {
            "performerName": "Foo Bar",
        },
    },
)
print(response.json())

# perform a mutation (write)
session.post(
    GQL_URL,
    json={
        "query": QL_MUTATION,
        "variables": {
            "scenes": ["123", "456"],
            "performer": "42",
        },
    },
)
