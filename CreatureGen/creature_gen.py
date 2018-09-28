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

def modifier(score):
  score = math.floor((score / 2) - 5)
  if score < 0:
    return str(score)
  else:
    return '+' + str(score)

def make_html():
  # required tag bits
  creature_file.write('<!DOCTYPE html>\n<html>')
  creature_file.write('<head>\n\t<meta charset="utf-8">\n\t<title>' + name + '</title>\n<head>\n')
  creature_file.write('<body>\n\t')
  # basic info
  creature_file.write('<h1>' + name + '</h1>\n\t')
  creature_file.write('<h2>' + category + '</h2>\n\t')
  creature_file.write('<p>' + description + '</p>\n\t')
  # SPAMFIC table
  creature_file.write('<table>\n\t')
  for key, value in creature_stats.items():
    creature_file.write('<th>' + key + '</th>')
  creature_file.write('\n<tr>')
  for key, value in creature_stats.items():
    creature_file.write('<td>' + str(value) + ' (' + modifier(value) + ') ' + '</td>')
  creature_file.write('\n</tr>\n</table>')
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

print('''Enter the number of the category that this creature belongs to. This is case sensitive.
Available categories are:
1. Sapient (a creature possessing the ability to think and act using knowledge and forms civilizations, e.g. human, aelvezim, mazorec)
2. Beast (an ordinary creature lacking sapience, e.g. parrot, dog, bear)
3. Megabeast (a magical or unusually dangerous creature lacking sapience, e.g. troglodyte, unicorn, roc)
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
1. Sapient
2. Beast
3. Monster
4. Legendary''')

category = creature_categories[int(category) - 1]

####### STATTING THE CREATURE

print('Input the stat scores of the creature. All stats must be integers greater than 0.')
print('''How much Spirit (SPR) does the creature have? Spirit represents the creature's mental fortitude. Spirit should differ with creature type. A Sapient has around 6-13 SPR, a Beast or Megabeast typically less than 5, and Legendaries are generally Sapient-level or higher.''')
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

print('''How much Intelligence (INT) does the creature have? Intelligence represents the mental aptitude of the creature. Intelligence should differ with creature type. A Sapient has around 6-13 Intelligence, a Beast or Megabeast typically less than 5, and Legendaries are generally Sapient-level or higher.''')
creature_int = int_positive()

print('''How much Charisma (CHR) does the creature have? Charisma represents the strength of personality of a creature. Charisma should increase with a creature's intelligence.''')
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

while True:
  try:
    techniques_allowed = str(input())
    if(techniques_allowed != 'y' and techniques_allowed != 'n'):
      raise ValueError('D:')
    break
  except ValueError:
    print(yn_error_msg)

print('''How many different attacks does it have?''')
num_attacks = int_positive()
attacks = set()
for i in range(0, num_attacks):
  attacks.add(add_attack())

print('''You're all done! Generating HTML page...''')
make_html()
print('''You can find the new bestiary entry in the same directory as this script.''')

