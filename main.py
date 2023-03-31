import PySimpleGUI as sg


def create_window(theme: str) -> sg.Window:
    """Crea una window

    Parameters
    ----------
    theme : str
        Tema de la window

    Returns
    -------
    sg.Window
        sg.Window con el tema pasado como argumento
    """

    sg.theme(theme)
    sg.set_options(font = "Franklin 14", button_element_size=(6,3))
    button_size = (6,3)
    layout = [[sg.Push(), sg.Text("", font="Franklin 26", pad=(10,20), key="-TEXT-")],
              [sg.Button("Clear", expand_x=True), sg.Button("Enter", expand_x=True)],
              [sg.Button(7, size=button_size), sg.Button(8, size=button_size), sg.Button(9, size=button_size), sg.Button("*", size=button_size)],
              [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(6, size=button_size), sg.Button("/", size=button_size)],
              [sg.Button(1, size=button_size), sg.Button(2, size=button_size), sg.Button(3, size=button_size), sg.Button("-", size=button_size)],
              [sg.Button(0, expand_x=True), sg.Button(".", size=button_size), sg.Button("+", size=button_size)]]

    return sg.Window("Calculadora", layout, return_keyboard_events=True)

def main():

    window = create_window("DarkGrey8")

    current_num = [""]
    full_operation = []
    operacion_realizada = False

    while True:
        
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            #Si anteriormente se realizó una operación, limpia current_num
            if operacion_realizada: 
                current_num = []
            #Setea false para se pueda agregar mas de un numero
            operacion_realizada = False

            current_num.append(event)
            num_string = "".join(current_num)
            if len(num_string) <= 16:
                window["-TEXT-"].update(num_string)

        if event in ["+", "-", "/", "*"]:
            full_operation.append("".join(current_num))
            current_num = []
            full_operation.append(event)
            window["-TEXT-"].update("")

        # Boton enter o enter del teclado
        if event == "Enter" or event == "\r":
            operacion_realizada = True
            full_operation.append("".join(current_num))
            if full_operation == [""]:
                result = ""
                full_operation = []
            else:
                try:
                    result = eval("".join(full_operation))
                    result = round(float(result), 14)
                    result = str(result)
                except SyntaxError:
                    sg.popup_error("Syntax error.")
                    result = ""
                except ZeroDivisionError:
                    sg.popup_error("No se puede dividir por cero!")
                    result = ""

                window["-TEXT-"].update(result)
                full_operation = []
                current_num = [str(result)]

        #Boton clear o escape del teclado
        if event == "Clear" or event == "Escape:27":
            full_operation = []
            current_num = [""]
            window["-TEXT-"].update("")
        
main()