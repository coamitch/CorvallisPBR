cpbrAscii1      = r'           /\\\\\\\\\   /\\\\\\\\\\\\\     /\\\\\\\\\\\\\       /\\\\\\\\\                        '
cpbrAscii2      = r'         /\\\////////   \/\\\/////////\\\  \/\\\/////////\\\   /\\\///////\\\                     '
cpbrAscii3      = r'        /\\\/            \/\\\       \/\\\  \/\\\       \/\\\  \/\\\     \/\\\                    '
cpbrAscii4      = r'        /\\\              \/\\\\\\\\\\\\\/   \/\\\\\\\\\\\\\\   \/\\\\\\\\\\\/                    '
cpbrAscii5      = r'        \/\\\              \/\\\/////////     \/\\\/////////\\\  \/\\\//////\\\                   '
cpbrAscii6      = r'         \//\\\             \/\\\              \/\\\       \/\\\  \/\\\    \//\\\                 '
cpbrAscii7      = r'           \///\\\           \/\\\              \/\\\       \/\\\  \/\\\     \//\\\               '
cpbrAscii8      = r'              \////\\\\\\\\\  \/\\\              \/\\\\\\\\\\\\\/   \/\\\      \//\\\             '
cpbrAscii9      = r'                  \/////////   \///               \/////////////     \///        \///             '
cpbrAsciiList 	= [cpbrAscii1, cpbrAscii2, cpbrAscii3, cpbrAscii4, cpbrAscii5, cpbrAscii6, cpbrAscii7,
				   cpbrAscii8, cpbrAscii9]

menuAscii1      = r'          /\\\\            /\\\\   /\\\\\\\\\\\\\\\   /\\\\\     /\\\   /\\\        /\\\          '
menuAscii2      = r'          \/\\\\\\        /\\\\\\  \/\\\///////////   \/\\\\\\   \/\\\  \/\\\       \/\\\         '
menuAscii3      = r'           \/\\\//\\\    /\\\//\\\  \/\\\              \/\\\/\\\  \/\\\  \/\\\       \/\\\        '
menuAscii4      = r'            \/\\\\///\\\/\\\/ \/\\\  \/\\\\\\\\\\\      \/\\\//\\\ \/\\\  \/\\\       \/\\\       '
menuAscii5      = r'             \/\\\  \///\\\/   \/\\\  \/\\\///////       \/\\\\//\\\\/\\\  \/\\\       \/\\\      '
menuAscii6      = r'              \/\\\    \///     \/\\\  \/\\\              \/\\\ \//\\\/\\\  \/\\\       \/\\\     '
menuAscii7      = r'               \/\\\             \/\\\  \/\\\              \/\\\  \//\\\\\\  \//\\\      /\\\     '
menuAscii8      = r'                \/\\\             \/\\\  \/\\\\\\\\\\\\\\\  \/\\\   \//\\\\\   \///\\\\\\\\\/     '
menuAscii9      = r'                 \///              \///   \///////////////   \///     \/////      \/////////      '
menuAsciiList 	= [menuAscii1, menuAscii2, menuAscii3, menuAscii4, menuAscii5, menuAscii6, menuAscii7, menuAscii8,
				   menuAscii9]

helpAscii1 		= 'Help menu 		- F1'
helpAscii2		= 'OK 			- F2'
helpAscii3		= 'Back 			- F3'
helpAscii4		= 'Quit 			- F4'
helpAsciiList	= [helpAscii1, helpAscii2, helpAscii3, helpAscii4]

if __name__ == '__main__':
	print('\n'.join(cpbrAsciiList))
	print('\n'.join(menuAsciiList))
	print('\n'.join(helpAsciiList))
