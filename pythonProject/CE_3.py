import FreeSimpleGUI as sg
from converters14 import convert

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="black")


window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()
