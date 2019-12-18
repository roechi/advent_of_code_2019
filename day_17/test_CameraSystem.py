from day_17.CameraSystem import CameraSystem

def test_show_image():
    cs = CameraSystem()
    cs.show_image()

    cs.find_intersections()
    cs.rescue()

def test_encoding():
    lzw = CameraSystem.encode_LZW('AAAABBCDEABCDABCAAABCDEEEEEECBBBBBBDDAAE')
    print(lzw)