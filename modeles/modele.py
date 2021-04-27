#!/usr/bin/python
# -*- coding: utf-8 -*-


from pymongo import MongoClient


collection = None

def getCollectionBD() :
	global collection
	try :
		if collection == None :
			 client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
			 db_data = client.dataDimog
			 collection = db_data['collecDimog']
		return collection
	except :
		return None
		
		
def getAllData():
	try :
		curseur = getCollectionBD().find()
		return curseur
	except :
		return None

#  ----------------------- FONCTIONS  DYNAMIQUES ----------------------
def getWithDate(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		curseur = getCollectionBD().aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}}])
		return curseur
	except :
		return None

def getMaxWithPopulation(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		max = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Average population (1 January)" : {"$max" : '$Average population (1 January)'}}}])
		return max
	except :
		return None

def getMinWithPopulation(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		min = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Average population (1 January)" : {"$min" : '$Average population (1 January)'}}}])
		return min
	except :
		return None

def getAvgWithPopulation(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		avg = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Average population (1 January)" : { "$avg" : '$Average population (1 January)'} }}])
		return avg
	except :
		return None

#  -------------- A CORRIGER LES REQUETTES de NAISSNACE---------------
def getMaxNaiss(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		max = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Live births" : {"$max" : '$Live births'}}}])
		return max
	except :
		return None

def getMinNaiss(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		min = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Live births" : {"$min" : '$Live births'}}}])
		return min
	except :
		return None

def getAvgNaiss(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		avg = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Live births" : { "$avg" : '$Live births'} }}])
		return avg
	except :
		return None

# ------------- A CORRIGER LES REQUETES DE DECES ---------------------
def getMaxDec(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		max = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Deaths" : {"$max" : '$Deaths'}}}])
		return max
	except :
		return None

def getMinDec(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		min = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Deaths" : {"$min" : '$Deaths'}}}])
		return min
	except :
		return None

def getAvgDec(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		avg = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Deaths" : { "$avg" : '$Deaths'} }}])
		return avg
	except :
		return None

# ------------- A CORRIGER LES REQUETES DE CHANGEMENT NATUREL ---------------------
def getMaxChNat(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		max = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Natural change" : {"$max" : '$Natural change'}}}])
		return max
	except :
		return None

def getMinChNat(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		min = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Natural change" : {"$min" : '$Natural change'}}}])
		return min
	except :
		return None

def getAvgChNat(yearDeb,yearFin):
	try :
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		avg = collection.aggregate([{"$match":{"$and": [{"Year": {'$gte':yearDeb}}, {"Year": {'$lte': yearFin}}]}},{"$group" : {"_id" : 'null', "Natural change" : { "$avg" : '$Natural change'} }}])
		return avg
	except :
		return None


# ------------- A CORRIGER LES REQUETES DE CHANGEMENT NATUREL % ---------------------
def getMaxChNatPourcen(yearDeb, yearFin):
	try:
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		max = collection.aggregate([{"$match": {"$and": [{"Year": {'$gte': yearDeb}}, {"Year": {'$lte': yearFin}}]}}, {
			"$group": {"_id": 'null', "Natural change (per 1000)": {"$max": '$Natural change (per 1000)'}}}])
		return max
	except:
		return None

def getMinChNatPoucen(yearDeb, yearFin):
	try:
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		min = collection.aggregate([{"$match": {"$and": [{"Year": {'$gte': yearDeb}}, {"Year": {'$lte': yearFin}}]}}, {
			"$group": {"_id": 'null', "Natural change (per 1000)": {"$min": '$Natural change (per 1000)'}}}])
		return min
	except:
		return None

def getAvgChNatPourcen(yearDeb, yearFin):
	try:
		yearDeb = int(yearDeb)
		yearFin = int(yearFin)
		avg = collection.aggregate([{"$match": {"$and": [{"Year": {'$gte': yearDeb}}, {"Year": {'$lte': yearFin}}]}}, {
			"$group": {"_id": 'null', "Natural change (per 1000)": {"$avg": '$Natural change (per 1000)'}}}])
		return avg
	except:
		return None


# --------------------------- FONCTIONS POPULATION SANS ARGUMENTS -------------------------
def getmaxPopulation():
	try :
		max = collection.aggregate([ {"$group" : {"_id" : 'null', "Average population (1 January)" : {"$max" : '$Average population (1 January)'}}}])
		return max
	except :
		return None

def getavgPopulation():
	try :
		avg = collection.aggregate([ {"$group" : {"_id" : 'null', "Average population (1 January)" : { "$avg" : '$Average population (1 January)'} }}])
		return avg
	except :
		return None

def getminPopulation():
	try :
		min = collection.aggregate([{"$group" : {"_id" : 'null', "Average population (1 January)" : {"$min" : '$Average population (1 January)'}}}])
		return min
	except :
		return None


# --------------------------- FONCTIONS NAISSANCE SANS ARGUMENTS -------------------------
def getmaxNaiss():
	try :
		max = collection.aggregate([ {"$group" : {"_id" : 'null', "Live births" : {"$max" : '$Live births'}}}])
		return max
	except :
		return None

def getavgNaiss():
	try :
		avg = collection.aggregate([ {"$group" : {"_id" : 'null', "Live births" : { "$avg" : '$Live births'} }}])
		return avg
	except :
		return None

def getminNaiss():
	try :
		min = collection.aggregate([{"$group" : {"_id" : 'null', "Live births" : {"$min" : '$Live births'}}}])
		return min
	except :
		return None


# --------------------------- FONCTIONS DECES SANS ARGUMENTS -------------------------
def getmaxDec():
	try :
		max = collection.aggregate([ {"$group" : {"_id" : 'null', "Deaths" : {"$max" : '$Deaths'}}}])
		return max
	except :
		return None

def getavgDec():
	try :
		avg = collection.aggregate([ {"$group" : {"_id" : 'null', "Deaths" : { "$avg" : '$Deaths'} }}])
		return avg
	except :
		return None

def getminDec():
	try :
		min = collection.aggregate([{"$group" : {"_id" : 'null', "Deaths" : {"$min" : '$Deaths'}}}])
		return min
	except :
		return None
'''def kvjb():
	avg = collection.aggregate([{"$match": {"$and": [{"Year": {'$gte': 1903}}, {"Year": {'$lte': 1912}}]}},
								{"$group": {"_id": 'null', "Deaths": {"$avg": '$Deaths'},'Year':'$Year' }}])'''
