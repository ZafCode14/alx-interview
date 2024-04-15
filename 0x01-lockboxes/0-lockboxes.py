#!/usr/bin/python3
"""Module with a python script"""


def canUnlockAll(boxes):
    """lockbox function"""
    if not boxes:
        return False

    visited = set()
    queue = [0]
    visited.add(0)

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                queue.append(key)
                visited.add(key)

    return len(visited) == len(boxes)
