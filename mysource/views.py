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
        print(sources)
        return render(request, 'mysource.html', {'sources': sources})


def Mysource_delete(request, id):
    source = My_Source.objects.get(id=id)
    print(source)
    source.delete()
    return redirect('mysource')

def Mysource_update(request, id):
    source = My_Source.objects.get(id=id)
    if request.method == 'POST':
        source.mysource = request.POST['mysource']
        source.note = request.POST['note']
        source.save()
        return redirect('mysource')
    else:
        return render(request, 'mysource', {'source', source})

# ------------------------------------------------------------------------------

def Mysource_detail(request,id):
    sources = My_source_detail.objects.filter(mysource_id=id)
    return render(request, 'mysource_detail.html', {'sources': sources,'mysource_id':id})

def Mysource_detail_delete(request, id, pk):
    source = My_source_detail.objects.get(id=pk)
    source.delete()
    return redirect('Mysource_detail', id)

def Mysource_detail_update(request, id, pk):
    source = My_source_detail.objects.get(id=pk)
    source.name = request.POST['name']
    source.link_address = request.POST['link_address']
    source.note = request.POST['note']
    source.save()
    return redirect('Mysource_detail', id)

def Mysource_detail_add(request, id):
    my_Source = My_Source.objects.get(id=id)
    name = request.POST['name']
    link_address = request.POST['link_address']
    note = request.POST['note']
    My_source_detail(mysource_id=my_Source, name=name, link_address=link_address, note=note).save()
    return redirect('Mysource_detail', id)
