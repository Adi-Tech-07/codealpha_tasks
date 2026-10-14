# Stock Portfolio Tracker

**CodeAlpha Python Programming Internship - Task 2**

A simple Python console application that calculates the value of a stock portfolio
from manually defined stock prices. The user adds stocks and quantities, and the
program works out the value of each holding plus the total investment.

## Description

Stock Portfolio Tracker is a beginner-friendly command line program. It shows a
small list of sample stocks with fixed prices, asks which stocks you want to own
and how many shares, then prints a clean portfolio summary with the total
investment value. The summary can optionally be saved to a text or CSV file.

The prices are static sample values written in the source code, as required by the
task. There is no live market data, no database and no third-party library.

## Objective

- Store sample stock prices in a Python dictionary.
- Accept stock symbols and quantities from the user.
- Validate user input and recover from mistakes without crashing.
- Calculate each holding's value as price x quantity.
- Calculate and display the total investment.
- Optionally save the summary to a `.txt` or `.csv` file.

## Features

- Hardcoded stock price dictionary with AAPL, TSLA, MSFT, GOOGL and AMZN.
- Case-insensitive symbol entry (`aapl` and `AAPL` both work).
- Add as many stocks as you like before finishing.
- Validation for unknown symbols, empty input, non-numeric quantities, zero and negative quantities.
- Validated yes/no prompts for "add another stock?" and for saving.
- Aligned portfolio table showing stock, price, quantity, value and total investment.
- Optional save to `portfolio.txt` or `portfolio.csv`.
- Graceful handling of `Ctrl+C` and end-of-input instead of a traceback.
- Zero third-party dependencies.

## Technologies Used

| Item | Detail |
| --- | --- |
| Language | Python 3 |
| Data structure | `dict` for prices, `list` of `dict` for holdings |
| I/O | `input()` and `print()` |
| Logic | `for` / `while` loops, `if` / `elif` / `else`, functions |
| Error handling | `try` / `except ValueError`, `try` / `except (KeyboardInterrupt, EOFError)` |
| File handling | built-in `open()`, standard library `csv` module |
| Dependencies | None |

## Project Structure

```text
Stock Portfolio Tracker/
|-- portfolio_tracker.py                      # application code
|-- README.md                                 # project documentation
|-- .gitignore                                # ignores caches and generated files
|-- CodeAlpha_StockPortfolioTracker_PRD.md    # project requirements document
`-- portfolio.txt / portfolio.csv             # created only when you choose to save
```

## How It Works

1. The program prints a welcome banner and the available stocks.
2. It asks for a stock symbol and checks it against the price dictionary.
3. It asks for a quantity and checks that it is a whole number greater than zero.
4. It calculates `price x quantity` and stores the holding.
5. It asks whether to add another stock and repeats until you answer `no`.
6. It prints the portfolio table and the total investment.
7. It optionally saves the summary to a text or CSV file.

Program flow:

```text
Start -> welcome -> show stocks -> ask symbol -> validate -> ask quantity
      -> validate -> calculate value -> store holding -> add another?
      -> (loop) -> calculate total -> show summary -> save? -> Exit
```

## Setup and Run Instructions

Requirements: Python 3.6 or newer. No packages to install.

```bash
git clone https://github.com/<your-username>/CodeAlpha_StockPortfolioTracker.git
cd CodeAlpha_StockPortfolioTracker
python portfolio_tracker.py
```

On some systems the command is `python3 portfolio_tracker.py`.

## Example Usage

Enter the values shown in the prompts:

```text
Enter stock symbol: AAPL
Enter quantity: 5
Add another stock? (yes/no): yes
Enter stock symbol: TSLA
Enter quantity: 2
Add another stock? (yes/no): no
Save summary to file? (txt/csv/no): txt
```

## Example Output

```text
========================================
        STOCK PORTFOLIO TRACKER
========================================

Available Stocks:
  AAPL   - $180.00
  TSLA   - $250.00
  MSFT   - $420.00
  GOOGL  - $160.00
  AMZN   - $190.00

Enter stock symbol: AAPL
Enter quantity: 5

Investment added: $900.00

Add another stock? (yes/no): yes
Enter stock symbol: TSLA
Enter quantity: 2

