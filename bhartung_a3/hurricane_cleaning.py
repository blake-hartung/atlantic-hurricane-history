#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:05:15 2021

@author: blake_hartung
"""

import os
import pandas as pd
import numpy as np
import json


def pressure_split(pressure_val):
    val = pressure_val.split(' ')[0]
    if val == "Unknown" or val == '' or val == '-':
        return(np.nan)
    else:
        val = val.replace(',', '').replace('<', '').replace('≤', '').strip()
        return(float(val))

def pressure_split_cat_4_1950(val):
    if val == "Unknown" or val == '' or val == '-':
        return(np.nan)
    else:
        val = val.replace(',', '').replace('<', '').replace('≤', '').strip()
        return(float(val))
    
def cat_1_2_sifting(cat_data, category):
    data = [line.split("\t")[0:4] for line in cat_data]
    df = pd.DataFrame(data, columns=['name',
                                     'date',
                                     'max_sust_winds',
                                     'pressure'])
    df["sust_winds_mph"] = df['max_sust_winds'].apply(lambda x: float(x.split(' ')[0]))
    df["pressure_hpa"] = df["pressure"].apply(pressure_split)
    df["year"] = df["date"].apply(lambda x: int(x.split(' ')[-1]))
    ret_df = df[["name", "year", "sust_winds_mph", "pressure_hpa"]]
    ret_df["category"] = category
    return(ret_df)

def cat_3_sifting(cat_data):
        data = [line.split("\t")[0:5] for line in cat_data]
        df = pd.DataFrame(data, columns=['name',
                                         'date',
                                         'duration',
                                         'max_sust_winds',
                                         'pressure'])
        df["sust_winds_mph"] = df['max_sust_winds'].apply(lambda x: float(x.split(' ')[0]))
        df["pressure_hpa"] = df["pressure"].apply(pressure_split)
        df["year"] = df["date"].apply(lambda x: int(x.replace('†', '').strip().split(' ')[-1]))
        ret_df = df[["name", "year", "sust_winds_mph", "pressure_hpa"]]
        ret_df["category"] = 3
        return(ret_df)

def cat_4_1950_sifting(cat_data):
    indeces = [0, 1, 2, 5, 6]
    data = [[line.split("\t")[i] for i in indeces] for line in cat_data]
    df = pd.DataFrame(data, columns = ['name',
                                       'year',
                                       'month',
                                       'max_sust_winds',
                                       'pressure'])
    df["sust_winds_mph"] = df["max_sust_winds"].apply(lambda x: float(x))
    df["pressure_hpa"] = df['pressure'].apply(pressure_split_cat_4_1950)
    df["year"] = df["year"].apply(lambda x: int(x))
    ret_df = df[["name", "year", "sust_winds_mph", "pressure_hpa"]]
    ret_df["category"] = 4
    return(ret_df)

def cat_4_present_sifting(cat_data):
    data = list()
    for i in range(len(cat_data)):
        if 'Hurricane' in cat_data[i]:
            sub_list = [cat_data[i]]
            string_ls = cat_data[i + 2].split('\t')
            sub_list.append(int(string_ls[0]))
            sub_list.append(float(string_ls[2].split(' ')[0]))
            sub_list.append(float(string_ls[3].split(' ')[0]))
            sub_list.append(4)
            data.append(sub_list)
    ret_df = pd.DataFrame(data, columns = ['name',
                                           'year',
                                           'sust_winds_mph',
                                           'pressure_hpa',
                                           'category'])
    return(ret_df)

def cat_5_sifting(cat_data):
    data = [line.split("\t")[0:5] for line in cat_data]
    df = pd.DataFrame(data, columns = ['name',
                                       'date',
                                       'duration',
                                       'max_sust_winds',
                                       'pressure'])
    df["sust_winds_mph"] = df["max_sust_winds"].apply(lambda x: float(x.split(' ')[0]))
    df["pressure_hpa"] = df["pressure"].apply(pressure_split)
    df["year"] = df["date"].apply(lambda x: int(x.replace('†', '').strip().split(' ')[-1]))
    ret_df = df[["name", "year", "sust_winds_mph", "pressure_hpa"]]
    ret_df["category"] = 5
    return(ret_df)
    

cwd = os.getcwd()

cat_1 = cwd + "/cat_1_atlantic_hist.txt"
cat_1_info = list()

with open(cat_1) as c1:
    for line in c1:
        cat_1_info.append(line)

cat_2 = cwd + "/cat_2_atlantic_hist.txt"
cat_2_info = list()

with open(cat_2) as c2:
    for line in c2:
        cat_2_info.append(line)

cat_3 = cwd + "/cat_3_atlantic_hist.txt"
cat_3_info = list()

with open(cat_3) as c3:
    for line in c3:
        cat_3_info.append(line)

cat_4_1950 = cwd + "/cat_4_atlantic_1853-1950.txt"
cat_4_1950_info = list()

with open(cat_4_1950) as c4:
    for line in c4:
        cat_4_1950_info.append(line)

cat_4_present = cwd + "/cat_4_atlantic_1951-2020.txt"
cat_4_present_info = list()

with open(cat_4_present) as c4:
    for line in c4:
        cat_4_present_info.append(line)

cat_5 = cwd + "/cat_5_atlantic_hist.txt"
cat_5_info = list()

with open(cat_5) as c5:
    for line in c5:
        cat_5_info.append(line)

df_cat_1 = cat_1_2_sifting(cat_1_info, 1)
df_cat_2 = cat_1_2_sifting(cat_2_info, 2)
df_cat_3 = cat_3_sifting(cat_3_info)
df_cat_4_1950 = cat_4_1950_sifting(cat_4_1950_info)
df_cat_4_present = cat_4_present_sifting(cat_4_present_info)
df_cat_5 = cat_5_sifting(cat_5_info)

df_complete = df_cat_1.append(df_cat_2).append(df_cat_3).append(df_cat_4_1950)\
    .append(df_cat_4_present).append(df_cat_5)

json_str = df_complete.to_json(orient="records")
json_list = json.loads(json_str)

with open("atlantic_hurricane_data.json", 'w') as f:
    json.dump(json_list, f)

df_complete.to_csv("atlantic_hurricane_data.csv", index=False)
