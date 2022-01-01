import pandas as pd
import numpy as np
from Bio.Seq import Seq 
from Bio import SeqIO
from itertools import permutations
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict,cross_val_score
from Bio.SeqUtils.ProtParam import ProteinAnalysis
#from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,matthews_corrcoef
import glob
from sklearn.model_selection import KFold
import collections



def get_df_from_fasta(fasta_location):
  data = []
  fasta_sequences = SeqIO.parse(open(fasta_location),'fasta') #opens fatsa file of the given 
  for fasta in fasta_sequences: #loops through fasta_Sequences
    name, sequence = fasta.description, str(fasta.seq)
    data.append((name, sequence))
  df = pd.DataFrame(data,columns=['Features','Sequence'])
  features = df['Features'].str.split('|',expand=True)# extracting features from metadata
  df = pd.concat([df,features],axis=1)
  return df


def get_dpc(sequence):
  unique_amino_acids = list(set(sequence))
  #get permutations
  total_dpc_permutation = list(permutations(unique_amino_acids,2))
  #adding the permutation of an amino acid with itself
  for amino_acid in unique_amino_acids:
    total_dpc_permutation.append((amino_acid,amino_acid))
  #the list is a list of tuples, converting to a list of strings
  final_dpc_columns = []
  for dpc_perm in total_dpc_permutation:
    final_dpc_columns.append("".join(dpc_perm))
  dpc_freq = {}
  for dpc in final_dpc_columns:
    dpc_freq[dpc] = sequence.count(dpc)
  
  return dpc_freq

def get_dpc_from_fasta(fasta_location):
  df = get_df_from_fasta(fasta_location) 
  dpc_all = []
  for sequence in df["Sequence"]:
    dpc_all.append(get_dpc(sequence))
  dpc_df = pd.DataFrame(dpc_all,columns=list(dpc_all[0].keys()))
  sum_dpc = dpc_df.sum(axis=1)
  dpc_df2 = dpc_df.div(sum_dpc,axis=0)
  dpc_df2 = dpc_df2*100
  dpc_df2 = dpc_df2.sort_index(axis=1)
  dpc_df2['Features'] = df['Features']
  return dpc_df2

def merge_dicts(dicts):            #AAC begins
    merged = collections.defaultdict(list)
    for d in dicts:
        for k, v in d.items():
            merged[k].append(v)
    return dict(merged)

def get_aac_from_fasta(fasta_location):
  df = get_df_from_fasta(fasta_location)
  seq_dictionary = []
  for i,sequence in enumerate(df['Sequence']):
    X = ProteinAnalysis(sequence)
    seq_dictionary.append(X.get_amino_acids_percent())

  merged = merge_dicts(seq_dictionary)
  percent_comp = pd.DataFrame(merged)
  percent_comp['Features'] = df['Features']

  return percent_comp