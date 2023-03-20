from datesCreation import get_holidays


def get_list_of_holidays():
    loh = list(get_holidays())
    loh.sort()
    result = []
    for i in loh:
        x = i.strftime('%d')
        y = i.strftime('%B')
        z = i.strftime('%Y')
        result.append((x, y, z))
    return result
