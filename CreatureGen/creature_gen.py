import math

####################################
## FUNCTIONS
####################################

# simple check for positive integer input
def int_positive():
  while True:
    try:
      num = int(input())
      if(num < 0): 
        raise ValueError('D:')
      break
    except ValueError:
      print('Error. Number must be greater than 0.')
  return num

def yes_no():
  while True:
    try:
      boolean = str(input())
      if(boolean != 'y' and boolean != 'n'):
        raise ValueError('D:')
      break
    except ValueError:
      print(yn_error_msg)
  if boolean == 'y':
    return True
  else: return False
  
# builds a tuple containing the information for one attack
def add_attack():
  print('''Input the name of the attack - Bite, Breathe Fire, etc.''')
  name = input()
  print('''Input the AP cost of the attack.''')
  ap_cost = int_positive()
  print('''Input the damage of the attack. Remember that damage in Cold Iron is in a XdY format, 
where X is the number of dice and Y is the number of faces on those dice.''')
  damage = input()
  print('''Input the description of the attack. Information such as its range, 
whether it requires a certain body part, etc. should go here.''')
  description = input()
  print('''Attack added.''')
  return (name, ap_cost, damage, description)

def add_trait():
  print('''Name the trait.''')
  name = input()
  print('''Describe it. Be specific about what it is.''')
  description = input()
  return (name, description)

def modifier(score):
  score = math.floor((score / 2) - 5)
  if score < 0:
    return str(score)
  else:
    return '+' + str(score)

# takes stats, calculates AP, wounds, willpower, guard,
# spits them back out as a tuple
def combat_stats(stat_dict):
  ap = math.floor(stat_dict['PER']/4) + math.floor(stat_dict['AGI']/1.5)
  willpower = math.floor(stat_dict['SPR']) + math.floor(stat_dict['CHR']/4)
  guard = math.floor(stat_dict['PER']/2.5) + math.floor(stat_dict['AGI']/2)
  wounded = stat_dict['FOR']
  very_wounded = stat_dict['FOR']*2 + math.floor(stat_dict['MGT']/2)
  dead = stat_dict['FOR']*3 + stat_dict['MGT']
  return (ap, willpower, guard, wounded, very_wounded, dead)

def make_html():
  # required tag bits
  creature_file.write('<!DOCTYPE html>\n<html>')
  creature_file.write('<head>\n\t<meta charset="utf-8">\n\t<title>' + name + '</title>\n<head>\n')
  creature_file.write('<body>\n\t')
  # basic info
  creature_file.write('<h1>' + name + '</h1>\n\t')
  creature_file.write('<h2>' + size + ' ' + category + '</h2>\n\t')
  creature_file.write('<p>' + description + '</p>\n\t')
  # SPAMFIC table
  creature_file.write('<table>\n\t')
  for key, value in creature_stats.items():
    creature_file.write('<th>' + key + '</th>')
  creature_file.write('\n<tr>')
  for key, value in creature_stats.items():
    creature_file.write('<td>' + str(value) + ' (' + modifier(value) + ') ' + '</td>')
  creature_file.write('\n</tr>\n</table>')
  # wounds, action points, willpower, guard table
  derived_stats = combat_stats(creature_stats)
  creature_file.write('<table>\n\t')
  creature_file.write('<tr><td>Action Points</td><td>' + str(derived_stats[0]) + '</td>')
  creature_file.write('<td>Wounded</td><td>' + str(derived_stats[3]) + '</td></tr>\n\t')
  creature_file.write('<tr><td>Willpower</td><td>' + str(derived_stats[1]) + '</td>')
  creature_file.write('<td>Very Wounded</td><td>' + str(derived_stats[4]) + '</td></tr>\n\t')
  creature_file.write('<tr><td>Guard</td><td>' + str(derived_stats[2]) + '</td>')
  creature_file.write('<td>Dead</td><td>' + str(derived_stats[5]) + '</td></tr></table>\n\t')
  # attacks
  creature_file.write('<h2>Attacks</h2>\n\t')
  for attack in attacks:
    creature_file.write('<p><b>' + attack[0] + '</b> ')
    creature_file.write('(AP Cost: ' + str(attack[1]) + ') ')
    creature_file.write('[Damage: ' + attack[2] + ']</p>\n\t')
    creature_file.write('<p>' + attack[3] + '</p>\n\t')
  creature_file.write('</body>\n</html>')


#################################
## FUNCTIONS END
#################################

print('''Welcome to the Cold Iron creature generator.
Enter a name for the creature, case sensitive:''')

# TODO: clean numbers and certain punctuation from the input
name = input()

creature_file = open(name + '.html', 'w+')

# TODO: add multiple paragraph support
print('''Enter a description of this creature.''')
description = input()

creature_sizes = ["Tiny", "Small", "Medium", "Large", "Huge", "Gigantic"]

