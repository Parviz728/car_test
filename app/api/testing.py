from flask import Blueprint

from app.extensions import db

testing = Blueprint('testing', __name__, url_prefix='/testing')


@testing.route('/create_tables')
def create_tables():
    db.create_all()

    return "Tables created"


@testing.route('/drop_tables')
def drop_tables():
    db.drop_all()

    return "Tables dropped"


@testing.route('/create_test_data')
def create_test_data():
    from app.models import Car, Tariff, Company

    companies = [
        Company(name="Гранд Такси",
                tariffs=[
                    Tariff(name="Эконом", rate=100.0,
                           cars=[
                               Car(model="Audi A4"),
                               Car(model="Kia Rio"),
                               Car(model="Hyundai Solaris"),
                           ]),
                    Tariff(name="Комфорт", rate=300.0,
                           cars=[
                               Car(model="Hyundai Solaris"),
                               Car(model="Toyota Camry"),
                               Car(model="Kia Optima"),
                               Car(model="Ford Mondeo"),
                           ]),
                    Tariff(name="Бизнес", rate=500.0,
                           cars=[
                               Car(model="BMW 5"),
                               Car(model="BMW 7"),
                               Car(model="Audu A6")
                           ]),
                ]),
        Company(name="Быстрая Поездка",
                tariffs=[
                    Tariff(name="Эконом", rate=100.0,
                           cars=[
                               Car(model="Audi A4"),
                               Car(model="Kia Rio"),
                               Car(model="Hyundai Solaris"),
                           ]),
                    Tariff(name="Комфорт", rate=400.0,
                           cars=[
                               Car(model="Toyota Camry"),
                               Car(model="Kia Optima"),
                           ])
                ]),
        Company(name="Автодрайв",
                tariffs=[
                    Tariff(name="Эконом", rate=50.0,
                           cars=[
                               Car(model="Audi A4"),
                               Car(model="Kia Rio"),
                           ]),
                    Tariff(name="Комфорт", rate=250.0,
                           cars=[
                               Car(model="Hyundai Solaris"),
                               Car(model="Kia Optima"),
                               Car(model="Ford Mondeo"),
                           ]),
                    Tariff(name="Комфорт+", rate=300.0,
                           cars=[
                               Car(model="Toyota Camry"),
                               Car(model="Kia Optima"),
                               Car(model="Hyundai Elantra"),
                           ]),
                    Tariff(name="Бизнес", rate=600.0,
                           cars=[
                               Car(model="BMW 5"),
                               Car(model="Audu A6"),
                               Car(model="Mercedes-Maybach S-class"),
                           ])
                ])
    ]

    db.session.add_all(companies)
    db.session.commit()
    return "Test data created"
