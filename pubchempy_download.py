#====================================================================================================================================
#
#          FILE: pubchempy_download.py
# 
# REQUIREMENTS:   create a file (input_cid) with your cid numbers of compunds you want to upload. Put this file in the same directory/folder as pubchempy_download.py. You must install first of all python on your computer. For more informations, go to webnsite (https://pubchemdocs.ncbi.nlm.nih.gov/downloads)of pubchem
# AUTHOR: KANKİNOU SELONOU GAUTİER 
# CREATED: 25-04-2022 
#====================================================================================================================================

import time
import pubchempy as pcp
myfiles = open("input_cid", "r")
for myline in myfiles:
    c = pcp.Compound.from_cid(myline)
    myline = myline.replace("\n","")
    a = str(myline+","+c.isomeric_smiles)
    lines = ['Readme', '']
    with open('output_cid.txt', 'a') as f:
        f.write(a)
        f.write('\n')
        time.sleep(1)
        print('************')
   

