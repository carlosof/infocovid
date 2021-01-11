# Programado por Carlosof96

import tkinter as tk
from covid import Covid
from tkinter import *
from datetime import datetime as dt
from tkinter.ttk import Combobox

#  Definición de la función CreateWidgets () para crear los widgets tkinter necesarios

def CreateWidgets():
    worldwideActiveLabel = Label(root, text="Casos activos en el mundo : ", bg="thistle4")
    worldwideActiveLabel.grid(row=0, column=0, padx=10, pady=5)
    worldwideActiveEntry = Label(root, width=20, bg='snow3')
    worldwideActiveEntry.grid(row=0, column=1, padx=10, pady=5)

    worldwideConfirmedLabel = Label(root, text="Casos confirmados en el mundo : ", bg="thistle4")
    worldwideConfirmedLabel.grid(row=1, column=0, padx=10, pady=5)
    worldwideConfirmedEntry = Label(root, width=20, bg='snow3')
    worldwideConfirmedEntry.grid(row=1, column=1, padx=10, pady=5)

    worldwideRecoveredLabel = Label(root, text="Total de recuperados en el mundo : ", bg="thistle4")
    worldwideRecoveredLabel.grid(row=2, column=0, padx=10, pady=5)
    worldwideRecoveredEntry = Label(root, width=20, bg='snow3')
    worldwideRecoveredEntry.grid(row=2, column=1, padx=10, pady=5)

    worldwideDeathsLabel = Label(root, text="Muertes totales en el mundo : ", bg="thistle4")
    worldwideDeathsLabel.grid(row=3, column=0, padx=10, pady=5)
    worldwideDeathsEntry = Label(root, width=20, bg='snow3')
    worldwideDeathsEntry.grid(row=3, column=1, padx=10, pady=5)

    worldwide_total_active_cases = Covid().get_total_active_cases()
    worldwide_total_confirmed_cases = Covid().get_total_confirmed_cases()
    worldwide_total_recovered = Covid().get_total_recovered()
    worldwide_total_deaths = Covid().get_total_deaths()

    worldwideActiveEntry.config(text=str(worldwide_total_active_cases))
    worldwideConfirmedEntry.config(text=str(worldwide_total_confirmed_cases))
    worldwideRecoveredEntry.config(text=str(worldwide_total_recovered))
    worldwideDeathsEntry.config(text=str(worldwide_total_deaths))

    countryLabel = Label(root, text="Nombre del pais : ", bg="thistle4")
    countryLabel.grid(row=4, column=0, padx=10, pady=5)

    countryName = []

    # Obtenemos y almacenamos la lista de países usando list_countries () de Covid Library

    countriesList = Covid().list_countries()
    for c in range(len(countriesList)):
        countryName.append(countriesList[c]['name'])
    # Mostramos la lista de paises
    root.countriesComboBox = Combobox(root, width=18, values=countryName, state="readonly")
    root.countriesComboBox.grid(row=4, column=1, padx=5, pady=2)

    findButton = Button(root, text="Buscar por pais", command=findDetails)
    findButton.grid(row=5, column=1, padx=5, pady=5, columnspan=2)

    activeCasesLabel = Label(root, text="Total de casos activos :       ", bg="thistle4")
    activeCasesLabel.grid(row=6, column=0, padx=10, pady=5)
    root.activeCases = Label(root, width=20, bg='snow3')
    root.activeCases.grid(row=6, column=1, padx=10, pady=5)

    confirmedCasesLabel = Label(root, text="Total de casos confirmados :    ", bg="thistle4")
    confirmedCasesLabel.grid(row=7, column=0, padx=10, pady=5)
    root.confirmedCases = Label(root, width=20, bg='snow3')
    root.confirmedCases.grid(row=7, column=1, padx=10, pady=5)

    recoveredCasesLabel = Label(root, text="Total de recuperados :    ", bg="thistle4")
    recoveredCasesLabel.grid(row=8, column=0, padx=10, pady=5)
    root.recoveredCases = Label(root, width=20, bg='snow3')
    root.recoveredCases.grid(row=8, column=1, padx=10, pady=5)

    deathsLabel = Label(root, text="Total de muertes confirmadas :       ", bg="thistle4")
    deathsLabel.grid(row=9, column=0, padx=10, pady=5)
    root.deaths = Label(root, width=20, bg='snow3')
    root.deaths.grid(row=9, column=1, padx=10, pady=5)

    updatedLabel = Label(root, text="Ultima actualización base de datos :    ", bg="thistle4")
    updatedLabel.grid(row=10, column=0, padx=10, pady=5)
    root.updated = Label(root, width=20, bg='snow3')
    root.updated.grid(row=10, column=1, padx=10, pady=5)

# Definicimos la función findDetails () para encontrar los detalles de covid del pais

def findDetails():
    country = root.countriesComboBox.get()
    # Buscamos la informacion especifica de ese pais
    specific_country_covid_info = Covid().get_status_by_country_name(country)

    country_total_active_cases = specific_country_covid_info['active']
    country_total_confirmed_cases = specific_country_covid_info['confirmed']
    country_total_recovered = specific_country_covid_info['recovered']
    country_total_deaths = specific_country_covid_info['deaths']
    updated_time_epoch = specific_country_covid_info['last_update']
    data_updated_at = dt.fromtimestamp(updated_time_epoch/1000).strftime("%d-%m-%Y %H:%M:%S")

    root.activeCases.config(text=str(country_total_active_cases))
    root.confirmedCases.config(text=str(country_total_confirmed_cases))
    root.recoveredCases.config(text=str(country_total_recovered))
    root.deaths.config(text=str(country_total_deaths))
    root.updated.config(text=str(data_updated_at))

root = tk.Tk()

# Ajustes estéticos

root.title("Contador de covid Creado por Carlosof")
root.config(background="thistle4")
root.geometry("470x390")
root.resizable(False, False)
#  CreateWidgets() function
CreateWidgets()
# Definición del bucle
root.mainloop()