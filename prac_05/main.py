def get_ages(names, ages):
    oldest_age = -1
    oldest_index = -1
    for i, age in enumerate(ages):
        if age > oldest_age:
            oldest_age = age
            oldest_index = i
    return names[oldest_index]
    #  return names[ages.index(max(ages))]






def run_test():
    i = 0
    names = ["robert", "joseph", "richard"]
    ages = [21, 48, 87]
    #  print(names[i], "is", ages[i], "years old")
    print(get_ages(names, ages))

run_test()
