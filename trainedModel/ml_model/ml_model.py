#!/usr/bin/env python
# coding: utf-8

# # Импорт и обработка данных

# In[83]:


# @title Импорт библиотек
import pandas as pd
import numpy as np
import joblib
import sklearn
from sklearn.ensemble import RandomForestClassifier

# In[89]:


# @title Импорт примера итоговых входных данных
inputDataTmp = pd.read_json(path_or_buf='./input.json', lines=True)
prof = pd.DataFrame.from_dict(inputDataTmp['profile'].tolist() )

# ----------------------------
prof = prof.fillna(0)
prof['birth_date'] = prof['birth_date'].astype(int)
prof.rename(columns = {'id':'profile_id'}, inplace = True )
# обработка input dataProfiles
prof['sex'] = prof['sex'] == 'male' # 0 - female, 1 - male
prof['sex'] = prof['sex'].astype(int)
prof['hr_delta'] = prof['hr_max'] -  prof['hr_rest']
del prof['hr_rest']
del prof['hr_max']
del prof['personal_goals']
# ----------------------------

inpData = pd.DataFrame.from_dict(inputDataTmp['sessions'].tolist() )

# ----------------------------
inpData = inpData.T
inpData.rename(columns = {0:'days'}, inplace = True )
inpData = pd.DataFrame.from_dict(inpData['days'].tolist() )
inpData['start_millis'] = inpData['start_millis'].astype(int)
inpData['stop_millis'] = inpData['stop_millis'].astype(int)
inpData['kkal'] = inpData['kkal'].astype(float)
inpData['activity_day'] = inpData['activity_day'].astype(int)
del inpData['timezone']
del inpData['skllzz_without_artifacts']
del inpData['skllzz_with_artifacts']
del inpData['skllzz']
del inpData['id']
inpData['delta_millis'] = inpData['stop_millis'] - inpData['start_millis']
del inpData['stop_millis']
del inpData['start_millis']
inpData = inpData.merge(prof, on='profile_id', how='inner')

inpDataSteps = pd.DataFrame.from_dict(inpData['steps'].tolist() )
del inpDataSteps['day']
del inpDataSteps['samples']
del inpData['steps']

inpData = inpData.join(inpDataSteps)
inpData = inpData.fillna(0)
# ----------------------------
inpData.head(1)


# # Импорт модели

# In[85]:


# Load model

model, ref_cols, target = joblib.load("./model.pkl")

tags = ref_cols
clf = model


# # Предсказание значений

# In[90]:


temp = pd.DataFrame(clf.predict_proba(inpData[tags]).tolist(), columns = clf.classes_)
prob_list = temp[1].tolist()

profileCheatProb = round( sum(prob_list)/len(prob_list) , 2)
prob_list = [profileCheatProb] + prob_list

print(prob_list) #первое значение вероятность читерства в сессии дней, далее вероятность читерства в каждом дне

