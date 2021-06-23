# Markov Decision Process Example
# Author: Christina Dimitriadou (christina.delta.k@gmail.com)
# Date: 20/06/2021

# Import Libraries
import sys
sys.setrecursionlimit(1000)

# create the model:
class TestMDP(object):
    def __init__(self, N):
        self.N = N # N is the number of blocks

    def initialState(self):

        return 1

    def stateEnd(self, state):

        return state == self.N

    def actions(self, state):
        # returns a list of valid actions
        outcome = []

        if state+1 <= self.N:
            outcome.append('action_1')
        if state*2 <= self.N:
            outcome.append('action_2')

        return outcome

    def succProbReward(self, state, action):

        # returns list with: new state, probability, reward
        # state = s, action = a, new state = s', prob = T(s,a,s'), reward = Reward(s,a, s')
        outcome = []

        if action == 'action_1':
            outcome.append((state+1, 1., -1.))
        elif action == 'action_2':
            outcome.append((state*2, 0.5, -2.))
            otcome.append((state, 0.5, -2.))

        return outcome

    def discount(self):
        return 1.

    def states(self):
        return range(1, self.N+1)
