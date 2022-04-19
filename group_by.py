# Function that create dictionary from function and iterable.
# The keys in dictionary are the return value of the function pass and the values inside are all the items
# with the same values.
def create_dict_of_fun_equal(function_to_use, iter_to_use):
    # dictionary comprehension
    # filters the item that for them the function returns the key.
    return \
        {function_to_use(item): list
        (filter(lambda iter_item: function_to_use(iter_item) == function_to_use(item), iter_to_use))
         for item in iter_to_use}


if __name__ == '__main__':
    print(create_dict_of_fun_equal(len, ["hi", "bye", "yo", "try"]))
