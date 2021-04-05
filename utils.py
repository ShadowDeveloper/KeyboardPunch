import math
import playsound
import random
import sys
import time
from vars import *
def write(pos, txt):
    text = graphics.Text(pos, txt)
    cont = graphics.Text(graphics.Point(cenx, ceny*1.5), "Click to continue")
    text.draw(area)
    cont.draw(area)
    area.getMouse()
    text.undraw()
    cont.undraw()

def inpt(pos, txt):
    text = graphics.Text(graphics.Point(cenx, ceny*0.5), txt)
    cont = graphics.Text(graphics.Point(cenx, ceny * 1.5), "Click to continue")
    box = graphics.Entry(pos, 25)
    box.draw(area)
    text.draw(area)
    cont.draw(area)
    area.getMouse()
    text.undraw()
    cont.undraw()
    box.undraw()
    playsound.playsound(rf"resources\sfx\{inputSfx[random.randint(0, len(inputSfx) - 1)]}")
    return box.getText()

def showImg(img):
    sprite = img
    sprite.draw(area)
def clearImg(img):
    sprite = img
    sprite.undraw()
def showatk():
    blade = graphics.Polygon(graphics.Point(cenx, ceny * 0.25), graphics.Point(cenx * 1.025, ceny * 0.33),
                             graphics.Point(cenx * 1.025, ceny * 0.5), graphics.Point(cenx * 0.975, ceny * 0.5),
                             graphics.Point(cenx * 0.975, ceny * 0.33))
    handle1 = graphics.Rectangle(graphics.Point(cenx * 0.9, ceny * 0.52), graphics.Point(cenx * 1.1, ceny * 0.5))
    handle2 = graphics.Rectangle(graphics.Point(cenx * 0.98, ceny * 0.52), graphics.Point(cenx * 1.02, ceny * 0.65))
    cont = graphics.Text(graphics.Point(cenx, ceny * 1.5), "Click to continue")
    blade.setFill("silver")
    blade.setOutline("black")
    handle1.setFill("gold")
    handle1.setOutline("gold")
    handle2.setFill("gold")
    handle2.setOutline("gold")
    blade.draw(area)
    handle1.draw(area)
    handle2.draw(area)
    cont.draw(area)
    area.getMouse()
    blade.undraw()
    handle1.undraw()
    handle2.undraw()
    cont.undraw()

def showspc():
    blade = graphics.Polygon(graphics.Point(cenx, ceny * 0.25), graphics.Point(cenx * 1.025, ceny * 0.33),
                             graphics.Point(cenx * 1.025, ceny * 0.5), graphics.Point(cenx * 0.975, ceny * 0.5),
                             graphics.Point(cenx * 0.975, ceny * 0.33))
    handle1 = graphics.Rectangle(graphics.Point(cenx * 0.9, ceny * 0.52), graphics.Point(cenx * 1.1, ceny * 0.5))
    handle2 = graphics.Rectangle(graphics.Point(cenx * 0.98, ceny * 0.52), graphics.Point(cenx * 1.02, ceny * 0.65))
    special = graphics.Circle(graphics.Point(cenx, ceny * 0.45), 70)
    cont = graphics.Text(graphics.Point(cenx, ceny * 1.5), "Click to continue")
    blade.setFill("silver")
    blade.setOutline("black")
    handle1.setFill("gold")
    handle1.setOutline("gold")
    handle2.setFill("gold")
    handle2.setOutline("gold")
    special.setOutline("lime")
    blade.draw(area)
    handle1.draw(area)
    handle2.draw(area)
    special.draw(area)
    cont.draw(area)
    area.getMouse()
    blade.undraw()
    handle1.undraw()
    handle2.undraw()
    special.undraw()
    cont.undraw()

