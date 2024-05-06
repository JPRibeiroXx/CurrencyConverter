# Currency Converter with Exchange Rate Graph

This project is a simple currency converter GUI that allows users to convert between different currencies. The main inspiration for this project comes from [this YouTube tutorial](https://www.youtube.com/watch?v=e4KGT7EvX1o&t=446s). However, I've extended the functionality by adding a graph of exchange rates for the past weeks for the selected currencies.

## Features
- Allows users to select the currency to convert from and to.
- Displays the current exchange rate and performs the currency conversion.
- Provides a graph of exchange rates for the past week for the selected currencies.
- Graph updates dynamically based on the selected currencies.

## How to Use
1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the `main.py` file.
4. Select the currencies you want to convert from and to using the dropdown menus.
5. Enter the amount you want to convert and click the "Convert" button.
6. The converted amount will be displayed, along with the current exchange rate.
7. Click the "Update Graph" button to view the exchange rate graph for the past week.

## Dependencies
- `forex-python`: Python library for fetching exchange rates from various sources.
- `matplotlib`: Python library for creating static, animated, and interactive visualizations in Python.

## Credits
- The main project idea and initial implementation are based on the YouTube tutorial by [Neuralnine](https://www.youtube.com/watch?v=e4KGT7EvX1o&t=446s).
- Additional features, such as the exchange rate graph, were implemented by JPRibeiroXx.

## License
This project is licensed under the [APACHE License].
