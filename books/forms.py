from dataclasses import fields
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms

from books.models import Review


class ReviewForm(forms.ModelForm):
    # body = forms.CharField(widget=forms.Textarea(attrs={'class': 'border'}),
    #                        label='Review comment', max_length=100)
    #image = forms.ImageField(label='Upload image', required=False)

    class Meta:
        model = Review
        fields = ['body', 'image']
        #Widget={'image': NotRequired}
