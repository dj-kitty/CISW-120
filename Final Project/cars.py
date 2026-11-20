


carBrands = {

"ford": {

    "mustang":{
        "model years": "1964 - current",
        "trims": ["EcoBoost & EcoBoost Premium", "GT & GT Premium", "Darkhorse & Darkhorse Premium", "Darkhorse SC"],
        "power source": ["2.3L turbocharged inline 4", "5.0L naturally aspirated V8", "5.0L V8", "supercharged 5.2L V8"],
        "hp": [315, 480, 500, 795],
        "combined mpg": [26, 18, 17, 17],
        "range": [416, 304, 272, 224],
        "trans": ["10-speed automatic", "6-speed manual or 10-speed automatic", "6-speed manual or 10-speed automatic", "7-speed dual clutch automatic"],
        "other specs": "Darkhorse SC has a 0-60 time of 2.9 secs, a 0-100 time of 3.2 secs, and a quarter mile time of 10.8 secs at 130 mph.",

    },
    "mustang mach-e":{
        "model years": "2021 - current",
        "trims": ["Select", "Premium", "GT", "Rally"],
        "power source": ["single motor", "dual motor", "dual motor", "dual motor"],
        "hp": [ 272, 370, 480, 480],
        "combined mpg": [ 107, 107, 90, 84],
        "range": [ 300, 320, 280, 255],
        "trans": ["none", "none", "none", "none"],
        "other specs": "This car is electronically governed to 130 mph. It is not rated for towing in the US, but in Europe it is rated for 2200 to 3,307 pounds.",

    },
    "bronco":{
        "model years": "1966-1996, 2021-current",
        "trims": ["Base", "Big Bend", "Outer Banks", "Badlands", "Heritage Edition", "Stroppe Edition", "Raptor"],
        "power source": ["2.3L inline-4", "2.3L inline-4", "2.3L inline-4", "2.3L inline-4", "2.3L inline-4", "2.7L V6", "3.0L V6"],
        "hp": [ 300, 300, 300, 300, 300, 330, 418],
        "combined mpg": [ 20, 20, 20, 20, 18, 17, 16],
        "range": [ "321-416", 395, 416, 354, 395, 354, 312],
        "trans": ["7-speed manual", "7-speed manual", "10-speed automatic", "7-speed manual", "7-speed manual", "10-speed automatic", "10-speed automatic"],
        "other specs": "This car has a towing capacity of 3,500 to 4,500 pounds, depending on the trim level. When it was first sold in 1996, it competed with the Jeep CJ-5 and the International Scout. It was originally two door, but stopped production once 4-door SUV became more liked. It started back up again with four doors, with some packages going back to the two door style. When it was re-started, it competed with the Chevrolet K5 Blazer, the Dodge Ramcharger, and the Jeep Wrangler.",

    },
    "explorer":{},
    "expedition":{},
    "escape":{},
    "maverick":{},
    "ranger":{},
    "f-150":{},
    "f-series super duty":{},
    "transit":{},
    "fusion":{},
    "focus":{},
    "taurus":{},
    "fiesta":{},


},
"chevy": {

    "trax":{},
    "trailblazer":{},
    "equinox":{},
    "blazer":{},
    "traverse":{},
    "tahoe":{},
    "suburban":{},
    "colorado":{},
    "silverado":{},
    "silverado hd":{},
    "bolt":{},
    "volt":{},
    "camaro":{},
    "corvette":{},
    "express":{},
    "spark":{},
    "sonic":{},
    "cruze":{},
    "malibu":{},
    "impala":{},


},
"dodge": {

    "charger":{},
    "challenger":{},
    "dart":{},
    "durango":{},
    "hornet":{},
    "grand caravan":{},
    "journey":{},


},
"nissan": {

    "sentra":{},
    "altima":{},
    "versa":{},
    "kicks":{},
    "rogue":{},
    "murano":{},
    "pathfinder":{},
    "armada":{},
    "frontier":{},
    "titan":{},
    "leaf":{},
    "ariya":{},
    "z":{},
    "nv van":{},
    "nv minivan":{},
    "quest":{},

},
"subaru": {

    "crosstrek":{},
    "outback":{},
    "forester":{},
    "ascent":{},
    "solterra":{},
    "uncharted":{},
    "trailseeker":{},
    "impreza":{},
    "wrx":{},
    "brz":{},


},
"honda": {

    "civic":{},
    "accord":{},
    "prelude":{},
    "hr-v":{},
    "cr-v":{},
    "passport":{},
    "pilot":{},
    "prologue":{},
    "odyssey":{},
    "midline":{},

},
"hyundai": {

    "venue":{},
    "tucson":{},
    "kona":{},
    "santa fe":{},
    "palisade":{},
    "elantra":{},
    "sonata":{},
    "ioniq 5":{},
    "ioniq 6":{},
    "ioniq 9":{},
    "santa cruz":{},

},
"toyota": {

    "corolla":{},
    "camry":{},
    "prius":{},
    "crown":{},
    "mirai":{},
    "gr86":{},
    "gr corolla":{},
    "gr supra":{},
    "corolla cross":{},
    "rav4":{},
    "bz":{},
    "highlander":{},
    "4runner":{},
    "land cruiser":{},
    "sequoia":{},
    "crown signia":{},
    "tacoma":{},
    "tundra":{},
    "sienna":{},

},
"volkswagen": {

    "taos":{},
    "tiguan":{},
    "atlas cross sport":{},
    "atlas":{},
    "jetta":{},
    "golf":{},
    "id.4":{},
    "id.buzz":{},

},
"jeep": {

    "compass":{},
    "cherokee":{},
    "grand cherokee":{},
    "wrangler":{},
    "gladiator":{},
    "wagoneer":{},
    "recon":{},

}

}

for make in carBrands.keys():
    print(make)
brand = input("Please enter the make of a car you would like to research:  ")


for model in carBrands([brand.keys()]):
    print(model)