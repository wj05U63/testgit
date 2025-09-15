import requests
import time
import json

url="http://47.100.49.19:8080/flexofficeall/api/w/baseSetController/editSaveSign"
token = "eyJhbGciOiJIUzUxMiIsInppcCI6IkRFRiJ9.eNqMj8FOxCAQhl_FcF4SGGgLezPxYqLGgy8ADDSsa2kotWuM7-509eDRhMPwzTd_Zj7ZqWV2ZBis9YMFHrxFrjsjuXVgeN8JpZTXQVnDDmxZPckQrHJeBAsWVQ9KSKoSKNDeg_OOxLwsJKZzvHi3RN7Ka5z4Eut7rHvXNXaUQzcIo8QgDixe5h8gpTQ7CKXO90gRgvQwPbm3SJ_NTeOJwLmMeXr5mHc2b0hkpezbEMo6tT9eynVpzxs-FswpR7xzbR8BAR2XgktzI-xR0VMkl5RyiA97NDmtrvE397rHP24udbyqUXbKJO3pNqd1Hx1aCIAag0T0AtjXNwAAAP__.f2hTs5lplPg995x4Jq1Bb90k82l0wlmI9MiJEelJIlzKb0x70_frYcw7f3jGGips_pvqiFKNK1CYrQkZ0sKOXw"

headers = {
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/x-www-form-urlencoded"
}

for i in range(1,2):
    params = {
        "signCheckbox":0,
        "signCheckbox":1,
        "signCheckbox":2,
        "signCheckbox":3,
        "meetingWay":0,
        "feedbackRadio":0,
        "meetviewRadio":0,
        "meetmodelRadio":1,
        "meetformhideSet":0,
        "isUseZone":0,
        "id":"2c93ab0c927af0f901927e4af4684aa4"
    }
    
    payload_json = json.dumps(params)
    response = requests.post(url,headers=headers,data=params)
    
    print(f"请求次数：{i}")
    print(f"响应状态码：{response.status_code}")
    print(f"响应内容：{response.text}")
    print("------------------------")
    
    time.sleep(1)