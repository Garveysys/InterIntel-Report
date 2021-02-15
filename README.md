**Give examples of different integration protocols you have come across and give example scripts in python 3 on how to achieve each one. (10 pts.)**

**INTERGRATION PROTOCOLS**

**API&#39;s**

Application programming interface is an application that allows two applications to communicate with each other. There can be categorized into private or public. An API allows data transfer between two software.

**Public API**

This are accessible to any third-party developer.

Most public API&#39;s are created for end customers

Public API&#39;s are also open and can be used for commercial purposes.

**Private API**

This are only used within a company or business.

This API&#39;s are often used by company staff / developers.

They are used for integrating organizations systems.

APIs from the Internet. The most popular one is this Web based API class. Web APIs provide machine-readable transmission of information and functionality between web-based systems reflecting the client-server architecture. These APIs primarily supply web application requests and server responses using Hypertext Transfer Protocol (HTTP).

**Below is a simple illustration of how API&#39;s work in Python.**

First we import the modules requests and pprint

Requests is a HTTP library built for humans. It allows us to send http requests with ease.

Then, we create variables to store the content that we get from our APIs.

We use requests to go and get all the information from API URL.

Print the status code to see how the response went.

Print (response.text) returns a nice formatted string.

We use json () as the standard data format to communicate with the API.

In our code below the script is accessing to different API&#39;s and returning json data.

