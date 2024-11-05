from diplomacy.persistence import phase
from diplomacy.persistence.board import Board
from diplomacy.persistence.player import Player
from diplomacy.persistence.province import Province, ProvinceType, Coast

italy = Player("Italy", "A4C499", 18, 3, set(), set())
france = Player("France", "79AFC6", 18, 3, set(), set())
england = Player("England", "EFC4E4", 18, 3, set(), set())
germany = Player("Germany", "A08A75", 18, 3, set(), set())
russia = Player("Russia", "A87E9F", 18, 4, set(), set())
austria = Player("Austria", "C48F85", 18, 3, set(), set())
turkey = Player("Turkey", "EAEAAF", 18, 3, set(), set())
classic_players: set[Player] = {italy, france, england, germany, russia, austria, turkey}

classic_provinces: set[Province] = set()
# Sea Provinces
classic_provinces.add(
    Province("Barents Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Norwegian Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("North Atlantic Ocean", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("North Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Irish Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Mid-Atlantic Ocean", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("English Channel", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Heligoland Bight", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Skaggerak", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Gulf of Bothnia", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Baltic Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Western Mediterranean", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Gulf of Lyon", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Tyrrhenian Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Ionian Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Adriatic Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Aegean Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Eastern Mediterranean", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Black Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
classic_provinces.add(
    Province("Black Sea", [], (0, 0), (0, 0), ProvinceType.SEA, False, set(), set(), None, None, None)
)
# Neutral Land Provinces
classic_provinces.add(
    Province("North Africa", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, None, None)
)
classic_provinces.add(Province("Tunis", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Portugal", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Spain", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Belgium", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Holland", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(
    Province("Denmark", [], (0, 0), (0, 0), ProvinceType.ISLAND, True, set(), set(), None, None, None)
)
classic_provinces.add(Province("Norway", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Sweden", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Rumania", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Serbia", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Bulgaria", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Greece", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), None, None, None))
classic_provinces.add(Province("Albania", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, None, None))
# England
classic_provinces.add(
    Province("Clyde", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, england, None)
)
classic_provinces.add(
    Province("Edinburgh", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), england, england, None)
)
classic_provinces.add(
    Province("Liverpool", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), england, england, None)
)
classic_provinces.add(
    Province("Yorkshire", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, england, None)
)
classic_provinces.add(
    Province("Wales", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, england, None)
)
classic_provinces.add(
    Province("London", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), england, england, None)
)
# France
classic_provinces.add(
    Province("Brest", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), france, france, None)
)
classic_provinces.add(
    Province("Picardy", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, france, None)
)
classic_provinces.add(
    Province("Paris", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), france, france, None)
)
classic_provinces.add(
    Province("Gascony", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, france, None)
)
classic_provinces.add(
    Province("Burgundy", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, france, None)
)
classic_provinces.add(
    Province("Marseilles", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), france, france, None)
)
# Italy
classic_provinces.add(
    Province("Piedmont", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, italy, None)
)
classic_provinces.add(Province("Venice", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), italy, italy, None))
classic_provinces.add(
    Province("Tuscany", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, italy, None)
)
classic_provinces.add(Province("Rome", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), italy, italy, None))
classic_provinces.add(Province("Apulia", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, italy, None))
classic_provinces.add(Province("Naples", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), italy, italy, None))
# Germany
classic_provinces.add(Province("Ruhr", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, germany, None))
classic_provinces.add(
    Province("Kiel", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), germany, germany, None)
)
classic_provinces.add(
    Province("Berlin", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), germany, germany, None)
)
classic_provinces.add(
    Province("Prussia", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, germany, None)
)
classic_provinces.add(
    Province("Munich", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), germany, germany, None)
)
classic_provinces.add(
    Province("Silesia", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, germany, None)
)
# Austria
classic_provinces.add(
    Province("Tyrolia", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, austria, None)
)
classic_provinces.add(
    Province("Trieste", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), austria, austria, None)
)
classic_provinces.add(
    Province("Vienna", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), austria, austria, None)
)
classic_provinces.add(
    Province("Bohemia", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, austria, None)
)
classic_provinces.add(
    Province("Galicia", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, austria, None)
)
classic_provinces.add(
    Province("Budapest", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), austria, austria, None)
)
# Russia
classic_provinces.add(
    Province("Finland", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, russia, None)
)
classic_provinces.add(
    Province("St. Petersburg", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), russia, russia, None)
)
classic_provinces.add(
    Province("Moscow", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), russia, russia, None)
)
classic_provinces.add(
    Province("Livonia", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, russia, None)
)
classic_provinces.add(
    Province("Warsaw", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), russia, russia, None)
)
classic_provinces.add(
    Province("Ukraine", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, russia, None)
)
classic_provinces.add(
    Province("Sevastopol", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), russia, russia, None)
)
# Turkey
classic_provinces.add(
    Province("Constantinople", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), turkey, turkey, None)
)
classic_provinces.add(
    Province("Ankara", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), turkey, turkey, None)
)
classic_provinces.add(
    Province("Smyrna", [], (0, 0), (0, 0), ProvinceType.LAND, True, set(), set(), turkey, turkey, None)
)
classic_provinces.add(
    Province("Armenia", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, turkey, None)
)
classic_provinces.add(Province("Syria", [], (0, 0), (0, 0), ProvinceType.LAND, False, set(), set(), None, turkey, None))

