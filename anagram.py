def are_anagrams(word1: str, word2: str) -> bool:
    return sorted(word1.lower()) == sorted(word2.lower())

if __name__ == "__main__":
    count = int(input("Neçə söz cütü yoxlamaq istəyirsən? "))

    for _ in range(count):
        w1 = input("Birinci söz: ")
        w2 = input("İkinci söz: ")
        if are_anagrams(w1, w2):
            print(f"{w1} və {w2} → Anagramdır ✅")
        else:
            print(f"{w1} və {w2} → Anagram deyil ❌")
