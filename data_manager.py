#this file will handle the data storage and retrieval
import json #importing Python's built-in library to work with JSON files

DATA_FILE = "period_data.json" #defining the name of the file on your desktop which will store all your period data 
#this is a constant variable - it is defined outside of any classes, so in case you need to change the name of the file, you can do it only once - here!


def save_data(data):
#this function takes the period data that you introduce to the app and saves it in the file that holds your data
    try:
        with open(DATA_FILE, "w") as f: #trying to open the file in 'w'(write) mode, which will allow us to put content inside
        #this also automatically closes the file after the process, even if an error occurs
            json.dump(data, f, indent=4) #this function writes the data into the file in JSON format
    except IOError as e: #if the file can't be written for any reason (such as permission issue), we print an error message
        print("There was an error saving your data: {e}")


def load_data():
#this function loads data from the JSON file so that we can see it in the app. If the file doesn't exist, it returns a default data structure.
#it returns the loaded data from the file or default dictionary

    try:
        with open(DATA_FILE, "r") as f: #trying to open the file in "r" (read) mode, which will allow us to see the data from the file
            data = json.load(f)
            return data
    except FileNotFoundError: #if the file does not exist (such as during the very first time the app is used), we are returning a clean, default structure. This prevent the app from crashing.
        print("Data file not found. Creating a new one.")
        return {"your period starts in []"}
    except json.JSONDecodeError:
        #handling the case where the file is empty or corrupted. We return a default structure to prevent a crash.
        print("Error decoding JSON from the data file. Starting fresh")
        return {"your period starts in []"}
    except IOError as e:
        #handling other potential file reading errors
        print(f"Error loading data: {e}")
        return {"your period starts in []"}