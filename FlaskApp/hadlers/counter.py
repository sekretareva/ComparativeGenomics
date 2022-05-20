import pandas as pd

def countFunctions(data, categories, systems):
    ranks = ['Category', 'System']
    files =  data.getClassified()
    count = pd.DataFrame([], columns=categories+systems)
    
    count.insert(0, 'Strain', [filename for filename in files])
    count.loc[:, 1:] = 0

    for filename in files:
        file = files[filename]
        index = count.loc[count['Strain']==filename].index

        for count_s in count.columns:
            if count_s != count.columns[0]:
                if count_s in categories:
                    param = ranks[0]
                else:
                    param = ranks[1]

                count_s = count_s.replace("?", " ")
                count.loc[(index, count_s)] = len(file[file[param].str.contains(count_s)].index.values)
                                     
    return count.sort_values('Strain', ascending=True)