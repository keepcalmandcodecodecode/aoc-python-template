class Day:
    
    def read_input(self):
        name = "inputs/"+type(self).__name__ + ".txt"
        with open(name, 'r') as file:
            data = file.read()
            return data

    def part1(self, data):
        print("No part1")

    def part2(self, data):
        print("No part2")

    def run(self):
        data = self.read_input()
        self.part1(data)
        self.part2(data)