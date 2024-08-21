class Person:
    def __init__(self, firstname, familyname, birthfamilyname, gender, fathername, spousename, age):
        self.firstname = firstname
        self.familyname = familyname
        self.birthfamilyname = birthfamilyname
        self.gender = gender
        self.fathername = fathername
        self.spousename = spousename
        self.age = age

    def __lt__(self, other):
        # Compare based on age first, family size second, and lexicographical order third
        if self.age != other.age:
            return self.age > other.age
        elif self.familyname != other.familyname:
            return self.familyname < other.familyname
        else:
            return self.firstname < other.firstname

    def change_family(self, new_familyname):
        self.familyname = new_familyname
        self.birthfamilyname = new_familyname

    def divorce(self):
        self.familyname = self.birthfamilyname
        self.spousename = "NA"

    def marry(self, spouse, new_familyname):
        self.spousename = spouse.firstname
        self.familyname = new_familyname

    def print_details(self, leader):
        print(f"{self.firstname} {self.familyname} {self.birthfamilyname} {self.gender} {self.fathername} {self.spousename} {self.age} {leader.firstname}")

    def is_alive(self):
        return self.age != -1


class Family:
    def __init__(self):
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def set_leader(self):
        if self.members:
            self.members.sort()
            return self.members[0]

    def print_details(self):
        for member in self.members:
            if member.is_alive():
                member.print_details(self.leader)
            else:
                if member.gender == "Female" and member.spousename != "NA":
                    print(f"{member.firstname} {member.familyname} {member.birthfamilyname} {member.gender} {member.fathername} {member.spousename} {member.age} {member.spousename}")
                else:
                    print(f"{member.firstname} {member.familyname} {member.birthfamilyname} {member.gender} {member.fathername} {member.spousename} {member.age} NA")

    def is_alive(self):
        for member in self.members:
            if member.is_alive():
                return True
        return False


def find_family(families, familyname):
    for family in families:
        if familyname == family.members[0].familyname:
            return family
    return None


N = int(input())
persons = {}
families = []
for _ in range(N):
    firstname, familyname, birthfamilyname, gender, fathername, spousename, age = input().split()
    age = int(age)
    persons[firstname] = Person(firstname, familyname, birthfamilyname, gender, fathername, spousename, age)

E = int(input())
for _ in range(E):
    event = input().split()
    if event[0] == "MA":
        person1, person2 = event[1], event[2]
        family1 = find_family(families, persons[person1].familyname)
        family2 = find_family(families, persons[person2].familyname)
        new_familyname = max(family1.members[0].familyname, family2.members[0].familyname)
        family1.add_member(persons[person2])
        family1.add_member(persons[person1])
        family2.members = []
        for person in family1.members:
            person.marry(persons[person2], new_familyname)
        family1.leader = family1.set_leader()
    elif event[0] == "DI":
        person1, person2 = event[1], event[2]
        family1 = find_family(families, persons[person1].familyname)
        family2 = find_family(families, persons[person2].familyname)
        for person in family1.members:
            if person.firstname == person1:
                person.divorce()
        for person in family2.members:
            if person.firstname == person2:
                person.divorce()
        family1.leader = family1.set_leader()
        family2.leader = family2.set_leader()
    elif event[0] == "BI":
        name, gender, father, mother = event[1], event[2], event[3], event[4]
        age = -1
        for person in persons.values():
            if person.firstname == father:
                age = person.age
        persons[name] = Person(name, father, father, gender, father, "NA", age)
    elif event[0] == "DE":
        person1 = event[1]
        for person in persons.values():
            if person.firstname == person1:
                person.age = -1
        family1 = find_family(families, persons[person1].familyname)
        family1.leader = family1.set_leader()
    elif event[0] == "YP":
        years = int(event[1])
        for person in persons.values():
            if person.is_alive():
                person.age += years

for person in persons.values():
    if person.is_alive():
        person.print_details("NA")

