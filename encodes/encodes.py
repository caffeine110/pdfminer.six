#########################################################################
### Find all the encodes with respective :: cid=digit
    
    ### steps to follow
    # find cid:digit in .txt file
    # find that line and word in .pdf file
    # write the cid:digit  into the  > ENCODES dictioanry




#########################################################################
#0 to 9
DIGITS = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९']


#########################################################################
#VOWELS
#13 vowels in Marathi,

STD_VOWELS = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'ऋ',  'ॠ',  'ऌ' , 'ॡ', 'अं',  'अः', 'अँ',  'ऽ'   ]

DEV_VOWELS = ['ा', 'ॅ', 'ॉ', 'ि', 'ी', 'ु','ु', 'ू', 'ॆ', 'े', 'ै', 'ॊ', 'ो', 'ौ', 'ृ', 'ॄ', 'ॢ', 'ॣ', 'ं', 'ः', '्']


#########################################################################
### Consonents

VELAR_CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ']
PALATAL_CONSONANTS = ['च', 'छ', 'ज', 'झ', 'ञ']
RETROFLEX_CONSONANTS = ['ट','ठ', 'ड', 'ढ', 'ण']
DENTAL_CONSONANTS = ['त', 'थ', 'द', 'ध', 'न']
LABIAL_CONSONANTS = ['प', 'फ', 'ब', 'भ', 'म']

###semi vowels in marathi
SEMI_VOWELS = ['य', 'र', 'ल', 'व']

###sibilants in marathi
SIBILANTS = ['श', 'ष', 'स']

###fricative consonant in marathi
FRIACTIVE_CONSONANTS = ['ह']

###additional consonants:
ADDITIONAL_CONSONANTS = ['ळ', 'क्ष', 'ज्ञ']










#########################################################################
### write only || cid:digit followed by respective charector... ||


###for example 
w = "मुद्यांवर"
for i in w:
    print(i)

#output =    ectraact char like this : ्    ||   म   ु द   ्  य   ा    ं  व   र ्



ENCODES = dict()


ECODES = {
    
    7018:'व्', 7016:'ल्', 6994:'च्', 7021:'स्', 7004:'त्', 7007:'ध्',
    7079: 'प्र', 7061: 'ग्र' ,
    7410: 'ि', 
    7275: 'त्त्', 7074: 'त्र', 7271: 'रु', 7398:'ष्ट्र', 7378: 'द्यां', 

    # and so on...


}







