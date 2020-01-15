def lookup():
    D = {
        "ROM": "READ ONLY MEMORY",
        "HDD": "HARD DISK DRIVE",
        "FDD": "FLOPPY DISK DRIVE",
        "RAM": "RANDOM ACCESS MEMORY",
        "CPU": "CENTRAL PROCESSING UNIT"
    }

    x = input("Enter Device Name: ").upper()

    result = [D.get(i) for i in D.keys() if i.startswith(x)]
    print("Device Not Found") if len(result) == 0 else [print(set(result))]


lookup()
lookup()
lookup()
