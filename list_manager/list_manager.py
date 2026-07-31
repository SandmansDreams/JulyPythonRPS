# List should be able to read from a file to populate
# Min requirements: add item, remove item, edit itmes, move item, save list to a file

""" IMPORTS AND DEFINITIONS """
FILE_NAME = "managed_list.txt"

""" HELPERS """
def loadList(fileName):
    try:
        with open(fileName, "r") as loadedFile:
            loadedList = loadedFile.readlines()
            for idx in range(len(loadedList)):
                loadedList[idx] = loadedList[idx].replace("\n", "")
    except Exception:
        loadedList = []

    return loadedList

def saveList(listToSave):
    with open(FILE_NAME, "w") as saveFile:
        for line in range(len(listToSave)):
            if line == len(listToSave) - 1:
                saveFile.write(listToSave[line])
            else:
                item = f"{listToSave[line]}\n"
                saveFile.write(item)

def printOptions():
    print("")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("")
    print("                LIST MANAGER - OPTIONS")
    print("")
    print("                1. View Item(s)")
    print("                2. Add Item(s)")
    print("                3. Remove Item(s)")
    print("                4. Edit Item(s)")
    print("                5. Move Item(s)")
    print("                6. Exit")
    print("")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

def printList(listIn):
    print("")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("")
    print("                YOUR LIST:")
    print("")
    if len(listIn) == 0:
        print("             This list is empty...")
    else:
        for idx in range(len(listIn)):
            print(f"               {idx + 1}. {listIn[idx]}")
    print("")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

def addItems(listIn):
    addMore = True

    while addMore:
        printList(listIn)
        print("Add Item?")
        toAdd = input(" --> ")

        if toAdd.lower().strip() in ["no", "n", "exit", "e", "quit", "q"]:
            addMore = False
        else: 
            listIn.append(toAdd)

    saveList(listIn)

def removeItems(listIn):
    removeMore = True

    while removeMore:
        validRemove = False

        while not validRemove:
            printList(listIn)
            print("Remove Item (index or item)?")
            toRemove = input(" --> ").lower()

            # Exit case
            if toRemove in ["no", "n", "exit", "e", "quit", "q"]:
                removeMore = False
                break
        
            # Test if an index was put in
            try:
                toRemove = int(toRemove) - 1
                if toRemove in range(len(listIn)):
                    listIn.pop(toRemove)
                    validRemove = True
            except ValueError:
                # Test if non-index is in the list
                for line in listIn:
                    if toRemove == line.lower():
                        listIn.remove(line)
                        validRemove = True
                        break

            if not validRemove:
                print("")
                print("Invalid input - please try again!")

    saveList(listIn)

def editItems(listIn):
    saveList(listIn)

def moveItems(listIn):
    saveList(listIn)

""" MAIN FUNCTION """
def main():
    appOn = True

    while appOn:
        list = loadList(FILE_NAME)
        printOptions()
        userChoice = input(" --> ").lower()

        if userChoice in ["1", "1.", "1 view list", "1. view list", "view list", "view", "list", "show"]:
            printList(list)
        elif userChoice in ["2", "2.", "2 add item", "2. add item", "add item", "add", "a", "+"]:
            addItems(list)
        elif userChoice in ["3", "3.", "3 remove item", "3. remove item", "remove item", "remove", "delete", "del", "r", "-"]:
            removeItems(list)
        elif userChoice in ["4", "4.", "4 edit item", "4. edit item", "edit item", "edit", "modify", "change", "e"]:
            editItems(list)
        elif userChoice in ["5", "5.", "5 move item", "5. move item", "move item", "move", "swap", "m"]:
            moveItems(list)
        elif userChoice in ["6", "6.", "6 exit", "6. exit", "exit", "quit", "q", "x"]:
            appOn = False
        else:
            print("Invalid choice - try again!")



main()