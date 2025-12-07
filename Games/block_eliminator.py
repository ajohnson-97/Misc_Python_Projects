# Fun little brain teaser game. Start by clicking the button with the lowest number 
# and clicking the next lowest number until all the buttons have been clicked. 
# Try to finish the game in the shortest amount of time possible.
#
# Written by Anthony Johnson
# https://github.com/ajohnson-97

import random
import tkinter as tk
from tkinter import messagebox

# Initialize variables
random_int_list = []
start_time = True
time = 0
count_disabled_buttons = 0

# Instantiate window object
window = tk.Tk()
window.title("Block Eliminator")

def random_int_generator():
    """Generate a random integer for the button widgets.

    Generates a random integer between 1-999 to assign to the button widgets,
    then appending the number to a list and discarding any number generated that is already
    in the list so that every button has a unique number associated with it.
    """
    random_int = random.randint(1,999)      # Generate a random integer between 1-999.
  
    while random_int in random_int_list:    # Check that the number generated is unique.
        random_int = random.randint(1,999)
      
    random_int_list.append(random_int)      # Adding the unique integer to the list.
    return random_int                       # Return the integer.

def click(event):
    """Get value from widget clicked and disable if it's the lowest value.

       Check if it's the first time a widget has been clicked, if it is, start the timer by 
       calling the "increment_time()" function. Get the integer value associated with the widget 
       that was clicked and compare it to [0] index of the sorted list (ascending) of randomly 
       generated integers and disable the widget if it's the button with the lowest value and
       remove that value from the list of integers.
    """
    global start_time
    global count_disabled_buttons
  
    if start_time:                          # Check if it's the first button click.
        start_time = not start_time         # Flip the start_time variable to make it known that a button has been clicked and the game has started.
        increment_time()                    # Call the increment_time function to start the timer.
      
    button = event.widget.cget("text")      # Get the value (text attribute) of the button that was clicked (integer).

    # Check to see if the button that was clicked is the lowest value of the buttons in the list
    # by comparing it to the zero index of the sorted (ascending) list of randomly generated integers.
    if button == random_int_list[0]:        
        event.widget.config(state="disabled")    # Disable the widget if it's associated integer is the lowest value in the list.
        count_disabled_buttons += 1              # Increment the count_disabled_buttons variable to update the number of buttons disabled.
        random_int_list.pop(0)                   # Remove the value of the disabled widget from the list so this block of code will work on the next widget clicked.

def increment_time():
    """Start the timer, increment the timer label every second, 
       terminate the program when all buttons have been clicked 
       and display the users score.
    """
    global time
  
    time += 1
    id = row5_col0.after(1000, increment_time)    # Increment the time every second.
    row5_col0.config(text=time)                   # Update the timer label with the new value (every second).
  
    if count_disabled_buttons == 25:              # Check to see if all 25 button widgets have been clicked and disabled.
        row5_col0.after_cancel(id)                # Stop the timer.
        messagebox.showinfo("Game Finished", f"Congratulations!\nYou finished the game in {time} seconds.")    # Display the "Game Finished" popup message, showing the users score.
    
# Instantiate the widgets
row0_col0 = tk.Button(text=random_int_generator(), width=10)
row1_col0 = tk.Button(text=random_int_generator(), width=10)
row2_col0 = tk.Button(text=random_int_generator(), width=10)
row3_col0 = tk.Button(text=random_int_generator(), width=10)
row4_col0 = tk.Button(text=random_int_generator(), width=10)
row0_col1 = tk.Button(text=random_int_generator(), width=10)
row1_col1 = tk.Button(text=random_int_generator(), width=10)
row2_col1 = tk.Button(text=random_int_generator(), width=10)
row3_col1 = tk.Button(text=random_int_generator(), width=10)
row4_col1 = tk.Button(text=random_int_generator(), width=10)
row0_col2 = tk.Button(text=random_int_generator(), width=10)
row1_col2 = tk.Button(text=random_int_generator(), width=10)
row2_col2 = tk.Button(text=random_int_generator(), width=10)
row3_col2 = tk.Button(text=random_int_generator(), width=10)
row4_col2 = tk.Button(text=random_int_generator(), width=10)
row0_col3 = tk.Button(text=random_int_generator(), width=10)
row1_col3 = tk.Button(text=random_int_generator(), width=10)
row2_col3 = tk.Button(text=random_int_generator(), width=10)
row3_col3 = tk.Button(text=random_int_generator(), width=10)
row4_col3 = tk.Button(text=random_int_generator(), width=10)
row0_col4 = tk.Button(text=random_int_generator(), width=10)
row1_col4 = tk.Button(text=random_int_generator(), width=10)
row2_col4 = tk.Button(text=random_int_generator(), width=10)
row3_col4 = tk.Button(text=random_int_generator(), width=10)
row4_col4 = tk.Button(text=random_int_generator(), width=10)
row5_col0 = tk.Label(text=time, width=65)    # Bottom timer label.

# Place widgets in the window using grid().
row0_col0.grid(row=0, column=0)
row1_col0.grid(row=1, column=0)
row2_col0.grid(row=2, column=0)
row3_col0.grid(row=3, column=0)
row4_col0.grid(row=4, column=0)
row0_col1.grid(row=0, column=1)
row1_col1.grid(row=1, column=1)
row2_col1.grid(row=2, column=1)
row3_col1.grid(row=3, column=1)
row4_col1.grid(row=4, column=1)
row0_col2.grid(row=0, column=2)
row1_col2.grid(row=1, column=2)
row2_col2.grid(row=2, column=2)
row3_col2.grid(row=3, column=2)
row4_col2.grid(row=4, column=2)
row0_col3.grid(row=0, column=3)
row1_col3.grid(row=1, column=3)
row2_col3.grid(row=2, column=3)
row3_col3.grid(row=3, column=3)
row4_col3.grid(row=4, column=3)
row0_col4.grid(row=0, column=4)
row1_col4.grid(row=1, column=4)
row2_col4.grid(row=2, column=4)
row3_col4.grid(row=3, column=4)
row4_col4.grid(row=4, column=4)
row5_col0.grid(row=5, column=0, columnspan=5)

window.bind_all("<Button-1>", click)    # Bind the left mouse click with every button in the window to the "click()" function.

random_int_list.sort()                  # Sort the random_int_list (ascending) before running the window to access the [0] index in the "click()" function.

if __name__ == "__main__"
    window.mainloop()                   # Run the program, as long as it's run directly and not imported.
else:
    print("This is not a module")
