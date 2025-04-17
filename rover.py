class Rover:
    DIR_MAP = {
        "N": [0, 1],
        "S": [0, -1],
        "E": [1, 0],
        "W": [-1, 0],
    }
    DIRS = ["N", "E", "S", "W"]
    ROT_MAP = {"L": -1, "R": 1, "None": 0}
    max_pos = [0, 0]

    def __init__(self, x, y, dir_index):
        self.dir_index = dir_index
        self.pos = [x, y]

    def execute_commands(self, input):
        for cmd in input:
            if cmd == "L" or cmd == "R":
                action = [cmd, 0]
            else:
                action = ["None", 1]
            self.move(action)

            pass

    def move(self, move):
        # wrap around array
        self.dir_index = (self.dir_index + Rover.ROT_MAP[move[0]]) % len(Rover.DIRS)

        self.pos[0] += (
            min(Rover.max_pos[0], Rover.DIR_MAP[Rover.DIRS[self.dir_index]][0])
            * move[1]
        )

        self.pos[1] += (
            min(Rover.max_pos[1], Rover.DIR_MAP[Rover.DIRS[self.dir_index]][1])
            * move[1]
        )

    def output(self):
        return [self.pos[0], self.pos[1], Rover.DIRS[self.dir_index]]


def run():
    inputs = ["5 5", "1 2 N", "LMLMLMLMM", "3 3 E", "MMRMMRMRRM"]
    max_pos_input = inputs[0].split(" ")
    rovers = []
    Rover.max_pos = [int(max_pos_input[0]), int(max_pos_input[1])]
    for i, line in enumerate(inputs):
        if i == 0:
            continue
        if i % 2 == 1:
            rover_params = line.split(" ")
            new_rover = Rover(
                int(rover_params[0]),
                int(rover_params[1]),
                Rover.DIRS.index(rover_params[2]),
            )
            rovers.append(new_rover)
        elif i % 2 == 0:
            rovers[-1].execute_commands(line)
            print("Final: ", rovers[-1].output())


run()
