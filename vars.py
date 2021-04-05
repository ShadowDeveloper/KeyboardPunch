import graphics
import os
area = graphics.GraphWin("Keyboard Punch", 600, 600)
area.setBackground(graphics.color_rgb(30, 90, 255))
cenx = area.getWidth()/2
ceny = area.getHeight()/2
center = graphics.Point(cenx, ceny)
sfx = os.listdir(r"resources\sfx")
hitSfx = sfx[:5]
inputSfx = sfx[5:]
inputSfx = inputSfx[:3]
logo = graphics.Image(center, r"resources\textures\Keyboard_Punch.png")
fail = graphics.Image(graphics.Point(cenx, ceny*0.5), r"resources\textures\Action_Fail.png")
attackSword = graphics.Image(graphics.Point(cenx, ceny*0.5), r"resources\textures\AttackSword.png")
specialSword = graphics.Image(graphics.Point(cenx, ceny*0.5), r"resources\textures\SpecialSword.png")
startMoney = 30
manaRate = 10