# Give players their centers
for province in classic_provinces:
    if province.has_supply_center and province.owner:
        province.owner.centers.add(province)

# Set adjacency
adjacency_dict = {
    "Barents Sea": ["St. Petersburg", "Norway", "Norwegian Sea"],
    "Norwegian Sea": [
        "Barents Sea",
        "Norway",
        "North Sea",
        "Edinburgh",
        "Clyde",
        "North Atlantic Ocean",
    ],
    "North Atlantic Ocean": ["Norwegian Sea", "Clyde", "Liverpool", "Irish Sea", "Mid-Atlantic Ocean"],
    "Irish Sea": ["North Atlantic Ocean", "Liverpool", "Wales", "English Channel", "Mid-Atlantic Ocean"],
    "North Sea": [
        "Norwegian Sea",
        "Norway",
        "Skaggerak",
        "Denmark",
        "Heligoland Bight",
        "Holland",
        "Belgium",
        "English Channel",
        "London",
        "Yorkshire",
        "Edinburgh",
    ],
    "Skaggerak": ["Norway", "Sweden", "Denmark", "North Sea"],
    "Heligoland Bight": ["North Sea", "Denmark", "Kiel", "Holland"],
    "Baltic Sea": ["Sweden", "Gulf of Bothnia", "Livonia", "Prussia", "Berlin", "Kiel", "Denmark"],
    "Gulf of Bothnia": ["Sweden, Finland, St. Petersburg", "Livonia", "Baltic Sea"],
    "English Channel": [
        "Wales",
        "London",
        "North Sea",
        "Belgium",
        "Picardy",
        "Brest",
        "Mid-Atlantic Ocean",
        "Irish Sea",
    ],
    "Mid-Atlantic Ocean": [
        "North Atlantic Ocean",
        "Irish Sea",
        "English Channel",
        "Brest",
        "Gascony",
        "Spain",
        "Portugal",
        "Western Mediterranean",
        "North Africa",
    ],
    "Western Mediterranean": ["Spain", "Gulf of Lyon", "Tyrrhenian Sea", "Tunis", "North Africa", "Mid-Atlantic Ocean"],
    "Gulf of Lyon": ["Marseilles", "Piedmont", "Tuscany", "Tyrrhenian Sea", "Western Mediterranean", "Spain"],
    "Tyrrhenian Sea": ["Gulf of Lyon", "Tuscany", "Rome", "Naples", "Ionian Sea", "Tunis", "Western Mediterranean"],
    "Ionian Sea": [
        "Naples",
        "Apulia",
        "Adriatic Sea",
        "Albania",
        "Greece",
        "Aegean Sea",
        "Eastern Mediterranean",
        "Tunis",
        "Tyrrhenian Sea",
    ],
    "Adriatic Sea": ["Venice", "Trieste", "Albania", "Ionian Sea", "Apulia"],
    "Aegean Sea": ["Bulgaria", "Constantinople", "Smyrna", "Eastern Mediterranean", "Ionian Sea", "Greece"],
    "Eastern Mediterranean": ["Ionian Sea", "Aegean Sea", "Smyrna", "Syria"],
    "Black Sea": ["Sevastopol", "Armenia", "Ankara", "Constantinople", "Bulgaria", "Rumania"],
    "Clyde": ["Liverpool", "North Atlantic Ocean", "Norwegian Sea", "Edinburgh"],
    "Edinburgh": ["Liverpool", "Clyde", "Norwegian Sea", "North Sea", "Yorkshire"],
    "Liverpool": ["Clyde", "Edinburgh", "Yorkshire", "Wales", "Irish Sea", "North Atlantic Ocean"],
    "Yorkshire": ["Edinburgh", "North Sea", "London", "Wales", "Liverpool"],
    "Wales": ["Liverpool", "Yorkshire", "London", "English Channel", "Irish Sea"],
    "London": ["Yorkshire", "North Sea", "English Channel", "Wales"],
    "Norway": ["Norwegian Sea", "Barents Sea", "St. Petersburg", "Finland", "Sweden", "Skaggerak", "North Sea"],
    "Sweden": ["Norway", "Finland", "Gulf of Bothnia", "Baltic Sea", "Denmark", "Skaggerak"],
    "Denmark": ["Skaggerak", "Sweden", "Baltic Sea", "Kiel", "Heligoland Bight", "North Sea"],
    "Holland": ["North Sea", "Heligoland Bight", "Kiel", "Ruhr", "Belgium"],
    "Belgium": ["North Sea", "Holland", "Ruhr", "Burgundy", "Picardy", "English Channel"],
    "Portugal": ["Mid-Atlantic Ocean", "Spain"],
    "Spain": ["Mid-Atlantic Ocean", "Burgundy", "Marseilles", "Gulf of Lyon", "Western Mediterranean", "Portugal"],
    "North Africa": ["Mid-Atlantic Ocean", "Western Mediterranean", "Tunis"],
    "Tunis": ["Tunis", "Western Mediterranean", "Tyrrhenian Sea", "Ionian Sea"],
    "Greece": ["Albania", "Serbia", "Bulgaria", "Aegean Sea", "Ionian Sea"],
    "Albania": ["Trieste", "Serbia", "Greece", "Ionian Sea", "Adriatic Sea"],
    "Serbia": ["Budapest", "Rumania", "Bulgaria", "Greece", "Albania", "Trieste"],
    "Rumania": ["Ukraine", "Sevastopol", "Black Sea", "Bulgaria", "Serbia", "Budapest", "Galicia"],
    "Bulgaria": ["Rumania", "Black Sea", "Constantinople", "Aegean Sea", "Greece", "Serbia"],
    "Brest": ["English Channel", "Picardy", "Paris", "Gascony", "Mid-Atlantic Ocean"],
    "Picardy": ["English Channel", "Belgium", "Burgundy", "Paris", "Brest"],
    "Paris": ["Picardy", "Burgundy", "Gascony", "Brest"],
    "Gascony": ["Brest", "Paris", "Burgundy", "Marseilles", "Spain", "Mid-Atlantic Ocean"],
    "Burgundy": ["Belgium", "Ruhr", "Munich", "Marseilles", "Gascony", "Paris", "Picardy"],
    "Marseilles": ["Burgundy", "Piedmont", "Gulf of Lyon", "Spain", "Gascony"],
    "Ruhr": ["Belgium", "Holland", "Kiel", "Munich", "Burgundy"],
    "Kiel": ["Denmark", "Baltic Sea", "Berlin", "Munich", "Ruhr", "Holland", "Heligoland Bight"],
    "Munich": ["Ruhr", "Kiel", "Berlin", "Silesia", "Bohemia", "Tyrolia", "Burgundy"],
    "Berlin": ["Baltic Sea", "Prussia", "Silesia", "Munich", "Kiel"],
    "Silesia": ["Berlin", "Prussia", "Warsaw", "Galicia", "Bohemia", "Munich"],
    "Prussia": ["Baltic Sea", "Livonia", "Warsaw", "Silesia", "Berlin"],
    "Piedmont": ["Marseilles", "Tyrolia", "Venice", "Tuscany", "Gulf of Lyon"],
    "Venice": ["Tyrolia", "Trieste", "Adriatic Sea", "Apulia", "Rome", "Tuscany", "Piedmont"],
    "Tuscany": ["Piedmont", "Venice", "Rome", "Tyrrhenian Sea", "Gulf of Lyon"],
    "Rome": ["Tuscany", "Venice", "Apulia", "Naples", "Tyrrhenian Sea"],
    "Apulia": ["Venice", "Adriatic Sea", "Ionian Sea", "Naples", "Rome"],
    "Naples": ["Rome", "Apulia", "Ionian Sea", "Tyrrhenian Sea"],
    "Tyrolia": ["Munich", "Bohemia", "Vienna", "Trieste", "Venice", "Piedmont"],
    "Bohemia": ["Munich", "Silesia", "Galicia", "Vienna", "Tyrolia"],
    "Vienna": ["Tyrolia", "Bohemia", "Galicia", "Budapest", "Trieste"],
    "Galicia": ["Silesia", "Warsaw", "Ukraine", "Rumania", "Budapest", "Vienna"],
    "Budapest": ["Vienna", "Galicia", "Rumania", "Serbia", "Trieste"],
    "Trieste": ["Tyrolia", "Vienna", "Budapest", "Serbia", "Albania", "Adriatic Sea", "Venice"],
    "Warsaw": ["Prussia", "Livonia", "Moscow", "Ukraine", "Galicia", "Silesia"],
    "Moscow": ["St. Petersburg", "Sevastopol", "Ukraine", "Warsaw", "Livonia"],
    "Livonia": ["Gulf of Bothnia", "St. Petersburg", "Moscow", "Warsaw", "Prussia", "Baltic Sea"],
    "Finland": ["Norway", "St. Petersburg", "Gulf of Bothnia", "Sweden"],
    "St. Petersburg": ["Finland", "Norway", "Barents Sea", "Moscow", "Livonia", "Gulf of Bothnia"],
    "Ukraine": ["Moscow", "Sevastopol", "Rumania", "Galicia", "Warsaw"],
    "Sevastopol": ["Moscow", "Armenia", "Black Sea", "Rumania", "Ukraine"],
    "Constantinople": ["Bulgaria", "Black Sea", "Ankara", "Smyrna", "Aegean Sea"],
    "Ankara": ["Black Sea", "Armenia", "Smyrna", "Constantinople"],
    "Smyrna": ["Constantinople", "Ankara", "Armenia", "Syria", "Eastern Mediterranean", "Aegean Sea"],
    "Armenia": ["Sevastopol", "Syria", "Smyrna", "Ankara", "Black Sea"],
    "Syria": ["Eastern Mediterranean", "Smyrna", "Armenia"],
}
name_to_province = {province.name: province for province in classic_provinces}
for province in classic_provinces:
    assert adjacency_dict[province.name] is not None
    province.adjacent = {name_to_province[name] for name in adjacency_dict[province.name]}
    assert None not in province.adjacent

