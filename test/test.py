import requests

#resp = requests.post("https://getprediction-tqc5taiqdq-lm.a.run.app", files={'file': open('eight.png', 'rb')})

q =  { "question": "Which college John Sister Goes" } 
print (q)
resp = requests.post("http://127.0.0.1:5000", json = q)
#resp =requests.post("https://bertqa-5aorr5lmzq-wl.a.run.app", json=q)
print(resp)
if resp.status_code == 200 :
    print(resp.json()['answer'] )
else :
    print (resp.status_code)



# q =  { "question": question} 
#         resp =requests.post("https://bertqa-5aorr5lmzq-wl.a.run.app", json=q)
#         if resp.status_code == 200 :
#             result = resp.json()['answer'] 
#         else :
#             result = str (resp.status_code))
#         return {"fulfillmentText": result}