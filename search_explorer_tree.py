def search(d, k, path=None):
    # searches for the key 'k' in the list 'PC' and returns the path as per the explorer tree in windows
    if path is None:
        path = []
    if not isinstance(d, dict):
        return False
    if k in d.keys():
        path.append(k)
        return path

    else:
        check = list(d.keys())
        while check:
            first = check[0]
            path.append(first)
            if search(d[first], k, path) is not False:
                break
            else:
                check.pop(0)
                path.pop(-1)
        else:
            return False
        return path
