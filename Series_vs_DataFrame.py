# -*- coding: utf-8 -*-
__author__ = 'Eduard'
__author__ = 'Merrick'
__author__ = 'Ed'#Hello ED
__author__='Nadia'
__author__='Timothée' #Name of last author

import pandas as pd

# Series: Is a unidimensional array with indexation. Similar to dictionary
spanishPlayers = pd.Series(
    ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez', 'Pedrito',
     'Iniesta', 'Villa', 'Raul'], index=[1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7, 7])
print("Spanish Football Players: \n%s" % spanishPlayers)
print('\n==================================================================\n')


# series through dictionary
dictPlayers = {1: 'Casillas', 15: 'Ramos', 3: 'Pique', 5: 'Puyol', 11: 'Capdevila', 14: 'Xabi Alonso',
               16: 'Busquets', 8: 'Xavi Hernandez', 18: 'Pedrito', 6: 'Iniesta', 7: 'Villa', 7: 'Raul'}
players2series = pd.Series(dictPlayers)
# Insert new player
players2series[10] = 'Cesc'
print("Spanish Football Players through dictionary: \n%s" % players2series)
print('\n==================================================================\n')


# DataFrame: data structure similar to excel or SQL table
spanishPlayersDF = pd.DataFrame(
    {
        'name': ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez',
                 'Pedrito', 'Iniesta', 'Villa', 'Raul'],
        'demarcation': ['Goalkeeper', 'Right back', 'Centre-back', 'Centre-back', 'Left back', 'Defensive midfield',
                        'Defensive midfield', 'Midfielder', 'Left winger', 'Right winger', 'Centre forward', 'Centre forward'],
        'team': ['Real Madrid', 'Real Madrid', 'FC Barcelona', 'FC Barcelona', 'Villareal', 'Real Madrid',
                 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'Real Madrid']
    }, columns=['name', 'demarcation', 'team'], index=[1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7, 7]
)
# Insert new player
spanishPlayersDF.loc[10] = ['Cesc', 'Forward', 'Arsenal']
print("Spanish Football Players DataFrame: \n%s" % spanishPlayersDF)
