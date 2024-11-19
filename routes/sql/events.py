from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from models.sql.events import Event, EventUpdate
from database.sql.connection import get_session
from sqlmodel import Session, select

event_router = APIRouter(
    tags=["Events"]
)


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session: Session = Depends(get_session)):
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session: Session = Depends(get_session)):
    event = session.get(Event, id)
    if event:
        return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.post("/new")
async def create_event(new_event: Event, session: Session = Depends(get_session)):
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message": "Event created successfully"
    }


@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session: Session = Depends(get_session)):
    event = session.get(Event, id)
    if event:
        event_data_dict = new_data.dict(exclude_none=True)
        for key, value in event_data_dict.items():
            setattr(event, key, value)

        session.add(event)
        session.commit()
        session.refresh(event)
        return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.delete("{id}")
async def delete_event(id: int, session: Session = Depends(get_session)):
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()

        return {
            "message": "Event deleted successfully"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
