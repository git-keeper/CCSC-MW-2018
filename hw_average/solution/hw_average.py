
def compute_hw_average(grades):
    if len(grades) == 0:
        return 0
    if len(grades) == 1:
        return grades[0]

    return (sum(grades)- min(grades)) / (len(grades) - 1)


print(compute_hw_average([1, 2, 3, 4]))