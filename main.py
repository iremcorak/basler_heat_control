#basler kameradan görüntü alma, kaydetme ve sıcaklık kontrolü

from pypylon import pylon
import platform

num_img_save = 10
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()

cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()
cam.StartGrabbing()

for i in range(num_img_save):
    with cam.RetrieveResult(2000) as result:

        img.AttachGrabResultBuffer(result)

        if platform.system() == 'Windows':
            # The JPEG format that is used here supports adjusting the image
            # quality (100 -> best quality, 0 -> poor quality).
            ipo = pylon.ImagePersistenceOptions()
            quality = 90 - i * 10
            ipo.SetQuality(quality)
