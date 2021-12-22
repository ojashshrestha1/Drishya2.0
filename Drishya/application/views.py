from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from application.models import ImageDetails
from application.kmeans import kmeansImage
from application.humanDetection import detecthuman
# Create your views here.


def index(request):
    return render (request, 'application/index.html')


def aboutus(request):
    return render (request, 'application/aboutus.html')


def upload(request):
    uploading = [1]
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location = "uploads")
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        colors = kmeansImage("uploads/" + filename)
        human = detecthuman("uploads/" + filename)
        image = ImageDetails(filename = myfile.name, color1R = colors[0][2], color1G = colors[0][1], color1B = colors[0][0],
                color2R = colors[1][2], color2G = colors[1][1], color2B = colors[1][0],
                color3R = colors[2][2], color3G = colors[2][1], color3B = colors[2][0],
                human = human)
        image.save()
        return render (request, 'application/upload.html', {'uploading': uploading})


def results(request):
    searchString = request.GET.get('result', '')
    imagelist = []
    all_entries = [data for data in ImageDetails.objects.all()]

    if(searchString == "Human"):
        for i in range(len(all_entries)):
            if(all_entries[i].human == True):
                images = all_entries[i].filename
                imagelist.append(images)
        return render (request, 'application/results.html', {'imagelist': imagelist})

    else:
        with open("colorFile/colorName.txt", "r") as f:
            data = f.readlines()
        for line in data:
            words = line.split()

            if(words[0] == searchString):
                colorR = int(words[1])
                colorG = int(words[2])
                colorB = int(words[3])
                color_list = [colorB, colorG, colorR]
                id_color_list = manhattan_distance(color_list, all_entries)

                if(len(id_color_list) == 0):
                    return render (request, 'application/results.html', {'imagelist': imagelist})
                else:
                    for i in range(len(id_color_list)):
                        database_entry = ImageDetails.objects.filter(id = id_color_list[i])
                        #print(database_entry)
                        images = database_entry[0].filename
                        #print(images)
                        imagelist.append(images)
                    return render (request, 'application/results.html', {'imagelist': imagelist})

        return render (request, 'application/results.html', {'imagelist': imagelist})



#manhattan distance for color matching

def manhattan_distance(color_list, all_entries):
    id_list = []
    manhattan_distance_list = []
    manhattan_distance_color1 = []
    manhattan_distance_color2 = []
    manhattan_distance_color3 = []
    id_color_list = []

    #all_entries = [data for data in ImageDetails.objects.all()]
    for i in range(len(all_entries)):
        id_list.append(all_entries[i].id)
        manhattan_distance1 = abs(color_list[0]-all_entries[i].color1B) + abs(color_list[1]-all_entries[i].color1G) + abs(color_list[2]-all_entries[i].color1R)
        manhattan_distance2 = abs(color_list[0]-all_entries[i].color2B) + abs(color_list[1]-all_entries[i].color2G) + abs(color_list[2]-all_entries[i].color3R)
        manhattan_distance3 = abs(color_list[0]-all_entries[i].color3B) + abs(color_list[1]-all_entries[i].color2G) + abs(color_list[2]-all_entries[i].color3R)

        manhattan_distance_color1.append(manhattan_distance1)
        manhattan_distance_color2.append(manhattan_distance2)
        manhattan_distance_color3.append(manhattan_distance3)

    for i in range(len(id_list)):
        #if(manhattan_distance_list1[i] <= 210 or manhattan_distance_list2[i] <= 210 or manhattan_distance_list3[i] <= 210):
        if(manhattan_distance_color1[i] <= 210):
            manhattan_distance_list.append(manhattan_distance_color1[i])
            id_color_list.append(id_list[i])

        elif(manhattan_distance_color2[i] <= 210):
            manhattan_distance_list.append(manhattan_distance_color2[i])
            id_color_list.append(id_list[i])

        elif(manhattan_distance_color3[i] <= 210):
            manhattan_distance_list.append(manhattan_distance_color3[i])
            id_color_list.append(id_list[i])

    #print(manhattan_distance_list)
    #print(id_color_list)

    quickSort(manhattan_distance_list, id_color_list)
    #print(manhattan_distance_list)
    #print(id_color_list)

    return id_color_list




#sorting for image rank

def quickSort(manhattan_distance_list, id_color_list):
   quickSortHlp(manhattan_distance_list, id_color_list,0,len(manhattan_distance_list)-1)

def quickSortHlp(manhattan_distance_list,id_color_list,first,last):
   if first < last:

       splitpoint = partition(manhattan_distance_list,id_color_list,first,last)

       quickSortHlp(manhattan_distance_list,id_color_list,first,splitpoint-1)
       quickSortHlp(manhattan_distance_list,id_color_list,splitpoint+1,last)


def partition(manhattan_distance_list,id_color_list,first,last):
   pivotvalue = manhattan_distance_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and manhattan_distance_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while manhattan_distance_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = manhattan_distance_list[leftmark]
           temp1 = id_color_list[leftmark]
           manhattan_distance_list[leftmark] = manhattan_distance_list[rightmark]
           id_color_list[leftmark] = id_color_list[rightmark]
           manhattan_distance_list[rightmark] = temp
           id_color_list[rightmark] = temp1

   temp = manhattan_distance_list[first]
   temp1 = id_color_list[first]
   manhattan_distance_list[first] = manhattan_distance_list[rightmark]
   id_color_list[first] = id_color_list[rightmark]
   manhattan_distance_list[rightmark] = temp
   id_color_list[rightmark] = temp1

   return rightmark
