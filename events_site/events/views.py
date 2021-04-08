from django.shortcuts import render

events = [
    {
        'organizer': 'Sziget Kft.',
        'title': 'Balaton Sound Official',
        'information': 'Festival by lake Balaton',
        'from': 'July 5, 2021',
        'to': 'July 10, 2021'
    },
    {
        'organizer': 'BCE HÖK',
        'title': 'Évzáró Feszivál Official',
        'information': 'Festival by lake Balaton',
        'from': 'August 5, 2021',
        'to': 'August 10, 2021'
    }
]


def home(request):
    context = {
        'events': events
    }
    return render(request, 'events/home.html', context)


def about(request):
    return render(request, 'events/about.html')
