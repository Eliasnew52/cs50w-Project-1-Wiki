from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
import random

from . import util

# MD to HTML
def MD_Convert(entry):
    MK = Markdown()
    HTML_Item = MK.convert(entry)
    return HTML_Item


# Function that Returns a List of all Available Entries
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



# Function that loads The Entry TITLE and its Content

def entry(request, TITLE):
    if request.method == 'GET':
        Entry = util.get_entry(TITLE)
        if Entry:
            Entry_Cont = MD_Convert(Entry)
            return render(request, "encyclopedia/entry.html", {"TITLE": TITLE,"Entry_Cont": Entry_Cont, "message":"Entry Found"})
        else:
            return render(request, "encyclopedia/entry.html")

def search(request):
    if request.method == 'GET':
        keyword = request.GET['q']
        All_Entries = [Entry.lower() for Entry in util.list_entries()]

        if not All_Entries:
            return render(request, "encyclopedia/search.html")
        
        if keyword.lower() in All_Entries:
            return redirect('entry', TITLE = keyword)
        else:
            All_Matches = Matches(keyword)
            if All_Matches:
                return render(request, "encyclopedia/search.html", {"keyword": keyword, "entries": All_Matches})
            else:
                return render(request, "encyclopedia/search.html", {"keyword": keyword })
            

#Match Search Function
              
def Matches(TITLE):
    results = []
    TITLE = TITLE.upper()
    All_Entries = util.list_entries()
    if not TITLE:
        return results
    else:
        results = [matches for matches in All_Entries if TITLE.lower() in matches.lower()]

        #List Check
        print(results)
        return results
