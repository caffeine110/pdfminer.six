##########################################################################
### program to exctract || cid:digit || from the text files


##########################################################################
### files to open
dhage = "in_txt_files/dhage_guljaar.txt"
fera = "in_txt_files/fera.txt"
kali = "in_txt_files/kali_jogin.txt"
maza = "in_txt_files/maza_gaon.txt"
revolution = "in_txt_files/revolution_2020.txt"

sakhi = "in_txt_files/sakhi.txt"
sanket = "in_txt_files/sanket.txt"
sattantar = "in_txt_files/sattantar.txt"
shekara = "in_txt_files/shekara.txt"




##########################################################################
### objects
with open(dhage, "r") as fp:
    text_dhage = fp.read()

with open(fera, "r") as fp:
    text_fera = fp.read()

with open(kali, "r") as fp:
    text_kali = fp.read()

with open(maza, "r") as fp:
    text_maza = fp.read()

with open(revolution, "r") as fp:
    text_revolution = fp.read()


with open(sakhi, "r") as fp:
    text_sakhi = fp.read()

with open(sanket, "r") as fp:
    text_sanket = fp.read()

with open(sattantar, "r") as fp:
    text_sattantar = fp.read()

with open(shekara, "r") as fp:
    text_shekara = fp.read()

    


##########################################################################
### complete text
text = text_dhage + text_fera + text_kali + text_maza + text_revolution + text_sakhi + text_sanket + text_sattantar + text_shekara


#text = text_dhage + text_fera + text_kali + text_maza + text_revolution + text_sakhi + text_sanket + text_sattantar + text_shekara
#text =  text_revolution 





##########################################################################
### prit le of text
print(len(text))





##########################################################################
### create dict of codes
dict_of_code = dict()

value = 0

for i in range(0, len(text)):
    if text[i] == '(' and text[i+1] == 'c' and text[i+2] == 'i' and text[i+3] == 'd' and text[i+4] == ':' :
        code = text[i:i+10]

        key = code

        
        if key not in dict_of_code:
            dict_of_code[key] = 1

        else:
            value = dict_of_code[key]
            dict_of_code[key] = value+1







print(dict_of_code)
print("EOF... Program is Succesfully Exicuted...")