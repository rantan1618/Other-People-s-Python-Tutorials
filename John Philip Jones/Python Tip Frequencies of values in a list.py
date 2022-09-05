from collections import Counter

hourly_temperatures = [25,25,26,26,26,27,27,26,
                       26,27,27,26,25,25,26,26,
                       26,26,26,27,26,25,26,26]

frequencies = Counter(hourly_temperatures)
print(frequencies)