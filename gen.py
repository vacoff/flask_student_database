import names 
import string
import random
from datetime import date, timedelta


class StudentGen:
    def __init__(self, count = 3):
        self.students_gen(count)

   
    def students_gen(self, count=50):
        self.students = []
        for x in range(count):
            name = names.get_full_name(gender = self.rand_gend()[1]).split()
            points = str(self.points())
            faculty = self.faculty()
            gender = self.rand_gend()[0]
            bdate = str(self.bdate())
            group = str(self.group())
            slug = self.slug()

            self.students.append({
                    "fname": name[0],
                    "sname":name[1],
                    "points": points,
                    "faculty": faculty,
                    "gender": gender,
                    "bdate": bdate,
                    "group": group,
                    "slug": slug
                })

    def points(self):
        return random.randint(51,100)

    def rand_gend(self):
        genders = ["male","female"]
        result = random.choice(genders)
        return [result[:1], result]

    def slug(self):
        result = "".join(random.choices(string.ascii_letters, k = 5))
        return result


    def faculty(self):
        bba_progs = ["Business Informatics","Industrial Engineering", "International Marketing","Mechatronics","Computer Engineering"]
        return random.choice(bba_progs)

    def bdate(self):
        start_date = date(1999, 1, 1)
        end_date = date(2003, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)

        return random_date

    def group(self):
        return f"{random.choice(['ZU','BA'])}0{random.randint(10,99)}"

