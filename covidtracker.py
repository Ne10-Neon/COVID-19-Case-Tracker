# importing required modules for the tracker

from tkinter import *
import requests
import webbrowser
import sys

# functions for displaying the data

def World_Data():
    # pass
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
    label_1.configure(foreground="blue", bg="white")

def countryData(cName):
    # pass
    api = f'https://corona.lmao.ninja/v2/countries/{cName}?yesterday&strict&query'
    json = requests.get(api).json()
    country_Name = str(json['country'])
    casesConf = str(json['cases'])
    deathConf = str(json['deaths'])
    recoveredConf = str(json['recovered'])
    criticalConf = str(json['critical'])
    activeConf = str(json['active'])
    casesPer10to6 = str(json['casesPerOneMillion'])
    testsConf = str(json['tests'])
    data_label.config(text = f"Total Number of COVID-19 cases in {country_Name} = " +casesConf+'\n'+f"Total Number of deaths in {country_Name}= " +deathConf+'\n'+
    f"Total number of recoveries in {country_Name} = "+recoveredConf+'\n'+f"Currently active cases of COVID-19 in {country_Name} = "+activeConf+'\n'+f"Cases per a million in {country_Name} = "
    +casesPer10to6+'\n'+f"Critical cases in {country_Name} = "+criticalConf+'\n'+f"Number of COVID-19 tests done in {country_Name} = "+testsConf)



# functions to open the web browser when clicking the button


urlTwt = 'https://twitter.com/NotNeon_DEV'
urlYt = 'https://www.youtube.com/channel/UCdqFdOJpMbyXGYnSAZdCX_Q'
urlGit = 'https://github.com/NotNeonDEV'


def openTwitter():
    webbrowser.open(urlTwt)


def openYouTube():
    webbrowser.open(urlYt)


def openGitHub():
    webbrowser.open(urlGit)


# function for dark mode/light mode theme

def dark():
    GUIWorkspace.configure(bg="black")
    label_1.configure(bg="black")
    searchbox.configure(bg="black")
    searchbox.configure(foreground="white")
    ytButton.configure(bg="black")
    githubButton.configure(bg="black")
    twitterButton.configure(bg="black")
    data_label.configure(bg="black")
    data_label.configure(foreground="white")
    error_text.configure(bg="black")
    print('Changed to dark mode.')


def light():
    GUIWorkspace.configure(bg="white")
    label_1.configure(bg="white")
    searchbox.configure(bg="white")
    searchbox.configure(foreground="black")
    ytButton.configure(bg="white")
    githubButton.configure(bg="white")
    twitterButton.configure(bg="white")
    data_label.configure(bg="white")
    data_label.configure(foreground="black")
    error_text.configure(bg="white")
    print('Changed to light mode.')


def exit_app():
    sys.exit()


def about_window():
    window = Toplevel(master=GUIWorkspace)
    window.title("About this App")
    window.geometry('950x400')

    about_label = Label(window, font=font_tuple, text="This software is created and owned by Neon (NotNeonDEV, @NotNeon_DEV, Neonツ)\nunder the GitHub MIT license. \n\nTo know more about the license info on this app, visit our github page.")
    about_label.pack()


# function to bind click to search_box

def search_click(event):
    searchbox.config(state=NORMAL)
    searchbox.delete(0, END)


# function to search individual country data

def search_by_country(event):
    # pass
    countryName = searchbox.get()
    if countryName:
        try:
            countryData(countryName)
            error_text.config(text="")
            print(f"Data Generated for {countryName}")
        except:
            print(f"{countryName} is not defined.")
            error_text.config(text=f"Error: {countryName} is not defined or un-available.\nPlease double check your spelling.")
            error_text.configure(foreground='red')


# writing tkinter ui code

GUIWorkspace = Tk()
GUIWorkspace.geometry('1100x550')
GUIWorkspace.title("COVID-19 Case Tracker")
GUIWorkspace.configure(bg="white")
font_tuple = ("calibri", 20)
menu = Menu(GUIWorkspace, font=font_tuple)

twticon = PhotoImage(file='twittericon.png')
yticon = PhotoImage(file='youtubeicon.png')
giticon = PhotoImage(file='githubicon.png')
icon = PhotoImage(file='icon_app.png')

GUIWorkspace.iconphoto(False, icon)

twitterButton = Button(GUIWorkspace, image = twticon, border = 0, command = openTwitter)
twitterButton.configure(bg="white")
twitterButton.place(x=30, y=30)

ytButton = Button(GUIWorkspace, image = yticon, border = 0, command = openYouTube)
ytButton.configure(bg="white")
ytButton.place(x=30, y=110)

githubButton = Button(GUIWorkspace, image = giticon, border = 0, command = openGitHub)
githubButton.configure(bg="white")
githubButton.place(x=30, y=190)

label_1 = Label(GUIWorkspace, font = font_tuple)
label_1.pack(pady=10)

data_label = Label(GUIWorkspace, font = font_tuple)
data_label.configure(bg="white")
data_label.pack(pady=10)

searchbox = Entry(GUIWorkspace, font = font_tuple, width = 20)
searchbox.insert(0, "Search a country here...")
searchbox.configure(bg="white")
searchbox.config(state=DISABLED)
searchbox.bind('<Button-1>', search_click)
searchbox.pack()

# search_button = Button(GUIWorkspace, font = font_tuple, height = 1, width = 15, text = "Search", command = search_by_country)
# search_button.pack()

error_text = Label(GUIWorkspace, font = font_tuple)
error_text.configure(bg="white")
error_text.pack()

Theme = Menu(menu, tearoff = 0)
menu.add_cascade(label="Display Settings", menu=Theme)
Theme.add_command(label="Dark Mode", command=dark)
Theme.add_command(label="Light Mode", command=light)

Settings = Menu(menu, tearoff = 0)
menu.add_cascade(label="Settings", menu=Settings)
Settings.add_command(label="Exit App", command=exit_app)
Settings.add_command(label="About The App", command=about_window)


GUIWorkspace.bind('<Return>', search_by_country)
GUIWorkspace.config(menu=menu)


World_Data()

GUIWorkspace.mainloop()


# COVID19-Tracker made with love and Python by Neon (a.k.a --> Neonツ, NotNeon_DEV, NotNeonDEV).
