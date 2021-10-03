ORIGINAL_COUNT = 19

id_portrait = {
               0  : "Terra",
               1  : "Locke",
               2  : "Cyan",
               3  : "Shadow",
               4  : "Edgar",
               5  : "Sabin",
               6  : "Celes",
               7  : "Strago",
               8  : "Relm",
               9  : "Setzer",
               10 : "Mog",
               11 : "Gau",
               12 : "Gogo",
               13 : "Umaro",
               14 : "Imp",
               15 : "General Leo",
               16 : "Banon",
               17 : "Ghost",
               18 : "Wedge-Vicks",

               30 : "Bartz-Xeblon-FF5",
               31 : "Berserker-JamesWhite89-FF5",
               32 : "Bird-JamesWhite89-FF6",
               33 : "Bomb-JamesWhite89-FF6",
               34 : "Cecil (Dark Knight)-HoxNorf-FF4A",
               35 : "Cecil (Dark Knight)-MetroidQuest-EC",
               36 : "Cecil (Paladin)-HoxNorf-FF4A",
               37 : "Cecil (Paladin)-MetroidQuest-EC",
               38 : "Cid-HoxNorf-FF4A",
               39 : "Cid-SpoonyBard-FF6A",
               40 : "Cirno-HoxNorf-Touhou",
               41 : "Edge-HoxNorf-FF4A",
               42 : "Edward-HoxNorf-FF4A",
               43 : "Edward-SpoonyBard-FF4C",
               44 : "Esper Terra-SpoonyBard-FF6A",
               45 : "Fish-JamesWhite89-FF6",
               46 : "Frog-MetroidQuest-EC",
               47 : "FuSoYa-HoxNorf-FF4A",
               48 : "Gestahl-MetroidQuest-EC",
               49 : "Gestahl-SpoonyBard-FF6A",
               50 : "Golbez-HoxNorf-FF4A",
               51 : "Heartless-Unknown-KH",
               52 : "Iffy-HoxNorf-Neptunia",
               53 : "Kain-HoxNorf-FF4A",
               54 : "Kain-MetroidQuest-EC",
               55 : "Kain-SpoonyBard-FF4C",
               56 : "Kefka-SpoonyBard-FF6A",
               57 : "Laguna-Xeblon-FF8",
               58 : "Lenna (White Mage)-HoxNorf-FF5",
               59 : "Magus-MetroidQuest-EC",
               60 : "Mog-JamesWhite89-FF6E",
               61 : "Nepgear-HoxNorf-Neptunia",
               62 : "Nepgear2-HoxNorf-Neptunia",
               63 : "Neptune Adult-HoxNorf-Neptunia",
               64 : "Neptune-HoxNorf-Neptunia",
               65 : "Neptune2-HoxNorf-Neptunia",
               66 : "Palom-HoxNorf-FF4A",
               67 : "Porom-HoxNorf-FF4A",
               68 : "Quina-SpoonyBard-FF9",
               69 : "Relm-MetroidQuest-EC",
               70 : "Reno-Xeblon-FF7",
               71 : "Robo-Badass-CT",
               72 : "Rosa-HoxNorf-FF4A",
               73 : "Rydia (Child)-HoxNorf-FF4A",
               74 : "Rydia-HoxNorf-FF4A",
               75 : "Schala-HoxNorf-CT",
               76 : "Soldier-LoneRedMage-FF4",
               77 : "Tellah-HoxNorf-FF4A",
               78 : "Terra-MetroidQuest-EC",
               79 : "Uni-HoxNorf-Neptunia",
               80 : "Yang-HoxNorf-FF4A",
               81 : "Zidane-Sutebenukun-FF9",
               82 : "Kuja-HoxNorf-FF9",
               83 : "Reimu-HoxNorf-Touhou",
               84 : "Ram-HoxNorf-Neptunia",
               85 : "Rom-HoxNorf-Neptunia",
               86 : "Marisa-HoxNorf-Touhou",
               87 : "Rumia-HoxNorf-Touhou",
               88 : "Papyrus-LoneRedMage-Undertale",
               89 : "Sans-LoneRedMage-Undertale",
               90 : "Toadette-HoxNorf-Mario",
               91 : "Talim-HoxNorf-SC4",
               92 : "Katt-ATinySpook-BOF2",
               93 : "Tonberry King-CDude-FF",
               94 : "Banjo Kazooie-JamesWhite89-BK",
               95 : "PajaMog-CDude-FF",
               96 : "GrimLocke-Taloswind-FF6",
               97 : "Aerith-CtrlxZ-KH",
               98 : "Ayla-CtrlxZ-CT",
               99 : "Crono-CtrlxZ-CT",
               100 : "Edea-CtrlxZ-FF8",
               101 : "Emperor-HoxNorf-FF2",
               102 : "Exdeath-CtrlxZ-FF5",
               103 : "Frog-CtrlxZ-CT",
               104 : "Gilgamesh-CtrlxZ-FF5",
               105 : "Seymour-CtrlxZ-FF10",
               106 : "Cirno2-HoxNorf-Touhou",
               107 : "Marisa2-HoxNorf-Touhou",
               108 : "Rumia2-HoxNorf-Touhou",
              }

def get_bin_path(id_):
    import os

    if id_ < ORIGINAL_COUNT:
        subdir = "original"
    else:
        subdir = "custom"

    name = id_portrait[id_]
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), subdir, name + ".bin")

def get_pal_path(id_):
    import os

    bin_path = get_bin_path(id_)
    return os.path.splitext(bin_path)[0] + ".pal"
