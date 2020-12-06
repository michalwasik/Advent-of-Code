file = open('puzzle/06.in', 'r')
test = file.read().split('\n\n')

anwser_1 = []
anwser_2 = []
for group in test:
    # part 1
    diff_question = set(question for question in group)-{'\n'}
    anwser_1.append(len(diff_question))
    # part 2
    sets_list = list(set(lettered) for lettered in(list(word) for word in group.split()))
    intersected = sets_list[0]
    for i in sets_list:
        intersected = set.intersection(intersected, i)
    anwser_2.append(len(intersected))
print(sum(anwser_1), sum(anwser_2))
