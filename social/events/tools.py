from django.shortcuts import render, redirect


def is_staff(request, redirection):
    if request.user.is_staff == False:
        return redirect(redirection)