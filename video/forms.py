from django import forms
from .models import Video, Comment


class Post_Model_From(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'content', 'thumbnail', 'video', 'category']



class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Add a comment...', 'class': 'form-control', }))

    class Meta:
        model = Comment
        fields = ('body',)
