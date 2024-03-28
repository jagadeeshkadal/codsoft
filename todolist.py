
import sys 
class ToDoList:
    def __init__(self):
        self.list = []
    def AddToList(self, item):
        self.list.append(item)
        print(" added to the list.",item)
        
    def DisplayList(self):
        if not self.list:
            print("The list is empty.")
        else:
            print("Current List:", self.list)


    def UpdateList(self, old_item, new_item):
        if old_item in self.list:
            index = self.list.index(old_item)
            self.list[index] = new_item
            print("old_item updated to", new_item)
            self.DisplayList()
            
        else:
            print("Item not found in list",old_item)
manage=ToDoList()
while True:
        print("OPERATIONS OF LIST")
        print("1. Add to List")
        print("2. display the List")
        print("3. update the List")
        print("4. Exit")

        choice = input("Enter your choice  ")

        if choice == '1':
            item = input("Enter the item to add: ")
            manage.AddToList(item)
           
        elif choice == '2':
            
            manage.DisplayList()
        elif choice == '3':
            old_item = input("Enter the item to update: ")
            new_item = input("Enter the new item: ")
            manage.UpdateList(old_item, new_item)
        elif choice == '4':
            sys.exit(0)
            
        else:
            print("please enter valid choice")


