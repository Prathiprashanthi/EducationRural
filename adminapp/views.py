from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import logout
import os
from userapp.models import *
from adminapp.models import *
from django.utils.datastructures import MultiValueDictKeyError
import random
import urllib.request
import urllib.parse
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings



EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
def generate_otp(length=4):
    otp = ''.join(random.choices('0123456789', k=length))
    return otp

def sendSMS(user, otp, mobile):
    data = urllib.parse.urlencode({
        'username': 'Codebook',
        'apikey': '56dbbdc9cea86b276f6c',
        'mobile': mobile,
        'message': f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.codebook.in server. Thank you',
        'senderid': 'CODEBK'
    })
    data = data.encode('utf-8')
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data)
    return f.read()
# Create your views here.

def ins_logout(request):
    logout(request)
    messages.info(request,"Logout Successfully ")
    return redirect('instructor_login')




def ins_dashboard(request):
    total_courses = Addcourse.objects.count()
    total_questions = Question.objects.count()
    total_students = StudentRegModel.objects.count()
 
    return render(request, 'admin/index.html', {
        'total_students': total_students,
        'total_courses': total_courses,
        'total_questions': total_questions,
    })



def add_courses(request):
    if request.method == 'POST':
        course_name = request.POST.get('courseName')
        course_image = request.FILES.get('courseImage')
        course_category = request.POST.get('courseCategory')
        course_language = request.POST.get('courseLanguage')
        video_url = request.POST.get('videourl')
        duration_weeks = request.POST.get('courseDuration')
        course = Addcourse.objects.create(
            course_name=course_name,
            course_image=course_image,
            course_category=course_category,
            course_language=course_language,
            video_url=video_url,
            duration_weeks=duration_weeks,
        )
        messages.success(request,"Course Added Successfully")
        return redirect('add_courses')
    return render(request, "admin/add-courses.html")


def add_scholarship(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        eligibility = request.POST.get('eligibility')
        deadline = request.POST.get('deadline')
        link = request.POST.get('link')
        description = request.POST.get('description')
        
        # Save the form data to the database
        application = ScholarshipApplication.objects.create(
            title=title,
            eligibility=eligibility,
            deadline=deadline,
            link=link,
            description=description,
        )
        messages.success(request, "Loan Application done Successfully")
        return redirect('add_scholarship')
    return render(request, "admin/add-scholarships.html")

def view_courses(request):
    courses = Addcourse.objects.all()
    paginator = Paginator(courses, 5)  # Show 5 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, "admin/view-courses.html", context)



# admin/views.py

def add_question(request):
    if request.method == 'POST':
        class_name = request.POST.get('courseSelect')
        question_text = request.POST.get('questionText')
        subject = request.POST.get('questionType')
        option_a = request.POST.get('optionA')
        option_b = request.POST.get('optionB')
        option_c = request.POST.get('optionC')
        option_d = request.POST.get('optionD')
        correct_answer = request.POST.get('correctAnswer')

        # Create and save the question instance
        question = Question.objects.create(
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_answer=correct_answer,
            subject=subject,
            class_name=class_name,
           
        )
        
        # Add a success message
        messages.success(request, "Question Added Successfully")
        
        # Redirect to all_questions view
        return redirect('all_questions')  # Ensure this name matches your URL pattern name
    
    return render(request, "admin/add-questions.html")

def all_questions(request):
    question_list = Question.objects.all()
    paginator = Paginator(question_list,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/all-questions.html", {'page_obj': page_obj})


def remove_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    messages.info(request,"Deleted Successfully !")
    return redirect('all_questions') 



def view_students(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        eligibility = request.POST.get('eligibility')
        deadline = request.POST.get('deadline')
        link = request.POST.get('link')
        description = request.POST.get('description')
        
        # Save the form data to the database
        application = LoanApplication.objects.create(
            title=title,
            eligibility=eligibility,
            deadline=deadline,
            link=link,
            description=description,
        )
        messages.success(request, "Loan Application done Successfully")
        return redirect('view_students')  # Redirect to the same page after form submission
    return render(request, "admin/view-students.html")


def view_student_feedbacks(request):
    feed = StudentFeedback.objects.all()
    return render(request, "admin/view-feedbacks.html", {"back": feed})

def view_student_sentiment(request):
    fee = StudentFeedback.objects.all()
    return render(request, "admin/view-sentiment.html", {"cat": fee})

def feedbacks_graph(request):
    feedbacks = StudentFeedback.objects.all()
    rating_counts = {
        'rating1': feedbacks.filter(rating=1).count(),
        'rating2': feedbacks.filter(rating=2).count(),
        'rating3': feedbacks.filter(rating=3).count(),
        'rating4': feedbacks.filter(rating=4).count(),
        'rating5': feedbacks.filter(rating=5).count(),
    }
    return render(request, "admin/feedback-graph.html", {'rating_counts': rating_counts})





def edit_course(request, course_id):
    course_details = Addcourse.objects.get(pk=course_id)
    if request.method == 'POST':
        course_details.course_name = request.POST.get('courseName') if request.POST.get('courseName') else course_details.course_name
        course_details.course_image = request.FILES['courseImage'] if 'courseImage' in request.FILES else course_details.course_image
        course_details.course_category = request.POST.get('courseCategory') if request.POST.get('courseCategory') else course_details.course_category
        course_details.course_language = request.POST.get('courseLanguage') if request.POST.get('courseLanguage') else course_details.course_language
        course_details.video_url = request.POST.get('videourl') if request.POST.get('videourl') else course_details.video_url
        course_details.duration_weeks = request.POST.get('courseDuration') if request.POST.get('courseDuration') else course_details.duration_weeks
        course_details.save()
        messages.success(request,"Updated successfully !")
        return redirect('view_courses')
    return render(request, "admin/edit-courses.html", {'course_details': course_details})




def remove_course(request, course_id):
    course = get_object_or_404(Addcourse, pk=course_id)
    course.delete()
    messages.error(request,"Deleted Successfully !")
    return redirect('view_courses')






def rating_view(request, rating, feedback_id):
    try:
        feedback = StudentFeedback.objects.get(pk=feedback_id)
        user = feedback.student
        if rating == 1 or rating == 2:
            subject = 'Improvement Feedback'
            message = 'Hello,\n\nThank you for your feedback. We have taken note of your suggestions and will work towards improving our services. Your input is valuable to us.'
        elif rating == 3:
            subject = 'Appreciation for Feedback'
            message = 'Hello,\n\nThank you for your feedback. We appreciate your suggestions and will strive to make improvements based on your input.'
        elif rating == 4 or rating == 5:
            subject = 'Appreciation for Feedback'
            message = 'Hello,\n\nThank you for your feedback. We are delighted to hear about your positive experience. Your satisfaction is our priority.'
        else:
            messages.error(request, 'Invalid rating provided.')
            return redirect('admin_view_feedbacks')
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(request, 'Email sent successfully!')
    except StudentFeedback.DoesNotExist:
        messages.error(request, 'Feedback does not exist.')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return redirect('view_student_feedbacks')




def remove_feedback_ins(request, feedback_id):
    feedback = get_object_or_404(StudentFeedback, pk=feedback_id)
    feedback.delete()
    messages.info(request,"Feedback deleted Successfully ")
    return redirect('view_student_feedbacks') 
