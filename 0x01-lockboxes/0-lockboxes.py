#!/usr/bin/env python3
"""Lockboxes function"""


def canUnlockAll(boxes):
    """function to unlock boxes by keys """
    if type(boxes) is not list or len(boxes) == 0:
        return False

    n = len(boxes)
    checkedBoxes = [False] * n
    checkedBoxes[0] = True
    keys = set(boxes[0])
    while keys:
        key = keys.pop()
        if key < n and not checkedBoxes[key]:
            checkedBoxes[key] = True
            for k in boxes[key]:
                if k < n and not checkedBoxes[k]:
                    keys.add(k)
    for status in checkedBoxes:
        if not status:
            return False

    return True
