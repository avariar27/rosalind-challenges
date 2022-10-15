#  This function solves the Rosalind problem described here, https://rosalind.info/problems/prot/
#
#  https://www.nature.com/scitable/topicpage/translation-dna-to-mrna-to-protein-393/
def translate_rna_to_protein(rna):
    rna = rna.upper()

    # The RNA encodes the amino acids of a peptide as a sequence of codons, with each codon consisting of three nucleotides, chosen from the alphabet set, {'U','C', 'A', 'G'}.
    # The lines below create a dictionary, codon_to_aa, mapping codons to amino acids where each amino acid is identified by its one-letter abbreviation (for example, R = arginine).
    # The codon AUG signals the start of translation within a nucleotide sequence as well as coding for the amino acid methionine.
    # The single asterisk character (*) is a stop codon, signalling termination of the RNA translation.
    bases = ['U', 'C', 'A', 'G']
    codons = [x + y + z for x in bases for y in bases for z in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_to_aa = dict(zip(codons, amino_acids))
    #print(codon_to_aa)

    n = 3
    protein = ''
    # The for loop below uses List Comprehension, meaing it converts the input sequence into
    # a list of elements each containing 3 symbols.
    for codon in [rna[m:m + n] for m in range(0, len(rna), n) ]:
        aa = codon_to_aa.get(codon, '-')
        if aa == '*':
            break
        protein += aa

    return protein