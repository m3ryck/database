#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:31:53 2019

@author: adriano
"""

import pandas as pd
 
 
dataset = pd.read_csv("ALL_FILTRADOS.csv")

dataset.drop(109,inplace=True)
dataset.drop(89,inplace=True)
dataset.drop(34,inplace=True)


dataset.drop(1,inplace=True)
dataset.drop(2,inplace=True)
dataset.drop(95,inplace=True)
dataset.drop(17,inplace=True)
dataset.drop(15,inplace=True)
dataset.drop(60,inplace=True)
dataset.drop(28,inplace=True)
dataset.drop(44,inplace=True)


dataset.drop('Unnamed: 0',axis=1,inplace=True)



 #Salvando em um novo CSV
 dataset.to_csv("ALL_FILTRADOS_BACKUP.csv")
 
 dataset.drop('Unnamed: 0',axis=1,inplace=True)
 
 
 dataset.to_csv("ALL_FILTRADOS.csv",index=False)
 