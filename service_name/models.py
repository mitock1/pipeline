from datetime import date
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DATETIME
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

# here you add db models


class AsDictMixin(object):
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), (datetime, date))
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns  # type: ignore
        }


class TimestampMixin:
    created_at = Column("CreatedAt", DATETIME, nullable=False)


class ModelBase(TimestampMixin, AsDictMixin):
    pass


Base = declarative_base(cls=ModelBase)


class A(Base):
    __tablename__ = "A"
    id = Column(Integer, primary_key=True)
