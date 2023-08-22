def roll_call_dwarves(dwarves_list):
    for index, dwarf in enumerate(dwarves_list, start=1):
        print(f'{index}. {dwarf}')

def summon_captain_planet(planeteer_calls):
    list_of_summons = [summon.title() + "!" for summon in planeteer_calls if not len(planeteer_calls) == 0 ]
    return list_of_summons


def long_planeteer_calls(list_of_calls):
    for call in list_of_calls:
        if len(call) > 4:
            return True
    return False

    

def find_the_cheese(list_of_strings):
     cheese_types = ["cheddar", "gouda","camembert"]

     for item in list_of_strings:
        if item in cheese_types:
            return item
     return None