def filtering(phrase, arr, by_what):
    phrase = phrase.lower()
    res = []
    if by_what == 'name':
        for i in arr:
            if phrase in i.name.lower():
                res.append(i)

    elif by_what == 'category':
        for i in arr:
            if phrase in i.category[0].name.lower():
                res.append(i)

    elif by_what == 'start_date':
        #  TODO check
        for i in arr:
            if phrase in i.name:
                res.append(i)

    return res if res else None
