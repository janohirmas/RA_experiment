from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions2(Page):
    def is_displayed(self):
        return (self.round_number == Constants.num_practice_rounds + 1)

    # we do this ti transfer the variables from the game to questionnaire app in order to run the lottery
    def before_next_page(self):
        self.participant.vars['number_of_all_rounds'] = Constants.num_rounds
        self.participant.vars['number_of_practice_rounds'] = Constants.num_practice_rounds

class Attention(Page):
    def is_displayed(self):
        return (self.round_number == 1)
            
class Trial_and_decision(Page):
    form_model = 'player'
    form_fields = ['dec_X', 'DT_X', 'FN_gains_X', 'FN_losses_X', 'left_X', 'first_X', 'last_screen_X', 'last_fix_t']
    def vars_for_template(self):
        randomized_table = self.player.treatments_player()
        row_for_the_trial = randomized_table.iloc[self.player.row_number]
        return dict(
            original_trial_num = row_for_the_trial['original_trial_num_X'],
            FT_gain_X = row_for_the_trial['FT_gain_X'],
            FT_loss_X = row_for_the_trial['FT_loss_X'],
            Loss_X = row_for_the_trial['Loss_X'],
            Gain_X = row_for_the_trial['Gain_X']
        )
    def is_displayed(self):
        return self.round_number <= Constants.num_rounds #True
    # we do this to transfer the variables from the game to questionnaire app in order to run the lottery
    def before_next_page(self):
        self.participant.vars[str(self.round_number)] = [self.player.dec_X, self.player.Gain_X, self.player.Loss_X]
        # Compute time spent on gains and losses overal per trial
        t_gains = self.player.FT_gain_X * self.player.FN_gains_X
        t_losses = self.player.FT_loss_X * self.player.FN_losses_X
        # adjust the last fixation time
        if self.player.dec_X != 0:
            if self.player.last_screen_X == 0: #loss
                t_losses = t_losses - self.player.FT_loss_X + self.player.last_fix_t
            elif self.player.last_screen_X == 1: #gain
                t_gains = t_gains - self.player.FT_gain_X + self.player.last_fix_t
        self.player.t_gains_X = t_gains
        self.player.t_losses_X = t_losses
class Feedback(Page):
    def vars_for_template(self):
        return dict(
            dec_X = self.player.dec_X,
        )
    def is_displayed(self):
        return self.round_number <= Constants.num_rounds #True

class Confidence(Page):
    form_model = 'player'
    form_fields = ['conf_X', 'conf_RT_X']
    def is_displayed(self):
        dec_X = self.player.dec_X
        return (dec_X != 0) and (self.round_number <= Constants.num_rounds) #True

class ResultsWaitPage(WaitPage):
    pass

class Middle_page(Page):
    def is_displayed(self):
        return (self.round_number == Constants.num_practice_rounds + (Constants.num_trial_rounds//2))

page_sequence = [Instructions2, Attention, Trial_and_decision, Feedback, Confidence, Middle_page]
