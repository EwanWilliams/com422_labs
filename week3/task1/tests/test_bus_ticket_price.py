import pytest
import main

class TestBusTicketPrice:

    def test_infant_price(self):
        assert main.bus_ticket_price(2) == 0
    
    def test_oap_price(self):
        assert main.bus_ticket_price(65) == 0
    
    def test_student_under_19_price(self):
        assert main.bus_ticket_price(18, True) == 2
    
    def test_student_19_plus_price(self):
        assert main.bus_ticket_price(19, True) == 4
    
    def test_3_to_64_price(self):
        assert main.bus_ticket_price(3) == 4
        assert main.bus_ticket_price(64) == 4
