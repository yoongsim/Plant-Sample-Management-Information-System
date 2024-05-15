#!/usr/bin/python

import MySQLdb
import cgi, cgitb
cgitb.enable() #debugger
form = cgi.FieldStorage()

#connect to MySQL database
db = MySQLdb.connect(host = "localhost", user = "root", db = "ys_plantdb")

#create a cur obejct to execute queries with cursur() method
cur = db.cursor()

table = form.getvalue('table')
attribute = form.getvalue('attribute')
keyword = form.getvalue('keyword') 

try:
    cur.execute("SET foreign_key_checks = 0;")
    cur.execute("DELETE FROM " + table + " WHERE " + attribute + " = '" + keyword +"'")
    msg1 = "Data Deleted Successfully"
    msg2 = "Please proceed to retrieve data to view updated data"
    
    db.commit()
   
except MySQLdb.Error:
    msg1 = "No Data Deleted"
    msg2 = "Please recheck your input"
    
db.close()

## WEBPAGE ##
print"Content-type:text/html\r\n\r\n";
print"<!DOCTYPE html>";
print"<html lang='en'>";
print"<head>";
print"<meta charset='UTF-8'>";
print"<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
print"<title>Assignment2_PSMIS</title>";
print"<link rel='stylesheet' href='/siv3009/yoongsim/.assignment2/styling.css'>";
print"<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>";
print"<link rel='icon' href='/siv3009/yoongsim/.assignment2/images/plant_logo.png'>";
print"</head>";
print"<body>";
print"<div id ='header_div'>";
print"<img src='/siv3009/yoongsim/.assignment2/images/plant_logo.png' alt='Logo' id='logo_image' style='height: 90px;'>";
print"<h1 id = 'h1_header_div'>Plant Sample Management Information System </h1>";
print"</div>";
print"<div id='header_nav'>";
print"<ul id='header_nav_ul'>";
print"<li id ='header_li' ><a href='/siv3009/yoongsim/.assignment2/main.html' >Home</a></li>";
print"<li id = 'header_li' ><a href='/siv3009/yoongsim/.assignment2/insert.html' >Insert Data</a></li>";
print"<li id = 'header_li' ><a href='/siv3009/yoongsim/.assignment2/update.html' >Update Data</a></li>";
print"<li id = 'header_li' ><a href='/siv3009/yoongsim/.assignment2/delete.html' >Delete Data</a></li>";
print"<li id = 'header_li'><a href='/siv3009/yoongsim/.assignment2/retrieve.html' >Retrieve Data</a></li>";
print"<button id='feedback_button'></button>";
print"</ul></div>";

print"<div id='content'>";
print"<div style = 'text-align: center'>";
print"<h3><b>%s</b></h3>" % msg1
print"<h3><b>%s</b></h3>" % msg2
print"</div><br>";
print"<br><br></div>";

print"<div id='footer'>";
print"<br><br>";
print"<p> SIV3009 Assignment 2 | Created by: &nbsp;&nbsp; U2004667 CHONG YOONG SIM  &nbsp;&nbsp; & &nbsp;&nbsp; U2004605 LAI HUI HUI<br></p>";
print"<br><br>";
print"</div>";
print"</body>";