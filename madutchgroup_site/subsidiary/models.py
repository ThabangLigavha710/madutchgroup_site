from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SubsidiaryImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(upload_to='subsidiary_images')


    # def __str__(self):
        # return f'{self.user.username} SubsidiaryImages'

class Logo(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    logo1 = models.ImageField(default='default.jpg', upload_to='logo_images')
    logo2 = models.ImageField(default='default.jpg', upload_to='logo_images')

    # def __self__(self):
        # return f'{self.user.username} Logo'


class HomeImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(default='default.jpg', upload_to='home_images')
    contentImage1 = models.ImageField(default='default.jpg', upload_to='home_images')
    contentImage2 = models.ImageField(default='default.jpg', upload_to='home_images')

    # def __self__(self):
        # return f'{self.user.username} HomeImages'

class PropertyDevelopmentImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    propertyDevelopment1 = models.ImageField(default='default.jpg', upload_to='property_development_images')
    propertyDevelopment2 = models.ImageField(default='default.jpg', upload_to='property_development_images')
    propertyDevelopment3 = models.ImageField(default='default.jpg', upload_to='property_development_images')
    propertyDevelopment4 = models.ImageField(default='default.jpg', upload_to='property_development_images')
    propertyDevelopment5 = models.ImageField(default='default.jpg', upload_to='property_development_images')

    # def __self__(self):
    #     return f'{self.user.username} PropertyDevelopmentImage'


class CleaningImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    cleaning1 = models.ImageField(default='default.jpg', upload_to='cleaning_images')
    cleaning2 = models.ImageField(default='default.jpg', upload_to='cleaning_images')
    cleaning3 = models.ImageField(default='default.jpg', upload_to='cleaning_images')
    cleaning4 = models.ImageField(default='default.jpg', upload_to='cleaning_images')
    cleaning5 = models.ImageField(default='default.jpg', upload_to='cleaning_images')

    # def __self__(self):
    #     return f'{self.user.username} CleaningImage'


class LandscapingImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    landscaping1 = models.ImageField(default='default.jpg', upload_to='landscaping_images')
    landscaping2 = models.ImageField(default='default.jpg', upload_to='landscaping_images')
    landscaping3 = models.ImageField(default='default.jpg', upload_to='landscaping_images')
    landscaping4 = models.ImageField(default='default.jpg', upload_to='landscaping_images')
    landscaping5 = models.ImageField(default='default.jpg', upload_to='landscaping_images')

    # def __self__(self):
        # return f'{self.user.username} LandscapingImage'


class SuppliesImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    supplies1 = models.ImageField(default='default.jpg', upload_to='supplies_images')
    supplies2 = models.ImageField(default='default.jpg', upload_to='supplies_images')
    supplies3 = models.ImageField(default='default.jpg', upload_to='supplies_images')
    supplies4 = models.ImageField(default='default.jpg', upload_to='supplies_images')
    supplies5 = models.ImageField(default='default.jpg', upload_to='supplies_images')

    # def __self__(self):
    #     return f'{self.user.username} SuppliesImage'


class AccountingImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    accounting1 = models.ImageField(default='default.jpg', upload_to='accounting_images')
    accounting2 = models.ImageField(default='default.jpg', upload_to='accounting_images')
    accounting3 = models.ImageField(default='default.jpg', upload_to='accounting_images')
    accounting4 = models.ImageField(default='default.jpg', upload_to='accounting_images')
    accounting5 = models.ImageField(default='default.jpg', upload_to='accounting_images')

    # def __self__(self):
        # return f'{self.user.username} AccountingImage'


class PayrollImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    payroll1 = models.ImageField(default='default.jpg', upload_to='payroll_images')
    payroll2 = models.ImageField(default='default.jpg', upload_to='payroll_images')
    payroll3 = models.ImageField(default='default.jpg', upload_to='payroll_images')
    payroll4 = models.ImageField(default='default.jpg', upload_to='payroll_images')
    payroll5 = models.ImageField(default='default.jpg', upload_to='payroll_images')

    # def __self__(self):
        # return f'{self.user.username} PayrollImage'


class TaxImage(models.Model):
    # user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    tax1 = models.ImageField(default='default.jpg', upload_to='tax_images')
    tax2 = models.ImageField(default='default.jpg', upload_to='tax_images')
    tax3 = models.ImageField(default='default.jpg', upload_to='tax_images')
    tax4 = models.ImageField(default='default.jpg', upload_to='tax_images')
    tax5 = models.ImageField(default='default.jpg', upload_to='tax_images')

    # def __self__(self):
        # return f'{self.user.username} TaxImage'