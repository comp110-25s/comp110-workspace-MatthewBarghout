"""The goal of this program is to plan a tea party for me and 333 friends"""

_author_: str = "730737376"


def main_planner(guests: int) -> None:
    """Main planner brings all functions together"""
    tea_count = tea_bags(guests)
    treat_count = treats(guests)
    total_cost = cost(tea_count, treat_count)
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_count))
    print("Treats: " + str(treat_count))
    print("Cost:$" + str(round(total_cost, 2)))


def tea_bags(people: int) -> int:
    """A function that returns the number of total tea bags"""
    return people * 2


def treats(people: int) -> int:
    """This Function computates the number of treats needed at the party"""
    teas = tea_bags(people=people)
    return int(teas * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function computates the cost of tea bags and treats combined"""
    tea_cost = tea_count * 0.50
    treat_cost = treat_count * 0.75
    return tea_cost + treat_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
