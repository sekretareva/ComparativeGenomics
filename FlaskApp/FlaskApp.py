from flask import Flask, request, render_template, send_file, make_response, Response
import pandas as pd
from hadlers.Data import Data
from hadlers.keywordsClassifier import keywordsClassify
from hadlers.classifier import classifyFunctions
from hadlers.clsDisplay import displayClassification
from hadlers.counter import countFunctions
from hadlers.visualize import buildPlots
from hadlers.validator import validate
from sys import getsizeof

app = Flask(__name__)
data = Data()
allowed_file_types = ['csv']

if data.getRastCls().shape[0] == 0:
        data.setRastCls(pd.read_csv('static/csvFiles/rastClassification.csv'))

if getsizeof(data.getHierarchy):
        hierarchy = displayClassification(data)
        data.setHierarchy(hierarchy)

@app.route('/')
def index():
     return render_template("index.html")

@app.route('/analisis', methods=['get', 'post'])
def analyse():
    return render_template("analisis.html", dict=data.getClassified(), hierarchy=data.getHierarchy(), countTable=data.getCount(), plots=data.getPlots(), displayCount=1)

@app.route('/documentation', methods=['get'])
def documentation():
    return render_template("documentation.html")

@app.route('/reset', methods=['post'])
def reset():
    data.reset()
    return render_template("analisisCls.html", dict=data.getClassified(), displayCount=1)


@app.route('/classify', methods=['post'])
def classify():
    cls_types = request.form.getlist('cls_type')
    rastDownloads = request.files.getlist("rastDownloads[]")
    userCls = request.files.get("userCls")

    errors = []
    if (userCls):
        errorUserCls, validated = validate(userCls, "userCls")
        data.setUserCls(validated)
        errors.append(errorUserCls)

    errorDownloads, validated = classifyFunctions(cls_types, rastDownloads, data)
    data.setClassified(validated)  
    errors.append(errorDownloads)

    return render_template("analisisCls.html", dict=data.getClassified(), displayCount=1, errors=errors)

@app.route('/fullClassified', methods=['get', 'post'])
def fullClassified():
    dict = data.getClassified()
    return render_template("fullClassified.html", dict=dict, displayCount=len(dict))


@app.route('/count', methods=['post'])
def count():
    categories = request.form.getlist('categories')
    systems = request.form.getlist('systems')
    data.setCount(countFunctions(data, categories, systems))    
    return render_template("analisisCount.html", countTable=data.getCount())

@app.route('/visualize', methods=['post'])
def visualize():
    methods = request.form.getlist('method')
    perplexity = request.form['perplexity']
    
    data.setPlots(buildPlots(data, methods, perplexity))
    
    return render_template("analisisVsl.html", plots=data.getPlots())

@app.route('/download/<type>/<filename>', methods=['get'])
def download(type, filename):
    if type == "classified":
        df = data.getClassified()[filename].to_csv(index=False)
    if type == "kwClassification":
        df = data.getKwCls().to_csv(index=False)
    if type == "counted":
        df = data.getCount().to_csv(index=False)
    return Response(df,status=200,headers={"Content-disposition":"attachment; filename="+filename+".csv"},mimetype="application/csv")

@app.route('/uploadBreakdown', methods=['post'])
def uploadBreakdown():
    breakdown = request.files.get("breakdown")
    error, validated = validate(breakdown, 'breakdown')
    data.setBreakdown(validated)
    return  render_template("breakdown.html", df=data.getBreakdown(), error=error)

if __name__ == "__main__":
  app.run(debug=True)