########################################
# Paper crawler and analysis of MICCAI19
# By Boss Liu: 774054270@qq.com
# Requirement pandas
########################################

import re
import os
import io
import pandas as pd

class Counter:
    def __init__(self, paperlist):
        self.mapping = dict()
        for title in paperlist:
            #print(title)
            allWord = title.split()
            #print(allWord)
            for word in allWord:
                word = word.lower()
                self.mapping[word] = self.mapping.get(word, 0) + 1
    def most_common(self, n):
        assert n > 0, "n should be large than 0"
        return sorted(self.mapping.items(), key=lambda item: item[1], reverse=True)[:n]

def list():
    os.system("wget -q https://www.miccai2019.org/programme/poster-sessions-tentative/ -O page")
    f = open('./page', 'r')
    data = f.read()
    f.close()

    
    key = data
    p1 = r"<td width=\"397\"><strong>(.+)</strong>"
    pattern1 = re.compile(p1)
    match = pattern1.findall(key)

    return match

if __name__ == "__main__":
    word = []
    count = []
    paperList = list()
    test2 = pd.DataFrame(data = [paperList])
    test2.to_csv('./title.csv')
    #print(paperList)
    most_count = Counter(paperList).most_common(5000)
    for item in most_count:
        print(item)
        #print(item[0])
        #print(item[1])
        word.append(item[0])
        count.append(item[1])
    test = pd.DataFrame(data = [word,count])
    test.to_csv('./miccai.csv')
