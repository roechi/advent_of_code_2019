from unittest import TestCase

from nose.tools import assert_equal

from day_3.WireTracer import WireTracer


class TestWireTracer(TestCase):
    def test_add_wire(self):
        tracer = WireTracer()
        tracer.add_wire(['R8', 'U5', 'L5', 'D3'])
        tracer.add_wire(['U7','R6','D4','L4'])
        assert_equal(tracer.get_closest_intersection(), (3, 3))
        assert_equal(tracer.get_closest_intersection_distance(), 6)

    def test_add_wires(self):
        wire_one_one = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
        wire_one_two = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
        distance_one = 159

        tracer_one = WireTracer()
        tracer_one.add_wire(wire_one_one)
        tracer_one.add_wire(wire_one_two)

        assert_equal(tracer_one.get_closest_intersection_distance(), distance_one)

        wire_two_one = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
        wire_two_two = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
        distance_two = 135

        tracer_two = WireTracer()
        tracer_two.add_wire(wire_two_one)
        tracer_two.add_wire(wire_two_two)

        assert_equal(tracer_two.get_closest_intersection_distance(), distance_two)

    def test_result_part_one(self):
        t = open('../resources/input_3.txt')
        lines = t.readlines()
        t.close()

        parsed_lines = list()

        for line in lines:
            parsed_line = line.split(',')
            parsed_lines.append(parsed_line)

        tracer = WireTracer()

        for line in parsed_lines:
            tracer.add_wire(line)

        print('The shortest distance to an intersection is: ' + str(tracer.get_closest_intersection_distance()))
