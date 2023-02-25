from datetime import date  # noqa: TC003
from email.message import EmailMessage
from typing import Annotated
from sqlalchemy.orm import Mapped
from starlite_saqlalchemy.repository.sqlalchemy import SQLAlchemyRepository
from starlite_saqlalchemy import db, dto
from starlite_saqlalchemy.service.sqlalchemy import RepositoryService

from starlite_saqlalchemy import dto
from app.modules import email
from app import settings
from starlite_saqlalchemy.worker import queue
from starlite_saqlalchemy.worker import enqueue_background_task_for_service


class Author(db.orm.AuditBase):
    name: Mapped[str]
    dob: Mapped[date]


class Repository(SQLAlchemyRepository[Author]):
    model_type = Author


class Service(RepositoryService[Author]):
    """Author service object."""

    repository_type = Repository

    async def create(self, data: Author) -> Author:
        created = await super().create(data)
        await enqueue_background_task_for_service(
            self,
            "send_author_created_email",
            message_content="Author Created , check the mailhog ui",
        )
        return created

    @staticmethod
    async def send_author_created_email(message_content: str) -> None:
        """Sends an email to alert that a new `Author` has been created.

        Args:
            message_content: The body of the email.
        """
        message = EmailMessage()
        message["From"] = settings.email.SENDER
        message["To"] = settings.email.RECIPIENT
        message["Subject"] = settings.email.NEW_AUTHOR_SUBJECT
        message.set_content(message_content)
        async with email.client:
            await email.client.send_message(message)


CreateDTO = dto.FromMapped[Annotated[Author, dto.config("write", exclude={"id"})]]
ReadDTO = dto.FromMapped[Annotated[Author, dto.config("read")]]
WriteDTO = dto.FromMapped[Annotated[Author, dto.config("write")]]

