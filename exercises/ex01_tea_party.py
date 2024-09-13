"""Goal is to define a function, call it, and produce outputs"""

__author__ = "730776458"


def main_planner(guest: int) -> None:
    """Determines number of guest attending party"""
    print("A Cozy Tea Party for " + str(guest) + " people!")
    print("Tea Bags" + ": " + str(tea_bags(people=guest)))
    print("Treats" + ": " + str(treats(people=guest)))
    print(
        "Cost"
        + ": "
        + "$"
        + str(
            float(
                cost(
                    tea_count=(tea_bags(people=guest)),
                    treat_count=(treats(people=guest)),
                )
            )
        )
    )


# function calls other function definitions to perform written calculation
# does not compute any direct calculation itself

# print(main_planner(guest=2))  # type: ignore

# print(main_planner(guest=334))  # type: ignore


def tea_bags(people: int) -> int:
    """Function determines tea bags needed for each people"""
    # Each person requires 2 tea bags

    return people * 2


# tea_bags(people=2)  # type: ignore
# tea_bags(people=4)  # type: ignore


def treats(people: int) -> int:
    """Function determines the numbers of treats needed for each tea"""

    # people on left is parameter from tea_bags
    # Determines that each people get 2 tea bags
    # people on right is paremeter from treats
    # Each tea bag is multiplied by 1.5
    # return value of treats for each people

    return int(tea_bags(people=people) * 1.5)


# Key word argument is people=2
# People is the parameter name and 2 is the value assigned to parameter
# treats(people=4)  # type: ignore


def cost(tea_count: int, treat_count: int) -> float:
    """Function calculate cost of tea bags and treats combined"""

    # cost per tea and treat
    tea_price = 0.50
    treat_price = 0.75

    # total cost of all tea together
    total_tea_cost = tea_price * tea_count

    # total cost of all treat together
    total_treat_cost = treat_price * treat_count

    # total cost of tea and treat together
    total_cost = total_tea_cost + total_treat_cost

    # return total cost
    return float(total_cost)


# cost(tea_count=2, treat_count=6)  # type: ignore:
# cost(tea_count=2, treat_count=1)  # type: ignore


if __name__ == "__main__":
    main_planner(guest=int(input("How many guests are attending your tea party? ")))
