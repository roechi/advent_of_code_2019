from nose.tools import assert_equal

from day_19.TractorBeam import TractorBeam

def test_get_affected_fields_0():
    tb = TractorBeam()

    affected_fields = tb.get_affected_fields(50, 50)
    print(affected_fields)

def test_get_affected_fields():
    tb = TractorBeam()

    #affected_fields = tb.get_affected_fields(50, 50)
    #print(affected_fields)

    ship = tb.fit_better()
    print(ship)
