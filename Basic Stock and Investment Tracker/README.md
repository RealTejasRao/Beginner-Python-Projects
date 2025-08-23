# Basic Stock and Investment Tracker

A Python-based stock market application that allows users to buy, sell, track stock prices, manage their investment portfolio, and visualize stock performance with real-time data from Yahoo Finance.

The application features a colorful command-line interface, real-time stock price fetching, portfolio management with CSV storage, profit/loss calculations, and graphical stock analysis capabilities.

## 📌 How It Works

1. **Imports and Setup**: The code starts by importing necessary modules - `colorama` for colored text output, `yfinance` for real-time stock data, `csv` for portfolio storage, `matplotlib` for stock price graphs, and `os` for file operations.

2. **Investment Class**: An `Investment` class is defined that contains all the stock trading and portfolio management methods. When the program starts, it creates an instance of this class which automatically calls the `__init__` method.

3. **Main Menu Loop**: The `__init__` method displays a menu asking users to choose an action (buy/sell/price/portfolio/graph/help/exit), validates their input, and calls the appropriate method based on their choice.

4. **Buy Method**: Prompts for stock ticker symbol, fetches real-time price using Yahoo Finance API, asks for quantity (limited to 1000 shares), calculates total cost, confirms purchase, and saves transaction to `data.csv` file. If stock already exists in portfolio, it updates the existing entry.

5. **Sell Method**: Checks if portfolio exists, prompts for stock ticker to sell, fetches current market price, calculates profit/loss based on purchase price, confirms sale, removes stock from portfolio, and displays profit/loss information with color coding.

6. **Price Method**: Allows users to check real-time stock prices by entering ticker symbols, fetches current closing price from Yahoo Finance, and displays rounded price value.

7. **Portfolio Method**: Reads the `data.csv` file and displays all owned stocks with their quantities and total purchase costs in a formatted, color-coded output.

8. **Graph Method**: Takes a stock ticker symbol, fetches 6 months of historical data from Yahoo Finance, creates a matplotlib line chart showing closing prices over time.

9. **Help Method**: Displays all available actions with descriptions and provides common stock ticker examples (AAPL, MSFT, TSLA, AMZN, GOOGL, META, NVDA, NFLX) along with a link to find more tickers.

10. **Data Persistence**: All portfolio data is automatically saved to `data.csv` file in CSV format with columns for stock name, number of shares, and total cost, ensuring data persistence between program sessions.

11. **Error Handling**: The application includes comprehensive error handling for invalid stock symbols, file operations, and user input validation to provide a robust user experience.

12. **Program Flow**: After each operation, the program returns to the main menu, allowing users to perform multiple actions in a single session. The exit command saves all data and gracefully terminates the program.
