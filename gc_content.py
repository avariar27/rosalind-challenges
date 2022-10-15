from typing import List,Tuple
from Bio import SeqIO

# This function is a solution to the GC Content problem described in  https://rosalind.info/problems/gc/
#
# The GC-content of a DNA sequence is the percentage of symbols in the sequence that are either 'C' or 'G'. For example, the GC-content of
# the sequence "AGCTATAT" is 0.25%.
#
# This function uses the genome sequence from the ls_orchid.fasta file, obtained from the NCBI Sequence database.
# See this article for more details on the FASTA format.
#   https://rpubs.com/ginawxng/824095
#
def find_dna_with_max_gc_content():
    record_id_gc_content: List[Tuple[float, str]] = []

    # Print out all the records in the fasta file
    # for dna_seq_record in SeqIO.parse("inputs/ls_orchid.fasta", "fasta"):
    #     print('ID -> ',dna_seq_record.id)
    #     print('Length -> ',len(dna_seq_record))
    #     print("Name: %s" % dna_seq_record.name)
    #     print("Description: %s" % dna_seq_record.description)
    #     print("Annotations: %s" % dna_seq_record.annotations)
    #     print("Sequence Record: %s" % dna_seq_record.seq)

    #
    for dna_record in SeqIO.parse("inputs/ls_orchid.fasta", "fasta"):
        gc = 0
        for symbol in dna_record.seq.upper():
            if symbol in ('C','G'):
                gc += 1

        percentage = (gc/len(dna_record)) * 100
        record_id_gc_content.append((percentage,dna_record.id))

        dna_with_max_gc_content = max(record_id_gc_content)

    return dna_with_max_gc_content
