from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    print('*'*80)
    print('in index')
    return render(request, 'django_ninja/index.html')

def process_money(request):
    print('*'*80)
    print('in processing_money')
    if request.method == 'POST':
        if 'activities' in request.session:
            if 'goldcount' in request.session:
                if(request.POST['location']=='farm'):
                    number = random.randint(10,15)
                    request.session['goldcount']+=number
                    request.session['activities']='<p class="green">You earned '+ str(number)+ " golds from the farm!</p>"+request.session['activities']
                    if(request.session['goldcount']>=150):
                        request.session['activities']="<h4 class='green'>YOU WON!</H4>"+request.session['activities']
                    elif(request.session['goldcount']<0):
                        request.session['activities']="<h4 class='red'>YOU LOSE! YOU GAMBLING FOOL!</h4>"+request.session['activities']
                    print(number)
                elif(request.POST['location']=='cave'):
                    number = random.randint(5, 10)
                    request.session['goldcount']+=number
                    request.session['activities']='<p class="green">You found '+ str(number) +" golds from the cave!</p>"+request.session['activities']
                    if(request.session['goldcount']>=150):
                        request.session['activities']="<h4 class='green'>YOU WON!</H4>"+request.session['activities']
                    elif(request.session['goldcount']<0):
                        request.session['activities']="<h4 class='red'>YOU LOSE! YOU GAMBLING FOOL!</h4>"+request.session['activities']
                    print(number)
                elif(request.POST['location']=='house'):
                    number = random.randint(2, 5)
                    request.session['goldcount']+=number
                    request.session['activities']='<p class="green">You earned '+ str(number)+ " golds from the house!</p>"+request.session['activities']
                    if(request.session['goldcount']>=150):
                        request.session['activities']="<h4 class='green'>YOU WON!</H4>"+request.session['activities']
                    elif(request.session['goldcount']<0):
                        request.session['activities']="<h4 class='red'>YOU LOSE! YOU GAMBLING FOOL!</h4>"+request.session['activities']
                    print(number)
                elif(request.POST['location']=='casino'):
                    number = random.randint(-50, 50)
                    request.session['goldcount']+=number
                    if(number>0):
                        request.session['activities']='<p class="green">You won '+ str(number)+ " golds from the casino!</p>"+request.session['activities']
                    else:
                        request.session['activities']='<p class="red">You lost '+str(number)+ " golds from the casino. Oops!</p>"+request.session['activities']
                    if(request.session['goldcount']>=150):
                        request.session['activities']="<h4 class='green'>YOU WON!</H4>"+request.session['activities']
                    elif(request.session['goldcount']<0):
                        request.session['activities']="<h4 class='red'>YOU LOSE! YOU GAMBLING FOOL!</h4>"+request.session['activities']
                    print(number)
            else:
                request.session['goldcount']=0
        else:
            request.session['activities']="<h6>You haven't performed any activites. Go out there and make some money!</h6>"        
        if(request.POST['location']=='restart'):
            request.session['goldcount']=0
            request.session['activities']="<h6>You haven't performed any activites. Go out there and make some money!</h6>"        
        return redirect('/')