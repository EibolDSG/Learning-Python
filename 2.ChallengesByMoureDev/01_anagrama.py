"""
Challenge Nº1 by MoureDev - ANAGRAMA
"""

def anagrama(wordOne, wordTwo):
    if wordOne == wordTwo:
        anagrama = False
    elif sorted(str.lower(wordOne)) == sorted(str.lower(wordTwo)):
        anagrama = True
    else:
        anagrama = False
    return(anagrama)

print(anagrama("dEl", "led"))