for province in classic_provinces:
    province.coasts = set()
    if province.type != ProvinceType.LAND:
        continue
    sea_or_island_provinces = {adjacent for adjacent in province.adjacent if adjacent.type != ProvinceType.LAND}
    if sea_or_island_provinces:
        province.coasts = {Coast(f"{province.name} coast", (0, 0), (0, 0), sea_or_island_provinces, province)}

# for province in classic_provinces:
#     if province.coasts:
#         coast = province.coasts.pop()
#
#         coastal_adjacencies = coast.get_adjacent_coasts()
#         if len(coastal_adjacencies) <= 2:
#             province.coasts.add(coast)
#             continue
#
#         contiguous_seas = [
#             {adjacent for adjacent in sea_province.adjacent if adjacent in coast.adjacent_seas} | {sea_province}
#             for sea_province in coast.adjacent_seas
#         ]
#         for sea_province in coast.adjacent_seas:
#             combined_seas = set()
#             i = 0
#             while i < len(contiguous_seas):
#                 sea = contiguous_seas[i]
#                 if sea_province in sea:
#                     combined_seas |= sea
#                     contiguous_seas.pop(i)
#                 else:
#                     i += 1
#             contiguous_seas.append(combined_seas)
#         for sea in contiguous_seas:
#             coastal_adjacencies = set()
#             for sea_province in sea:
#                 adjacent_land = {
#                     adjacent_province
#                     for adjacent_province in sea_province.adjacent
#                     if adjacent_province.type == ProvinceType.LAND
#                 }
#                 coastal_adjacencies.update(adjacent_land & province.adjacent)

classic_board = Board(classic_players, classic_provinces, set(), phase.initial())
