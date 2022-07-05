import random

def random_number(x, y):
    '''
    method for random integers
    '''
    rng = random.Random()
    number = rng.randint(x, y)
    return number


def detect_screenout(self):
    '''this function will check for characteristics a participant needs to
    take part in the survey, (f.e. a certain age or being eligible to vote)'''

    if self.player.eligible_question == 4: # screen out anybody who is 40+
        self.player.screenout = 1

def detect_quota(self):
    '''this function will check if a quota is already filled'''
    participant_number = self.group.counter
    #declare quota reached if we have more than 1 participant that started

    if self.player.gender == 1:      # if participant is male
        if participant_number > 2:       # if more than 2 males participate
            self.player.quota = 1

    if self.player.gender == 2:      # if participant is female
        if participant_number > 2:        # if more than 2 females participate
            self.player.quota = 1

    if self.player.gender == 3:      # if participant is other
        if participant_number > 2:      # if more than 2 other participate
            self.player.quota = 1

    if self.player.gender == 4:      # if participant is prefer not to say
        if participant_number > 2:      # if more than 2 participate
            self.player.quota = 1

