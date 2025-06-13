import customtkinter as ctk #importing customtkinter library, which gives us a modern look for the GUI (Graphical User Interface)
from tkcalendar import Calendar
from datetime import date

class App(ctk.CTk): #defining the main application as class App, which inherits from ctk.CTk
#this section will keep all window-related code and properties (like size of the window, title, etc.)
    def __init__(self):
        super().__init__()

        #configure the window
        self.title("My Period Tracker") #setting the title of the window
        self.geometry("600x500") #setting the size of the window
        self.minsize(400, 300) #setting the minimum size of the window (should be integers, not strings)
        ctk.set_appearance_mode("System") #setting the appearance mode of the window


        #--- UI WIDGETS --- (creating the view and functionalities of the main window of the app)
        self.prediction_label = ctk.CTkLabel(
             self, text= "Your next period starts in ... days",
             font=ctk.CTkFont(size=20, weight="bold")
        ) #creating a label which tells you how many days you have left until your period

        self.prediction_label.pack(pady=20, padx=20) #.pack places widgets on the window; I'm also determining the spacing of it with padding

        today = date.today() #getting today's date to initialize the calendar properly
        self.calendar = Calendar(
            self, selectmode='day', year=today.year, month=today.month, day=today.day,
            #styling for better look and feel
            background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1],
            foreground='white',
            headersbackground=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1],
            normalbackground=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0],
            weekendbackground=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0],
            othermonthforeground='gray50',
            othermonthbackground=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0],
            othermonthweforeground='gray50',
            othermonthwebackground=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0],
            selectbackground=ctk.ThemeManager.theme["CTkButton"]["fg_color"][1],
            bordercolor=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1]
        )
        self.calendar.pack(pady=19, padx=20, fill="both", expand=True)
        #"add period start" button
        self.add_period_button = ctk.CTkButton(self, text="Add Period",
        #command is a function that will run the button when it is clicked
        command=lambda: print("Add Period Start button clicked") #TODO: change the placeholder
        )
        self.add_period_button.pack(pady=10)

        #---frame for entering symptoms---
        self.symptom_frame = ctk.CTkFrame(self)
        self.symptom_frame.pack(pady=10, padx=20, fill="x")

        self.symptom_entry = ctk.CTkEntry(
             self.symptom_frame,
             placeholder_text="Enter symptoms for selected date"
        )
        self.symptom_entry.pack(
             side="left", fill="x", expand=True
        ) #fill="x" makes it expand horizontally, expand=True makes it take up available space

        self.save_symptom_button = ctk.CTkButton(
             self.symptom_frame,
             text="Save Symptom",
             command=lambda: print("Save Symptom button clicked") #TODO: change placeholder to action
        ) #creating the save symptom button
        self.save_symptom_button.pack(side="left")

if __name__ == "__main__": #this is the main entry point of the application
        #creating an instance of the App class (this creates the window)
        app = App()

        app.mainloop() #this is the main loop of the application, which keeps the window running