from coaster.sqlalchemy import BaseMixin  # id, created_at, updated_at
from sqlalchemy.orm import validates
from sqlalchemy import (
    Column, String, Text
)
from database import Base


class MyContact(BaseMixin, Base):
    __tablename__ = 'my_contact'

    name = Column(String(32), nullable=False)
    number = Column(String(32), nullable=False)
    about = Column(Text(64), nullable=False)

    @validates('number')
    def validate_email(self, key, number):
        # add validation logic here
        if 8 <= len(str(number)) <= 12:
            return number
        raise Exception("Number not valid length")

    def __repr__(self):
        return '<MyContact - {name} - {number}>'.format(name=self.name, number=self.number)
