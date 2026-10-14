"""
Stock Portfolio Tracker
CodeAlpha Python Programming Internship - Task 2

A simple console application that calculates the value of a portfolio
using hardcoded sample stock prices. No external libraries, no live
market data, no database.
"""

import csv

# Sample prices are static, as required by the task.
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 160,
    "AMZN": 190,
}

LINE_WIDTH = 46


def format_currency(amount):
    """Return a readable dollar amount, for example $1,400.00."""
    return f"${amount:,.2f}"


def display_welcome():
    """Print the program title."""
    print("=" * 40)
    print("STOCK PORTFOLIO TRACKER".center(40))
    print("=" * 40)
    print()


def display_stocks():
    """Print every available stock symbol and its price."""
    print("Available Stocks:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol:<6} - {format_currency(price)}")
    print()


def get_stock_input():
    """Ask for a stock symbol until a valid one is entered."""
    while True:
        symbol = input("Enter stock symbol: ").strip().upper()

        if not symbol:
            print("Stock symbol cannot be empty.\n")
        elif symbol not in stock_prices:
            print("Stock not found. Please enter a valid stock symbol.")
            print(f"Valid symbols: {', '.join(stock_prices)}\n")
        else:
            return symbol


def get_quantity():
    """Ask for a quantity until a positive whole number is entered."""
    while True:
        raw_quantity = input("Enter quantity: ").strip()

        if not raw_quantity:
            print("Quantity cannot be empty. Please enter a number.\n")
            continue

        try:
            quantity = int(raw_quantity)
        except ValueError:
            print("Invalid quantity. Please enter a whole number, such as 5.\n")
            continue

        if quantity <= 0:
            print("Invalid quantity. Quantity must be greater than 0.\n")
            continue

        return quantity


def calculate_investment(price, quantity):
    """Return the value of a single holding: price x quantity."""
    return price * quantity


def calculate_total(portfolio):
    """Return the total value of every holding in the portfolio."""
    return sum(entry["value"] for entry in portfolio)


def ask_add_another():
    """Ask whether the user wants to add another stock."""
    while True:
        answer = input("Add another stock? (yes/no): ").strip().lower()

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False

        print("Please enter 'yes' or 'no'.")


def display_portfolio(portfolio, total):
    """Print the portfolio table and the total investment."""
    print()
    print("=" * LINE_WIDTH)
    print("PORTFOLIO SUMMARY".center(LINE_WIDTH))
    print("=" * LINE_WIDTH)
    print()
    print(f"{'Stock':<8}{'Price':>12}{'Quantity':>12}{'Value':>14}")
    print("-" * LINE_WIDTH)

    for entry in portfolio:
        print(
            f"{entry['symbol']:<8}"
            f"{format_currency(entry['price']):>12}"
            f"{entry['quantity']:>12}"
            f"{format_currency(entry['value']):>14}"
        )

    print("-" * LINE_WIDTH)
    print(f"{'Total Investment':<34}{format_currency(total):>12}")
    print("=" * LINE_WIDTH)


def write_txt(filename, portfolio, total):
    """Save a readable plain-text summary."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Stock Portfolio Summary\n\n")
        for entry in portfolio:
            file.write(
                f"{entry['symbol']} - Price: {format_currency(entry['price'])}, "
                f"Quantity: {entry['quantity']}, "
                f"Value: {format_currency(entry['value'])}\n"
            )
        file.write(f"\nTotal Investment: {format_currency(total)}\n")


def write_csv(filename, portfolio, total):
    """Save the summary as comma-separated values."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Price", "Quantity", "Value"])
        for entry in portfolio:
            writer.writerow(
                [
                    entry["symbol"],
                    entry["price"],
                    entry["quantity"],
                    entry["value"],
                ]
            )
        writer.writerow(["TOTAL", "", "", total])


def save_to_file(portfolio, total):
    """Ask for an output format and save the summary to that file."""
    print()
    while True:
        choice = input("Save summary to file? (txt/csv/no): ").strip().lower()

        if choice == "txt":
            filename = "portfolio.txt"
            save_function = write_txt
            break
        if choice == "csv":
            filename = "portfolio.csv"
            save_function = write_csv
            break
        if choice in ("", "no", "n"):
            print("Summary not saved.")
            return None

        print("Please enter 'txt', 'csv' or 'no'.")

    try:
        save_function(filename, portfolio, total)
    except OSError as error:
        print(f"Could not write {filename}: {error}")
        return None

    print(f"\nPortfolio saved to {filename}")
    return filename


def collect_portfolio():
    """Collect stock holdings from the user until they choose to finish."""
    portfolio = []

    while True:
        symbol = get_stock_input()
        quantity = get_quantity()
        price = stock_prices[symbol]
        value = calculate_investment(price, quantity)

        portfolio.append(
            {
                "symbol": symbol,
                "price": price,
                "quantity": quantity,
                "value": value,
            }
        )
        print(f"\nInvestment added: {format_currency(value)}\n")

        if not ask_add_another():
            return portfolio


def main():
    """Run the Stock Portfolio Tracker."""
    display_welcome()
    display_stocks()

    try:
        portfolio = collect_portfolio()
    except (KeyboardInterrupt, EOFError):
        print("\n\nInput cancelled.")
        portfolio = []

    if not portfolio:
        print("\nNo stocks were added, so there is nothing to summarise.")
        return

    total = calculate_total(portfolio)
    display_portfolio(portfolio, total)

    try:
        save_to_file(portfolio, total)
    except (KeyboardInterrupt, EOFError):
        print("\nSave cancelled.")


if __name__ == "__main__":
    main()
