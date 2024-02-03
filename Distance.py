import geopy.distance

def distance(coordinates,destination):
    destination_coordinates = [[56.732014, -111.375961],[49.246292,-123.116226],[39.9042,116.4074]]
    distances = []
    for coordinate in destination_coordinates:
        distances.append(geopy.distance.geodesic(coordinates, coordinate).km)

    if destination == 'Fort McMurray':
        return distances[0]
    elif destination == 'Vancouver':
        return distances[1]
    elif destination == 'Beijing':
        return distances[2]