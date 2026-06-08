from kivy.config import Config

# Permite adaptação automática da tela
Config.set('graphics', 'resizable', True)

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


KV = '''

ScreenManager:
    Tela1:
    Tela2:
    Tela3:


<Tela1>:
    name: "tela1"

    FloatLayout:

        Image:
            source: "Tela1.png"
            size_hint: 1, 1
            pos_hint: {"x":0, "y":0}
            allow_stretch: True
            keep_ratio: False


<Tela2>:
    name: "tela2"

    FloatLayout:

        Image:
            source: "Tela2.png"
            size_hint: 1, 1
            pos_hint: {"x":0, "y":0}
            allow_stretch: True
            keep_ratio: False


        Label:
            text: "Escolha uma opção"
            font_size: "26sp"
            bold: True
            color: 0,0,0,1

            size_hint: 1,None
            height: "40dp"

            pos_hint: {"center_x":0.5,"center_y":0.70}


        Button:
            text: "Necessidade Pessoal"

            size_hint: 0.60,None
            height: "60dp"

            pos_hint: {"center_x":0.5,"center_y":0.55}

            background_normal: ""
            background_color: 0.15,0.55,0.80,1

            on_release:
                app.gerar_resultado("pessoal")


        Button:
            text: "Necessidade Profissional"

            size_hint: 0.60,None
            height: "60dp"

            pos_hint: {"center_x":0.5,"center_y":0.45}

            background_normal: ""
            background_color: 0.15,0.55,0.80,1

            on_release:
                app.gerar_resultado("profissional")


<Tela3>:
    name: "tela3"

    FloatLayout:

        Image:
            source: "Tela3.png"
            size_hint: 1, 1
            pos_hint: {"x":0, "y":0}
            allow_stretch: True
            keep_ratio: False


        Label:
            text: "Resultado"
            font_size: "32sp"
            bold: True
            color: 0,0,0,1

            pos_hint: {"center_x":0.5,"center_y":0.75}


        Label:
            text: "Necessidade Pessoal"
            font_size: "22sp"
            color: 0,0,0,1

            pos_hint: {"center_x":0.5,"center_y":0.62}


        Label:
            text: str(app.pessoal) + "%"
            font_size: "54sp"
            bold: True
            color: 0,0,0,1

            pos_hint: {"center_x":0.5,"center_y":0.56}


        Label:
            text: "Necessidade Profissional"
            font_size: "22sp"
            color: 0,0,0,1

            pos_hint: {"center_x":0.5,"center_y":0.42}


        Label:
            text: str(app.profissional) + "%"
            font_size: "54sp"
            bold: True
            color: 0,0,0,1

            pos_hint: {"center_x":0.5,"center_y":0.36}


        Button:
            text: "Voltar"

            size_hint: 0.50,None
            height: "55dp"

            pos_hint: {"center_x":0.5,"y":0.05}

            background_normal: ""
            background_color: 0.15,0.55,0.80,1

            on_release:
                app.root.current = "tela2"

'''


class Tela1(Screen):
    pass


class Tela2(Screen):
    pass


class Tela3(Screen):
    pass


class MeuApp(App):

    pessoal = NumericProperty(0)
    profissional = NumericProperty(0)

    votos_pessoal = 0
    votos_profissional = 0

    def build(self):

        sm = Builder.load_string(KV)

        sm.transition = FadeTransition(duration=0.4)

        Clock.schedule_once(self.ir_tela2, 3)

        return sm


    def ir_tela2(self, *args):
        self.root.current = "tela2"


    def gerar_resultado(self, tipo):

        if tipo == "pessoal":
            self.votos_pessoal += 1
        else:
            self.votos_profissional += 1

        total = self.votos_pessoal + self.votos_profissional

        self.pessoal = round(
            (self.votos_pessoal / total) * 100
        )

        self.profissional = round(
            (self.votos_profissional / total) * 100
        )

        self.root.current = "tela3"


MeuApp().run()
