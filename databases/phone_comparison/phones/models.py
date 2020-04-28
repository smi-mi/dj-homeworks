from django.db import models


class Phone(models.Model):
    model = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    os = models.CharField(max_length=10)
    ram = models.PositiveIntegerField(null=True)
    ppi = models.PositiveIntegerField()
    double_camera = models.BooleanField()
    processor = models.CharField(max_length=50)
    screen_resolution = models.CharField(max_length=10)
    fm_radio = models.BooleanField()


class Iphone(Phone):
    air_pods = models.BooleanField()
    face_id = models.BooleanField()
    apple_pay = models.BooleanField()

    def extra(self):
        res = ''
        if self.air_pods:
            res += 'AirPods\n'
        if self.face_id:
            res += 'FaceID\n'
        if self.apple_pay:
            res += 'ApplePay\n'
        return res


class Samsung(Phone):
    double_sided_screen = models.BooleanField()

    def extra(self):
        res = ''
        if self.double_sided_screen:
            res += 'Двусторонний экран\n'
        return res


class Mi(Phone):

    def extra(self):
        res = ''
        return res
