#!/usr/local/bin/python3
import subrocess
import sys


def database(TYPE):
	while True:
		print("specifing the database")
		react= input('Please specify the type of the database.\nEnter "p" for protein, or "n" for nucleotide.')
		if react == "n":
			TYP= 'nucleotide'#Term for esearch
			TYPE= 'nucl'#Term for blast
		elif react == "p":
			TYP= 'protein'
			TYPE= 'prot'
		else:
			print("Please enter a valid character.")
		fam= input('Please enter the family of the database, or enter "n" to skip.\n')
		org= input('Please enter the organism of interest, or enter "n" to skip.\n')
		print('Will be looking for:\n Family: %s\n Organism: %s'%(fam,org))
		react= input('Enter "y" to submit, "n" to enter again, or any other key to choose the other type of database.\n')
		if react== "y":
			print("Submitted")
			#Specify the searching terms
			if fam != 'n':
				FAM= str(fam)
			else:
				FAM= '' 
			if org != 'n':
				ORG= ' AND %s [Organism]'%(org)
			else:
				ORG= ''
#Make bash commands for blastp
			search_data= "esearch -db {} -query '{}{} NOT PARTIAL' | efetch -format fasta > data.fasta".format(TYP,FAM,ORG)
			make_database= "makeblastdb in data.fasta -dbtype {} -out database".format(TYPE)
			print("This may take a while...")
			subprocess.call(search_data, shell=True))
			print("The archived data is kept in 'data.fasta'.\n")
			subprocess.call(make_database, shell=True)
			print("Database made.")	
			break
		elif react== "n"
			print("Decided to enter again.")
		else:
			break   #Returning to the starting loop
	return TYPE

def blast():
#Input the query's name
	while True:
		name= input("Please enter the file name of your query.\n")
		print("This is the input name: %s")%(str(name))
		outmane= input("Please name the outpt file.\n")
		print("The output file will be named %s")%(str(outname))
		react= ("\nPress 'y' to confirm, or any other key to enter again.\n")
		if react== 'y'
			print("Confirmed")
			break
		else:
			print("Decided to enter again.")
	react1= input("Please specify the type of your query.\nEnter 'p' for protein, or 'n' for nucleotide.\n")
	if TYPE=='prot': #The type of the database is protein

		if react1 == 'p':
			try:
				command= "blastp -db database -query {} > {}".format(name,outname)
				subprocess.call(command,shell=True)
				print("Finished, the output is saved in the current directory.")
				break
			except:
				print("Some error happend.")
		if react1 == 'n':
			try:
				command= "blastx -db database -query {} > {}".format(name,outname)
				subprocess.call(command,shell=True)
				print("Finished, the output is saved in the current directory.")
				break
	else:  #The type of database is nucleotide
		if react1 == 'p':
                        try:
                                command= "tblastn -db database -query {} > {}".format(name,outname) 
                                subprocess.call(command,shell=True)
                                print("Finished, the output is saved in the current directory.")
				break
                        except:
                                print("Some error happened.")
                if react1 == 'n':
                        try:
                                command= "blastn -db database -query {} > {}".format(name,outname)
                                subprocess.call(command,shell=True)
                                print("Finished, the output is saved in the current directory.")
				break
			except:
				print("Some error happened.")

# The main proces
while True:
	TYPE=''
	print("***This is the start menu***")
	print("Please make sure the query of interest is kept in the current directory.")
	react= input("Enter 'n' to start a new analysis, or enter any other keys to leave.")
	if react== "n":
		try:
			database()
			blast()
		except:
			print("Some error happened.")
	else:
		break
