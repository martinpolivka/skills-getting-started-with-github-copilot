def test_get_activities_returns_seeded_structure(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in payload
    assert {"description", "schedule", "max_participants", "participants"}.issubset(
        payload[expected_activity].keys()
    )


def test_root_redirects_to_static_index(client):
    # Arrange
    root_path = "/"

    # Act
    response = client.get(root_path, follow_redirects=False)

    # Assert
    assert response.status_code in {302, 307}
    assert response.headers["location"] == "/static/index.html"
