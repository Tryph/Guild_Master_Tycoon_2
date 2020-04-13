import random

from pytest import fixture

from sources.Creatures.WaterElem import WaterElem
from sources.Entity import Entity, Mage, Hunter, Warrior
from sources.Equipments.Equipments import Equipments, Armor, Weapon
from sources.Characts.Characts import Strength, Intelligence, Dexterity, \
    Characts, HitPoint, Wounds, AttackSpeed


@fixture
def strength():
    return Strength(5)


@fixture
def intelligence():
    return Intelligence(10)


@fixture
def dexterity():
    return Dexterity(20)


@fixture
def hit_point():
    return HitPoint(50)


@fixture
def wounds():
    return Wounds(3)


@fixture
def attack_speed():
    return AttackSpeed(1.)


@fixture
def characts(strength, intelligence, dexterity, hit_point, wounds):
    return Characts(strength, intelligence, dexterity, hit_point, wounds)


@fixture
def mage():
    return Mage('Merlin')


@fixture
def hunter():
    return Hunter('Gon')


@fixture
def warrior():
    return Warrior('Conan')


@fixture
def water_elem():
    return WaterElem()


@fixture
def weapon(characts):
    return Weapon('Starforge', characts)


@fixture
def armor(characts):
    return Armor('Headhunter', characts)


@fixture
def equipments(weapon, armor):
    return Equipments(weapon, armor)


def test_class_creation(characts):
    char = Entity('Blob', 'Random', characts)
    assert char.name == 'Blob'
    assert char.class_ == 'Random'

    mage = Mage('Merlin')
    assert mage.name == 'Merlin'
    assert mage.class_ == 'Mage'

    hunter = Hunter('Gon')
    assert hunter.name == 'Gon'
    assert hunter.class_ == 'Hunter'

    warrior = Warrior('Conan')
    assert warrior.name == 'Conan'
    assert warrior.class_ == 'Warrior'

    water_elem = WaterElem()
    assert water_elem.name == 'Water Elemental'
    assert water_elem.class_ == 'Mage'


def test_fight_between_entities(mage, hunter, warrior, water_elem):
    random.seed(0)
    assert mage - water_elem
    assert mage.fight(water_elem)
    assert hunter - water_elem
    assert hunter.fight(water_elem)
    assert warrior - water_elem
    assert warrior.fight(water_elem)


def test_stats():
    strength = Strength(5)
    assert strength == 5
    assert type(strength()) is int

    intelligence = Intelligence(10)
    assert intelligence == 10
    assert type(intelligence()) is int

    dexterity = Dexterity(20)
    assert dexterity == 20
    assert type(dexterity()) is int

    hit_point = HitPoint(50)
    assert hit_point == 50
    assert type(hit_point()) is int

    wounds = Wounds(3)
    assert wounds == 3
    assert type(wounds()) is int

    attack_speed = AttackSpeed(3.)
    assert attack_speed == 3.
    assert type(attack_speed()) is float

    statistics = Characts(strength, intelligence, dexterity, hit_point)
    assert statistics.strength == 5
    assert statistics.intelligence == 10
    assert statistics.dexterity == 20
    assert statistics.hit_point == 50

    statistics = Characts(10, 5, 2, 42)
    assert statistics.strength == 10
    assert statistics.intelligence == 5
    assert statistics.dexterity == 2
    assert statistics.hit_point == 42
    assert statistics() == (10, 5, 2, 42)

    statistics = Characts(wounds=wounds)
    assert statistics.strength == 0
    assert statistics.intelligence == 0
    assert statistics.dexterity == 0
    assert statistics.hit_point == 0
    assert statistics.wounds == 3


def test_equipment_with_stat(characts):
    headhunter = Armor('Headhunter', characts)
    assert headhunter.type_ == 'Armor'
    assert headhunter.name == 'Headhunter'
    assert headhunter.characts() == (5, 10, 20, 50, 3)


def test_equipment_creation(characts):
    headhunter = Armor('Headhunter', characts)
    assert headhunter.name == 'Headhunter'
    assert headhunter.characts() == (5, 10, 20, 50, 3)
    assert headhunter.type_ == 'Armor'

    starforge = Weapon('Starforge', characts)
    assert starforge.name == 'Starforge'
    assert starforge.characts() == (5, 10, 20, 50, 3)
    assert starforge.type_ == 'Weapon'


def test_char_with_equipments(weapon, armor, characts, equipments):
    char = Entity('Blob', 'Random', characts, equipments)

    assert char.equipments.weapon.name == 'Starforge'
    assert char.equipments.armor.name == 'Headhunter'

    mage = Mage('Merlin')
    assert mage.equipments.weapon.name == 'Staff'
    assert mage.equipments.armor.name == 'Wizard dress'
    assert mage.strength == 1

    hunter = Hunter('Gon')
    assert hunter.equipments.weapon.name == 'Bow'
    assert hunter.equipments.armor.name == 'Leather armor'
    assert hunter.strength == 11

    warrior = Warrior('Conan')
    assert warrior.equipments.weapon.name == 'Sword'
    assert warrior.equipments.armor.name == 'Full plate armor'
    assert warrior.strength == 27


def test_fight_sim(warrior, water_elem):
    result = warrior - water_elem
    assert result.win
    assert result.time == 2
    assert result.overkill == 17
