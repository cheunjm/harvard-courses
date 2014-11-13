"""
    This module provides the class that represents a POMDP model.

"""

class POMDP(object):
    """
    POMDP model class.

    :param tps: transition probabilities
    :type tps: 3d list indexed by [action][source][sink]
    :param ops: observ probabilities
    :type ops: 3d list indexed  by [action][state][observ]
    :param rws: rewards
    :type rws: 4d list indexed by [action][source][sink][observ]

    :param state_names: (optional) state names, default are indices
    :type state_names: list of strings
    :param action_names: (optional) action names, default are indices
    :type action_names: list of strings
    :param observ_names: (optional) observ names, default are indices
    :type observ_names: list of strings


    """

     def __init__(self,
                 state_names  = None,
                 action_names = None,
                 observ_names = None,
                 tps,
                 ops,
                 rws,
                 
                 name         = None):

        self.tps = tps
        self.ops = ops
        self.rws = rws

        self.states  = list(xrange(self.num_states))
        self.actions = list(xrange(self.num_actions))
        self.observs = list(xrange(self.num_observs))

        self.state_names       = state_names       or map(
                lambda n: 'state'      +str(n),self.states      )
        self.action_names      = action_names      or map(
                lambda a: 'action'     +str(a),self.actions     )
        self.observ_names = observ_names or map(
                lambda o: 'observ'+str(o),self.observs)

        self.name = name

    @property
    def num_states(self):
        """
        :return: number of states
        :rtype: int
        """
        return len(self.tps[0])

    @property
    def num_actions(self):
        """
        :return: number of actions
        :rtype: int
        """
        return len(self.tps)

    @property
    def num_observs(self):
        """
        :return: number of observs
        :rtype: int
        """
        return len(self.rws[0][0][0])


    def next_beliefs(self, belief_state, actions=None, observs=None):
        """
        Given a belief state return all possible belief states in the next step.

        :param belief_state: current belief state
        :type  belief_state: [float]

        :return: list of next step beliefs for each action/observ
                 combination
        :rtype: list of tuples (action, observ, belief)
        """
        actions = actions or self.actions
        observs = observs or self.observs

        situations = []

        for action in actions:
            for observ in observs:
                belief = self.update(belief_state, action, observ)
                situations.append((action,observ,belief))

        return situations


    def process_update(self, belief_state, action):
        """
        Apply process update of the given action to belief_state

        :param belief_state: current belief state
        :type  belief_state: list of doubles
        :param action: index of taken action
        :type  action: int

        :return: new belief state
        :rtype:  list of double
        """

        # add some weight to avoid 0., since b=[0,1] * a=[1,0] => b'=[0.,0.]
        belief_state = [b + EPSILON for b in belief_state]

        # b_{t+1}(s') = b_t(s) * T(s,a,s')
        t = numpy.array(self.tps[action])
        belief = numpy.array(belief_state)
        next_belief = numpy.dot(t, belief).tolist()

        # normalize belief
        next_belief = util.normalize(next_belief,val=1.0)

        return next_belief


    def observation_update(self, belief_state, action, observ):
        """
        Given a current belief state, an (last) action and an observ, return
        the new belief state: b'(s) = p(s|o) * b(s)

        :param belief_state: current belief state
        :type  belief_state: list of doubles
        :param action: index of taken action
        :type  action: int
        :param observ: index of perceived observ
        :type  observ: int

        :return: new belief state
        :rtype:  list of double
        """

        # add some weight to avoid 0., since b=[0,1] * o=[1,0] => b'=[0.,0.]
        belief_state = [b + EPSILON for b in belief_state]

        # apply observation to belief
        o_slice = [ i[observ] for i in self.ops[action]]
        next_belief = [b*o for b,o in zip(belief_state,o_slice)]

        # normalize belief
        next_belief = util.normalize(next_belief, val=1.0)
        return next_belief


    def update(self, belief_state, action, observ):
        """
        Given a current belief state, an action and an observ, return
        the new belief state applying the process and the observation model

        :param belief_state: current belief state
        :type  belief_state: [float]
        :param action: index of taken action
        :type  action: int
        :param observ: index of perceived observ
        :type  observ: int

        :return: next belief state
        :rtype:  [double]
        """
        intermediate_belief = self.process_update(belief_state, action)
        next_belief = self.observation_update(intermediate_belief, action, observ)
        return next_belief