print('''Enter the number of the size that this creature is. The larger it is, the easier it is to hit in combat and the more space it takes up on the battlemap.
Available categories and their general are:
1. Tiny (less than 15cm: ants, spiders, small birds, etc.)
2. Small (15cm to 1m: dogs, cats, birds of prey (eagles), etc.)
3. Medium (1m to 2m: goblins, humans, mazorecs, goats, ghouls, etc.)
4. Large (2m to 7m: bears, lions, wyverns, giant cave spiders, manticores, crocodiles, qhonitari, etc.)
5. Huge (7m to 12m: rocs, hydra, elephants, rhinoceros, griffins, etc.)
6. Gigantic (12m and beyond: dragons, sphinxes, landwyrms, etc.''')
while True:
  try:
    size = input()
    if size not in ["1", "2", "3", "4", "5", "6"]:
      raise ValueError('D:')
    break
  except ValueError:
    print('''Invalid category. Available categories are:
1. Tiny, 2. Small, 3. Medium, 4. Large, 5. Huge, 6. Gigantic''')

size = creature_sizes[int(size) - 1]

print('''Enter the number of the category that this creature belongs to.
Available categories are:
1. Sapient (a creature possessing the ability to think and act using knowledge and form civilizations, e.g. human, aelvezim, mazorec)
2. Beast (an ordinary creature lacking sapience, e.g. parrot, dog, bear)
3. Megabeast (a magical or unusually dangerous creature lacking sapience, e.g. troglodyte, unicorn, ogre)
4. Legendary (an incredibly powerful, intelligent, special creature, e.g. dragon, werebeast, vampire)''')

creature_categories = ["Sapient", "Beast", "Megabeast", "Legendary"]

while True:
  try:
    category = input()
    if category not in ["1", "2", "3", "4"]:
      raise ValueError('D:')
    break
  except ValueError:
    print('''Invalid category. Available categories are:
1. Sapient, 2. Beast, 3. Megabeast, 4. Legendary''')

category = creature_categories[int(category) - 1]

####### STATTING THE CREATURE

print('''Input the stat scores of the creature. All stats must be integers greater than 0. 
Please see the Rules/SPAMFIC Stat System for more information on each stat.''')
print('''How much Spirit (SPR) does the creature have? Spirit represents the creature's mental fortitude. 
Spirit should differ with creature type. A Sapient has around 6-13 SPR, a Beast or Megabeast typically less than 5, and Legendaries are generally Sapient-level or higher.''')
yn_error_msg = 'Error. Please input y or n.'
creature_spr = int_positive()

print('''How much Perception (PER) does the creature have? Perception represents sharp senses.''')
creature_per = int_positive()

print('''How much Agility (AGI) does the creature have? Agility represents the coordination/speed of the creature.''')
creature_agi = int_positive()

print('''How much Might (MGT) does the creature have? Might represents the physical strength of the creature.''')
creature_mgt = int_positive()

print('''How much Fortitude (FOR) does the creature have? Fortitude represents the hardiness of the creature.''')
creature_for = int_positive()

print('''How much Intelligence (INT) does the creature have? Intelligence represents the mental aptitude of the creature. 
Intelligence should differ with creature type. A Sapient has around 6-13 Intelligence, a Beast or Megabeast typically less than 5, and Legendaries are generally Sapient-level or higher.''')
creature_int = int_positive()

print('''How much Charisma (CHR) does the creature have? Charisma represents the strength of personality of a creature. 
Charisma for Beasts and Megabeasts should increase a little higher than their intelligence.''')
creature_chr = int_positive()

creature_stats = {
  'SPR': creature_spr,
  'PER': creature_per,
  'AGI': creature_agi,
  'MGT': creature_mgt,
  'FOR': creature_for,
  'INT': creature_int,
  'CHR': creature_chr,
}

####### ADDING ATTACKS TO THE CREATURE

print('''Now you will add attacks to your creature. Every creature has at least one attack it can use.''')
print('''Can your creature use techniques? (y/n)''')
techniques_allowed = yes_no()

print('''How many different attacks does it have?''')
num_attacks = int_positive()
attacks = set()
for i in range(0, num_attacks):
  attacks.add(add_attack())

####### ADDING INNATE PERKS/TRAITS TO THE CREATURE
print('''Does your creature have any perks? Check the perks page for a list of valid perks.''')
perks_allowed = yes_no()
if perks_allowed == True:
  print('''List the creature's perks, seperated by commas. i.e. perk1, perk2, perk3...''')
  perks = input()

print('''Does your creature have any unique traits? Traits are qualities more along
the lines of "no predisposition for magic" or "regenerates 5 Wounds per round of combat".''')
traits_allowed = yes_no()
traits = set()
if traits_allowed == True:
  print('''List the number of the creature's traits.''')
  num_traits = int_positive()
  for i in range(0, num_traits):
    traits.add(add_trait)

print('''You're all done! Generating HTML page...''')
make_html()
print('''You can find the new bestiary entry in the same directory as this script.''')

