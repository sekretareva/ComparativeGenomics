from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, AffinityPropagation
from sklearn.decomposition import PCA
from sklearn.manifold import MDS, TSNE
import pandas as pd
import plotly
import plotly.express as px
import json

def match(table_to, table_from):
    for rowIndex, row in table_to.iterrows():
        strain = row['Strain']
        table_from_indexes = table_from[table_from['Strain'] == strain].index.values
        if (len(table_from_indexes)) > 0:
            table_to.loc[(rowIndex,'Breakdown Type')] = table_from.iloc[table_from_indexes[0]]['Breakdown Type'].strip()

def buildScatter(data, components, strains, predictions):
    components.insert(0, 'Strain', strains)
    components.loc[:, 'Breakdown Type'] = 'unknown'
    components.loc[:, 'Cluster'] = 0
    if not data.getBreakdown().empty:
        match(components, data.getBreakdown())
    if len(predictions) > 0:
        components.loc[:, 'Cluster'] = predictions

    components["Cluster"] = 'Cluster # ' + components["Cluster"].astype(str)
    fig = px.scatter(components, x='Component 1', y='Component 2', color='Breakdown Type', symbol='Cluster', text='Strain', 
                     color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.layout = plotly.graph_objects.Layout(plot_bgcolor='#ffffff', width=700, height=500)
    fig.update_traces(textposition='top left', marker_size = 10)

    pltJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return pltJSON
   
def buildPlots(data, methods, perplexity, clusterMethods, n_clusters, linkage):
    plots = {}
    genes_count = data.getCount()
    genes_count = genes_count.loc[:, (genes_count != 0).any(axis=0)]
    if genes_count.empty:
        return plots

    strains = genes_count[genes_count.columns[0]]
    features = genes_count.columns[1:]

    predictions = []

    if len(strains) > 1:
    
        if len(features)>1:
    
            x = genes_count.loc[:, features].values
            x = StandardScaler().fit_transform(x)

            if '0' in clusterMethods:
                model = KMeans(n_clusters=int(n_clusters))
                model.fit(x)
                predictions = model.predict(x)
            if '1' in clusterMethods:
                model = AgglomerativeClustering(n_clusters=int(n_clusters), affinity='euclidean', linkage=linkage)
                model.fit_predict(x)
                predictions = model.labels_
            if '2' in clusterMethods:
                model = AffinityPropagation()
                model.fit(x)
                predictions = model.labels_


            if '0' in methods:
                methodData = PCA(n_components=2, random_state=0)
                components = pd.DataFrame(data = methodData.fit_transform(x), columns = ['Component 1', 'Component 2'])
                plots['PCA'] = buildScatter(data, components, strains, predictions)

            if '1' in methods:
                methodData = MDS(random_state=0)
                components = pd.DataFrame(data = methodData.fit_transform(x), columns = ['Component 1', 'Component 2'])
                plots['MDS'] = buildScatter(data, components, strains, predictions)

            if '2' in methods:
                methodData = TSNE(random_state=0, perplexity=int(perplexity))
                components = pd.DataFrame(data = methodData.fit_transform(x), columns = ['Component 1', 'Component 2'])
                plots['t-SNE'] = buildScatter(data, components, strains, predictions)

        else:
            x = []
            y = []
            for value in genes_count.loc[:, features].values:
                x.append(value[0])
                y.append(0)

            components = pd.DataFrame(data={'Component 1': x, 'Component 2': y})
        
            plots['No method'] = buildScatter(data, components, strains)

    return plots
        
