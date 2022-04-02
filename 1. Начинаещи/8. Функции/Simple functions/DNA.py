
seq="CTTATTATGTTAGACTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACA"
seq2="TTCCCAGGTAACAAACCAACCAACTTAAACGAACATCGATCTCTTGTAGATCTGTTCTCT"
rev="GGATCTGAAAACTATGTCAGGGTAATAAACACCACGTGTGAAAGAATTAGTGTATGCAGGGGGTAATTGAGTT"
joi="CTTATTATGTTAGACTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACAGGATCTGAAAACTATGTCAGGGTAATAAACACCACGTGTGAAAGAATTAGTGTATGCAGGGGGTAATTGAGTT"
def reverce(seq):
    rev_seq=seq[::-1]
    return rev_seq
def complement(seq):
    d={'A':'T','T':'A','C':'G','G':'C'}
    compl_seq=""
    for s in seq:
        compl_seq+=d[s]
    return compl_seq
def rev_compl(seq):
    rev_comp=reverce(seq)
    rev_comp=complement(rev_comp)
    return rev_comp

print(seq)
print(reverce(seq))
print(complement(seq))
print(rev_compl(seq))
print(rev)


