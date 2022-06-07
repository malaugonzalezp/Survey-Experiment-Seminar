from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start.

class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width']

#with the function before_next_page you can can control what should happen. It is a nice feature for filtering
#or also setting variables
    def before_next_page(self):
        #here we are increasing the counter for each player that goes past the Welcome Page
        self.group.counter += 1


class DemoPage(Page):
    form_model = Player
    form_fields = ['please_state_your_age', 'what_is_your_favorite_beverage', 'food', 'hidden_input']

class Html_overview(Page):
    form_model = Player
    form_fields = ['duck']
    def is_displayed(self):
        '''this is another otree specific function that regulates if a page is displayed or not '''
        #this will show the page to anybody who has the right assignment so in this case
        return self.player.group_assignment == 1


class PopoutPage(Page):
    form_model = Player
    form_fields = ['popout_question', 'popout_yes', 'popout_no', 'time_popout']


class EndPage(Page):
    def vars_for_template(self):
        '''this is another function by otree which allows you to "send" variables
        to html files if you need to access them from there'''
        return {"group_assignment": safe_json(self.player.group_assignment)}

    # style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player


# Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                 DemoPage,
                 Html_overview,
                 PopoutPage,
                 EndPage]
