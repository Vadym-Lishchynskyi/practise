def sort_by_name(arr):
    arr.sort(key=lambda x: x.name)

    return arr


def sort_by_category(arr):
    arr.sort(key=lambda x: x.category[0].name)

    return arr


def sort_by_date(arr):
    arr.sort(key=lambda x: x.start_date)

    return arr