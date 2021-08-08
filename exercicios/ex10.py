# Exercício 10

#

import math


def hourToSecond(hour, minute, second):
    return ((hour * 60 * 60) + (minute * 60) + second)


def secondToHour(second):
    hour = math.floor(second / 3600)
    second -= hour * 3600

    minute = math.floor(second / 60)
    second -= minute * 60

   #  answer = []
   #  answer.append(hour)
   #  answer.append(minute)
   #  answer.append(second)

    return [hour, minute, second]


hourEntry = input("Digite o horário de entrada no formato (HH:MM:SS): ")
secondEntry = hourToSecond(int(hourEntry[0:2]), int(
    hourEntry[3:5]), int(hourEntry[6:8]))

hourExit = input("Digite o horário de saída no formato (HH:MM:SS): ")
secondExit = hourToSecond(int(hourExit[0:2]), int(
    hourExit[3:5]), int(hourExit[6:8]))

totalTimeInSeconds = secondExit - secondEntry
totalTime = secondToHour(totalTimeInSeconds)

print("O usuário ficou conectado {}:{}:{}.".format(
    totalTime[0],
    totalTime[1],
    totalTime[2]
))
