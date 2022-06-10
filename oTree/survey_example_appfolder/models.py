from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


import random

from survey_example_appfolder.HelperFunctions import random_number

author = 'My name is Maria Gonzalez'
doc = 'Test for implementing an online survey in oTree'


class Constants(BaseConstants):
    name_in_url = 'Homework_Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        '''this is a function by otree (same can not be changed)
        which is creating a new subsession. Any variables that are needed to be custom
        (so declaring it in a different way before) are created here'''
        for p in self.get_players():
            #here we want to declare the players to different groups (2 in total)
            #we use a python function here from 'random' we imported earlier
            p.group_assignment = random.Random().randint(0, 1)
            #or:
            #p.group_assignment = random_number(0,2)


class Group(BaseGroup):
    counter = models.IntegerField(initial=0)
    # this is how you can implement variables that can be used by every player
    # they are called group variables and useful for example when quota checking


class Player(BasePlayer):
    # this is the most important feature of this file. We can collect all the variables used on the html pages here
    screenout = models.BooleanField(initial=0)
    quota = models.BooleanField(initial=0)

    # The Variables are structured on the base of pages
    # WelcomePage
    device_type = models.IntegerField(initial=-999)
    operating_system = models.IntegerField(initial=-999)
    screen_height = models.IntegerField(initial=-999)
    screen_width = models.IntegerField(initial=-999)
    eligible_question = models.IntegerField()
    gender = models.IntegerField(initial=-999, label='Gender Question')
    #HtmlPage
    duck = models.IntegerField(initial=-999)
    # DemoPage
    please_state_your_age = models.IntegerField()  # we can also have max and min guidelines
    what_is_your_favorite_beverage = models.StringField(blank=True)  # this is an optional field through blank = True
    food = models.IntegerField(initial=-999)  # we can add an initial value
    hidden_input = models.IntegerField(initial=50, blank=True)
    # PopoutPage
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    time_popout = models.StringField(initial='-999')
    # EndPage
    group_assignment = models.IntegerField()

    # custom error message
    # has to:
    # 1) be in the class Player (important to indent the right way)
    # 2) have a specific name "variablename"_error_message
    def age_question_error_message(player, value):
        if value > 40:
            return 'Age invalid. Please try again'
