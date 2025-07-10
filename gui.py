#graphical user interface
import functions
import FreeSimpleGUI as sg
import time

sg.theme("LightBlue6")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do") #creats a label on window, has to be a string
input_box = sg.InputText(tooltip="Enter todo", key="todo") #és el lloc on escrivim, tooltip és el missatge que surt si passem el cursor per sobre
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout=[[clock],[label], [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]]
window = sg.Window('My To_Do App', layout=layout, font=('Helvetica',15)) #title of the window and layout
#fiquem doble [[ ]] perquè si està dins de dos brackets fica la box al costat del label



while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event) #event és add o edit
    print(values) #values és el que afegeixes i que és de la categoria de to do
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n" #perquè values representa un diccionari on 'to do' és el nostre to do
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0] #el [0] ens dona l'string
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("helvetica", 12))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item firest.", font=("helvetiva", 12))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break #fem servir break i no exit perquè exit() atura tot el programa directament



print("Bye")
window.close()