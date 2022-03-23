Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def update_damages(damages):
  updated_damages = []
  for damage in damages:
    if damage == 'Damages not recorded':
      updated_damages.append(damage)
    if 'M' in damage:
      updated_damages.append(float(damage.split('M')[0])*conversion['M'])
    if 'B' in damage:
      updated_damages.append(float(damage.split('B')[0])*conversion['B'])
  return updated_damages

# test function by updating damages
updated_damages = update_damages(damages)
print(updated_damages)  
print('')
# 2 
# Create a Table
def dict_hurricanes(names, months, years, max_sustained_winds, areas_affected, damage, deaths):
  list_hurricanes_values = []
  for i in range(len(names)):
    hurricanes_values = {}
    hurricanes_values.update({'Name':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind':max_sustained_winds[i], 'Areas Affected':areas_affected[i], 'Damage':damage[i], 'Death':deaths[i]})
    list_hurricanes_values.append(hurricanes_values)
  dict_hurricanes = {name:value for name, value in zip(names, list_hurricanes_values)}
  return dict_hurricanes

# Create and view the hurricanes dictionary
dict_hurricanes = dict_hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(dict_hurricanes)
print('')
# 3
#Organizing by Year
def organizing_by_year(dict_hurricanes):
  dict_hurricanes_by_year = {}
  for name in dict_hurricanes:
    current_year = dict_hurricanes[name]['Year']
    current_cane = dict_hurricanes[name]
    if current_year in dict_hurricanes_by_year:
      dict_hurricanes_by_year[current_year].append(current_cane)
    else:
      dict_hurricanes_by_year[current_year] = [current_cane]
  return dict_hurricanes_by_year

# create a new dictionary of hurricanes with year and key
dict_hurricanes_by_year = organizing_by_year(dict_hurricanes)
print(dict_hurricanes_by_year)
print('')
# 4
# Counting Damaged Areas
def counting_damaged_areas(dict_hurricanes):
  dict_areas_affected = {}
  for values in dict_hurricanes.values():
    for area in values['Areas Affected']:
      if area in dict_areas_affected:
        dict_areas_affected[area] += 1
      else:
        dict_areas_affected[area] = 1
  return dict_areas_affected

# create dictionary of areas to store the number of hurricanes involved in
dict_areas_affected = counting_damaged_areas(dict_hurricanes)
print(dict_areas_affected)
print('')
# 5 
# Calculating Maximum Hurricane Count
# def max_areas_affected(dict_areas_affected):
#   max_count = max(dict_areas_affected.values())
#   for area in dict_areas_affected.keys():
#     if dict_areas_affected[area] == max_count:
#       return area + ' was affected by the most hurricanes, which is ' + str(max_count) + ' times.'

def max_areas_affected(dict_areas_affected):
  max_area = 'South Texas'
  max_count = 0
  for area, count in dict_areas_affected.items():
    if count > max_count:
      max_area = area
      max_count = count
  return max_area + ' was affected by the most hurricanes, which is ' + str(max_count) + ' times.'

# find most frequently affected area and the number of hurricanes involved in
most_frequently_affected_area = max_areas_affected(dict_areas_affected)
print(most_frequently_affected_area)
print('')
# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(dict_hurricanes):
  max_hurricane = 'Felix'
  max_deaths = 0
  for name in dict_hurricanes:
    if dict_hurricanes[name]['Death'] > max_deaths:
      max_hurricane = name
      max_deaths = dict_hurricanes[name]['Death']
  return 'The deadliest hurricane is ' + max_hurricane + ', which killed ' + str(max_deaths) + ' people.'
# find highest mortality hurricane and the number of deaths
deadliest_hurricane = deadliest_hurricane(dict_hurricanes)
print(deadliest_hurricane)
print('')
# 7
# Rating Hurricanes by Mortality
def mortality_ratings(dict_hurricanes):
  dict_mortality_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for name in dict_hurricanes:
    num = dict_hurricanes[name]['Death']
    if num == 0:
      dict_mortality_ratings[0].append(name)
    elif num <= 100:
      dict_mortality_ratings[1].append(name)
    elif num <= 500:
      dict_mortality_ratings[2].append(name)
    elif num <= 1000:
      dict_mortality_ratings[3].append(name)
    elif num <= 10000:
      dict_mortality_ratings[4].append(name)
    else:
      dict_mortality_ratings[5].append(name)
  return dict_mortality_ratings
# categorize hurricanes in new dictionary with mortality severity as key
dict_mortality_ratings = mortality_ratings(dict_hurricanes)
print(dict_mortality_ratings)
print('')
# 8 Calculating Hurricane Maximum Damage
def max_damage(dict_hurricanes):
  max_name = 'Cuba I'
  max_damage = 0
  for name in dict_hurricanes:
    if dict_hurricanes[name]['Damage'] == 'Damages not recorded':
      continue
    if dict_hurricanes[name]['Damage'] > max_damage:
      max_damage = dict_hurricanes[name]['Damage']
      max_name = name
  return 'The highest damage inducing hurricane is ' + max_name + ', which caused damaged worth $' + str(max_damage) + '.'
# find highest damage inducing hurricane and its total cost
max_damage = max_damage(dict_hurricanes)
print(max_damage)
print('')
# 9
#Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def rating_by_damage(dict_hurricanes):
  rating_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 'Damages not recorded':[]}
  for name in dict_hurricanes:
    if dict_hurricanes[name]['Damage'] == 'Damages not recorded':
      rating_by_damage['Damages not recorded'].append(name)
    elif dict_hurricanes[name]['Damage'] == damage_scale[0]:
      rating_by_damage[0].append(name)
    elif dict_hurricanes[name]['Damage'] <= damage_scale[1]:
      rating_by_damage[1].append(name)
    elif dict_hurricanes[name]['Damage'] <= damage_scale[2]:
      rating_by_damage[2].append(name)
    elif dict_hurricanes[name]['Damage'] <= damage_scale[3]:
      rating_by_damage[3].append(name)
    elif dict_hurricanes[name]['Damage'] <= damage_scale[4]:
      rating_by_damage[4].append(name)
    else:
      rating_by_damage[5].append(name)      
  return rating_by_damage

# categorize hurricanes in new dictionary with damage severity as key
rating_by_damage = rating_by_damage(dict_hurricanes)
print(rating_by_damage)
