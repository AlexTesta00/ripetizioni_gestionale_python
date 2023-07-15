# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:15:31 2023

@author: Alecs
"""

def compute_dictionary(start_dictionary):
    return {'k': list(start_dictionary.keys()), 
            'v':list(start_dictionary.values()), 
            'kv' : list(start_dictionary.items())}


print(compute_dictionary({1:10, 2:20, 3:30}))