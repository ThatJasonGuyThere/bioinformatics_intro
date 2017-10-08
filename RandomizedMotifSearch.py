import random

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs

def RandomMotifs(Dna, k, t):
    #k = random.randint(1, len(Dna[0]))
    t = len(Dna)
    rndstring = []
    for i in range(t):
        j = random.randint(1, len(Dna[i]))
        while ((j + k) > len(Dna[0])):
            j = random.randint(1, len(Dna[i]))
        rndstring.append(Dna[i][j:j+k])        
    return rndstring

def Motifs(Profile, Dna):
    motifs= []
    for i in range(len(Dna)):
        motifs.append(ProfileMostProbablePattern(Dna[i], len(Profile["A"]), Profile))
    return motifs    

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p*Profile[Text[i]][i]
    return p

def ProfileMostProbablePattern(Text, k, Profile):
    currentP = 0
    newP = 0
    currentText = Text[0:k]
    for i in range(len(Text)-k+1):
        newP = Pr(Text[i:i+k], Profile)
        if (newP > currentP):
            currentP = newP
            currentText = Text[i:i+k]
    return currentText


def Count(Motifs):
    count = {} # initializing the count dictionary
    
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1 #divide by t for Profile problem
    
    return count

def CountWithPseudocounts(Motifs):
    count = Count(Motifs)
    k = len(Motifs[0])
    for symbol in "ACGT":
        for j in range(k):
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    profile = CountWithPseudocounts(Motifs)
    t = profile["A"][0] + profile["T"][0] + profile["C"][0]+ profile["G"][0]
    k = len(Motifs[0])
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] = profile[symbol][j] / t
    
    return profile

def Consensus(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    
    return consensus

def Score(Motifs):
    score = 0
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            if Motifs[i][j] != Consensus(Motifs)[j]:
                score += 1            
    return score

profile = { 
'A': [0.8, 0.0, 0.0, 0.2 ],
'C': [ 0.0, 0.6, 0.2, 0.0], 
'G': [ 0.2 ,0.2 ,0.8, 0.0], 
'T': [ 0.0, 0.2, 0.0, 0.8]
}   

dna = [
'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'
]

#k = random.randint(1, len(dna[0]))
k = 8
t = 5

print(RandomMotifs(dna, k, t))



