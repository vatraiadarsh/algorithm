# We sort the list of denominations {a1, a2, a3 ...an}.
# We get the largest denomination in {a1, a2, a3...an} which is smaller than A.
# We obtain the division by dividing A by the largest denomination.
# We get the remaining amount A by getting the remainder using (A % largest denominator).
# If the value of A becomes 0, then we return the result.
# Else If the value of A is greater than 0, we append the largest denominator and division variable in the result variable. And repeat the steps 2-5.

def basic_small_change(denom, total_amount):
    sorted_denominations = sorted(denom, reverse=True)

    number_of_denoms = []

    for i in sorted_denominations:
        div = total_amount // i
        total_amount = total_amount % i
        if div > 0:
            number_of_denoms.append((i, div))

    return number_of_denoms

# sort the list in reverse so that we can obtain the largest denomination at index 0.
#  Now, starting from index 0 of the sorted list of denominations, sorted_denominations,
#  we iterate and apply the greedy technique:


def optimal_small_change(denom, total_amount):
    sorted_denominations = sorted(denom, reverse=True)
    series = []
    for j in range(len(sorted_denominations)):
        term = sorted_denominations[j:]
        # The outer for loop enables us to limit the denominations from which we find our solution
        # Assuming that we have the list [5, 4, 3] in sorted_denominations, slicing it with [j:]
        #  helps us obtain the sublists [5, 4, 3], [4, 3], and [3], from which we try to find the right combination.
        number_of_denoms = []
        local_total = total_amount
        for i in term:
            div = local_total // i
            local_total = local_total % i
            if div > 0:
                number_of_denoms.append((i, div))

        series.append(number_of_denoms)

    return series


denom = [5, 4, 3, 2, 1]
print(basic_small_change(denom, 17))

print(optimal_small_change(denom, 17))
