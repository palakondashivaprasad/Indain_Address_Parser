import re

address = raw_input("Enter address... \n")
tokend_address = list(address.split())

for i in range(len(tokend_address)):
    tokend_address[i] = tokend_address[i].capitalize()


main_address = {}

print "Lets start"
print main_address
print tokend_address

#------------------------------------------------------------------------------------------------
#   GET DATA FROM EXCEL SHEET
#------------------------------------------------------------------------------------------------

import xlrd
import unicodedata

path = "...." #path of Countries.xls in the PC

book = xlrd.open_workbook(path)

first_sheet = book.sheet_by_index(0)

countries = first_sheet.col_values(0)
del countries[0]

India_States = first_sheet.col_values(1)
del India_States[0]

Districts = first_sheet.col_values(2)
del Districts[0]

Sub_Districts = first_sheet.col_values(3)
del Sub_Districts[0]

#------------------------------------------------------------------------------------------------
#     IMPORTING DATA FROM EXCEL SHEET
#------------------------------------------------------------------------------------------------

import xlrd

path = r"..." #path of Localities.xls in the PC

book = xlrd.open_workbook(path)

first_sheet = book.sheet_by_index(0)

Localities = first_sheet.col_values(0)
del Localities[0]

Sub_Localities = first_sheet.col_values(1)
del Sub_Localities[0]

Landmarks = first_sheet.col_values(2)
del Landmarks[0]

Roadnames = first_sheet.col_values(3)
del Roadnames[0]

print tokend_address

#------------------------------------------------------------------------------------------------
#    PINCODE
#------------------------------------------------------------------------------------------------

Pincode = ""
for i in range(len(tokend_address)):
    if tokend_address[i].isdigit() and len(tokend_address[i])== 6:
        Pincode = tokend_address[i]
        main_address["Pincode"] = str(tokend_address[i])
        tokend_address.remove(tokend_address[i])
        break
print "Pincode is finished"
print main_address
print tokend_address

#------------------------------------------------------------------------------------------------
# CHECK IF LIST a IS IN LIST b
#------------------------------------------------------------------------------------------------

def sublist(a, b):
    if not a:
        return True
    for k in range(len(b)):
        if a[0] == b[k]:
            return sublist(a[1:], b[k+1:])
    return False


#------------------------------------------------------------------------------------------------
#     STATES (INDIA ONLY)
#------------------------------------------------------------------------------------------------


India_States_set = list(set(India_States))
State = ""

max_state = 0
for k in range(len(India_States_set)):
    dummy_list = list(India_States_set[k].split())
    if len(dummy_list) > max_state:
        max_state = len(dummy_list)


i_state = len(tokend_address)-1
t_state = ""
count_state = 0
for k in range(0,max_state):
    if i_state-k >= 0:
        t_state = tokend_address[i_state-k] + " " + t_state
        if count_state == 0:
            t_state = t_state[:len(t_state)-1]
            count_state += 1
        for j in range(len(India_States_set)):
            if t_state == India_States_set[j]:
                State = India_States_set[j]
                main_address["State"] = State
                dummy_list = list(State.split())
                for i in range(len(dummy_list)):
                    tokend_address.remove(dummy_list[i])
                break
#
print "State is finished"
print main_address
print tokend_address

#------------------------------------------------------------------------------------------------
#     DISTRICTS/CITY
#------------------------------------------------------------------------------------------------



Districts_set = list(set(Districts))
District = ""

max_District = 0
for k in range(len(Districts_set)):
    dummy_list = list(Districts_set[k].split())
    if len(dummy_list) > max_District:
        max_District = len(dummy_list)

i_District = len(tokend_address)-1
t_District = ""
count_District = 0
for k in range(max_District):
    if i_District-k >= 0:
        t_District = tokend_address[i_District-k] + " " + t_District
        if count_District == 0:
            t_District = t_District[:len(t_District)-1]
            count_District += 1
        for j in range(len(Districts_set)):
            if t_District == Districts_set[j]:
                District = Districts_set[j]
                main_address["City"] = District
                dummy_list = list(District.split())
                for i in range(len(dummy_list)):
                    tokend_address.remove(dummy_list[i])
                break

print "City is finshed"
print main_address
print tokend_address

#------------------------------------------------------------------------------------------------
#     SUB_DISTRICTS/LOCALITY
#------------------------------------------------------------------------------------------------



