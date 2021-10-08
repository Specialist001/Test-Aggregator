### News Aggregator on Django (TEST)

#### Prerequisite
You need to have some basic knowledge of these libraries:

- Django Framework
- BeautifulSoup
- requests module

It is a web application which aggregates data (news articles) from multiple websites ([theonion.com](https://www.theonion.com) and [upl.uz](https://upl.uz)). Then presents the data in one location.
<br>

#### Steps to Build Django Project on News Aggregator App

Before starting, we will need to install some of the libraries. We will install the requests and BeautifulSoup libraries. You can install them using pip.
<pre>
<code>pip install bs4</code>
</pre>
<pre>
<code>pip install requests</code>
</pre>
<pre>
<code>pip install python-dotenv</code>
</pre>
<br>

##### Copy <code>.env.example</code> file to <code>.env</code> and paste your <code>SECRET_KEY</code>
<pre>
<code>cp .env.example .env</code>
</pre>

#### Run migrations
<pre>
<code>python manage.py migrate</code>
</pre>

#### Run server
<pre>
<code>python manage.py runserver</code>
</pre>

