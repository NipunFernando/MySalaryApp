from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

class SalaryForm(FlaskForm):
    salary_lkr = FloatField('Salary 50% in LKR', validators=[DataRequired()])
    salary_usd = FloatField('Salary 50% in USD', validators=[DataRequired()])
    commute_expenses = FloatField('Commute Expenses', validators=[DataRequired()])
    food_expenses = FloatField('Food Expenses', validators=[DataRequired()])
    epf_percent = FloatField('EPF % on Salary 50% in LKR', validators=[DataRequired()])
    etf_percent = FloatField('ETF % on Salary 50% in LKR', validators=[DataRequired()])
    other_expenses = FloatField('Other Expenses', validators=[DataRequired()])
    other_expenses_comment = StringField('Other Expenses Comment', validators=[DataRequired()])
    exchange_rate = FloatField('USD to LKR Exchange Rate', validators=[DataRequired()])
    submit = SubmitField('Calculate Salary')
