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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rand_int = models.IntegerField()
    prolific_id = models.StringField()
    # answers to the questions checking the understanding of instructions
    q1 = models.StringField(label="How many decisions are you going to make (without counting the practice trials)?",
                            blank=True)
    q2 = models.StringField(label="How many outcomes will be selected for payment?", blank=True)
    q3 = models.IntegerField(
        label="To accept a lottery, you need to press:",
        choices=[
            [1, '↑'],
            [2, '↓']
        ],
        blank=True
    )
    q4 = models.IntegerField(
        label="Can the lottery, selected in the end, come from the first 3 trials?",
        choices=[
            [1, 'Yes'],
            [2, 'No']
        ],
        blank=True
    )
    consent = models.IntegerField(choices=[
        [1, 'I agree to the conditions and want to participate in the study.'],
        [2, 'I do not agree to participate.']
    ], widget=widgets.RadioSelect)

    # 0 = false, 1 = true
    fullscreen = models.IntegerField()


