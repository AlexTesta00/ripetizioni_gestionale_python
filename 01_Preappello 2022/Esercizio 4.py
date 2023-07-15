# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:35:41 2023

@author: Alecs
"""

class Meteo():
    
    #Inizializzo il costruttore
    def __init__(self,good_day = lambda x:x['rain'] == 0):
        #Dizionario di dizionari che conterrà tutte le liste di dati
        self.ss = {}
        self.gd = good_day
    
    #Richiama il metodo toString dell'oggetto corrente
    def __str__(self):
        return f'Data base with {len(self.ss)} days'
    
    #Inserisce un nuovo dato meteo all'interno del dizionario
    def insert(self, data, values):
        """
        Ammettendo che non posso inserire la stessa data due volte
        Inserisco nel dizionario interno dela classe (.ss) i dati meteo
        di un giorno specifico.
        """
        self.ss[data] = dict(zip(('temp_min', 'temp_max', 'rain', 'wind'), values))
    
    #Insert alternativo (va benissimo comunque)
    def alternative_insert(self, data, temp_min, temp_max, rain, wind):
        self.ss[data] = {
            'temp_min' : temp_min,
            'temp_max' : temp_max,
            'rain' : rain,
            'wind' : wind
        }
        
    #Soluzione del prof (fa esattamente quello che vedi nel metodo sotto)
    def il_meteo(self,data):
        x = self.ss.get(data,None)
        if x == None: return "Dato non presente"
        if x['rain'] == 0: return "Sereno"
        else: return "Piovoso"
    
    def alternative_il_meteo(self, data):
        #Controllo se il dizionario contiene la chiave
        if data in self.ss.keys(): 
            #Se i mm di pioggia sono pari a zero restituisco sereno altrimenti piovoso
            current_rain = self.ss.get(data)
            if current_rain['rain'] == 0:
                return 'Sereno'
            else:
                return 'Piovoso'
        else:
            return 'Dato non presente'
    
    def __iter__(self):
        #Ordino dal giorno più recente al meno recente
        days = sorted(self.ss.keys(), key = lambda x:x[-1::-1])
        for d in days:
            stat = self.ss[d]
            if self.gd(stat):
                yield d, stat #Restituisce gli oggetti al chiamante

    
    def alternative_iter(self):
        #Costruisco la lista di giorni che soddisfano la condizione self.gd
        valid_day = []
        for key in self.ss.keys():
            if self.gd(self.ss[key]):
                valid_day.append(key) #Inserisco le date che rispettano la condizione
        valid_day.sort(key= lambda tup : tup[2]) #Ordino le tuple per anno
        return valid_day
    
    def stat(self,
             flt1 = lambda k,v: v['rain'] > 0,
             flt2 = lambda k,v: True):
        per = len([(k,v) for k,v in self.ss.items() if flt1(k,v)])/len([(k,v) for k,v in self.ss.items() if flt2(k,v)])
        return f'{per:5.2%}'
                
    
    
"""
TEST
"""

m = Meteo()
ds = [(i,1,2000) for i in range(1,10)] #alcune date
ds[0] = (1,1,2002)
values = [(19,29,0,6),(19,25,0,0),(14,22,50,0),(19,25,0,0),(19,26,10,0),
(19,25,0,0),(19,25,0,0),(14,22,50,0),(19,30,0,7)] #i corrispondenti valori
for d,v in zip(ds, values): #inserimento di date e valori
    m.insert(d,v)

m.gd = lambda v: v['rain'] == 0 and v["temp_max"] <= 26


for d in m: # si elencano i giorni di pioggia con temperatura massima inferiore a 26
    print(d)
    
f1 = lambda k,v: v['wind'] > 5 and k[1] == 1
f2 = lambda k,v: k[1] == 1
x = m.stat(f1, f2) #% di giorni ventosi a gennaio