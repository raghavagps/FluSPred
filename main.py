from nfeat import *
from getDPC import *

import argparse  
from argparse import RawTextHelpFormatter

import warnings
from collections  import defaultdict
import  pandas as pd
import os


warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser(description='Please provide following arguments to proceed',formatter_class=RawTextHelpFormatter) 

## Read Arguments from command

parser.add_argument("-i", "--input", type=str,required=True,help="Input File Name: protein or genome sequence in FASTA format")
parser.add_argument("-o","--option",type=str,required=True, help="Select which kind of file you are giving, Protein(P) or Genome(G)\n""\n""P : Protein\n""G : Genome \n""\n")
parser.add_argument("-pn","--proteinName",type=str, help="This argument is only required when choosing OPTION as protein" "\n" "enter the Protein name from 15 proteins listed below""\n""HA :  Haemagglutinin \n""PA :  Polymerase Acidic\n""PB1 :  Polymerase Basic 1\n""PB2 :  Polymerase Basic 2\n""NP :  Nucleoprotein\n""NA :  Neuraminidase\n""M1 :  Matrix Protein 1\n""M2 :  Matrix Protein 2\n""NS1 : Non-Structural 1\n""NS2 : Non-Structural 2\n""PB1F2 : PB1F2\n""PB1N40 : PB1-N40\n""PAN155 : PA-N155\n""PAN182 : PA-N182\n""PAX : PAX\n")

print("loading...\n")

# Parameter initialization or assigning variable for command level arguments
args = parser.parse_args()
f1 = args.input 


# change this output
out= "outfile.csv" 

# open(out, 'a').close()

if (args.option.upper()) == "G":
    calcNfeat(f1)
elif (args.option.upper()) == "P":
    if (args.proteinName != None):
        if (args.proteinName == "PB1F2" or args.proteinName == "NS2"):
            test_df = get_aac_from_fasta(f1)
            computeMLProtein(test_df,args.proteinName.upper())
        else:
            test_df = get_dpc_from_fasta(f1)
            computeMLProtein(test_df,args.proteinName.upper())
    else:
        print("Please enter the correct protein name")
        exit()

else:
    print("Please enter correct options. See help for more details")
    exit()

print("Program Excution Completed! Please check the output file.")