Sub_Districts_set = list(set(Sub_Districts))
Sub_District = ""

max_Sub_District = 0
for k in range(len(Sub_Districts_set)):
    dummy_list = list(Sub_Districts_set[k].split())
    if len(dummy_list) > max_Sub_District:
        max_Sub_District = len(dummy_list)

i_Sub_District = len(tokend_address)-1
t_Sub_District = ""
count_Sub_District = 0
for k in range(max_Sub_District):
    if i_Sub_District - k >= 0:
        t_Sub_District = tokend_address[i_Sub_District-k] + " " + t_Sub_District
        if count_Sub_District == 0:
            t_Sub_District = t_Sub_District[:len(t_Sub_District)-1]
            count_Sub_District += 1
        for j in range(len(Sub_Districts_set)):
            if t_Sub_District == Sub_Districts_set[j]:
                Sub_District = Sub_Districts_set[j]
                main_address["Locality"] = Sub_District
                dummy_list = list(Sub_District.split())
                for i in range(len(dummy_list)):
                    tokend_address.remove(dummy_list[i])
                break

print "Locality is finshed"
print main_address
print tokend_address

#------------------------------------------------------------------------------------------------
#    SUB-LOCALITY
#------------------------------------------------------------------------------------------------

Sub_Localities_set = list(set(Sub_Localities))
Sub_Locality = ""

max_Sub_Locality = 0
for k in range(len(Sub_Localities_set)):
    dummy_list = list(Sub_Localities_set[k].split())
    if len(dummy_list) > max_Sub_Locality:
        max_Sub_Locality = len(dummy_list)

i_Sub_Locality = len(tokend_address)-1
t_Sub_Locality = ""
count_Sub_Locality = 0
for k in range(max_Sub_Locality):
    if i_Sub_Locality - k >= 0:
        t_Sub_Locality = tokend_address[i_Sub_Locality-k] + " " + t_Sub_Locality
        if count_Sub_Locality == 0:
            t_Sub_Locality = t_Sub_Locality[:len(t_Sub_Locality)-1]
            count_Sub_Locality += 1
        for j in range(len(Sub_Localities_set)):
            if t_Sub_Locality == Sub_Localities_set[j]:
                Sub_Locality = Sub_Localities_set[j]
                main_address["Sub_Locality"] = Sub_Locality
                dummy_list = list(Sub_Locality.split())
                for i in range(len(dummy_list)):
                    tokend_address.remove(dummy_list[i])
                break

print "Subloclaity is finshed"
print main_address
print tokend_address

#andhra pradesh krishna vijayawada 509001

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#------------------------------------------------------------------------------------------------
#    DOOR/UNIT NUMBER  and  APT/HOUSE NUMBER
#------------------------------------------------------------------------------------------------

D_first_key = ["Dr","dr","DOOR","door","Door","D.","unit","Unit","Dr.","flat"]
D_second_key = ["num","no.","#","No.","NO","No"]

for i in range(len(D_first_key)):
    D_first_key[i] = D_first_key[i].capitalize()

for i in range(len(D_second_key)):
    D_second_key[i] = D_second_key[i].capitalize()

main_address["Door_num"] = ""
for i in range(len(tokend_address)-1):
    if tokend_address[i] in D_first_key:
        if tokend_address[i+1] in D_second_key:
            if re.match(r'\d+\w*[-/]?\w*[-/]?.*', tokend_address[i+2]):
                Drum = tokend_address[i+2]
                if not(Drum.isalpha()):
                    main_address["Door_num"] = tokend_address[i+2]
                    a = tokend_address[i]
                    b = tokend_address[i+1]
                    c = tokend_address[i+2]
                    tokend_address.remove(a)
                    tokend_address.remove(b)
                    tokend_address.remove(c)
                    break

print "Door with key is finshed"
print main_address
print tokend_address


A_first_key = ["apt","Apt","H.","House","h.","Apt.","Plot","Pl.","Pl","bldg","Building","B.","B"]
A_second_key = ["num","no.","#","No.","no","No"]

for i in range(len(A_first_key)):
    A_first_key[i] = A_first_key[i].capitalize()

for i in range(len(A_second_key)):
    A_second_key[i] = A_second_key[i].capitalize()

