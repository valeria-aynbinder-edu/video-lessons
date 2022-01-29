# Python sets - properties

"""
Property 1 - Uniqueness
"""

# Rainy months from multiple years
rainy_months_list = [
    'Jan', 'Feb', 'Dec', 'Mar',
    'Nov', 'Dec', 'Feb',
    'Jan', 'Feb', 'Dec']
print(f"""
Total {len(rainy_months_list)} rainy months in list: {rainy_months_list}
""")

# Getting unique months with rainfall by initializing set from the list above
rainy_months_set = set(rainy_months_list)
print(f"""
Total {len(rainy_months_set)} UNIQUE rainy months in set: {rainy_months_set}
""")

# An attempt to add already existing element to the set
# will not change it
print(f"Adding Dec to the set...")
rainy_months_set.add('Dec')
print(f"""
The set did not change, as expected.
Total {len(rainy_months_set)} UNIQUE rainy months in set: {rainy_months_set}
""")

"""
Property #2 - Absence of order
# """
# An attempt to get set element at specific index
# will raise an exception
print(f"\nTrying to access set element by index...")
try:
    rainy_months_set[0]
except TypeError as e:
    print(f"Error:{e}")

# But, you can iterate over set
print(f"Iterating over set...")
for i, month in enumerate(rainy_months_set):
    print(f"{month}")
