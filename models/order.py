# Library components for describing the structure of a table
from sqlalchemy import Column, DateTime, Integer, ForeignKey
# Importing module for linking tables
from sqlalchemy.orm import relationship, backref

# Importing the product model for linking models
from models.product import Products
from data_base.dbcore import Base



class Order(Base):
    """
    A class for creating the 'Order' table, based on the declarative SQLAlchemy style
    """
    # The name of the table
    __tablename__ = 'orders'

    # The fields of the table
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer)

    # For cascading deletion of data from the table
    products = relationship(
        Products,
        backref=backref('orders',
                        uselist=True,
                        cascade='delete,all'))

    def __repr__(self):
        """
        The method returns a formal string representation of the specified object
        """
        return f"{self.quantity} {self.data}"
