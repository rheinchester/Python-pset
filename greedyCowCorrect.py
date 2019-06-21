def greedy_cow_transport(cows,limit=100):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def sortDict(dictionary):
        newDict = {}
        for key, value in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
            newDict[key] = value
        return newDict
    
    cowDict= sortDict(cows)
    sliceList = cowDict.copy()
    oneTrip, allTrip = [], []
    totalWeight = 0
    if len(sliceList) == 0:
        return allTrip
    else:
        for cow, weight in cowDict.items():
            if totalWeight + weight <= limit:
                totalWeight+=weight
                sliceList.pop(cow)
                oneTrip.append(cow)
        allTrip = allTrip + [oneTrip]
        return allTrip + greedy_cow_transport(sliceList, limit)

#  Progress:
# 1) we have sorted the dictionary correctly
# 2) we can return first item and pull out of list
# 3) we can slice item from list
# 4) we have created a recursive way to make another trip
# 5) we have appended one trip to all trips, via recursion

#
cows = {'Miss Bella': 15, 'MooMoo': 85, 'Louis': 45, 'Muscles': 65, 'Polaris': 20,
    'Horns': 50, 'Milkshake': 75, 'Clover': 5, 'Lotus': 10, 'Patches': 60}
limit = 100

print(greedy_cow_transport(cows, limit))



