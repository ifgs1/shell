from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMultiAlternatives

from gettingstarted.settings import BASE_DIR, PROJECT_ROOT
from models import Proyecto,Design, Designer, Trayecto
from models import Usuario
import os
import time
from django.core.files.base import ContentFile

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def getProject(request,idProject):

    if request.method == 'GET':
        jsonProject = json.loads(request.body.decode('utf-8'))
        proyecto = Proyecto.objects.get(pk=idProject)
        return HttpResponse(serializers.serialize("json",proyecto))

@csrf_exempt
def getCompany(request,companyName,companyId):
    print companyName,
    return HttpResponseRedirect("http://127.0.0.1:8000/#/company/"+companyName+"/"+companyId)

@csrf_exempt
def getDesignsByProject(request,projectId):
    print projectId
    designs = Design.objects.filter(project__pk=projectId).order_by('-created_date')
    return HttpResponse(serializers.serialize("json",designs,use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def getCompanyById(request,userId):
    if request.method == 'GET':

        page = request.GET.get('page')
        user = request.user
        proyecto = Proyecto.objects.filter(usuario__pk=userId)
        paginator = Paginator(proyecto, 10) # Show 25 contacts per page
        try:
            proyectos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            proyectos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            proyectos = paginator.page(paginator.num_pages)
        data =serializers.serialize("json",proyectos.object_list)
        return HttpResponse(serializers.serialize("json",proyecto))

@csrf_exempt
def createProject(request):

    if request.method == 'POST':

     jsonProject = json.loads(request.body)
     proyecto = Proyecto()
     print str("Entro ")

     print str("pasooooo ")

     proyecto.name = jsonProject['name']
     proyecto.description = jsonProject['description']
     proyecto.image = jsonProject['image']
     proyecto.estimated_price= jsonProject['estimatedPrice']
     proyecto.usuario = request.user
     proyecto.save()
     return HttpResponse(serializers.serialize("json",{proyecto}))

    if request.method == 'GET':
        #proyecto = Proyecto.objects.all()


        page = request.GET.get('page')
        user = request.user
        proyecto = Proyecto.objects.filter(usuario=user)
        paginator = Paginator(proyecto, 10) # Show 25 contacts per page
        try:
            proyectos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            proyectos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            proyectos = paginator.page(paginator.num_pages)
        data =serializers.serialize("json",proyectos.object_list)
        return HttpResponse(serializers.serialize("json",proyecto))

        ##return JsonResponse({"proyectos":data,"numeroPaginas":paginator.num_pages})

    if request.method == 'PUT':
        jsonProject = json.loads(request.body.decode('utf-8'))

        proyecto = Proyecto.objects.get(pk=jsonProject.get('pk'))
        proyecto.name = jsonProject.get('name')
        proyecto.description = jsonProject.get('description')
        proyecto.image = jsonProject.get('image')
        proyecto.save()

        return HttpResponse(serializers.serialize("json",{proyecto}))

    if request.method == 'DELETE':
            jsonProject = json.loads(request.body.decode('utf-8'))

            proyecto = Proyecto.objects.get(pk=jsonProject.get('pk'))
            proyecto.delete()

            return HttpResponse(serializers.serialize("json",""))

@csrf_exempt
def registerManager(request):
    if request.method == 'POST':
        objs = json.loads(request.body)

        name = objs['full_name'].lower()
        password = objs['password']
        user_identifiation = objs['user_identifiation']
        birth_date = objs['birth_date']
        email = objs['email']


        userQS = User.objects.filter(username=name)
        userList = list(userQS[:1])
        if userList:
            print 'Paila ya existe el man'
            return HttpResponse(status=400)


        userModel = User.objects.create_user(username=name, password=password)
        userModel.first_name=name
        userModel.last_name=name
        userModel.email=email
        userModel.save()
        print 'Se crea el usuario'

        '''
        userQS = User.objects.filter(username=company)
        userList = list(userQS[:1])
        userObject = userList[0]
        '''
        manager = Usuario()
        manager.full_name = name
        manager.email=email
        manager.birth_date =birth_date
        manager.user_identifiation = user_identifiation
        manager.user=userModel
        manager.save()

        print 'Se crea el manager'

        return HttpResponse(serializers.serialize("json", {manager}))
@csrf_exempt
def loginUser(request):
    message = ''

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        username = jsonUser.get('username')
        password = jsonUser.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            message = 'OK'
            print 'El man se logeo'
        else:
            message = 'Usuario y/o clave invalida'
            print 'Paila el man no se logeo'

    return JsonResponse({'message':message})

@csrf_exempt
def loginUser(request):
    message = ''

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        username = jsonUser.get('username')
        password = jsonUser.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            message = 'OK'
        else:
            message = 'Usuario y/o clave invalida'

    return JsonResponse({'message':message})

@csrf_exempt
def isLoggedUser(request):
    if request.user.is_authenticated():
        logged = True
    else:
        logged = False
    return JsonResponse({'logged':logged})

@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({'logout':True})

@csrf_exempt
def createDesign(request):
    if request.method == 'POST':

        objs = json.loads(request.body)

        designer = Designer()
        designer.name = objs['designer_name']
        designer.lastname = objs['designer_last_name']
        designer.email = objs['designer_email']
        designer.save()

        design = Design()

        design.price = objs['price']
        design.status = 1

        base64_string = objs['imageFile'].encode('utf-8')
        print objs['imageFile']
        print base64_string

        filename = str(time.time())+".png"

        # decoding base string to image and saving in to your media root folder
        fh = open(os.path.join(PROJECT_ROOT+'/static/images', filename), "wb")
        fh.write(bytes(base64_string.decode('base64')))
        fh.close()

        # saving decoded image to database
        decoded_image = base64_string.decode('base64')
        design.imageFile = ContentFile(decoded_image, filename)

        projectQS = Proyecto.objects.filter(pk=int(objs['project_pk']))
        projectsList = list(projectQS[:1])
        projectObject = projectsList[0]

        design.project = projectObject
        design.designer = designer

        design.save()

    return JsonResponse({})

@csrf_exempt
def createRide(request):

    if request.method == 'POST':

     jsonProject = json.loads(request.body)
     trayecto = Trayecto()
     print str("Entro ")

     print str("pasooooo ")

     trayecto.name = jsonProject['name']
     trayecto.description = jsonProject['description']
     trayecto.latitude_origin = jsonProject['latitude_origin']
     trayecto.longitude_origin= jsonProject['longitude_origin']
     trayecto.latitude_destination= jsonProject['latitude_destination']
     trayecto.longitude_destination= jsonProject['longitude_destination']
     trayecto.date_ride= jsonProject['date_ride']
     trayecto.seats= jsonProject['seats']
     trayecto.plates= jsonProject['plates']
     trayecto.seats= jsonProject['seats']
     user = Usuario.objects.get(pk=jsonProject.get('pk'))
     trayecto.usuario = user
     trayecto.save()
     return HttpResponse(serializers.serialize("json",{trayecto}))

    if request.method == 'GET':
        trayectos = Trayecto.objects.all()
        compra_trayectos = Trayecto.objects.filter().values('plates',
                                                            'usuario__email',
                                                            'name',
                                                            'description',
                                                            'seats',
                                                            'latitude_origin',
                                                            'longitude_origin',
                                                            'latitude_destination',
                                                            'longitude_destination',
                                                            'date_ride',
                                                            'seats',
                                                            'usuario__full_name')
        compra_trayectos = json.loads(json.dumps(list(compra_trayectos)))
        return JsonResponse(compra_trayectos, safe=False)

    if request.method == 'PUT':
        jsonProject = json.loads(request.body.decode('utf-8'))

        proyecto = Proyecto.objects.get(pk=jsonProject.get('pk'))
        proyecto.name = jsonProject.get('name')
        proyecto.description = jsonProject.get('description')
        proyecto.image = jsonProject.get('image')
        proyecto.save()

        return HttpResponse(serializers.serialize("json",{proyecto}))

    if request.method == 'DELETE':
            jsonProject = json.loads(request.body.decode('utf-8'))

            proyecto = Proyecto.objects.get(pk=jsonProject.get('pk'))
            proyecto.delete()

            return HttpResponse(serializers.serialize("json",""))

'''
@csrf_exempt
def getIndependents(request):
    independents = Independent.objects.all().order_by('-user__date_joined')
    return HttpResponse(serializers.serialize("json",independents,use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def getJobs(request):
    jobs = Job.objects.all()
    return HttpResponse(serializers.serialize("json",jobs))

@csrf_exempt
def loginUser(request):
    message = ''

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        username = jsonUser.get('username')
        password = jsonUser.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            message = 'OK'
        else:
            message = 'Usuario y/o clave invalida'

    return JsonResponse({'message':message})

@csrf_exempt
def isLoggedUser(request):
    if request.user.is_authenticated():
        logged = True
    else:
        logged = False
    return JsonResponse({'logged':logged})

@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({'logout':True})

@csrf_exempt
def profile(request):
    user = request.user
    independent = Independent.objects.get(user=user)

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))

        independent.name = jsonUser.get('name')
        independent.lastName = jsonUser.get('last_name')
        independent.yearsOfExperience = jsonUser.get('experience')
        independent.phoneNumber = jsonUser.get('phone_number')
        independent.email = jsonUser.get('email')
        independent.imageFileUrl = jsonUser.get('image')

        jobQS = Job.objects.filter(jobName=str(jsonUser.get('job')).lstrip().rstrip())
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]

        independent.job = jobObject
        independent.job.save()
        independent.save()

    return HttpResponse(serializers.serialize("json",{independent},use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def registerIndependent(request):
    if request.method == 'POST':
        objs = json.loads(request.body)

        jobString = str(objs['job']).lstrip().rstrip()
        jobQS = Job.objects.filter(jobName=jobString)
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]
        username = objs['username']
        password = objs['password']
        email = objs['email']
        name = objs['name']
        lastName = objs['lastName']
        imageFileUrl = objs['imageFileUrl']
        phoneNumber = objs['phoneNumber']
        yearsOfExperience = objs['yearsOfExperience']

        userModel = User.objects.create_user(username=username, password=password)
        userModel.first_name=name
        userModel.last_name=lastName
        userModel.email=email
        userModel.save()
        print 'Se crea el usuario'

        userQS = User.objects.filter(username=username)
        userList = list(userQS[:1])
        userObject = userList[0]
        independent = Independent()
        independent.email=email
        independent.lastName=lastName
        independent.imageFileUrl=imageFileUrl
        independent.job=jobObject
        independent.name=name
        independent.phoneNumber=phoneNumber
        independent.yearsOfExperience = yearsOfExperience
        independent.user=userObject
        independent.save()
        print 'Se crea el independiente'


    return HttpResponse(status=200)

@csrf_exempt
def registerComment(request):

    if request.method == 'POST':
        objs = json.loads(request.body)
        idIndependent = objs['idIndependent']
        comment = objs['comment']
        userEmail = objs['userEmail']

        comentario = "<strong>Comentario:</strong> %s <br><br><strong>Enviado por:</strong> %s" % (comment, userEmail)

        independent = Independent.objects.get(id=idIndependent)

        emailIndependent = independent.email

        commentModel = Comment()
        commentModel.independent=independent
        commentModel.comment=comentario
        commentModel.userEmail=userEmail
        commentModel.save()

        print 'Se crea comentario para el idIndependent: '+ idIndependent

        #send_mail('Busco Ayuda - Comentario', comentario, userEmail, [emailIndependent], fail_silently=False)

        asunto = 'Busco Ayuda - Comentario'
        text_content = ''
        html_content = comentario
        from_email = userEmail
        to = emailIndependent

        mensaje = EmailMultiAlternatives(asunto, text_content, from_email, [to])
        mensaje.attach_alternative(html_content, "text/html")
        mensaje.send()

        print 'Se envia el correo electronico a: '+ emailIndependent

    return HttpResponse(status=200)


@csrf_exempt
def detail(request):
    user = request.user
    independent = Independent.objects.get(user=user)

    if request.method == 'POST':
        independentJson = json.loads(request.body)
        idIndependent = independentJson['idIndependent']

        independent = Independent.objects.filter(id=idIndependent)

        jobQS = Job.objects.filter(jobName=str(independentJson.get('job')).lstrip().rstrip())
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]

        independent.job = jobObject
        independent.job.save()
        independent.save()

    return HttpResponse(serializers.serialize("json",{independent},use_natural_foreign_keys=True, use_natural_primary_keys=True))
'''