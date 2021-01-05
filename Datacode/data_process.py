import os
import fileinput


# store data in local files
def data_storage(x1, y1, phit, t,
                 u1='', T='', z1='',
                 x2='', y2='', z2='',
                 rudder_angle=''):
    x1_save = 'D:\\Wave glider modelling\\data\\x1.txt'
    with open(x1_save, 'a') as obj:
        obj.write('\n' + str(x1[-1]))

    y1_save = 'D:\\Wave glider modelling\\data\\y1.txt'
    with open(y1_save, 'a') as obj:
        obj.write('\n' + str(y1[-1]))

    phit_save = 'D:\\Wave glider modelling\\data\\phit.txt'
    with open(phit_save, 'a') as obj:
        obj.write('\n' + str(phit[-1]))

    t_save = 'D:\\Wave glider modelling\\data\\time.txt'
    with open(t_save, 'a') as obj:
        obj.write('\n' + str(t))

    if u1:
        u1_save = 'D:\\Wave glider modelling\\data\\u1.txt'
        with open(u1_save, 'a') as obj:
            obj.write('\n' + str(u1[-1]))

    if T:
        T_save = 'D:\\Wave glider modelling\\data\\T.txt'
        with open(T_save, 'a') as obj:
            obj.write('\n' + str(T[-1]))

    if z1:
        z1_save = 'D:\\Wave glider modelling\\data\\z1.txt'
        with open(z1_save, 'a') as obj:
            obj.write('\n' + str(z1[-1]))

    if x2:
        x2_save = 'D:\\Wave glider modelling\\data\\x2.txt'
        with open(x2_save, 'a') as obj:
            obj.write('\n' + str(x2[-1]))

    if y2:
        y2_save = 'D:\\Wave glider modelling\\data\\y2.txt'
        with open(y2_save, 'a') as obj:
            obj.write('\n' + str(y2[-1]))

    if z2:
        z2_save = 'D:\\Wave glider modelling\\data\\z2.txt'
        with open(z2_save, 'a') as obj:
            obj.write('\n' + str(z2[-1]))

    if rudder_angle:
        rudder_angle_save = 'D:\\Wave glider modelling\\data\\rudder_angle.txt'
        with open(rudder_angle_save, 'a') as obj:
            obj.write('\n' + str(rudder_angle[-1]))


# clear previous stored data.
def data_elimation():
    open('D:\\Wave glider modelling\\data\\x1.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\y1.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\phit.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\time.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\u1.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\T.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\z1.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\x2.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\y2.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\z2.txt', 'w').close()
    open('D:\\Wave glider modelling\\data\\rudder_angle.txt', 'w').close()
    os.remove(r'D:\\Wave glider modelling\\data\\x1.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\y1.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\phit.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\time.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\u1.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\T.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\z1.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\x2.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\y2.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\z2.txt')
    os.remove(r'D:\\Wave glider modelling\\data\\rudder_angle.txt')


def data_delete_first_line():
    x1_json = 'D:\\Wave glider modelling\\data\\x1.txt'
    for line in fileinput.input(x1_json, inplace=1):
        if not fileinput.isfirstline():
            print(line.replace('\n', ''))

    y1_json = 'D:\\Wave glider modelling\\data\\y1.txt'
    for line in fileinput.input(y1_json, inplace=1):
        if not fileinput.isfirstline():
            print(line.replace('\n', ''))

    phit_json = 'D:\\Wave glider modelling\\data\\phit.txt'
    for line in fileinput.input(phit_json, inplace=1):
        if not fileinput.isfirstline():
            print(line.replace('\n', ''))

    t_json = 'D:\\Wave glider modelling\\data\\time.txt'
    for line in fileinput.input(t_json, inplace=1):
        if not fileinput.isfirstline():
            print(line.replace('\n', ''))

    rudder_angle_json = 'D:\\Wave glider modelling\\data\\rudder_angle.txt'
    for line in fileinput.input(rudder_angle_json, inplace=1):
        if not fileinput.isfirstline():
            print(line.replace('\n', ''))

    u1_json = 'D:\\Wave glider modelling\\data\\u1.txt'
    for line in fileinput.input(u1_json, inplace=1):
        if not fileinput.isfirstline():
            print(line.replace('\n', ''))

    loss_json = 'D:\\Wave glider modelling\\data\\loss.txt'
    for line in fileinput.input(loss_json, inplace=1):
        if not fileinput.isfirstline():
            print(line.replace('\n', ''))