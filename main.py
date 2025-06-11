import customtkinter as ctk #importing customtkinter library, which gives us a modern look for the GUI (Graphical User Interface)

class App(ctk.CTk): #defining the main application as class App, which inherits from ctk.CTk
#this section will keep all window-related code and properties (like size of the window, title, etc.)
    def __init__(self):
        super().__init__()

        #configure the window
        self.title("My Period Tracker") #setting the title of the window
        self.geometry("600x500") #setting the size of the window
        self.minsize("400x300") #setting the minimum size of the window
        ctk.set_appearance_mode("System") #setting the appearance mode of the window

       

        #adding a button to the window
        self.button = ctk.CTkButton(self, text="Add Period")
        self.button.pack(pady=20)

if __name__ == "__main__": #this is the main entry point of the application
        #creating an instance of the App class (this creates the window)
        app = App()

        app.mainloop() #this is the main loop of the application, which keeps the window running