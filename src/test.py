import random


def printCard(c):
    shape=[chr(9824),chr(9829),chr(9830),chr(9827)]
    number=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    for i in c:
        s=int(i)//13
        n=int(i)%13
        print(shape[s]+number[n])
    print()


def printMessage():
    Element("player").write('玩家的牌：'+str(printCard(playerCard)))
    Element("playerPoint").write('玩家的牌面點數：'+str(printCard(playerPoint)))
    Element("dealer").write('莊家的牌：'+str(printCard(dealerCard)))
    Element("dealerPoint").write('莊家的牌面點數：'+str(printCard(dealerPoint)))


def cardPoint(x):  # index = 0 ~ 51 , 代表黑桃、愛心、鑽石、梅花
    if x % 13 == 0:  # A -> 11點
        return 11
    elif x % 13 > 9:  # x = index =  J , Q , K -> 10點
        return 10
    else:
        return x % 13 + 1


def deal(gamerCard, gamerPoint):
    temp = card.pop()
    gamerCard.append(temp) 
    gamerPoint.append(cardPoint(temp)) 

def main():
    card = list(range(0, 52))
    random.shuffle(card)

    playerCard = []
    playerPoint = []
    dealerCard = []
    dealerPoint = []

    # 發牌
    for i in range(2):
        deal(playerCard, playerPoint)
    deal(dealerCard, dealerPoint)
    while True:
        ans = input('玩家要加牌嗎(Y/N)?')
        if ans == 'N' or ans == 'n':
            break
        deal(playerCard, playerPoint) 
        if sum(playerPoint) > 21:
            if 11 in playerPoint: 
                ans_1 = input('玩家要把A換成11嗎(Y/N)?')
                if ans_1 == 'N' or ans_1 == 'n':
                    playerPoint[playerPoint.index(11)] = 1 
                    printMessage()
                else:
                    playerPoint[playerPoint.index(11)] = 11
                    if sum(playerPoint) > 21:
                        Element("winer").write('玩家爆牌，莊家獲勝,玩家: '+str (sum(playerPoint), "莊家電腦:", sum(dealerPoint)))
                        break
            else:
                printMessage() 
                Element("winer").write('玩家爆牌，莊家獲勝')
                break
        else:
            printMessage()
    if sum(playerPoint) < 22:
        while sum(dealerPoint) < 17:
            deal(dealerCard, dealerPoint)
            if sum(dealerPoint) > 21:
                if 11 in dealerPoint:
                    dealerPoint[dealerPoint.index(11)] = 1 
            printMessage()

        if sum(dealerPoint) > 21:
            Element("winer").write('莊家爆牌,玩家勝利', "玩家:", str(sum(playerPoint), "莊家電腦:", sum(dealerPoint)))
        elif sum(playerPoint) > sum(dealerPoint):
            Element("winer").write('玩家勝利', "玩家:", str(sum(playerPoint), "莊家電腦:", sum(dealerPoint)))
        elif sum(playerPoint) < sum(dealerPoint):
            Element("winer").write('莊家勝利', "玩家:", str(sum(playerPoint), "莊家電腦:", sum(dealerPoint)))
        elif sum(playerPoint) == sum(dealerPoint):
            Element("winer").write('和局', "玩家:", str(sum(playerPoint), "莊家電腦:", sum(dealerPoint)))