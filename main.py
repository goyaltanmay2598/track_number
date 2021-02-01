import phonenumbers
from test import number

from phonenumbers import geocoder
cc = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(cc,"en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))



#CH --> country history
#ch --> for country
# en --> for english language
#RO --> REGION OPERATOR