from django.http import HttpResponse,request,Http404
from django.shortcuts import redirect
from .models import store
from django.shortcuts import render
from django.contrib import messages
import cv2
import numpy as np
import os
import base64

def home(request):
    return render(request,'index.html')

def display(request,id):
    data = store.objects.get(id=id)
    return render(request,'properties.html',{'image_data':data})

def upload(request):
    return render(request,'upload.html')

def view(request):
    images = store.objects.all()
    return render(request,'view.html',{'images':images})

def submit(request):
    if request.method == "POST" and request.FILES['image']:
        uploaded_image = request.FILES['image']
        name = uploaded_image.name
        new_entry = store(name=name,image = uploaded_image )
        new_entry.save()
        messages.success(request,"image uploaded successfully")
        return redirect('home')
    
def home(request):
    return render(request,'index.html')

def properties(request,id):
    
    try:
        data = store.objects.get(id=id)
        image = cv2.imread(data.image.path)
        rows, columns, _ = image.shape
        pixels = rows * columns
        properties_data = {'rows': rows,'columns':columns,'pixels':pixels}
        context = {
            'image_data': data,
            'properties_data': properties_data
        }
        return render(request, 'test.html', context)
    except:
        raise Http404('Image does not exist')

def resize(request,id):
    data = store.objects.get(id=id)
    if request.method == "POST":
        global width
        global height
        width = int(request.POST['width'])
        height = int(request.POST['height'])
        image = cv2.imread(data.image.path)
        new_image = cv2.resize(image, (width, height))
        
        _,buffer = cv2.imencode('.jpg',new_image)
        image_bytes = buffer.tobytes()
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
        return render(request,'test3.html',{'image':encoded_image,'id':id,'image_data':data})
        
        
    else:
             
        return render(request,'test3.html',{'id':id,'image_data':data})
    
def download(request,id):
    image = store.objects.get(id=id)
    path = image.image.path
    new_image = cv2.resize(cv2.imread(path),(width,height))
    
    _, buffer = cv2.imencode('.jpg', new_image)
    response = HttpResponse(buffer.tobytes(), content_type='image/jpeg')
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(image.name)
    return response

def gray(request,id):
    data = store.objects.get(id = id)
    gray_img = cv2.cvtColor(cv2.imread(data.image.path),cv2.COLOR_BGR2GRAY)
    _,buffer = cv2.imencode('.jpg',gray_img)
    image_bytes = buffer.tobytes()
    encoded_image = base64.b64encode(image_bytes).decode('utf-8')
    return render(request,'gray.html',{'image':encoded_image,'id':id,'image_data':data})
    
    
def test(request,id):
    data = store.objects.get(id = id)
    
    if request.method == "POST":
        alpha = int(request.POST['contrast'])/10
        beta = int(request.POST['brightness'])-100
        image = cv2.imread(data.image.path)
        conv_image = cv2.convertScaleAbs(image,alpha=alpha,beta=beta)
        _,buffer = cv2.imencode('.jpg',conv_image)
        image_bytes = buffer.tobytes()
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
        return render(request,'cont_bri.html',{'image':encoded_image,'id':id,'image_data':data})
    
    else:
        return render(request,'cont_bri.html',{'id':id,'image_data':data})    

def delete(request,id):
    data = store.objects.get(id=id)
    data.delete()
    messages.success(request,"image deleted successfully")
    return redirect('view')
    