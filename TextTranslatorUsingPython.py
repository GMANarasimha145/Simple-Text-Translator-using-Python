#importing Required Libraries
from tkinter import ttk
from tkinter import *
from googletrans import Translator, LANGUAGES

#creating root object of Tk, to create labels and buttons
root=Tk()
root.geometry("900x500")
root.iconbitmap(r"C:\Users\HP\OneDrive\Documents\MyPic_Green Cropped.ico")
root['bg']="#9acd32"
root.title("Simple Language Translator")
root.resizable(100,100)

#Main Label to place at Center of Window.
Label(root,text="Language Translator ",font="arial 20 bold",bg="white smoke").pack()

#Prompt Label for user to "Enter text below"
Label(root, text="Exter Text below:",font="arial 15 bold",bg="yellow").place(x=90,y=80)

#Input Box for user to enter the text.
Input_text = Entry(root,width=40)
Input_text.place(x=54,y=140)

#Label for Translated Text
Label(root, text="Translated Text: ",font="arial 13 bold", bg="yellow").place(x=630,y=80)

#Textbox to show output to user.
Output_text = Text(root,font="arial 10", height=11,wrap=WORD,padx=5, pady=5,width=50,bg="white smoke")
Output_text.place(x=515,y=120)

#Collecting list of languages.
language = list(LANGUAGES.values())

#Creating Style object to apply colors to Combobox
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "yellow", background= "orange")

#Creating combobox
dest_lang = ttk.Combobox(root,values=language,width=60)
dest_lang.place(x=260,y=360)
dest_lang.set("Choose Language")

#Method to translate the Given text by getting user selected Language.
def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    Output_text.delete(1.0,END)
    #Writing to output textbox
    Output_text.insert(END,translated.text)

#Adding button to translate
trans_button = Button(root,text='Translate',font="arial 20 bold",pady=5, command=Translate, bg="white smoke")
trans_button.place(x=400,y=400)

#Executing the page.
root.mainloop()