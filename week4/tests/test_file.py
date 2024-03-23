from Dog import Dog
from Enclosure import Enclosure
from Kennel_Company import Kennel_Company
import pytest

def load_enclosures_stub(self):
    return [
        Enclosure(1, 10, 7),
        Enclosure(2, 15, 1)
    ]

#[Dog("Fido", "Dan", 3, "Spaniel", "N/A"), Dog("Millie", "Ewan", 11, "Doodle", "Special Food")]
#[Dog("Barney", "Charlie", 4, "Newfie", "Big")]

@pytest.fixture
def kennel_example(monkeypatch):
    monkeypatch.setattr(Kennel_Company, 'load_enclosures', load_enclosures_stub)
    kennel = Kennel_Company()
    return kennel


def test_book_dog(monkeypatch, kennel_example):
    # Book 2 dogs in to the kennels
    monkeypatch.setattr(Enclosure, 'check_suitability', lambda args, dog: True)
    monkeypatch.setattr(Enclosure, 'add_occupant', lambda self, dog: self.occupants.append(dog))
    kennel_example.book_dog(Dog("new", "new", 0, "new", "new"))
    kennel_example.book_dog(Dog("new2", "new2", 0, "new2", "new2"))
    # Check that the overall number of spaces left in the kennels is correct after the 2 bookings
    assert kennel_example.spaces_left() == 6


def test_remove_dog(monkeypatch, kennel_example):
    # Create a kennel company
    # The kennel company will need to have at least 1 dog staying with it - facilitate this
    kennel_example.enclosures[0].occupants.append(Dog("Barney", "Charlie", 4, "Newfie", "Big"))
    # Remove the dog
    monkeypatch.setattr(Kennel_Company, 'is_authorised', lambda args: True)
    kennel_example.remove_dog("Barney")
    # Check that the overall number of spaces left is correct after the removal
    assert kennel_example.spaces_left() == 8
