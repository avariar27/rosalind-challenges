
# This function is a solution to the Hamming Distance problem described in https://rosalind.info/problems/hamm/
#
# The Hamming distance is a measure of dissimilarity between 2 DNA sequences. It is defined as the number of positions that two DNA
# sequences of the same length differ. It can also be defined as the minimum number of symbol substitutions required to transform
# one DNA sequence to the other.

def find_hamming_distance(seq1, seq2):
    hamming_dist = 0

    # The zip() function takes a list of lists (iterables) and returns a zipped iterable object (a list of tuples), where the first items in each passed
    # iterator are paired together, and then the second items in each passed iterator are paired together and so on.
    # If the passed iterators have different lengths, then the iterator with the least length determines the length of the zipped iterator.
    list_tuples = zip(seq1, seq2)

    for (p, q) in list_tuples:
        if p != q:
            hamming_dist += 1
    return hamming_dist