"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # near_earth_objects holds all NEOs in the csv
    near_earth_objects = []
    with open(neo_csv_path, 'r') as infile:
        csv_reader = csv.DictReader(infile, delimiter=',')
        for line in csv_reader:
            # map data so that they are in the correct format
            haz = (lambda x: x == 'Y')(line['pha'])
            diam = (lambda x: float('nan') if x == '' else float(line['diameter']))(line['diameter'])
            name = (lambda x: None if x == '' else line['name'])(line['name'])
            # create a near earth object for each csv line
            obj = NearEarthObject(designation=line['pdes'], name=name, diameter=diam, hazardous=haz)
            near_earth_objects.append(obj)
    return near_earth_objects


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # near_earth_objects holds all close approaches in the csv
    approach_objects = []
    with open(cad_json_path, 'r') as infile:
        # loads json data into dict-like structure
        data = json.load(infile)
        for line in data['data']:
            # convert necessary values to floats
            approach_velocity = float(line[7])
            approach_distance = float(line[4])
            obj = CloseApproach(time=line[3], distance=approach_distance, velocity=approach_velocity, neo_designation=line[0])
            approach_objects.append(obj)
    return approach_objects
