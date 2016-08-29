'''
Created on 25 de ago de 2016

@author: airton
'''
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    html = "<html>"+ "<head>"+"<script type=\"text/javascript\" src=\"https://www.gstatic.com/charts/loader.js\"></script>"+"<script type=\"text/javascript\">"+"google.charts.load('current', {'packages':['corechart']});"+"google.charts.setOnLoadCallback(drawChart);"+"function drawChart() {"+"var data = google.visualization.arrayToDataTable(["+"['Task', 'Hours per Day'],"+"['Work',     11],"+"['Eat',      2],"+"['Commute',  2],"+"['Watch TV', 2],"+"['Sleep',    7]"+"]);"+"var options = {"+"title: 'My Daily Activities'"+"};"+"var chart = new google.visualization.PieChart(document.getElementById('piechart'));"+"chart.draw(data, options);"+"}"+"</script>"+"</head>"+"<body>"+"<div id=\"piechart\" style=\"width: 900px; height: 500px;\"></div>"+"</body>"+"</html>"
    return HttpResponse(html)

def post_list(request):
    return render(request, 'post_list.html', {})