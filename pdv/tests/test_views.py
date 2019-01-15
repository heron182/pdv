def test_graphql_route_works_as_expected(client):
    resp = client.get("/graphql")

    assert resp.status_code == 400
