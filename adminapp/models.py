from django.db import models

# Create your models here.
class InstructorRegModel(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=100,help_text="Enter Email")
    phone_number = models.BigIntegerField(null=True)
    gender =models.CharField(max_length=50,default=False)
    # experience = models.CharField(max_length=100)
    # category = models.CharField(help_text='Select Category',max_length=50,default='category')   
    password = models.CharField(max_length=100,help_text="Enter Password")
    photo = models.ImageField(default=False)
    status = models.CharField(default='Pending',max_length=100, null=True)
    reg_date = models.DateField(auto_now_add=True, null=True)
    address = models.CharField(max_length=255)
    otp = models.CharField(max_length=6,default=0) 
    otp_status = models.CharField(max_length=15, default='Not Verified')
    

    class Meta:
        db_table = 'Instructor_Details'




class Addcourse(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    course_image = models.ImageField(upload_to='course_images/')
    course_category = models.CharField(max_length=100)
    course_language = models.CharField(max_length=100)
    video_url = models.URLField()
    duration_weeks = models.IntegerField()
    added_date = models.DateField(auto_now_add=True, null=True)



    class Meta:
        db_table = 'Courses_details'





class Question(models.Model):
    SUBJECT_CHOICES = [
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('Physical Education', 'Physical Education'),
        ('Art', 'Art'),
        ('Music', 'Music'),
        ('Computer Science', 'Computer Science'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Physics', 'Physics'),
        ('Economics', 'Economics'),
        ('Sociology', 'Sociology'),
        ('Psychology', 'Psychology'),
        ('Foreign Languages', 'Foreign Languages'),
    ]
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    question_text = models.TextField()
    class_name = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    #course = models.ForeignKey(Addcourse, on_delete=models.CASCADE)

    class Meta:
        db_table = 'questions'
        
class ScholarshipApplication(models.Model):
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=10)
    deadline = models.DateField()
    link = models.URLField()  # Assuming you want a URL field for the "Link" input
    description = models.TextField()
    
    class Meta:
        db_table = 'scholarship'
        
class LoanApplication(models.Model):
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=10)
    deadline = models.DateField()
    link = models.URLField()  # Assuming you want a URL field for the "Link" input
    description = models.TextField()

    class Meta:
        db_table = 'loan'