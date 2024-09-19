# MySalaryApp
A web application to calculate the gross salary when the employee login and enter the net salalry. The gross salary calculation is done as follows : - Net salary is given as input in USD. - 50% of Net salary is credited to the employee's RFC account in USD. - Remaining 50% is converted to LKR according the the USD to LKR exchange reate in https://www.oanda.com/currency-converter/en/?from=USD&to=LKR&amount=1 as per 15th of that month (so need to keep a record of the rate on 15 every month) - The LKR amount is accounted to taxing according to the government criteria as follows : tax slab, Rate (%), tax Rs. 0.00 - Rs. 100,000.00, 0%, Rs. 0.00 Rs. 100,000.00 - Rs. 141,667.00, 6%, Rs. 2,500.00 Rs. 141,667.00 - Rs. 183,333.00, 12%, Rs. 5,000.00 Rs. 183,333.00 - Rs. 225,000.00, 18%, Rs. 7,500.00 Rs. 225,000.00 - Rs. 266,667.00, 24%, Rs. 10,000.00 Rs. 266,667.00 - Rs. 308,333.00, 30%, Rs. 12,500.00 Rs. 308,333.00 - Rs. 500,000.00, 36%, Rs. 69,000.12 - EPF and ETF is also decuted from the LKR salary - Expenses for food and commute is also decuted, so need fields for the employee to input the values - Final net salary should be displayed in as two, the USD amount and LKR amount Also, there should be a graph showing the variation of the USD - LKR exchange rate on every months 15th, and this should be done from the oand website information Need to use a python scripts to get the exchange rates and the tax calculations results from the above given websites, but the webpage should be used to do the tasks, no Front-End React JS Graph to track the USD-LKR exchange rate every month Form to submit net salaray, expenses and finally calculate the gross salaray Back-End Express JS Database MySQL


Salary Calculator App
----------------------

I want to create a web application using python Flask, that will calculate my monthly salary.
The app should be able to save all the values to a database that I input and give a table with the history of input values in a different tab. In the main tab it should take the following float input values from the user : 
1. Salary 50% in LKR
2. Salary 50% in USD
3. Commute Expenses
4. Food Expenses
5. EPF % on Salary 50% in LKR
6. ETF % on Salary 50% in LKR
7. Other Expenses (Also a comment indicating the other expsese)
8. USD to LKR Exchange rate

The final net salary calculation should be done as following.

Step 1 : Convert the "2. Salary 50% in USD" to LKR using the "8. USD to LKR Exchange rate".
Step 2 : Add the above value from Step 1 to "1. Salary 50% in LKR"
Step 3 : Add all expenses "3. Commute Expenses" + "4. Food Expenses" + "7. Other Expenses" + "1. Salary 50% in LKR" * "5. EPF % on Salary 50% in LKR" + "1. Salary 50% in LKR" * "6. ETF % on Salary 50% in LKR". Note the multiplication of EPF and ETF from the "1. Salary 50% in LKR"
Step 4 : Output the final net salary as "Step 2" final value -  "Step 3" final value.

Also, I need the graph showing the variation of the exchange rate. As in the start there are no data to plot, initialize the history values of 1 USD to LKR as : 


Date            LKR
Sep 19, 2024	304.678	
Sep 18, 2024	303.444	
Sep 17, 2024	302.504	
Sep 16, 2024	302.163	
Sep 13, 2024	301.500	
Sep 12, 2024	301.300	
Sep 11, 2024	300.800	
Sep 10, 2024	300.500	
Sep 09, 2024	300.800	
Sep 06, 2024	298.900	
Sep 05, 2024	298.750	
Sep 04, 2024	298.850	
Sep 03, 2024	299.000	
Sep 02, 2024	298.900	
Aug 30, 2024	299.000	
Aug 29, 2024	300.000	
Aug 28, 2024	300.500	
Aug 27, 2024	300.300	
Aug 26, 2024	300.700	
Aug 23, 2024	299.700	
Aug 22, 2024	301.000	
Aug 21, 2024	300.250	
Aug 20, 2024	299.400	
Aug 19, 2024	298.818	

