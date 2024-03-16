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
    logo_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('logo_images', 'logo_image', 1))
    logo_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('logo_images', 'logo_image', 2))

    def __self__(self):
        return f'{self.user.username} Logo'


class HomeImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(default='default.jpg', upload_to=rename.rename_file('home_images', 'home_image', 1))
    contentImage1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('home_images', 'home_image', 2))
    contactUsImage = models.ImageField(default='default.jpg', upload_to=rename.rename_file('home_images', 'home_image', 3))

    def __self__(self):
        return f'{self.user.username} HomeImages'

class PropertyDevelopmentImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'welcome_image', 0))
    propertyDevelopment_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 1))
    propertyDevelopment_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 2))
    propertyDevelopment_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 3))
    propertyDevelopment_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 4))
    propertyDevelopment_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('property_development_images', 'property_development_image', 5))

    def __self__(self):
        return f'{self.user.username} PropertyDevelopmentImage'


class CleaningImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'welcome_image', 0))
    cleaning_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 1))
    cleaning_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 2))
    cleaning_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 3))
    cleaning_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 4))
    cleaning_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('cleaning_images', 'cleaning_image', 5))

    def __self__(self):
        return f'{self.user.username} CleaningImage'


class LandscapingImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'welcome_image', 0))
    landscaping_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 1))
    landscaping_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 2))
    landscaping_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 3))
    landscaping_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 4))
    landscaping_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('landscaping_images', 'landscaping_image', 5))

    def __self__(self):
        return f'{self.user.username} LandscapingImage'


class SuppliesImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    WelcomeImage = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','welcome_image', 0))
    supplies_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 1))
    supplies_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 2))
    supplies_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 3))
    supplies_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 4))
    supplies_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('supplies_images','supplies_image', 5))

    def __self__(self):
        return f'{self.user.username} SuppliesImage'


class AccountingImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    welcomeImage = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'welcome_image', 0))
    accounting_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 1))
    accounting_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 2))
    accounting_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 3))
    accounting_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 4))
    accounting_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('accounting_images', 'accounting_pic', 5))


    def __self__(self):
        # file_change = rename.rename_file('accounting_images')
        return f'{self.user.username} AccountingImage'


class PayrollImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    payroll_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 1))
    payroll_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 2))
    payroll_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 3))
    payroll_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 4))
    payroll_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('payroll_images','payroll_image', 5))

    def __self__(self):
        return f'{self.user.username} PayrollImage'


class TaxImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    tax_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 1))
    tax_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 2))
    tax_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 3))
    tax_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 4))
    tax_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('tax_images','tax_image', 5))

    def __self__(self):
        return f'{self.user.username} TaxImage'
    

class BusinessConsultingImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    businessConsulting_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('business_consulting_images','business_consulting_image', 1))
    businessConsulting_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('business_consulting_images','business_consulting_image', 2))
    businessConsulting_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('business_consulting_images','business_consulting_image', 3))
    businessConsulting_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('business_consulting_images','business_consulting_image', 4))
    businessConsulting_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('business_consulting_images','business_consulting_image', 5))

    def __self__(self):
        return f'{self.user.username} BusinessConsultingImage'


class ManufacturingImage(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    Welcome_Image = models.ImageField(default='default.jpg', upload_to=rename.rename_file('manufacturing_images','welcome_image', 0))
    manufacturing_1 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('manufacturing_images','manufacturing_image', 1))
    manufacturing_2 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('manufacturing_images','manufacturing_image', 2))
    manufacturing_3 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('manufacturing_images','manufacturing_image', 3))
    manufacturing_4 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('manufacturing_images','manufacturing_image', 4))
    manufacturing_5 = models.ImageField(default='default.jpg', upload_to=rename.rename_file('manufacturing_images','manufacturing_image', 5))

    def __self__(self):
        return f'{self.user.username} ManufacturingImage'