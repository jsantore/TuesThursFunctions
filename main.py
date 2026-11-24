def load_data():
    all_countries = []
    with open("CountryData.txt") as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.split("*")
            this_country = {}
            this_country["name"] = data[1]
            this_country["population"] = int(data[2])
            this_country["pop_change"] = int(data[4])
            this_country["median_age"] = float(data[-3])
            this_country['pop_density']=float(data[5])
            all_countries.append(this_country)
    return all_countries

def main():
    country_data = load_data()
    print(country_data)
    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == "9":
            break
        elif choice == "1":
            age_cutoff = float(input("Enter age cutoff: "))
            density_cutoff = float(input("Enter density cutoff: "))
            find_young_densely_pop(age_cutoff, density_cutoff, country_data)

def find_young_densely_pop(how_young, how_dense, country_list):
    for country in country_list:
        if country["pop_density"]>how_dense  and country['median_age']<how_young:
            print(f"{country['name']} is a young densely poulated country")

def print_menu():
    print("""
    [1] Find young countries that are densely populated
    [2] Find counties with greatest pop change
    [9] Exit
    """)

main()
