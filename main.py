import tkinter as tk
from Commands import check_balance

#create the main window
root = tk.Tk()

#add the title to main window
root.title("ATM Simulator")
#specify main window size
root.geometry("500x400")

#Add account number entry
account_number_entry = tk.Entry(root,width=50)
account_number_entry.pack(side="top")

#add check balance button
check_balance_btn = tk.Button(
    root, 
    text ="check balance",
    command=lambda : check_balance(account_number_entry.get ()))
check_balance_btn.pack(side="top")

#add deposit button
Deposit_btn = tk.Button (root, text = "Deposit")
Deposit_btn.pack (side="top")

#open the main window
root.mainloop()