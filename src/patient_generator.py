import random

from faker import Faker

fake = Faker("en_US")

male_first_names = [
    "Muhammad", "Ahmed", "Ali", "Usman", "Hamza",
    "Bilal", "Hassan", "Hussain", "Ayan", "Zain",
    "Saad", "Talha", "Abdullah", "Farhan", "Imran"
]

female_first_names = [
    "Fatima", "Ayesha", "Sara", "Zainab", "Hira",
    "Noor", "Iqra", "Maham", "Maryam", "Laiba",
    "Areeba", "Anaya", "Kinza", "Rabia", "Sana"
]

last_names = [
    "Khan", "Ahmed", "Malik", "Sheikh", "Raza",
    "Iqbal", "Butt", "Qureshi", "Siddiqui",
    "Ansari", "Mirza", "Ali"
]

doctor_names = [
    "Dr. Ayesha Khan",
    "Dr. Bilal Ahmed",
    "Dr. Hassan Raza",
    "Dr. Sana Malik",
    "Dr. Imran Sheikh"
]


def generate_patient(index):

    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        first = random.choice(male_first_names)
    else:
        first = random.choice(female_first_names)

    last = random.choice(last_names)

    patient = {
        "patient_id": f"P{index:05}",
        "report_id": f"R{index:05}",
        "name": f"{first} {last}",
        "age": random.randint(18, 75),
        "gender": gender,
        "phone": fake.numerify(text="03#########"),
        "doctor": random.choice(doctor_names)
    }

    return patient


if __name__ == "__main__":

    for i in range(1, 6):
        print(generate_patient(i))