import pytest
import main

class TestSpeedingOutcome:

    def test_issue_ticket(self):
        assert main.speeding_outcome(30, 31) == (True, False)
