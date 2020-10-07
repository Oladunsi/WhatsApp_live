from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget

class MainApp(MDApp):
    def on_start(self):
        #Set colors
        self.theme_cls.primary_palette= "Teal"

        #Add messages
        self.new_message("Oladunsi", "Hello World","git.jpg")
        self.new_message("Google", "Lewis Hamilton will hope to equal the record for Formula One race wins at the second attempt at the Eifel Grand Prix this weekend.","Images/Uduma.jpg")
        self.new_message("Seun", "Hamilton's chances of equalling the record in Sochi were dealt a significant blow by a 10-second penalty for doing two illegal practice starts prior to the race.","Images/SEUN.jpg")
        self.new_message("Ola", "The midfielder was the Spanish club's best player as Atletico beat Liverpool 3-2 at Anfield - knocking them out of the competition they were defending in the Round of 16.","Images/Ola.jpg")
        self.new_message("Uduma", "Manchester United's leaders questioned as Solskjaer told to be ruthless with players","Images/Google.jpg")
        self.new_message("Yomi", "Southampton's funny transfer 'warning' after Liverpool skipper Jordan Henderson's Danny Ings love-in","Images/Oni.jpg")
        self.new_message("Odun", "Sky Sports has live and exclusive broadcasting rights in the United Kingdom with the build-up to the F1 race starting from 11:30am ahead of lights out at 1:10pm.","Images/Odun.jpg")



    def new_message(self, name, message, image_name):
        new_message = TwoLineAvatarIconListItem(text=name, secondary_text=message)
        new_message.add_widget(ImageLeftWidget(source=image_name))
        self.root.ids.list.add_widget(new_message)

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs
        :param instance_tab: <__main__.Tab object
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object
        :param tab_text: text or name icon of tab;
        '''
        pass




class Tab(FloatLayout,MDTabsBase):
    """docstring for header tabs."""
MainApp().run()
