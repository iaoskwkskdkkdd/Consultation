from telethon import events
import phoenix.client
client = phoenix.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def help(event):
	await event.delete()
	messagelocation = event.to_id
	await event.client.send_message(messagelocation, ("""
*القائمة**
		  
Umumiy modullar: 63
<== **سورس استشوير** ==>
الاوامر:  

[01] قائمة المساعدة - .help
[02] قنابل إيموجي - .bombs
[03] تحميل متحرك - .loading
[04] تعديل نص بإيموجي - .emoji <اكتب النص>
[05] سكب الحلوى - .dump
[06] وحدة ياشرن (خاصة)
[07] كتابة متحركة - .type <اكتب النص>
[08] ضحك متحرك - .lul
[09] لعبة السنكه - .snake
[10] مو سعيد - .nothappy
[11] ساعة متحركة - .clock
[12] بوسة متحركة - .muah
[13] قلب متحرك - .heart
[14] تمارين رياضية - .gym
[15] الأرض - .earth
[16] القمر - .moon
[17] حلوى - .candy
[18] قمر smoon - .smoon
[19] قمر tmoon - .tmoon
[20] مهرج - .clown
[21] نجوم وفراشات - .butterfly
[22] مربعات ألوان - .boxs
[23] مطر - .rain
[24] شكو؟ - .clol
[25] أودرا - .odra
[26] اتركني - .fleaveme
[27] أحبك - .loveu
[28] طيارة - .plane
[29] شرطة - .police
[30] جيو - .jio
[31] النظام الشمسي - .solarsystem
[32] وحدة ياشرن (خاصة)
[33] ردود فعل - .react help
[34] ثلج - .snow
[35] قلوب سحرية - .magic
[36] قلوب - .hearts
[37] تصبح على خير - .gn
[38] حب وغرام - .lovely
[39] كَتدم - .ketdim
[40] ليش؟ - .why
[41] أنميشن "أوزبك سلة" - .uzb

اوامر الخدمات 🇮🇶

[42] كتم - .mute (m, h, d)
[43] تحويل نص إلى صوت - .tts <رمز اللغة> <رد>
[44] طرد - .kick
[45] ساعة بالبايو - .setbioclock <رقم>
[46] ساعة بالاسم - .setclock <رقم> <الاسم>
[47] مؤقت متحرك - .timer <رقم>
[48] وضع أفك - .afk-on <نص> / .afk-off / .afk-info
[49] أرقام - .numbers <رقم>
[50] منشن للكل - .tagall
[51] تشفير Base64 - .b64 en <رد> / .b64 de <رسالة مشفرة>
[52] كشف الحسابات المحذوفة - .finda
[53] حفظ صورة - .psave
[54] حذف الحسابات المحذوفة - .removeakk
[55] تتبع IP - .ipعنوان IP>
[56] إعادة تسمية - .rename <الاسم الأول> / <الاسم الثاني>
[57] معلومات المستخدم - .userinfo <رد>
[58] سبام رسائل - .spam <الوقت> <العدد> <النص>
[59] حفظ رسالة - .msave
[60] تحديث الرسائل - .rgm
[61] عكس النص - .rev <رد>
[62] كتابة ملاحظات - .konspekt <رد>
[63] ترجمة - .tr <رمز اللغة> <رد>
[++] المساعدة للأنميشن - .ahelp

@Vnber
@R_6_7_X

"""))
