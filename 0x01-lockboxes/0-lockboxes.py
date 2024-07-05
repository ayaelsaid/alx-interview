#!/usr/bin/env python3
"""Lockboxes function"""


def canUnlockAll(boxes):
    """
    function to unlock boxes by keys
    """
    if type(boxes) is not list or len(boxes) == 0:
        return False

    n = len(boxes)
    checkedBoxes = [False] * n  # Initialize a list to track unlocked status of each box
    checkedBoxes[0] = True  # Box 0 is initially unlocked
    keys = set(boxes[0])  # Keys available initially in Box 0
    # Process keys to unlock more boxes
    while keys:
        key = keys.pop()
        if key < n and not checkedBoxes[key]:
            checkedBoxes[key] = True
            for k in boxes[key]:
                if k < n and not checkedBoxes[k]:
                    keys.add(k)
    # Check the last element using pop and iterate over the rest
    for status in checkedBoxes:
        if not status:
            return False

    return True
