import playsound

def printmeplz(string):
    if type(string) != str:
        string = 'converted_' + str(string)
    print(string)


def intmeplz(integer):
    if type(integer) != int:
        try:
            integer = int(integer)
        except ValueError:
            return print('Wrong format!')
    print(integer)


def bugmeplz(text):
    playsound.playsound(r'sounds/error.wav')
    raise Exception(text)

bugmeplz('Buhahahahha !')