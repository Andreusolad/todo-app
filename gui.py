#graphical user interface
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do") #creats a label on window, has to be a string
input_box = sg.InputText(tooltip="Enter todo", key="todo") #és el lloc on escrivim, tooltip és el missatge que surt si passem el cursor per sobre
add_button = sg.Button("Add")


window = sg.Window('My To_Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica',15)) #title of the window and layout
#fiquem doble [[ ]] perquè si està dins de dos brackets fica la box al costat del label

while True:
    event, values = window.read()
    print(event) #event és add
    print(values) #values és el que afegeixes i que és de la categoria de to do
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n" #perquè values representa un diccionari on 'to do' és el nostre to do
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()