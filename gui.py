#graphical user interface
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do") #creats a label on window, has to be a string
input_box = sg.InputText(tooltip="Enter todo", key="todo") #és el lloc on escrivim, tooltip és el missatge que surt si passem el cursor per sobre
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")



window = sg.Window('My To_Do App',
                   layout=[[label], [input_box, add_button],
                    [list_box, edit_button ]],
                   font=('Helvetica',15)) #title of the window and layout
#fiquem doble [[ ]] perquè si està dins de dos brackets fica la box al costat del label



while True:
    event, values = window.read()
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
            todo_to_edit = values['todos'][0] #el [0] ens dona l'string
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break




window.close()