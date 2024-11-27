class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_call_for_score(self, score):
        calls = {}
        calls[0] = "Love"
        calls[1] = "Fifteen"
        calls[2] = "Thirty"
        calls[3] = "Forty"
        return calls[score]
    
    def get_leading_player_name(self):
        if self.player1_score > self.player2_score:
            return self.player1_name
        else:
            return self.player2_name

    def scores_are_equal(self):
        if self.player1_score >= 3:
            return "Deuce"
        else:
            return self.get_call_for_score(self.player1_score) + "-All"
        
    def score_is_more_than_four(self):
        difference = abs(self.player1_score - self.player2_score)
        if difference == 1:
            return "Advantage " + self.get_leading_player_name()
        else:
            return "Win for " + self.get_leading_player_name()
                    
    def scores_are_less_than_four(self):
        return self.get_call_for_score(self.player1_score) + "-" + self.get_call_for_score(self.player2_score)

    def get_score(self):

        if self.player1_score == self.player2_score:
            return self.scores_are_equal()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.score_is_more_than_four()
        
        else:
            return self.scores_are_less_than_four()
