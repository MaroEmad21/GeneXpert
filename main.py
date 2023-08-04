"""
    importing  libraries needed to do the tool
    this is a simple software that could help you to get better info  and data 
    that could be used In Bioinformatics
    this is Version 1.0  
"""
import random 
from Bio import SeqIO 
from Bio.Seq import Seq 
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import *
from funcs import *   # to use functions made that not exist in Biopython

Nucleotides= ["A","C","G","T"]
# this is used as debugger to  the tool
randomStr=''.join([random.choice(Nucleotides)
                   for nuc in range(21)])



# First Question
answer = input( 
               """which sequece you will type?
(Dna or 1)
(Rna or 2)  """)

if answer.upper() in ["DNA","1"]:
    parse_or_seq = input("file or seq: ")
    """user enters file path and file type manually but used once
                    (will be updated)""" 
    if parse_or_seq.lower() in ["file","1"]:
        #file_path= input("file name: ")
        #file_type= input("file type: ")
        for record in SeqIO.parse(f"sequence.fasta", "fasta"):
            seq = record.seq
            ids = record.id
            print(f"id = {record.description} \n your sequence is: {seq}")
    # the second choice will be removed later
    elif parse_or_seq.lower() in ["seq","2"]:
        sequence = randomStr
        seq = Seq(sequence)
        print(f"sequence is: {seq}")
    else:
        print("Choose well")    
    # this loops to get more info from the same file
    while True:
        next_step = input(
    """what's next: 
    1) transcribe   
    2) translate  
    3)complement seq(comp) 
    4)reverse_complement(rev-comp) 
    5)reverse_complement_rna(5) 
    6)GC content(%) 
    7)Molecular weight(mw)
    8)six frame translation
    9)Alignment
    10)phylognetic tree
    __stop or x:  """)
        # transcription
        if next_step.lower() in  ['transcribe' ,'1']:
            print(f"m-RNA is: {seq.transcribe()}")
            records= SeqRecord(seq.transcribe(),id='',name='transcribe',description=f'{record.description}')
            name = input("name of file:")
            with open(name +".fasta", "w") as handle:
                SeqIO.write(records, handle, "fasta")
        # translate        
        elif next_step.lower() in ['translate','2']:
                print(f"Amino acid seq: {seq.translate()}") 
                records= SeqRecord(seq.translate(),id='',name='translate',description=f'{record.description}')
                name = input("name of file:")
                with open(name +".fasta", "w") as handle:
                   SeqIO.write(records, handle, "fasta")
        # complementary sequence           
        elif   next_step.lower() in ['comp','3'] :
                print(f"complement seq: {seq.complement()}")
                records= SeqRecord(seq.complement(),id='',name='complementary sequence',description=f'{record.description}')
                name = input("name of file:")
                with open(name +".fasta", "w") as handle:
                   SeqIO.write(records, handle, "fasta")  
        #reverse complementary            
        elif next_step.lower() in ['rev-comp','4']:
            print(f"{seq.reverse_complement()}")
            records= SeqRecord(seq.reverse_complement(),id='',name='reverse complementary sequence',description=f'{record.description}')
            name = input("name of file:")
            with open(name +".fasta", "w") as handle:
                   SeqIO.write(records, handle, "fasta") 
        # Rna complementary sequence
        elif next_step.lower() in ['comp_rna','5']:
            print(f"complment rna:{seq.complement_rna()}")   
            records= SeqRecord(seq.complement_rna(),id='',name='reverse complementary_rna sequence',description=f'{record.description}')
            name = input("name of file:")
            with open(name +".fasta", "w") as handle:
                SeqIO.write(records, handle, "fasta")
        #GC content        
        elif next_step.lower() in  ['gc','6']:
            print(f"GC %: {round(gc_fraction(seq) * 100) }")
        # molecular weight    
        elif next_step.lower() in ['mw', '7']:
            print(f'Moleceular weight: {molecular_weight(seq)}')
        # ORFs    
        elif next_step.lower() in ['sixframe', '8']:
            print(f'{six_frame_translations(seq) }')     
            name = input("name of file:")
            test = open(name+".txt",'w')
            test.write(str(six_frame_translations(seq) ))
            test.close()
        # making alignment    
        elif next_step.lower() in ['al', '9']:
            make_alignment(seq)
        # makes and reads phylogenetic tree    
        elif next_step.lower() in ['phylo', '10']:
            make_phylo(seq,ids) 
        # to break the loop   
        elif next_step.lower() in  ['stop' ,'x']:
            break

    """
        this makes nearly same things as in Dna 
        but for Rna Except back transcribe
    """

