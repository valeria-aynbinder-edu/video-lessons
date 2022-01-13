# Python sets - rules

"""
Rule #1 - No duplicates
"""

# Rainy months from multiple years
rainy_months_list = [
    'Jan', 'Feb', 'Dec', 'Mar',
    'Nov', 'Dec', 'Feb',
    'Jan', 'Feb', 'Dec']
print(f"\nRainy months list "
      f"(total {len(rainy_months_list)}):"
      f"\n{rainy_months_list}")

# Getting unique months with rainfall
rainy_months_set = set(rainy_months_list)
print(f"\nUnique rainy months "
      f"(total {len(rainy_months_set)}):"
      f"{rainy_months_set}")

# An attempt to add already existing element to the set
# will not change it
print(f"\nAdding Mar to the set...")
rainy_months_set.add('Dec')
print(f"\nUnique rainy months "
      f"(total {len(rainy_months_set)}):"
      f"{rainy_months_set}")

"""
Rule #2 - No order
# """
# An attempt to get set element at specific index
# will raise an exception
print(f"\nTrying to access set element by index...")
try:
    rainy_months_set[0]
except Exception as e:
    print(f"\nError: {e}")

# Instead, you can iterate over set
print(f"Iterating over set...")
for month in rainy_months_set:
    print(f"{month}")
