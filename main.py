#basler kameradan görüntü alma, kaydetme ve sıcaklık kontrolü

from pypylon import pylon

img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()

cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()
cam.StartGrabbing()