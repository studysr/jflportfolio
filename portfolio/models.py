from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    send_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name





type_choice=[
('webapp','webapp'),
('website','website'),
('card','card'),
]


class Portfolio(models.Model):
	title = models.CharField(max_length=255)
	p_type = models.CharField(max_length=50,choices=type_choice,default='webapp')
	body = models.TextField()
	image = models.ImageField(upload_to='images/')


	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:30]



#for image upload:

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)