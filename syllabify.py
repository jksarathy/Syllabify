#Jayshree Sarathy
#jayshree.sarathy@yale.edu
#using Python 3

import sys

#dictionary encoding the sonority level of each phoneme
son = { 'AA': 4, 'AE' : 4, 'AH' : 4, 'AO' : 4, 'AW' : 4, 'AY' : 4,
             'B'  : 0, 'CH' : 0, 'D' : 0, 'DH' : 0, 'EH' : 4, 'ER' : 4,
             'EY' : 4, 'F': 0, 'G': 0, 'HH': 0, 'IH': 4, 'IY': 4, 'JH': 0,
             'K': 0, 'L': 2, 'M': 1, 'N': 1, 'NG': 1, 'OW': 4, 'OY': 4,
             'P': 0, 'R': 2, 'S': 0, 'SH': 0, 'T': 0, 'TH': 0, 'UH': 4,
             'UW': 4, 'V': 0, 'W': 3, 'Y': 3, 'Z': 0, 'ZH': 0}

#create empty dictionary to fill with syllable types
types = {}

#open file
file = open(sys.argv[1])

#read through each line of file
for line in file.readlines():
    words = line.split()
    words.reverse()

    vowel = -1
    plus = -1
    i = 0
    
    #iterate through each position of the word list. Using a while loop accounts for changing length of list.
    while i < len(words)-1:
        current = words[i]
        after = words[i+1]

        #check if the current phoneme is a vowel and mark the position
        if current in son and current != "+" and son[current] == 4:
            vowel = i
            
            #two vowels can't be in the same syllable
            if after in son and son[after] == 4:
                words.insert(i + 1, "+")
                plus = i + 1
                i +=1          

        #check if the current phenome is a consonant in the onset of the syllable
        elif current in son and current != "+" and son[current] < 4 and vowel > plus:

            #check if the following syllable isnt S and is a vowel or a valid consonant according to the rule of onsets
            if after in son and after != "S" and (son[after] == 4 or (son[after] < 4 and son[current] - son[after] < 2)):
                words.insert(i + 1, "+")
                plus = i+1
                i +=1

        #increment i
        i +=1
                                                
    words.reverse()

    #print list of words with spaces in between
    final = ' '.join(words)
    print(final)

    #iterate through syllables separated by plus
    for syllable in final.split("+"):
        
        s = ""

        #iterate through individual phenomes
        for phoneme in syllable.split():

            #build string of syllable type
            if phoneme in son and son[phoneme] == 4:
                s+= "V"
            elif phoneme in son and 0 <= son[phoneme] < 4:
                s+= "C"

        #if a string was built, increment its counter in types or add it to types
        if s != "":
            types[s] = types.get(s,0.0) + 1.0

#print out the syllable types and relative frequencies from types
for stype, count in sorted(types.items()):
    print("Frequency of {0} : {1:.2f}".format(stype, 100.0 *count/sum(types.values())))

        


        
        

 
            
                
                
            
        
