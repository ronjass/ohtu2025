from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self.matcher = All()

    def build(self):
        return self.matcher

    def plays_in(self, team):
        self.matcher = And(self.matcher, PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self.matcher = And(self.matcher, HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self.matcher = And(self.matcher, HasFewerThan(value, attr))
        return self

    