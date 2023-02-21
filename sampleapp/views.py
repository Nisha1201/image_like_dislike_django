# from django.shortcuts import render, redirect 
from .models import Image
from .forms import ImageUploadForm 
from django.shortcuts import render, redirect, get_object_or_404



def uploadView(request):
    # data=[]                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
            form = ImageUploadForm()
            data = Image.objects.all()
            print(data)
        
    return render(request, 'upload.html', {'form': form,'data':data})

# def image_upload(request):
#     if request.method == 'POST':
#         if 'like' in request.POST:
#             like_image(request, request.POST['like'])
#         elif 'dislike' in request.POST:
#             dislike_image(request, request.POST['dislike'])
#         return redirect('upload_image')
#     form = ImageUploadForm()
#     data = Image.objects.all()
#     print(form,"kkkkkkkkkkkkkkkkkk")
#     print(data,"dddddddddddddddddd")
#     return render(request, 'upload.html', {'form': form, 'data': data})



def like_image(request, id):
    #  if request.method == 'POST':
        # image = Image.objects.all(Image, pk=id)
        image = get_object_or_404(Image, id=id)
        print(f"Liking image with id={id}")
        print(f"Image before: {image}")
        print(image,"lllllllllllllllllllllllll")
        image.likes += 1
        image.save()
        print(f"Image after: {image}")
        # print(image,"ooooooooooooooooooo")
        return redirect('upload_image')

def dislike_image(request, id):
     if request.method == 'POST':
        image = Image.objects.get(id=id)
        # image = get_object_or_404(Image, pk=id)
        image.likes -= 1
        image.dislikes += 1
        image.save()
        print(image)
        return redirect('upload_image')

