# Import the necessary libraries
import datetime
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from forex_python.converter import CurrencyRates

# Define a list of currency identifiers
currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

class CurrencyConverter:
    """A class for creating a simple currency converter GUI.

    Attributes:
        root (tk.Tk): The main window of the GUI.
        from_currency (tk.StringVar): The currency to convert from.
        to_currency (tk.StringVar): The currency to convert to.
        from_menu (tk.OptionMenu): Dropdown menu for selecting the 'from' currency.
        to_menu (tk.OptionMenu): Dropdown menu for selecting the 'to' currency.
        amount_label (tk.Label): Label for displaying 'Amount' text.
        amount_entry (tk.Entry): Entry field for entering the amount.
        convert_button (tk.Button): Button for triggering the conversion.
        result_label (tk.Label): Label for displaying the conversion result.
    """
    def __init__(self):
        """Initialize the CurrencyConverter class."""
        
        # Main windows display
        self.root = tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('1000x1000')
        
        # Define string variables
        self.from_currency = tk.StringVar(self.root)
        self.from_currency.set('USD')
        
        self.to_currency = tk.StringVar(self.root)
        self.to_currency.set('EUR')
        
        # Define drop-down lists
        self.from_menu = tk.OptionMenu(self.root, self.from_currency, *currencies)
        self.from_menu.pack(pady=5)
        
        self.to_menu = tk.OptionMenu(self.root, self.to_currency, *currencies)
        self.to_menu.pack(pady=5)
        
        # Display the final conversion
        self.amount_label = tk.Label(self.root, text='Amount:')
        self.amount_label.pack(pady=5)
        
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)
        
        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert)
        self.convert_button.pack(pady=2)
        
        self.result_label = tk.Label(self.root, text='')
        self.result_label.pack(pady=2)
        
        # Initialize the graph canvas
        self.init_graph()
        self.graph_button = tk.Button(self.root, text='Update Graph', command=self.plot)
        self.graph_button.pack(pady=2)
        
        self.root.mainloop()
        
    def init_graph(self):
        """Initialize the graph canvas."""
        self.fig, self.ax = plt.subplots(figsize=(5,5))
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Exchange Rate')
        self.ax.set_title('Currency Exchange Rate')
        self.graph_window = FigureCanvasTkAgg(self.fig, master=self.root)
        self.graph_window.draw()
        self.graph_window.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def convert(self):
        """Convert the entered amount from one currency to another."""
        
        try:
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            c_rate = CurrencyRates()
            
            conversion_rate = float(c_rate.get_rate(from_curr, to_curr))
            converted = amount * conversion_rate
            
            self.result_label.config(text=f'{amount} {from_curr} = {converted: .2f} {to_curr}')
        except ValueError:
            self.result_label.config(text='Please enter a valid amount')
        except Exception as e:
            self.result_label.config(text=f'An error occurred: {str(e)}')
    
    def plot(self):
        """Display a chart of the currency exchange rate for the last week."""
        try:
            # Clear any previous plots
            self.ax.clear()
            
            # Get the currencies from the buttons
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            # Instantiate a CurrencyRates object
            c_rate = CurrencyRates()
            
            X = []
            Y = []
            
            # Create a datetime object for the last month
            for day in range(7):
                date = datetime.datetime.now() - datetime.timedelta(days=day)
                # Get the conversion rate for that day
                conversion_rate = float(c_rate.get_rate(from_curr, to_curr, date))
                # Append the date and rate to lists
                X.append(date)
                Y.append(conversion_rate)
            
            # Plot the graph
            self.ax.plot(X, Y)
            self.ax.set_xlabel('Date')
            self.ax.set_ylabel(f'{from_curr} to {to_curr} Exchange Rate')
            self.ax.set_title(f'{from_curr} to {to_curr} Exchange Rate')
            self.ax.tick_params(axis='x', rotation=45)
            self.fig.tight_layout()
            self.ax.set_aspect('equal')
            self.graph_window.draw()
        except ValueError:
            self.result_label.config(text='Please enter a valid amount')
        except Exception as e:
            self.result_label.config(text=f'An error occurred: {str(e)}')
        
    