def actions(player, nextup, AI, moves, AImoves, AIlevel):
    write(center, f"{player.name}'s turn.")
    if player in AI:
        if AIlevel < 5:
            action = AImoves[random.randint(0, len(AImoves)-1)]
        elif AIlevel < 10:
            if player.hp < player.maxhp/4:
                action = AImoves[1]
        time.sleep(random.randint(0, 5))
    else:
        action = inpt(center, "What would you like to do?")
    if player.hp > 0:
        if action in moves:
            if action == "shop":
                write(center, f"{player.name} is going to the shop.")
                shop(player, AI)
            elif action == "attack":
                if player.mn > 9:
                    player.attack(nextup)
            elif action == "special":
                if player.mn > 19:
                    playsound.playsound(r"resources\sfx\Special.wav")
                    player.special(nextup)
            elif action == "check balance":
                write(center, f"{player.name} has ${player.money}")
                actions(player, nextup, AI, moves, AImoves, AIlevel)
            elif action == "check mana":
                write(center, f"{player.name} has {player.mn} mana.")
                actions(player, nextup, AI, moves, AImoves, AIlevel)
            player.mn += manaRate
        else:
            write(center, f"That is not an action. Here are the available actions:")
            for i in moves:
                write(center, i)
    else:
        if player in AI:
            write(center, "You won!")
        else:
            write(center, "You lost!")
            start()

items = {
    "dmg - Yeet Sword" : 10,
    "dmg - Pog Pistol" : 15,
    "dfn - MLG Shield" : 10
}
itemkeys=list(items)


# noinspection PyUnboundLocalVariable
def shop(buyer, AIs):
    if buyer not in AIs:
        write(center, "Here are all the items.")
        x=0
        for i in items:
            item = itemkeys[x]
            price = items[i]
            write(center, f"Item #{x+1} is {item} for ${price}")
            x+=1
        purchasedItem = inpt(center, "Which item would you like to purchase?")
        item = purchasedItem
        x=0
        for _ in items:
            itemkey = itemkeys[x]
            if itemkey.find(item) >= 0:
                item = itemkey
            x+=1
        try:
            price = items[item]
            dmgBonus = price / 2
            hpBonus = price * 2
            dfnBonus = price
            mnBonus = price * 2
        except:
            pass
        if buyer.money >= price:
            if item == item:
                if item == "exit":
                    write(center, "Exiting shop...")
                else:
                    buyer.money -= price
                    write(center, f"{buyer.name} purchased {item} for ${price}. {buyer.name}'s new balance is ${buyer.money}.")
                    if "dmg" in item:
                        write(center, f"This item gives you a damage bonus of {dmgBonus}")
                        buyer.dmg += dmgBonus
                    elif "hp" in item:
                        write(center, f"This item gives you a health bonus of {hpBonus}")
                        buyer.hp += hpBonus
                    elif "dfn" in item:
                        write(center, f"This item gives you a defense bonus of {dfnBonus}")
                        buyer.dfn += dfnBonus
                    elif "mn" in item:
                        write(center, f"This item has a mana boost of {mnBonus}")
                    else:
                        write(center, "That isn't an item.")
                        shop(buyer, AIs)
        else:
            write(center, "You don't have enough money")
    else:
        item = itemkeys[random.randint(0, len(itemkeys)-1)]
        x = 0
        for _ in items:
            itemkey = itemkeys[x]
            if itemkey.find(item) >= 0:
                item = itemkey
            x += 1
        try:
            price = items[item]
            dmgBonus = price / 2
            hpBonus = price * 2
            dfnBonus = price
            mnBonus = price * 2
        except:
            pass
        if buyer.money >= price:
            if item == item:
                if item == "exit":
                    write(center, "Exiting shop...")
                else:
                    buyer.money -= price
                    write(center,
                          f"{buyer.name} purchased {item} for ${price}. {buyer.name}'s new balance is ${buyer.money}.")
                    if "dmg" in item:
                        write(center, f"This item gives you a damage bonus of {dmgBonus}")
                        buyer.dmg += dmgBonus
                    elif "hp" in item:
                        write(center, f"This item gives you a health bonus of {hpBonus}")
                        buyer.hp += hpBonus
                    elif "dfn" in item:
                        write(center, f"This item gives you a defense bonus of {dfnBonus}")
                        buyer.dfn += dfnBonus
                    elif "mn" in item:
                        write(center, f"This item has a mana boost of {mnBonus}")
                    else:
                        write(center, "That isn't an item.")
                        shop(buyer, AIs)
