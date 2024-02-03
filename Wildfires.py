from tkinter import *
from DataCompiler import func
from PIL import Image, ImageTk
from Location import location

def update_label(): # This function checks the inputted values and finds the risk assessment.
    try:
        global responses
        location = clicked0.get()  # Get the selected location from the dropdown menu

        # Get the selected range of fire and map it to a numerical value
        range_of_fire = clicked1.get()
        if range_of_fire == '1':
            fire_range = 10
        elif range_of_fire == '2':
            fire_range = 100
        elif range_of_fire == '3':
            fire_range = 500
        elif range_of_fire == '4':
            fire_range = 1000
        elif range_of_fire == '5':
            fire_range = 2000

        difficulty = int(clicked2.get())  # Get the selected difficulty value
        severity = int(clicked3.get())    # Get the selected severity value
        
        responses = [location, fire_range, difficulty, severity]  # Store the selected values in a list
        new_text = func(responses)  # Call a function to compute the risk assessment based on the selected values
        main_label.config(text=new_text)  # Update the label with the computed risk assessment
    except:
        main_label.config(text='Please Fill All The Required Information')  # Display an error message if not all information is provided

# Create the main tkinter window
root = Tk()
root.title("Wildfires")
root.geometry("1920x1080")

# Load and display an image on the window
image = Image.open("ForestFire.png")
resize_image = image.resize((1920, 1080))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(root, image=img)
label1.image = img
label1.place(x=0, y=0, relwidth=1, relheight=1)

# Create and display a label for the application title
label = Label(root, text='WILDFIRE', bg='orange', fg='white')
label.config(font=('Times New Roman', 44, 'bold'))
label.pack(pady=20)

# Create and display a label with the selected location
label = Label(root, text='(' + location() + ')', bg='orange', fg='white')
label.config(font=('Times New Roman', 30, 'bold'))
label.pack(pady=10)

# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
]
Locations = [
    "Vancouver",
    "Fort McMurray",
    "Beijing",
]

# Create dropdown menus for different parameters
clicked0 = StringVar()
clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()

clicked0.set("Location")  # Set the initial menu text
drop = OptionMenu(root, clicked0, *Locations)  # Create the location dropdown menu
drop.config(font=('Times New Roman', 14, 'bold'), fg='white', bg='black')
drop.pack(padx=10, pady=10)

clicked1.set("Range Of Fire")
drop = OptionMenu(root, clicked1, *options)  # Create the range of fire dropdown menu
drop.config(font=('Times New Roman', 14, 'bold'), fg='white', bg='black')
drop.pack(padx=10, pady=10)

clicked2.set("Difficulty to contain the Fire")
drop = OptionMenu(root, clicked2, *options)  # Create the difficulty dropdown menu
drop.config(font=('Times New Roman', 14, 'bold'), fg='white', bg='black')
drop.pack(padx=10, pady=10)

clicked3.set("Severity Of Fire")
drop = OptionMenu(root, clicked3, *options)  # Create the severity dropdown menu
drop.config(font=('Times New Roman', 14, 'bold'), fg='white', bg='black')
drop.pack(padx=10, pady=10)

# Create and display an "ENTER" button that triggers the update_label function
button = Button(root, text="ENTER", command=update_label)
button.config(font=('Calibri', 18, 'bold'), fg='black', bg='white')
button.pack(padx=10, pady=10)

# Create and display a label for the risk assessment result
main_label = Label(root, text='')
main_label.config(font=('Times New Roman', 18, 'bold'), bg='orange')
main_label.pack()

# Start the tkinter main loop to run the application
root.mainloop()
