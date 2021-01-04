import urllib.request

try:
    # Sources:
    # - https://ourworldindata.org/covid-vaccinations
    # - https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/vaccinations.csv
    # Columns: location,iso_code,date,total_vaccinations,daily_vaccinations,total_vaccinations_per_hundred,
    #          daily_vaccinations_per_million
    vaxxed_data = urllib.request.urlopen(
        'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv')\
        .readlines()
except Exception as e:
    for key, value in e.__dict__.items():
        print('------------------------------- EXCEPTION CAUGHT -------------------------------')
        print(key, value)
        print('--------------------------------------------------------------------------------')

# headers = vaxxed_data[0]

latest_day_data = [datum for datum in
                   [row.decode('utf-8').split(',') for row in vaxxed_data][::-1]
                   if datum[0] == 'United States'][0]

datestring = latest_day_data[2]
total_vaxxed = int(latest_day_data[3])

def generate_flag_emoji(country_code):
    """
    :param str country_code: A two letter all-caps country code like "US". it's actually called a regional indicator
                             symbol. See here: https://en.wikipedia.org/wiki/Regional_indicator_symbol

    Also see:
     - (main source) https://schinckel.net/2015/10/29/unicode-flags-in-python/
     - (linked above in main source) https://esham.io/2014/06/unicode-flags

    :rtype str: Generated flag emoji
    """
    OFFSET = ord('🇦') - ord('A') 
    return chr(ord(country_code[0]) + OFFSET) + chr(ord(country_code[1]) + OFFSET)

us_flag_emoji = generate_flag_emoji('US')

stats_str = f'{us_flag_emoji} {datestring}: {total_vaxxed:,} total vaxxed'
source_str = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'

print(f'{stats_str} | {source_str}')
