# # Define a set 's'
# s = {'a', 'c', 'd'}
#
# # Statement A
# result_A = 'a' in s or 'b' not in s
# print(f"Result of Statement A: {result_A}")  # Output will be True
#
#
# # Statement B
# result_B = 'a' in s or not ('b' in s)
# print(f"Result of Statement B: {result_B}")  # Output will be True
#
# # Statement C
# result_C = not ('a' not in s and 'b' in s)
# print(f"Result of Statement C: {result_C}")  # Output will be True

# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for element in l:
#     if element[:6] != 'Forest':
#         print(element)

        # if not element.startswith("Forest"):



# if not element[:6] == "Forest":

# f_suburbs = dict()
# f_suburbs["Fairfield"] = 18081
# f_suburbs["Fairfield East"] = 5273
# f_suburbs["Fairfield Heights"] = 7517
# f_suburbs["Fairfield West"] = 11575
# f_suburbs["Fairlight"] = 5840
# f_suburbs["Fiddletown"] = 233
# f_suburbs["Five Dock"] = 9356
# f_suburbs["Flemington"] = None
# f_suburbs["Forest Glen"] = None
# f_suburbs["Forest Lodge"] = 4583
# f_suburbs["Forestville"] = 8329
# f_suburbs["Freemans Reach"] = 1973
# f_suburbs["Frenchs Forest"] = 13473
# f_suburbs["Freshwater"] = 8866

# for suburb, population in f_suburbs.items():
#     if suburb.startswith("F") and not suburb.startswith("Forest") and population is not None:
#         print(f"{suburb}: {population}")

# for suburb, population in f_suburbs.items():
#     if suburb.startswith("F") and not suburb.startswith("Forest") and population is not None:
#         print(f"{suburb}: {population}")

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 != 0:
#         print(f"{i}: Fizz")
#     elif i % 5 == 0 and i % 3 != 0:
#         print(f"{i}: Buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print(f"{i}: FIZZ BUZZ")
#     else:
#         print(i)


# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for positional_index, suburb in enumerate(l):
#     print(f'{positional_index}: {suburb}')

# first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
# middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
# last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
#
# for first_name in first_names:
#     for middle_name in middle_names:
#         for last_name in last_names:
#             full_name = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
#             print(full_name)

first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']

for last_name in last_names:
    for first_name in first_names:
        for middle_name in middle_names:
            if middle_name is not None:
                full_name = f'{first_name} {middle_name} {last_name}'
            else:
                full_name = f'{first_name} {last_name}'
            print(full_name)
