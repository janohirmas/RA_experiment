from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['consent']

    def is_displayed(self):
        return True


class ConsentIfFalse(Page):
    def is_displayed(self):
        return (self.player.in_round(1).consent == 2)


class Instructions(Page):
    form_model = 'player'
    form_fields = ['rand_int', 'q1', 'q2', 'q3', 'q4']

    def is_displayed(self):
        return (self.round_number == 1) and (self.player.in_round(1).consent == 1)

    def error_message(self, values):
        if (values['q1'] != "44") or (values['q2'] != "1") or (values['q3'] != 1) or (values['q4'] != 2):
            return 'Some of your answers contain an error'

    def before_next_page(self):
        self.participant.vars['rand_int'] = self.player.rand_int
        self.player.prolific_id = self.participant.label



class FullScreenPrompt(Page):
    form_model = 'player'
    form_fields = ['fullscreen']
    def is_displayed(self):
        return True


page_sequence = [ConsentForm, ConsentIfFalse, Instructions, FullScreenPrompt]
