#!/usr/bin/python

import MySQLdb
import cgi, cgitb
cgitb.enable() #debugger
form = cgi.FieldStorage()

#connect to MySQL database
db = MySQLdb.connect(host = "localhost", user = "root", db = "ys_plantdb")

#create a cur obejct to execute queries with cursur() method
cur = db.cursor()

table = form.getvalue("table")

cur.execute("SELECT * FROM " + table)
# Fetch all rows using fetchall() method
result = cur.fetchall()

db.close()

## WEBPAGE ##
print"Content-type:text/html\r\n\r\n";
print"<!DOCTYPE html>"
print"<html lang='en'>"
print"<head>"
print"<meta charset='UTF-8'>"
print"<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
print"<title>Assignment2_PSMIS</title>"
print"<link rel='stylesheet' href='/siv3009/yoongsim/.assignment2/styling.css'>"
print"<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>"
print"<link rel='icon' href='/siv3009/yoongsim/.assignment2/images/plant_logo.png'>"
print"</head>"
print"<body>"
print"<div id ='header_div'>"
print"<img src='/siv3009/yoongsim/.assignment2/images/plant_logo.png' alt='Logo' id='logo_image' style='height: 90px;'>"
print"<h1 id = 'h1_header_div'>Plant Sample Management Information System </h1>"
print"</div>"
print"<div id='header_nav'>"
print"<ul id='header_nav_ul'>"
print"<li id ='header_li' ><a href='/siv3009/yoongsim/.assignment2/main.html' >Home</a></li>"
print"<li id = 'header_li' ><a href='/siv3009/yoongsim/.assignment2/insert.html' >Insert Data</a></li>"
print"<li id = 'header_li' ><a href='/siv3009/yoongsim/.assignment2/update.html' >Update Data</a></li>"
print"<li id = 'header_li' ><a href='/siv3009/yoongsim/.assignment2/delete.html' >Delete Data</a></li>"
print"<li id = 'header_li'><a href='/siv3009/yoongsim/.assignment2/retrieve.html' >Retrieve Data</a></li>"
print"<button id='feedback_button'></button>"
print"</ul></div>"

print"<div id='content'>"
print "<table style='margin-left: auto; margin-right: auto;'>"

if table == "species":
	print "<div style='text-align:center;'><h3><b>Species Table</b></h3><hr>" 
	print "<tr><td><b>spID</b></td><td><b>spAuthors</b></td><td><b>spYear</b></td><td><b>spName</b></td></tr>"

	for x in result:
		print "<tr><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td></tr>" % (x[0],x[1],x[2],x[3])

elif table == "spDetails":
	print "<div style='text-align:center;'><h3><b>Species Details Table</b></h3><hr>"
	print "<tr><td><b>spID</b></td><td><b>descWhole</b></td><td><b>descFlower</b></td><td><b>descFruit</b></td><td><b>descBark</b></td><td><b>descLeaf</b></td></tr>"

	for x in result:
		print "<tr><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td></tr>" % (x[0],x[1],x[2],x[3],x[4],x[5])

elif table == "samples":
	print "<div style='text-align:center;'><h3><b>Samples Table</b></h3><hr>"

	print "<tr><td><b>sampleID</b></td><td><b>collectorName</b></td><td><b>recordDate</b></td><td><b>description</b></td><td><b>spID</b></td></tr>"

	for x in result:
		print "<tr><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td></tr>" % (x[0],x[1],x[2],x[3],x[4])

elif table == "samplesDistributions":
	print "<div style='text-align:center;'><h3><b>Samples Distributions Table</b></h3><hr>"

	print "<tr><td><b>sampleID</b></td><td><b>distID</b></td></tr>"

	for x in result:
		print "<tr><td>%s<span class='tab'></td><td>%s<span class='tab'></td></tr>" % (x[0],x[1])


elif table == "distributions":
	print "<div style='text-align:center;'><h3><b>Distributions Table</b></h3><hr>"

	print "<tr><td><b>distID</b></td><td><b>geoSpatialCoverage</b></td><td><b>geoSpatialCoordinates</b></td></tr>"

	for x in result:
		print "<tr><td>%s<span class='tab'></td><td>%s<span class='tab'></td><td>%s<span class='tab'></td></tr>" % (x[0],x[1],x[2])


print "</table></div><br><br><br><br><br><br>"

print"<div id='footer'>"
print"<br><br>"
print"<p> SIV3009 Assignment 2 | Created by: &nbsp;&nbsp; U2004667 CHONG YOONG SIM  &nbsp;&nbsp; & &nbsp;&nbsp; U2004605 LAI HUI HUI<br></p>"
print"<br><br>"
print"</div>"
print"</body>"
