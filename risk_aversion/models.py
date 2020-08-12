from numpy import random
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

author = 'Evgeny Vasilets'

doc = """
This is the experiment investigating the nature of loss-aversion.
"""


class Constants(BaseConstants):
    name_in_url = 'risk_aversion'
    players_per_group = None
    num_trial_rounds = 48
    num_practice_rounds = 3
    num_rounds = num_trial_rounds + num_practice_rounds


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
# variables that are saved for each participant
    # demographic questions
    demography_age = models.IntegerField(label="Your age")
    demography_country = models.StringField(label="What country do you live in now?")
    demography_gender = models.IntegerField( label="What is your gender?", choices=[
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Other'],
    ])

    # anwers to the questions checking the understanding of instructions
    q1 = models.StringField(label="How many decisions are you going to make (without counting the practice trials)?", blank = True)
    q2 = models.StringField(label = "How many outcomes will affect your payment?", blank = True)
    q3 = models.IntegerField(
        label="To accept a lottery, you need to press:",
        choices=[
            [1, '↑'],
            [2, '↓']
        ],
        blank = True
    )
    q4 = models.IntegerField(
        label="Can the lottery, selected in the end, come from the first 3 trials?",
        choices=[
            [1, 'Yes'],
            [2, 'No']
        ],
        blank = True
    )
    # random generated int that defines randomisation order for each participant
    rand_int = models.IntegerField()
    cluster = models.IntegerField()
    # number of a trial in a non-randomised data-frame
    original_trial_num = models.IntegerField()
    # 1 = accepted, 0 = rejected
    decision = models.IntegerField(blank=True)
    # -1 - smaller, 0 - equal, 1 - larger
    last_fix_condition = models.IntegerField()
    # gain or loss
    first_fix_value = models.StringField()
    # gain or loss
    last_fix_value = models.StringField()
    # 2,3, 4 or 5
    number_of_fixations = models.IntegerField()
    # values in ECU
    lose_value = models.IntegerField()
    gain_value = models.IntegerField()
    # time per each fixation for losses and gains (if the number of fixations is smaller than 5,
    lose_time_1 = models.FloatField()
    lose_time_2 = models.FloatField()
    lose_time_3 = models.FloatField()
    lose_time_4 = models.FloatField()
    lose_time_5 = models.FloatField()
    gain_time_1 = models.FloatField()
    gain_time_2 = models.FloatField()
    gain_time_3 = models.FloatField()
    gain_time_4 = models.FloatField()
    gain_time_5 = models.FloatField()
    # binary: 0 - real trials, 1 - training trials
    practice_trial = models.IntegerField()
    # win or lose
    row_number = models.IntegerField()
    # how much a participant wins/loses
    lottery_result = models.IntegerField(blank=True)
    # time per decision in ms
    decision_time_ms = models.IntegerField(blank= True)
    # write down gains and loss conditions (high or low)
    gain_condition = models.StringField()
    loss_condition = models.StringField()

    def lottery(self):
    # this function defines how ,uch a participant wins or loses at the end of the experiment.
        values = []
        for ind in range(Constants.num_rounds):
            rnd_num = ind+1
            if (self.in_round(rnd_num).decision == 1) & (self.in_round(rnd_num).practice_trials() == 0):
                win_value = random.choice([self.in_round(rnd_num).gain_value, self.in_round(rnd_num).lose_value])
                values.append(win_value)
        if not values:
            final_value = 0
        else:
            final_value = random.choice(values)
        return final_value

    def treatments_player(self):
        # create the dictionary with the variables
        treatments_dic = {
            'original_trial_num': [],
            'cluster': [],
            'last_fix_condition': [],
            'first_fix_value': [],
            'last_fix_value': [],
            'number_of_fixations': [],
            'lose_value': [],
            'gain_value': [],
            'gain_condition':[],
            'loss_condition':[],
            'lose_times': [],
            'gain_times': [],
        }


        clusters = [0, 1]  # 0 - fast scanning (1 or 2 fixations), 1 - long fixations (3,4 or 5 fix)
        last_fix_conditions = [-1, 0, 1]  # -1 - shorter, 0 - equal, 1 - longer
        low_losses = list(range(-13, -21, -1))
        high_losses = list(range(-21, -28, -1))
        losses_lists = [high_losses, low_losses]

        low_gains = list(range(20, 29, 1))
        high_gains = list(range(29, 39, 1))
        gains_lists = [low_gains, high_gains]
        last_fixes = ['gain', 'loss']
        trial_time_clus0 = 1.365
        trial_time_clus1 = 2.110
        # what is (in %) the last fixation difference is?
        last_fix_larger_by = .25
        count = 1
        # use for loop to create all combinations of treatments
        for clus in clusters:
            for last_fix_condition in last_fix_conditions:
                    for gains in gains_lists:
                        for losses in losses_lists:
                            for last_fix_val in last_fixes:
                                gain = random.choice(gains)
                                lose = random.choice(losses)
                                treatments_dic['original_trial_num'].append(count)
                                treatments_dic['cluster'].append(clus)
                                treatments_dic['last_fix_condition'].append(last_fix_condition)
                                treatments_dic['lose_value'].append(lose)
                                treatments_dic['gain_value'].append(gain)
                                if gains == low_gains:
                                    treatments_dic['gain_condition'].append('low_gains')
                                elif gains == high_gains:
                                    treatments_dic['gain_condition'].append('high_gains')
                                if losses == high_losses:
                                    treatments_dic['loss_condition'].append('high_losses')
                                elif losses == low_losses:
                                    treatments_dic['loss_condition'].append('low_losses')
                                if clus == 0:
                                    fix_num = 2
                                    treatments_dic['number_of_fixations'].append(2)
                                    time_per_fix = trial_time_clus0 / fix_num
                                elif clus == 1:
                                    # define how many fixations will there be
                                    fix_num = random.randint(3, 5)
                                    treatments_dic['number_of_fixations'].append(fix_num)
                                    time_per_fix = trial_time_clus1 / fix_num
                                # compute lose and gain times
                                time_per_fix_larger = time_per_fix * (1 + last_fix_larger_by)
                                time_per_fix_smaller = time_per_fix * (1 - last_fix_larger_by)
                                lose_times = []
                                gain_times = []
                                first_value = None

                                # define whether gains or losses are shown last
                                treatments_dic['last_fix_value'].append(last_fix_val)
                                # now define which value will be shown first
                                if (fix_num % 2 == 0) & (last_fix_val == 'gain'):
                                    first_value = 'loss'
                                elif (fix_num % 2 == 0) & (last_fix_val == 'loss'):
                                    first_value = 'gain'
                                elif (fix_num % 2 != 0) & (last_fix_val == 'gain'):
                                    first_value = 'gain'
                                elif (fix_num % 2 != 0) & (last_fix_val == 'loss'):
                                    first_value = 'loss'
                                treatments_dic['first_fix_value'].append(first_value)
                                # create arrays that will include all fixation times
                                for time_ind in range(fix_num):
                                    # check if it's a first fixation to mitigate the reaction delay
                                    if time_ind == 0:
                                        time_per_fix = time_per_fix + .165
                                    if (first_value == 'gain') & ((time_ind % 2) == 0):
                                        gain_times.append(time_per_fix)
                                    elif (first_value == 'loss') & ((time_ind % 2) == 0):
                                        lose_times.append(time_per_fix)
                                    elif (first_value == 'gain') & ((time_ind % 2) != 0):
                                        lose_times.append(time_per_fix)
                                    elif (first_value == 'loss') & ((time_ind % 2) != 0):
                                        gain_times.append(time_per_fix)
                                    # substract the error time if this was the first fixation
                                    if time_ind == 0:
                                        time_per_fix = time_per_fix - .165
                                    if time_ind == fix_num - 1:
                                        if last_fix_condition == 1:
                                            if last_fix_val == 'gain':
                                                gain_times[-1] = time_per_fix_larger
                                            elif last_fix_val == 'loss':
                                                lose_times[-1] = time_per_fix_larger
                                        elif last_fix_condition == -1:
                                            if last_fix_val == 'gain':
                                                gain_times[-1] = time_per_fix_smaller
                                            elif last_fix_val == 'loss':
                                                lose_times[-1] = time_per_fix_smaller
                                # add the fixation times to the dictionary
                                treatments_dic['lose_times'].append(lose_times)
                                treatments_dic['gain_times'].append(gain_times)
                                count += 1
        treatments_df = pd.DataFrame(treatments_dic)
        # randomize the table using random-generated number (which will be the same for all trials for a specific participant)
        randomized = treatments_df.sample(frac=1, random_state=self.in_round(1).rand_int)
        # re-index the new table in order so we could present the new randomized table from start to the end
        randomized['new_indexing'] = list(range(0, len(randomized)))
        randomized = randomized.set_index(randomized['new_indexing'])
        # Check whether the trials are practice to decide whether to show random or
        # ordered rows from the randomized table
        pt = self.practice_trials()
        if pt == 0:
            row_number = self.round_number - 1 - Constants.num_practice_rounds
        elif pt == 1:
            row_number = random.randrange(0, len(randomized))
        # write down the data for the participant for each row so we can see it during the data analysis
        self.original_trial_num = randomized.loc[row_number, 'original_trial_num']
        self.cluster = randomized.loc[row_number, 'cluster']
        self.lose_value = randomized.loc[row_number, 'lose_value']
        self.gain_value = randomized.loc[row_number, 'gain_value']
        self.last_fix_condition = randomized.loc[row_number, 'last_fix_condition']
        self.first_fix_value = randomized.loc[row_number, 'first_fix_value']
        self.last_fix_value = randomized.loc[row_number, 'last_fix_value']
        self.number_of_fixations = randomized.loc[row_number, 'number_of_fixations']
        self.row_number = row_number
        self.gain_condition = randomized.loc[row_number, 'gain_condition']
        self.loss_condition = randomized.loc[row_number, 'loss_condition']
        # Create distinct variables for all fix times
        row_gain_times = randomized.loc[row_number, 'gain_times']
        row_lose_times = randomized.loc[row_number, 'lose_times']
        for index in range(1,6):
            var = 'lose_time_'+str(index)
            if len(row_lose_times) < index:
                lose_fix_time = 0
            else:
                lose_fix_time = row_lose_times[index-1]
            exec("self.%s = %f" % (var, lose_fix_time))
            var = 'gain_time_' + str(index)
            if len(row_gain_times) < index:
                gain_fix_time = 0
            else:
                gain_fix_time = row_gain_times[index-1]
            exec("self.%s = %f" % (var, gain_fix_time))
        return randomized
    def practice_trials(self):
        # this function defines whether these trials are training or real
        if self.round_number > Constants.num_practice_rounds:
            self.practice_trial = 0
            return 0
        else:
            self.practice_trial = 1
            return 1


