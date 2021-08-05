import phonenumbers


from phonenumbers import geocoder

from phonenumbers import carrier

ch_number = phonenumbers.parse("+91763XXXX56560","CH")

print(geocoder.description_for_number(ch_number,"en"))

service_number = phonenumbers.parse("+91763XXXXX5650","RO")

print(carrier.name_for_number(service_number,"en"))
