class Stat():
    def __init__(self, value):
        self.value = value
        self.mod = self.getMod(value)
    

def getMod(val):
    return (val - 10) // 2

class DnDCharacter():
    def __init__(self):
        self.name = "Default"
        self.level = 1
        self.str = Stat(10)
        self.dex = Stat(10)
        self.con = Stat(10)
        self.int = Stat(10)
        self.wis = Stat(10)
        self.cha = Stat(10)
        self.prof = 2
        self.ac = 10 + self.dex.mod
        self.hp = 10 + self.con.mod
        self.speed = 30
        self.skills = {}
        self.saves = {}
        self.proficiencies = []
        self.languages = []
        self.traits = []
        self.actions = []
        # self.spells = []
        # self.spellSlots = []
        # self.spellSave = 8 + self.wis.mod
        # self.spellAttack = self.prof + self.wis.mod
    
    def setStr(self, val):
        self.str.value = val
        self.str.mod = self.getMod(val)
        self.ac = 10 + self.dex.mod
    
    def setDex(self, val):  
        self.dex.value = val
        self.dex.mod = self.getMod(val)
        self.ac = calcAC()

    def setCon(self, val):
        self.con.value = val
        self.con.mod = self.getMod(val)
        self.hp = calcHP()

    def setInt(self, val):
        self.int.value = val
        self.int.mod = self.getMod(val)
    
    def setWis(self, val):
        self.wis.value = val
        self.wis.mod = self.getMod(val)

    def setCha(self, val):
        self.cha.value = val
        self.cha.mod = self.getMod(val)
    
    
