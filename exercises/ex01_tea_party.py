"""The goal of this program is to plan a tea party for me and 333 friends"""

__author__ = "730737376"


# Implements all functions created and use other functions to run
def main_planner(guests: int) -> None:
    """Main planner brings all functions together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# This function takes an argument of a given number of people and doubles it to calculate the number of tea bags needed
def tea_bags(people: int) -> int:
    """A function that returns the number of total tea bags"""
    return people * 2


# This function takes an argument of a given number of people and returns the int version of the amount of teabags needed times 1.5
def treats(people: int) -> int:
    """This Function computates the number of treats needed at the party"""
    return int((tea_bags(people=people)) * 1.5)


# This function calculates the cost of the tea party based on the fact that each tea bag costs 50 cents and each treat costs 75 cents
def cost(tea_count: int, treat_count: int) -> float:
    """This function computates the cost of tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


# Calls the main_planner function and everything created
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
