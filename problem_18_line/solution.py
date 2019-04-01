genome = input()
print (((genome.lower().count('c') + genome.lower().count('g'))/len(genome))*100)