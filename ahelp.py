from telethon import events

import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".ahelp"))
async def ahelp(event):
	client.parse_mode = "html"
	await event.delete()
	messagelocation = event.to_id
	await event.client.send_message(messagelocation, ("""
<b>ANIMATSIONS MENU</b>

[01] فن وحش - .monster
[02] فن خنزير - .pig
[03] فن قاتل - .killer
[04] فن مسدس - .gun
[05] فن كلب - .dog
[06] سلام كبير - .hello
[07] فن "هلو يا صديقي" - .hmf
[08] فن ثنين - .couple
[09] فن سوبرمي - .sup
[10] نص ترحيب - .welc
[11] فن أفعى - .asnake
[12] فن قط - .cat
[13] نص وداع - .bye
[14] فن شيتوس - .shitos
[15] رفض كبير - .dislike
[16] هيبنو - .hypno
[17] سكوير - .squ
[18] قاتل - .kiler
[19] أنميشن قطار - .train
[20] أنميشن فضائي - .rocket
[21] أنميشن قلب - .hart
[22] أنميشن اغتصاب - .raped
[23] FNL - .fnl
[24] أنميشن قرد - .monkey
[25] أنميشن إيدين - .hands
[26] عداد أرقام - .count
[27] F كبير - .kf
[28] F - .f {نص}
[29] أوف كبير - .bigoff
[30] وردة - .flower {نص}
[31] أنميشن قلوب - .vheart {نص}
[32] أنميشن أحبك - .luvart {نص}
[33] فن "أحبك" - .iloveu

@Vnber
@R_6_7_X
"""))