from view import View
from controller import Controller
from model import Model

def main():
    model = Model()
    controller = Controller()
    view = View()

    controller.definir_tela(view)
    controller.definir_model(model)
    
    view.definir_controller(controller)
    model.set_controller(controller)
    view.iniciar()

main()    

