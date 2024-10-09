#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for key in range(1, len(boxes) - 1):
        status = False
        for idx in range(len(boxes)):
            status = (key in boxes[idx] and key != idx)
            if status:
                break
        if status is False:
            return status
    return True
