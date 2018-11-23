import random

getJoke = open("Jokes.txt", "r")
jokelist = getJoke.readlines()


def getJoke():
    jokenumber = random.randint(0, 11)
    return jokelist[jokenumber]


def joke(number: int) -> str:
    return jokelist[number]
