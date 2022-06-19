'''
    用于确认数据标签信息，是否在原始数据集中存在
'''

import os
import sys
import numpy as np
import pandas as pd

from tqdm import tqdm

df = pd.read_excel('./normals/ACPI.xlsx', sheet_name='Sheet1')
for index, row in tqdm(df.iterrows()):
    SITE_ID = str(row['site_name'])
    SUB_ID = str(row['pid'])
    age = float(row['age'])
    gender = int(row['gender'])

    # diction = {'CALTECH' : 'Caltech'}
    # site = diction[SITE_ID]
    site = SITE_ID

    img_dir = '/data/dataset/ACPI/' + site
    pid = 'sub-' + SUB_ID.zfill(7)

    img_path = os.path.join(img_dir, pid, 'ses-1', 'anat')  # , pid + '_T1w.nii.gz'

    if not os.path.exists(img_path):
        print(SUB_ID)