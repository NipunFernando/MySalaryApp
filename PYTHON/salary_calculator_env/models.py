from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SalaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salary_lkr = db.Column(db.Float, nullable=False)
    salary_usd = db.Column(db.Float, nullable=False)
    commute_expenses = db.Column(db.Float, nullable=False)
    food_expenses = db.Column(db.Float, nullable=False)
    epf_percent = db.Column(db.Float, nullable=False)
    etf_percent = db.Column(db.Float, nullable=False)
    other_expenses = db.Column(db.Float, nullable=False)
    other_expenses_comment = db.Column(db.String(100))
    exchange_rate = db.Column(db.Float, nullable=False)
    net_salary = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class ExchangeRateHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    lkr = db.Column(db.Float, nullable=False)
