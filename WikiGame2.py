import wikipediaapi
WIKI = wikipediaapi.Wikipedia("WikipediaGame (hatrain.toronto@gmail.com)", "en")
from random import randrange

CommonWordsFile = open(r'CommonWords', 'r')
CommonWordsString = CommonWordsFile.read()

CatDict = {}
with open(r'Categories', 'r') as f:
    for line in f:
        (key, val) = line.split(":")
        CatDict[key] = val

while True:
    # print("Categories: ")
    # for k in CatDict.keys():
    #     print(k)
    cat = "FEATURED"
    # while cat not in CatDict.keys():
    #     cat = input("WHAT CATEGORY? ").upper()
    #     print()
    #     if cat not in CatDict.keys():
    #         print("NOT A CATEGORY")
    #         print()
    
    ArticleList = list(WIKI.page("Category:" + CatDict[cat]).categorymembers.keys())

    ChosenArticle = WIKI.page(ArticleList[randrange(0, len(ArticleList) - 1)])
    # ChosenArticle = WIKI.page("The Man from U.N.C.L.E. (film)")
    # while len(ChosenArticle.text.split("\n")) <= 2 or "(disambiguation)" in ChosenArticle.title.split():
    #     ChosenArticle = WIKI.page(ArticleList[randrange(0, len(ArticleList) - 1)])
    # ChosenArticle = WIKI.page("The Man from U.N.C.L.E. (film)")

    Title = ChosenArticle.title.upper()
    Text = ChosenArticle.text.upper()

    Summary = []
    for l in list(Text):
        if l == "\n":
            break
        else:
            Summary.append(l)
    Summary = "".join(Summary)

    SummarySentenceList = Summary.split(". ")

    print(Title)
    print()

    BlankList = []
    TempBlankList = []
    for s in range(len(SummarySentenceList)):
        for w in SummarySentenceList[s].split():
            if w not in CommonWordsString:
                TempBlankList.append("_" * len(w))
            else:
                TempBlankList.append(w)
        BlankList.append(" ".join(TempBlankList))
        TempBlankList = []

    AnsList = []
    for s in range(len(BlankList)):
        while True:
            # print()
            # print(SummarySentenceList[s])
            # print()
            for a in AnsList:
                TempBlankList2 = BlankList[s].split()
                for w in range(len(SummarySentenceList[s].split())):
                    if a == SummarySentenceList[s].split()[w] and a not in BlankList[s][w]:
                        TempBlankList2[w] = SummarySentenceList[s].split()[w]
                        Correct = True
                    elif a + list(SummarySentenceList[s].split()[w])[-1] == SummarySentenceList[s][w] and a not in BlankList[s][w]:
                        TempBlankList2[w] = SummarySentenceList[s].split()[w]
                        Correct = True
                    elif list(SummarySentenceList[s].split()[w])[0] + a == SummarySentenceList[s][w] and a not in BlankList[s][w]:
                        TempBlankList2[w] = SummarySentenceList[s].split()[w]
                        Correct = True
                    else:
                        pass
                    BlankList[s] = " ".join(TempBlankList2)
            
            print(BlankList[s])
            print()

            a = input("FILL IN A BLANK: ").upper()
            print()

            if a == "":
                b = input("GIVE UP? Y/N: ").upper()
                print()
                if b == "Y":
                    print(SummarySentenceList[s])
                    print()
                    break
                else:
                    pass
            
            Correct = False
            TempBlankList2 = BlankList[s].split()
            for w in range(len(SummarySentenceList[s].split())):
                if a == SummarySentenceList[s].split()[w] and a not in BlankList[s][w]:
                    TempBlankList2[w] = SummarySentenceList[s].split()[w]
                    Correct = True
                elif a + list(SummarySentenceList[s].split()[w])[-1] == SummarySentenceList[s][w] and a not in BlankList[s][w]:
                    TempBlankList2[w] = SummarySentenceList[s].split()[w]
                    Correct = True
                elif list(SummarySentenceList[s].split()[w])[0] + a == SummarySentenceList[s][w] and a not in BlankList[s][w]:
                    TempBlankList2[w] = SummarySentenceList[s].split()[w]
                    Correct = True
                else:
                    pass
            
            
            if Correct:
                print("CORRECT")
                print()
                BlankList[s] = " ".join(TempBlankList2)
                Correct = False
                AnsList.append(a)
                if BlankList[s] == SummarySentenceList[s]:
                    break
                else:
                    continue
            elif not Correct:
                print("INCORRECT")
                print()
                continue
            
            break
    
    print()
    print(Title)
    print()
    print(Summary)
    print()
    print("YOU'RE DONE")
    print()

    a = input("Again? Y/N: ").upper()   
    if a == "Y":
        continue
    else:
        break
    