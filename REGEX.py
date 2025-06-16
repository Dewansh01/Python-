import re
text='''
Elon musk's phone number is +919991116666, +918669403701 ,  call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 , Modi's phone : (747)-375-4636 , 9322162332
'''

patter = " [+]\d{12}|\d{10}|\(\d{3}\)-\d{3}-\d{4} "
matches = re.findall(patter , text)
matches

output : [' +919991116666',
 ' +918669403701',
 '(999)-333-7777 ',
 '(747)-375-4636 ',
 '9322162332']
