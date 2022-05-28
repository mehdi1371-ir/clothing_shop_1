from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title

class OurTeam(models.Model):
    about = models.ForeignKey(AboutUs, related_name='team', on_delete=models.CASCADE)
    members_name = models.CharField(max_length=100)
    members_position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')

    class Meta:
        verbose_name_plural = 'Our Team'

    def __str__(self):
        return self.members_name

class OurService(models.Model):
    about = models.ForeignKey(AboutUs, related_name='service', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service/')

    class Meta:
        verbose_name_plural = 'Our services'

    def __str__(self):
        return self.title
    