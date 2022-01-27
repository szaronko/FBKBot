import discord
import os
import random
from keep_alive import keep_alive
import asyncio
from myFunctions import fbkTo, fbkCoSadzisz, fbkIleSoji, fbkPrzytul, fbkCoTo, fbkKimJest, fbkKto, fbkbadlist, asterixandobelixquote, lotrquote
from replit import db

agreelist = ["Oczywiście :3", "Jeszcze jak!"]
fbklist = ["Jak ja kocham Fubuki!", "Fubuki to najlepsza waifu", "Neko janai desu ;-;", "Nya~ Nya~ >.<"]

client = discord.Client()
my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
  print("Hejo! Jestem {0.user}".format(client))


@client.event
async def on_message(message):

  msg = str.lower(message.content)
  usrid = message.author.id
  tag = message.author.mention
  channel = message.channel.name

  if message.author == client.user:
    return

  if msg.startswith("!d bump"):
    bumpChannel = message.channel
    await asyncio.sleep(7199) 
    await bumpChannel.send("Można już bumpować! ;3")
  
  if msg.startswith("&showdatabase"):
    await message.channel.send(db["msgtofbk"])

  if channel.startswith("nsfw"):
    chance = random.randint(1, 10)
    if chance >= 7:
      await message.channel.send(random.choice(["To jest wgl legalne? 0.0", "Milordzie, nie wstyd ci? https://tenor.com/view/movember-skype-emoji-skype-emoticon-pinnacle-mustache-gif-15341782"]))

  if msg.startswith("fbk") | msg.startswith("fubuki"):
    try:
      m = db["msgtofbk"][str(usrid)]
      m = m + 1
      db["msgtofbk"][str(usrid)] = m
    except:
      db["msgtofbk"][str(usrid)] = 1

    #fbk czy lubisz?
    if "lubisz" in msg:
      if "dup" in msg:
        await message.channel.send("No chyba ty")
      else:
        await message.channel.send(random.choice(agreelist))
    #fbk kochasz mnie
    elif any(u in msg for u in ["kocha", "waifu", "żon", "ożeni", "ożeń"]):
      await message.channel.send("No no no! No waifu! A friend!")
    #fbk catto
    elif any(u in msg for u in [" kot", "cat", " neko", "kotem"]):
      await message.channel.send(random.choice(["Mam dzwonić po vtubersa?", "https://youtu.be/E-Xxo6utgNA"]))
    #fbk soja detector
    elif any(u in msg for u in ["ile", "jaki"]) & any(u in msg for u in ["soji"]):
      await message.channel.send(tag + fbkIleSoji(msg, usrid))
    #fbk czy kłamiesz
    elif any(u in msg for u in ["kłam", "oszukuj",]):
      await message.channel.send("Nigdy w życiu nie kłamię! No chyba, że w grę wchodzą pieniądze...")
    #fbk flat
    elif any(u in msg for u in ["flat", "pettan", "płask"]):
      await message.channel.send("No! No! I'm boing boing!")
    #fbk gay
    elif any(u in msg for u in ["gay", "yaoi", "gej",]):
      await message.channel.send("Paanie... ale żeby tak chłop ze chłopem?")
    #fbk wytłumacz
    elif any(u in msg for u in ["wytłumacz", "wyjaśnij",]):
      await message.channel.send("Ale tak za darmo?")
    #fbk nudzi mi sie
    elif any(u in msg for u in ["nudno", "nudzi"]):
      await message.channel.send("Zawszę możesz pooglądać moje streamy albo albo filmy na kanale vtubers polska :D")
    #fbk ulubione
    #fbk pytania
    elif any(u in msg for u in ["po co", "poco",]):
      await message.channel.send("Poco to się nogi noco")
    elif "co to" in msg:
      await message.channel.send(fbkCoTo(msg))
    elif " kim " in msg:
      await message.channel.send(fbkKimJest(msg))
    elif " co się " in msg:
      await message.channel.send("A co się? Co się ctało?")
    elif "ile" in msg:
      if any(u in msg for u in ["masz lat",]):
        await message.channel.send("Tyle ile średnio ma każda loli w anime, czyli 8969")
      elif "wiadomości" in msg:
        await message.channel.send(str(db["msgtofbk"][str(usrid)]))
      else:
        await message.channel.send(str(random.randrange(0, 100)))
    elif "kto" in msg:
      await message.channel.send(fbkKto(msg))
    elif "która godzina" in msg:
      await message.channel.send("Twoja ostatnia hehe <3")
    elif "jak to jest" in msg:
      await message.channel.send(asterixandobelixquote)
    elif "jak" in msg:
      if any(u in msg for u in ["egzyst", "życi", "żyć"]):
        await message.channel.send("Moim zdaniem życie samo w sobie nie ma sensu. Chodzi o to by samemu sobie taki sens nadać. Musisz pomyśleć o tym co jest dla ciebie ważne i podążać za tym")
      else:
        await message.channel.send(" <:idk:886562655496720426> ")
    elif "nie?" in msg:
      await message.channel.send(" <:idk:886562655496720426> ")
    elif "kiedy" in msg:
      await message.channel.send("jak wpłacisz 5zł na tego patronite https://patronite.pl/vtuberspolska")
    elif any(u in msg for u in ["chcesz czegoś", "potrzebujesz czegoś",]):
      await message.channel.send("No jak mi dasz piniądze to będzie mi miło :3 https://patronite.pl/vtuberspolska")
    elif any(u in msg for u in ["Dziękuję", "dzięki",]):
      await message.channel.send("Ależ nie ma za co! 5 złotych się należy https://patronite.pl/vtuberspolska (sorry ale biznes to biznes) ")
    elif any(u in msg for u in ["czym jest", "co to",]):
      await message.channel.send("Mnie pytasz? Popatrz w wikipedii")
    elif "gdzie" in msg:
      await message.channel.send("W północnej Korei w mieście o nazwie Tokyo") 
    elif "czyj" in msg:
      if "wina" in msg:
        await message.channel.send("To wszystko wina Tuska")
      else:
        await message.channel.send("A skąd ja mam to wiedzieć?")
    elif "czy" in msg:
      await message.channel.send("Wsm nie wiem ale się wypowiem: " + random.choice(["tak", "nie"]))
    #fbk sex
    elif any(u in msg for u in ["sex", "nudes", "sperm", "pizd", "chuj", "dup", "seks", "fuck", "pierdolić",]):
      await message.channel.send(random.choice(["<:HORNY:886857909219254292>", "Onii chan wa hentai!!!", "Baaaka! Hentai! Ahoo~",]))
    elif any(u in msg for u in ["zrób mi loda", "zrób mi louda"]):
      await message.channel.send("Halo? Policja?")
    #fbk zrób
    elif any(u in msg for u in ["zrób",]):
      await message.channel.send("A muszę?")
    #fbk sus
    elif "sus" in msg:
      await message.channel.send(" https://cdn.discordapp.com/attachments/900069754960740375/935953423633874944/maxresdefault.jpg ")
    #fbk obrazy i pochwały
    elif any(u in msg for u in ["fbk jest", "fubuki jest", "fbk to ", "fubuki to "]):
      await message.channel.send(fbkTo(msg))
    elif any(u in msg for u in ["jeb", "pier", "wal się", "chuj ci", "kurw"]) | any(u in msg for u in fbkbadlist):
      await message.channel.send(str(tag) + " No U!")
      await message.channel.send("destroyed")
    elif any(u in msg for u in ["nienawidzę", "nie lubię",]) & any(u in msg for u in ["cię", "cie"]):
      await message.channel.send("Przykro mi ;-; W czym problem?")
    elif any(u in msg for u in ["kocham", "lubię", "uwielbiam",]) & any(u in msg for u in ["cię", "cie"]):
      await message.channel.send("Dziękuję! Wiele to dla mnie znaczy ;3")
    #fbk interakcje
    elif any(u in msg for u in [" mofu", " pat",]):
      await message.channel.send("A! C-c-co ty robisz? https://preview.redd.it/1lmx8s7pnhd51.png?auto=webp&s=b3dc7d798df31cfc5753407468f06ef560eccf4c")
    #fbk co tam
    elif any(u in msg for u in ["co tam", "jak tam", "jak się czujesz", "co u ciebie"]):
      await message.channel.send("Super! A co u ciebie?")
    #fbk co sądzisz o
    elif any(u in msg for u in ["myślisz", "sądzisz",]) & all(u in msg for u in ["co", " o ",]):
      await message.channel.send(fbkCoSadzisz(msg, usrid))
    #fbk help
    elif any(u in msg for u in ["pomoc", "help", "kim jesteś", "kto ty", "kim ty jesteś",]):
      await message.channel.send("Jestem przyjaznym botem! Możesz ze mną porozmawiać na różne tematy. Mogę również sprawdzić ilość soji w twojej duszy. Wystarczy poprosić. Mogę również przytulić ciebie albo kogoś innego! Zostałam stworzona przez vtubers Polska! ")
    #fbk przywitania
    elif any(u in msg for u in ["hej", "cześć", "wita", "siema", "elo",]):
      await message.channel.send(random.choice(["Hejka przyjacielu :3", "witaj kolego ^^"]))
    #fbk dziendobry
    elif "dzień dobry" in msg:
      await message.channel.send(lotrquote)
    #fbk pozegnania
    elif any(u in msg for u in ["pa pa", "do zobaczenia", "do widzenia",]):
      await message.channel.send("Pa pa! Mam nadzieję, że pogadamy jeszcze kiedyś ^^")
    #fbk dobranoc
    elif any(u in msg for u in ["dobranoc", "idę spać", "miłych snów",]):
      await message.channel.send("Miłych snów! Niech Ci się przyśni coś przyjemnego! :3")
    #fbk ladny dzien
    elif any(u in msg for u in ["ładn",]) & any(u in msg for u in ["dzień", "pogoda", "dzionek"]):
      await message.channel.send("Jeśli chcesz mnie poderwać to wymyśl coś bardziej oryginalnego :3")
    #fbk powiedz coś
    elif any(u in msg for u in ["powiedz coś", "zaskocz mnie"]):
      await message.channel.send("Gorące mamuśki w okolicy! Tylko za 5zł patronite! https://patronite.pl/vtuberspolska")
    #fbk twoja wina
    elif "twoja wina" in msg:
      await message.channel.send("To wszystko wina tuska")
    #fbk nya
    elif "nya" in msg:
      await message.channel.send("https://tenor.com/view/shirakami-fubuki-fubuki-hololive-shirakami-fubuki-fubuki-nyan-fubuki-cat-gif-20922322")
    #fbk matsuri
    elif "matsuri" in msg:
      await message.channel.send("Czy ktoś powiedział matsuri? Gdzie??")
    #fbk smutno mi
    elif any(u in msg for u in ["przykro mi", "smutno mi", "źle się czuję", "mam depresję", "pociesz"]):
      await message.channel.send("https://www.youtube.com/watch?v=xR-E2pwgFJo")
    #fbk żart
    #elif any(u in msg for u in ["żart", "dowcip"]) | ("powiedz" in msg):
    #  await message.channel.send("")
    #fbk powtorz
    elif "powtórz" in msg:
      print(msg)
      if any(u in msg for u in ["kurw", "pizd", "chuj", "vtubers to dyktator", "vtuber to dyktator"]):
        await message.channel.send("Dobrze się czujesz? -_-")
      else:
        await message.channel.send(msg.replace("fbk powtórz ", ""))
    #fbk przytul
    elif "przytul " in msg:
      await message.channel.send(embed=await fbkPrzytul(msg, message, tag))
    #fbk else
    else:
      await message.channel.send(random.choice(fbklist))

#todo fbk wyslij art, fbk mozemy byc przyjaciolmi, fbk gift za rozmawianie, fbk idź juz spac bo juz puzyno, fbk opowiedz zart, fbk ulubione

keep_alive()
client.run(my_secret)
