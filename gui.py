from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
import match_cv
import binary_search_tree
from kivymd.uix.list import ThreeLineListItem
from kivy.animation import Animation
import webbrowser


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.match_cv = match_cv
        self.cv_files = []
        self.bst = binary_search_tree
        self.help_open = False

    def on_enter(self, *args):
        Window.bind(on_dropfile=self._on_file_drop)

    def _on_file_drop(self, window, file_path):
        self.cv_files.append(file_path)
        self.ids.cv_lst.add_widget(MDLabel(text=str(file_path)))
        return

    def match(self):
        values = []
        sk = self.ids["sk"].text.lower().split(",")
        hk = self.ids["hk"].text.lower().split(",")
        vals = (int(self.ids["hk_slider"].value)/10, int(self.ids["sk_slider"].value)/10)
        theTree = self.bst.Tree(vals)
        for cv in self.cv_files:
            name = str(cv)
            temp = (name,)
            temp += self.match_cv.Match(cv, sk, hk).match_keywords()
            values.append(temp)
        theTree.create_tree(values)
        theTree.preOrderTrav(theTree.root)
        self.display_results(theTree.sorted_nodes)

    def display_results(self, nodes):
        anim = Animation(pos_hint={"center_x": 0.5}, duration=0.5)
        anim.start(self.ids["res_card"])
        for itm in nodes:
            start = itm[0].rfind("/")
            end = itm[0].find(".pdf")
            name = itm[0][start+1:end]
            self.ids.res_lst.add_widget(
                ThreeLineListItem(id=itm[0],
                                  text=name,
                                  secondary_text=f'Hard Keys match: {int(itm[1])}% Soft Keys match: {int(itm[2])}%',
                                  tertiary_text=f'Distance to Ideal Candidate: {int(itm[3])} lu', on_release=self.opn_file)
            )

    def opn_file(self, instance):
        start = instance.id.find("/")
        ref_id = instance.id[start:len(instance.id)-1]
        webbrowser.open_new(ref_id)

    def go_back(self):
        anim = Animation(pos_hint={"center_x": -0.5}, duration=0.5)
        anim.start(self.ids["res_card"])
        self.ids.res_lst.clear_widgets()

    def help(self):
        if (not self.help_open):
            anim = Animation(pos_hint={"center_y": 0.3}, duration=0.3)
            anim.start(self.ids["help_card"])
            self.help_open = True
            self.ids["hl_left"].text = """
                HOW TO USE
                Drag & Drop pdf files to the window.
                The files loaded will be shown in a list.
                Input keywords that you would like
                to search the CVs for.
                
                When the "Match" key is pressed the
                different files get measured against
                the "ideal candidate" which gets
                calculated out of the significance
                sliders.
                Lower distance from the
                "ideal candidate" means a higher
                match value.
            """
            self.ids["hl_right"].text = """
                HARD KEYS
                These are skills such as "carpentry"
                or "programming"
                Use colon-sign to separate skills
                
                SOFT KEYS
                These are attributes such as "positive"
                or "pragmatic"
                Use colon to separate attributes
                
                SIGNIFICANCE SLIDERS
                These values the hard/soft keys.
                Higher Value gets the hard/soft keys valued
                higher.
                
                READ THE CV
                Simply click the CV in the match-list
                to open it. (This works in Linux)
            
            """
        else:
            anim = Animation(pos_hint={"center_y": -0.5}, duration=0.3)
            anim.start(self.ids["help_card"])
            self.help_open = False

class WindowManager(ScreenManager):
    pass

class ApplicationClassifier(MDApp):
    Window.size = (800, 900)
    def build(self):
        wm = WindowManager()
        wm.add_widget(MainScreen())
        return wm




if __name__ == "__main__":
    ApplicationClassifier().run()



