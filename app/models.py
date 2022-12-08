from app.extensions import db


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    tariffs = db.relationship("Tariff", backref="company")


class Tariff(db.Model):
    __tablename__ = "tariffs"
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    cars = db.relationship("Car", backref="tariff")

    def __repr__(self):
        cars = ", ".join([car.model for car in self.cars])
        return f"<Tariff {self.name} {self.rate} {cars}>"


class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    tariff_id = db.Column(db.Integer, db.ForeignKey("tariffs.id"), nullable=False)
    model = db.Column(db.String(255), nullable=False)

    # image_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Car {self.model} {self.tariff}>"
