from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

dnaseq = Seq("AGTACTAGAGCATTCTATGGAG", generic_dna)

gencode = {
      'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
      'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
      'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
      'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
      'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
      'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
      'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
      'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
      'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
      'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
      'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
      'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
      'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
      'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
      'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
      'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def translate_frameshifted(sequence):
      translate = ''.join([gencode.get(sequence[3*i:3*i+3],'X') for i in range(len(sequence)//3)])
      return translate

print(translate_frameshifted(dnaseq[0:]))    # first frame
print(translate_frameshifted(dnaseq[1:]))   # second frame
print(translate_frameshifted(dnaseq[2:]))   # third frame
print(translate_frameshifted(dnaseq[::-1][0:]))    # first frame from end
print(translate_frameshifted(dnaseq[::-1][1:]))    # second frame from end
print(translate_frameshifted(dnaseq[::-1][2:]))    # third frame from end

def lensort(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            if len(a[i]) > len(a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a
print(lensort([translate_frameshifted(dnaseq[0:]), translate_frameshifted(dnaseq[1:]), translate_frameshifted(dnaseq[2:]), translate_frameshifted(dnaseq[::-1][0:]), translate_frameshifted(dnaseq[::-1][1:]), translate_frameshifted(dnaseq[::-1][2:])]))











