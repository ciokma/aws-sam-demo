import json
import requests
# import requests


def lambda_handler(event, context):
    print("evento", event)
  
    
    country= "nicaragua"
    if("country" in event):
        country = event["country"]
    # api-endpoint
    URL = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    print(URL)
    # sending get request
    data = requests.get(url = URL).json()
    capital = "Not Found"
    try:
        #print(data)
        #Get request status
        if("status" in data):
            if (data["status"]== 404):
                print("Country not Found, please try again.")
            else:
                print("No Data")
        else:
            # showing capital
            print(data[0]["capital"][0])
            capital = data[0]["capital"][0]

    except requests.RequestException as e:
         # Send some context about this error to Lambda Logs
         print(e)

         raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello, for this country '{country}' this is the capital name '{capital}'",
            # "location": ip.text.replace("\n", "")
        }),
    }
