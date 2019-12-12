from nose.tools import assert_equal

from day_12.MoonTracker import MoonTracker


def test_apply_step():
    moons = [(-1, 0, 2),
             (2, -10, -7),
             (4, -8, 8),
             (3, 5, -1)]

    tracker = MoonTracker(moons)
    for i in range(10):
        tracker.apply_step()

    energy = tracker.calc_system_energy()
    assert_equal(energy, 179)

def test_simulate():
    moons = [(-1, 0, 2),
             (2, -10, -7),
             (4, -8, 8),
             (3, 5, -1)]

    tracker = MoonTracker(moons)
    steps = tracker.simulate_until_state_repeats()
    assert_equal(steps, 2772)


def test_result_part_one():
    moons = [(15, -2, -6),
             (-5, -4, -11),
             (0, -6, 0),
             (5, 9, 6)]
    tracker = MoonTracker(moons)
    for i in range(1000):
        tracker.apply_step()

    energy = tracker.calc_system_energy()
    print('Total energy: {}'.format(energy))
