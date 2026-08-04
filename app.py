from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
import os
import sys

from logica.sistema import evaluar


def resource_path(relative_path):
    """Obtiene la ruta correcta tanto en desarrollo como en PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Tamaño de la ventana (solo para PC)
Window.size = (520, 780)


class Ventana(BoxLayout):

    def calcular(self):
        try:
            cemento = float(self.ids.cemento.text)
            agua = float(self.ids.agua.text)
            superplastificante = float(self.ids.superplastificante.text)
            fino = float(self.ids.fino.text)
            edad = float(self.ids.edad.text)

            resistencia = evaluar(
                cemento,
                agua,
                superplastificante,
                fino,
                edad
            )

            self.ids.resultado.text = f"{resistencia:.2f} MPa"

        except ValueError:
            self.ids.resultado.text = "Datos inválidos"

        except Exception as e:
            self.ids.resultado.text = "Error"
            print(e)


class SistemaDifusoApp(App):

    title = "Predicción de Resistencia del Concreto"

    def build(self):
        return Builder.load_file(resource_path("interfaz/interfaz.kv"))


if __name__ == "__main__":
    SistemaDifusoApp().run()