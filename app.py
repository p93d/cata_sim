import requests
import json
import pandas as pd
from dataclasses import dataclass


# r = requests.get(
#     "https://queslar.com/api/player/full/580fa93745120134266d8e050ae7d187c5047629ace6cce69ce3a9888d381273"
# )


# data = r.json()


# with open('data.json', 'w') as f:
#     json.dump(data, f)

"""
catacombBanner
catacombCharacter
catacombGuardian
catacombGeneral
catacombHistory
catacombTomeInventory

Need:
Village - Blacksmith
    this starts at 1% boost per level, and every 20 levels it increases by 1%
    ie
    10-19       1%
    20-39       2%
    40-59       3%
    60-79       4%
    80-99       5%
    100-120     6%
    
Character
Banner
Relic Boosts
Guardian Boosts
"""

@dataclass
class CataPlayer:

    v_blacksmith: float

    r_health: float
    r_dodge: float
    r_hit: float
    r_ele: float
    r_damage: float




    c_health: int






with open('data.json', 'r') as f:
    data = json.loads(f.read())

print(data['catacombGuardian'])

# with open('rankings.json', 'r') as f:
#     data = json.loads(f.read())

# d = {
#     'id': [],
#     'uses': [],
#     'space_req': [],
#     'mobs': [],
#     'reward_mult': [],
#     'char_mult': [],
#     'mob_debuff': [],
#     'lifesteal': []
# }

# for tome in data['catacombTomeInventory']:

#     d['id'].append(tome['id'])
#     d['uses'].append(tome['uses_remaining'])
#     d['space_req'].append(tome['space_requirement'])
#     d['mobs'].append(tome['mobs'])
#     d['reward_mult'].append(tome['reward_multiplier'])
#     d['char_mult'].append(tome['character_multiplier'])
#     d['mob_debuff'].append(tome['mob_multiplier'])
#     d['lifesteal'].append(tome['lifesteal'])

# df = pd.DataFrame.from_dict(d)
# df.to_csv('tomes.csv')
