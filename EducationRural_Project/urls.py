"""
URL configuration for EducationRural_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from userapp import views as userviews
from adminapp import views as adminviews


urlpatterns = [
    #user
    path('admin/', admin.site.urls),
    path('',userviews.index,name="index"),
    path('index/about/',userviews.about,name="about"),
    path('index/student-login/',userviews.student_login,name="student_login"),
    path('index/student-register/',userviews.student_register,name="student_register"),
   
    path('index/contact/',userviews.contact,name="contact"),
    path('index/otp/',userviews.otp,name="otp"),
    path('instructor/ins-otp/',userviews.ins_otp,name="instructorotp"),
    path('student/dashboard/',userviews.student_dashboard,name="student_dashboard"),
    path('student/courses/',userviews.student_courses,name="student_courses"),
    path('student/my-courses/',userviews.my_courses,name="my_courses"),
    path('student/test-result/',userviews.test_result,name="test_result"),
   
    path('student/view-deatils/',userviews.view_details,name="view_details"),
    path('student/profile/',userviews.student_profile,name="student_profile"),
    path('student/feedback/',userviews.student_feedback,name="student_feedback"),
    path('student/logout/',userviews.student_logout,name="student_logout"),
    path('student/schloarship/',userviews.schloarship,name="schloarship"),
    path('student/razorpay-paymet/', userviews.loans, name="loans"),
    #path('paymenthandler/', userviews.paymenthandler, name='paymenthandler'),
    path('submit-test/<int:course_id>/', userviews.submit_test, name='submit_test'),  
    path('index/instructor-login/',userviews.instructor_login,name="instructor_login"),
    path('index/instructor-register/',userviews.instructor_register,name="instructor_register"),

    #Admin
    path('instructor/dashboard/',adminviews.ins_dashboard,name="ins_dashboard"),
    path('instructor/add-courses/',adminviews.add_courses,name="add_courses"),
    path('instructor/view-courses/',adminviews.view_courses,name="view_courses"),
    path('instructor/add-question/',adminviews.add_question,name="add_question"),
    path('instructor/add-scholarship/',adminviews.add_scholarship,name="add_scholarship"),
    path('instructor/all-question/',adminviews.all_questions,name="all_questions"),
    path('instructor/view-students/',adminviews.view_students,name="view_students"),
    path('instructor/view-students-feedbacks/',adminviews.view_student_feedbacks,name="view_student_feedbacks"),
    path('instructor/view-students-sentiment/',adminviews.view_student_sentiment,name="view_student_sentiment"),
    path('instructor/view-students-feedbacks-graph/',adminviews.feedbacks_graph,name="ins_feedbacks_graph"),
    path('instructor/logout/',adminviews.ins_logout,name="ins_logout"),
    path('instructor/edit-courses/<int:course_id>/',adminviews.edit_course,name="edit_course"),


    path('remove-course/<int:course_id>/', adminviews.remove_course, name='remove_course'),
    path('remove-question/<int:question_id>/', adminviews.remove_question, name='remove_question'),

    path('instructor-mail-reply/rating/<int:rating>/<int:feedback_id>/', adminviews.rating_view, name='ins_rating_view'),
    path('remove-feedback/<int:feedback_id>/', adminviews.remove_feedback_ins, name='remove_feedback_ins'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
