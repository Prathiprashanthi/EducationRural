from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
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
from EducationRural_Project.eduenv.RazorPayApi import RazorpayClient



from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest,HttpResponse
from django.db.models import Count
from django.core.paginator import Paginator
from random import sample

from django.utils.text import slugify
from django.utils import timezone
from nltk.sentiment.vader import SentimentIntensityAnalyzer
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


def generate_otp(length=4):
    otp = ''.join(random.choices('0123456789', k=length))
    return otp


def sendSMS(user,otp,mobile):
    data =  urllib.parse.urlencode({'username':'Codebook','apikey': '56dbbdc9cea86b276f6c' , 'mobile': mobile,
        'message' : f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.codebook.in server. Thank you', 'senderid': 'CODEBK'})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data)
    return f.read()




def student_logout(request):
    logout(request)
    messages.info(request,"Logout Successfully ")
    return redirect('student_login')

# Create your views here.

def index(requrest):
    return render(requrest,"user/index.html")



def about(request):
    return render(request,"user/about.html")


def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            student = StudentRegModel.objects.get(email=email)   
            if student.password == password:
                if student.otp_status == 'Verified':
                    messages.success(request, 'Login successful!')
                    request.session['student_id_after_login'] = student.student_id
                    return redirect('student_dashboard')
                else:
                    otp = generate_otp()
                    student.otp = otp
                    student.save()
                    subject = 'OTP Verification for Account Activation'
                    otp = f'Your OTP for verification is: {student.otp}'
                    message = f'Hello {student.full_name},\n\nYou are attempting to log in to your query account. Your OTP for login verification is: {otp}\n\nIf you did not request this OTP, please ignore this email.'
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [student.email]
                    resp =  sendSMS(student.full_name, student.otp, student.phone_number)
                    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                    messages.success(request, 'Otp sent to mail and phone number !')
                    return redirect('otp')
            else:
                messages.error(request, 'Incorrect Password')
                return redirect('student_login')
        except StudentRegModel.DoesNotExist:
            messages.error(request, 'No User Found')
            return redirect('student_register')
    return render(request,"user/student-login.html")


def instructor_login(request):
    admin_name = 'admin'
    admin_pwd = 'admin'
    if request.method == 'POST':
        admin_n = request.POST.get('username')
        admin_p = request.POST.get('password')
        if (admin_n == admin_name and admin_p == admin_pwd):
            messages.success(request, 'You are logged in..')
            return redirect('ins_dashboard')
        else:
            messages.error(request, 'You are trying to loging with wrong details..')
            return redirect('instructor_login')
    return render(request, "user/instructor-login.html")




def student_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        location = request.POST.get('address')
        profile = request.FILES.get('profile')
        class_selected = request.POST.get('class')
        
        try:
            StudentRegModel.objects.get(email=email)
            messages.info(request, 'Email Already Exists!')
            return redirect('student_register')
        except StudentRegModel.DoesNotExist:
            otp = generate_otp()
            user = StudentRegModel.objects.create(full_name=name, email=email, phone_number=phone, photo=profile, password=password, address=location, otp=otp,class_selected=class_selected )
            print(user)
            resp = sendSMS(user.full_name, user.otp, user.phone_number)
            subject = 'OTP Verification for Account Activation'
            otp_message = f'Your OTP for verification is: {user.otp}'
            message = f'Hello {user.full_name},\n\nYou are attempting to Register an Account. {otp_message}\n\nIf you did not request this OTP, please ignore this message.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            request.session['student_id'] = user.student_id
            print(request.session['student_id'])
            messages.info(request, 'OTP Sent To Email and Phone!')
            return redirect('otp')
    return render(request, "user/student-register.html")


def instructor_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        location = request.POST.get('address')
        profile = request.FILES.get('profile')
        gender = request.POST.get('gender')
        try:
            InstructorRegModel.objects.get(email=email)
            messages.info(request, 'Email Already Exists!')
            return redirect('instructor_login')
        except InstructorRegModel.DoesNotExist:
            otp = generate_otp()
            ins = InstructorRegModel.objects.create(full_name=name, email=email, phone_number=phone, photo=profile, password=password, address=location, otp=otp)
            print(ins)
            resp = sendSMS(ins.full_name, ins.otp, ins.phone_number)
            subject = 'OTP Verification for Account Activation'
            otp_message = f'Your OTP for verification is: {ins.otp}'
            message = f'Hello {ins.full_name},\n\nYou are attempting to Register an Account. {otp_message}\n\nIf you did not request this OTP, please ignore this message.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [ins.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            request.session['ins_id'] = ins.instructor_id
            messages.info(request, 'OTP Sent To Email and Phone!')
            return redirect('instructorotp')
    return render(request,"user/instructor-register.html")








def contact(request):
    return render(request,"user/contact.html")




def ins_otp(request):
    ins_id = request.session.get('ins_id')
    if request.method == "POST":
        otp_entered = request.POST.get('ins_otp')
        if not otp_entered:
            messages.error(request, 'Please enter the OTP')
            print("OTP not entered")
            return redirect('instructorotp')
        try:
            instructor = InstructorRegModel.objects.get(pk=ins_id)
            if str(instructor.otp) == otp_entered:
                instructor.otp_status = 'Verified'
                instructor.save()
                # user_id = request.session['user_id']
                messages.success(request, 'OTP verification successful!')
                return redirect('instructor_login')
            else:
                messages.error(request, 'Invalid OTP entered')
                print("Invalid OTP entered")
                return redirect('instructorotp')
        except instructor.DoesNotExist:
            messages.error(request, 'Invalid Instructor')
            print("Invalid Instructor")
            return redirect('instructor_register')
    return render(request,"user/ins-otp.html")




def otp(request):
    student_id = request.session.get('student_id')
    student = StudentRegModel.objects.get(student_id=student_id)
    if request.method == "POST":
        otp_entered = request.POST.get('otp')
        print(otp_entered,"otp enterd")
        print(student)
        if not otp_entered:
            messages.error(request, 'Please enter the OTP')
            print("OTP not entered")
            return redirect('otp')
        try:
            student = StudentRegModel.objects.get(student_id=student_id)
            if str(student.otp) == otp_entered:
                student.otp_status = 'Verified'
                student.save()
                # user_id = request.session['user_id']
                messages.success(request, 'OTP verification successful!')
                return redirect('student_login')
            else:
                messages.error(request, 'Invalid OTP entered')
                print("Invalid OTP entered")
                return redirect('otp')
        except student.DoesNotExist:
            messages.error(request, 'Invalid Student')
            print("Invalid Student")
            return redirect('student_register')
    return render(request,"user/otp.html")


def student_dashboard(request):
    # Get counts of various objects
    course_count = Addcourse.objects.count()
    question_count = Question.objects.count()
    scholarship_count = ScholarshipApplication.objects.count()
    loan_count = LoanApplication.objects.count()

    # Fetch all questions (or filtered based on your criteria)
    questions = Question.objects.all()
    
    # Assuming you want to use the first question's class_name and subject
    if questions.exists():
        class_name = questions.first().class_name
        subject = questions.first().subject
    else:
        class_name = None
        subject = None

    # Set session variables for class_name and subject
    request.session['class_name'] = class_name
    request.session['subject'] = subject

    

    # Fetch all courses
    courses = Addcourse.objects.all()

    # Initialize a list to store course details
    courses_list = []

    # Loop through each course and extract details
    for course in courses:
        course_details = {
            'course_name': course.course_name,
            'course_image': course.course_image.url if course.course_image else None,
            'course_category': course.course_category,
            'course_language': course.course_language,
            'video_url': course.video_url,
            'duration_weeks': course.duration_weeks,
            'added_date': course.added_date.strftime('%Y-%m-%d') if course.added_date else None,
        }
        courses_list.append(course_details)

    # Set session variable for course details
    request.session['courses'] = courses_list

    # Debugging: Print the session data to console
    for course in courses_list:
        print(f"Course Name: {course['course_name']}")
        print(f"Course Image URL: {course['course_image']}")
        print(f"Course Category: {course['course_category']}")
        print(f"Course Language: {course['course_language']}")
        print(f"Video URL: {course['video_url']}")
        print(f"Duration Weeks: {course['duration_weeks']}")
        print(f"Added Date: {course['added_date']}")
        print("-" * 30)

        # Fetch Scholarship details
    scholarship = ScholarshipApplication.objects.first()
    if scholarship:
        request.session['scholarship_title'] = scholarship.title
        request.session['scholarship_eligibility'] = scholarship.eligibility
        request.session['scholarship_deadline'] = scholarship.deadline.strftime('%Y-%m-%d')
        request.session['scholarship_link'] = scholarship.link
        request.session['scholarship_description'] = scholarship.description
    else:
        request.session['scholarship_title'] = None
        request.session['scholarship_eligibility'] = None
        request.session['scholarship_deadline'] = None
        request.session['scholarship_link'] = None
        request.session['scholarship_description'] = None
    # Print session variables for verification
    print("Scholarship Session Variables:")
    print(f"Title: {request.session['scholarship_title']}")
    print(f"Eligibility: {request.session['scholarship_eligibility']}")
    print(f"Deadline: {request.session['scholarship_deadline']}")
    print(f"Link: {request.session['scholarship_link']}")
    print(f"Description: {request.session['scholarship_description']}")
    # Fetch Loan details
    loan = LoanApplication.objects.first()  # Assuming you want the first loan application, adjust query as needed
    if loan:
        request.session['loan_title'] = loan.title
        request.session['loan_eligibility'] = loan.eligibility
        request.session['loan_deadline'] = loan.deadline.strftime('%Y-%m-%d') if loan.deadline else None
        request.session['loan_link'] = loan.link
        request.session['loan_description'] = loan.description
    else:
        # If no loan application exists, set session variables to None
        request.session['loan_title'] = None
        request.session['loan_eligibility'] = None
        request.session['loan_deadline'] = None
        request.session['loan_link'] = None
        request.session['loan_description'] = None

    # Optional: Debug print statements to verify session data
    print("\nLoan Session Variables:")
    print(f"Title: {request.session['loan_title']}")
    print(f"Eligibility: {request.session['loan_eligibility']}")
    print(f"Deadline: {request.session['loan_deadline']}")
    print(f"Link: {request.session['loan_link']}")
    print(f"Description: {request.session['loan_description']}")

    # Render the template with the counts
    return render(request, "user/student-dashboard.html", {
        'a': course_count,
        'b': question_count,
        'c': scholarship_count,
        'd': loan_count,
    })








def student_courses(request):
    # Retrieve class_name and subject from session
    class_name = request.session.get('class_name', 'default_class_value')
    subject = request.session.get('subject', 'default_subject_value')
    
    # Filter questions based on class_name and subject
    questions = Question.objects.filter(class_name=class_name, subject=subject)
    
    # Retrieve all courses and students (not directly used in processing)
    courses = Addcourse.objects.all()
    students = StudentRegModel.objects.all()
    
    if request.method == 'POST':
        results = []
        total_marks = 0
        for question in questions:
            answer_key = f'question_{question.id}_answer'
            if answer_key in request.POST:
                selected_answer = request.POST[answer_key].strip()
                correct_answer = question.correct_answer.strip()
                
                if selected_answer == correct_answer:
                    total_marks += 1
                    results.append({
                        'question_id': question.id,
                        'question_text': question.question_text,
                        'selected_answer': selected_answer,
                        'correct_answer': correct_answer,
                        'is_correct': True,
                    })
                    messages.success(request, f'Question {question.id}: Correct!')
                else:
                    results.append({
                        'question_id': question.id,
                        'question_text': question.question_text,
                        'selected_answer': selected_answer,
                        'correct_answer': correct_answer,
                        'is_correct': False,
                    })
                    messages.error(request, f'Question {question.id}: Wrong. The correct answer is {correct_answer}.')
            else:
                # Handle case where a question has not been answered
                messages.error(request, f'Question {question.id}: Please select an answer.')
                return redirect('student_courses')  # Redirect back to the test if not all questions are answered
        
        # Store the results in the session
        request.session['results'] = results
        request.session['total_marks'] = total_marks

        # Redirect to the view_details page after processing
        return redirect('view_details')

    # Context for rendering the template on GET request
    context = {
        'questions': questions,
        'selected_subject': subject,
        'students': students,
        
    }
    
    return render(request, "user/test.html", context)




def view_details(request):
    # Assuming the results and total marks are stored in the session
    results = request.session.get('results', [])
    total_marks = request.session.get('total_marks', 0)
    
    # Calculate correct and wrong answers
    correct_answers = sum(1 for result in results if result.get('is_correct'))
    wrong_answers = sum(1 for result in results if not result.get('is_correct'))
    
    # Total marks available
    total_marks_available = len(results)  # Adjust based on actual total marks logic
    
    # Calculate percentage
    percentage = (total_marks / total_marks_available) * 100 if total_marks_available else 0

    context = {
        'results_details': results,
        'correct_Answers': correct_answers,
        'wrong_Answers': wrong_answers,
        'total_marks_final': total_marks,
        'percentage': percentage,
    }

    return render(request, "user/test-result.html", context)



def schloarship(request):
    # Retrieve the list of courses from session
    courses_list = request.session.get('courses', [])

    # Prepare context for rendering
    context = {
        'courses': courses_list,
    }

    # Debug: Print the context to the console
    print(context)
    
    return render(request, 'user/scholarship.html', context)
def loans(request):
    # Fetching all loan applications and scholarships (adjust as needed)
    loans = LoanApplication.objects.all()
    scholarships = ScholarshipApplication.objects.all()

    # Prepare context dictionaries
    loan_context = []
    for loan in loans:
        loan_context.append({
            'loan_title': loan.title,
            'loan_eligibility': loan.eligibility,
            'loan_deadline': loan.deadline.strftime('%Y-%m-%d') if loan.deadline else None,
            'loan_description': loan.description,
            'loan_link': loan.link,
        })

    scholarship_context = []
    for scholarship in scholarships:
        scholarship_context.append({
            'scholarship_title': scholarship.title,
            'scholarship_eligibility': scholarship.eligibility,
            'scholarship_deadline': scholarship.deadline.strftime('%Y-%m-%d') if scholarship.deadline else None,
            'scholarship_description': scholarship.description,
            'scholarship_link': scholarship.link,
        })
    return render(request, 'user/loanspage.html', {
        'scholarship_context': scholarship_context,
        'loan_context': loan_context,
    })

def test_result(request):
    student_id = request.session.get('student_id_after_login')
    if student_id is not None:
        student_tests = UserTestModel.objects.filter(test_user_id=student_id).order_by('-id')
        paginator = Paginator(student_tests, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "user/test-result.html", {'page_obj': page_obj})
    else:
        messages.error(request, "Student not logged in or session data missing")
        return redirect("student_login")




def my_courses(request):
    student_id = request.session.get('student_id_after_login')
    if student_id is None:
        messages.warning(request,"No student found , please login again !")
        return redirect('student_login')
    student_courses = StudentCourses.objects.filter(student_id=student_id)
    student_courses_with_question_count = student_courses.annotate(
        question_count=Count('course__question')
    )
    context = {
        'student_courses': student_courses_with_question_count
    }
    return render(request, "user/my-courses.html", context)









def submit_test(request, course_id):
    if request.method == 'POST':
        answers = {}
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                answers[question_id] = value
        try:
            course = Addcourse.objects.get(pk=course_id)
        except Addcourse.DoesNotExist:
            messages.error(request, "Course not found.")
            return redirect('test')
        user_id = request.session.get('student_id_after_login')
        if not user_id:
            messages.error(request, "User not logged in.")
            return redirect('student_login') 
        course_name = course.course_name
        unique_identifier = slugify(course_name) 
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        user_test = UserTestModel.objects.create(
            test_user_id=user_id,
            test_name=f"Test for {course_name} ({unique_identifier}) - {timestamp}",
            test_marks=0
        )
        for question_id, answer in answers.items():
            try:
                question = Question.objects.get(pk=question_id)
            except Question.DoesNotExist:
                messages.error(request, "Question not found.")
                return redirect('test')  
            marks = 1 if answer == question.correct_answer else 0
            ResultModel.objects.create(
                user_id=user_id,
                test_id=user_test.id,
                test_name=user_test.test_name,
                question=question.question_text,
                useranswer=answer,
                correctanswer=question.correct_answer,
                marks=marks
            )
            user_test.test_marks += marks
        user_test.save()
        messages.success(request, "Test submitted successfully.")
        return redirect('test_result')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('test')


def student_profile(request):
    student_id  = request.session['student_id_after_login']
    print(student_id)
    student = StudentRegModel.objects.get(student_id= student_id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        try:
            profile = request.FILES['profile']
            student.photo = profile
        except MultiValueDictKeyError:
            profile = student.photo
        password = request.POST.get('password')
        location = request.POST.get('location')
        student.full_name = name
        student.email = email
        student.phone_number = phone
        student.password = password
        student.address = location
        student.save()
        messages.success(request , 'updated succesfully!')
        return redirect('student_profile')
    return render(request,"user/student-profile.html",{'student':student})










def student_feedback(request):
    if request.method == 'POST':
        selected_course_name = request.POST.get('course_name')
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        rating = int(request.POST.get('rating'))
        additional_comments = request.POST.get('additional_comments')
        
        student_id = request.session.get('student_id_after_login')
        
        # Perform sentiment analysis
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(additional_comments)
        
        # Determine sentiment based on compound score
        if score['compound'] > 0.5:
            sentiment = 'very positive'
        elif score['compound'] > 0:
            sentiment = 'positive'
        elif score['compound'] < -0.5:
            sentiment = 'very negative'
        elif score['compound'] < 0:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        if selected_course_name and user_name and user_email and student_id is not None:
            # Create StudentFeedback object
            feedback = StudentFeedback.objects.create(
                student_id=student_id,
                course_name=selected_course_name,
                user_name=user_name,
                user_email=user_email,
                rating=rating,
                additional_comments=additional_comments,
                sentiment=sentiment  # Assign sentiment to the field
            )
            messages.success(request, 'Feedback submitted successfully.')
            return redirect('student_feedback')
        else:
            messages.error(request, 'Incomplete data. Please fill in all required fields.')
    
    # Fetch student's enrolled courses
    student_id = request.session.get('student_id_after_login')
    if student_id:
        student_courses = StudentCourses.objects.filter(student_id=student_id).values_list('course__course_name', flat=True)
        context = {'student_courses': student_courses}
        return render(request, "user/student-feedback.html", context)
    else:
        messages.error(request, 'You need to be logged in to access this page.')
        return redirect('login')


@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            api = RazorpayClient()
            result = api.client.utility.verify_payment_signature(params_dict)
            if result:
                student_id = request.session.get('student_id_after_login')
                if student_id is None:
                    return HttpResponseBadRequest('Student ID not found in session')

                print(student_id, "Student ID")
                try:
                    user = StudentRegModel.objects.get(pk=student_id)
                except StudentRegModel.DoesNotExist:
                    return HttpResponseBadRequest('Student not found')

                cart = get_object_or_404(CartModel, cart_user=user)
                fee = cart.cart_booking.price
                amount = fee * 100  # Convert to paisa
                try:
                    api.client.payment.capture(payment_id, amount)
                    cart = get_object_or_404(CartModel, cart_user=user)
                    StudentCourses.objects.create(
                        student=user,
                        course=cart.cart_booking,
                        amount=fee,
                        payment_status="Successful",
                        payment_id=payment_id,
                        order_id=razorpay_order_id
                    )
                    messages.success(request, 'Payment successfully completed')
                    return redirect('my_courses')
                except Exception as e:
                    messages.error(request, 'Payment Failed: ' + str(e))
                    return redirect('student_courses')
            else:
                messages.error(request, 'Signature verification failed')
                return redirect('student_courses')
        except Exception as e:
            print("Error:", e)
            return HttpResponseBadRequest('An error occurred during payment processing')
    else:
        return HttpResponseBadRequest('Only POST requests are allowed')