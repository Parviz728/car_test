import logging

from flask import Blueprint, render_template, request

from app.extensions import db
from app.models import Car

cars = Blueprint('cars', __name__, url_prefix='/cars')


@cars.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        c = Car.query.with_entities(Car.id, Car.model).distinct(Car.model)
        return render_template('cars/car_choice.html', cars=c)
    elif request.method == 'POST':
        car_model = request.form.get('car_model')
        car = Car.query.filter_by(model=car_model).first()
        c = Car.query.with_entities(Car.id, Car.model).distinct(Car.model)
        companies = db.session.execute(
            f"""
                    SELECT c.name, t.name, t.rate
                    FROM companies c
                    JOIN tariffs t ON c.id = t.company_id
                    JOIN cars car ON t.id = car.tariff_id
                    WHERE car.model = '{car_model}'
                    """
        ).fetchall()
        tariffs_by_companies = {}
        for company, tariff, rate in companies:
            tariffs_by_companies.setdefault(company, []).append((tariff, rate))
        return render_template('/cars/car_cards.html', cards=tariffs_by_companies.items(), cars=c, model=car_model, car=car)
    else:
        logging.error('Unknown request method')
        return render_template('/error.html', error="Unknown request method")
