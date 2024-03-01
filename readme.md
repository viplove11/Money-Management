# Budget Management System

This Python script provides functionality for managing a budget with support for depositing and withdrawing money, tracking transactions, and displaying budget details categorized by expenses.

## Dependencies
- `mysql-connector-python`: for connecting to the MySQL database
- `os`: for system operations like clearing the screen
- `time`: for time-related operations

## Database Setup
1. Install MySQL and create a database named `Budget`.
2. Below are the details of the database tables:

### Table: `admin`
- Columns:
  - `admin_id` (INT, Primary Key, Auto Increment)
  - `admin_name` (VARCHAR)
  - `admin_pass` (VARCHAR)

### Table: `deposit`
- Columns:
  - `deposit_id` (INT, Primary Key, Auto Increment)
  - `Date_time` (DATETIME)
  - `deposit_amount` (FLOAT)

### Table: `withdraw`
- Columns:
  - `date_time` (DATETIME)
  - `category` (VARCHAR)
  - `reason` (VARCHAR)
  - `withdraw_amount` (FLOAT)
  - `balanced_amount` (FLOAT)

## Usage
1. Run the script.
2. Choose between registration and login options.
3. After logging in as an admin, you can deposit or withdraw money, display transactions, and view budget details.
4. Follow the on-screen prompts to perform the desired operation.

## Features
- Secure admin registration and login functionality.
- Deposit and withdraw money from the budget.
- Track transactions with date, category, reason, withdraw amount, and balanced amount.
- Display budget details categorized by expenses.
- Simple and intuitive interface.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
