# include<iostream>
from random import randint
import json
from time import sleep
wore = False
point = 0
sum1 = 35
with open('./weapons.json', 'r', encoding='utf8')as fp:
    weapons = json.load(fp)
with open('./armor.json', 'r', encoding='utf8')as fp:
    armor = json.load(fp)
mhp = 0
matt = 0
mdefe = 0
mhit = 0
mdodge = 0
hp = 0
att = 0
defe = 0
hit = 0
xp = 0
times = 1
level = 1
profession = ''
monster_list = ['小士兵', '芝诺龟', '论坛兵', '开源社区军队', 'github怪']


if __name__ == '__main__':
    print('欢迎来到Python游戏世界，请为您的角色设置名字:', end='')
    name = input()
    print('您好', name, '!', sep='')
    print('选择成功,请分配能力值!')
    print('你有五个能力值，它们分别为生命、攻击、防御、闪避和命中率')  # 它们的值是', hp, ',', att, ',', defe, ',', dodge, ',', hit, sep=''
    print('请输入它们,中间用空格隔开,总和为25,攻击和防御不要相同', sep='')
    while not False:
        try:
            hp, att, defe, dodge, hit = map(int, input().split(' '))
            if att == defe:
                print('攻击和防御相同,请重新输入:')
                continue
            if hp + att + defe + dodge + hit != 25:
                print('和不为25!请重新输入:')
            else:
                print('设置成功!')
                break
        except ValueError:
            print('输入错误,请重新输入!')
    finished = False
    while not finished:
        sum1 = hp + att + defe + hit + dodge
        print('现在,你要干什么呢?')
        print('--------------\n| 输入你的选择|\n--------------\n输入1修炼\t输入2打怪\t输入s前往商城\t输入c抽奖\t输入q退出', end='')
        choice = input()
        if choice == 'q':
            print('感谢游玩!')
            finished = True
            exit()
        if choice == '1':

            print('开始修炼...')
            sleep(0.1)
            tmp1, tmp2 = randint(1, 3), randint(1, 3)
            if tmp1 == tmp2:
                print('------------\n|修炼成功!   |\n|获得十点经验!|\n------------')
                print('你现在有', xp, '点经验', sep='')
                xp += 10
                del tmp1, tmp2
                if xp >= 100:
                    print('--------\n|升级!|\n------')
                    xp -= 100
                    print('你现在可以为你的属性点增加一共5点的值，输入5个由空格隔开的数')
                    while not False:
                        try:
                            a, b, c, d, e = map(int, input().split(' '))
                            hp += a
                            att += b
                            defe += c
                            dodge += d
                            hit += e
                            break
                        except ValueError:
                            print('输入错误,请重新输入:')
            else:
                print('修炼失败!')
                print('你现在有', xp, '点经验', sep='')
                del tmp1, tmp2
                continue
        if choice == '2':
            player_health = hp * 50 + 100
            monster_health = mhp * 50 + 100
            if times % 10 == 0:
                print('你遇到了boss怪!')
                a1 = 10 * matt - 10 * defe
                a2 = 10 * att - 10 * mdefe
                if a1 < 0:
                    a1 = randint(xp, level * 20)
                if a2 < 0:
                    a2 = randint(xp, level * 20)
                mhp, matt, mdefe, mhit, mdodge = 400 * level, 400 * level, 400 * level, 400 * level, 400 * level
            else:
                monster = monster_list[randint(0, 4)]
                tmp = randint(1, 3)
                if tmp == 1:
                    mhp = round(sum1 / 5)
                    matt = round(sum1 / 5 - 1)
                    mdefe = round(sum1 / 5 + 1)
                    mhit = round(sum1 / 5)
                    mdodge = sum1 - mhp - matt - mdefe - mhit
                elif tmp == 2:
                    matt = round(sum1 * 0.25)
                    mhit = round(sum1 * 0.3)
                    mdefe = round(sum1 * 0.18)
                    mhp = round(sum1 * 0.15)
                    mdodge = sum1 - mhp - matt - mdefe - mhit
                elif tmp == 3:
                    mdefe = round(sum1 * 0.2)
                    mhp = round(sum1 * 0.3)
                    matt = round(sum1 * 0.17)
                    mhit = round(sum1 * 0.15)
                    mdodge = sum1 - mhp - matt - mdefe - mhit
                    del tmp
                print('你遇到了', monster, sep='')
                a1 = 10 * matt - 10 * defe
                a2 = 10 * att - 10 * mdefe
                if a1 < 0:
                    a1 = randint(xp, level * 20)
                if a2 < 0:
                    a2 = randint(xp, level * 20)
            print('你的生命为', player_health, '!', sep='')
            print('怪物的生命为', monster_health, '!', sep='')
            probability = (dodge - mhit) * 10
            mprobability = (mdodge - hit) * 10
            while not False:
                print('按下回车以继续')
                a = input()
                print('怪物攻击!')
                if randint(1, 4) == randint(1, 4):
                    print('你躲避了怪物的攻击!')
                    print('你还剩', player_health, '点血量')
                    print('怪物还剩', monster_health, '点血量')
                    sleep(2)
                else:
                    player_health -= a1
                    print('你还剩', player_health, '点血量')
                    print('怪物还剩', monster_health, '点血量')
                print('按下回车以继续')
                a = input()
                print('你攻击!')
                if randint(1, 4) == randint(1, 4):
                    print('怪物躲避了你的攻击!')
                    print('你还剩', player_health, '点血量')
                    print('怪物还剩', monster_health, '点血量')
                else:
                    monster_health -= a2
                    print('你还剩', player_health, '点血量')
                    print('怪物还剩', monster_health, '点血量')
                if player_health <= 0:
                    print('你输了!')
                    print('你获得了5经验')
                    print('你没有获得金币')
                    xp += 5
                    times += 1
                    break
                elif monster_health <= 0:
                    print('你赢了!')
                    print('你获得了20经验')
                    print('你获得了20金币')
                    point += 20
                    xp += 20
                    times += 1
                    break
        elif choice == 's':
            print('这里有一些商品:')
            tmp1 = weapons.keys()
            tmp2 = armor.keys()
            print('武器:')
            for i in tmp1:
                print(i)
            print('防具:')
            for j in tmp2:
                print(j)
            print('你要买什么?', end='')
            a = input()
            full = False
            if a == '皮革甲':
                if point >= 5:
                    del armor['皮革甲']
                    hp += 5
                    point -= 5
                    defe += 5
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '铁甲':
                if point >= 10:
                    del armor['铁甲']
                    hp += 10
                    point -= 10
                    defe += 10
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '金甲':
                if point >= 20:
                    del armor['金甲']
                    hp += 5
                    point -= 20
                    defe += 5
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '钻石甲':
                if point >= 30:
                    del armor['钻石甲']
                    hp += 10
                    point -= 30
                    defe += 15
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '破木剑':
                if point >= 5:
                    del weapons['破木剑']
                    att += 5
                    point -= 5
                    hit += 1
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '小石剑':
                if point >= 10:
                    del weapons['小石剑']
                    att += 10
                    point -= 10
                    hit += 1
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '普通铁剑':
                if point >= 20:
                    del weapons['普通铁剑']
                    att += 15
                    point -= 20
                    hit += 2
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '附魔铁剑':
                if point >= 25:
                    del weapons['附魔铁剑']
                    att += 15
                    point -= 20
                    hit += 4
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '金剑':
                if point >= 25:
                    del weapons['金剑']
                    att += 5
                    point -= 25
                    hit += 8
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
            elif a == '钻石剑':
                if point >= 35:
                    del weapons['钻石剑']
                    att += 25
                    point -= 35
                    hit += 6
                    print('购买成功!')
                else:
                    print('金币不足,购买失败!')
        elif choice == 'c':
            if point - 20 < 0:
                print('金币不足,无法抽奖!')
            else:
                print('已支付20金币')
                print('正在抽奖...')
                tmp = randint(1, 3)
                if tmp == 1:
                    print('你抽到了一只可爱的宠物:', chr(randint(0x100, 0x1BB0)), chr(randint(0x100, 0x1BB0)), chr(randint(0x100, 0x1BB0)), '但ta并没有什么用', sep='')
                elif tmp == 2:
                    if wore:
                        print('你什么都没抽到')
                    else:
                        tmp1, tmp2, tmp3, tmp4, tmp5 = randint(10, 30), randint(10, 20), randint(10, 20), randint(1, 3), randint(1, 3)
                        print('你抽到了一件装备,属性为生命', tmp1, '攻击', tmp2, '防御', tmp3, '闪避', tmp4, '命中率', tmp5, sep='')
                        print('是否装备?(是/否)', end = '')
                        a = input()
                        if a == '是':
                            hp += tmp1
                            att += tmp2
                            defe += tmp3
                            dodge += tmp4
                            hit += tmp5
                            del tmp1, tmp2, tmp3, tmp4, tmp5
                            print('穿戴成功!')
                        else:
                            print('未穿戴')
                            del tmp1, tmp2, tmp3, tmp4, tmp5
                else:
                    print('你什么也没抽到')
        else:
            print('输入错误,请重新输入')
