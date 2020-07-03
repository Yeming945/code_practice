import unittest


def city_country(city, country, population=0):
    if population == 0:
        result = f"{city}, {country}"
    else:
        result = f"{city}, {country} - population {population}"
    return result.title()


print(city_country('santiago', 'chile', 5000000))


class CountryTestClass(unittest.TestCase):
    def test_city_country(self):
        a = city_country('santiago', 'chile')
        self.assertEqual(a, 'Santiago, Chile')

    def test_city_country_population(self):
        a = city_country('santiago', 'chile', 5000000)
        self.assertEqual(a, 'Santiago, Chile - Population 5000000')


unittest.main()
