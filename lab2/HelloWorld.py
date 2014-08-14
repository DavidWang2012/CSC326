from bottle import request, route, run, debug,error, template, static_file
from bottle import BaseRequest
from collections import Counter
import sqlite3
# Lab 2 frontend
# added sql query funtion
# make page look nicer compare to lab1
@route('/')
def frontpage():
    """ This is a default route for the frontend implementation
    Which is the frontpage.
    The front page has implemented the following:
        1. HTML
	2. CSS, with emphasis on button, hovering, and alignment
	3. JavaScript DOM and XML standard, known as AJAX
	4. POST method for form submission
    """
    return '''<!DOCTYPE html>
    <html>
        <head>
	    <style>
	            body {
		        margin:0;
			padding:0;
		        background-color:#d0e4fe;
		    }
		    img {
		        align-items: center;
                        border:2px solid;
                        border-radius:25px;
			height:auto;
			width:auto;
			left:10%;
			position:relative;
		    }
		    img:hover {
		        opacity:0.6;
			filter:alpha(opacity=60); /* For IE8 and earlier */
		    }
	            h1 {
                        color:orange;
                        text-align:center;
                    }
		    h2 {
		        color:green;
			text-align:center;
		    }
		    .center {
		        margin-left:auto;
                        margin-right:auto;
			width:70%;
                    }
                    .button {
                        -moz-box-shadow:inset 0px 1px 0px 0px #bbdaf7;
	                -webkit-box-shadow:inset 0px 1px 0px 0px #bbdaf7;
                        box-shadow:inset 0px 1px 0px 0px #bbdaf7;
                        -webkit-gradient( linear, left top, left bottom, color-stop(0.05, #79bbff), color-stop(1, #378de5) );
	                -moz-linear-gradient( center top, #79bbff 5%, #378de5 100% );
	                filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#79bbff', endColorstr='#378de5');
	                background-color:#79bbff;
	                -webkit-border-top-left-radius:20px;
	                -moz-border-radius-topleft:20px;
	                border-top-left-radius:20px;
	                -webkit-border-top-right-radius:20px;
	                -moz-border-radius-topright:20px;
	                border-top-right-radius:20px;
	                -webkit-border-bottom-right-radius:20px;
	                -moz-border-radius-bottomright:20px;
	                border-bottom-right-radius:20px;
	                -webkit-border-bottom-left-radius:20px;
	                -moz-border-radius-bottomleft:20px;
	                border-bottom-left-radius:20px;
	                text-indent:0;
	                border:1px solid #84bbf3;
	                display:inline-block;
	                color:#ffffff;
	                font-family:Arial;
	                font-size:15px;
	                font-weight:bold;
	                font-style:normal;
	                height:65px;
	                line-height:65px;
	                width:131px;
	                text-decoration:none;
	                text-align:center;
	                text-shadow:1px 1px 0px #528ecc;
                    }
                    .button:hover {
                        -webkit-gradient( linear, left top, left bottom, color-stop(0.05, #378de5), color-stop(1, #79bbff) );
                        -moz-linear-gradient( center top, #378de5 5%, #79bbff 100% );
                        filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#378de5', endColorstr='#79bbff');
                        background-color:#378de5;
                    }
		    .button:active {
                        position:relative;
                        top:1px;
                    }
	    </style>
	    <script>
                function loadXMLDoc()
                {
                    var xmlhttp;
                    if (window.XMLHttpRequest)
                    {// code for IE7+, Firefox, Chrome, Opera, Safari
                        xmlhttp=new XMLHttpRequest();
                    }
                    else
                    {// code for IE6, IE5
                        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
                    }
                    xmlhttp.onreadystatechange=function()
                    {
                        if (xmlhttp.readyState==4 && xmlhttp.status==200)
                        {
                            document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
                        }
                    }
                    xmlhttp.open("GET","ajax_info.txt",true);
                    xmlhttp.send();
                }
                (function() {
                       var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                       po.src = 'https://apis.google.com/js/client:plusone.js';
                       var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
                       })();
                       function signinCallBack(authResult) {
                           if (authResult['access_token']) {
                               document.getElementById('signinButton').setAttribute('style', 'display: none');
                           } else if (authResult['error']) {
                               console.log('Sign-in state: ' + authResult['error']);
                           }
                       }
                       function disconnectUser(access_token) {
                           var revokeUrl = 'https://accounts.google.com/o/oauth2/revoke?token=' + access_token;
                           $.ajax({
                               type: "GET",
                               url: revokeUrl,
                               async: false,
                               contentType: "application/json",
                               dataType: 'jsonp',
                               success: function(nullResponse) {
                                   // Do something now that user is disconnected
                                         // The response is always undefined.
                               },
                               error: function(e) {
                                   //console.log(e); handle the error here
                               }
                           });
                       }
                       // It could trigger disconnect button with one click.
                       $('#revokeButton').click(disconnectUser);
            </script>
        <head>
        <title>CSC326 Search Engine Group 1</title>
        <body>
            <div class="center">
                <img src="http://individual.utoronto.ca/zhwzh308/crab.jpg" alt="Crawler" />
                <h1>Please input your keyword:</h1>
	        <form action="/" method="POST">Search <input size="80" type="text" name="query"><br />
                    <button class="button" type="submit">Submit</button>
                </form>
	    </div>
	    <div class="center">
                <span id = "signinButton">
                    <span
                        class="g-signin"
                        data-callback="signinCallBack"
                        data-clientid="search-engine-326"
                        data-cookiepolicy="single_host_origin"
                        data-requestvisibleactions="http://schemas.google.com/AddActivity"
                        data-scope="https://www.googleapis.com/auth/plus.login">
                    </span>
                </span>
                <div id="myDiv"><h2>Let AJAX change this text</h2></div>
		<button class="button" type="button" onclick="loadXMLDoc()">Change Content</button>
	    </div>
        </body>
    </html>
'''
@route('/', method='POST')
def query():
    queryString = request.forms.get('query')
    if queryString == None:
        return error404();
    tokens = queryString.split()
    # Use split() to split list into tokens
    querySet = set()
    # Stores unique query word
    queryFirst = tokens[0]
    # Search for the first query only!
    returnPage = """<!DOCTYPE html>
    <html><title>Search Result Page</title>
    <body>
    """
    # The page to be returned
    returnPage += "<h1>Search \"" + queryFirst + "\"</h1><br />"
    returnPage += """
    <table border = \"1\">
        <tr>
	    <td>
	        <b>Word</b>
	    </td>
	    <td>
	        <b>Count</b>
            </td>
	</tr>
	"""
    # It may look messy, what is does is, start a table with 2 columns, one row for word
    # the other for count.
    for index in range(len(tokens)):
        querySet.add(tokens[index]);
	# This for loop adds items to the querySet, which should be unique.
    for token in querySet:
        n = 0
        for i in range(len(tokens)):
            if (token == tokens[i]):
                n += 1
        returnPage += ("<tr><td>" +token + "</td><td>" + str(n) + "</td></tr>")
    # returnPage += ("</table><p>You queried " + queryFirst + "</p></body></html>")
    returnPage += "</table><br /><p>Search Results</p><table border = \"1\">"
    returnPage += queryDB(queryFirst)
    returnPage += "</table></body></html>"
    # Closing tags
    return returnPage

