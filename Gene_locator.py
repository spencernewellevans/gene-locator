#FIND PATTERN FUNCTION
def FindPattern(pattern, search_text, start_loc, stop_loc, increment, threshold):

    pattern_len = len(pattern)
    text_len = len(search_text)

    for i in range(start_loc, stop_loc + 1, increment):
        count = 0
        j = i
        for k in range(0, pattern_len):
            if search_text[j] == pattern[k]:
                count = count + 1
            j = j + 1
        if count >= threshold:
            return i
    return -1


# SEQUENCE PREPARATION
# User inputs path to text file containing a DNA sequence.
DNAsequence = input("\nDNA sequence file path: ")
# Sample DNA sequence.
#f1 = open("../DNAsequences/AF516335.txt")
f1 = open(DNAsequence)
# ONLY USE THIS LINE IF DNA TEXT FILE IS IN 'FASTA' FORMAT TO DISCARD FIRST LINE OF TEXT.
# If the sequence begins at the start of the text file this line should be commented out.
line1 = f1.readline()
print(line1)
seq = f1.read()
len1 = len(seq)
# Removes newline characters for continuous reading.
seq = seq.replace('\n', '')
len1 = len(seq)
print('length of sequence = ', len1)


i = 0
while i < len1 - 102:
    # Find first start codon.
    # Only Searches until length of sequence - 103 because the minimum open reading frame length is 100.
    atg = FindPattern('ATG', seq, i, len1 - 103, 1, 3)
    # If no start codon is found the program terminates. There is no gene in this DNA sequence.
    if atg == -1:
        break
    i = atg + 3
    stops = []
    # Find TAG stop codon.
    stop1 = FindPattern('TAG', seq, i, len1 - 3, 3, 3)
    if stop1 > -1:
        stops.append(stop1)
        print('TAG codon found at:', stop1)
    # Find TGA stop codon.
    stop2 = FindPattern('TGA', seq, i, len1 - 3, 3, 3)
    if stop2 > -1:
        stops.append(stop2)
        print('TGA codon found at:', stop2)
    # Find TAA stop codon.
    stop3 = FindPattern('TAA', seq, i, len1 - 3, 3, 3)
    if stop3 > -1:
        stops.append(stop3)
        print('TAA codon found at:', stop3)
    # If no stop codons are found for this reference frame continue to look for next ATG.
    if len(stops) == 0:
        continue
    firststop = min(stops)
    # Check the length of the open reading frame.
    # If the open reading frame is shorter than 100 bases it is invalid.
    # Loop continues to search for next start codon.
    ORFlen = firststop - atg
    if ORFlen < 99:
        continue
    print('Open reading frame found at: ', atg, '\nLength of ORF is: ', ORFlen)
    # Seaches for Shine-Dalgarno sequence before ORF
    # Threshold argument for FindPattern is 5 because AGGAGG is 6 char long but only needs 5/6 to match
    # Start is atg - 13 because SD is 6 bases long and must be maxmimum 7 bases before ATG
    aggagg = FindPattern('AGGAGG', seq, atg - 13, atg - 9, 1, 5)
    # If no SD is found program continue searching
    if aggagg == -1:
        print('No AGGAGG found... searching for new ORF')
        continue
    # Valid ORF with SD found.
    if aggagg > -1:
        print('AGGAGG found at: ', aggagg)
        break

# Located Gene Info
print('\n\nGENE FOUND\n==========')
print(seq[aggagg : firststop + 3])
print('\nShine-Dalgarno found at: ', aggagg)
print('Start codon found at: ', atg)
print('Stop codon found at: ', firststop)
print('Length of the gene is: ', ORFlen, '\n')
input('Press Enter to Exit')
