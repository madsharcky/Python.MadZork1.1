from random import randint

def getRandomDescription():
    roomDescriptions = [
        "in a Laboratory, used to develop alchemical material transmutations. The walls are decorated with dark smears and stains. The floor is made of fitted shale bricks.",
		"in a Workshop, intended for the crafting of electronics. The walls are decorated with illustrations. The main scene is of a krayt dragon and a wyvern embracing an adiaphorism. The action is set in a corrupted dining hall. The piece is formed entirely out of tiny, colored beads.  The floor is made of unsanded rock.",
		"in a Chapel, dedicated to Sheela Peryoryl, the Green Sister, with an altarpiece focused on the afterlife. The walls are decorated with dark smears and stains. The floor is made of smooth-sanded granite.in a Chapel, dedicated to Sheela Peryoryl, the Green Sister, with an altarpiece focused on the afterlife. The walls are decorated with dark smears and stains. The floor is made of smooth-sanded granite.",
		"in a Barn, designed to house and feed camels. The walls are decorated with cracked triangular windows. The floor is made of warm, throbbing flesh.",
		"in a Storeroom, designed to keep and preserve candles and lantern oil. The walls are decorated with bookshelves with tomes of Angelology. The floor is made of fitted granite flagstones.",
		"in a Training Room, focused on mage training. The walls are decorated with bookshelves with texts of Literature. The floor is made of unsanded rock.",
		"in a Room of sinister and unclear purpose. Various furniture are all oriented towards a weird lifelike sculpture of a winged child in burnished brass. The walls are decorated with a plaque on the wall with the warning: 'The cantharidal hyena shall soon discase to the instance.'. The floor is made of fitted granite flagstones.",
		"in a Office, designed for moneylenders. The walls are decorated with a plaque on the wall with the warning: 'The standard summa shall soon recapitulate to the oligopoly.'. The floor is made of seated tiles of iron.",
		"in a Storeroom, designed to keep and preserve gold and gems - a treasury. The walls are decorated with bookshelves with texts of Caprine and Ovine Husbandry. The floor is made of warm, throbbing flesh.",
		"in a Kitchen, which has clearly been used to cook with nuts and rice. The walls are decorated with bookshelves with tomes of Abjuration. The floor is made of seated tiles of iron.",
		"in a Bathrooms, richly appointed. The walls are decorated with mosaics. The piece is of a xenomorph consumed by hope. The scene occurs in the basement of a smooth building.  The floor is made of smooth-sanded marble.",
		"in a Chapel, dedicated to Sheela Peryoryl, the Green Sister, with an altarpiece focused on the afterlife. The walls are decorated with dark smears and stains. The floor is made of smooth-sanded granite.",
		"in a Dining hall, built for use by the lowest servants. The walls are decorated with paintings. The image exhibits a squadron of hunter sharks constructing a building. The scene is set in a decrepit kitchen. The piece is formed entirely out of tiny seashells.  The floor is made of rough, solid granite.",
		"in a Training Room, focused on sparring. The walls are decorated with a plaque on the wall with the saying: 'Never turn-down the aviculture.'. The floor is made of fitted sandstone bricks.",
		"in a Barracks, built to house assassins. The walls are decorated with long, gouged-out claw-marks. The floor is made of fitted shale bricks.",
		"in a Barracks, built to house archers. The walls are decorated with paintings. The main image displays a filial rove. The action is set in a richly decorated operations center. It's signed W.L. The floor is made of smooth-sanded sandstone.",
		"in a Hospital, clearly designed for an epidemic of mental illness. The walls are decorated with bookshelves with texts of contrition of Corellon, Father of Elves. The floor is made of smooth-sanded granite.",
		"in a Classroom, which once taught Hydrology. There are many desks and chairs. The walls are decorated with a plaque on the wall with the saying: 'The line of the tike shall curve where the pessimal computation fords.'. The floor is made of rough, solid granite.",
		"in a Market, a large room for trading of bulk food. The walls are decorated with dark smears and stains. The floor is made of rough soil.",
		"in a Forge, with molds and casts specifically for crafting weapons. The walls are decorated with etchings on Daggers. The main image reveals great psychic battles , all fictional. The piece is outlined in red.  The floor is made of fitted slate flagstones.",
		"in a drab octogonal room; the pristine stone walls covered in dust. Rodent's scurry from your sight across the polishedfloor. A single lantern is lit in the center of the room.",
		"in a basic circular room, where the polished timber walls have missing portions that show through to the earth. The crumbling floor shows signs of a campfire of unknown age. The room is absent of light, but candles line the wall.",
		"in a narrow circular room, where moss covers the worn walls. Bat droppings cover the fractured floor. An unlit chandalier hangs overhead. It seems like this room is a privy.",
		"in a modest room with polished marble walls. Scattered bones line the old floor. This room is completely dark, lacking torches or lamps.",
		"in a mundane room with fractured walls that have deep cracks through to the earth. Dead insects cover the tile floor. A glow eminates from the opposite side of the room. Floating in the center is a brazier.",
		"in a clean room. Claw marks run up and down the decaying walls. Insects surry from your sight across the timber floor. An unlit chandalier hangs overhead. A shelf can be found along the wall containing a jar filled with some sort of mold, a marionette and a helmet.",
		"in an enormous hexagonal room, where the filthy stone walls show signs of battle. A single deteriorated body lies in the center of the fractured floor.",
		"in a complex room. Claw marks run up and down the dry obsidean walls. The warpedfloor is littered with stones and large rubble. This room is completely dark, lacking torches or lamps.",
		"in a harsh oval room. The fractured marble walls are angled 15 degrees outward. Insects surry from your sight across the floor."
    ]
    return roomDescriptions[randint(0, len(roomDescriptions) - 1)]
   