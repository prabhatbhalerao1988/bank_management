Classes:

Transaction: Represents a transaction (either "Deposit" or "Withdraw") with an amount.
Account: Represents a bank account with properties like account number, account holder name, balance, and a list of transactions.
Bank: A container for all bank accounts. It manages account creation, transaction handling, and finding specific accounts by number.

Methods:

Methods like deposit, withdraw, and view_statement are now part of the Account class. These methods modify the account's balance and transaction history.
The Bank class contains the logic to create accounts, find accounts by account number, and provide the necessary functions for deposits, withdrawals, and viewing bank statements.
