def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
            
        if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs
                
    return BestMotifs

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

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
Dna = ["GGCGTTCAGGCA","AAGAATCAGTCA","CAAGGAGTTCGC","CACGTCAATCAC","CAATAATATTCG"]
k = 3
t = len(Dna)
Motifs = GreedyMotifSearchWithPseudocounts(Dna, k , t)
print(Motifs)