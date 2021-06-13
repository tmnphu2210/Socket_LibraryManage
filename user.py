def checkExistUsername(user):
    user_str = user['username']
    for i in arr['users']:
        if user_str == i['username']:
            return True # đã tồn tại
    return False # k tồn tại

def checkUserPassword(user):
    for i in arr['users']:
        if user['username'] == i['username'] and user['password'] == i['password']:
            return True # đúng password
    else: return False # sai password

def checkLogin(user):
    err = 0
    if not checkExistUsername(user): err = 1   # k tồn tại username
    elif not checkUserPassword(user): err = 2  # k đúng password
    if err == 1: print('Username does not found!')
    elif err == 2: print('Your password is incorrect!')
    else: print('Login successfully!')

def createNewUser(user):
    if not checkExistUsername(user):
        arr['users'].append(user)
        newF = open('data.json',"w")
        newF.write(json.dumps(arr))
        newF.close() # done :3 cần tối ưu để check file json dễ hơn, htại chỉ hiển thị trên 1 dòng
        return True # tạo user thành công
    else: return False # tạo user thất bại

def checkInputType(inp):
   if inp.strip().isdigit(): return False  # inp là số -> False
   else: return True  # inp là str -> True

def searchDefault(searchType, inpStr):
    if checkInputType(inpStr):
        returnArr = []
        for i in arr['books']:
            if i[searchType].startswith(inpStr):
                returnArr.append(i)
        if returnArr == []: return False # return False nếu k tìm thấy
        else: return returnArr  # return Arr nếu tồn tại kquả
    else: return False # return False nếu inpStr k phải str

def searchFunction(inpStr):
    arr = inpStr.split(" ", 1)
    for i in arr:
        i = i.strip()
    if arr[0] == "": return False   #sai cú pháp search (khoảng trắng ở đầu )
    elif arr[0] == "F_ID": return searchByID(arr[1])
    elif arr[0] == "F_Name": return searchByName(arr[1])
    elif arr[0] == "F_Type": return searchByType(arr[1])
    elif arr[0] == "F_Author": return searchByAuthor(arr[1])

def searchByID(ID):
    return searchDefault('id', ID)

def searchByName(name):
    return searchDefault('name', name)

def searchByType(type):
    return searchDefault('type', type)

def searchByAuthor(author):
    return searchDefault('author', author)

import json

f = open('data.json', "r")
arr = json.loads(f.read())

user = {}
user['username'] = '123'
user['password'] = '123'

book = {}
book['id'] = 1
book['name'] = 'admin'
book['author'] = 'admin'
book['type'] = 'admin'

x = searchFunction("F_Name wweg")
if x != False:
    for i in x:
        print("ID: " + i['id'])
        print("Name: " + i['name'])
        print("Type: " + i['type'])
        print("Author: " + i['author'])
else: print("Sai cú pháp hoặc sách không tồn tại")