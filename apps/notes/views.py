from django.shortcuts import render
from django.http import HttpResponse
from .models import Note


def list_notes(request):
    # limit to 10 latest notes
    notes = Note.objects.all().order_by('-created_at')[:10]

    notes_text = ""

    for note in notes:
        notes_text += f"@{note.created_by} {note.contents}"

    return HttpResponse(notes_text)
