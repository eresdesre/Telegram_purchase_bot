# Library components for describing the structure of a table
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
# Importing module for linking tables
from sqlalchemy.orm import relationship, backref

# Importing the Category model for linking models
from models.category import Category
from data_base.dbcore import Base


class Products(Base):
    """
    A class for creating the 'Product' table, based on the declarative SQLAlchemy style
    """
    # The name of the table
    __tablename__ = 'products'

    # The fields of the table
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    # For cascading deletion of data from the table
    category = relationship(
        Category,
        backref=backref('products',
                        uselist=True,
                        cascade='delete,all'))

    def __repr__(self):
        """
        The method returns a formal string representation of the specified object
        """
        return f"{self.name} {self.title} {self.price}"
