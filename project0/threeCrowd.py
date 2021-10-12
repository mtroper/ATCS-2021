def crowd_test(names):
    if len(names) > 3:
        print("Room is crowded")
names = ["henry", "sheldon", "frank", "bill"]
crowd_test(names)
names.remove("henry")
names.remove("frank")
crowd_test(names)

