from Models import City, Road, Ticket

Vancouver = City("Vancouver", wharf=True)
Anchorage = City("Anchorage", wharf=True)
Winnipeg = City("Winnipeg", wharf=False)
Los_Angeles = City("Los Angeles", wharf=True)
New_York = City("New York", wharf=True)
Miami = City("Miami", wharf=True)
Caracas = City("Caracas", wharf=True)
Lima = City("Lima", wharf=True)
Rio_de_Janeiro = City("Rio de Janeiro", wharf=True)
Buenos_Aires = City("Buenos Aires", wharf=True)
Reykjavik = City("Reykjavik", wharf=True)
Moskva = City("Moskva", wharf=False)
Hamburg = City("Hamburg", wharf=True)
Edinburgh = City("Edinburgh", wharf=True)
Marseille = City("Marseille", wharf=True)
Athina = City("Athina", wharf=True)
Casablanca = City("Casablanca", wharf=True)
Al_Qahira = City("Al-Qahira", wharf=True)
Lagos = City("Lagos", wharf=True)
Djibouti = City("Djibouti", wharf=False)
Luanda = City("Luanda", wharf=True)
Dar_El_Salaam = City("Dar El Salaam", wharf=True)
Cape_Town = City("Cape Town", wharf=True)
Empty_Point = City("Empty Point", wharf=True)
Tiksi = City("Tiksi", wharf=True)
Novosibirsk = City("Novosibirsk", wharf=False)
Tehran = City("Tehran", wharf=False)
Labore = City("Labore", wharf=False)
Mumbai = City("Mumbai", wharf=True)
Bangkok = City("Bangkok", wharf=True)
Yakutsk = City("Yakutsk", wharf=False)
Petropavlovsk = City("Petropavlovsk", wharf=True)
Beijing = City("Beijing", wharf=False)
Tokyo = City("Tokyo", wharf=True)
Christchurch = City("Christchurch", wharf=True)
Cambridge_Bay = City("Cambridge Bay", wharf=True)
Murmansk = City("Murmansk", wharf=True)
Manila = City("Manila", wharf=True)
Mexico = City("Mexico", wharf=False)
Honolulu = City("Honolulu", wharf=True)
Valparaiso = City("Valparaiso", wharf=True)
Sydney = City("Sydney", wharf=True)
Jakarta = City("Jakarta", wharf=True)
Toamasina = City("Toamasina", wharf=True)
Port_Moresby = City("Port Moresby", wharf=True)
Perth = City("Perth", wharf=True)
Darwin = City("Darwin", wharf=True)
Honk_Kong = City("Honk Kong", wharf=True)

