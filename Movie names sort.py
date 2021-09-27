movi = input("Input the movies: \n")
movies = movi.split(',')

fixedMovie = []

for m in movies:
    if m not in fixedMovie:
        fixedMovie.append(m)
        
        
fixedMovie.sort()

print("\n")

exceptions = ['the', 'a', 'is', 'an', 'of', 'at', 'The', 'A', 'Is','An','Of', 'At', 'And', 'If', 'if']

fixedMovie = [fixedM.title() for fixedM in fixedMovie]

fixedMovie2 = []


for i in range(len(fixedMovie)):
    fixedMovie2.append(fixedMovie[i].split())
                
        
for i in range(len(fixedMovie2)):
    flag = 0
    for k in range(len(fixedMovie2[i])):
        if fixedMovie2[i][k] in exceptions and flag == 1:
            fixedMovie2[i][k] = fixedMovie2[i][k].lower()
        flag = 1

fixedMovie3 = []

for i in range(len(fixedMovie2)):
    fixedMovie3.append(' '.join(fixedMovie2[i]))
    

print(fixedMovie3)