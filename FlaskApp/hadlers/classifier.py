import pandas as pd
from hadlers.keywordsClassifier import keywordsClassify
from hadlers.validator import validate

def rastClassify(data, table_to, table_to_index):
    rastCls = data.getRastCls()

    if table_to.iloc[table_to_index]['Subsystem'] != '- none -':  
        if match('Subsystem', rastCls, table_to, table_to_index) > 0:
            return True
        else:
            return False

def userClassify(data, table_to, table_to_index):
    if match('Function', data.getUserCls(), table_to, table_to_index) > 0:
        return True
    else:
        return False

def kwClassify(data, table_to, table_to_index):
    for value in table_to.iloc[table_to_index]['Function'].split('; <br>'):
        keywordsClassify(value, data)
        match('Function', data.getKwCls(), table_to, table_to_index)

def match(match_type, table_from, table_to, table_to_index):
    matchCount = 0
    for value in table_to.iloc[table_to_index][match_type].split('; <br>'):
        table_from_indexes = table_from[table_from[match_type] == value.strip()].index.values
        if len(table_from_indexes) > 0:
            for table_from_index in table_from_indexes:
                addRank('Category', table_to, table_from, table_to_index, table_from_index)
                addRank('System', table_to, table_from, table_to_index, table_from_index)
                matchCount += 1
                if match_type == 'Function':
                    addRank('Subsystem', table_to, table_from, table_to_index, table_from_index)
    return matchCount

def addRank(column, t_to, t_from, raw_to, raw_from):
    if  'none' in t_to.iloc[raw_to][column]:
        t_to.loc[(raw_to,column)] = t_from.iloc[raw_from][column].strip()
    else:
        if t_to.iloc[raw_to][column]:
            column_array = t_to.iloc[raw_to][column].split(';')
            column_array = [j.strip() for j in column_array]
            if t_from.iloc[raw_from][column].strip() not in column_array:
                column_array.append(t_from.iloc[raw_from][column].strip())
                t_to.loc[(raw_to,column)] = '; '.join(sorted(column_array))

def classifyFunctions(cls_types, files, data):
    resultsList = data.getClassified()
    displayError = ''

    for file in files:
        error, fileContent = validate(file, "rastDownload")
        if len(error) > 0:
            displayError = error
            continue
        if not set(['System', 'Category']).issubset(fileContent.columns):
            fileContent.loc[:, "System"] = 'none'
            fileContent.loc[:, "Category"] = 'none'

        for index, row in fileContent.iterrows():
            classified = False
            if "0" in cls_types:
                classified = rastClassify(data, fileContent, index)

            if "1" in cls_types and not classified:
                if not data.userCls.empty:
                    classified = userClassify(data, fileContent, index)

            if "2" in cls_types and not classified:
                kwClassify(data, fileContent, index)

        
    
        fileContent.drop(fileContent.columns.difference(['Category', 'System', 'Subsystem', 'Function']), 1, inplace=True)
        filename = '.'.join(file.filename.split('.')[:-1])
        resultsList[filename] = fileContent

    return displayError, resultsList
