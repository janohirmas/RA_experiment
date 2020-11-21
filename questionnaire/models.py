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

import pandas as pd
import random

author = 'Your name here'

doc = """
This app records answers to demographic questions and impulsivity questionnaire.
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # variables for Questionnaire
    QT1 = models.IntegerField(label=' I plan tasks carefully.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT2 = models.IntegerField(label=' I do things without thinking.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT3 = models.IntegerField(label=' I make-up my mind quickly.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT4 = models.IntegerField(label=' I am happy-go-lucky.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT5 = models.IntegerField(label=' I don’t “pay attention.”',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT6 = models.IntegerField(label=' I have “racing” thoughts.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT7 = models.IntegerField(label=' I plan trips well ahead of time.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT8 = models.IntegerField(label=' I am self controlled.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT9 = models.IntegerField(label=' I concentrate easily.',
                              choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                       [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT10 = models.IntegerField(label=' I save regularly.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT11 = models.IntegerField(label=' I “squirm” at plays or lectures.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT12 = models.IntegerField(label=' I am a careful thinker.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT13 = models.IntegerField(label=' I plan for job security.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT14 = models.IntegerField(label=' I say things without thinking.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT15 = models.IntegerField(label=' I like to think about complex problems.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT16 = models.IntegerField(label=' I change jobs.', choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                                                 [4, 'Almost Always/Always']],
                               widget=widgets.RadioSelectHorizontal)
    QT17 = models.IntegerField(label=' I act “on impulse.”',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT18 = models.IntegerField(label=' I get easily bored when solving thought problems.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT19 = models.IntegerField(label=' I act on the spur of the moment.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT20 = models.IntegerField(label=' I am a steady thinker.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT21 = models.IntegerField(label=' I change residences.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT22 = models.IntegerField(label=' I buy things on impulse.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT23 = models.IntegerField(label=' I can only think about one thing at a time.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT24 = models.IntegerField(label=' I change hobbies.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT25 = models.IntegerField(label=' I spend or charge more than I earn.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT26 = models.IntegerField(label=' I often have extraneous thoughts when thinking.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT27 = models.IntegerField(label=' I am more interested in the present than the future.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT28 = models.IntegerField(label=' I am restless at the theater or lectures.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT29 = models.IntegerField(label=' I like puzzles.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT30 = models.IntegerField(label=' I am future oriented.',
                               choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                        [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    QT_check = models.IntegerField(label='Please indicate "Often" in this question.',
                                   choices=[[1, 'Rarely/Never'], [2, 'Occasionally'], [3, 'Often'],
                                            [4, 'Almost Always/Always']], widget=widgets.RadioSelectHorizontal)
    # demographic questions

    demography_age = models.IntegerField(label="Your age", max=99, min=5)
    demography_country = models.StringField(label="What country do you live in now?", blank=True)
    demography_gender = models.IntegerField(label="Which gender do you identify most with?", choices=[
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Other'],
        [4, 'Prefer not to say']
    ])
    demography_nationality = models.StringField(label="Nationality", blank=True)
    q_statistics = models.IntegerField(label="Have you ever been instructed in Statistics and/or Calculus?", choices=[
        [1, 'Yes'],
        [2, 'No'],
        [3, 'Do not know']
    ], widget=widgets.RadioSelect)
    q_study = models.StringField(label="What did you study?", blank=True)
    q_purpose = models.LongStringField(label="What do you think it was the purpose of this study?", blank=True)
    q_strategy_binary = models.IntegerField(label="Did you use a specific strategy?", choices=[
        [1, "Yes"],
        [2, "No"]
    ], widget=widgets.RadioSelect)
    strategy = models.LongStringField(
        label="Could you explain how did you decide to accept or reject the gambles in each trial? (max - 250 characters)",
        max_length=250, blank=True)
    q_other_exp = models.IntegerField(
        label="Have you ever participated in an incentivized economic experiment like this one?", choices=[
            [1, "Yes"],
            [2, "No"],
            [3, "Do not know"]
        ], widget=widgets.RadioSelect)
    q_improve = models.LongStringField(
        label="Please help us improve our previous studies. Was there something that was not clear in the instructions? (max - 250 characters)",
        max_length=250, blank=True)
    q_own_corona_concern = models.IntegerField(
        label="Are you concerned about your own health due to the novel coronavirus?", choices=[
            [1, "Very concerned"],
            [2, "Concerned"],
            [3, "Neither concerned nor unconcerned"],
            [4, "Unconcerned"],
            [5, "Very Unconcerned"]
        ], widget=widgets.RadioSelect)
    q_relat_corona_concern = models.IntegerField(
        label="Are you concerned about the health of your family members due to the Covid-19?", choices=[
            [1, "Very concerned"],
            [2, "Concerned"],
            [3, "Neither concerned nor unconcerned"],
            [4, "Unconcerned"],
            [5, "Very Unconcerned"]
        ], widget=widgets.RadioSelect)
    # q_own_corona_likelihood = models.IntegerField(
    #     label="How likely do you think it is, that you will get infected by Covid-19 and experience serious health problems before the end of 2021?",
    #     choices=[
    #         [1, "Very Unlikely"],
    #         [2, "Unlikely"],
    #         [3, "Neither unlikely nor likely"],
    #         [4, "Likely"],
    #         [5, "Very Likely"]
    #     ], widget=widgets.RadioSelect)
    # q_relat_corona_likelihood = models.IntegerField(
    #     label="How likely do you think it is, that someone you know will die from Covid-19 before the end of 2021?",
    #     choices=[
    #         [1, "Very Unlikely"],
    #         [2, "Unlikely"],
    #         [3, "Neither unlikely nor likely"],
    #         [4, "Likely"],
    #         [5, "Very Likely"]
    #     ], widget=widgets.RadioSelect)
    # how much a participant wins/loses
    lottery_result = models.IntegerField(blank=True)
    # 0 = false, 1 = true
    fullscreen_second_check = models.IntegerField()
    def lottery(self):
        random.seed(self.participant.vars['rand_int'])
        winning_round = random.choice(range(self.participant.vars['number_of_practice_rounds']+1, self.participant.vars['number_of_all_rounds']+1))
        decision_in_winning_round, winning_value_gain, winning_value_loss = self.participant.vars[str(winning_round)]
        # if accepted
        if decision_in_winning_round == 2:
            random.seed(self.participant.vars['rand_int'])
            final_value = random.choice([winning_value_loss, winning_value_gain])
        # if no choice
        elif decision_in_winning_round == 0:
            final_value = winning_value_loss
        # if rejected
        else:
            final_value = 0
        final_value_and_lottery = [final_value, winning_round, decision_in_winning_round]
        return final_value_and_lottery
