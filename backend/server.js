// File: backend/server.js
const express = require('express');
const cors = require('cors');
const mysql = require('mysql2/promise');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

app.post('/calculate-salary', async (req, res) => {
  const { netSalary, foodExpenses, commuteExpenses } = req.body;
  
  try {
    // Fetch the latest exchange rate from the database
    const [rateRows] = await pool.query('SELECT rate FROM exchange_rates ORDER BY date DESC LIMIT 1');
    const exchangeRate = rateRows[0].rate;

    // Calculate gross salary (this is a simplified version, you'll need to implement the full logic)
    const usdAmount = netSalary * 0.5;
    const lkrAmount = netSalary * 0.5 * exchangeRate;
    
    // TODO: Implement tax calculation based on the provided tax slabs
    // TODO: Implement EPF and ETF deductions
    // TODO: Subtract food and commute expenses

    res.json({
      grossSalaryUSD: usdAmount,
      grossSalaryLKR: lkrAmount,
      // Include other calculated values here
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred while calculating the salary' });
  }
});

app.get('/exchange-rates', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT date, rate FROM exchange_rates ORDER BY date DESC LIMIT 12');
    res.json(rows);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred while fetching exchange rates' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));