"""
Mod class defines a mod.
TODO: alias_names needs work/implementation
"""
class Mod:
    def __init__(self, mod_name, nexus_id, game_name, alias_names=[]):
        self.mod_name = mod_name
        self.nexus_id = nexus_id
        self.game_name = game_name
        # for like "iHUD to Immersive HUD, or EC for Enhanced Camera"
        self.alias_names = [] 


    def print_out(self):
        print (self.mod_name + "\t" + str(self.nexus_id) + "\t")


    def get_mod_link(self):
        return "[" + self.mod_name + "](https://www.nexusmods.com/" + self.game_name + "/mods/" + str(self.nexus_id) + ")"

    """
    Returns JSON output
    {'alias_names': [],
     'game_name': 'skyrim',
     'mod_name': 'iHUD',
     'nexus_id': 3222}
    """
    def get_mod_info_as_json(self):
        return self.__dict__