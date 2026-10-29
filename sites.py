"""The six sites: domain, colour and menu. Page content lives in content_<key>.py."""

PHONE = "0400 369 865"
PHONE_TEL = "+61400369865"
UPDATED = "29 October 2026"
UPDATED_ISO = "2026-10-29"
ORG_ID = "https://getmypermit.com.au/#org"
QUOTE_URL = "https://getmypermit.com.au/quote"
QUOTE_EMAIL = "rossdelport1998@gmail.com"

SITES = {
    "gmp": {
        "key": "gmp", "repo": "getmypermit", "domain": "getmypermit.com.au", "name": "GetMyPermit", "short": "GetMyPermit",
        "logo": "GetMyPermit", "accent": "#2b59d1", "permit": "", "image": "gmp",
        "images": ["gmp", "shed", "pergola", "carport", "granny", "tiny"],
        "service": "Building permit and council approval service",
        "nav": [("/do-i-need-approval", "Do I need approval?"), ("/retrospective-approval", "Already built"),
                ("/for-builders", "For builders"), ("/guides", "Guides")],
        "foot_links": [("/do-i-need-approval", "Do I need approval?"), ("/retrospective-approval", "Retrospective approval"),
                       ("/for-builders", "For builders and installers"), ("/about", "About GetMyPermit"), ("/guides", "All guides and free tools")],
        "aside_title": "Let us handle it", "aside_text": "Tell us what you are building. We reply with a fixed price, usually within one business day.",
        "band_title": "Hand over the paperwork.", "band_text": "Pick your project, tell us about it, and we take it from there: plans, forms, council, and updates until your permit is issued.",
        "llms": "GetMyPermit prepares and lodges building permit and council approval applications for homeowners and builders in Perth and Western Australia: sheds, garages, carports, patios, pergolas, decks, granny flats, tiny homes, pools and retrospective approvals.",
    },
    "shed": {
        "key": "shed", "repo": "shedbuildingpermit", "domain": "shedbuildingpermit.com.au", "name": "Shed Building Permit",
        "short": "Sheds and garages", "logo": "Shed Building Permit", "accent": "#237a4b", "permit": "shed", "image": "shed",
        "images": ["shed"], "service": "Shed and garage building permit applications",
        "nav": [("/do-i-need-a-permit-for-a-shed", "Do I need one?"), ("/garage-building-permit", "Garages"),
                ("/retrospective-shed-approval", "Already built"), ("/guides", "Guides")],
        "foot_links": [("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/garage-building-permit", "Garage building permit"),
                       ("/retrospective-shed-approval", "Retrospective shed approval"), ("/guides", "All guides and free tools")],
        "foot_about": "Shed and garage building permits for Perth and Western Australia. Plans, forms and council lodgement, done for you.",
        "aside_title": "Get your shed approved", "aside_text": "Send us the shed size and your address. We reply with a fixed price, usually within one business day.",
        "band_title": "Your shed, approved without the runaround.", "band_text": "We prepare the site plan, fill in the forms, lodge with your council and answer their questions. You get on with choosing the colour.",
        "llms": "Shed Building Permit (part of GetMyPermit) prepares and lodges building permit applications for sheds, garages and outbuildings in Perth and Western Australia.",
    },
    "pergola": {
        "key": "pergola", "repo": "pergolabuildingpermit", "domain": "pergolabuildingpermit.com.au", "name": "Pergola Building Permit",
        "short": "Pergolas, patios and decks", "logo": "Pergola Building Permit", "accent": "#bb5317", "permit": "pergola", "image": "pergola",
        "images": ["pergola"], "service": "Pergola, patio and deck building permit applications",
        "nav": [("/do-i-need-council-approval-for-a-pergola", "Do I need one?"), ("/patio-building-permit", "Patios"),
                ("/deck-building-permit", "Decks"), ("/guides", "Guides")],
        "foot_links": [("/do-i-need-council-approval-for-a-pergola", "Do I need approval for a pergola?"), ("/patio-building-permit", "Patio building permit"),
                       ("/deck-building-permit", "Deck building permit"), ("/guides", "All guides and free tools")],
        "foot_about": "Pergola, patio and deck building permits for Perth and Western Australia. Plans, forms and council lodgement, done for you.",
        "aside_title": "Get your pergola approved", "aside_text": "Send us the size and your address. We reply with a fixed price, usually within one business day.",
        "band_title": "Long lunches start with the right paperwork.", "band_text": "We prepare the plans and forms, lodge with your council and deal with their questions, so your builder can start on time.",
        "llms": "Pergola Building Permit (part of GetMyPermit) prepares and lodges building permit applications for pergolas, patios, verandahs and decks in Perth and Western Australia.",
    },
    "carport": {
        "key": "carport", "repo": "carportpermit", "domain": "carportpermit.com.au", "name": "Carport Permit",
        "short": "Carports", "logo": "Carport Permit", "accent": "#0b7f86", "permit": "carport", "image": "carport",
        "images": ["carport"], "service": "Carport building permit and council approval applications",
        "nav": [("/carport-council-approval", "Council approval"), ("/carport-in-front-setback", "Front of house"),
                ("/retrospective-carport-approval", "Already built"), ("/guides", "Guides")],
        "foot_links": [("/carport-council-approval", "Carport council approval"), ("/carport-in-front-setback", "Carports in the front setback"),
                       ("/retrospective-carport-approval", "Retrospective carport approval"), ("/guides", "All guides and free tools")],
        "foot_about": "Carport building permits and planning approvals for Perth and Western Australia. Plans, forms and council lodgement, done for you.",
        "aside_title": "Get your carport approved", "aside_text": "Send us the size, where it goes and your address. We reply with a fixed price, usually within one business day.",
        "band_title": "Park the paperwork with us.", "band_text": "Planning approval, building permit or both: we work out what your council needs and lodge it for you.",
        "llms": "Carport Permit (part of GetMyPermit) prepares and lodges building permit and planning approval applications for carports in Perth and Western Australia.",
    },
    "granny": {
        "key": "granny", "repo": "grannyflatpermit", "domain": "grannyflatpermit.com.au", "name": "Granny Flat Permit",
        "short": "Granny flats", "logo": "Granny Flat Permit", "accent": "#6d4ac7", "permit": "granny-flat", "image": "granny",
        "images": ["granny"], "service": "Granny flat (ancillary dwelling) building permit applications",
        "nav": [("/granny-flat-rules-wa", "WA rules"), ("/granny-flat-approval-process", "The process"),
                ("/granny-flat-on-a-rural-lot", "Rural lots"), ("/guides", "Guides")],
        "foot_links": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-approval-process", "Granny flat approval process"),
                       ("/granny-flat-on-a-rural-lot", "Granny flats on rural lots"), ("/guides", "All guides and free tools")],
        "foot_about": "Granny flat building permits for Perth and Western Australia. We coordinate the plans, the surveyor and the council for you.",
        "aside_title": "Get your granny flat approved", "aside_text": "Tell us the size, your lot and your address. We reply with a fixed price, usually within one business day.",
        "band_title": "A granny flat is a big project. The paperwork shouldn't be.", "band_text": "We check the 70 m&sup2; rules, line up the drawings and engineering, and lodge with your council. You get one point of contact from start to permit.",
        "llms": "Granny Flat Permit (part of GetMyPermit) handles building permit applications for granny flats (ancillary dwellings) in Perth and Western Australia, including checking the R-Codes exemption for granny flats up to 70 square metres.",
    },
    "tiny": {
        "key": "tiny", "repo": "tinyhomepermit", "domain": "tinyhomepermit.com.au", "name": "Tiny Home Permit",
        "short": "Tiny homes", "logo": "Tiny Home Permit", "accent": "#9c6410", "permit": "tiny-home", "image": "tiny",
        "images": ["tiny"], "service": "Tiny home approvals (caravan approvals and building permits)",
        "nav": [("/tiny-home-on-wheels-rules-wa", "On wheels"), ("/fixed-tiny-home-permit", "Fixed tiny homes"),
                ("/tiny-home-council-application", "Applying"), ("/guides", "Guides")],
        "foot_links": [("/tiny-home-on-wheels-rules-wa", "Tiny homes on wheels in WA"), ("/fixed-tiny-home-permit", "Fixed tiny home permits"),
                       ("/tiny-home-council-application", "Applying to your council"), ("/guides", "All guides and free tools")],
        "foot_about": "Tiny home approvals for Perth and Western Australia, on wheels or on a slab. We work out the right approval and apply for you.",
        "aside_title": "Get your tiny home approved", "aside_text": "Tell us about your tiny home and the land. We reply with a fixed price, usually within one business day.",
        "band_title": "Live small. Apply once.", "band_text": "On wheels or on footings, we work out which approval your tiny home needs and handle the application with your council.",
        "llms": "Tiny Home Permit (part of GetMyPermit) helps people in Western Australia get approval for tiny homes: local government approval for tiny homes on wheels (treated as caravans) and building permits for fixed tiny homes.",
    },
}
