'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 

Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Verified working. Problem difficulty of 5%
'''

from csv import reader

offset = ord('A') - 1
filePath = "p022_names.txt"

def calculateNameScore(name, index):
    score = 0
    for char in name:
        score += ord(char) - offset
    return score * index

if __name__ == '__main__':
    score = 0
    index = 1
    with open(filePath, 'r') as read_file:
        csvReader = reader(read_file)
        contents = list(csvReader)

    contents = sorted(contents[0])

    for name in contents:
        score += calculateNameScore(name, index)
        index += 1

    print(score)