def selectStart(player):
    factions = ["knight", "archer", "wizard", "paladin", "gunner", "shaman", "tank", "sniper", "alchemist"]
    if player == 'ai':
        nameString = "Lucy Cope Ashlea Miller Dawson Ellison Yasmine Parry Stanley Wagstaff Darlene Betts Willard John Ahmet Glass Catrina Sion Merritt Charity Garner Taybah Oneill Isobelle Mcfarlane Ayesha Gamble Kayley Deacon Glenda Mckinney Shanay Lang Scarlett Carr Jonah MelendezAlayna Mustafa Desiree Eastwood Junaid Durham Yasmeen Holden Mya Robin Jaidan Moran Ayaana Hanna Lily May Cochran Olive Kirby Kailum Pittman Cosmo Shaw Tonicha Decker Heidi Quintana Joely Guy Seren Spooner Fredrick Hughes Montgomery Ali Dulcie Wills Theresa Whitfield Iain Rios Sanjeev Sadler Ashlyn Brady Charlie Markham Aaisha Higgins Bella Cantu Kiaan Camacho Adelaide Bouvet Bayley Raymond Nelson Conrad Aryaan Farrow Shanai Farrell Iolo Ewing Sanna OSullivan Dakota Kendall Manuel Butt Solomon Dickinson Sullivan Greaves Maiya Best Alix Cairns Leela Emerson Abdulrahman Yates Tonisha Barber Jac Guest Prisha Bevan Blanka Redmond Taran Dawson Jill Foreman Kaitlin Morrison Mert Butler Rick Branch Malachy Calvert Claudia Finley Izzy Redman Sylvie Stubbs Trey Summer Jarvis George Eryk Maxwell Haris Marriott Malaikah Marsden Teigan Peralta Cienna Monroe Timothy Randall Scott Hancock Taryn Wilde Selin Blundell Rania Reader Kalum Ferreira Dillon Blackwell Azeem Travers Finnley Hendrix Gloria Rhodes Abbie Murillo Aishah Ireland Anaya West Cristina Bowler Sue Medrano Rex Cousins Leila Salas Mariah Hubbard Jolene ODoherty Viola Ford"
        names = nameString.split(' ')
        faction = factions[random.randint(0, len(factions)-1)]
        name = names[random.randint(0, len(names)-1)]
    else:
        name = inpt(center, "Input your name")
        write(center, "Here are the available factions:")
        factionString = ''
        for i in factions:
            factionString += f"{i}, "
        write(center, factionString)
        faction = inpt(center, "Input your faction.").lower()

    if faction in factions:
        if faction == "knight":
            return Knight(name, 100, 10, 20, 100, startMoney)
        if faction == "paladin":
            return Paladin(name, 100, 10, 30, 100, startMoney)
        if faction == "tank":
            return Tank(name, 100, 10, 40, 100, startMoney)
        if faction == "archer":
            return Archer(name, 150, 10, 10, 100, startMoney)
        if faction == "gunner":
            return Gunner(name, 150, 15, 10, 100, startMoney)
        if faction == "sniper":
            return Sniper(name, 150, 15, 20, 100, startMoney)
        if faction == "wizard":
            return Wizard(name, 100, 20, 10, 100, startMoney)
        if faction == "shaman":
            return Shaman(name, 100, 20, 10, 100, startMoney)
        if faction == "alchemist":
            return Alchemist(name, 150, 20, 10, 100, startMoney)
    else:
        write(center, "Oops! You put in an invalid faction. We are forced to quit the game. Please restart!")
        sys.exit()
def start():
    title()

    def init():
        p1 = selectStart('p')
        p2 = selectStart('ai')
        players=[p1, p2]
        AIs=[p2]
        AImoves = ["attack", "special", "shop"]
        moves = ["attack", "special", "shop", "check balance", "check mana"]
        try:
            AIlevel = int(inpt(center, "What level is the AI?"))
        except:
            AIlevel = 1
        return p1, p2, players, AIs, AImoves, moves, AIlevel

    def nextTarget(player, players):
        nextup = players[random.randint(0, 1)]
        if nextup.name == player.name:
            nextTarget(player, players)
        else:
            return nextup

    def tryAction(player, nextup, AIs, moves, AImoves, AIlevel):
        try:
            actions(player, nextup, AIs, moves, AImoves, AIlevel)
        except:
            showImg(fail)
            write(center, f"Oops! {player.name} couldn't complete the action!")
            clearImg(fail)
            #20% Chance of Slip-Up
            if random.randint(1, 5) == 1:
                write(center, f"Your opponent slipped up and gave you another chance to act!")
                tryAction(player, nextup, AIs, moves, AImoves, AIlevel)

    def gameplay(AIlevel):
        p = 0
        opponentFaction = str(type(p2)).split('.')
        opponentFaction = opponentFaction[1]
        opponentFaction = opponentFaction[:len(opponentFaction)-2]
        write(center, f"You are facing {p2.name}. Their faction is {opponentFaction}.")
        rnd = 1
        while True:
            player = players[p]
            nextup = nextTarget(player, players)
            if player.hp > 0:
                write(center, f"Turn {rnd}")
                tryAction(player, nextup, AIs, moves, AImoves, AIlevel)
                if p+1 != len(players):
                    p+=1
                else:
                    p=0
            else:
                break
            rnd += 1
        if player in AIs:
            write(center, f"{player.name} died! Next round!")
            gameplay(AIlevel+random.randint(0, 2))
        else:
            write(center, "You died! Game Over!")
            sys.exit()

    p1, p2, players, AIs, AImoves, moves, AIlevel = init()
    gameplay(AIlevel)

