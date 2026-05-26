import src.app as app_module


def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": existing_email}
    )

    # Assert
    assert response.status_code == 200
    assert existing_email not in app_module.activities[activity_name]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_non_member_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    non_member_email = "not.registered@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": non_member_email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
