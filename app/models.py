from coaster.sqlalchemy import BaseMixin  # id, created_at, updated_at
from sqlalchemy import (
    Column, String, Text
)
from database import Base


class MyContact(BaseMixin, Base):
    __tablename__ = 'my_contact'

    name = Column(String(32), nullable=False)
    number = Column(String(32), nullable=False)
    about = Column(Text(64), nullable=False)

    def __repr__(self):
        return '<MyContact - {name} - {number}>'.format(name=self.name, number=self.number)
