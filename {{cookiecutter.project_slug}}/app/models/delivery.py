from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    sender_name = Column(String, nullable=False)
    sender_phone = Column(String, nullable=False)
    sender_email = Column(String)
    sender_address = Column(String, nullable=False)
    receiver_name = Column(String, nullable=False)
    receiver_country = Column(String, nullable=False)
    receiver_postal_code = Column(String, nullable=False)
    receiver_tel = Column(String)
    receiver_address = Column(String, nullable=False)


from enum import Enum


class Role(Enum):
    ADMIN = "admin"
    STAFF = "staff"
    AGENT = "agent"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(Enum(Role), nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String)
    verified = Column(Boolean, default=False)


from sqlalchemy import Column, Integer, Float, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True)
    flight_date = Column(Date)
    invoice_date = Column(Date)
    bill_to = Column(String)
    no = Column(String)
    pass_code = Column(String)
    particular = Column(String)
    rate = Column(Float)
    amount_for_particular = Column(Float)
    packaging_rate = Column(Float)
    packaging_cost = Column(Float)
    delivery_rate = Column(Float)
    delivery_cost = Column(Float)
    payment_method = Column(String)
    payment_currency = Column(String)
    total = Column(Float)

    delivery_progress_id = Column(Integer, ForeignKey("delivery_progresses.id"))
    delivery_progress = relationship("DeliveryProgress", back_populates="deliveries")


class DeliveryProgress(Base):
    __tablename__ = "delivery_progresses"

    id = Column(Integer, primary_key=True)
    status = Column(
        Enum(
            "Pick Up",
            "Myanmar Airport Transit",
            "Foreign Airport Transit",
            "Foreign Department Arrive",
            "3rdparty Agent Update",
            "Delivered",
        )
    )

    deliveries = relationship("Delivery", back_populates="delivery_progress")


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    invoice_date = Column(Date)
    amount = Column(Float)

    delivery_id = Column(Integer, ForeignKey("deliveries.id"))
    delivery = relationship("Delivery", back_populates="invoices")


class Rate(Base):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True)
    currency = Column(String)
    rate = Column(Float)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)


## Examples

import asyncio
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
delivery_data = {
    "flight_date": "2023-02-11",
    "invoice_date": "2023-02-11",
    "bill_to": "John Doe",
    "no": 123456,
    "particular": "Laptop",
    "rate": 1000,
    "amount_for_particular": 1000,
    "packaging_rate": 100,
    "packaging_cost": 100,
    "delivery_rate": 200,
    "delivery_cost": 200,
    "payment_method": "Credit Card",
    "payment_currency": "USD",
    "total": 1300,
    "delivery_progress": "Pick Up",
    "customer_id": 1,
    "package_id": 123456,
}

delivery = Delivery(**delivery_data)


async def create_delivery(delivery_data: dict):
    async with engine.connect() as conn:
        async with conn.begin():
            session = Session(bind=conn)
            delivery = Delivery(
                flight_date=delivery_data["flight_date"],
                invoice_date=delivery_data["invoice_date"],
                bill_to=delivery_data["bill_to"],
                no=delivery_data["no"],
                pass_code=delivery_data["pass_code"],
                particular=delivery_data["particular"],
                rate=delivery_data["rate"],
                amount_for_particular=delivery_data["amount_for_particular"],
                packaging_rate=delivery_data["packaging_rate"],
                packaging_cost=delivery_data["packaging_cost"],
                delivery_rate=delivery_data["delivery_rate"],
                delivery_cost=delivery_data["delivery_cost"],
                payment_method=delivery_data["payment_method"],
                payment_currency=delivery_data["payment_currency"],
                total=delivery_data["total"],
            )
            session.add(delivery)
            session.commit()
            session.close()


async def get_delivery(delivery_id: int):
    async with engine.connect() as conn:
        async with conn.begin():
            session = Session(bind=conn)
            delivery = session.query(Delivery).get(delivery_id)
            session.close()
            return delivery


async def update_delivery(delivery_id: int, delivery_data: dict):
    async with engine.connect() as conn:
        async with conn.begin():
            session = Session(bind=conn)
            delivery = session.query(Delivery).get(delivery_id)
            delivery.flight_date = delivery_data["flight_date"]
            delivery.invoice_date = delivery_data["invoice_date"]
            delivery.bill_to = delivery_data["bill_to"]
            delivery.no = delivery_data["no"]
            delivery.pass_code = delivery_data["pass_code"]
            delivery.particular = delivery_data["particular"]
            delivery.rate = delivery_data["rate"]
            delivery.amount_for_particular = delivery_data["amount_for_particular"]
            delivery.packaging_rate = delivery_data["packaging_rate"]
            delivery.packaging_cost = delivery_data["packaging_cost"]
            delivery.delivery_rate = delivery_data["delivery_rate"]
            delivery.delivery_cost = delivery_data["delivery_cost"]
            delivery.payment_method = delivery_data["payment_method"]
            delivery.payment_currency = delivery_data["payment_currency"]
            delivery.total = delivery_data["total"]
            session.commit()
            session.close()