def queryDB(query):
    con = sqlite3.connect('dbFile.db')
    cursor = con.cursor()
    result=''
    # SELECT PageRank.ranking, DocIndex.url, Lexicon.wordID, InvertedIndex.docID
    cursor.execute('''SELECT PageRank.ranking, DocIndex.url FROM Lexicon
    INNER JOIN InvertedIndex
        ON Lexicon.wordID = InvertedIndex.wordID
    INNER JOIN DocIndex
        ON InvertedIndex.docID = DocIndex.doc_ID
    INNER JOIN PageRank
        ON DocIndex.doc_ID = PageRank.docID
    WHERE Lexicon.word = ?
    ORDER BY ranking DESC''', [query]);
    # Rank result from high to low.
    # con.commit() , url ASC
    rows = cursor.fetchall()
    # print rows
    for row in rows:
        result += '<tr><td>PageRank: %s</td><td><a href="%s">%s</a></td></tr>' % (str(row[0]), row[1], row[1])
    con.close()
    return result

# /hello is tester function
@route('/hello')
def hello():
    return 'Hello World!'
# Dynamic content generate.
@route('/ajax_info.txt')
def ajax_info():
    return """<p align="center">AJAX is not a new programming language.<br />
AJAX is a technique for creating fast and dynamic web pages.</p>
"""
#error (404) handling
@error(404)
def error404(error):
    return '''<!DOCTYPE html>
    <html>
    <title>Page Not Found</title>
    <body>
    <img src="http://individual.utoronto.ca/zhwzh308/oops.jpg" />
    <h1>The resource you requested is not available</h1>
    <p>You can click <a href="/">here</a> to return to the front page</p> 
    </body></html>'''
#error (403) handling
@error(403)
def error403(error):
    return 'There is a mistake in your url!'
# debug gives out more information during run time
debug(True)
# reloader reloads python script on any change. The default run location is
# http://127.0.0.1:8080/
run(reloader=True)
# run(host="localhost",port=8080,debug=True)
