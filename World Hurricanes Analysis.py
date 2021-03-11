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

#####################################################

print("\n")
print("1 - Updated Damages Readability\n")

def update_damages(damages):
    new_damages = []
    conversion = {"M": 1000000,
                  "B": 1000000000}
    for damage in damages:
        if damage == 'Damages not recorded':
            new_damages.append(damage)
        elif damage[-1] in conversion.keys():
            new_value = float(damage[:-1]) * conversion[damage[-1]]
            new_damages.append(new_value)

    return new_damages

updated_damages = update_damages(damages)

print(updated_damages)

print("\n")
print("2 - Gather all given lists and create correspondent Hurricanes dictionary.\n")

def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}
    numb_hurricanes = len(names)
    for i in range(numb_hurricanes):
        hurricanes[names[i]] = {"Name": names[i],
                                "Month": months[i],
                                "Year": years[i],
                                "Max Sustained Wind": max_sustained_winds[i],
                                "Areas Affected": areas_affected[i],
                                "Damage": updated_damages[i],
                                "Deaths": deaths[i]}
    return hurricanes

hurricanes = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes['Katrina'])

print("\n")
print("3 - Arrange Hurricanes dictionary by Year as Key and list of Hurricanes dictionary's as values.\n")

hurricanes_by_year= {}

for name, month, year, max_wind, area, updt_damage, death in zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurr_year = {year: {'Name': name, 'Month':month, 'Year': year, 'Max_sustained_wind': max_wind, 'Area_affected': area, 'Damage': updt_damage, 'Deaths': death}}
    hurricanes_by_year.update(hurr_year)

print(hurricanes_by_year)

print("\n")
print("4 - Arrange Hurricanes dictionary by Area as Key and a count of how may times the Area was affected by Hurricanes as Values .\n")

affected_areas_count = {}

def affected_areas(dict):
    for hurricane_name in dict:
        for area in dict[hurricane_name]['Areas Affected']:
            if area in affected_areas_count:
                affected_areas_count[area] += 1
            else:
                affected_areas_count[area] = 1
    return affected_areas_count

print(affected_areas(hurricanes))


print("\n")
print("5 - Calculating the most affect Area by Hurricanes count.\n")

def max_areas_affected(affected_areas_count):
    max_area = ''
    max_count = 0
    for area in affected_areas_count:
        if affected_areas_count[area] > max_count:
            max_area = area
            max_count = affected_areas_count[area]
    return max_area, max_count

max_area, max_count = max_areas_affected(affected_areas_count)
print(max_area, max_count)


print("\n")
print("6 - Calculating the deadliest Hurricane.\n")

def deadliest (hurricanes):
    deadliest_hurricane = ''
    number_of_deaths = 0
    for hurricane in hurricanes:
        if hurricanes[hurricane]['Deaths'] > number_of_deaths:
            deadliest_hurricane = hurricane
            number_of_deaths = hurricanes[hurricane]['Deaths']
    return deadliest_hurricane, number_of_deaths 

deadliest, number = deadliest(hurricanes)
print(deadliest, number)

print("\n")
print("7 - Rating Hurricanes by Mortality [0-5]- Creating a new dictionary from Hurricanes existing dictionary.\n")

def mortality(hurricanes):
    mortality_rates = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane in hurricanes:
        rate = 0
        deaths = hurricanes[hurricane]['Deaths']

        if deaths == 0:
            rate = 0
        elif deaths > 0 and deaths <= 100:
            rate = 1
        elif deaths > 100 and deaths <= 500:
            rate = 2
        elif deaths > 500 and deaths <= 1000:
            rate = 3
        elif deaths > 1000 and deaths <= 10000:
            rate = 4
        else:
            rate = 5

        if rate not in mortality_rates:
            mortality_rates[rate] = hurricanes[hurricane]
        else:
            mortality_rates[rate].append(hurricanes[hurricane])
    return mortality_rates

mortality_rates = mortality(hurricanes)
print(mortality_rates)


print("\n")
print("8 - Calculating Hurricane that caused the Maximum Damage.\n")

def maximum_damage(hurricanes):
    damages = []
    for hurr in hurricanes:
        if hurricanes[hurr]['Damage'] != 'Damages not recorded':
            damages.append(hurricanes[hurr]['Damage'])
    greatest_damage = max(damages)
    for hurr in hurricanes:
        if hurricanes[hurr]['Damage'] == greatest_damage:
            return hurr, greatest_damage

print(maximum_damage(hurricanes))


print("\n")
print("9 - Rating Hurricanes by Damage [0-5] - Creating a new dictionary from Hurricanes existing dictionary.\n")

hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

def rate_by_damage(hurricanes):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    for name in hurricanes:
        if hurricanes[name]['Damage'] == 'Damages not recorded':
            hurricanes_by_damage[0].append(hurricanes[name])
        elif damage_scale[0] < hurricanes[name]['Damage'] <= damage_scale[1]:
            hurricanes_by_damage[1].append(hurricanes[name])
        elif damage_scale[1] < hurricanes[name]['Damage'] <= damage_scale[2]:
            hurricanes_by_damage[2].append(hurricanes[name])
        elif damage_scale[2] < hurricanes[name]['Damage'] <= damage_scale[3]:
            hurricanes_by_damage[3].append(hurricanes[name])
        elif damage_scale[3] < hurricanes[name]['Damage'] <= damage_scale[4]:
            hurricanes_by_damage[4].append(hurricanes[name])
        else:
            hurricanes_by_damage[5].append(hurricanes[name])
    return hurricanes_by_damage

print(rate_by_damage(hurricanes))