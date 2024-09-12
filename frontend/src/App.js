// File: frontend/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function App() {
  const [netSalary, setNetSalary] = useState('');
  const [foodExpenses, setFoodExpenses] = useState('');
  const [commuteExpenses, setCommuteExpenses] = useState('');
  const [result, setResult] = useState(null);
  const [exchangeRates, setExchangeRates] = useState([]);

  useEffect(() => {
    fetchExchangeRates();
  }, []);

  const fetchExchangeRates = async () => {
    try {
      const response = await axios.get('http://localhost:5000/exchange-rates');
      setExchangeRates(response.data);
    } catch (error) {
      console.error('Error fetching exchange rates:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/calculate-salary', {
        netSalary: parseFloat(netSalary),
        foodExpenses: parseFloat(foodExpenses),
        commuteExpenses: parseFloat(commuteExpenses)
      });
      setResult(response.data);
    } catch (error) {
      console.error('Error calculating salary:', error);
    }
  };

  return (
    <div className="App">
      <h1>MySalary App</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          value={netSalary}
          onChange={(e) => setNetSalary(e.target.value)}
          placeholder="Net Salary (USD)"
          required
        />
        <input
          type="number"
          value={foodExpenses}
          onChange={(e) => setFoodExpenses(e.target.value)}
          placeholder="Food Expenses (LKR)"
          required
        />
        <input
          type="number"
          value={commuteExpenses}
          onChange={(e) => setCommuteExpenses(e.target.value)}
          placeholder="Commute Expenses (LKR)"
          required
        />
        <button type="submit">Calculate Gross Salary</button>
      </form>

      {result && (
        <div>
          <h2>Results</h2>
          <p>Gross Salary (USD): {result.grossSalaryUSD}</p>
          <p>Gross Salary (LKR): {result.grossSalaryLKR}</p>
          {/* Display other calculated values here */}
        </div>
      )}

      <h2>USD-LKR Exchange Rate History</h2>
      <LineChart width={600} height={300} data={exchangeRates}>
        <XAxis dataKey="date" />
        <YAxis />
        <CartesianGrid strokeDasharray="3 3" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="rate" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}

export default App;