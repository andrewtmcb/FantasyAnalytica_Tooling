from dataworld import league
class Team(object):

    def __init__(self, relativeIds, owner, active):

        self.relativeIds = relativeIds
        self.owner = owner
        self.active = active
        self.scores = []
        self.waivers = []


    # this must be done in order.
    def data_add(self,data,data_set_target):
        data_set_target.append(data)
