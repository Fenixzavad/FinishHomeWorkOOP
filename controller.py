import model
import view
import zoo

def Start():
    num = view.menu()
    match num:
        case 1:
            addAnimal()
        case 2:
            deleteAnimal()
        case 3:
            infoAnimal()
        case 4:
            sayAnimal()    
        case 5:
            model.showAll()
            Start()
        case 6:
            model.sayAll()
            Start()
        case 7:
            exit()


def addAnimal():
    num = view.addAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        Start()
    else:
        model.addAnimal(num)
        Start()


def deleteAnimal():
    model.showAll()
    num = view.deleteAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        Start()
    else:
        model.deleteAnimal(num)
        Start()


def sayAnimal():
    model.showAll()
    num = view.sayAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        Start()
    else:
        model.sayAnimal(num)
        Start()


def infoAnimal():
    model.showAll()
    num = view.showAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        Start()
    else:
        model.showInfo(num)
        Start()