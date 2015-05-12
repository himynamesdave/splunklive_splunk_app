#Splunk>live! App

##Overview:

![SplunkLive App Twitter](https://raw.githubusercontent.com/himynamesdave/splunklive_splunk_app/master/static/screenshot-twitter.jpeg)

![SplunkLive App Instagram](https://raw.githubusercontent.com/himynamesdave/splunklive_splunk_app/master/static/screenshot-instagram.jpeg)

An app that visualises Tweets / Instagram images containing #splunklive & #splunk.

##Instructions:

**Get the app**

Download and install the Splunk>live! App (https://github.com/himynamesdave/splunklive_splunk_app/raw/master/splunklive_splunk_app.tar.gz) onto your Splunk Instance.

**Install the "REST API Modular Input app**

Copy the folder SPLUNK HOME/etc/apps/instagram/install/rest_ta to SPLUNK HOME/etc/apps/

This will install the official REST API modular input created by Damien Dallimore that is used for connecting to the Instagram API. This version of rest_ta includes some custom python response handlers to handle the Instagram API json format. These are not included in the REST API Modular input app that can be found on Splunkbase. 

##Configure Twitter Feed

**Get your Twitter API keys**

[Instructions on how to do this here: steps 1-2](http://blogs.splunk.com/2014/07/03/splunking-social-media-tracking-tweets/).

**Add your Twitter API kets to the to the "SplunkLiveTwitterFeed" REST input**

To do this navigate to Settings > Data Inputs > REST > "SplunkLiveTwitterFeed".

Replace the missing API keys with the ones you have just generated during step 2, then hit "save". Note: you can also change the tweets collected on this page. By default the app will track all tweets with the hashtag #splunklive. If you want to change the hashtag, or add others, simply change the URL arguments field.

e.g:
URL Arguments: track=#splunk,#bigdata,#mytag^stall_warnings=true

**Enable input**

To do this navigate to Settings > Data Inputs > REST. For the "SplunkLiveTwitterFeed" select "Enable".

##Configure Instagram Feed

**Get an account**

[Create a developer account with Instagram](https://instagram.com/developer).

**Create an app**

[Register a client to obtain your Instagram Client ID and Client Secret](https://instagram.com/developer/clients/register/).

For website and redirect URL you can set: www.splunk.com

The Splunk app for Instagram uses implicit authentication so you have to un-check the checkbox "Disable implicit Oauth" (under security tab).

**Obtain your Instagram Access Token**

The entire process is described on this page](https://instagram.com/developer/authentication/)

As we are using implicit authentication you can skip to the section called "Client-Side (implicit) authentication" which is described below under 3.1 and 3.2.

In a browser paste the following URL, with CLIENT-ID and REDIRECT-URI replaced with the values created earlier (4b):

https://instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=token

At this point, you are presented with a login screen and then a confirmation screen where you will approve your app’s access to your Instagram data. Note, that unlike the explicit flow the response type here is "token".

**Receive the access_token from the URL**

Once you have authenticated and then authorized your application, we’ll redirect them to your redirect_uri with the access_token now in the url. It’ll look like so:
http://your-redirect-uri#access_token=ACCESS-TOKEN

Simply copy the access_token off the URL token.

**Edit input**

Add your Instagram API kets to the to the "SplunkInstagramFeed" and "SplunkInstagramFeed" REST input. To do this navigate to Settings > Data Inputs > REST > "SplunkInstagramFeed" / "SplunkInstagramFeed".

Replace the access token, client ID and client secret for these Instagram REST Inputs with those just created.

**Enable inputs**

To do this navigate to Settings > Data Inputs > REST. For the "SplunkInstagramFeed" / "SplunkInstagramFeed" select "Enable".

##Final (important) step

5. Restart Splunk.

6. Profit.

##Top tip:

Do all these steps 2 hours before the event begins to allow the index to populate with some tweets and images.

##Say hi (or help!):

dgreenwood@splunk.com

p.s You can contribute to this app here: https://github.com/himynamesdave/splunklive_splunk_app
