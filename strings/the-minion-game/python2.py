def is_vowel(letter):
    return letter in ['A', 'E', 'I', 'O', 'U']

def calculate_score(string, start_with_vowel):
    l = len(string)
    score = 0
    for i in xrange(l):
        if is_vowel(string[i]) == start_with_vowel:
            score += l - i
    return score

def minion_game(string):

    stuart_score = calculate_score(string, False)
    kevin_score = calculate_score(string, True)

    if stuart_score == kevin_score:
        print 'Draw'
    elif stuart_score > kevin_score:
        print 'Stuart', stuart_score
    else:
        print 'Kevin', kevin_score


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)