Pprint.print (r.json (&#39;posts&#39;) returns full lists of live posts

And the last line of code returns the url for posts at the zero index.

import requests

import pprint

response = requests.get(&quot;https://randomfox.ca/floof&quot;)

r = requests.get(&quot;https://api.dailysmarty.com/posts&quot;)

print(response.status\_code)

# print(response.text)

fox = response.json()

r.json()

print(fox[&#39;image&#39;])

# pprint.pprint(r.json())

# pprint.pprint(r.json()[&#39;posts&#39;])

# pprint.pprint(r.json()[&#39;posts&#39;][1])

pprint.pprint(r.json()[&#39;posts&#39;][0][&#39;url\_for\_post&#39;])

**WEB HOOKS**

Webhooks are automated messages sent from apps when an event or something happens. They contain a payload message and are sent to a unique URL.

Webhooks offer a way for API&#39;s to communicate events to each other. They are just simple Http message sent from one server to another to signify an event.

Such events are fully customizable and they communicate any type of information e.g.

- A device going offline
- CPU threshold being reached

**Below is a script to send webhooks.**

First we import requests and json modules

We then, define a webhook URL which is going to be our destination url we send our webhook to. For this we use webhook.site.

We also generate the request and create the request object.

The request object then takes data n formats it to json n then sends the data.

Finally, we set our HTTP headers.

This process is basically sending a webhook to a webhook server.

mport requests

import json

# webhook\_url = &#39;https://webhook.site/85e6efbf-8bf9-4d62-9ada-195c768d32f4&#39;

webhook\_url = &#39;http://127.0.0.1:5000/webhook&#39;

data = {

    &#39;name&#39;:&#39;mark macharia&#39;,

    &#39;Channel URL&#39;: &#39;https://studio.youtube.com/channel/UCqBr2bpQAgoVa8-sLwejhgA&#39;,

    &#39;alias&#39;: &#39;Garvey&#39;

}

r = requests.post(webhook\_url, _data_=json.dumps(data), _headers_={&#39;Content-Type&#39;: &#39;application/json&#39;})

Output of above script

&quot;name&quot;: &quot;mark macharia&quot;,

&quot;Channel URL&quot;: &quot;https://studio.youtube.com/channel/UCqBr2bpQAgoVa8-sLwejhgA&quot;,

&quot;alias&quot;: &quot;Garvey&quot;

RECEIVING A WEBHOOK

In order to receive a webhook, we need to create a simple python webserver that listens to webhooks.

First we import flask and its modules.

Set up the app for flask.

Set URL that the server is listening on.

Upon receiving a webhook, it runs the function webhook which checks if it&#39;s a POST method and prints it out. Else, it aborts

We then test our server by sending a webhook with our previous script send webhook.

Finally, we send a POST request, change webhook\_url and point it to our flask server.

Server waits and listens for POST messages.

SERVER.PY script

from flask import Flask, request, abort

app = Flask(\_\_name\_\_)

@app.route(&#39;/webhook&#39;, _methods_=[&#39;POST&#39;])

_def_ webhook():

    if request.method == &#39;POST&#39;:

        print(request.json)

        return &#39;success&#39;, 200

    else:

        abort(400)

if \_\_name\_\_ == &#39;\_\_main\_\_&#39;:

    app.run()

OUTPUT

(Webhooks\_Intel-s2JWkiNw) E:\Webhooks Intel\&gt;python server.py

\* Serving Flask app &quot;server&quot; (lazy loading)

\* Environment: production

WARNING: This is a development server. Do not use it in a production deployment.

Use a production WSGI server instead.

\* Debug mode: off

\* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

**{**

**&#39;name&#39;: &#39;mark macharia&#39;,**

**&#39;Channel URL&#39;: &#39;https: //studio.youtube.com/channel/UCqBr2bpQAgoVa8-sLwejhgA&#39;,**

**&#39;alias&#39;: &#39;Garvey&#39;**

**}**

127.0.0.1 –

The above code output is highlighted in bold.

**Give a walkthrough of how you will manage a data streaming application sending one million notifications every hour while giving examples of technologies and configurations you will use to manage load and asynchronous services. (10 pts.)**

I would use NOSQL databases such as MongoDB since this a data streaming application does a lot of reading and less writing. For my server I would use node.js and express since node is asynchronous in nature. Node.js can be easily integrated with Socket.IO. I would also use Socket. IO with UWS back end. I would recommend using a third party service to handle the many push notifications needed to be sent if cost is not an issue. I would also consider using firebase cloud messaging.

Another example of a good third-party push notification service would be OneSignal. It is able to send many notifications at once. It achieves this by using:

Their dedicated database servers use NVMe SSD. This SSD can reach speeds of 5GB per second and 1,000,000 4K IOPs. With such hardware at their core systems speed is guaranteed.

They use Rust as their programming language for their notification delivery stack. Rust is a fast system programming language with it inbuilt thread safety and segfaults making it handle even demanding workloads.

One signal delivery system is parallelized across 32 threads and sent by an optimized network stack.

Core Technologies I would consider using:

**SOCKET.IO**

Socket.io is a JavaScript library which enables real time bi-directional communication between web servers and clients. It consists of two parts a client-side library which runs on the browser and server-side uses node.js. They share the same type of API. When an event occurs, the server will get it and push it to the appropriate clients.

Socket.io works on any platforms browser or device. It takes care of reliability and speed.

I would use ExpressJS to write the webserver that Socket.IO will work with. Also, it is easier to define routes in ExpressJs.

Socket.io can be used to push messages to your users much faster and easier.

Socket.IO is only fast for moderate applications.

**SCALING SOCKET.IO**

To scale socket.io, I would recommend using **uWebSockets (UWS)** as web socket engine in Socket.io. To achieve more optimization you can use Socket.IO with microservices. In your application make sure Socket.IO uses UWS back end instead of pure JS web sockets.

At a larger scale you can use UWS as the underlying socket library.

UWS Js design is one event loop per thread, isolated and without shared data. NodeJs uses per process while UWS uses per thread. UWS is asynchronous and runs local to one thread. For scaling use individual threads just as Node.Js uses individual processes.

UWS design is similar to express where you can attach callbacks to different URL routes making it easier to build REST/WebSocket services.

Another way to scale is to configure HAProxy to scale socket.io Node.Js applications with SSL. This enables for the load balancing of the socket.io servers. If a client is not connected to the same server a third party link like Redis can be used to store the message from the client then have the socket.io push it to the user once the user is connected.

I would suggest the use of HaProxy for load balancing. Adding more server addresses which Socket.IO runs can solve the problem

The idea is to store the data in a centralized database such as MongoDB or Redis where it can be accessed by all instances of socket.io to read from.

**Give examples of different encryption/hashing methods you have come across (one way and two way) and give example scripts in python 3 on how to achieve each one. (20 pts.)**

**ENCRYPTION/HASHING METHODS**

RIVETT-SHAMIR-ALDEMAN (RSA)

This algorithm is asymmetrical this basically means it uses two keys a public and a private key. The data is encrypted using a public key and decrypted using a private key here you will need to keep the private key a secret.

This type of encryption offers a high level of security since it uses two keys.

RSA uses an asymmetric cipher that uses two keys. The public key is used to encrypt and the private one is used to decrypt.

It is regarded as the most secure encryption algorithm. Its key length is 1024-bit and 2048-bit. The encryption process is slow due to the large key size. Large amounts of data are encrypted slower.

In RSA we sign by:

- Importing the private key
- Hashing our plain text using SHA 256
- Create an object to sign the hashed text
- Write signature and text to a file i.e. signature.pem and text.txt

In RSA we verify by:

- Importing and reading the public key
- Read received message and signature
- Hash the received text
- Compare both hashes
- Verify signature and text
- If they match the message and signature are not modified

The code below signs the message with a private key

from Crypto.PublicKey import RSA

from Crypto.Hash import SHA256

from Crypto.Signature import pkcs1\_15

text = _b_&#39;This message is from me&#39;

#import the private key

key = RSA.import\_key(open(&#39;private.key&#39;).read())

#hash the text

hash = SHA256.new(text)

#sign the hashed text

#create an object we can use to sign the hashed text

signer = pkcs1\_15.new(key)

#my hash signed by private key

signature = signer.sign(hash)

#write signature and text to a file

file\_out = open(&#39;signature.pem&#39;, &#39;wb&#39;)

file\_out.write(signature)

file\_out.close()

file\_out = open(&#39;text.txt&#39;, &#39;wb&#39;)

file\_out.write(text)

file\_out.close()

print (signature.hex())

print(signature)

Printing signature in the above code we get the following scrambled data:

b&#39;\xad\x12\x86\x083{\x8e\xd1\xf0\x847\xba\x9f\x1c\xc07a\*\xb4OR3\x1ao\xeec6\_}\xe0e\xb4\x84\xfc\x03v\xda\x8e\x81\xb5\xac\xd7\xae22!\xe9\x95\xef\xd5nz\xcc\xee\x97\xach\xa3\x10;\x8d\xeekm\x06^\x90\x8b\xe9L\x9e\x1c\xdc\xbaa\x0ft\x94oX\x90R?\xadT\x024p\x9c\xbbu|h\x9di\xdf\xc6x\xcf\x92\x80\xe9m\xc1\xd5!\&lt;\x11\_\x95\xd4\xedV\xd7\x7fC\xc3tz\x85CRX\x01\x13}\x1f;\x90\xc5|a\x0c#\xd0`\xb0\x1a9&quot;n:\xb7\xfd$\xaeM=\xce\xeb\xc0\x93\x07\x9a;\x8c\nl\xe65\xfa\&#39;\xbbh\xc5\xb48\x8d\xfct\x14\xdc\n\xa5u\x9fN\xa1\x15\xf9\x84\x97\xd29hR97n\xf11;:\xfa\x03\x86%w\x9fefV3\x14-\xd0!\xef\&gt;[\x1e\x12pY\x9eX\x156o\x86z\xfe\xe0oB\xd5\xae\xc7\xefkHN\xc8\xc9l\xd0\xa3\x8b\xd5\xc7%\x83lIr\x81\xb1\xa5\x97\xfc\xf3,\xb2\xeb\x9bY&#39;

The code below verifies the text and key:

from Crypto.PublicKey import RSA

from Crypto.Hash import SHA256

from Crypto.Signature import pkcs1\_15

#import and read public key

key = RSA.import\_key(open(&#39;public.key&#39;).read())

# read received message and signature

file\_in = open(&#39;text.txt&#39;, &#39;rb&#39;)

text = file\_in.read()

file\_in.close()

file\_in = open(&#39;signature.pem&#39;, &#39;rb&#39;)

signature = file\_in.read()

file\_in.close()

#compare both hashes

text = SHA256.new(text)

try:

    pkcs1\_15.new(key).verify(text, signature)

    print(&quot;The signature is valid, Message has not been changed.&quot;)

except (_ValueError_, _TypeError_):

    print(&quot;This is not the original message&quot;)

Output of the code is:

The signature is valid, Message has not been changed.

**ADVANCED ENCRYPTION STANDARD (AES)**

The advanced encryption standard uses Rijndael Algorithm. It is a symmetrical form of encryption that uses one key to encrypt and decrypt. Block-ciphers are used and encryption is done one fixed-size block at a time. The key length can be 128-bit, 192-bit and 256-bit. It uses a single private key thus guarantees a high level of security. The encryption was developed by the US National Institute of Standards and Technology.

How it works:

AES uses the following three block-ciphers

- AES-128 uses 128- bit key length for both encryption and decryption
- AES-192 uses 192- bit key length for both encryption and decryption
- AES-256 uses 256- bit key length for both encryption and decryption

The above ciphers encrypts and decrypts data in blocks of 128 bits using cryptographic keys of 128, 192 and 256 bits, respectively.

128-bit key has 10 rounds

192 bit has 12 rounds

256 bit has 14 rounds

A round has steps such as:

- Substitution
- Transposition
- Transformation of plain text to cipher text

AES is fast and secure type of asymmetric encryption.

Asymmetric encryption is basically the type of encryption that uses one key to encrypt and decrypt data.

AES is a 128 bit block cipher with key lengths of 128, 192 and 256.

Plain text goes through a block cipher /algorithm which encrypts it with a key and gives the encrypted cipher text.

An initialization vector (IV) of fixed size input also 128bits is used to randomize the cipher text.

The IV is used to avoid similar text or phrases in your plaintext to be encrypted with similar cipher text

For the decryption the process is reversed you need a key, an IV and the cipher text.

The two Python 3 Scripts below illustrate how AES encryption works.

The first one encrypts the plaintext. The cipher text and IV are written in a cipher \_ file.

from Crypto.Cipher import AES

from Crypto.Util.Padding import pad

# generate key manually

key = _b_&#39;mysecretpassword&#39;

# create the cipher and select mode

cipher = AES.new(key, AES.MODE\_CBC)

plaintext = _b_&quot;This is a classified message for top officials&quot;

ciphertext = cipher.encrypt(pad(plaintext, AES.block\_size))

# print(ciphertext)

#write ciphertext and iv to a file

with open(&#39;cipher\_file&#39;, &#39;wb&#39;) as f:

    f.write(cipher.iv)

    f.write(ciphertext)

OUTPUT of first script:

i.e. on print(ciphertext)

b&#39;\xec\x11\xf6\xd4\xce\xc9R\x95u\x1f\x1f\xf73\xfb`f\xc6\xda\n\x1c\x0c\xb4\x7f\xa9\xa7^n\x1c\*\x0fC\xf06\x11q\x8cO245\xeaE}9~\xe3R\xfd&#39;

The second one decrypts the cipher text.

from Crypto.Cipher import AES

from Crypto.Util.Padding import unpad

# generate key

key = _b_&#39;mysecretpassword&#39;

#open up a cipher\_file file to retrieve the iv and cipher text

with open(&#39;cipher\_file&#39;, &#39;rb&#39;) as c\_file:

    #read the first 16bytes

    iv = c\_file.read(16)

    #pull subsqeuent bytes

    ciphertext = c\_file.read()

#create a cipher to decrypt

#takes key mode and iv

cipher = AES.new(key, AES.MODE\_CBC, iv )

#plaintext is unpadded and decrypted

plaintext = unpad(cipher.decrypt(ciphertext), AES.block\_size)

# print the original message in byte format

print(plaintext)

print(plaintext.decode())

b&#39;This is a classified message for top officials&#39;

This is a classified message for top officials

TRIPLE DATA ENCRYPTION STANDARD (TRIPLEDES)

TripleDES is a symmetrical form of data encryption. It is an advanced form of DES block-cipher. The DES block cipher uses a 56- bit key, while the TripleDES uses the 56-bit key three times making it a 168-bit key. Encryption process involves: encrypts, decrypts and re-encrypts. Decryption process involves: decrypt, encrypt and decrypt again. It is not very secure since encrypts data in shorter block- lengths this makes it easy to decrypt.

It is commonly used to secure UNIX passwords.

TDES has a fixed block size of 8 bytes.

TDES has 3 single DES ciphers where each stage uses a different sub key for encryption.

The TDES key is usually 24 bytes long a combination of all 3 different keys say k1, K2 and k3 to achieve 112 bits of security.

The following modes requires the plain text to be a multiple of 8:

Modes ECB, CBC &amp; OFB.

The Script below illustrates TripleDES process in Python3 using pycryptodome.

from Crypto.Cipher import DES3

from Crypto.Random import get\_random\_bytes

# Raises Value error if the key is not 16 or 24 bytes

#Raises ValueError if the key becomes single DES

while True:

    try:

        key = DES3.adjust\_key\_parity(get\_random\_bytes(24))

        print(key)

        break

    except _ValueError_:

        pass

cipher = DES3.new(key, DES3.MODE\_CFB)

# plain text has to be a multiple of 8

plaintext= _b_&#39;We are no longer the knights who say no!&#39;

# check to see if string is multiple of eight

print(len(plaintext))

# run the encryption cipher

msg = cipher.iv + cipher.encrypt(plaintext)

print(msg)

# run the decryption cipher

cipher\_decrypt = DES3.new(key, DES3.MODE\_CFB)

original\_text = cipher.iv + cipher\_decrypt.decrypt(msg)

print(original\_text)

# re\_encrypt again

re\_encrypted\_text = cipher.iv + cipher.encrypt(original\_text)

print(re\_encrypted\_text)

Output of the above script:

b&#39;y\xba\x07J\xbca\x0b\x91\x15\xbcb\x91\xcb\x15^\x19\xe9\xc7\xf2vCp4\&gt;&#39;

40

b&#39;\xc8\xbe.T\xef\x96\xe6$\xd7\xabZ@S\xacl,T;%)m\xfeR\xf1\xfcO\xdf\x9d[\x1c\x89:o\xd4\x14O\x95\xffY\xddE\x8c\xedT\xf6,\xd3\xe7&#39;

b&#39;\xc8\xbe.T\xef\x96\xe6$a`\xf2I\x95H\xe2\xc7We are no longer the knights who say no!&#39;

b&quot;\xc8\xbe.T\xef\x96\xe6$z\x10&#39;z\xde\xd3/u);\xdc\x1d\x85\xab\x116Z\xdf\xd6#S\x9b\xdf\xc3\x99g+\x10\xdd\x1aY\xa3\xbc\xe8Z\xca\*\xe7^\xa6\xef\\-.\x15\x1c\x88-\xe7S\xf8\xd39k\xdd\xa6&quot;

HASHING

A hash function is a one way encryption using an algorithm and no key. Python standard library has module hashlib used for this purposes. Hashlib supports the following algorithms: SHA1, SHA224, SHA256, SHA384, SHA512 AND MD5.

Hashes are used for storing the hash of a password, they can also be used to hash a file. The hashed file and then are then sent separately. The receiver of the file then runs a hash on the sent file to see if it is similar to the hash that was sent.

**MD5 ENCRYPTION**

MD5 hashing is generating an md5 hash from a string

It is a type of encryption where a hash is generated from a given string.

It is a form of a one way encryption

To decrypt md5 you have to match the hash with the original string.

The following script is a simple example on how to implement md5 hashing in python 3 using the hashlib module:

import hashlib

# create an instance of an md5 object

md5hash = hashlib.md5()

#convert to byte string since md5 only uses byte string

md5hash.update(_b_&#39;This is the string to be hashed&#39;)

#to obtain the hash we call the digest method

print(md5hash.digest())

#to get the hex digest call the hex digest method

print(md5hash.hexdigest())

The output of the above code snippet is shown below:

digest output:

b&#39;\xb2\xba-\xca]\xd2\xaej\x18\xbb?r\xec\x1b\x93\x89&#39;

hexdigest output:

b2ba2dca5dd2ae6a18bb3f72ec1b9389

SECURE HASH ALGORITHMS (SHA)

These algorithms are a group of cryptographic hash functions.

Cryptographic hash functions produce irreversible and unique hashes.

SHA1 uses a 160 bit hash function.

SHA2 has two hash functions that are the same but with different block size. They include SHA256 AND SHA512.

SHA256 uses 32 byte words

SHA515 uses 64 byte words

The below code snippet illustrate how to use python 3 module hashlib to implement SHA.

import hashlib

#create a hash instance &amp; call the hex digest method

sha = hashlib.sha1(_b_&#39;This is secure hash algorithm&#39;).hexdigest()

sha256 = hashlib.sha256(_b_&#39;This is secure hash algorithm&#39;).hexdigest()

sha512 = hashlib.sha512(_b_&#39;This is secure hash algorithm&#39;).hexdigest()

print(sha)

print(sha256)

print(sha512)

Output of the above code in hex digest form is:

6a646db4deb95812414a6c54242b72291bb02d90

d5120b8d0a74b5ddea4622f28c6cf38fad48e4c075462d9c919fe577a7e70802

778b1fa9868d769fb0fe46b334032585437ceae1d58944bde4119566caee34c83384aab6c60e33deaee4bb096f0b75a353d9252f1d8a226e73e7cd4e99c93a67

1. **Create a login and a success page in Django. A mockup of the created pages should also be submitted. The mockups should have been created by using advanced design/wireframe tools thus showcasing prowess in usage of the tools and use of production server deployments on uwsgi/nginx. Ensure that the sessions are well and securely managed.(60 pts.)**

Django is a high level Python Web framework that is free and open source. It used for rapid development to get web apps up and running really quickly.

Django uses a model-view-template (MTV) design pattern.

Model: Data Access Layer: interacts, relates and validates the data

Template: Presentation Layer: Presentation

Views: Business Logic Layer: Access the model and displays the appropriate template.

Django is:

Fully featured: it offers user authentication and administration.

Secure: Protects against sql injection cross site scripting and forgery

Scalable: Handles lots of traffic

Login and Success page in django:

Create project folder and use pipenv to create our virtual environment

Pipenv creates virtual environment and handles dependencies in the pip file and pip lock file.

We then install django using

```pipenv install -r ./reqs.txt

```

Each project/ website has separate apps for our project we have accounts and or separate app is called register\_app.

```django-admin start project accounts

```

Change directory into accounts using:

```cd accounts

```

```Python manage.py startapp register\_app

```

Run migrate, create super user and run server to start the development server.

```python manage.py migrate

```

```python manage.py createsuperuser

```

```python manage.py run server

```

Inside register\_app create templates folder and then create a folder which matches the name of the app.

In the templates folder I created login.html register.html and index.html.

Update urls

from django.contrib import admin

from django.urls import path , include

# from django.conf import settings

# from django.conf.urls.static import static

urlpatterns = [

    path(&#39;admin/&#39;, admin.site.urls),

    path(&#39;&#39;, include(&#39;register\_app.urls&#39;))

]

Create our models.py

from django.db import models

# Create your models here.

_class_ Customer(_models_._Model_):

    name = models.CharField(_max\_length_=200, _null_=True)

    phone = models.CharField(_max\_length_=200, _null_=True)

    email = models.CharField(_max\_length_=200, _null_=True)

    date\_created = models.DateTimeField(_auto\_now\_add_=True, _null_=True)

    _def_ \_\_str\_\_(_self_):

        return self.name

We then define our views.py:

from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.forms import inlineformset\_factory

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login\_required

# Create your views here.

from .models import \*

from .forms import CreateUserForm

_def_ registerPage(_request_):

    if request.user.is\_authenticated:

        return redirect(&#39;home&#39;)

    else:

        form = CreateUserForm()

        if request.method == &#39;POST&#39;:

            form = CreateUserForm(request.POST)

            if form.is\_valid():

                form.save()

                user = form.cleaned\_data.get(&#39;username&#39;)

                messages.success(request, &#39;Account has been created for &#39; + user)

                return redirect(&#39;login&#39;)

    # pass it in to our template and render it

    context = {&#39;form&#39;:form}

    # pass the name of the template to render

    return render(request, &#39;register\_app/register.html&#39;, context)

_def_ loginPage(_request_):

    if request.user.is\_authenticated:

        return redirect(&#39;home&#39;)

    else:

        if request.method == &#39;POST&#39;:

            username = request.POST.get(&#39;username&#39;)

            password = request.POST.get(&#39;password&#39;)

            user = authenticate(request, _username_=username, _password_=password)

            if user is not None:

                login(request, user)

                return redirect(&#39;home&#39;)

            else:

                messages.info(request, &#39;Username OR Password is incorrect&#39;)

        context= {}

        return render(request, &#39;register\_app/login.html&#39;, context)

_def_ logoutUser(_request_):

    logout(request)

    return redirect(&#39;login&#39;)

@login\_required(_login\_url_=&#39;login&#39;)

_def_ home(_request_):

    context = {}

    return render(request, &#39;register\_app/index.html&#39;, context)

_View registerPage:_

If the user is authenticated redirect back to home also this function is used

to validate and save the data.

# pass the name of the template to render

    return render(request, &#39;register\_app/register.html&#39;, context)

_Views .loginPage_

If the user is authenticated redirect back to home.

If method is POST then get username and password

Authenticate the users.

_View logout_

Logout the user

Log out the user and redirect him to login page.

_Views home_

To access home page one must login

This views render our html files.

CSRF TOKEN

We then put csrf tokens into our forms so when we submit our data django is able to handle it.

We also have to create a static folder to hold our css, js and media. We make sure to edit the settings.py file to support and serve the static file as shown in the code below:

# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC\_URL = &#39;/static/&#39;

MEDIA\_URL = &#39;/images/&#39;

STATIC\_ROOT = os.path.join(os.path.dirname(BASE\_DIR), &quot;static&quot;, &quot;css&quot; , &quot;js&quot;)

MEDIA\_ROOT = os.path.join(os.path.dirname(BASE\_DIR), &quot;static&quot;, &quot;images&quot;)

STATICFILES\_DIRS = [

    os.path.join(BASE\_DIR, &#39;static&#39;)

]

Load the static files in your desired html files eg: I have used bootstrap 4 to customize the project

{% load static %}

    \&lt;link rel=&quot;stylesheet&quot; href=&quot;{% static &#39;css/bootstrap.min.css&#39; %}&quot;\&gt;

For templates we have 3 html files

One for creating users, another for login and a home page

Index.html for home page:

{% block content %}

{% load static %}

\&lt;style\&gt;

  .hello-msg{

    _font-size_: 18px;

    _color_: #fff;

    _margin-right_: 20px;

  }

\&lt;/style\&gt;

\&lt;link rel=&quot;stylesheet&quot; href=&quot;{% static &#39;css/bootstrap.min.css&#39; %}&quot;\&gt;

\&lt;nav class=&quot;navbar navbar-expand-lg navbar-dark bg-dark&quot;\&gt;

 \&lt;img src=&quot;{% static &#39;images/logo1.png&#39; %}&quot;\&gt;

  \&lt;button class=&quot;navbar-toggler&quot; type=&quot;button&quot; data-toggle=&quot;collapse&quot; data-target=&quot;#navbarNav&quot; aria-controls=&quot;navbarNav&quot; aria-expanded=&quot;false&quot; aria-label=&quot;Toggle navigation&quot;\&gt;

    \&lt;span class=&quot;navbar-toggler-icon&quot;\&gt;\&lt;/span\&gt;

  \&lt;/button\&gt;

  \&lt;div class=&quot;collapse navbar-collapse&quot; id=&quot;navbarNav&quot;\&gt;

    \&lt;ul class=&quot;navbar-nav&quot;\&gt;

      \&lt;li class=&quot;nav-item active&quot;\&gt;

        \&lt;a class=&quot;nav-link&quot; href=&quot;{% url &#39;home&#39; %}&quot;\&gt;Home\&lt;/a\&gt;

      \&lt;/li\&gt;

    \&lt;/ul\&gt;

  \&lt;/div\&gt;

  \&lt;span class=&quot;hello-msg&quot;\&gt;Hello, {{request.user}}\&lt;/span\&gt;

  \&lt;span \&gt;\&lt;a  class=&quot;hello-msg&quot; href=&quot;{% url &#39;logout&#39; %}&quot;\&gt;Logout\&lt;/a\&gt;\&lt;/span\&gt;

\&lt;/nav\&gt;

\&lt;br\&gt;

    \&lt;div class=&quot;container&quot; align=&quot;center&quot; background=&quot;#efefef&quot;\&gt;

        \&lt;h2\&gt;Welcome to GeeHub \&lt;/h2\&gt;

        \&lt;h4\&gt;Sign Up for more offers\&lt;/h4\&gt;

        \&lt;div class=&quot;mt-4&quot;\&gt;

            \&lt;div class=&quot;d-flex justify-content-center links&quot;\&gt;

                Don&#39;t have an account? \&lt;a href=&quot;{% url &#39;register&#39; %}&quot; class=&quot;ml-2&quot;\&gt;Sign Up\&lt;/a\&gt;

            \&lt;/div\&gt;

        \&lt;/div\&gt;

    \&lt;/div\&gt;

{% endblock %}

URL Patterns for register\_apps:

from django.urls import path

from . import views

urlpatterns = [

    path(&#39;register/&#39; , views.registerPage, _name_=&#39;register&#39;),

    path(&#39;login/&#39; , views.loginPage, _name_=&#39;login&#39;),

    path(&#39;&#39;, views.home, _name_=&#39;home&#39;),

    path(&#39;logout/&#39; , views.logoutUser, _name_=&#39;logout&#39;),

]

The above project creates a user logs him in and out and gives authentication, and profile name in the home page. When you login successfully you are redirected to the homepage.

**5. Create a search and results page using Django and postgreSQL database. The Django application should be deployed on uwsgi/nginx webserver and NOT the development server. This should also be deployed on a red-hat based Linux environment or an alpine docker image container. (60 pts.)**

Full text search using Postgres

We create a search form using Django forms to take advantage of the built in security.

- Search Options
- Basic filters
- Q objects
- Full text search with postgres

Full text search satisfies a query and sorts by relevance

**Full text Search Features**

Rankings

Indexing

Phrase search

Stop words

Stemming

INDEXING

Indexing is good for performance. If you have a million rows in your database, doing a filter on that would be very slow. With indexing you can preprocess your search then create indexes.

If the data is static use a gin if its dynamic use a gist.

**Stop Words**

Strip words with no meaning.

**Stemming**

Reduce a word to its base step. Stemming is a built in algorithm

**How does Full text Search work?**

It preprocesses the search

Turns document to token then to lexemes.

Indexing is then used for optimization purposes.

**POSTGRESQL DATA TYPES**

Tsvector this are preprocessed documents.

Tsquery this are preprocessed queries

**Django Contrib Postgres Search**

They are five classes built-in django that link with postgres this include

SearchVector: searches multiple fields

SearchQuery: adds stemming and / or stop words.

SearchRank: apply rank to result of document.

WeightedQueries: add weight

SearchVectorField: enhances performance upgrade with manual triggers.

**Django Code**

**For models.py we have:**

from django.db import models

from django.contrib.postgres.search import SearchVectorField, SearchVector

# Create your models here.

_class_ Car(_models_._Model_):

    name = models.CharField(_max\_length_=255)

    brand = models.CharField(_max\_length_=255)

    search = SearchVectorField(_null_=True)

    _def_ \_\_str\_\_(_self_):

        return self.name

Car.objects.all().update(_search_=SearchVector(&#39;name&#39;))

**For Views.py we have:**

# from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, FormView

from .forms import SearchForm

from django.contrib.postgres.search import SearchVector

from .models import Car

_class_ HomePageView(_FormView_):

    template\_name = &#39;home.html&#39;

    form\_class = SearchForm

_class_ SearchResultsView(_ListView_):

    model = Car

    template\_name = &#39;search\_results.html&#39;

    _def_ get\_queryset(_self_):

        query = self.request.GET.get(&#39;q&#39;)

        object\_list = Car.objects.annotate(

            _search1_ = SearchVector(&#39;name&#39;, &#39;brand&#39;),

        ).filter(_search1_=query)

        return object\_list

**For templates we have home.html and searchresults html**

\&lt;h1\&gt;Home Page\&lt;/h1\&gt;

{% block content %}

{% load static %}

\&lt;link rel=&quot;stylesheet&quot; href=&quot;{% static &#39;css/bootstrap.min.css&#39; %}&quot;\&gt;

\&lt;div class=&quot;jumbotron&quot;\&gt;

    \&lt;form action=&quot;{% url &#39;search\_results&#39; %}&quot; method=&quot;get&quot; class=&quot;form-inline my-2 my-lg-0&quot;\&gt;

        {{form}}

    \&lt;/form\&gt;

\&lt;/div\&gt;

{% endblock %}

\&lt;h1\&gt;Search Results\&lt;/h1\&gt;

{% block content %}

{% load static %}

\&lt;link rel=&quot;stylesheet&quot; href=&quot;{% static &#39;css/bootstrap.min.css&#39; %}&quot;\&gt;

\&lt;ul class=&quot;list-group&quot;\&gt;

  {% for car in object\_list %}

    \&lt;li class=&quot;list-group-item&quot;\&gt;

      {{ car.name }}, {{ car.brand }}

    \&lt;/li\&gt;

  {% endfor %}

\&lt;/ul\&gt;

{% endblock %}

**For settings.py we have:**

&quot;&quot;&quot;

Django settings for Search project.

Generated by &#39;django-admin startproject&#39; using Django 3.1.5.

For more information on this file, see

https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see

https://docs.djangoproject.com/en/3.1/ref/settings/

&quot;&quot;&quot;

import os

from pathlib import Path

# Build paths inside the project like this: BASE\_DIR / &#39;subdir&#39;.

# BASE\_DIR = Path(\_\_file\_\_).resolve().parent.parent

BASE\_DIR = os.path.dirname(os.path.dirname(os.path.abspath(\_\_file\_\_)))

# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET\_KEY = &#39;dseay%pgm!7n%##k1j+scaiku\*n$(slwhw2z@\_$t6o49wab7ok&#39;

# SECURITY WARNING: don&#39;t run with debug turned on in production!

DEBUG = True

ALLOWED\_HOSTS = []

# Application definition

INSTALLED\_APPS = [

    &#39;django.contrib.admin&#39;,

    &#39;django.contrib.auth&#39;,

    &#39;django.contrib.contenttypes&#39;,

    &#39;django.contrib.sessions&#39;,

    &#39;django.contrib.messages&#39;,

    &#39;django.contrib.staticfiles&#39;,

    &#39;django.contrib.postgres&#39;,

    &#39;search\_app&#39;

]

MIDDLEWARE = [

    &#39;django.middleware.security.SecurityMiddleware&#39;,

    &#39;django.contrib.sessions.middleware.SessionMiddleware&#39;,

    &#39;django.middleware.common.CommonMiddleware&#39;,

    &#39;django.middleware.csrf.CsrfViewMiddleware&#39;,

    &#39;django.contrib.auth.middleware.AuthenticationMiddleware&#39;,

    &#39;django.contrib.messages.middleware.MessageMiddleware&#39;,

    &#39;django.middleware.clickjacking.XFrameOptionsMiddleware&#39;,

]

ROOT\_URLCONF = &#39;Search.urls&#39;

TEMPLATES = [

    {

        &#39;BACKEND&#39;: &#39;django.template.backends.django.DjangoTemplates&#39;,

        # &#39;DIRS&#39;: [str(BASE\_DIR.joinpath(&#39;search\_app/templates&#39;))],

        # &#39;DIRS&#39;: [

        #     os.path.join(BASE\_DIR, &#39;templates&#39;),

        # ],

        &#39;DIRS&#39;: [os.path.join(BASE\_DIR, &#39;templates&#39;)],

        &#39;APP\_DIRS&#39;: True,

        &#39;OPTIONS&#39;: {

            &#39;context\_processors&#39;: [

                &#39;django.template.context\_processors.debug&#39;,

                &#39;django.template.context\_processors.request&#39;,

                &#39;django.contrib.auth.context\_processors.auth&#39;,

                &#39;django.contrib.messages.context\_processors.messages&#39;,

            ],

        },

    },

]

WSGI\_APPLICATION = &#39;Search.wsgi.application&#39;

# Database

# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {

    &#39;default&#39;: {

        &#39;ENGINE&#39;: &#39;django.db.backends.postgresql&#39;,

        &#39;NAME&#39;: &#39;postgres&#39;,

        &#39;USER&#39;: &#39;postgres&#39;,

        &#39;PASSWORD&#39;: &#39;Kernsys#4&#39;,

        &#39;HOST&#39;: &#39;localhost&#39;,

        &#39;PORT&#39;: &#39;5432&#39;,

    }

}

# Password validation

# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH\_PASSWORD\_VALIDATORS = [

    {

        &#39;NAME&#39;: &#39;django.contrib.auth.password\_validation.UserAttributeSimilarityValidator&#39;,

    },

    {

        &#39;NAME&#39;: &#39;django.contrib.auth.password\_validation.MinimumLengthValidator&#39;,

    },

    {

        &#39;NAME&#39;: &#39;django.contrib.auth.password\_validation.CommonPasswordValidator&#39;,

    },

    {

        &#39;NAME&#39;: &#39;django.contrib.auth.password\_validation.NumericPasswordValidator&#39;,

    },

]

# Internationalization

# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE\_CODE = &#39;en-us&#39;

TIME\_ZONE = &#39;UTC&#39;

USE\_I18N = True

USE\_L10N = True

USE\_TZ = True

# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC\_URL = &#39;/static/&#39;

EDIA\_URL = &#39;/images/&#39;

STATIC\_ROOT = os.path.join(os.path.dirname(BASE\_DIR), &quot;static&quot;, &quot;css&quot; , &quot;js&quot;)

MEDIA\_ROOT = os.path.join(os.path.dirname(BASE\_DIR), &quot;static&quot;, &quot;images&quot;)

STATICFILES\_DIRS = [

    os.path.join(BASE\_DIR, &#39;static&#39;)

]