def title():
    bg = logo
    start = graphics.Text(graphics.Point(cenx, ceny*1.5), "Start!")
    bg.draw(area)
    start.draw(area)
    area.getMouse()
    bg.undraw()
    start.undraw()
    playsound.playsound(r"resources\sfx\Start.wav")
# factions
class Fighter:
    def __init__(self, name, hp, dmg, dfn, mn, money):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.dmg = dmg
        self.dfn = dfn
        self.mn = mn
        self.money = money

    def damage(self, hit):
        res = round(self.dfn/10, 2)
        self.hp -= hit-res
        playsound.playsound(rf"resources\sfx\{hitSfx[random.randint(0, len(hitSfx) - 1)]}")
        if self.hp <= 0:
            self.hp = 0
            write(center, f"{self.name} is dead! Their balance of {self.money} has been decreased by 25.")
            if self.money >= 25:
                self.money -= 25
            else:
                self.money = 0

    def attack(self, other):
        showImg(attackSword)
        try:
            write(center, f"{self.name} has attacked {other.name} dealing {self.dmg} damage leaving them with {other.hp-self.dmg} health!")
        except:
            pass
        clearImg(attackSword)
        other.damage(self.dmg)
        self.money += 5
        self.mn -= self.dmg

    def special(self, other):
        repeat = random.randint(1, 3)
        x = 0
        while x < repeat:
            showImg(specialSword)
            try:
                write(center, f"Hit #{x+1}! {self.name} has attacked {other.name} dealing {self.dmg} damage leaving them with {other.hp-self.dmg} health!")
            except:
                pass
            clearImg(specialSword)
            other.damage(self.dmg)
            x += 1
            self.money += 5
            self.mn -= self.dmg

class Ranger:
    def __init__(self, name, hp, dmg, dfn, mn, money):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.dmg = dmg
        self.dfn = dfn
        self.mn = mn
        self.money = money

    def damage(self, hit):
        res = round(self.dfn / 10, 2)
        self.hp -= hit - res
        playsound.playsound(rf"resources\sfx\{hitSfx[random.randint(0, len(hitSfx) - 1)]}")
        if self.hp <= 0:
            self.hp = 0
            write(center, f"{self.name} is dead! Their balance of {self.money} has been decreased by 25.")
            if self.money>=25:
                self.money-=25
            else:
                self.money=0

    def attack(self, other):
        showImg(attackSword)
        try:
            write(center, f"{self.name} has attacked {other.name} dealing {self.dmg} damage leaving them with {other.hp-self.dmg} health!")
        except:
            pass
        clearImg(attackSword)
        other.damage(self.dmg)
        self.money += 5
        self.mn -= self.dmg

    def special(self, other):
        showImg(specialSword)
        try:
            write(center, f"{self.name} has attacked {other.name} dealing {self.dmg*3} damage leaving them with {other.hp-self.dmg*3} health!")
        except:
            pass
        clearImg(specialSword)
        other.damage(self.dmg * 3)
        self.money += 5*3
        self.mn -= self.dmg*3


