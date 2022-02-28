import tkinter.messagebox
from tkinter import*
from tkinter.ttk import*
from PIL import Image, ImageTk

def PigLatin(): # This is the function to translate English to new language "Pig Latin"
    message = str(en1.get()) # Get English sentence from Entry input of GUI. Change input to Entry

    VOLES = ('a', 'e', 'i', 'o', 'u', 'y') # Save the Vowels + y as VOLES. y is Vowels of Pig Latin.

    pigLatin = []  # A list of the words in Pig Latin.
    for word in message.split():
        # split() is for splitting text. (ex) "My name is..." to ["My", "name", "is"]
        # Separate the non-letters at the start of this word;
        prefixNonletters = '' # Save non letters to dispose non letters such as "."
        while len(word) > 0 and not word[0].isalpha():
            # isalpha() is to find out the value is alphabet or not
            prefixNonletters += word[0]
            word = word[1:]
            if len(word) == 0:
                pigLatin.append(prefixNonletters)
                continue
            # Separate the non-letters at the end of this word:
            # Append if entire word is non letters.(ex) 4000)
        suffixNonletters = ''
        while not word[-1].isalpha():
            suffixNonletters += word[-1]
            word = word[:-1]

        # Remember if the word was in uppercase or title case.
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()  # Make the word lowercase for translation.

        # Separate the consonants at the start of this word:
        prefixConsonants = '' # Pulling off consonants and storing them to prefixConsonants
        while len(word) > 0 and not word[0] in VOLES:
            prefixConsonants += word[0]
            word = word[1:]
        # Add the Pig Latin ending to the word:
        if prefixConsonants != '':
            word + prefixConsonants + 'ay'
        else:
            word += 'yay'

        # Set the word back to uppercase or title case:
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        # Add the non-leters back to the start or end of the word.
        pigLatin.append(prefixNonletters + word + suffixNonletters)

    tkinter.messagebox.showinfo("Pig Latin",' '.join(pigLatin))

# Create GUI by Tkinter(Original). Name it as Try
Try = Tk(className="Pig Latin Translator") # set class name as "Pig Latin Translator". Other setting is default.
Try.geometry("400x300") # Set size of interface "400x300"
Try.resizable(0,0) # Do not allow user to expand the interface
Try.config(bg="Orange") # Set background color as "Orange"

#---Uneed Function---#
#Img = PhotoImage(file="csumb.jpg")
#---Unneed Function---#

font_msg = ("Comic Sans MS", 20, "bold") # Setting of font(type, size, bold) for Message
font_label = ("Comic Sans MS", 10)       # Setting of font(type, size) for Label
font_entry = ("Comic Sans MS", 30)       # Setting of font(type, size) for Entry

msg = Message(Try,text="PIG LATIN") # Message widget of Tkinter. Use it as a title ("PIG LATIN")
msg.config(bg="Pink",fg="White",font=font_msg,width=200)
# Setting of the Message. (Background color as "Pink", Font color as "White", Font type = font_msg, width=200)
msg.pack(ipadx=60) # Place the Message on the top of interface. ipadx is size of the Message

Label(Try, text="Enter English message to translate into Pig Latin:", font=font_label).pack()
# Label widget of Tkinter. Use it as an introduction of PIG LATIN function
# (Name of the GUI, Text, Font type(font_label)
# Place it below of Message

#---Unneed Function---#
#var = IntVar()
#Radiobutton(Try, text='Male', variable=var, value=1).grid(row=3,column=0)
#Radiobutton(Try, text='Female', variable=var, value=2).grid(row=3,column=1)
#Radiobutton(Try, text='Other', variable=var, value=3).grid(row=3,column=2)
#---Unneed Function---#

en1 = Entry(Try,width=40,font=font_entry)
# Entry widget of Tkinter
# Allows user to put English sentence
# (Name of the GUI, width, Font type(font_entry))
en1.pack(ipadx=60,ipady=60)
# Place Entry below the Label. (ipadx and ipady are size of Entry)

btn = Button(Try,text="Translate",command=PigLatin)
# Button widget of Tkinter
# Create button to activate the function
# (Name of the GUI, Text, Command(activate function when user click this button) = PigLatin())
# Write PigLatin() as PigLatin. Otherwise the function is activated automatically without clicking.
btn.pack()
# Place this button below the Entry

#---Unneed function---#
#Label(Try, image=Img).pack()
#---Unneed function---#

Try.mainloop() # Activate the GUI

#---Sources---#
# TkinterGUI = https://pythongeeks.org/gui-programming-in-python/
# Pig Latin = https://gist.github.com/kappter/9936137