roads = [
    Road(Vancouver, Anchorage, 2, ["gray"], ["hard terrain railway"]),
    Road(Vancouver, Winnipeg, 2, ["yellow"], ["railway"]),
    Road(Vancouver, Los_Angeles, 1, ["red", "green"], ["railway"]),
    Road(Vancouver, Tokyo, 6, ["white"], ["sea route"]),
    Road(Cambridge_Bay, Reykjavik, 6, ["white"], ["sea route"]),
    Road(Cambridge_Bay, Anchorage, 6, ["black"], ["sea route"]),
    Road(Winnipeg, Cambridge_Bay, 4, ["black"], ["railway"]),
    Road(Winnipeg, New_York, 2, ["green"], ["railway"]),
    Road(Winnipeg, Los_Angeles, 3, ["gray"], ["railway"]),
    Road(Los_Angeles, New_York, 4, ["purple", "black"], ["railway"]),
    Road(Los_Angeles, Mexico, 2, ["yellow", "white"], ["railway"]),
    Road(Los_Angeles, Tokyo, 7, ["black", "green"], ["sea road"]),
    Road(Los_Angeles, Honolulu, 3, ["yellow"], ["sea road"]),
    Road(New_York, Miami, 2, ["white"], ["railway"]),
    Road(New_York, Reykjavik, 6, ["yellow"], ["sea route"]),
    Road(New_York, Edinburgh, 7, ["red", "purple"], ["sea route"]),
    Road(Miami, Caracas, 2, ["white"], ["sea route"]),
    Road(Miami, Casablanca, 7, ["green"], ["sea route"]),
    Road(Mexico, Caracas, 3, ["red", "purple"], ["railway"]),
    Road(Caracas, Lima, 2, ["white", "yellow"], ["railway"]),
    Road(Caracas, Lagos, 7, ["red"], ["sea route"]),
    Road(Caracas, Rio_de_Janeiro, 4, ["green", "black"], ["railway"]),
    Road(Lima, Valparaiso, 2, ["grey", "grey"], ["railway"]),
    Road(Lima, Honolulu, 6, ["grey"], ["sea route"]),
    Road(Lima, Sydney, 8, ["black", "purple"], ["sea route"]),
    Road(Valparaiso, Buenos_Aires, 3, ["green"], ["sea route"]),
    Road(Valparaiso, Christchurch, 7, ["yellow"], ["sea route"]),
    Road(Rio_de_Janeiro, Buenos_Aires, 1, ["white", "red"], ["railway"]),
    Road(Rio_de_Janeiro, Cape_Town, 6, ["white", "black"], ["sea route"]),
    Road(Rio_de_Janeiro, Luanda, 6, ["grey"], ["sea route"]),
    Road(Buenos_Aires, Cape_Town, 7, ["purple", "yellow"], ["sea route"]),
    Road(Reykjavik, Edinburgh, 2, ["grey"], ["sea route"]),
    Road(Reykjavik, Murmansk, 4, ["green"], ["sea route"]),
    Road(Murmansk, Moskva, 2, ["purple"], ["railway"]),
    Road(Murmansk, Tiksi, 7, ["red"], ["sea route"]),
    Road(Moskva, Novosibirsk, 4, ["green", "yellow"], ["railway"]),
    Road(Moskva, Tehran, 3, ["red"], ["railway"]),
    Road(Hamburg, Moskva, 2, ["white", "black"], ["railway"]),
    Road(Hamburg, Edinburgh, 1, ["yellow", "black"], ["sea route"]),
    Road(Hamburg, Marseille, 1, ["red", "purple"], ["railway"]),
    Road(Hamburg, Athina, 2, ["grey"], ["railway"]),
    Road(Edinburgh, Marseille, 1, ["white", "green"], ["sea route"]),
    Road(Marseille, Athina, 2, ["red"], ["sea route"]),
    Road(Marseille, Casablanca, 1, ["grey"], ["hard terrain railway"]),
    Road(Athina, Tehran, 2, ["grey"], ["railway"]),
    Road(Athina, Al_Qahira, 1, ["green"], ["sea route"]),
    Road(Casablanca, Al_Qahira, 3, ["grey"], ["railway"]),
    Road(Casablanca, Lagos, 4, ["grey"], ["railway"]),
    Road(Al_Qahira, Tehran, 1, ["yellow", "black"], ["railway"]),
    Road(Al_Qahira, Djibouti, 2, ["red", "white"], ["railway"]),
    Road(Lagos, Luanda, 1, ["purple", "yellow"], ["railway"]),
    Road(Djibouti, Dar_El_Salaam, 1, ["red", "black"], ["railway"]),
    Road(Luanda, Dar_El_Salaam, 2, ["grey"], ["hard terrain railway"]),
    Road(Luanda, Cape_Town, 2, ["grey"], ["railway"]),
    Road(Dar_El_Salaam, Cape_Town, 3, ["green", "purple"], ["railway"]),
    Road(Dar_El_Salaam, Jakarta, 7, ["green", "purple"], ["sea route"]),
    Road(Dar_El_Salaam, Mumbai, 4, ["white"], ["sea route"]),
    Road(Dar_El_Salaam, Toamasina, 1, ["yellow"], ["sea route"]),
    Road(Cape_Town, Toamasina, 3, ["grey"], ["sea route"]),
    Road(Cape_Town, Empty_Point, 5, ["red", "green"], ["sea route"]),
    Road(Empty_Point, Perth, 5, ["white", "purple"], ["sea route"]),
    Road(Tiksi, Novosibirsk, 3, ["grey"], ["railway"]),
    Road(Tiksi, Yakutsk, 1, ["green"], ["railway"]),
    Road(Tiksi, Petropavlovsk, 7, ["black"], ["sea route"]),
    Road(Tiksi, Anchorage, 8, ["yellow"], ["sea route"]),
    Road(Novosibirsk, Yakutsk, 3, ["purple"], ["railway"]),
    Road(Novosibirsk, Beijing, 3, ["red", "black"], ["railway"]),
    Road(Novosibirsk, Labore, 2, ["white"], ["railway"]),
    Road(Tehran, Labore, 2, ["grey"], ["hard terrain railway"]),
    Road(Tehran, Mumbai, 3, ["white", "purple"], ["railway"]),
    Road(Labore, Beijing, 3, ["grey"], ["hard terrain railway"]),
    Road(Labore, Mumbai, 1, ["green", "black"], ["railway"]),
    Road(Mumbai, Bangkok, 3, ["red", "yellow"], ["railway"]),
    Road(Yakutsk, Beijing, 3, ["yellow"], ["railway"]),
    Road(Yakutsk, Petropavlovsk, 3, ["white"], ["railway"]),
    Road(Petropavlovsk, Tokyo, 2, ["grey"], ["sea route"]),
    Road(Petropavlovsk, Anchorage, 3, ["purple"], ["sea route"]),
    Road(Beijing, Honk_Kong, 2, ["white", "green"], ["railway"]),
    Road(Tokyo, Honk_Kong, 3, ["grey"], ["sea route"]),
    Road(Tokyo, Honolulu, 5, ["red"], ["sea route"]),
    Road(Tokyo, Manila, 2, ["yellow"], ["sea route"]),
    Road(Honk_Kong, Bangkok, 2, ["white"], ["sea route"]),
    Road(Honk_Kong, Manila, 1, ["purple"], ["sea route"]),
    Road(Honolulu, Manila, 5, ["white"], ["sea route"]),
    Road(Honolulu, Port_Moresby, 3, ["green"], ["sea route"]),
    Road(Manila, Bangkok, 2, ["red"], ["sea route"]),
    Road(Manila, Jakarta, 2, ["grey"], ["sea route"]),
    Road(Bangkok, Jakarta, 2, ["white"], ["sea route"]),
    Road(Jakarta, Darwin, 2, ["black"], ["sea route"]),
    Road(Jakarta, Perth, 3, ["grey"], ["sea route"]),
    Road(Darwin, Perth, 2, ["red"], ["railway"]),
    Road(Darwin, Sydney, 2, ["green"], ["railway"]),
    Road(Darwin, Port_Moresby, 1, ["red"], ["sea route"]),
    Road(Sydney, Port_Moresby, 3, ["yellow"], ["sea route"]),
    Road(Perth, Sydney, 2, ["white", "yellow"], ["railway"]),
    Road(Christchurch, Sydney, 1, ["red", "white"], ["sea route"]),
]