elif answer.upper() in ["rna","2"]:
    parse_or_seq = input("file or seq: ")
    """user enters file path and file type manually but used once
                    (will be updated)""" 
    if parse_or_seq.lower() in ["file","1"]:
        #file_path= input("file name: ")
        #file_type= input("file type: ")
        for record in SeqIO.parse(f"sequence.fasta", "fasta"):
            seq = record.seq
            ids = record.id
            print(f"id = {record.description} \n your sequence is: {seq}")
    # the second choice will be removed later
    elif parse_or_seq.lower() in ["seq","2"]:
        sequence = randomStr
        seq = Seq(sequence)
        print(f"sequence is: {seq}")
    else:
        print("Choose well")    
    # this loops to get more info from the same file
    while True:
        next_step = input(
    """what's next: 
    1)Back transcribe   
    2)translate  
    3)complement seq(comp) 
    4)reverse_complement(rev-comp) 
    5)reverse_complement_rna(5) 
    6)GC content(%) 
    7)Molecular weight(mw)
    8)six frame translation
    9)Alignment
    10)phylognetic tree
    __stop or x:  """)
        # transcription
        if next_step.lower() in  ['transcribe' ,'1']:
            print(f"m-RNA is: {seq.back_transcribe()}")
            records= SeqRecord(seq.back_transcribe(),id='',name='back_transcribe',description=f'{record.description}')
            name = input("name of file:")
            with open(name +".fasta", "w") as handle:
                SeqIO.write(records, handle, "fasta")
        # translate        
        elif next_step.lower() in ['translate','2']:
                print(f"Amino acid seq: {seq.translate()}") 
                records= SeqRecord(seq.translate(),id='',name='translate',description=f'{record.description}')
                name = input("name of file:")
                with open(name +".fasta", "w") as handle:
                   SeqIO.write(records, handle, "fasta")
        # complementary sequence           
        elif   next_step.lower() in ['comp','3'] :
                print(f"complement seq: {seq.complement()}")
                records= SeqRecord(seq.complement(),id='',name='complementary sequence',description=f'{record.description}')
                name = input("name of file:")
                with open(name +".fasta", "w") as handle:
                   SeqIO.write(records, handle, "fasta")  
        #reverse complementary            
        elif next_step.lower() in ['rev-comp','4']:
            print(f"{seq.reverse_complement()}")
            records= SeqRecord(seq.reverse_complement(),id='',name='reverse complementary sequence',description=f'{record.description}')
            name = input("name of file:")
            with open(name +".fasta", "w") as handle:
                   SeqIO.write(records, handle, "fasta") 
        # Rna complementary sequence
        elif next_step.lower() in ['comp_rna','5']:
            print(f"complment rna:{seq.complement_rna()}")   
            records= SeqRecord(seq.complement_rna(),id='',name='reverse complementary_rna sequence',description=f'{record.description}')
            name = input("name of file:")
            with open(name +".fasta", "w") as handle:
                SeqIO.write(records, handle, "fasta")
        #GC content        
        elif next_step.lower() in  ['gc','6']:
            print(f"GC %: {round(gc_fraction(seq) * 100) }")
        # molecular weight    
        elif next_step.lower() in ['mw', '7']:
            print(f'Moleceular weight: {molecular_weight(seq)}')
        # ORFs    
        elif next_step.lower() in ['sixframe', '8']:
            print(f'{six_frame_translations(seq) }')     
            name = input("name of file:")
            test = open(name+".txt",'w')
            test.write(str(six_frame_translations(seq) ))
            test.close()
        # making alignment    
        elif next_step.lower() in ['al', '9']:
            make_alignment(seq)
        # makes and reads phylogenetic tree    
        elif next_step.lower() in ['phylo', '10']:
            make_phylo(seq,ids) 
        # to break the loop   
        elif next_step.lower() in  ['stop' ,'x']:
            break
else:
    pass        



