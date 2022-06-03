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

author = 'My name is Maria Gonzalez'
doc = 'Test for implementing an online survey in oTree'


class Constants(BaseConstants):
    name_in_url = 'Homework_Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    counter = models.IntegerField(initial=0)
    # this is how you can implement variables that can be used by every player
    # they are called group variables and useful for example when quota checking


class Player(BasePlayer):
    # this is the most important feature of this file. We can collect all the variables used on the html pages here

    # The Variables are structured on the base of pages
    please_state_your_age = models.IntegerField(max=110, min=1)  # we can also have max and min guidelines
    what_is_your_favorite_beverage = models.StringField(blank=True)  # this is an optional field through blank = True
    food = models.IntegerField(initial=-999)  # we can add an initial value
    hidden_input = models.IntegerField(initial=50, blank=True)

    # custom error message
    # has to:
    # 1) be in the class Player (important to indent the right way)
    # 2) have a specific name "variablename"_error_message
    def age_question_error_message(player, value):
        if value > 80:
            return 'Age invalid. Please try again'
