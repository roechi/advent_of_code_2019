from day_17.CameraSystem import CameraSystem

def test_show_image():
    cs = CameraSystem()
    cs.show_image()

    cs.find_intersections()
    cs.rescue()
