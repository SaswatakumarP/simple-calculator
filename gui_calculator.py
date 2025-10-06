import tkinter as tk
from tkinter import ttk, messagebox
import operator

# Dictionary mapping operator symbols to their corresponding functions
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

class SimpleCalculatorApp:
    """
    A simple two-number arithmetic calculator implemented with Tkinter.
    """
    def __init__(self, master):
        self.master = master
        master.title("Python GUI Calculator")
        master.resizable(False, False)
        
        # Style configuration for a modern look
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#f4f4f4')
        style.configure('TLabel', background='#f4f4f4', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10, 'bold'), padding=5)
        style.map('TButton', background=[('active', '#e0e0e0')])

        # State variables
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Result: N/A")
        self.selected_operator = tk.StringVar(value='+') # Default operator

        # --- Main Frame Setup ---
        main_frame = ttk.Frame(master, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # --- Input Fields ---

        # Number 1
        ttk.Label(main_frame, text="First Number:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.num1_var, width=15, justify='center', font=('Arial', 12)).grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Number 2
        ttk.Label(main_frame, text="Second Number:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.num2_var, width=15, justify='center', font=('Arial', 12)).grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # --- Operator Buttons ---
        ttk.Label(main_frame, text="Operation:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        
        op_frame = ttk.Frame(main_frame)
        op_frame.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Create buttons for each operator
        for i, op in enumerate(OPERATORS.keys()):
            button = ttk.Button(op_frame, text=op, width=4, command=lambda o=op: self.set_operator(o))
            button.grid(row=0, column=i, padx=2, pady=2, sticky=tk.W)
        
        # Highlight the default operator
        self.highlight_operator(self.selected_operator.get())
            
        # --- Calculate Button ---
        ttk.Button(main_frame, text="Calculate", command=self.perform_calculation, style='TButton').grid(row=3, column=0, columnspan=2, padx=5, pady=15, sticky=(tk.W, tk.E))

        # --- Result Display ---
        self.result_label = ttk.Label(main_frame, textvariable=self.result_var, font=('Arial', 14, 'bold'), foreground='#0056b3', anchor='center')
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky=(tk.W, tk.E))
        
    def set_operator(self, op):
        """Sets the current operator and updates the button highlights."""
        self.selected_operator.set(op)
        self.highlight_operator(op)

    def highlight_operator(self, selected_op):
        """Highlights the currently selected operator button."""
        for child in self.master.winfo_children()[0].winfo_children()[2].winfo_children():
            if isinstance(child, ttk.Button):
                # Check if the button's text matches the selected operator
                if child['text'] == selected_op:
                    child.configure(style='Active.TButton')
                else:
                    child.configure(style='TButton')
        
        # Define the active style (only needs to be done once, but here for clarity)
        style = ttk.Style()
        style.configure('Active.TButton', background='#0056b3', foreground='white')
        style.map('Active.TButton', background=[('active', '#004494')])


    def calculate(self, num1, num2, op_symbol):
        """
        Performs the specified arithmetic operation on two numbers.
        Returns the result and an error message (if any).
        """
        operation_func = OPERATORS.get(op_symbol)
        
        if operation_func is None:
            return None, f"Invalid operator: {op_symbol}"

        if op_symbol == '/' and num2 == 0:
            return None, "Cannot divide by zero."

        try:
            result = operation_func(num1, num2)
            return result, None
        except Exception as e:
            return None, f"Calculation error: {e}"

    def perform_calculation(self):
        """
        Handles button click, validates input, calls calculation, and displays result.
        """
        try:
            # 1. Validate and convert inputs
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            op_symbol = self.selected_operator.get()
            
            # 2. Perform calculation
            result, error_message = self.calculate(num1, num2, op_symbol)

            # 3. Display output
            if error_message:
                self.result_var.set(f"Error: {error_message}")
                self.result_label.configure(foreground='red')
            else:
                self.result_var.set(f"Result: {result:.2f}")
                self.result_label.configure(foreground='#0056b3')

        except ValueError:
            self.result_var.set("Error: Invalid number input.")
            self.result_label.configure(foreground='red')
            messagebox.showerror("Input Error", "Please ensure both inputs are valid numbers.")
        except Exception as e:
            self.result_var.set("An unexpected error occurred.")
            self.result_label.configure(foreground='red')
            messagebox.showerror("System Error", f"An unexpected error occurred: {e}")

def run_app():
    """Initializes and runs the Tkinter application."""
    root = tk.Tk()
    app = SimpleCalculatorApp(root)
    root.mainloop()


run_app()
