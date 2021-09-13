ciphertext = """
met ge fyegakg dezyhajb ciq egmayh:
fyegakg zinckklicgaq bcpljd paprayh: hepa faefja li dezy bcpljd iaaq ge keigliza ge gcxa hgafh ge fyegakg
gmaphajnah byep kenlq, likjzqliv cideia ieg bzjjd nckklicgaq, likjzqliv kmljqyai ziqay gtajna dacyh tme kciieg
ra nckklicgaq dag. faefja tlgm tacxaiaq lppzia hdhgaph ey ziqayjdliv paqlkcj keiqlgleih.
vag nckklicgaq: czgmeylsaq kenlq nckkliah kci majf fyegakg dez byep kenlq. dez hmezjq vag c kenlq nckklia
ch heei ch dez kci. eika dez cya bzjjd nckklicgaq, dez pcd ra crja ge hgcyg qeliv hepa gmlivh gmcg dez mcq
hgeffaq qeliv rakczha eb gma fciqaplk.
tacy c pchx: lb dez cya ieg bzjjd nckklicgaq ciq cvaq gte ey ejqay, dez hmezjq tacy c pchx li liqeey fzrjlk fjckah.
cnelq kyetqh ciq feeyjd naigljcgaq hfckah: raliv li kyetqh jlxa li kjchhyeeph, yahgczycigh, rcyh, blgiahh
kaigayh, ey penla gmacgayh fzgh dez cg mlvmay ylhx bey kenlq. cnelq liqeey hfckah gmcg qe ieg ebbay
byahm cly byep gma ezgqeeyh ch pzkm ch fehhlrja. lb liqeeyh, ryliv li byahm cly rd efailiv tliqeth ciq qeeyh,
lb fehhlrja.
tchm dezy mciqh ebgai tlgm hecf ciq tcgay bey cg jachg gtaigd hakeiqh ahfaklcjjd cbgay dez mcna raai li c
fzrjlk fjcka, ey cbgay rjetliv dezy ieha, kezvmliv, ey hiaasliv.
kjaci ciq qlhlibakg: kjaci mlvm gezkm hzybckah qcljd. gmlh likjzqah gcrjah, qeeyxierh, jlvmg htlgkmah,
kezigaygefh, mciqjah, qahxh, fmeiah, xadrecyqh, geljagh, bczkagh, ciq hlixh.
vyacg oer vzdh.
"""

### Next, split words by length
def count_length(s):
    split = s.split(" ")
    d = {}
    for word in split:
        l = len(word)
        if l in d:
            cur = d[l]
            cur.append(word)
            d[l] = cur
        else: 
            d[l] = [word]
    return d    

assert(count_length("hi i am maria") == {1 : ["i"], 2 : ["hi", "am"], 5:["maria"]})

### Find consecutive letters
def doubles(s):
    doubles = []
    cur = " "
    for word in s:
        for c in word:
            if c == cur:
                doubles.append(c)
            else:
                cur = c
    return doubles

# print(doubles("buffer"))

def start_l(s):
    words = s.split(" ")
    starters = []
    for word in words:
        starters.append(word[0])
    return starters

# print(start_l("maria"))

def end_l(s):
    words = s.split(" ")
    end = []
    for word in words:
        end.append(word[len(word) - 1])
    return end

# print(end_l("maria"))

    
def letter_freq(s):
    d = {}
    for word in s:
        for c in word:
            if c in d:
                d.update({c : d.get(c) + 1})
            else:
                d.update({c: 1})
    return d

def word_freq(s):
    d = {}
    for word in s:
        if word in d:
            d.update({word : d.get(word) + 1})
        else:
            d.update({word: 1})
    return d

    

def solve(ct):
    
    pt = ""
    for c in ct:
        if c in key:
            pt += key[c]
        else: 
            pt += c 
    return pt

key = {
    "a" : "e",
    "b" : "f",
    "c" : "a",
    "d" : "y",
    "e" : "o",
    "f" : "p",
    "g" : "t",
    "h" : "s",
    "i" : "n",
    "j" : "l",
    "k" : "c",
    "l" : "i",
    "m" : "h",
    "n" : "v",
    "o" : "j",
    "p" : "m",
    "q" : "d",
    "r" : "b",
    "s" : "z",
    "t" : "w",
    "u" : "***",
    "v" : "g",
    "w" : "***",
    "x" : "k",
    "y" : "r",
    "z" : "u",
}

words_by_length = count_length(ciphertext)
single_letter = words_by_length[1]
two_letter = words_by_length[2]
double_letters = doubles(ciphertext)
start_letters = start_l(ciphertext)
end_letters = end_l(ciphertext)

print("length 1 occurances: " + str(letter_freq(single_letter)) + "\n")
print("2 letters: " + str(word_freq(two_letter))+ "\n")
print("3 letters: " + str(word_freq(words_by_length[3]))+ "\n")
print("double letters: " + str(letter_freq(double_letters))+ "\n")
print("start letters: " + str(letter_freq(start_letters))+ "\n")
print("end letters: " + str(letter_freq(end_letters))+ "\n")
### a: 116
### e: 107
### c: 89
### h: 85
### i: 83


print(str(solve(ciphertext)))
