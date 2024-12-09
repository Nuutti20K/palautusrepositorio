from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, query = All(), matchers = []):
        self.matchers = matchers
        self.matchers.append(query)

    def build(self):
        return And(self.matchers)

    def plays_in(self, team):
        return QueryBuilder(PlaysIn(team), self.matchers)
    
    def has_at_least(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr), self.matchers)
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr), self.matchers)