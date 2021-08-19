# importing required modules for the tracker
from tkinter import *
import requests
import webbrowser

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


def countryDataUSA():
    #pass
    apiUSA = 'https://corona.lmao.ninja/v2/countries/USA?yesterday&strict&query'
    jsonUSA = requests.get(apiUSA).json()
    casesConf = str(jsonUSA['cases'])
    deathConf = str(jsonUSA['deaths'])
    recoveredConf = str(jsonUSA['recovered'])
    activeConf = str(jsonUSA['active'])
    criticalConf = str(jsonUSA['critical'])
    activeConf = str(jsonUSA['active'])
    casesPer10to6 = str(jsonUSA['casesPerOneMillion'])
    testsConf = str(jsonUSA['tests'])
    label_countryData.config(text = "Total Number of COVID-19 cases in USA = " +casesConf+'\n'+"Total Number of deaths in USA= " +deathConf+'\n'+
    "Total number of recoveries in USA = "+recoveredConf+'\n'+"Currently active cases of COVID-19 in USA = "+activeConf+'\n'+"Cases per a million in USA = " 
    +casesPer10to6+'\n'+"Critical cases in USA = "+criticalConf+'\n'+"Number of COVID-19 tests done in USA = "+testsConf)

def countryDataIND():
    #pass
    apiIND = 'https://corona.lmao.ninja/v2/countries/India?yesterday&strict&query'
    jsonIND = requests.get(apiIND).json()
    casesConf = str(jsonIND['cases'])
    deathConf = str(jsonIND['deaths'])
    recoveredConf = str(jsonIND['recovered'])
    activeConf = str(jsonIND['active'])
    criticalConf = str(jsonIND['critical'])
    activeConf = str(jsonIND['active'])
    casesPer10to6 = str(jsonIND['casesPerOneMillion'])
    testsConf = str(jsonIND['tests'])
    label_countryData.config(text = "Total Number of COVID-19 cases in India = " +casesConf+'\n'+"Total Number of deaths in India = " +deathConf+'\n'+
    "Total number of recoveries in India = "+recoveredConf+'\n'+"Currently active cases of COVID-19 in India = "+activeConf+'\n'+"Cases per a million in India = " 
    +casesPer10to6+'\n'+"Critical cases in India = "+criticalConf+'\n'+"Number of COVID-19 tests done in India = "+testsConf)

def countryDataRUS():
    #pass
    apiRUS = 'https://corona.lmao.ninja/v2/countries/Russia?yesterday&strict&query'
    jsonRUS = requests.get(apiRUS).json()
    casesConf = str(jsonRUS['cases'])
    deathConf = str(jsonRUS['deaths'])
    recoveredConf = str(jsonRUS['recovered'])
    activeConf = str(jsonRUS['active'])
    criticalConf = str(jsonRUS['critical'])
    activeConf = str(jsonRUS['active'])
    casesPer10to6 = str(jsonRUS['casesPerOneMillion'])
    testsConf = str(jsonRUS['tests'])
    label_countryData.config(text = "Total Number of COVID-19 cases in Russia = " +casesConf+'\n'+"Total Number of deaths in Russia = " +deathConf+'\n'+
    "Total number of recoveries in Russia = "+recoveredConf+'\n'+"Currently active cases of COVID-19 in Russia = "+activeConf+'\n'+"Cases per a million in Russia = " 
    +casesPer10to6+'\n'+"Critical cases in Russia = "+criticalConf+'\n'+"Number of COVID-19 tests done in Russia = "+testsConf)    

def countryDataITA():
    #pass
    apiITA = 'https://corona.lmao.ninja/v2/countries/Italy?yesterday&strict&query'
    jsonITA = requests.get(apiITA).json()
    casesConf = str(jsonITA['cases'])
    deathConf = str(jsonITA['deaths'])
    recoveredConf = str(jsonITA['recovered'])
    activeConf = str(jsonITA['active'])
    criticalConf = str(jsonITA['critical'])
    activeConf = str(jsonITA['active'])
    casesPer10to6 = str(jsonITA['casesPerOneMillion'])
    testsConf = str(jsonITA['tests'])
    label_countryData.config(text = "Total Number of COVID-19 cases in Italy = " +casesConf+'\n'+"Total Number of deaths in Italy = " +deathConf+'\n'+
    "Total number of recoveries in Italy = "+recoveredConf+'\n'+"Currently active cases of COVID-19 in Italy = "+activeConf+'\n'+"Cases per a million in Italy = " 
    +casesPer10to6+'\n'+"Critical cases in Italy = "+criticalConf+'\n'+"Number of COVID-19 tests done in Italy = "+testsConf) 

def countryDataFRA():
    #pass
    apiFRA = 'https://corona.lmao.ninja/v2/countries/France?yesterday&strict&query'
    jsonFRA = requests.get(apiFRA).json()
    casesConf = str(jsonFRA['cases'])
    deathConf = str(jsonFRA['deaths'])
    recoveredConf = str(jsonFRA['recovered'])
    activeConf = str(jsonFRA['active'])
    criticalConf = str(jsonFRA['critical'])
    activeConf = str(jsonFRA['active'])
    casesPer10to6 = str(jsonFRA['casesPerOneMillion'])
    testsConf = str(jsonFRA['tests'])
    label_countryData.config(text = "Total Number of COVID-19 cases in France = " +casesConf+'\n'+"Total Number of deaths in France = " +deathConf+'\n'+
    "Total number of recoveries in France = "+recoveredConf+'\n'+"Currently active cases of COVID-19 in France = "+activeConf+'\n'+"Cases per a million in France = " 
    +casesPer10to6+'\n'+"Critical cases in France = "+criticalConf+'\n'+"Number of COVID-19 tests done in France = "+testsConf)    