Investment added: $500.00

Add another stock? (yes/no): no

==============================================
              PORTFOLIO SUMMARY
==============================================

Stock          Price    Quantity         Value
----------------------------------------------
AAPL         $180.00           5       $900.00
TSLA         $250.00           2       $500.00
----------------------------------------------
Total Investment                     $1,400.00
==============================================

Save summary to file? (txt/csv/no): txt

Portfolio saved to portfolio.txt
```

Error handling looks like this:

```text
Enter stock symbol: XYZ
Stock not found. Please enter a valid stock symbol.
Valid symbols: AAPL, TSLA, MSFT, GOOGL, AMZN

Enter quantity: abc
Invalid quantity. Please enter a whole number, such as 5.

Enter quantity: 0
Invalid quantity. Quantity must be greater than 0.
```

## File Saving

After the summary is printed you can choose `txt`, `csv` or `no`. The file is
written to the folder you run the program from and is listed in `.gitignore`.

`portfolio.txt`:

```text
Stock Portfolio Summary

AAPL - Price: $180.00, Quantity: 5, Value: $900.00
TSLA - Price: $250.00, Quantity: 2, Value: $500.00

Total Investment: $1,400.00
```

`portfolio.csv`:

```text
Stock,Price,Quantity,Value
AAPL,180,5,900
TSLA,250,2,500
TOTAL,,,1400
```

## Concepts Demonstrated

- Dictionaries for lookup of stock prices.
- Lists of dictionaries to store the portfolio.
- `input()` and `print()` for console interaction.
- Basic arithmetic for value and total calculation.
- `while` loops for repeated input and re-validation.
- `for` loops for the stock list and summary table.
- Conditional logic for validation and yes/no prompts.
- Functions to split the program into small, readable steps.
- `try` / `except` for input, interrupt and file errors.
- Standard file handling with `open()` and the `csv` module.
- f-strings for aligned, formatted output.

## Testing

Manual test cases, all passing:

| # | Test | Input | Expected | Result |
| --- | --- | --- | --- | --- |
| 1 | One valid stock | `AAPL`, `5` | value 900, total $900.00 | Pass |
| 2 | Multiple stocks | `AAPL` x5, `TSLA` x2 | total $1,400.00 | Pass |
| 3 | Invalid stock | `XYZ` | "Stock not found" message, retries | Pass |
| 4 | Text quantity | `abc` | "Invalid quantity" message, retries | Pass |
| 5 | Zero quantity | `0` | "must be greater than 0" message | Pass |
| 6 | Negative quantity | `-5` | "must be greater than 0" message | Pass |
| 7 | Empty quantity | blank line | "cannot be empty" message | Pass |
| 8 | Empty symbol | blank line | "cannot be empty" message | Pass |
| 9 | Lowercase symbol | `aapl`, `4` | accepted, value $720.00 | Pass |
| 10 | All five stocks | one share of each | total $1,200.00 | Pass |
| 11 | Invalid yes/no | `maybe` | "Please enter 'yes' or 'no'." | Pass |
| 12 | TXT save | choose `txt` | `portfolio.txt` created with correct total | Pass |
| 13 | CSV save | choose `csv` | `portfolio.csv` created with correct total | Pass |
| 14 | No save | choose `no` | no file written | Pass |
| 15 | Invalid save choice | `pdf` | "Please enter 'txt', 'csv' or 'no'." | Pass |
| 16 | End of input | truncated input | exits cleanly, no traceback | Pass |

To reproduce a test, run `python portfolio_tracker.py` and type the values from
the table at each prompt.

## CodeAlpha Internship Context

This project is **Task 2 - Stock Portfolio Tracker** of the CodeAlpha Python
Programming Internship. The scope is intentionally limited to core Python
concepts: dictionaries, user input, arithmetic, loops, conditions and functions.
Live price APIs, databases, web frameworks, GUIs, authentication and prediction
features are deliberately out of scope.

## Author

- **Name:** Your Name
- **Role:** Python Programming Intern, CodeAlpha
- **Task:** Task 2 - Stock Portfolio Tracker

Update the name above with your own before submitting the repository.
