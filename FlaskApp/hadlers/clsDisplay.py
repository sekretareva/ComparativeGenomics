import pandas as pd
import os
import re

def displayClassification(data):
    ranks = ['Category', 'System']

    #загрузка и соединение категорезированных функций
    ctg = data.getRastCls()

    hierarchy = {}
    categories = []
    systemsInCategory = []

    for categoryN, categoryName in enumerate(ctg.sort_values(ranks[0])[ranks[0]].unique()):
        systems = []
        for systemN, systemName in enumerate(ctg.loc[ctg[ranks[0]]==categoryName].sort_values(ranks[1])[ranks[1]].unique()):
            systems.append(systemName)
        systemsInCategory.append(systems)
        hierarchy[categoryName] = systems
    return hierarchy
