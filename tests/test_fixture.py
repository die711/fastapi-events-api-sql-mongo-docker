import pytest

from models.mongo.events import EventUpdate


@pytest.fixture
def event() -> EventUpdate:
    return EventUpdate(
        title="FastAPI Book Launch",
        image="https://google.com",
        description="We will be discussing",
        tags=["python", "fastapi", "book"],
        location="Google Meet"
    )


def test_event_name(event: EventUpdate) -> None:
    assert event.title == "FastAPI Book Launch"
