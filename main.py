def load_data():
    all_countries = []
    with open("CountryData.txt") as file:
        lines = file.readlines()
        for line in lines:
            data = line.split("*")
            this_country = {}
            this_country["name"] = data[1]
            this_country["population"] = int(data[2])
            this_country["pop_change"] = int(data[3])
            this_country["median_age"] = int(data[-3])
            all_countries.append(this_country)
    return all_countries

def main():
    pass

def print_menu():
    pass