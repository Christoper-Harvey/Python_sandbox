my_list = [1, 2, 3, 4, 5]
range_list = [x for x in range(5)]
multiply_list = [x * 5 for x in range(6)]

print(multiply_list)

print([n for n in range(10) if n % 2 == 0])

people_you_know = ['John', 'Jacob', 'anna', 'CHRIS']
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)