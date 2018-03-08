# gene-locator

This python script searches a DNA sequence for possible gene sequences.
The program requires an the DNA sequence to be in a text file in either FASTA format or as a plain sequence.
This text file is given as a user input after the program has been run.

Gene Requirements:
- Start codon (ATG)
- Stop codon (TAG, TGA, TAA) following a start codons
- Open reading frame of at least 100
- Shine-Dalgarno sequence (AGGAGG or similar) located within 7 bases before the start codon

Output:
- Full gene starting with Shine-Dalgarno sequence
- Location of the Shine-Dalgarno sequence
- Location of the start codons
- Location of the stop codons
- Length of the gene

