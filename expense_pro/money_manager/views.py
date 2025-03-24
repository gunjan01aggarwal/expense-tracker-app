from django.shortcuts import render,redirect,get_object_or_404
from .models import Expense
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import Expenseform
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.db.models import Count,Sum
from datetime import datetime,timedelta
from django.utils import timezone
from django.core.paginator import Paginator
from Users.models import User,Profile

# Create your views here.
def index(request):
    expenses=Expense.objects.order_by('-id')
    description=request.GET.get('description')
    data=Expense.objects.all()
    #search by using description
    if description:
        expenses=data.filter(description__icontains=description)
    #pagination
    item_per_page=5
    paginator=Paginator(data,item_per_page)
    page=request.GET.get('page')
    expenses=paginator.get_page(page)   
    #calculate serial number
    #page_obj contains all objects on the basis of item_per_page
    #page_obj.number gives the current page number    
    start_serial_number=(expenses.number-1)*item_per_page 
    # Add serial number to each expense
    for index, expense in enumerate(expenses, start=1):
        expense.serial_number = start_serial_number + index  # Assign serial number manually

    """if date:
        expenses=data.filter(date__icontains=date) """   
    return render(request, "Money_Manager/index.html",{'expenses':expenses})

def analysis(request):
    return render(request, "Money_Manager/analysis.html")

def add(request):
    if request.method == "POST":
        try:
            # Extract data from POST request
            category = request.POST.get('category')
            description = request.POST.get('description')
            date = request.POST.get('date')
            amount = request.POST.get('amount')

            # Validate required fields
            if not category or not date or not description or not amount:
                messages.error(request, 'Missing required fields.')
                return redirect('money_manager:add')  # Redirect back to the form page

            # Create and save employee in the database
            Exp_info = Expense.objects.create(
                category=category,
                date=date,
                description=description,
                amount=amount
            )
            Exp_info.save()

            # Add success message and redirect
            messages.success(request, 'Expenses  successfully added!')
            return redirect('money_manager:index')

        except ValidationError as e:
            # Handle validation errors
            messages.error(request, f'Validation error: {str(e)}')
            return redirect('money_manager:add')  # Redirect back to the form page

    return render(request, "Money_Manager/createform.html")


def view(request,exp_id):
    if request.method == "POST":
        expense_ = Expense.objects.get(id=exp_id)
        form = Expenseform(request.POST, instance=expense_)
        if form.is_valid():
            form.save()
        return redirect("money_manager:index")
    else:
        expense_ = Expense.objects.get(id=exp_id)
        form = Expenseform(instance=expense_)
    return render(request,'Money_Manager/viewform.html',{'form':form,'expense_':expense_})

def edit(request, exp_id):
    expense_ = get_object_or_404(Expense, id=exp_id)

    if request.method == "POST":
        date_input = request.POST.get('date')
        if date_input:
            expense_.date = parse_datetime(date_input)  # Converts string to datetime object

        form = Expenseform(request.POST, instance=expense_)
        if form.is_valid():
            form.save()
            return redirect("money_manager:index")
    else:
        form = Expenseform(instance=expense_)

    return render(request, 'Money_Manager/editform.html', {"form": form, "expense_": expense_})


def delete(request,exp_id):
    expense_ = get_object_or_404(Expense, id=exp_id) 
    if request.method == 'POST':
       expense_.delete()
       messages.error(request,"Expenses successfully deleted.")
       return redirect("money_manager:index")
    return render(request,'Money_Manager/deleteform.html',{'expense_':expense_})

