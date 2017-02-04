from src.db import AddressDatabase
from src.address import Result


db = AddressDatabase()

code_insee_list = (
    '06085',
    '13002',
    '13004',
    '16102',
    '30032',
    '34129',
    '69091',
    '69256',
    '74256',
    '83047',
    '83050',
    '92078',
    '93032',
    '93047',
    '93071',
    '93073',
    '93078',
    '94011',
    '94077',
    '94078',
    '95280',
    '95323',
    '95637',
)

streets = set()
for street in db.streets:
    if street['code_insee'].decode('utf-8') in code_insee_list:
        streets.add(street['street_id'])
# print("# streets : ", len(streets))

localities = set()
for locality in db.localities:
    if locality['code_insee'].decode('utf-8') in code_insee_list:
        localities.add(locality['locality_id'])
# print('# locality : ', len(localities))

print(';'.join(('code_insee', 'addresse', 'x', 'y', 'code_iris')))
for idx, number in enumerate(db.numbers):
    if number['street_id'] in streets or number['locality_id'] in localities:
        r = Result.from_plate(db, idx, 0).to_address()
        address = r.text[0] + ', ' + r.text[1]
        insee = db.streets[number['street_id']]['code_insee'].decode('utf-8') if number['street_id'] \
            else db.localities[number['locality_id']]['code_insee'].decode('utf-8')
        line = (insee, address, r.x, r.y, r.code_iris)
        print(";".join(map(str, line)))