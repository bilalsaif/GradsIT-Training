x = input("Enter a sentence : ")
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
vowel = []

for i in x:
    if (i == "a"):
        vowel.append('a')
        count_a = count_a + 1
    elif (i == "e"):
        vowel.append('e')
        count_e = count_e + 1
    elif (i == "i"):
        vowel.append('i')
        count_i = count_i + 1
    elif (i == "o"):
        vowel.append('o')
        count_o = count_o + 1
    elif (i == "u"):
        vowel.append('u')
        count_u = count_u + 1
    elif (i == "A"):
        vowel.append('a')
        count_a = count_a + 1
    elif (i == "E"):
        vowel.append('e')
        count_e = count_e + 1
    elif (i == "I"):
        vowel.append('i')
        count_i = count_i + 1
    elif (i == "O"):
        vowel.append('o')
        count_o = count_o + 1
    elif (i == "U"):
        vowel.append('u')
        count_u = count_u + 1

dict={'a':count_a,'e':count_e,'i':count_i,'o':count_o,'u':count_u}
print("All vowels present in sentence",set(vowel))
print("Total no. for each vowel ",dict)