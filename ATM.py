import tkinter as tk
from tkinter import messagebox, font

class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        return f"Your current balance is ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount:.2f} has been deposited. {self.check_balance()}"
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"${amount:.2f} has been withdrawn. {self.check_balance()}"
            else:
                return "Insufficient funds. Withdrawal cancelled."
        else:
            return "Invalid withdrawal amount. Please enter a positive number."

class ATMGUI:
    def __init__(self, master):
        self.master = master
        self.atm = ATM(1000)  # Initialize with $1000
        master.title("ATM Simulator")
        master.geometry("400x500")
        master.configure(bg='#f0f0f0')

        self.style()

        self.create_widgets()

    def style(self):
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)
        self.button_font = font.Font(family="Helvetica", size=10, weight="bold")

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.master, text="ATM Simulator", font=self.title_font, bg='#f0f0f0', fg='#333333')
        self.title_label.pack(pady=20)

        # Balance Frame
        self.balance_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.balance_frame.pack(pady=10)

        self.balance_button = tk.Button(self.balance_frame, text="Check Balance", command=self.check_balance,
                                        font=self.button_font, bg='#4CAF50', fg='white', padx=10, pady=5)
        self.balance_button.pack()

        # Deposit Frame
        self.deposit_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.deposit_frame.pack(pady=10)

        self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Amount:", font=self.label_font, bg='#f0f0f0')
        self.deposit_label.pack(side=tk.LEFT, padx=5)

        self.deposit_entry = tk.Entry(self.deposit_frame, font=self.label_font, width=15)
        self.deposit_entry.pack(side=tk.LEFT, padx=5)

        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=self.deposit,
                                        font=self.button_font, bg='#2196F3', fg='white', padx=10, pady=5)
        self.deposit_button.pack(side=tk.LEFT, padx=5)

        # Withdraw Frame
        self.withdraw_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.withdraw_frame.pack(pady=10)

        self.withdraw_label = tk.Label(self.withdraw_frame, text="Withdraw Amount:", font=self.label_font, bg='#f0f0f0')
        self.withdraw_label.pack(side=tk.LEFT, padx=5)

        self.withdraw_entry = tk.Entry(self.withdraw_frame, font=self.label_font, width=15)
        self.withdraw_entry.pack(side=tk.LEFT, padx=5)

        self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw", command=self.withdraw,
                                         font=self.button_font, bg='#FF9800', fg='white', padx=10, pady=5)
        self.withdraw_button.pack(side=tk.LEFT, padx=5)

    def check_balance(self):
        messagebox.showinfo("Balance", self.atm.check_balance())

    def deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            result = self.atm.deposit(amount)
            messagebox.showinfo("Deposit", result)
            self.deposit_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            result = self.atm.withdraw(amount)
            messagebox.showinfo("Withdraw", result)
            self.withdraw_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ATMGUI(root)
    root.mainloop()