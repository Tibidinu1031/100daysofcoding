class character:
  name = None
  health = 100
  magicPoints = 100

  def __init__(self, name):
    self.name = name

  def seeStats(self):
    print(f"Name: {self.name}\tHP: {self.health}\tMP: {self.magicPoints}")

  def setStats(self,health, magicPoints):
    self.health = health
    self.magicPoints = magicPoints

#-------------------------------------------------

class player(character):
  nickname = None
  lives = 30

  def __init__(self, nickname):
    self.name = "Jon Doe"
    self.nickname = nickname
  

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} is alive because he has {self.lives} lives.")
    else:
      print(f"{self.nickname} is dead because he has {self.lives} lives.")
      return

  def seeStats(self):
    print(f"Name: {self.name}\tNickname: {self.nickname}\tHP: {self.health}\tMP: {self.magicPoints}")

me = player("Jonno")
print()
me.seeStats()
me.isAlive()
print()


#=================================================

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def seeStats(self):
    print(f"Name: {self.name}\tType: {self.type}\tStrength: {self.strength}\tHP: {self.health}\tMP: {self.magicPoints}")

#-------------------------------------------------

class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def seeStats(self):
    print(f"Name: {self.name}\tType: {self.type}\tStrength: {self.strength}\tHP: {self.health}\tMP: {self.magicPoints}\tSpeed: {self.speed}")

o1 = orc(100)
o2 = orc(101)
o3 = orc(102)

print()
o1.seeStats()
o2.seeStats()
o3.seeStats()
print()

#=============================================

class vampire(enemy):
  day = True

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day

  def seeStats(self):
    print(f"Name: {self.name}\tType: {self.type}\tStrength: {self.strength}\tHP: {self.health}\tMP: {self.magicPoints}\tDay: {self.day}")

  def setStats(self,name, type, health, magicPoints, strength):
    self.name = name
    self.type = type
    self.health = health
    self.magicPoints = magicPoints
    self.strength = strength

v1 = vampire(True)
v2 = vampire(False)
v3 = vampire(True)
v4 = vampire(False)
v3.setStats("plm1", "plm2", 100, 1000,10000)
v4.setStats("plm3", "plm4", 101, 1001, 10001)

print()
v1.seeStats()
v2.seeStats()
v3.seeStats()
v4.seeStats()
print()

#=================================================


  
  