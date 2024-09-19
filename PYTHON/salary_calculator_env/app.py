from flask import Flask, render_template, redirect, url_for, request
from models import db, SalaryEntry, ExchangeRateHistory
from forms import SalaryForm
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salary.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = SalaryForm()
    if form.validate_on_submit():
        # Calculate net salary
        salary_lkr = form.salary_lkr.data
        salary_usd = form.salary_usd.data * form.exchange_rate.data
        total_salary = salary_lkr + salary_usd
        
        epf_deduction = salary_lkr * form.epf_percent.data / 100
        etf_deduction = salary_lkr * form.etf_percent.data / 100
        total_expenses = form.commute_expenses.data + form.food_expenses.data + form.other_expenses.data + epf_deduction + etf_deduction
        net_salary = total_salary - total_expenses
        
        # Save entry to database
        salary_entry = SalaryEntry(
            salary_lkr=salary_lkr,
            salary_usd=form.salary_usd.data,
            commute_expenses=form.commute_expenses.data,
            food_expenses=form.food_expenses.data,
            epf_percent=form.epf_percent.data,
            etf_percent=form.etf_percent.data,
            other_expenses=form.other_expenses.data,
            other_expenses_comment=form.other_expenses_comment.data,
            exchange_rate=form.exchange_rate.data,
            net_salary=net_salary
        )
        db.session.add(salary_entry)
        db.session.commit()

        return redirect(url_for('history'))
    
    return render_template('index.html', form=form)

# @app.route("/history")
# def history():
#     salary_entries = SalaryEntry.query.all()
#     exchange_history = ExchangeRateHistory.query.order_by(ExchangeRateHistory.date.desc()).all()
#     return render_template('history.html', salary_entries=salary_entries, exchange_history=exchange_history)


from datetime import datetime

# Add this function to populate historical exchange rates
def populate_exchange_rate_history():
    historical_rates = [
        {'date': '2024-09-19', 'lkr': 304.678},
        {'date': '2024-09-18', 'lkr': 303.444},
        {'date': '2024-09-17', 'lkr': 302.504},
        {'date': '2024-09-16', 'lkr': 302.163},
        {'date': '2024-09-13', 'lkr': 301.500},
        {'date': '2024-09-12', 'lkr': 301.300},
        {'date': '2024-09-11', 'lkr': 300.800},
        {'date': '2024-09-10', 'lkr': 300.500},
        {'date': '2024-09-09', 'lkr': 300.800},
        {'date': '2024-09-06', 'lkr': 298.900},
        {'date': '2024-09-05', 'lkr': 298.750},
        {'date': '2024-09-04', 'lkr': 298.850},
        {'date': '2024-09-03', 'lkr': 299.000},
        {'date': '2024-09-02', 'lkr': 298.900},
        {'date': '2024-08-30', 'lkr': 299.000},
        {'date': '2024-08-29', 'lkr': 300.000},
        {'date': '2024-08-28', 'lkr': 300.500},
        {'date': '2024-08-27', 'lkr': 300.300},
        {'date': '2024-08-26', 'lkr': 300.700},
        {'date': '2024-08-23', 'lkr': 299.700},
        {'date': '2024-08-22', 'lkr': 301.000},
        {'date': '2024-08-21', 'lkr': 300.250},
        {'date': '2024-08-20', 'lkr': 299.400},
        {'date': '2024-08-19', 'lkr': 298.818},
    ]
    
    for rate in historical_rates:
        rate_entry = ExchangeRateHistory(
            date=datetime.strptime(rate['date'], '%Y-%m-%d').date(),
            lkr=rate['lkr']
        )
        db.session.add(rate_entry)
    db.session.commit()



import matplotlib.pyplot as plt
import io
import base64
from flask import Response

# Add this function to generate the graph as an image
@app.route('/exchange-rate-graph')
def exchange_rate_graph():
    exchange_history = ExchangeRateHistory.query.order_by(ExchangeRateHistory.date.asc()).all()
    
    dates = [entry.date.strftime('%Y-%m-%d') for entry in exchange_history]
    rates = [entry.lkr for entry in exchange_history]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, rates, marker='o', color='blue')
    plt.title('USD to LKR Exchange Rate History')
    plt.xlabel('Date')
    plt.ylabel('LKR per USD')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save plot to a string buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    plt.close()

    return f'<img src="data:image/png;base64,{graph_url}"/>'



# Modify history route to include the graph
@app.route("/history")
def history():
    salary_entries = SalaryEntry.query.all()
    return render_template('history.html', salary_entries=salary_entries, graph_url=url_for('exchange_rate_graph'))



# Call this function when the app starts
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not ExchangeRateHistory.query.first():  # Populate only if table is empty
            populate_exchange_rate_history()
    app.run(debug=True)



