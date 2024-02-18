
from django.shortcuts import render,redirect
from .models import Cosmetic,Groceries,Cold,Ice,Seller
import random

listquan=[]
listitem=[]
listpr=[]
listtot=[]
ctax=[]
gtax=[]
ictax=[]
cotax=[]
total=[]
name=[]
phon=[]
def index(request):
    data1 = Cosmetic.objects.all()
    data2 = Groceries.objects.all()
    data3 = Cold.objects.all()
    data4 = Ice.objects.all()
   
    if request.method=="POST":
        listquan.clear()
        listitem.clear()
        listpr.clear()
        listtot.clear()
        ctax.clear()
        gtax.clear()
        ictax.clear()
        cotax.clear()
        total.clear()
        name.clear()
        phon.clear()
        csum = 0
        gsum = 0
        cosum = 0
        isum = 0
        name.append(request.POST.get('cname'))
        phon.append(request.POST.get('cphone'))
    
        for i in data1:
            val = request.POST.get(str(i.itemid))  # Use str() to get the itemid as a string
            if val:
                listquan.append(val)
                listitem.append(i.item)
                listpr.append(i.itemprice)
                listtot.append(int(val)*i.itemprice)
                csum += int(val)*i.itemprice  # Convert the value to an integer before adding it to the sum
    
        for i in data2:
            val = request.POST.get(str(i.itemid))
            if val:
                listquan.append(val)
                listitem.append(i.item)
                listpr.append(i.itemprice)
                listtot.append(int(val)*i.itemprice)
                gsum += int(val)*i.itemprice
    
        for i in data3:
            val = request.POST.get(str(i.itemid))
            if val:
                listquan.append(val)
                listitem.append(i.item)
                listpr.append(i.itemprice)
                listtot.append(int(val)*i.itemprice)
                cosum += int(val)*i.itemprice
    
        for i in data4:
            val = request.POST.get(str(i.itemid))
            if val:
                listquan.append(val)
                listitem.append(i.item)
                listpr.append(i.itemprice)
                listtot.append(int(val)*i.itemprice)
                isum += int(val)*i.itemprice
    
        tot = csum + cosum + gsum + isum
        total.append(tot)
        ctax.append(float(0.05*csum))
    
        gtax.append(float(0.02*gsum))
    
        cotax.append(float(0.07*cosum))
        
        ictax.append(float(0.03*isum))
    
    
        context = {
            'item': data1,
            'item2': data2,
            'item3': data3,
            'item4': data4,
            'gsum': gsum,
            'cosum': cosum,
            'csum': csum,
            'isum': isum,
            'ctax':ctax[0],
            'gtax':gtax[0],
            'cotax':cotax[0],
            'ictax':ictax[0]
        }
        return render(request, 'index.html', context)
    else:
        context = {
            'item': data1,
            'item2': data2,
            'item3': data3,
            'item4': data4,
            'total': 0,
            'gsum': 0,
            'cosum':0,
            'csum': 0,
            'isum': 0,
            'ctax':0,
            'gtax':0,
            'cotax':0,
            'ictax':0
        }
        return render(request, 'index.html',context) 
    

def counter(request):
  personal=Seller.objects.all()
  mylist = zip(listquan, listitem,listpr,listtot)
  mylist2 = zip(ctax,gtax,ictax,cotax)
  mylist3=zip(name,phon)
  var=random.randint(0,9999)
  context = {
            'mylist': mylist,
            'perso':personal,
            'ctax':ctax,
            'mylist2':mylist2,
            'total':total,
            'mylist3':mylist3,
            'rand':var
        }
 
  
  return render(request, 'counter.html', context)
