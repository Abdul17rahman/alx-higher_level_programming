#!/usr/bin/python3
def best_score(a_dictionary):
    """ best_score - Finds a key with the bigst score

        Args:
            a_dictionary: dict with values

        Returns:
            a key with the highest score
    """
    if not a_dictionary:
        return None
    best_val = max(a_dictionary.values())
    for k, val in a_dictionary.items():
        if val == best_val:
            return k
