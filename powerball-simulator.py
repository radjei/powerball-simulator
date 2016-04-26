# Author: Ross A.
# The Powerball Simulator"

import random
from collections import Counter, defaultdict


class Powerball:
    print ""
    print "The Powerball Simulator"
    print "======================="

    # ticket_numbers = set(range(5))
    # ticket_powerball = 0
    #
    # balls = tuple(range(69))
    # powerballs = tuple(range(26))

    # def match_lists(list1, list2):
    #     """Find the dupes or number of matching items in each list"""
    #     set1 = set(list1)
    #     set2 = set(list2)
    #     # set3 contains all items common to set1 and set2
    #     set3 = set1.intersection(set2)
    #     # return number of matching items
    #     return len(set3)

    def __init__(self):
        Powerball.track_favorite_numbers = []

    def total_employees(self):
        tot_num_emps = 0
        while tot_num_emps <= 0:
            try:
                tot_num_emps = input("Enter the number of Greenphire employees to play: ")
                print ""
            except:
                print "\nEnter a number greater than zero. Please try again..."
        return tot_num_emps

    def employee_picks(self):
        employees_numbers = []
        employees = self.total_employees()

        for employee in range(employees):
            favorite_numbers = []

            is_valid = False
            while not is_valid:
                try:
                    first = raw_input("\nEnter your first name: ")
                    first_check = int(first)
                    if isinstance(first_check, int):
                        print "The first name cannot be an integer"
                        is_valid = False
                        continue
                    else:
                        is_valid = True
                except:
                    # When string is parsed to int, it throws exeption.
                    # Just ignore by setting the boolean
                    is_valid = True

            is_valid = False
            while not is_valid:
                try:
                    last = raw_input("Enter your last name: ")
                    last_check = int(last)
                    if isinstance(last_check, int):
                        print "The last name cannot be an integer"
                        is_valid = False
                        continue
                    else:
                        is_valid = True
                except:
                    # When string is parsed to int, it throws exeption.
                    # Just ignore by setting the boolean
                    is_valid = True

            selected = False
            while not selected:
                try:
                    firstpick = input("select 1st # (1 thru 69): ")
                    if (firstpick not in favorite_numbers) and (1 <= firstpick <= 69) and isinstance(firstpick, int):
                        favorite_numbers.append(firstpick)
                        self.track_favorite_numbers.append(firstpick)
                        selected = True
                except:
                    print "Please enter a number!"

            selected = False
            while not selected:
                try:
                    secondpick = input("select 2nd # (1 thru 69 excluding {}): ".format(firstpick))
                    if (secondpick not in favorite_numbers) and (1 <= secondpick <= 69) and isinstance(secondpick, int):
                        favorite_numbers.append(secondpick)
                        self.track_favorite_numbers.append(secondpick)
                        selected = True
                except:
                    print "Please enter a number!"

            selected = False
            while not selected:
                try:
                    thirdpick = input("select 3rd # (1 thru 69 excluding {} and {}): "
                                      .format(firstpick, secondpick))
                    if (thirdpick not in favorite_numbers) and (1 <= thirdpick <= 69) and isinstance(thirdpick, int):
                        favorite_numbers.append(thirdpick)
                        self.track_favorite_numbers.append(thirdpick)
                        selected = True
                except:
                    print "Please enter a number!"

            selected = False
            while not selected:
                try:
                    forthpick = input("select 4th # (1 thru 69 excluding {}, {}, and {}): "
                                      .format(firstpick, secondpick, thirdpick))
                    if (forthpick not in favorite_numbers) and (1 <= forthpick <= 69) and isinstance(forthpick, int):
                        favorite_numbers.append(forthpick)
                        self.track_favorite_numbers.append(forthpick)
                        selected = True
                except:
                    print "Please enter a number!"

            selected = False
            while not selected:
                try:
                    fifthpick = input("select 5th # (1 thru 69 excluding {}, {}, {}, and {}): "
                                      .format(firstpick, secondpick, thirdpick, forthpick))
                    if (fifthpick not in favorite_numbers) and (1 <= fifthpick <= 69) and isinstance(fifthpick, int):
                        favorite_numbers.append(fifthpick)
                        self.track_favorite_numbers.append(fifthpick)
                        selected = True
                except:
                    print "Please enter a number!"

            selected = False
            while not selected:
                try:
                    powerball_number = input("select Power Ball # (1 thru 26): ")
                    if (1 <= powerball_number <= 26) and isinstance(powerball_number, int):
                        self.track_favorite_numbers.append(powerball_number)
                        selected = True
                except:
                    print "Please enter a number!"

            employee_numbers = {
                'first': first,
                'last': last,
                'balls': sorted(favorite_numbers),
                'powerball': powerball_number
            }

            employees_numbers.append(employee_numbers)

        return employees_numbers

    def freq_of_numbers_in_dict(self, items):
        d = defaultdict(int)
        for item in items:
            d[item] += 1
        return d

    def unique_dupes_count(self, items):
        return [item for item, count in Counter(items).items() if count >= 1]

    def high_dict_elements_values(self, d):
        high_dict = dict((k, v) for k, v in d.items() if v > 1)
        if not high_dict:
            return d
        return high_dict


if __name__ == "__main__":
    powerball = Powerball()
    picks = powerball.employee_picks()

    d = powerball.freq_of_numbers_in_dict(Powerball.track_favorite_numbers)
    dict_elements = powerball.high_dict_elements_values(d)
    duplicates_count = powerball.unique_dupes_count(dict_elements.values())
    random.shuffle(duplicates_count)
    tied = random.choice(duplicates_count)

    # Display all employees with corresponding entries:
    print ""
    print "Display all employees with corresponding entries:"
    for record in picks:
        b_one = record['balls'][0]
        b_two = record['balls'][1]
        b_three = record['balls'][2]
        b_four = record['balls'][3]
        b_five = record['balls'][4]
        print "{} {} {} {} {} {} {} powerball: {}" \
            .format(record['first'], record['last'], b_one, b_two,
                    b_three, b_four, b_five, tied)

    # Powerball winning number:
    print ""
    print "Powerball winning number:"
    chosen_balls = random.sample(Powerball.track_favorite_numbers, 5)
    p_one = chosen_balls[0]
    p_two = chosen_balls[1]
    p_three = chosen_balls[2]
    p_four = chosen_balls[3]
    p_five = chosen_balls[4]
    print "{} {} {} {} {} powerball: {}".format(p_one, p_two, p_three, p_four, p_five, tied)
