from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

gbk_filename = "D:\Projects\InsilicoKDD\Exec\DataSets\Escherichia-coli-str.-K-12.gbk"

mito_frags = []
promoter_start = 40
promoter_end = 0
fragmet_start = promoter_start
frament_end = promoter_end
output_handle = open("40_nuc.txt", "w")
faa_filename = open("40_nuc.fasta", "w")
i = 0

for seq_record in SeqIO.parse(gbk_filename, "genbank"):
    print("Dealing with GenBank record %s" % seq_record.id)
    for seq_feature in seq_record.features:
        if seq_feature.type == "gene":
            mito_frag = seq_record.seq[seq_feature.location.start - fragmet_start: seq_feature.location.start - frament_end]
            output_handle.write("%s\n" % (mito_frag)) # write to plane text file

            record = SeqRecord(mito_frag, 'fragment_%i' % (i+1), '', '')
            mito_frags.append(record)
            i = i + 1

SeqIO.write(mito_frags, faa_filename, "fasta") # write to fasta file
output_handle.close()
print("Done")
