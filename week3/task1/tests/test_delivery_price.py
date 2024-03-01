import pytest
import main

class TestDeliveryPrice:

    def test_price_under_10m_over_100p(self):
        assert main.delivery_price(100, 10) == 0
    
    def test_price_under_10m_under_100p(self):
        assert main.delivery_price(99, 10) == 5
    
    def test_price_over_10m(self):
        assert main.delivery_price(99, 11) == 10

    def test_price_over_20m(self):
        assert main.delivery_price(99, 21) == 15
    
    def test_price_over_30m(self):
        assert main.delivery_price(99, 31) == 15.5
        assert main.delivery_price(99, 35) == 17.5
