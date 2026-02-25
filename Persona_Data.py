PROTAG_PERSONAS = [
    "Orpheus",   # P3
    "Izanagi",   # P4
    "Arsène",    # P5
]
RARITY_WEIGHTS = {
    "Common": 60.0,
    "Rare": 30.0,
    "Legendary": 9.9,
    "Mythical": 0.1
}

PERSONA_POOL = {
    "Fool": {
        "Common": ["Legion", "Obariyon", "Yomotsu-Shikome"],
        "Rare": ["Black Frost", "Ose", "Decarabia", "Bugs"],
        "Legendary": ["Susano-o", "Loki", "Dionysus", "Vishnu"],
        "Mythical": ["Izanagi Picaro", "Orpheus Picaro", "Orpheus Telos", "Satanael", "Orpheus", "Izanagi", "Arsène", "Raoul" ]
    },

    "Magician": {
       "Common": ["Nekomata", "Jack Frost", "Pyro Jack", "Sandman", "Chorozonzon"],
       "Rare": ["Sati", "Orobas", "Rangda", "Jinn", "Dis", "Hua Po"],
       "Legendary": ["Surt", "Futsunushi", "Dada", "Queen Mab"], 
       "Mythical": ["Hermes", "Trismegistus", "Jiraiya", "Susano-o", "Takehaya Susano-o", "Zorro", "Mercurius", "Diego"]
    },
    "Priestess": {
        "Common": ["Apsaras", "Unicorn", "High Pixie", "Sarasvati", "Ganga", "Parvati", "Kikuri-Hime", "Sati" "Ame no Uzume"],
        "Rare": ["Hathor", "Hariti", "Tzitzimitl", "Saki Mitama", "Skadi", "Lakshmi"],
        "Legendary": ["Scathach","Gabriel", "Cybele","Isis (P4/5)"],
        "Mythical": ["Lucia", "Juno", "Konohana Sakuya", "Amaterasu", "Sumeo-Okami", "Johanna",  "Anat", "Agnes" ]
    },
    "Empress": {
        "Common": ["Leanan Sidhe", "Yaksini", "Hariti"], 
        "Rare": ["Gabriel", "Skadi", "Dakini", "Gorgon" ], 
        "Legendary": ["Mother Harlot", "Alilat", "Lamia", "Titania", "Kali", "Isis"], 
        "Mythical": ["Artemisia", "Penthesilea", "Milady", "Astarte", "Lucy" ]
    },
    "Emperor": {
        "Common": ["Forneus", "Oberon", "Take-Mikazuchi", "Setanta", "King Frost", "Pabilsag"],
        "Rare": ["Raja Naga", "Barong", "Eligor", "Regent"],
        "Legendary": ["Baal", "Kingu", "Okuninushi", "Thoth"],
        "Mythical": ["Polydeuces", "Caesar", "Take-Mikazuchi", "Rokuten Maoh", "Goemon", "Kamu Susano-o", "Gorokichi"]
    },
    "Hierophant": {
        "Common": ["Omoikane","Berith","Flauros","Hokuto Seikun"], 
        "Rare": ["Shiisaa","Anzu","Mishaguji","Cerberus (P4/5)","Daisoujou","Bishamonten"],
        "Legendary": ["Thoth","Unicorn","Hachiman", "Kohryu"],
        "Mythical": ["Castor","Psyche"]
    },
    "Lovers": {
        "Common": ["Pixie", "Alp", "Silky", "Tam Lin"],
        "Rare": ["Narcissus", "Raphael", "Undine", "Kushinada"],
        "Legendary": ["Cybele", "Ishtar"],
        "Mythical": ["Io", "Isis (P3)", "Carmen", "Hecate", "Himiko", "Kanzeon", "Kouzeon", "Célestine"]
    },
    "Chariot": {
        "Common": ["Ara Mitama", "Chimera", "Zouchuouten", "Slime", "Agathion"],
        "Rare": ["Ares", "Oumitsunu", "Nata Taishi", "Kin-Ki", "Shiki-Ouji","Mezuki","Triglav"],
        "Legendary": ["Thor", "Koumokuten", "Futsunushi", "Atavaka" ],
        "Mythical": ["Palladion", "Pallas Athena", "Tomoe", "Suzuka Gongen", "Haraedo-no-Okami", "Captain Kidd", "Seiten Taisei", "William", "Athena Picaro"]
    },
    "Strength": {
        "Common": ["Sandman","Valkyrie","Titan","Rakshasa", "Kelpie", "Shiisaa"],
        "Rare": ["Oni", "Hanuman", "Kusi Mitama", "Jikokuten"],
        "Legendary": ["Zaou-Gongen", "Kali", "Siegfried"],
        "Mythical": ["Cerberus (P3)"]
    },
    "Hermit": {
        "Common": ["Bicorn", "Koropokkuru", "Ippon-Datara", "Sudama"],
        "Rare": ["Naga", "Kumbhanda", "Nidhoggr", "Nebiros", "Forneus", "Mothman"],
        "Legendary": ["Arahabaki", "Koumokuten", "Kurama Tengu", "Ongyo-Ki"],
        "Mythical": ["Moros", "Necronomicon", "Prometheus", "Al Azif"]
    },
    "Fortune": {
        "Common": ["Fortuna", "Clotho", "Lachesis"],
        "Rare": ["Ananta", "Atropos"],
        "Legendary": ["Norn", "Lakshmi"],
        "Mythical": ["Hermes (P2)", "Chronos", "Hypnos", "Sukuna-Hikona","Asterius Picaro", "Yamato-Takeru", "Yamato Sumeragi", "Ariadne Picaro",  "Ariadne", "Asterius"]
    },
    "Justice": {
        "Common": ["Angle", "Archangel", "Principality", "Power"],
        "Rare": ["Melchizedek", "Dominion", "Throne", "Virtue"],
        "Legendary": ["Uriel", "Metatron", "Sraosha", "Seraph"],
        "Mythical": ["Nemesis", "Kala-Nemi", "Robin Hood", "Loki (P5)"]
    },
    "Hanged Man": {
        "Common": ["Hua Po", "Inugami", "Orthrus", "Take-Minakata", "Makami"],
        "Rare": ["Jatayu", "Hecatoncheires", "Taowu", "Yatsufusa"],
        "Legendary": ["Attis", "Macabre", "Moloch"],
        "Mythical": ["Medea"]
    },
    "Death": {
        "Common": ["Mandrake", "Mokoi", "Turdak"],
        "Rare": ["Nue", "Pisaca", "Chernobog", "Mot"],
        "Legendary": ["Matador", "Hell Biker", "White Rider", "Pale Rider", "Red Rider", "Alice", "Mahakala"],
        "Mythical": ["Thanatos", "Thanatos Picaro"]
    },
    "Temperance": {
        "Common": ["Genbu", "Koppa Tengu", "Makami", "Kikokuten"],
        "Rare": ["Mitrha", "Raja Nage", "Seiryu", "Okuninushi"],
        "Legendary": ["Gabriel", "Byakko", "Suzaku"],
        "Mythical": ["Adrha", "Vishnu", "Yurlungur"]
    },
    "Devil": {
        "Common": ["Ukobach", "Incubus", "Andras", "Flauros"],
        "Rare": ["Lilim", "Pazuzu", "Vetala"],
        "Legendary": ["Baphomet", "Nebiros", "Belial", "Lilith"],
        "Mythical": ["Beelzebub"]
    },
    "Tower": {
        "Common": ["Tao Tie", "Cu Chulainn"],
        "Rare": ["Abaddon", "Seker", "Aeshma", "Kanaloa"],
        "Legendary": ["Mada", "Yoshitsune", "Mara", "Black Rider", "Seth", "Masakado", "Hastur"],
        "Mythical": ["Magatsu-Izanagi", "Magatsu-Izanagi Picaro", "Nyrarlathotep" ]
    },
    "Star": {
        "Common": ["Koadma", "Fuu-ki", "Neko Shogun"],
        "Rare": ["Kaiwan", "Ananta", "Garuda", "Hanuman"],
        "Legendary": ["Sraosha", "Vasuki"],
        "Mythical": ["Lucifer", "Helel", "Kintoki-Douji", "Kamui"]
    },
    "Moon": {
        "Common": ["Succubus", "Onmoraki", "Andra", "Nozuchi"],
        "Rare": ["Sui-Ki", "Black Ooze", "Alraune", "Girimehkala"],
        "Legendary": ["Sandalphon", "Byakhee", "Baal Zebul"],
        "Mythical": ["Kaguya", "Kaguya Picaro", "Tsukiyomi", "Tsukiyomi Picaro"]
    },
    "Sun": {
        "Common": ["Thudnerbird", "Mithras", "Quetzalcoatl"],
        "Rare": ["Phoenix", "Gdon", "Cu Sith"],
        "Legendary": ["Yatagarasu", "Horus", "Suparna"],
        "Mythical": ["Asura"]
    },
    "Judgement": {
        "Common": ["Anubis", "Berserker"],
        "Rare": ["Trumpeter", "Yamata no Orochi"],
        "Legendary": ["Michael", "Satan", "Shiva"],
        "Mythical": ["Messiah", "Messiah Picaro"]
    },
    "World": {
        "Common": ["Quetzalcoatl","Illuyanka" ],
        "Rare": ["Demeter", "Njord", "Hunab Ku", "Mucalinda"],
        "Legendary": ["Ouroboros", "Shokuin"],
        "Mythical": ["Izanagi-no-Okami", "Izanagi-no-Okami Picaro"]
    }
}

POINT_VALUES = {
    "Common": 10,
    "Rare": 50,
    "Legendary": 100,
    "Mythical": 200
}