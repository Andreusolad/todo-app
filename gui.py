#graphical user interface
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do") #creats a label on window, has to be a string
input_box = sg.InputText(tooltip="Enter todo") #és el lloc on escrivim, tooltip és el missatge que surt si passem el cursor per sobre
add_button = sg.Button("Add")


window = sg.Window('My To_Do App', layout=[[label], [input_box, add_button]]) #title of the window and layout
#fiquem doble [[ ]] perquè si està dins de dos brackets fica la box al costat del label



window.read()
print("Window has been closed")
window.close()