#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.url("- المطور العظيم.", url="t.me/R2RR7")]])
                              
    
async def vc_menu(event):
    await event.edit("**اصدار البوت v1.4**", 
                    buttons=[
                        [Button.inline("معلومات.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/R2RR7")]])
    
