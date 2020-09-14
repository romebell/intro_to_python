class NBAPlayer():
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team
        self.salary = 0

    def add_salary(self, salary_amount=500000):
        self.salary += salary_amount

    def fine(self, fine_amount):
        self.salary -= fine_amount

    def trade_player(self, new_team):
        self.team = new_team

lebron_james = NBAPlayer("Lebron James", "PG", "Lakers")
lebron_james.name # Lebron James
lebron_james.position # PG
lebron_james.team # Lakers
lebron_james.salary # 0


lebron_james.add_salary(35000000)
print("{} salary is ${}.".format(lebron_james.name, lebron_james.salary))
lebron_james.add_salary(2000000)

carmelo_anthony = NBAPlayer("Carmelo Anthony", "SF", "Rockets")
carmelo_anthony.add_salary(5000000)
print("{} salary is ${}.".format(carmelo_anthony.name, carmelo_anthony.salary))

carmelo_anthony.fine(20000)
print(f"{carmelo_anthony.name} is fine 20000")

carmelo_anthony.trade_player("Blazers")
print(f"{carmelo_anthony.name} is currently a member of the {carmelo_anthony.team}")
