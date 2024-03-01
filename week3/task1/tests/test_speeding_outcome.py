import pytest
import main

class TestSpeedingOutcome:

    def test_issue_ticket(self):
        assert main.speeding_outcome(30, 31) == (True, False)
    
    def test_issue_ticket_and_summon(self):
        assert main.speeding_outcome(30, 41) == (True, True)
        
    def test_issue_nothing(self):
        assert main.speeding_outcome(30, 30) == (False, False)