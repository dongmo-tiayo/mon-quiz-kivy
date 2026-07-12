from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#1E1E2F")

questions = [
    ["Combien font 2 + 2 ?", "4"],
    ["Quelle est la capitale de la France ?", "paris"],
    ["Combien de continents y a-t-il ?", "7"],
]

class QuizApp(App):
    def build(self):
        self.index = 0
        self.score = 0

        self.layout = BoxLayout(
            orientation='vertical',
            padding=40,
            spacing=20
        )

        self.question_label = Label(
            text=questions[self.index][0],
            font_size='24sp',
            color=get_color_from_hex("#FFFFFF"),
            size_hint=(1, 0.35)
        )

        self.champ_reponse = TextInput(
            multiline=False,
            font_size='20sp',
            size_hint=(1, 0.15),
            background_color=get_color_from_hex("#2D2D44"),
            foreground_color=get_color_from_hex("#FFFFFF"),
            padding=[20, 20, 20, 20]
        )

        self.feedback_label = Label(
            text="",
            font_size='18sp',
            size_hint=(1, 0.15)
        )

        bouton_valider = Button(
            text="Valider",
            font_size='20sp',
            size_hint=(1, 0.15),
            background_color=get_color_from_hex("#5B8DEF"),
            background_normal=''
        )
        bouton_valider.bind(on_press=self.verifier_reponse)

        self.layout.add_widget(self.question_label)
        self.layout.add_widget(self.champ_reponse)
        self.layout.add_widget(self.feedback_label)
        self.layout.add_widget(bouton_valider)

        return self.layout

    def verifier_reponse(self, instance):
        reponse = self.champ_reponse.text.lower()
        bonne_reponse = questions[self.index][1].lower()

        if reponse == bonne_reponse:
            self.score += 1
            self.feedback_label.text = "✅ Correct !"
            self.feedback_label.color = get_color_from_hex("#4CAF50")
        else:
            self.feedback_label.text = "❌ Faux, c'était : " + bonne_reponse
            self.feedback_label.color = get_color_from_hex("#E74C3C")

        self.index += 1

        if self.index < len(questions):
            self.question_label.text = questions[self.index][0]
            self.champ_reponse.text = ""
        else:
            self.question_label.text = "Quiz terminé ! Score : " + str(self.score) + "/" + str(len(questions))
            self.champ_reponse.text = ""

QuizApp().run()