class Mage:
    def __init__(self, name, hp, dmg, dfn, mn, money):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.dmg = dmg
        self.dfn = dfn
        self.mn = mn
        self.money = money

    def damage(self, hit):
        res = round(self.dfn / 10, 2)
        playsound.playsound(rf"resources\sfx\{hitSfx[random.randint(0, len(hitSfx) - 1)]}")
        self.hp -= hit - res
        if self.hp <= 0:
            self.hp = 0
            write(center, f"{self.name} is dead! Their balance of {self.money} has been decreased by 25.")
            if self.money >= 25:
                self.money -= 25
            else:
                self.money = 0

    def attack(self, other):
        showImg(attackSword)
        try:
            write(center, f"{self.name} has attacked {other.name} dealing {self.dmg} damage leaving them with {other.hp-self.dmg} health!")
        except:
            pass
        clearImg(attackSword)
        other.damage(self.dmg)
        self.money+=5
        self.mn -= self.dmg

    def special(self, other):
        repeat = math.ceil(random.randint(1, 2))
        x = 0
        while x < repeat:
            showImg(specialSword)
            hurt = random.randint(1, 2)
            try:
                write(center, f"Hit #{x+1}! {self.name} has attacked {other.name} dealing {self.dmg*hurt} damage leaving them with {other.hp-self.dmg*hurt} health!")
            except:
                pass
            clearImg(specialSword)
            other.damage(self.dmg * hurt)
            x += 1
            self.money += 5*hurt
            self.mn -= self.dmg*hurt


class Knight(Fighter):
    pass
class Paladin(Fighter):
    # noinspection PyArgumentList
    def __init__(self, name, hp, dmg, dfn, mn, money):
        super().__init__(name, hp, dmg, dfn, mn, money)

    def special(self, other):
        repeat = random.randint(2, 5)
        x = 0
        while x < repeat:
            showImg(specialSword)
            try:
                write(center,
                      f"Hit #{x+1}! {self.name} has attacked {other.name} dealing {self.dmg} damage leaving them with {other.hp - self.dmg} health!")
            except:
                pass
            clearImg(specialSword)
            other.damage(self.dmg)
            x += 1
            self.money += 5
            self.mn -= self.dmg

class Tank(Fighter):
    def __init__(self, name, hp, dmg, dfn, mn, money):
        super().__init__(name, hp, dmg, dfn, mn, money)

    def special(self, other):
        self.dfn += self.dmg
        showImg(specialSword)
        try:
            write(center, f"{self.name} has raised their defense by {self.dmg}, now they have a defense of {self.dfn}!")
        except:
            pass
        clearImg(specialSword)
class Archer(Ranger):
    pass
class Gunner(Ranger):
    # noinspection PyArgumentList
    def __init__(self, name, hp, dmg, dfn, mn, money):
        super().__init__(name, hp, dmg, dfn, mn, money)

    def special(self, other):
        showImg(specialSword)
        try:
            write(center,
              f"{self.name} has attacked {other.name} dealing {self.dmg * 4} damage leaving them with {other.hp - self.dmg * 4} health!")
        except:
            pass
        clearImg(specialSword)
        other.damage(self.dmg * 4)
        self.money += 5 * 4
        self.mn -= self.dmg * 4

class Sniper(Ranger):
    def __init__(self, name, hp, dmg, dfn, mn, money):
        super().__init__(name, hp, dmg, dfn, mn, money)

    def special(self, other):
        showImg(specialSword)
        try:
            write(center,
                  f"{self.name} has attacked {other.name} dealing {self.dmg * 5} damage leaving them with {other.hp - self.dmg * 5} health!")
        except:
            pass
        clearImg(specialSword)
        other.damage(self.dmg * 5)
        self.money += 5 * 5
        self.mn -= self.dmg * 5

class Wizard(Mage):
    pass
class Shaman(Mage):
    # noinspection PyArgumentList
    def __init__(self, name, hp, dmg, dfn, mn, money):
        super().__init__(name, hp, dmg, dfn, mn, money)

    def special(self, other):
        repeat = math.ceil(random.randint(1, 3))
        x = 0
        while x < repeat:
            hurt = random.randint(1, 3)
            showImg(specialSword)
            try:
                write(center, f"Hit #{x+1}! {self.name} has attacked {other.name} dealing {self.dmg*hurt} damage leaving them with {other.hp-self.dmg*hurt} health!")
            except:
                pass
            other.damage(self.dmg * hurt)
            x += 1
            self.money += 5*hurt
            self.mn -= self.dmg*hurt

        clearImg(specialSword)
class Alchemist(Mage):
    def __init__(self, name, hp, dmg, dfn, mn, money):
        super().__init__(name, hp, dmg, dfn, mn, money)

    def special(self, other):
        showImg(specialSword)
        try:
            if self.hp < self.maxhp:
                self.hp += self.dmg
                write(center, f"{self.name} healed themselves {self.dmg} health, leaving them with {self.hp} health!")
            else:
                write(center, "You are already on max health!")
        except:
            pass
        clearImg(specialSword)
