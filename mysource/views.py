from django.shortcuts import render, redirect

# Create your views here.
from mysource.models import My_Source, My_source_detail


def Mysource(request):
    if request.method == "POST":
        mysource = request.POST['mysource']
        note = request.POST['note']
        source = My_Source(mysource=mysource, note=note)
        source.save()
        return redirect('mysource')
    else:
        sources = My_Source.objects.all()
        return render(request, 'mysource.html', {'sources': sources })


def Mysource_detail(request):
    mysource_id = request.POST['mysource_id']
    sources = My_source_detail.objects.filter(mysource_id=mysource_id)
    return render(request, 'mysource_detail.html', {'sources': sources })

def Mysource_delete(request, id):
    source = My_Source.objects.get(id=id)
    print(source)
    source.delete()
    return redirect('mysource')

def Mysource_update(request, id):
    source = My_Source.objects.get(id=id)
    print(source)
    if request.method == 'POST':
        source.mysource = request.POST['mysource']
        source.note = request.POST['note']
        source.save()
        return redirect('mysource')
    else:
        return render(request, 'mysource', {'source', source})


