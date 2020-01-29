def parse_query():
    query = ""
    special_tokens = ["AND", "OR", "NOT"]
    found = False
    while query == "":
        query = input('Type the search criteria: ')
        criteria = query.split()

    # checks if the correct way of defining criteria is followed
    for i in range(0, len(criteria)):
        if criteria[i] in special_tokens:
            if len(criteria) != 3:
                raise IndexError
            if i != 1:
                raise ValueError
    print(criteria)
    return criteria
