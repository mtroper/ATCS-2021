mountain_heights = {
"Mount Everest": 29029,
"K2": 28251,
"Kangchenjunga": 28169,
"Lhotse": 27940,
"Makalu": 27838
}
print("Mountain names")
for mountain in mountain_heights:
    print(mountain)
print("Mountain heights")
for mountain in mountain_heights:
    print(mountain_heights[mountain])
print("Mountain names and heights")
for mountain in mountain_heights:
    print(mountain + " is " + str(mountain_heights[mountain]) + " feet tall")