known_tickets = [
    Ticket(Honk_Kong, Jakarta, 5),#
    Ticket(Marseille, Al_Qahira, 5),#

    Ticket(Bangkok, Tokyo, 6),#
    Ticket(Mumbai, Beijing, 6),#
    Ticket(Valparaiso, Rio_de_Janeiro, 6),#

    Ticket(Jakarta, Sydney, 7),#
    Ticket(Djibouti, Labore, 7),#

    Ticket(Hamburg, Dar_El_Salaam, 8),#

    Ticket(Vancouver, Miami, 9),#
    Ticket(Miami, Buenos_Aires, 9),#

    Ticket(New_York, Marseille, 10),#
    Ticket(Edinburgh, Luanda, 10),#
    Ticket(Lagos, Tehran, 10),#

    Ticket(Los_Angeles, Jakarta, 11),#
    Ticket(Moskva, Toamasina, 11),#
    Ticket(Mexico, New_York, 11),#
    Ticket(Rio_de_Janeiro, Dar_El_Salaam, 11),#
    Ticket(Tokyo, Sydney, 11),#

    Ticket(Caracas, Athina, 12),#

    Ticket(Cape_Town, Jakarta, 13),#
    Ticket(Hamburg, Beijing, 13),#
    Ticket(Miami, Moskva, 13),#
    Ticket(Reykjavik, Mumbai, 13),#
    Ticket(Mexico, Beijing, 13),#
    Ticket(Moskva, Honk_Kong,13),#
    Ticket(Buenos_Aires, Sydney, 13),#
    Ticket(Vancouver, Edinburgh, 13),#
    Ticket(Novosibirsk, Darwin, 13),#
    Ticket(Caracas, Al_Qahira, 13),#

    Ticket(Winnipeg, Perth, 14),#
    Ticket(Marseille, Beijing, 14),#
    Ticket(Athina, Manila, 14),#
    Ticket(Lima, Jakarta, 14),#
    Ticket(Los_Angeles, Hamburg, 14),#
    Ticket(Lagos, Honk_Kong, 14),#

    Ticket(New_York, Tokyo, 15),#
    Ticket(Mexico, Mumbai, 15),#
    Ticket(Los_Angeles, Rio_de_Janeiro, 15),#
    Ticket(Moskva, Petropavlovsk, 15),#
    Ticket(Dar_El_Salaam, Tokyo, 15),#

    Ticket(Casablanca, Yakutsk, 16),#
    Ticket(Casablanca, Honolulu, 16),#

    Ticket(Buenos_Aires, Manila, 17),#
    Ticket(Rio_de_Janeiro, Perth, 17),#
    Ticket(Los_Angeles, Dar_El_Salaam, 17),#
    Ticket(New_York, Sydney, 17),#
    Ticket(Edinburgh, Honk_Kong, 17),#

    Ticket(Buenos_Aires, Marseille, 18),#
    Ticket(Marseille, Jakarta, 18),#
    Ticket(Rio_de_Janeiro, Hamburg, 18),#

    Ticket(New_York, Cape_Town, 19),#
    Ticket(New_York, Mumbai, 19),#
    Ticket(Al_Qahira, Sydney, 19),#

    Ticket(Rio_de_Janeiro, Tokyo, 20),#
    Ticket(Edinburgh, Tokyo, 22),#
    Ticket(Marseille, Christchurch, 23),#
    Ticket(Edinburgh, Sydney, 25),#

]
