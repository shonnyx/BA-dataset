'''
    用于确认数据标签信息，是否在原始数据集中存在
'''

import os
import sys
import numpy as np
import pandas as pd

import lmdb
from tqdm import tqdm

df = pd.read_excel('./ABIDE-select.xlsx', sheet_name='Sheet1')
for index, row in tqdm(df.iterrows()):
    SITE_ID = str(row['SITE_ID'])
    SUB_ID = str(row['SUB_ID'])
    age = float(row['AGE_AT_SCAN'])
    gender = int(row['SEX'])

    diction = {'CALTECH' : 'Caltech'}

    if SITE_ID == 'CALTECH':

        site = diction[SITE_ID]

        img_dir = '/data/dataset/ABIDE/' + site
        pid = 'sub-' + SUB_ID.zfill(7)

        img_path = os.path.join(img_dir, pid, 'anat', pid + '_T1w.nii.gz')

        if not os.path.exists(img_path):
            print(SUB_ID)