# Library components for describing the structure of a table
from sqlalchemy import Column, String, Integer, Boolean

from data_base.dbcore import Base


class Category(Base):
    """
    A model class for describing the 'Product Category' table, based on the declarative SQLAlchemy style
    """
    # The name of the table
    __tablename__ = 'category'

    # The fields of the table
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    is_active = Column(Boolean)

    def __repr__(self):
        """
        The method returns a formal string representation of the specified object
        """
        return self.name
