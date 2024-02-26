from django.test import TestCase

# Create your tests here.
# from Recepies.Recepies.settings import PHONES
from models import Phone
import csv


database = []
def download():
    with open('phones.csv', newline='') as filer:
        reader = csv.DictReader(filer, delimiter=';')
        for row in reader:
            database.append(row)
download()


for i in database:
    print(i)

phone = Phone(
                id=database[1]['id'],
                name=database[1]['name'],
                price=database[1]['price'],
                image=database[1]['image'],
                release_date=database[1]['release_date'],
                lte_exists=database[1]['lte_exists'],
                slug=database[1]['slug'],
            )
phone.save()
    # return f'all done. New phone {phone.name}, {phone.price}'


# for i in database:
#     print(i['name'])
# print(database)

# id = models.CharField(max_length=50)
# name = models.CharField(max_length=50)
# price = models.CharField(max_length=50)
# image = models.CharField(max_length=50)
# release_date = models.CharField(max_length=50)
# lte_exists = models.CharField(max_length=50)
# slug = models.CharField(max_length=50)