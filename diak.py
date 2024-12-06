class Diak:
    def __init__(self, name):
        self.name = name
        self.subjects = {
            "matematika": [],
            "tortenelem": [],
            "fizika": []
        }

    def add_points(self, subject, score):
        if subject in self.subjects:
            if isinstance(score, int) and score >= 0:
                self.subjects[subject].append(score)
            else:
                raise ValueError("A pontszám egy nemnegatív egész szám kell, hogy legyen.")
        else:
            raise ValueError(f"{subject} nem érvényes tantárgy.")

    def calc_average(self, subject):
        if subject in self.subjects:
            tests = self.subjects[subject]
            if tests:
                return sum(tests) / len(tests)
            return None
        else:
            raise ValueError(f"{subject} nem érvényes tantárgy.")

    def calc_all_average(self):

        all_tests = []
        for subject, tests in self.subjects.items():
            all_tests.extend(tests)
        if all_tests:
            return sum(all_tests) / len(all_tests)
        return None



