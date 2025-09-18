def famous_births(figures):
    # แปลง dict → list ของ dict
    values = list(figures.values())

    n = len(values)

    # เริ่มการ sort แบบ bubble sort
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            year_current = int(values[j]["date_of_birth"])
            year_next = int(values[j + 1]["date_of_birth"])

            if year_current > year_next:
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp

            j = j + 1
        i = i + 1

    # แสดงผลหลัง sort เสร็จ
    k = 0
    while k < n:
        person = values[k]
        print(person["name"] + " is a great scientist born in " + person["date_of_birth"] + ".")
        k = k + 1


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
