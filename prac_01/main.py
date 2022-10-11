# names = ["mason","matt","eric"]
# number = int(input(f"enter a number, up to {len(names)}: "))
#try:
#     print(names[number - 1])
# except IndexError:
#     print("invalid number")

#from operator import itemgetter

#score_pairs = [['derek',7], ['carrie', 8], ['bob', 6]]
#new_score = input("please enter a name and a score: ").split()
#new_score[1] = int(new_score[1])
#score_pairs.append(new_score)
#score_pairs.sort(key = itemgetter(1), reverse= True )
#print(score_pairs)

print("*".join([len(word) for word in "one*two*three".split('*')]));