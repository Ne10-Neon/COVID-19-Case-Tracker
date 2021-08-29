# importing required modules for the tracker
import tkinter 
from tkinter import *
import requests
import webbrowser
############################################## FIRST PART OF THE TK FOR view
GUIWorkspace = Tk()
GUIWorkspace.geometry('1100x550')

GUIWorkspace.title("COVID-19 Case Tracker")
font_tuple = ("Helvetica", 20)
font_button_tuple = ("Helvetica", 12)
# functions for displaying the data
label_1 = Label(GUIWorkspace, font = font_tuple)
label_1.pack(pady=10)
label_countryData = Label(GUIWorkspace, font = font_tuple)
label_countryData.pack(pady=10)
############################################## FIRST PART OF THE TK FOR view
def getWorld_Data():
    pass
    covid_api = 'https://corona.lmao.ninja/v2/all?yesterday='
    covid_json = requests.get(covid_api).json()
    total = str(covid_json['cases'])
    totalDeaths = str(covid_json['deaths'])
    recovered = str(covid_json['recovered'])
    active = str(covid_json['active'])
    casesPer10to6 = str(covid_json['casesPerOneMillion'])
    countriesAffected = str(covid_json['affectedCountries'])
    label_1.config(text = "Total Number of COVID-19 cases = " +total+'\n'+"Total Number of deaths = " +totalDeaths+'\n'+
    'Total number of recoveries = '+recovered+'\n'+"Currently active cases of COVID-19 = "+active+'\n'+"Cases per a million = " 
    +casesPer10to6+'\n'+"Total number of countries affected by the COVID-19 Pandemic = "+countriesAffected)
    label_1.configure(foreground="blue")
getWorld_Data()


def countryData(countryN):
    #pass
    api = f'https://corona.lmao.ninja/v2/countries/{countryN}?yesterday&strict&query'
    json = requests.get(api).json()
    casesConf = str(json['cases'])
    country_fullName = str(json['country'])
    deathConf = str(json['deaths'])
    recoveredConf = str(json['recovered'])
    activeConf = str(json['active'])
    criticalConf = str(json['critical'])
    activeConf = str(json['active'])
    casesPer10to6 = str(json['casesPerOneMillion'])
    testsConf = str(json['tests'])
    label_countryData.config(text = f"Total Number of COVID-19 cases in {country_fullName} = " +casesConf+'\n'+f"Total Number of deaths in {country_fullName}= " +deathConf+'\n'+
    f"Total number of recoveries in {country_fullName} = "+recoveredConf+'\n'+f"Currently active cases of COVID-19 in {country_fullName} = "+activeConf+'\n'+f"Cases per a million in {country_fullName} = " 
    +casesPer10to6+'\n'+f"Critical cases in {country_fullName} = "+criticalConf+'\n'+f"Number of COVID-19 tests done in {country_fullName} = "+testsConf)


def search_by_country(event):
    #pass
    countryName = country_searchbox.get().upper()
    if countryName:
        try :
            countryData(countryName)
            print(f"{countryName} Information Generated.")
        except :
            print(f"{countryName} is not defined.")
            error_text.config(text=f"Error: {countryName} is not defined or not available.\nPlease double check your spelling.")
            error_text.configure(foreground="red")


# twitterButton = Button(GUIWorkspace, font = font_button_tuple, text = "My Twitter!", height=1, command = openTwitter)
# twitterButton.pack(side='bottom')
# ytButton = Button(GUIWorkspace, font = font_button_tuple, text = "My YouTube!", height=1, command = openYouTube)
# ytButton.pack(side='bottom')

############################################## SECOND PART OF THE TK FOR SEARCH
country_searchbox = Entry(GUIWorkspace, font = font_tuple, text = "Search by Country:", width = 20)
country_searchbox.pack()
search_button = Button(GUIWorkspace, font = font_tuple, width = 15, text = "Search", command = search_by_country)
search_button.pack()
error_text = Label(GUIWorkspace, font = font_tuple)
error_text.pack()
GUIWorkspace.bind('<Return>', search_by_country)
GUIWorkspace.mainloop()
############################################## SECOND PART OF THE TK FOR SEARCH






# functions to open the web browser when clicking the button

def openTwitter():
    webbrowser.open(urlTwt)

def openYouTube():
    webbrowser.open(urlYt)


# writing  ui code

urlTwt = 'https://twitter.com/Neon_DEVFN'
urlYt = 'https://www.youtube.com/channel/UCdqFdOJpMbyXGYnSAZdCX_Q'


# function to search individual country data

# COVID19-Tracker made with love and Python by Neon (a.k.a --> Neonツ, Neon__DEV, Ne10-Neon).s