def countryDataGER():
    #pass
    apiGER = 'https://corona.lmao.ninja/v2/countries/Germany?yesterday&strict&query'
    jsonGER = requests.get(apiGER).json()
    casesConf = str(jsonGER['cases'])
    deathConf = str(jsonGER['deaths'])
    recoveredConf = str(jsonGER['recovered'])
    activeConf = str(jsonGER['active'])
    criticalConf = str(jsonGER['critical'])
    activeConf = str(jsonGER['active'])
    casesPer10to6 = str(jsonGER['casesPerOneMillion'])
    testsConf = str(jsonGER['tests'])
    label_countryData.config(text = "Total Number of COVID-19 cases in Germany = " +casesConf+'\n'+"Total Number of deaths in Germany = " +deathConf+'\n'+
    "Total number of recoveries in Germany = "+recoveredConf+'\n'+"Currently active cases of COVID-19 in Germany = "+activeConf+'\n'+"Cases per a million in Germany = " 
    +casesPer10to6+'\n'+"Critical cases in Germany = "+criticalConf+'\n'+"Number of COVID-19 tests done in Germany = "+testsConf)    

def countryDataCAN():
    #pass
    apiCAN = 'https://corona.lmao.ninja/v2/countries/Canada?yesterday&strict&query'
    jsonCAN = requests.get(apiCAN).json()
    casesConf = str(jsonCAN['cases'])
    deathConf = str(jsonCAN['deaths'])
    recoveredConf = str(jsonCAN['recovered'])
    activeConf = str(jsonCAN['active'])
    criticalConf = str(jsonCAN['critical'])
    activeConf = str(jsonCAN['active'])
    casesPer10to6 = str(jsonCAN['casesPerOneMillion'])
    testsConf = str(jsonCAN['tests'])
    label_countryData.config(text = "Total Number of COVID-19 cases in Canada = " +casesConf+'\n'+"Total Number of deaths in Canada = " +deathConf+'\n'+
    "Total number of recoveries in Canada = "+recoveredConf+'\n'+"Currently active cases of COVID-19 in Canada = "+activeConf+'\n'+"Cases per a million in Canada = " 
    +casesPer10to6+'\n'+"Critical cases in Canada = "+criticalConf+'\n'+"Number of COVID-19 tests done in Canada = "+testsConf)    




# functions to open the web browser when clicking the button
def openTwitter():
    webbrowser.open(urlTwt)

def openYouTube():
    webbrowser.open(urlYt)


# writing  ui code
twitter = "URL below"
urlTwt = 'https://twitter.com/Neon_DEVFN'
youtube = "URL below"
urlYt = 'https://www.youtube.com/channel/UCdqFdOJpMbyXGYnSAZdCX_Q'


def search_by_country():
    #pass
    countryName = country_searchbox.get()
    if countryName == "USA":
        countryDataUSA()
    elif countryName == "India":
        countryDataIND()
    elif countryName == "Russia":
        countryDataRUS()
    elif countryName == "Italy":
        countryDataITA()
    elif countryName == "France":
        countryDataFRA()  
    elif countryName == "Germany":
        countryDataGER()
    elif countryName == "Canada":
        countryDataCAN()
    else: 
        error_text.config(text = "Error: Country is not defined or not available.\nPlease double check your spelling.")
        error_text.configure(foreground="red")



# icon for the app
iconImage = PhotoImage(file = 'icon.png')


# writing tkinter ui code
GUIWorkspace = Tk()
GUIWorkspace.geometry('1100x550')
GUIWorkspace.title("COVID-19 Case Tracker")
GUIWorkspace.iconphoto(True, iconImage)
font_tuple = ("calibri", 20)


# twitterButton = Button(GUIWorkspace, font = font_tuple, text = "My Twitter!", height=1, command = openTwitter)
# twitterButton.pack(side='left', side='bottom')
# ytButton = Button(GUIWorkspace, font = font_tuple, text = "My YouTube!", height=1, command = openYouTube)
# ytButton.pack(side='left', side='bottom')

label_1 = Label(GUIWorkspace, font = font_tuple)
label_1.pack(pady=10)
label_countryData = Label(GUIWorkspace, font = font_tuple)
label_countryData.pack(pady=10)
country_searchbox = Entry(GUIWorkspace, font = font_tuple, text = "Search by Country:", width = 20)
country_searchbox.pack()
search_button = Button(GUIWorkspace, font = font_tuple, width = 15, text = "Search", command = search_by_country)
search_button.pack()
error_text = Label(GUIWorkspace, font = font_tuple)
error_text.pack()


getWorld_Data()

GUIWorkspace.mainloop()

# COVID19-Tracker made with love (actually made with Python but yeah lol) by Neon (a.k.a --> Neonツ, Neon_DEVFN, Ne10-Neon).