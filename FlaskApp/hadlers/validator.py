import pandas as pd

def template(allowed_file_types, data, columns, error):
    content = pd.DataFrame()
    file_type = data.filename.split('.')[-1]
    if file_type in allowed_file_types:
        if file_type =='tsv':
            content = pd.read_csv(data, sep='\t')
        else:
            content = pd.read_csv(data)
        if set(columns).issubset(content.columns):
            error = ''
        else:
            content = pd.DataFrame()
    return error, content

def validate(data, type):

    if type == "userCls":
        allowed_file_types = ['csv']
        comumns = ['Function','Subsystem', 'System', 'Category']
        error = 'Неверный формат пользовательской классификации'

    if type == "rastDownload":
        allowed_file_types = ['csv', 'tsv']
        comumns = ['Function','Subsystem']
        error = 'Неверный формат выгрузок из RAST'

    if type == "breakdown":
        allowed_file_types = ['csv']
        comumns = ['Strain','Breakdown Type']
        error = 'Неверный формат разбивки данных'

    return template(allowed_file_types, data, comumns, error) 

