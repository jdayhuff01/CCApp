from django.forms import ModelForm
from django.db import models
from team_creator.models import GameRosters
from django import forms

class TeamsForm(ModelForm):
    team_1_name = forms.TextInput()
    p1_team1 = forms.TextInput()
    p2_team1 = forms.TextInput()
    p3_team1 = forms.TextInput()
    p4_team1 = forms.TextInput()
    p5_team1 = forms.TextInput()
    p6_team1 = forms.TextInput()
    team_2_name = forms.TextInput()
    p1_team2 = forms.TextInput()
    p2_team2 = forms.TextInput()
    p3_team2 = forms.TextInput()
    p4_team2 = forms.TextInput()
    p5_team2 = forms.TextInput()
    p6_team2 = forms.TextInput()
    class Meta:
        model = GameRosters
        fields = ['team_1_name','p1_team1','p2_team1','p3_team1','p4_team1','p5_team1','p6_team1', 'team_2_name','p1_team2','p2_team2','p3_team2','p4_team2','p5_team2','p6_team2']



    
    

    


