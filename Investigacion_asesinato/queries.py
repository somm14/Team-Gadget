
# Query para ver el informe del crimen
query1 = '''
SELECT *
FROM crime_scene_report
WHERE ("date" LIKE 20180115) AND (type = "murder") AND (city LIKE "SQL City");
'''

# Query para saber quién es la testigo_1
query2 = '''
SELECT a.name, a.address_street_name, a.address_number, b.transcript
FROM person AS a
LEFT JOIN interview AS b
ON a.id = b.person_id
WHERE (address_street_name LIKE "%Northwestern Dr%")
'''

# Query del testigo_2

query3 = '''
SELECT a.name, a.address_street_name, a.address_number, b.transcript
FROM person AS a
LEFT JOIN interview AS b
ON a.id = b.person_id
WHERE (address_street_name LIKE "%Franklin Ave%") AND (a.name LIKE "%Annabel%")
'''

# Query filtrando por las pistas_3

query4 = '''
SELECT * 
FROM "get_fit_now_member"
WHERE (membership_status = "gold") AND (id LIKE "%48%")
'''

# Query para saber quien tiene la matricula
query5 = '''
SELECT a.name, b.plate_number
FROM person AS a
LEFT JOIN drivers_license AS b
ON a.license_id = b.id
WHERE (a.id = 28819) OR (a.id = 67318)
AND b.plate_number LIKE "%H42W%"
'''