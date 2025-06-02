from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.utils.dateparse import parse_date

def dashboard(request):
    transactions = Transaction.objects.order_by('-date')

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    t_type = request.GET.get('type')

    if start_date:
        transactions = transactions.filter(date__gte=parse_date(start_date))
    if end_date:
        transactions = transactions.filter(date__lte=parse_date(end_date))
    if t_type in ['income', 'outcome']:
        transactions = transactions.filter(type=t_type)

    income = sum(t.amount for t in transactions if t.type == 'income')
    outcome = sum(t.amount for t in transactions if t.type == 'outcome')
    balance = income - outcome

    return render(request, 'transactions/dashboard.html', {
        'transactions': transactions,
        'income': income,
        'outcome': outcome,
        'balance': balance,
        'start_date': start_date,
        'end_date': end_date,
        't_type': t_type,
    })

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})
