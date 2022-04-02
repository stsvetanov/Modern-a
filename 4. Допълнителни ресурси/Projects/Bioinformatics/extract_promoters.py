from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

gbk_filename = "D:\Projects\InsilicoKDD\Exec\DataSets\Escherichia-coli-str.-K-12.gbk"

mito_frags = []
promoter_start = 35
promoter_end = 0
ttgaca_start = 35
ttgaca_end = 29
tataat_start = 10
tataat_end = 4
i = 0

promoter_type = input('Enter promoter type : ')
promoter_type = int(promoter_type)
if promoter_type == 1:
    fragmet_start = promoter_start
    frament_end = promoter_end
    faa_filename = "promoters.fasta"
    output_handle = open("promoters.txt", "w")
elif promoter_type == 2:
    fragmet_start = ttgaca_start
    frament_end = ttgaca_end
    faa_filename = "ttgaca.fasta"
    output_handle = open("ttgaca.txt", "w")
elif promoter_type == 3:
    fragmet_start = tataat_start
    frament_end = tataat_end
    faa_filename = "tataat.fasta"
    output_handle = open("tataat.txt", "w")
else: print("Must be 1, 2 or 3!")

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
print ("Done")