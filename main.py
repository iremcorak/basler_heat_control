#basler kameradan görüntü alma, kaydetme ve sıcaklık kontrolü

from pypylon import pylon

num_img_save = 10
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()

cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()
cam.StartGrabbing()

for i in range(num_img_save):
    with cam.RetrieveResult(2000) as result:

        img.AttachGrabResultBuffer(result)
