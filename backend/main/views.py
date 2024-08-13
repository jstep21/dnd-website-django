from django.shortcuts import render, redirect, reverse
from spells.utils import fetch_spell_data

# Create your views here.
CLASSES = [('barbarian', 'For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength.'),
           ('bard', 'Whether scholar, skald, or scoundrel, a bard weaves magic through words and music to inspire allies, demoralize foes, manipulate minds, create illusions, and even heal wounds. The bard is a master of song, speech, and the magic they contain.'),
           ('cleric', 'Clerics are intermediaries between the mortal world and the distant planes of the gods. As varied as the gods they serve, clerics strive to embody the handiwork of their deities. No ordinary priest, a cleric is imbued with divine magic.'),
           ('druid', "Whether calling on the elemental forces of nature or emulating the creatures of the animal world, druids are an embodiment of nature's resilience, cunning, and fury. They claim no mastery over nature, but see themselves as extensions of nature's indomitable will."),
           ('fighter', 'Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. They are well acquainted with death, both meting it out and staring it defiantly in the face.'),
           ('monk', 'Monks are united in their ability to magically harness the energy that flows in their bodies. Whether channeled as a striking display of combat prowess or a subtler focus of defensive ability and speed, this energy infuses all that a monk does.'),
           ('paladin', "Whether sworn before a god's altar and the witness of a priest, in a sacred glade before nature spirits and fey beings, or in a moment of desperation and grief with the dead as the only witness, a paladin's oath is a powerful bond."),
           ('ranger', 'Far from the bustle of cities and towns, past the hedges that shelter the most distant farms from the terrors of the wild, amid the dense-packed trees of trackless forests and across wide and empty plains, rangers keep their unending watch.'),
           ('rogue', "Rogues rely on skill, stealth, and their foes' vulnerabilities to get the upper hand in any situation. They have a knack for finding the solution to just about any problem, demonstrating a resourcefulness and versatility that is the cornerstone of any successful adventuring party."),
           ('sorcerer', 'Sorcerers carry a magical birthright conferred upon them by an exotic bloodline, some otherworldly influence, or exposure to unknown cosmic forces. No one chooses sorcery; the power chooses the sorcerer.'),
           ('warlock', 'Warlocks are seekers of the knowledge that lies hidden in the fabric of the multiverse. Through pacts made with mysterious beings of supernatural power, warlocks unlock magical effects both subtle and spectacular.'),
           ('wizard', 'Wizards are supreme magic-users, defined and united as a class by the spells they cast. Drawing on the subtle weave of magic that permeates the cosmos, wizards cast spells of explosive fire, arcing lightning, subtle deception, brute-force mind control, and much more.')]


def home_page(request):
    """check if a user makes a search request, if so redirect to search page;
    otherwise, render home page"""
    spells_data = fetch_spell_data()
    spells = spells_data.get('results', [])
    
    return render(request, 'index.html', {
        'spells_data': spells_data,
        'spells': spells,
        'classes': CLASSES
    })


def about_page(request):
    """Renders the about page."""
    return render(request, 'about.html')
