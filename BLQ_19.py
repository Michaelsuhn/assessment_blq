'''
“Sphinx of black quartz, judge my vow”
“Brawny gods just flocked up to quiz and vex him”
“Check back tomorrow; I will see if the book has arrived.”
'''
import regex as re
import string


input = 'Check back tomorrow; I will see if the book has arrived.'
inputkalimat = input.translate(str.maketrans('', '', string.punctuation))
edit = inputkalimat.replace(' ','').lower()
#print(edit)

length = len(edit)
result_abjad = []


for i in range(length):
    if edit[i] not in result_abjad:
        result_abjad.append(edit[i])
       
print(sorted(result_abjad))
#print(len(result_abjad))
if len(result_abjad) == 26:
    print('Pangram')
else:
    print('Bukan Pangram')