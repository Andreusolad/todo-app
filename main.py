import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action=input("Write add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo=user_action[4:]

        todos = functions.get_todos()

        todos.append(todo +'\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        print(todos)


        for index, item in enumerate(todos):
            index = index + 1
            item = item.strip('\n') #Això és una altra forma de fer exactament el mateix de suprimiruna líniea, només sobreescrivm la variable item.
            row = f"{index}-{item}"
            print(row)
        print(f"The length is {len(todos)}")

    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo=input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid. ")
            continue
            #continue el que fa és ignorar tot el que hi ha a sota i
            #tornar al principi de tot



    elif user_action.startswith("complete"):
        try:
            nombre = int(user_action[9:])

            todos = functions.get_todos()
            nombre = nombre - 1

            todo_to_remove = todos[nombre].strip('\n')

            todos.pop(nombre) #Fem servir el pop perquè el "remove" és pel valor de l'item i pop va per l'índex.

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")