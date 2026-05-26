import src.app as app_module


def test_signup_then_unregister_flow(client):
    # Arrange
    activity_name = "Science Club"
    email = "flow.student@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup", params={"email": email}
    )
    unregister_response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email}
    )

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    assert email not in app_module.activities[activity_name]["participants"]


def test_signup_can_exceed_max_participants_current_behavior(client):
    # Arrange
    activity_name = "Tennis Club"
    activity = app_module.activities[activity_name]
    initial_count = len(activity["participants"])
    max_participants = activity["max_participants"]
    signups_needed = (max_participants - initial_count) + 1

    # Act
    last_response = None
    for index in range(signups_needed):
        email = f"overflow{index}@mergington.edu"
        last_response = client.post(
            f"/activities/{activity_name}/signup", params={"email": email}
        )

    # Assert
    assert last_response is not None
    assert last_response.status_code == 200
    assert len(app_module.activities[activity_name]["participants"]) == max_participants + 1
