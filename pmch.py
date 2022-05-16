import math

RNA="""AUGAUCUUAGUUACCCGACAUCGAAGGGCGAAGCCGUUCUGUGAGCAAUGCGCCCACGGC
CAUUGCCUGGUA

"""

AU=RNA.count("A")
GC=RNA.count("G")

matchings =math.factorial(AU)*math.factorial(GC) 
print(matchings)
