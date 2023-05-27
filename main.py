from tkinter import *
root = Tk()
root.title("DESKTOP APPLICATION")
root.configure(background="red")
root.minsize(200, 200)  # width, height
root.maxsize(500, 500)
root.geometry("3000x3000+50+50")  # width x height + x + y

# Create Label in our window
text = Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = Label(root, text="- Maya Angelou")
text2.pack()

# Adding an Image
image = PhotoImage(file="trans.png")
image = Label(root, image=image)
image.pack()

# Adding a Button
# use Button and Label widgets to create a simple TV remote
turn_on = Button(root, text="ON")
turn_on.pack()

def volumeUp():
    '''output message to terminal to tell that the button is working'''
    print("Volume Increase +1")

turn_off = Button(root, text="OFF", command=root.quit, background="blue", bd="12px")
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+",command=volumeUp)
vol_up.pack()

vol_down = Button(root, text="-")
vol_down.pack()

# Example of how to arrange Button widget using pack
button1 = Button(root, text="Click me")
button1.pack(side="left")

# Example of how to arrange Label widgets using pack
label1 = Label(root, text="Read me", bg="skyblue")
label1.pack(side="right")
label2 = Label(root, text="Hello", bg="purple")
label2.pack(side="right")

def toggled():
    '''display a message to the terminal every time the check button
    is clicked'''
    print("The check button works.")

# Example of how to arrange Checkbutton widget using pack
var = IntVar()  # Variable to check if checkbox is clicked, or not
check = Checkbutton(root, text="Click me", bg="skyblue", command=toggled, variable=var)
check.pack(side="bottom")

root.mainloop()