from django import forms

from .models import Player
from .models import Match


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match