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

# write your update damages function here:
def update_damage(damages):
    new_damages = []
    for el in damages:
        if el != "Damages not recorded":
            if el[-1] == "M":
                damage = float(el[:-1])*10**6
                new_damages.append(damage)
            else:
                damage = float(el[:-1])*10**9
                new_damages.append(damage)
        else:
            new_damages.append(el)
    return new_damages

damages = update_damage(damages)






# write your construct hurricane dictionary function here:
def hurricanes_dictionary_function(names,months,years,max_sustained_winds,areas_affected,damages,deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {"Name":names[i], "Month":months[i], "Year":years[i],
                                "Max Sustained Wind":max_sustained_winds[i], "Areas Affected": areas_affected[i],
                               "Damage":damages[i],"Deaths":deaths[i]}
    return hurricanes

hurricanes = hurricanes_dictionary_function(names,months,years,max_sustained_winds,areas_affected,damages,deaths)


# write your construct hurricane by year dictionary function here:

def hurricanes_by_year(hurricanes, years):
    new_dictionary = {}
    for year in years:
        list_year = []
        for hurricane in hurricanes:
            if hurricanes.get(hurricane).get("Year") == year:
                list_year.append(hurricanes.get(hurricane))
        new_dictionary[year] = list_year
    return new_dictionary

new_hurricanes = hurricanes_by_year(hurricanes, years)



# write your count affected areas function here:

def counting_damaged_areas(areas_affected):
    dic = {}
    for hurricane in areas_affected:
        for area in hurricane:
            if area not in dic.keys():
                dic[area] = 1
            else:
                dic[area] += 1
    return dic
        
damaged_areas = counting_damaged_areas(areas_affected)  

#forma alternativa de fazer

def different_area(areas_affected):
    areas = []
    for hurricane in areas_affected:
        for area in hurricane:
            if area not in areas:
                areas.append(area)
    return areas

def counting_damaged_areas_alternative(areas_affected):
    dic = {}
    areas = different_area(areas_affected)
    for area in areas:
        count = 0
        for hurricane in areas_affected:
            for el in hurricane:
                if el == area:
                    count += 1
        dic[area] = count
    return dic



# write your find most affected area function here:

def max_hurricane(areas):
    max_hurricane = 0
    for area in areas:
        if areas[area] > max_hurricane:
            max_area = area
            max_hurricane = areas[area]
    return "The area affected by the most hurricanes is {max_area} with {max_hurricane} hurricanes.".format(max_area=max_area,max_hurricane=max_hurricane)

max_area = max_hurricane(damaged_areas)


# write your greatest number of deaths function here:

def max_deaths(hurricanes):
    max_hurricane_deaths = 0
    for hurricane in hurricanes:
        if hurricanes[hurricane].get("Deaths") > max_hurricane_deaths:
            max_hurricane_deaths = hurricanes[hurricane].get("Deaths")
            hurricane_name = hurricane
    return "The deadliest hurricane was {hurricane_name} with {max_hurricane_deaths} deaths.".format(hurricane_name=hurricane_name,max_hurricane_deaths=max_hurricane_deaths)

deadliest_hurricane = max_deaths(hurricanes)



# write your catgeorize by mortality function here:

def rating_hurricanes_mortality(hurricanes):
    dic = {}
    dic[0] = [hurricanes.get(hurricane) for hurricane in hurricanes if hurricanes[hurricane].get("Deaths") == 0]
    dic[1] = [hurricanes.get(hurricane) for hurricane in hurricanes if 100 >= hurricanes[hurricane].get("Deaths") > 0]
    dic[2] = [hurricanes.get(hurricane) for hurricane in hurricanes if 500 >= hurricanes[hurricane].get("Deaths") > 100]
    dic[3] = [hurricanes.get(hurricane) for hurricane in hurricanes if 1000 >= hurricanes[hurricane].get("Deaths") > 500]
    dic[4] = [hurricanes.get(hurricane) for hurricane in hurricanes if 10000 >= hurricanes[hurricane].get("Deaths") > 1000]
    dic[5] = [hurricanes.get(hurricane) for hurricane in hurricanes if hurricanes[hurricane].get("Deaths") > 10000]
    return dic

rating_by_mortality = rating_hurricanes_mortality(hurricanes)



# write your greatest damage function here:

def max_damage(hurricanes):
    max_hurricane_damage = 0
    for hurricane in hurricanes:
        if type(hurricanes[hurricane].get("Damage")) != str:
            if hurricanes[hurricane].get("Damage") > max_hurricane_damage:
                max_hurricane_damage = hurricanes[hurricane].get("Damage")
                hurricane_name = hurricane
    max_hurricane_damage = str(int(max_hurricane_damage/10**9)) + "B"
    return "The hurricane that caused the greates damage was {hurricane_name} that cost {max_hurricane_damage} dollars.".format(hurricane_name=hurricane_name,max_hurricane_damage=max_hurricane_damage)

max_hurricane_damage = max_damage(hurricanes)





# write your catgeorize by damage function here:

def rating_hurricanes_damages(hurricanes):
    dic = {}
    hurricanes_update = {key:value for key, value in hurricanes.items() if type(value["Damage"]) != str}
    dic[0] = [hurricanes_update.get(hurricane) for hurricane in hurricanes_update if hurricanes_update[hurricane].get("Damage") == 0]
    dic[1] = [hurricanes_update.get(hurricane) for hurricane in hurricanes_update if 100000000 >= hurricanes_update[hurricane].get("Damage") > 0]
    dic[2] = [hurricanes_update.get(hurricane) for hurricane in hurricanes_update if 1000000000 >= hurricanes_update[hurricane].get("Damage") > 100000000]
    dic[3] = [hurricanes_update.get(hurricane) for hurricane in hurricanes_update if 10000000000 >= hurricanes_update[hurricane].get("Damage") > 1000000000]
    dic[4] = [hurricanes_update.get(hurricane) for hurricane in hurricanes_update if 50000000000 >= hurricanes_update[hurricane].get("Damage") > 10000000000]
    dic[5] = [hurricanes_update.get(hurricane) for hurricane in hurricanes_update if hurricanes_update[hurricane].get("Damage") > 50000000000]
    return dic    

rating_by_damage = rating_hurricanes_damages(hurricanes)
