# FluSPred

A bioinformatic-ware to predict the zoonotic host tropism of Influenza A virus.

## Introduction
FluSPred(Flu Spread Prediction) is a machine learning based tool to predict the zoonotic host tropism of the Influenza A virus with the help of its protein and genome sequences, stating whether a viral strain has the potential to infect human hosts. This was developed to help prioritize high-risk viral strains for future research, aid the study of emergence or the risk a novel influenza virus possesses if it acquires the capability to spread human to human.

## Web Server
We are also providing the web-server using which user can directly submit their sequences and can download the predictions in the .csv format. The user can avail the web-server facility at https://webs.iiitd.edu.in/raghava/fluspred 

## Reference
Roy et al. (2022) In silico method for predicting infectious strains of influenza A virus from its genome and protein sequences. <a href="https://pubmed.ncbi.nlm.nih.gov/36318663/">J Gen Virol. 2022 Nov;103(11). doi: 10.1099/jgv.0.001802.</a>
                        <a>
## Pip installation
The pip version of FluSpread is also available for easy installation and usage of the tool. The following command is required to install the package 
```
pip install fluspred
```
To know about the available option for the pip package, type the following command:
```
fluspred -h
```
## Standalone
To cater to a wider usersbase, and contribute to the scientific community, we have provided an open source standalone tool for FluSPred.
### Download
- Clone the repo using `git clone https://github.com/Logan1x/FluSPred.git`
- go into the repository by `cd FluSpred`
- see How to Use to find instructions for running the program.

Alternatively, you can download the zip folder using,

- Download the repo using https://github.com/Logan1x/FluSPred/archive/refs/heads/main.zip
- extract or uncompress the zip file.
- Go into the repository by `cd FluSpred` or double-clicking the folder.
- See How to Use to find instructions for running the program.

### How to Use

#### Installing dependencies

Use the command `pip install -r requirements.txt` to install the library dependencies in the terminal. This step will install all required dependencies in your system.
After this step, your system is ready to run the program.

#### Running the program


Run `python main.py -h` for instructions regarding running of the program.

It will output in this,

```BASH
$ python main.py -h
loading...

usage: main.py [-h] -i INPUT -o OPTION [-pn PROTEINNAME]

Please provide following arguments to proceed

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input File Name: protein or genome sequence in FASTA format
  -o OPTION, --option OPTION
                        Select which kind of file you are giving, Protein(P) or Genome(G)
                        
                        P : Protein
                        G : Genome 
                        
  -pn PROTEINNAME, --proteinName PROTEINNAME
                        This argument is only required when choosing OPTION as protein
                        enter the Protein name from 15 proteins listed below
                        HA :  Haemagglutinin 
                        PA :  Polymerase Acidic
                        PB1 :  Polymerase Basic 1
                        PB2 :  Polymerase Basic 2
                        NP :  Nucleoprotein
                        NA :  Neuraminidase
                        M1 :  Matrix Protein 1
                        M2 :  Matrix Protein 2
                        NS1 : Non-Structural 1
                        NS2 : Non-Structural 2
                        PB1F2 : PB1F2
                        PB1N40 : PB1-N40
                        PAN155 : PA-N155
                        PAN182 : PA-N182
                        PAX : PAX
 ```
 
 As you can see from the options above, this program needs at least two arguments (3 in the case of protein) to run. The first argument is of an input file, which you want to predict for, in fasta format. The second argument asks for the type of sequences you gave in the input file. If the input file contains nucleotide or genome sequences, provide the option as **G**, and if the file includes protein or peptide sequences, give the option as **P**. If your choice of selection for the option is P then the program needs one additional argument called a Protein name. You have to provide one of fifteen proteins provided in the command output above.
 

That's It!. You are good to go. You can run the example program for genome file by using the below command, 

```BASH
python main.py -i genomeSample.fasta -o G 
```
Similarly, For Protein file, you can run using below command

```BASH
python main.py -i ProteinSample.fasta -o P -pn pax
```

An **`Output.csv`** file will be generated containg all your outputs.
