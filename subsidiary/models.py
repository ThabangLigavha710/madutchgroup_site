from django.db import models
from django.contrib.auth.models import User
from . import rename

# Create your models here.

class SubsidiaryImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(upload_to=rename.rename_file('subsidiary_images', 'subsidiary_image', 1))


    def __str__(self):
        return f'{self.user.username} SubsidiaryImages'

class Logo(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    logo1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('logo_images', 'logo_image', 1))
    logo2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('logo_images', 'logo_image', 2))

    def __self__(self):
        return f'{self.user.username} Logo'


class HomeImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(default='default.jpg', upload_to=rename.rename_file('home_images', 'home_image', 1))
    contentImage1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('home_images', 'home_image', 2))
    contentImage2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('home_images', 'home_image', 3))

    def __self__(self):
        return f'{self.user.username} HomeImages'

class PropertyDevelopmentImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    propertyDevelopment1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 1))
    propertyDevelopment2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 2))
    propertyDevelopment3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 3))
    propertyDevelopment4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 4))
    propertyDevelopment5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 5))

    def __self__(self):
        return f'{self.user.username} PropertyDevelopmentImage'


class CleaningImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    cleaning1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 1))
    cleaning2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 2))
    cleaning3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 3))
    cleaning4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 4))
    cleaning5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 5))

    def __self__(self):
        return f'{self.user.username} CleaningImage'


class LandscapingImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    landscaping1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 1))
    landscaping2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 2))
    landscaping3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 3))
    landscaping4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 4))
    landscaping5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 5))

    def __self__(self):
        return f'{self.user.username} LandscapingImage'


class SuppliesImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    supplies1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 1))
    supplies2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 2))
    supplies3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 3))
    supplies4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 4))
    supplies5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 5))

    def __self__(self):
        return f'{self.user.username} SuppliesImage'


class AccountingImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    accounting1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 1))
    accounting2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 2))
    accounting3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 3))
    accounting4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 4))
    accounting5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 5))


    def __self__(self):
        # file_change = rename.rename_file('accounting_images')
        return f'{self.user.username} AccountingImage'


class PayrollImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    payroll1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 1))
    payroll2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 2))
    payroll3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 3))
    payroll4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 4))
    payroll5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 5))

    def __self__(self):
        return f'{self.user.username} PayrollImage'


class TaxImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    tax1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 1))
    tax2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 2))
    tax3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 3))
    tax4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 4))
    tax5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 5))

    def __self__(self):
        return f'{self.user.username} TaxImage'