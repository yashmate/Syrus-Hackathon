import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'subject#': "1",   
                            'age': "72",   
                            'sex': "0",   
                            'test_time': "5.6431",   
                            'motor_UPDRS': "28.199",   
                            'Jitter(%)': "0.00662",   
                            'Jitter(Abs)': "0.0000338",   
                            'Jitter:RAP': "0.00401",   
                            'Jitter:PPQ5': "0.00317",   
                            'Jitter:DDP': "0.01204",   
                            'Shimmer': "0.02565",   
                            'Shimmer(dB)': "0.23",   
                            'Shimmer:APQ3': "0.01438",   
                            'Shimmer:APQ5': "0.01309",   
                            'Shimmer:APQ11': "0.01662",   
                            'Shimmer:DDA': "0.04314",   
                            'NHR': "0.01429",   
                            'HNR': "21.64",   
                            'RPDE': "0.41888",   
                            'DFA': "0.54842",   
                            'PPE': "0.16006",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/ec96a2014fd441a7b2f4efae6886a43b/services/5d8024e7ce964c2fa4530d3fd6836472/execute?api-version=2.0&format=swagger'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'subject#': "1",   
                            'age': "72",   
                            'sex': "0",   
                            'test_time': "5.6431",   
                            'motor_UPDRS': "28.199",   
                            'Jitter(%)': "0.00662",   
                            'Jitter(Abs)': "0.0000338",   
                            'Jitter:RAP': "0.00401",   
                            'Jitter:PPQ5': "0.00317",   
                            'Jitter:DDP': "0.01204",   
                            'Shimmer': "0.02565",   
                            'Shimmer(dB)': "0.23",   
                            'Shimmer:APQ3': "0.01438",   
                            'Shimmer:APQ5': "0.01309",   
                            'Shimmer:APQ11': "0.01662",   
                            'Shimmer:DDA': "0.04314",   
                            'NHR': "0.01429",   
                            'HNR': "21.64",   
                            'RPDE': "0.41888",   
                            'DFA': "0.54842",   
                            'PPE': "0.16006",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/ec96a2014fd441a7b2f4efae6886a43b/services/5d8024e7ce964c2fa4530d3fd6836472/execute?api-version=2.0&format=swagger'
api_key = 'DoxtMjzLEOCjv9XmZUk4rXJ2porO/s28OHOdotADua/3GgxYD7DJxOcHnXI8J8krDe1OWJKaqW2K7iWuW04ZIQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
