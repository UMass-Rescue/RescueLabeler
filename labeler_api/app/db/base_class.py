from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime


@as_declarative()
class Base:
    """SqlAlchemy Base with override for tablename generation"""

    created_at = Column(DateTime, default=func.now())
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
