"""The `create_filters` function produces a collection of objects.

This is used by the `query` method to generate a stream of `CloseApproach` objects that match
all of the desired criteria. The arguments to `create_filters` are provided by
the main module and originate from the user's command-line options.

The `limit` function simply limits the maximum number of values produced by an
iterator.

"""
import operator
import itertools


def create_filters(date=None, start_date=None, end_date=None,
                   distance_min=None, distance_max=None,
                   velocity_min=None, velocity_max=None,
                   diameter_min=None, diameter_max=None,
                   hazardous=None):
    """Create a collection of filters from user-specified criteria.

    The return value must be compatible with the `query` method of `NEODatabase`
    because the main module directly passes this result to that method. For now,
    this can be thought of as a collection of `AttributeFilter`s.

    :param date: A `date` on which a matching `CloseApproach` occurs.
    :param start_date: A `date` on or after which a matching `CloseApproach` occurs.
    :param end_date: A `date` on or before which a matching `CloseApproach` occurs.
    :param distance_min: A minimum nominal approach distance for a matching `CloseApproach`.
    :param distance_max: A maximum nominal approach distance for a matching `CloseApproach`.
    :param velocity_min: A minimum relative approach velocity for a matching `CloseApproach`.
    :param velocity_max: A maximum relative approach velocity for a matching `CloseApproach`.
    :param diameter_min: A minimum diameter of the NEO of a matching `CloseApproach`.
    :param diameter_max: A maximum diameter of the NEO of a matching `CloseApproach`.
    :param hazardous: Whether the NEO of a matching `CloseApproach` is potentially hazardous.
    :return: A collection of filters for use with `query`.
    """
    # create an array of filters that that have been passed to the function
    filters = []
    # append a filter for each argument that has been passed to the function
    if distance_min:
        filters.append((lambda x: x if x.distance >= distance_min else False))
    if distance_max:
        filters.append((lambda x: x if x.distance <= distance_max else False))
    if velocity_min:
        filters.append((lambda x: x if x.velocity >= velocity_min else False))
    if velocity_max:
        filters.append((lambda x: x if x.velocity <= velocity_max else False))
    if hazardous is not None:
        filters.append((lambda x: x if x.neo.hazardous == hazardous else False))
    if diameter_min:
        filters.append((lambda x: x if x.neo.diameter >= diameter_min else False))
    if diameter_max:
        filters.append((lambda x: x if x.neo.diameter <= diameter_max else False))
    if date:
        filters.append((lambda x: x if x.time.date() == date else False))
    if start_date:
        filters.append((lambda x: x if x.time.date() >= start_date else False))
    if end_date:
        filters.append((lambda x: x if x.time.date() <= end_date else False))

    return filters


def limit(iterator, n=None):
    """Produce a limited stream of values from an iterator.

    If `n` is 0 or None, don't limit the iterator at all.

    :param iterator: An iterator of values.
    :param n: The maximum number of values to produce.
    :yield: The first (at most) `n` values from the iterator.
    """
    if (n == 0) or (n is None):
        return iterator

    return itertools.islice(iterator, n)
