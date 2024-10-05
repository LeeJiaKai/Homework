name = input()
alphabet_list = 26*[0]
for alphabet in name:
    alphabet_list[ord(alphabet) - ord('a')] = 1
if alphabet_list.count(1) %2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")