main_address["Apt_num"] = ""
for i in range(len(tokend_address)-1):
    if tokend_address[i] in A_first_key:
        if tokend_address[i+1] in A_second_key:
            if re.match(r'\d+\w*[-/]?\w*[-/]?.*',tokend_address[i+2]):
                Drum = tokend_address[i+2]
                if not(Drum.isalpha()):
                    main_address["Apt_num"] = tokend_address[i+2]
                    a = tokend_address[i]
                    b = tokend_address[i+1]
                    c = tokend_address[i+2]
                    del tokend_address[i+1]
                    tokend_address.remove(a)
                    tokend_address.remove(c)
                    break

print "Apt with key is finshed"
print main_address
print tokend_address

#------------------------------------------------------------------------------------------------
#    FLOOR NUMBER
#------------------------------------------------------------------------------------------------
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def text2int(textnum, numwords={}):
    start=0
    if not numwords:
        units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']


        tens = ["", "", 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        scales = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion']

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'First':1, 'Second':2, 'Third':3, 'Fifth':5, 'Eighth':8, 'Ninth':9, 'Twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    textnum = textnum.replace('-', ' ')

    current = result = 0
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                if start==0:
                    continue

            scale, increment = numwords[word]
            start=1
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def tex(x):
    numwords = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred', 'Thousand', 'Million', 'Billion', 'Trillion', 'And']
    ordinal_words = ['First', 'Second', 'Third', 'Fifth', 'Eighth', 'Ninth', 'Twelfth']
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    if x not in ordinal_words:
        for ending, replacement in ordinal_endings:
            if x.endswith(ending):
                x = "%s%s" % (x[:-len(ending)], replacement)

        if x in numwords:
            return True
    else:
        return True
    return False
j=100
number = ["no","No", "num","number"]

for i in range(len(number)):
    number[i] = number[i].capitalize()

def isThere(A):
    for x in number:
        if x in A:
            return True
    return False

i = 0
f = []
mid=None
lta = len(tokend_address)
while i < lta:
    if "Floor" in tokend_address[i] or "floor" in tokend_address[i]:
        if i >= 1 and tex(tokend_address[i-1]):
            j = i-1
            y = []
            while tex(tokend_address[j]) and j >= 0:
                y.append(tokend_address[j])
                j -= 1
            y.reverse()
            f = text2int(" ".join(y))
            del tokend_address[i]
            del tokend_address[j+1:i]
            break
        elif i <= (len(tokend_address)-2) and tex(tokend_address[i + 1]):
            j = i+1
            while j < len(tokend_address) and tex(tokend_address[j]):
                f.append(tokend_address[j])
                j += 1
            f = text2int(" ".join(f))
            del tokend_address[i:j]
            break
        elif i <= (len(tokend_address)-3) and tex(tokend_address[i+2]) and isThere(tokend_address[i+1]):
            j = i + 2
            while j < len(tokend_address) and tex(tokend_address[j]):
                f.append(tokend_address[j])
                j += 1
            f=text2int(" ".join(tokend_address[i+2:j]))
            del tokend_address[i:j]
            break
        elif hasNumbers(tokend_address[i]):
            f=tokend_address[i]
            del tokend_address[i]
            break
        elif i <= (len(tokend_address)-3) and hasNumbers(tokend_address[i+2]) and isThere(tokend_address[i+1]):
            f=tokend_address[i+2]
            del tokend_address[i:i+3]
            break
        elif i >= 1 and hasNumbers(tokend_address[i - 1]):
            f = tokend_address[i - 1]
            del tokend_address[i - 1:i + 1]
            break
        elif i <= (len(tokend_address)-2) and hasNumbers(tokend_address[i+1]):
            f = tokend_address[i+1]
            del tokend_address[i:i+2]
            break
    i += 1
mid = min(i,j)

r = []
if type(f) != int:
    for x in f:
        if x.isdigit():
            r.append(x)
else:
    r.append(str(f))
main_address["Floor_num"] = "".join(r)

print "Floor is finshed"
print main_address
print tokend_address

f_keywords_roadnames = ["rd.","rd","road","line","way","marg","pass","street","drive","putih","gali","veedhi","galli","path","lane","khand","cross","avenue","square","walk","layout","Street"]
s_keywords_roadnames = ["num","no.","#","No.","no","No"]

if main_address["Door_num"] == "":
    for i in range(len(tokend_address)):
        if re.match(r'\d+\w*[-/]?\w*[-/]?.*',tokend_address[i]):
            if tokend_address[i-1] not in s_keywords_roadnames and tokend_address[i-2] not in f_keywords_roadnames:
                Drum = tokend_address[i]
                if not(Drum.isalpha()):
                    if i < mid:
                        main_address["Door_num"] = tokend_address[i]
                        del tokend_address[i]
                        break
#
print "Door without key is finshed"
print main_address
print tokend_address


if main_address["Apt_num"] == "":
    for i in range(len(tokend_address)):
        if re.match(r'\d+\w*[-/]?\w*[-/]?.*',tokend_address[i]):
            if tokend_address[i-1] not in s_keywords_roadnames and tokend_address[i-2] not in f_keywords_roadnames and tokend_address[i-1] not in f_keywords_roadnames:
                Drum = tokend_address[i]
                if not(Drum.isalpha()):
                    main_address["Apt_num"] = tokend_address[i]
                    del tokend_address[i]
                    break

print "Apt without key is finished"
print main_address
print tokend_address


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#------------------------------------------------------------------------------------------------
#    LANDMARKS
#------------------------------------------------------------------------------------------------

main_address["Landmark"] = ""

keywords_s_landmarks = ["near","opp","opposite","beside","behind","above","below","next"]
keywords_e_landmarks = ["tower","enclave","apt","apartment","nivas","building","bhawan","bhavan","niwas","villa","hospital","school",
                          "office","center","nilayam","hotel","product","diagnostic","enterprise",
                            "dispensary","clinic","scan","technolog","sadan","shop","complex","work","restautant","mansion","mess",
                          "medic","residen","plaza","hostel","home","nilyam","care","bar","centre","class","travel","niwas","hub","trader","point"
,"college","corporation","arts","pharmac","institute","temple","land","theatre","pvt ltd","towers","Residency","layout","township","statue","mess"]

for i in range(len(keywords_s_landmarks)):
    keywords_s_landmarks[i] = keywords_s_landmarks[i].capitalize()

for i in range(len(keywords_e_landmarks)):
    keywords_e_landmarks[i] = keywords_e_landmarks[i].capitalize()

dummy_s_landmarks = []
for i in keywords_s_landmarks:
    if i in tokend_address:
        dummy_s_landmarks.append(tokend_address.index(i))

dummy_e_landmarks = []
for i in keywords_e_landmarks:
    if i in tokend_address:
        dummy_e_landmarks.append(tokend_address.index(i))

first = True

if len(dummy_s_landmarks) != 0:
    dummy_s_landmarks.sort()
    dummy_e_landmarks.sort()


    i_s_landmarks = 0
    i_e_landmarks = 0

    while(i_s_landmarks != len(dummy_s_landmarks) and i_e_landmarks != len(dummy_e_landmarks)):
        if dummy_e_landmarks[i_e_landmarks] <= dummy_s_landmarks[i_s_landmarks]:
            i_e_landmarks += 1
        else:
            for i in range(dummy_s_landmarks[i_s_landmarks],dummy_e_landmarks[i_e_landmarks]+1):
                main_address["Landmark"] += tokend_address[i] + " "
            i_e_landmarks += 1
            i_s_landmarks += 1

    landmark_dummy_list = list(main_address["Landmark"].split())

    for q in range(len(landmark_dummy_list)):
        if first == True:
            index = tokend_address.index(landmark_dummy_list[q])
            tokend_address[index] = "....."
            first = False
        else:
            tokend_address.remove(landmark_dummy_list[q])


print "Landmark is finshed"
print main_address
print tokend_address

#------------------------------------------------------------------------------------------------
#    BUILDING NAME
#------------------------------------------------------------------------------------------------

keywords_buildingnames = ["tower","enclave","apt","apartment","nivas","building","bhawan","bhavan","niwas","villa","hospital","school",
                          "office","center","nilayam","hotel","product","diagnostic","enterprise",
                            "dispensary","clinic","scan","technolog","sadan","shop","complex","work","restautant","mansion","mess",
                          "medic","residen","plaza","hostel","home","nilyam","care","bar","centre","class","travel","niwas","hub","trader","point"
,"college","corporation","arts","pharmac","institute","temple","land","theatre","pvt ltd","towers","Residency","layout"]


for i in range(len(keywords_buildingnames)):
    keywords_buildingnames[i] = keywords_buildingnames[i].capitalize()

dummy_buildingnames = []
main_address["Building name"] = ""
for i in keywords_buildingnames:
    if i in tokend_address:
        dummy_buildingnames.append(tokend_address.index(i))

keywords_roadnames = ["rd.","rd","road","line","way","marg","pass","street","drive","putih","gali","veedhi","galli","path","lane","khand","cross","avenue","square","walk","layout","Street"]
s_keywords_roadnames = ["num","no.","#","No.","no","No"]

for i in range(len(keywords_roadnames)):
    keywords_roadnames[i] = keywords_roadnames[i].capitalize()

dummy_roadnames = []
main_address["Road name"] = ""
for i in keywords_roadnames:
    if i in tokend_address:
        dummy_roadnames.append(tokend_address.index(i))

dummy_buildingnames.sort()

dot_index = -1

if "....." in tokend_address:
    dot_index = tokend_address.index(".....")

if len(dummy_roadnames) != 0  and len(dummy_buildingnames) != 0:
    if (((dummy_roadnames[0] > dot_index and dummy_buildingnames[0] > dot_index ) or ( dummy_roadnames[0] < dot_index and dummy_buildingnames[0] < dot_index )) and (dummy_roadnames[0] < dummy_buildingnames[0])):
        if "....." in tokend_address:
            tokend_address.remove(".....")
        if dummy_roadnames[0] != 0:
            for i in range(0, dummy_roadnames[0]):
                main_address["Road name"] += tokend_address[i] + " "
            road_dummy_list = list(main_address["Road name"].split())
            if len(road_dummy_list) != 0:
                for i in range(len(road_dummy_list)):
                    tokend_address.remove(road_dummy_list[i])
            for i in range(len(tokend_address)):
                main_address["Building name"] += tokend_address[i] + " "
        else:
            if tokend_address[0] in keywords_roadnames:
                if tokend_address[1] in s_keywords_roadnames:
                    main_address["Road name"]  = tokend_address[0] + "number" + tokend_address[2]
                else:
                    main_address["Road name"] = tokend_address[0] + "number" + tokend_address[1]
                road_dummy_list = list(main_address["Road name"].split())
                if len(road_dummy_list) != 0:
                    for i in range(len(road_dummy_list)):
                        tokend_address.remove(road_dummy_list[i])
                for i in range(len(tokend_address)):
                    main_address["Building name"] += tokend_address[i] + " "


    else:
        if len(dummy_buildingnames) != 0:
            if dot_index >= 0:
                if dot_index > dummy_buildingnames[0]:
                    for k in range(0,dummy_buildingnames[0]+1):
                        main_address["Building name"] += tokend_address[k] + " "
                else:
                    for k in range(dot_index+1,len(tokend_address)):
                        main_address["Building name"] += tokend_address[k] + " "
            else:
                for k in range(0,dummy_buildingnames[0]+1):
                    main_address["Building name"] += tokend_address[k] + " "

        if first == False:
            tokend_address.remove(".....")

        building_dummy_list = list(main_address["Building name"].split())
        if len(building_dummy_list) != 0:
            for i in range(len(building_dummy_list)):
                tokend_address.remove(building_dummy_list[i])

        print "Buliding name is finshed"
        print main_address
        print tokend_address

        #------------------------------------------------------------------------------------------------
        #    ROAD NAME
        #------------------------------------------------------------------------------------------------

        keywords_roadnames = []
        dummy_roadnames = []
        main_address["Road name"] = ""

        if len(tokend_address) > 0:
            for k in range(len(tokend_address)):
                main_address["Road name"] += tokend_address[k] + " "

        print "Road name is finished"
        print main_address
        print tokend_address

print main_address
print "Door number : ", main_address["Door_num"]
print "Floor number : ", main_address["Floor_num"]
print "Building number : ", main_address["Apt_num"]
print "Building name : ", main_address["Building name"]
print "Road name : ", main_address["Road name"]
print "Landmark : ", main_address["Landmark"]
print "Sub locality : ", main_address["Sub_Locality"]
print "Locality : ", main_address["Locality"]
print "City/District : ", main_address["City"]
print "State : ", main_address["State"]
print "Pincode : ", main_address["Pincode"]
