# importing required modules for the tracker
import tkinter as tk
import requests
import webbrowser

def getC_Data():

    #pass
    covid_api = 'https://corona.lmao.ninja/v2/all?yesterday='
    covid_json = requests.get(covid_api).json()
    total = str(covid_json['cases'])
    totalDeaths = str(covid_json['deaths'])
    recovered = str(covid_json['recovered'])
    active = str(covid_json['active'])
    casesPer10to6 = str(covid_json['casesPerOneMillion'])
    countriesAffected = str(covid_json['affectedCountries'])
    label_1.config(text = "Total Number of COVID-19 cases = " +total+'\n'+"Total Number of deaths = " +totalDeaths+'\n'+
    "Total number of recoveries = "+recovered+'\n'+"Currently active cases of COVID-19 = "+active+'\n'+"Cases per a million = " 
    +casesPer10to6+'\n'+"Total number of countries affected by the COVID-19 Pandemic = "+countriesAffected)
    label_1.configure(foreground="red")


    #print(f'Total COVID-19 cases = {total}')
    #print(f'Total number of deaths = {totalDeaths}')
    #print(f'Total number of recoveries = {recovered}')
    #print(f'Currently active cases of COVID-19 = {active}')
    #print(f'Total cases per a million = {casesPer10to6}')
    #print(f'Number of countries affected with the COVID-19 Pandemic = {countriesAffected}')

    
def openTwitter():
    webbrowser.open(url)

def openYT():
    webbrowser.open(urlYt)


# making socials gui code
twitter = 1
url = 'https://twitter.com/Ne0nDEV'
youtube = 1
urlYt = 'https://www.youtube.com/channel/UCdqFdOJpMbyXGYnSAZdCX_Q'


# making tkinter gui code
GUIWorkspace = tk.Tk()
GUIWorkspace.geometry('1100x550')
GUIWorkspace.title("COVID-19 Case Tracker")
font_tuple = ("courier", 20, "bold")


guibutton = tk.Button(GUIWorkspace, font = font_tuple, text = "Re-Load All Data", command = getC_Data, foreground="orange")
guibutton.pack(pady=50)

# supportLabel = tk.Label(GUIWorkspace, font = font_tuple, text = "Support me:")
# supportLabel.pack(pady=15)
twitterButton = tk.Button(GUIWorkspace, font = font_tuple, text = "My Twitter Page!", command = openTwitter)
twitterButton.pack(side='bottom',padx=50,pady=5)
ytButton = tk.Button(GUIWorkspace, font = font_tuple, text = "My YouTube Channel!", command = openYT)
ytButton.pack(side='bottom',padx=50,pady=5)

# COVIDimage = tk.PhotoImage('covid19_logo.png')

label_1 = tk.Label(GUIWorkspace, font = font_tuple)
label_1.pack(pady=10)
# label_2 = tk.Label(GUIWorkspace, font = font_tuple, text = "COVID-19 Tracker made with love by Neon.\n If you liked my work, \nclick on my Twitter and Youtube account buttons\n and drop me a sub and a follow! \nThank you!")
# label_2.pack(pady=30)

getC_Data()

GUIWorkspace.mainloop()

# COVID19-Tracker made with love (actually made with Python but yeah lol) by Neon (a.k.a --> Neonツ, Ne0nDEV, Ne10-Neon).