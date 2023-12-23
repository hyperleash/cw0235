import sys
import random
from Bio import SeqIO

"""
usage: python select_ids.py INPUT.fasta 2000
"""

def read_input(file):
    """
    Function reads a fasta formatted file of protein sequences
    """
    # print("READING FASTA FILES")
    ids = []
    for record in SeqIO.parse(file, "fasta"):
        ids.append(record.id)
    return(ids)


if __name__ == "__main__":
    ids = read_input(sys.argv[1])
    # print(ids)
    rand_list = random.sample(ids, int(sys.argv[2]))
    for id in rand_list:
        print(id)