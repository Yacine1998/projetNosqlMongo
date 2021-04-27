#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *

import modeles.modele
from modeles import modele

app = Flask(__name__)
app.secret_key = 'Data'


@app.route('/accueil', methods=['GET'])
def index():
    table1 = modele.getAllData()
    table2 = modele.getAllData()
    return render_template('vueAccueil.html', table1=table1, table2=table2)

@app.route('/tableau', methods=['GET'])
def tab():
    table = modele.getAllData()
    return render_template('tableau.html', table=table)

@app.route('/graph', methods=['GET'])
def graph():
    table = modele.getAllData()
    graphie = modele.getAllData()

    maxPopulation = modele.getmaxPopulation()
    minPopulation = modele.getminPopulation()
    avgPopulation = modele.getavgPopulation()

    maxNaiss = modele.getmaxNaiss()
    minNaiss = modele.getminNaiss()
    avgNaiss = modele.getavgNaiss()

    maxDec = modele.getmaxDec()
    minDec = modele.getminDec()
    avgDec = modele.getavgDec()

    return render_template('graph.html', table=table, graphie=graphie,avgDec=avgDec,maxDec=maxDec,minDec=minDec,avgNaiss=avgNaiss,minNaiss=minNaiss,maxNaiss=maxNaiss, maxPopulation=maxPopulation, minPopulation=minPopulation,avgPopulation=avgPopulation)

@app.route('/poster', methods=['GET'])
def poster():
    table1 = modele.getAllData()
    table2 = modele.getAllData()
    return render_template('poster.html', table1=table1, table2=table2)

@app.route('/vueAccueil/vueDate', methods=['POST'])
def getWithDate():
    yearDeb = request.form['yearDeb']
    yearFin = request.form['yearFin']
    table1 = modele.getAllData()
    table2 = modele.getAllData()
    if yearFin != '' and yearFin != '':
        tableA = modele.getWithDate(yearDeb, yearFin)
        tableB = modele.getWithDate(yearDeb, yearFin)

        dataGraphPop = modele.getWithDate(yearDeb,yearFin)
        dataGraphNaissEtDec = modeles.modele.getWithDate(yearDeb,yearFin)
        dataGraphChNat = modele.getWithDate(yearDeb,yearFin)

        maxPop = modele.getMaxWithPopulation(yearDeb,yearFin)
        minPop = modele.getMinWithPopulation(yearDeb,yearFin)
        avgPop = modele.getAvgWithPopulation(yearDeb, yearFin)
        maxNaiss = modele.getMaxNaiss(yearDeb,yearFin)
        minNaiss = modele.getMinNaiss(yearDeb,yearFin)
        avgNaiss = modele.getAvgNaiss(yearDeb,yearFin)
        maxDec = modele.getMaxDec(yearDeb,yearFin)
        minDec = modele.getMinDec(yearDeb,yearFin)
        avgDec = modele.getAvgDec(yearDeb,yearFin)
        maxChNat = modele.getMaxChNat(yearDeb,yearFin)
        minChNat = modele.getMinChNat(yearDeb,yearFin)
        avgChNat = modele.getAvgChNat(yearDeb,yearFin)
        maxChNatPourcen = modele.getMaxChNatPourcen(yearDeb,yearFin)
        minChNatPourcen = modele.getMinChNatPoucen(yearDeb,yearFin)
        avgChNatPourcen = modele.getAvgChNatPourcen(yearDeb,yearFin)

        infoRecue = True
        return render_template('vueDateInsert.html' ,dataGraphChNat=dataGraphChNat,dataGraphNaissEtDec=dataGraphNaissEtDec,dataGraphPop=dataGraphPop,minChNatPourcen=minChNatPourcen,avgChNatPourcen=avgChNatPourcen,avgChNat=avgChNat,maxChNatPourcen=maxChNatPourcen,minDec=minDec,avgDec=avgDec,maxChNat=maxChNat,minChNat=minChNat,minNaiss=minNaiss,avgNaiss=avgNaiss,maxDec=maxDec, maxNaiss=maxNaiss,table1=table1, table2=table2, tableA=tableA, tableB=tableB, infoRecue = infoRecue, maxPop = maxPop , minPop = minPop, avgPop=avgPop )
    else:
        redirect('/poster')

@app.route('/dynamic', methods=['POST'])
def getWithDateDynam():
    yearDebDynam = request.form['yearDeb']
    yearFinDynam = request.form['yearFin']
    tableDynam1 = modele.getAllData()
    tableDynam2 = modele.getAllData()
    if yearFinDynam != '' and yearFinDynam != '':
        tableDynam = modele.getWithDate(yearDebDynam, yearFinDynam)
        maxPopDynam = modele.getMaxWithPopulation(yearDebDynam,yearFinDynam)
        minPopDynam = modele.getMinWithPopulation(yearDebDynam,yearFinDynam)
        avgPopDynam = modele.getAvgWithPopulation(yearDebDynam, yearFinDynam)
        infoRecueDynam = True
        return render_template('dynamic.html', tableDynam1=tableDynam1, tableDynam2=tableDynam2, tableDynam=tableDynam, infoRecueDynam = infoRecueDynam, maxPopDynam = maxPopDynam , minPopDynam = minPopDynam, avgPopDynam=avgPopDynam )
    else:
        redirect('/poster')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
