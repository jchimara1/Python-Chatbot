# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 01:15:40 2023

@author: Justice
"""

import csv
import pandas as pd
import json


df = pd.read_csv("Conversation.csv")

df = df.drop("Unnamed: 0", axis = "columns")


new = df.to_json(orient = "records")


txt = {"question": new
}


 
# Writing to sample.json
with open("knowledge_base_test.json", "w") as outfile:
    outfile.write(str(txt))

  
    