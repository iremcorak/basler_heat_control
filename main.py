#Basler save image and check cam temperature

from pypylon import pylon
import platform

num_img_save = 3
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()

cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()
cam.StartGrabbing()

for i in range(num_img_save):
    with cam.RetrieveResult(2000) as result:

        img.AttachGrabResultBuffer(result)

        if platform.system() == 'Windows':
            # quality (100 -> best quality, 0 -> poor quality).
            ipo = pylon.ImagePersistenceOptions()
            quality = 90 - i * 10
            ipo.SetQuality(quality)

            filename = "pypylon_img_%d.jpeg" % quality
            img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
        else:
            filename = "pypylon_img_%d.png" % i
            img.Save(pylon.ImageFileFormat_Png, filename)
        t = cam.DeviceTemperature.Value
        print("Cam temperature: ", t)
        img.Release()

    cam.StopGrabbing()
    cam.Close()
