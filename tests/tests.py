from sources.Creatures.WaterElem import WaterElem
from sources.Entity import Entity
from sources.Classes.Hunter import Hunter
from sources.Classes.Mage import Mage
from sources.Classes.Warrior import Warrior
from sources.Equipments.Armor import Armor
from sources.Equipments.Equipments import Equipments
from sources.Equipments.Weapon import Weapon


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


def test_weapon_creation():
    headhunter = Armor('Headhunter', 10)
    starforge = Weapon('Starforge', 3)

    assert (headhunter.name, headhunter.strength, headhunter.type_ == (
        'Headhunter',
        10,
        'Armor'
    ))
    assert (starforge.name, starforge.strength, starforge.type_ == (
        'Starforge',
        3,
        'Weapon'
    ))


def test_char_with_equipments():
    headhunter = Armor('Headhunter', 10)
    starforge = Weapon('Starforge', 3)
    char = Entity('Blob', 'Random', 2, Equipments(starforge, headhunter))

    assert char.equipments.weapon.name == 'Starforge'
    assert char.equipments.armor.name == 'Headhunter'

    mage = Mage('Merlin')
    assert mage.equipments.weapon.name == 'Staff'
    assert mage.equipments.armor.name == 'Wizard dress'
    assert mage.strength == 3

    hunter = Hunter('Gon')
    assert hunter.equipments.weapon.name == 'Bow'
    assert hunter.equipments.armor.name == 'Leather armor'
    assert hunter.strength == 16

    warrior = Warrior('Conan')
    assert warrior.equipments.weapon.name == 'Sword'
    assert warrior.equipments.armor.name == 'Full plate armor'
    assert warrior.strength == 27



