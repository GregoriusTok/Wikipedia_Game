import wikipediaapi
WIKI = wikipediaapi.Wikipedia("WikipediaGame (hatrain.toronto@gmail.com)", "en")
from random import randrange

CommonWordsFile = open(r'CommonWords', 'r')
CommonWordsString = CommonWordsFile.read()
while True:
    ArticleList = list(WIKI.page("Category:Featured articles").categorymembers.keys())
    ChosenArticle = WIKI.page(ArticleList[randrange(0, len(ArticleList) - 1)])
    # ChosenArticle = WIKI.page("The Man from U.N.C.L.E. (film)")

    ArticleTitle = ChosenArticle.title.upper()
    ArticleText = ChosenArticle.text.upper()
    ArticleLettList = list(ArticleText)

    ArticleSumm = []
    for l in ArticleLettList:
        if l != "\n":
            ArticleSumm.append(l)
        else:
            break
    ArticleSumm = "".join(ArticleSumm)

    ArticleSummList = ArticleSumm.split() 

    ArticleBlankList = []
    for w in ArticleSummList:
        if CommonWordsString.find(w) != -1 or w in list(ArticleTitle) or len(w) == 1:
            ArticleBlankList.append(w)
        else:
            # print(len(w))
            ArticleBlankList.append('_' * len(w))
    ArticleBlank = " ".join(ArticleBlankList)

    ArticleAnswered = ArticleBlankList.copy()

    while True:
        print()
        print(ArticleTitle)
        print()
        print(ArticleBlank)
        # print()
        # print(ArticleSumm)

        answer = input("Fill in a Blank: ").upper()
        correct = False
        already = False
        for w in range(len(ArticleSummList)):
            if answer == ArticleSummList[w] and answer != ArticleBlankList[w]:
                ArticleBlankList[w] = "\033[4m" + answer + "\033[0m"
                ArticleAnswered[w] = answer
                correct = True
            elif answer + list(ArticleSummList[w])[-1] == ArticleSummList[w] and answer != ArticleBlankList[w]:
                ArticleBlankList[w] = "\033[4m" + answer + list(ArticleSummList[w])[-1] + "\033[0m"
                ArticleAnswered[w] = answer + list(ArticleSummList[w])[-1]
                correct = True
            elif list(ArticleSummList[w])[0] + answer == ArticleSummList[w] and answer != ArticleBlankList[w]:
                ArticleBlankList[w] = "\033[4m" + list(ArticleSummList[w])[0] + answer + "\033[0m"
                ArticleAnswered[w] = list(ArticleSummList[w])[0] + answer
                correct = True
            elif answer in ArticleAnswered:
                already = True
            elif answer != ArticleSummList[w]:
                pass
        if correct:
            print()
            print("Correct")
        elif already:
            print()
            print("Already Answered")
        else:
            print()
            print("Incorrect")

        ArticleBlank = " ".join(ArticleBlankList)

        if ArticleAnswered == ArticleSummList:
            break
        else:
            continue
    print()
    print(ArticleTitle)
    print()
    print(ArticleBlank)
    print()
    print("YOU HAVE WON!!")
    print()
    a = input("Play Again? Y/N ").upper()
    if a == "Y":
        continue
    else:
        break