def handle_action(request, exp_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        expense = get_object_or_404(Expense, id=exp_id)

        if action == 'view':
            return redirect('money_manager:view', expense.id)
        elif action == 'edit':
            return redirect('money_manager:edit', expense.id)
        elif action == 'delete':
            return redirect('money_manager:delete', expense.id)

    # Default behavior if no action matches
    return redirect('money_manager:index')   

#Calculate today expenses
"""def today_exp():
    data=Expense.objects.all().values()
    today_expenses = 0

    # Get today's date in YYYY-MM-DD format (IST timezone aware)
    today_date = timezone.localdate().strftime('%Y-%m-%d')
    for i in range(len(data)):
        # Ensure 'date' exists and is formatted properly
        expense_date = data[i]['date'].strftime('%Y-%m-%d') if data[i]['date'] else None
        if expense_date == today_date:
            today_expenses += data[i]['amount']  # Assuming 'amount' is a numeric field
    print(today_expenses)
    
    today_expenses=float(today_expenses)
    return today_expenses
"""
def daily():
    data=Expense.objects.all().values()
    daily_exp=0
    today_date=datetime.today().strftime('%Y-%m-%d')    
    for i in range(len(data)):
        expense_date=data[i]['date'].strftime('%Y-%m-%d') if data[i]['date'] else None
        if expense_date==today_date:
            daily_exp+=data[i]['amount']            
    daily_exp=float(daily_exp)
    return daily_exp

# Calculate yesterday expenses
def yesterday():
    data=Expense.objects.all().values()
    yesterday_expenses=0
    # Get yesterday's date in YYYY-MM-DD format (IST timezone aware)
    yesterday_date=(datetime.today()-timedelta(days=1)).strftime('%Y-%m-%d')
    for i in range(len(data)):
        # Ensure 'date' exists and is formatted properly
        expense_date=data[i]['date'].strftime('%Y-%m-%d') if data[i]['date'] else None
        if expense_date==yesterday_date:
            yesterday_expenses+=data[i]['amount']
    yesterday_expenses=float(yesterday_expenses)
    return yesterday_expenses        

#Calculate weekly expenses
def weekly():
    data=Expense.objects.all().values()
    weekly_expenses=0
    # Get today's date in YYYY-MM-DD format (IST timezone aware)
    today_date=datetime.today().strftime('%Y-%m-%d')
    Before_week_date=(datetime.today()-timedelta(days=7)).strftime('%Y-%m-%d')
    while Before_week_date<=today_date:
        for i in range(len(data)):
            expense_date=data[i]['date'].strftime('%Y-%m-%d') if data[i]['date'] else None
            if expense_date==Before_week_date:
                weekly_expenses+=data[i]['amount']
        Before_week_date=(datetime.strptime(Before_week_date,'%Y-%m-%d')+timedelta(days=1)).strftime('%Y-%m-%d') 
    weekly_expenses=float(weekly_expenses)
    return weekly_expenses          

#Calculate monthly expenses
def monthly():
    data=Expense.objects.all().values()
    monthly_expenses={'January':0,'February':0,'March':0,'April':0,
                      'May':0,'June':0,'July':0,'August':0,'September':0,
                      'October':0,'November':0,'December':0}
    # Get today's date in YYYY-MM-DD format (IST timezone aware)
    months={'01':'January','02':'February','03':'March','04':'April',
            '05':'May','06':'June','07':'July','08':'August','09':'September',
            '10':'October','11':'November','12':'December'}
    for i in range(len(data)):
        expense_month=data[i]['date'].strftime('%m') if data[i]['date'] else None
        expense_month=months[expense_month]
        for key in monthly_expenses.keys():
            if expense_month==key:
                monthly_expenses[key]+=data[i]['amount']
    print(monthly_expenses)
    monthly_expenses={key:float(value) for key,value in monthly_expenses.items()}   
    return monthly_expenses         
def chart_view(request):
    #for chart1
    #Aggregrate count of occurence of each category.
    category_counts=Expense.objects.values('category').annotate(total=Count('category'))    
    labels1=[item['category'] for item in category_counts]
    values1=[item['total'] for item in category_counts]
    #for chart2
    #Calculate sum of amount for each category.
    category_sum=Expense.objects.values('category').annotate(total_sum=Sum('amount'))
    labels2=[item['category'] for item in category_sum]
    values2=[float(item['total_sum']) for item in category_sum]
    #for chart3
    daily_exp=daily()
    #for chart4
    yesterday_exp=yesterday()
    #for chart5
    weekly_exp=weekly()
    #for chart6
    monthly_exp=monthly()
    labels3=[key for key in monthly_exp.keys()]
    values3=[value for value in monthly_exp.values()] 
    return render(request,'Money_Manager/analysis.html',{'labels1':labels1,
                                                         'values1':values1,
                                                         'labels2':labels2,'values2':values2
                                                         ,'daily_exp':daily_exp,
                                                         'yesterday_exp':yesterday_exp,
                                                         'weekly_exp':weekly_exp,
                                                        'labels3':labels3,'values3':values3
                                                         })
#Current Month Analysis
"""def cma(request):
    current_month=datetime.today().strftime('%m')
    month_expenses=monthly()
    current_month_expense=month_expenses[current_month]
    Amt=Profile.objects.get(user=request.user).monthly_income
    Rem_Amt=Amt-current_month_expense

    remaining_percent = (Rem_Amt / Amt) * 100  # Calculate remaining percentage

    context = {
        "Rem_Amt": Rem_Amt,
        "Amt": Amt,
        "remaining_percent": remaining_percent,  # Send percentage to template
    }
    return render(request, "Money_Manager/analysis.html", context)
"""

