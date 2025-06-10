# Get the full form of NASA from Dictionary

# My Knowledge Dictionary
kd = {
    'R' : "Russia",
    'E':'European',
    'C': "Catherine",
    'S': ['Space','Space','Samantha'], # Nearest occurence is at 0th index
    'U':'Ursula',
    'A': ['Aeronautics', 'Administration', 'Agency'],
    'N': "National",  
}


# Split the letters and get the names then how to get from array??
# 

freq = {}
acronym = 'NASAESA'
abbr = []

for ltr in acronym:
    freq[ltr] = freq.get(ltr, 0) + 1
    if ltr in kd:
    

        # Get the order of count
        if type(kd[ltr]) == list:
            count = freq[ltr] - 1
            abbr.append(kd[ltr][count])
        else:
            abbr.append(kd[ltr])

print(abbr)

