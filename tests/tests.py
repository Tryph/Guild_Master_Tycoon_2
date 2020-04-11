from sources.Creatures.WaterElem import WaterElem
from sources.Entity import Entity
from sources.Classes.Hunter import Hunter
from sources.Classes.Mage import Mage
from sources.Classes.Warrior import Warrior


def test_class_creation():
    char = Entity('Blob', 'Random', 2)
    mage = Mage('Merlin')
    hunter = Hunter('Gon')
    warrior = Warrior('Conan')
    water_elem = WaterElem()
    assert char.name, char.class_ == ('Blob', 'Random')
    assert mage.name, mage.class_ == ('Merlin', 'Mage')
    assert hunter.name, hunter.class_ == ('Gon', 'Hunter')
    assert warrior.name, warrior.class_ == ('Conan', 'Warrior')
    assert water_elem.name, water_elem.class_ == ('Water Elemental', 'Mage')


def test_fight_between_entities():
    merlin = Mage('Merlin')
    gon = Hunter('Gon')
    conan = Warrior('Conan')
    water_elem = WaterElem()

    assert not merlin - water_elem
    assert not merlin.fight(water_elem)
    assert gon - water_elem
    assert gon.fight(water_elem)
    assert conan - water_elem
    assert conan.fight(water_elem)

