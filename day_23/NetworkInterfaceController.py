from day_13.IntcodeComputer import IntcodeComputer


class NetworkInterfaceController:
    def __init__(self) -> None:
        t = open('../resources/input_23.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))

        self.computers = [IntcodeComputer(program) for i in range(50)]
        self.packet_queues = [list() for i in range(50)]
        for c in range(50):
            mem, out, exit_code = self.computers[c].run_program(input=[c])
            print('Booting computer {}: {}'.format(c, out))
        self.nat_storage = None
        self.nat_sent_y = list()


    def run_network(self):
        while True:
            idle = True
            for c in range(len(self.computers)):
                if self.packet_queues[c]:
                    packet = self.packet_queues[c].pop(0)
                    if type(packet) is tuple:
                        self.packet_queues[c].insert(0, packet[1])
                        value = packet[0]
                    else:
                        value = packet
                    idle = False
                else:
                    value = -1
                mem, out, exit_code = self.computers[c].run_program(input=[value],
                                                                    reset_relative_pointer=False,
                                                                    reset_pointer=False,
                                                                    reset_memory=False)
                if out and len(out) % 3 == 0:
                    idle = False
                    while out:
                        addr = out.pop(0)
                        x = out.pop(0)
                        y = out.pop(0)
                        if addr < len(self.packet_queues):
                            self.packet_queues[addr].append((x, y))
                        else:
                            if addr == 255:
                                self.nat_storage = (x, y)
                        print('Sending -> {}: {}, {}'.format(addr, x, y))
            if idle:
                if self.nat_storage[1] not in self.nat_sent_y:
                    self.nat_sent_y.append(self.nat_storage[1])
                    self.packet_queues[0].append(self.nat_storage)
                else:
                    print('First y sent twice: {}'.format(self.nat_storage[1]))


controller = NetworkInterfaceController()
controller.run_network()