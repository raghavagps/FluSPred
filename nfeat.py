# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:44:18 2020

@author: Megha Mathur
"""

from ml_run import *
import argparse  
import warnings
from collections  import defaultdict
import  pandas as pd
import os


    
def allp(k):
  n =['A','T','C','G']
  s=[]
  if (k==1):
    return n
  elif(k==2):
    for i in n:
      for j in n:
        se = i+j
        if (se not in s):
          s.append(se)
    return s
  elif(k==3):
    for i in n:
      for j in n:
        for k in n:
          se = i+j+k
          if (se not in s):
            s.append(se)
    return s

  elif(k==4):
    for i in n:
      for j in n:
        for k in n:
          for l in n:
            se = i+j+k+l
            if (se not in s):
              s.append(se)
    return s


def kmer(k,seq,order):
    s=[]
    for i in range(len(seq)):
        se=""
        if (i+k > len(seq)):
            break
        for j in range(k):
            if i+(j*order)>=len(seq):
                break
            else:
                se = se+seq[i+(j*order)]
        if len(se)<k:
            break
        s.append(se)
    return s

def k_mer_comp(f1,k,order,dict_n):
    a=allp(k)
    rs = kmer(k,f1,order)
    #calculating basic k-mer composition
    for i in a:
        ct =(rs.count(i)/len(rs))*100
        dict_n[i].append(ct)   


def calcNfeat(f1):

    k = 3

    order = int(1)


    dict_n = defaultdict(list)
    a=allp(k)
    filename, file_extension = os.path.splitext(f1)

    cdk = pd.DataFrame()


    if(file_extension==""):
        f1=f1.upper()
        alphabet=['A','C','G','T']
        for i in f1:
            if i not in alphabet:
                print("Invalid Character found in the given sequence")
                exit()
        k_mer_comp(f1,k,order,dict_n)
        s = []
        s.append(f1)
        if 'Sequence'  not in cdk.columns:
            cdk['Sequence']=s
        for i in a:
            cdk["CDK_"+i]= dict_n[i]
        # cdk.to_csv(out,index=False)
        computeML(cdk)
    else:
        f=open(f1,"r")
        b= f.readlines()
        sequence=[]
        s_id =[]
        s=""
        f.close()
        for i in b:
            if i[0] == '>':
                i=i.split("\n")
                s_id.append(i[0])
                if s!= "":
                    sequence.append(s)
                    s=""
                    
                else:
                    continue
            else:
                for j in i:
                    j=j.capitalize()
                    if(j in ['A','G','C','T']):
                        s = s+j
        if s!="":
            sequence.append(s)
        for i in sequence:
            k_mer_comp(i,k,order,dict_n)
        if 'Sequence_ID' not in cdk.columns:
            cdk['Sequence_ID'] = s_id
        
        for i in a:
            cdk["CDK_"+i]= dict_n[i]
        computeML(cdk)