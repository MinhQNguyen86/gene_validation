"""CSCA08 Assignment 0, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Minh Nguyen
 Date: 10/20/17
"""


def split_input(dna_seq):
    '''(str) -> list
    Given a string of a DNA sequence, returns a three
    element list with the upstream data, the gene, and
    the downstream data. An empty string will be returned
    if no gene is found.
    REQ: dna_seq is a valid DNA sequence containing only
    the letters 'A', 'G', 'C', and 'T'
    >>> split_input("AAATGCATGT")
    ['AA', 'ATGC', 'ATGT']
    >>> split_input("ATGA")
    ['', 'ATGA', '']
    '''

    # Split the string at most into 3 parts
    # the length of the resulting list
    # determines what is the upstream, gene,
    # and downstream

    temp = dna_seq.replace(' ', '').split('ATG', 2)
    if len(temp) == 1:
        upstream = temp[0]
        gene = ''
        downstream = ''
    elif len(temp) == 2:
        upstream = temp[0]
        gene = 'ATG' + temp[1]
        downstream = ''
    else:
        upstream = temp[0]
        gene = 'ATG' + temp[1]
        downstream = 'ATG' + temp[2]

    # Returns the list of upstream, gene, and downstream

    gene_list = [upstream, gene, downstream]
    return gene_list


def get_gene(dna_seq):
    '''(str) -> str
    Takes in a string of dna sequence, and if
    a gene exists, return that gene.
    A string, "ERROR" is returned elsewise.
    REQ: dna_seq is one string containing
    'A', 'T', 'C', and 'G', without any spaces.
    >>> get_gene("AATCATGCAT")
    'ATGCAT'
    >>> get_gene("")
    'ERROR'
    '''

    # Get the gene, and if it's not empty,
    # the gene is valid

    gene = split_input(dna_seq.replace(' ', ''))[1]
    gene_str = 'ERROR'
    if len(gene) != 0:
        gene_str = gene
    return gene_str


def validate_gene(str_rep_gene):
    '''(str) -> bool
    Given a string representation of a gene,
    checks if the gene is valid. Validity
    means all the following critera are met:
    i) it must start with "ATG"
    ii) it must contain one codon after "ATG"
    iii) its length must be a multiple of three
    iv) it cannot contain four back to back
    letters that are identical
    REQ: str_rep_gene contains only 'A', 'T',
    'C' and 'G' or 'ERROR'
    >>> validate_gene("ATGAAGTTC")
    True
    >>> validate_gene("ATGAA")
    False
    '''

    # Create variables for consecutive nucleotides

    a = 'AAAA'
    t = 'TTTT'
    c = 'CCCC'
    g = 'GGGG'

    # Create a variable for validity,
    # arbitrary assigning it to True

    validity = True

    # Remove all spaces from the string

    str_rep_gene = str_rep_gene.replace(' ', '')

    # Check if the str_rep_gene starts
    # with 'ATG'

    if str_rep_gene[:3] != 'ATG':
        validity = False

    # Check if there's at least one codon
    # after the start codon

    if len(str_rep_gene) < 6:
        validity = False

    # Check if str_rep_gene contains only
    # full codons

    if len(str_rep_gene) % 3 != 0:
        validity = False

    # Check if there are four consecutive,
    # identical nucleotides

    if (a or t or c or g) in str_rep_gene:
        validity = False

    # return the validity of the gene

    return validity


def is_palindromic(str_rep_gene):
    '''(str) -> bool
    Given a gene in the form of a string, checks
    if that string is the same forwards and
    backwards.
    REQ: str_rep_gene only contains 'A', 'T',
    'C', and 'G'
    REQ: str_rep_gene is not empty
    >>> is_palindromic("ATGCAAG")
    False
    >>> is_palindromic("ATGGTA")
    True
    '''

    # Remove all spaces from gene

    str_rep_gene = str_rep_gene.replace(' ', '')

    # Checks if the reverse of the gene is
    # equal to the normal string

    is_pal = False
    if str_rep_gene == str_rep_gene[::-1]:
        is_pal = True
    return is_pal


def evaluate_sequence(dna_seq):
    '''(str) -> str
    Takes in a DNA sequence and returns either:
    i) No Gene Found
    ii) Invalid Gene
    iii) Valid Gene Found
    iv) Valid Palindromic Gene Found
    depending on the results of the other
    functions
    REQ: dna_seq only contains 'A', 'T',
    'C', and 'G'
    >>> evaluate_sequence("ATGAAAGTA")
    'Valid Palindromic Gene Found'
    '''

    message = ''
    gene = get_gene(dna_seq)

    # Check if a gene exists, and if it does,
    # then check whether or not it's a valid
    # gene, an invalid gene, or a valid
    # palindromic gene

    if gene != 'ERROR':
        if validate_gene(gene):
            if is_palindromic(gene):
                message = 'Valid Palindromic Gene Found'
            else:
                message = 'Valid Gene Found'
        else:
            message = 'Invalid Gene'
    else:
        message = 'No Gene Found'
    return message
