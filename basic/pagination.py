def pagination(result_set):
    if len(result_set) > 0:
        while True:
            try:
                page_length = int(input("Enter the page length: "))

                if page_length > len(result_set):
                    # print("Page length cannot be greater than ", len(result_set))
                    raise Exception
                elif page_length <= 0:
                    # print("Page length must be greater than 0")
                    raise Exception
                else:
                    break
                break
            except:
                print("Enter only numbers in range of 1 to ", len(result_set))

        index = 0
        printable = result_set[index:page_length]
        print()
        if printable:
            for (key, value) in printable:
                line_new = '{:<150}   {:>15}'.format(value,key)
                print(line_new)

        index = page_length

        while True:
            print()
            char = input(
                "Enter A for the previous page, D for the next page and X for changing the page length, Q for exit:  ")
            if char == 'X':
                while True:
                    try:
                        page_length = int(input("Enter the page length:  "))

                        if page_length <= 0 or page_length> len(result_set):
                            raise Exception
                        else:
                            index = 0
                            printable = result_set[index:page_length]
                            print()
                            if printable:
                                for (key,value) in printable:
                                    line_new = '{:<150}   {:>15}'.format(value,key)
                                    print(line_new)
                            index = page_length
                            break
                    except:
                        print("Enter only numbers in range of 1 to ", len(result_set))
            elif char == 'A':
                tmp = index
                index = index - 2 * page_length
                print()
                printable = result_set[index: index + page_length]
                if printable:
                    for (key, value) in printable:
                        line_new = '{:<150}   {:>15}'.format(value,key)
                        print(line_new)
                    index = index + page_length
                else:
                    print("There is no previous page")
                    index = tmp


            elif char == 'D':
                printable = result_set[index: index + page_length]
                print()
                if printable:
                    for (key, value) in printable:
                        line_new = '{:<150}   {:>15}'.format(value,key)
                        print(line_new)
                    index = index + page_length
                else:
                    print("There is no next page")

            elif char == 'Q':
                break

            else:
                print("Only enter the aforementioned characters!")
