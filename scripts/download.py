"""Download CSV files from https://www.ncdrisc.org/data-downloads-height.html

This script would automatically download the Global, Country and Region \
specific height data from the NCD RisC website.
"""
import urllib.request as request

sources = {
    'global': 'https://www.ncdrisc.org/downloads/bmi_height/height/global/NCD_RisC_Lancet_2020_height_child_adolescent_global.csv',
    'country-specific': 'https://www.ncdrisc.org/downloads/bmi_height/height/all_countries/NCD_RisC_Lancet_2020_height_child_adolescent_country.csv',
    'region-specific': 'https://www.ncdrisc.org/downloads/bmi_height/height/regional/NCD_RisC_Lancet_2020_height_child_adolescent_region.csv'
}

for key, value in sources.items():
    print('Downloading {k} height data into archive/{k}.csv...'
            .format(k=key))
    filename, headers = request.urlretrieve(value, 'archive/{}.csv'.format(key))
    print('Downloaded into {}'.format(filename), '\n\n')
