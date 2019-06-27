n = int(raw_input())
countries = [raw_input() for _ in xrange(n)]
uniqueCountries = set(countries)
total = len(uniqueCountries)

print total