Splunk>live App
===

Overview:
---

An app that visualises tweets containing #splunklive.

Instructions:
---

1. Download and install the Splunk REST API Modular Input (https://splunkbase.splunk.com/app/1546/) onto your Splunk Instance.

2. Get your own Twitter API keys to start collecting tweets. To do this follow steps 1 & 2 here: http://blogs.splunk.com/2014/07/03/splunking-social-media-tracking-tweets/

3. Navigate to Settings > Data Inputs > REST > SplunkLiveTwitterFeed. Replace the missing API keys with the ones you have just generated during step 2, then hit "save". Now select "enable".

4. Restart Splunk.

5. Profit.

More info:
---

Ideally do all these steps 2 hours before the event begins to allow the index to populate with some tweets.

There is one dashboard #SplunkLive Twitter Stream. This is automatically configured to only show tweets for "today". You do not need to play around with the searches, but you can if you choose too :)

Say hi (or help!):
---

dgreenwood@splunk.com

p.s You can contribute to this app here: https://github.com/himynamesdave/splunklive_splunk_app