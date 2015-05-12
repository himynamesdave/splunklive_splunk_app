#add your custom response handler class to this module
import json
import datetime

#the default handler , does nothing , just passes the raw output directly to STDOUT
class DefaultResponseHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        cookies = response_object.cookies
        if cookies:
            req_args["cookies"] = cookies        
        print_xml_stream(raw_response_output)
          
#template
class MyResponseHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):        
        print_xml_stream("foobar")

'''various example handlers follow'''
        
class BoxEventHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        if response_type == "json":        
            output = json.loads(raw_response_output)
            if not "params" in req_args:
                req_args["params"] = {}
            if "next_stream_position" in output:    
                req_args["params"]["stream_position"] = output["next_stream_position"]
            for entry in output["entries"]:
                print_xml_stream(json.dumps(entry))   
        else:
            print_xml_stream(raw_response_output)  

class QualysGuardActivityLog:
    '''Response handler for QualysGuard activity log.'''

    def __init__(self,**args):
        pass

    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        if not "params" in req_args:
            req_args["params"] = {}
        date_from = (datetime.datetime.now() - datetime.timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        req_args["params"]["date_from"] = date_from
        print_xml_stream(raw_response_output) 
                          
class FourSquareCheckinsEventHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        if response_type == "json":        
            output = json.loads(raw_response_output)
            last_created_at = 0
            for checkin in output["response"]["checkins"]["items"]:
                print_xml_stream(json.dumps(checkin)) 
                if "createdAt" in checkin:
                    created_at = checkin["createdAt"]
                    if created_at > last_created_at:
                        last_created_at = created_at
            if not "params" in req_args:
                req_args["params"] = {}
            
            req_args["params"]["afterTimestamp"] = last_created_at
                      
        else:
            print_xml_stream(raw_response_output) 
            
class ThingWorxTagHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        if response_type == "json":        
            output = json.loads(raw_response_output)
            for row in output["rows"]:
                print_xml_stream(json.dumps(row))                      
        else:
            print_xml_stream(raw_response_output) 
            
class FireEyeEventHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        if response_type == "json":        
            output = json.loads(response_object.content)
            last_display_id = -1
            for alert in output["alerts"]:
                print_xml_stream(json.dumps(alert))  
                if "displayId" in alert:
                    display_id = alert["displayId"]
                    if display_id > last_display_id:
                        last_display_id = display_id
            if not "params" in req_args:
                req_args["params"] = {}
            
            if last_display_id > -1:
                req_args["params"]["offset"] = last_display_id

        else:
            print_xml_stream(raw_response_output) 
              
          
class BugsenseErrorsEventHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        if response_type == "json":        
            output = json.loads(raw_response_output)
            
            for error in output["data"]:
                print_xml_stream(json.dumps(error))   
        else:
            print_xml_stream(raw_response_output)

class MyCustomHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        
        req_args["data"] = 'What does the fox say'   
         
        print_xml_stream(raw_response_output)
                               

class TwitterEventHandler:

    def __init__(self,**args):
        pass

    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):       
            
        if response_type == "json":        
            output = json.loads(raw_response_output)
            last_tweet_indexed_id = 0
            for twitter_event in output["statuses"]:
                print_xml_stream(json.dumps(twitter_event))
                if "id_str" in twitter_event:
                    tweet_id = twitter_event["id_str"]
                    if tweet_id > last_tweet_indexed_id:
                        last_tweet_indexed_id = tweet_id
            
            if not "params" in req_args:
                req_args["params"] = {}
            
            req_args["params"]["since_id"] = last_tweet_indexed_id
                       
        else:
            print_xml_stream(raw_response_output)

class InstagramFollowedByEventHandler:
    
    def __init__(self,**args):
        pass
    
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):       
        
    	if response_type == "json":        
            output = json.loads(raw_response_output)
            last_indexed_id = 0
           
            for instagram_event in output["data"]:
                print_xml_stream(json.dumps(instagram_event))
            
            if not "params" in req_args:
                req_args["params"] = {}
            
            next_cursor = 0
            if "next_cursor" in output["pagination"]:
                next_cursor = output["pagination"]["next_cursor"]
                req_args["params"]["cursor"] = next_cursor
            else:
            	if 'cursor' in req_args["params"]: del req_args["params"]['cursor']
                       
        else:
            print_xml_stream(raw_response_output)

class InstagramTagEventHandler:
    
    def __init__(self,**args):
        pass
    
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):       
        
    	if response_type == "json":        
            output = json.loads(raw_response_output)
            
            for instagram_event in output["data"]:
                print_xml_stream(json.dumps(instagram_event))
            
            if not "params" in req_args:
                req_args["params"] = {}
            
            next_cursor = 0
            if "next_max_tag_id" in output["pagination"]:
                next_cursor = output["pagination"]["next_max_tag_id"]
                req_args["params"]["max_tag_id"] = next_cursor
            else:
            	if 'max_tag_id' in req_args["params"]: del req_args["params"]['max_tag_id']
            
            #req_args["params"]["max_tag_id"] = next_cursor
                       
        else:
            print_xml_stream(raw_response_output)

class InstagramUserFeedEventHandler:
    
    def __init__(self,**args):
        pass
    
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):       
        
    	if response_type == "json":        
            output = json.loads(raw_response_output)
            
            for instagram_event in output["data"]:
                print_xml_stream(json.dumps(instagram_event))
            
            if not "params" in req_args:
                req_args["params"] = {}
                
            next_cursor = 0
            if "next_max_id" in output["pagination"]:
                next_cursor = output["pagination"]["next_max_id"]
                req_args["params"]["max_id"] = next_cursor
            else:
            	if 'max_id' in req_args["params"]: 
            		del req_args["params"]['max_id']
            		req_args["params"]["min_timestamp"] = int(time.time())
                        
        else:
            print_xml_stream(raw_response_output)

class JSONArrayHandler:

    def __init__(self,**args):
        pass

    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        if response_type == "json":
            output = json.loads(raw_response_output)

            for entry in output:
                print_xml_stream(json.dumps(entry))
        else:
            print_xml_stream(raw_response_output)
                                      
                                                                             
#HELPER FUNCTIONS
    
# prints XML stream
def print_xml_stream(s):
    print "<stream><event unbroken=\"1\"><data>%s</data><done/></event></stream>" % encodeXMLText(s)



def encodeXMLText(text):
    text = text.replace("&", "&amp;")
    text = text.replace("\"", "&quot;")
    text = text.replace("'", "&apos;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace("\n", "")
    return text