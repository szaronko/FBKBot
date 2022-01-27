import random
import discord

client = discord.Client()

fbkgoodlist = ["super", "ciekaw", "fajn", "mił", "najlepsz", "zajebist", "mądr",]
fbkbadlist = ["zł", "kurw", "pizd", "chuj", "słab", "najgorsz", "idiot", "głup",]
vtuberspolskalist = ["vtubers"]

vtuberhugslist = ["https://preview.redd.it/qrjxxs261za41.jpg?auto=webp&s=7fe0f9da7a880a7484653c9300a72f6073f762a9", "https://i.redd.it/5r62fhovfpx41.jpg", "https://w0.peakpx.com/wallpaper/586/638/HD-wallpaper-gura-anya-samehada-anya-melfissa-gawr-gura-hololive-hololiveen-hololiveid-vtubers.jpg", "https://cdn.donmai.us/original/da/83/da83ae9bc9a872063e59312fb3a090d3.jpg", "https://i.redd.it/46rd9veiexn51.jpg", "https://cdn.discordapp.com/attachments/885201876981809223/936194997915635753/9ETIznrHjT2fKFjM62nmE8FnCu8SoK3GcjTTQJ8YjQE.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192989351538749/sample_5c5fff7b3d5fb35b0b6a24cd663afa2b.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192971504771072/sample_be8115798181960c998a90d0338958a8.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192958540152852/sample_a0d48f129cee34aeee72d76429fc3099.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192944489250816/46a9dc5201ec6df79fe2ac91b62aab71.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192932942327868/sample_83f6b0cb92c45db88cfb88d8da90bb31.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192918518128640/sample_b284f9c2735c49c49c15ac312262d9a3.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192904509145108/sample_54743a000032b14b547355ca0e0042a1.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192891422920754/sample_a7d12d2530ebd16d2447927884735e46.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192877019688991/sample_b58a5c4db6a785c732ac0dfa216ee10e.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192862951989309/sample_1a1bc69ba891c5eca594f963232e99bd.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192848326447134/sample_75cd0454e6e427fe289d00e43b26b6da.png", "https://cdn.discordapp.com/attachments/885201876981809223/936192834653011989/sample_e815cc32883794c45a29de81102142b4.png",]

asterixandobelixquote = "Moim zdaniem to nie ma tak, że dobrze albo że nie dobrze. Gdybym miała powiedzieć, co cenię w życiu najbardziej, powiedziałabym, że ludzi. Ekhm… Ludzi, którzy podali mi pomocną dłoń, kiedy sobie nie radziłam, kiedy byłam sama. I co ciekawe, to właśnie przypadkowe spotkania wpływają na nasze życie. Chodzi o to, że kiedy wyznaje się pewne wartości, nawet pozornie uniwersalne, bywa, że nie znajduje się zrozumienia, które by tak rzec, które pomaga się nam rozwijać. Ja miałam szczęście, by tak rzec, ponieważ je znalazłam. I dziękuję życiu. Dziękuję mu, życie to śpiew, życie to taniec, życie to miłość. Wielu ludzi pyta mnie o to samo, ale jak ty to robisz? Skąd czerpiesz tę radość? A ja odpowiadam, że to proste, to umiłowanie życia, to właśnie ono sprawia, że dzisiaj na przykład robię streamy, a jutro… kto wie, dlaczego by nie, oddam się pracy społecznej i będę ot, choćby sadzić… znaczy… marchew. "
lotrquote = "Co masz na myśli? Czy masz na myśli, że życzysz mi dobrego dnia czy może próbujesz powiedzieć, że dzień jest dobry czy tego chcę czy nie? A może chcesz przekazać, że czujesz się dobrze w tym akurat dniu? A może poprostu uważasz, że to dobry dzień by być dobrym."
zartdefinicja = "Dowcip, żart, kawał – krótka forma humorystyczna, służąca rozśmieszeniu słuchacza. Najczęstszą formą rozpowszechniania dowcipu jest przekaz słowny. Dowcipy można spotkać w różnych stronach internetowych ,prasie, w specjalnych rubrykach. Publikowane są książki i czasopisma z dowcipami. Dowcipy można też spotkać na wielu stronach internetowych. Istnieją też ponure żarty („czarny dowcip”) oraz „puste dowcipy”, śmieszące tylko opowiadającego. Innym gatunkiem dowcipu jest „dowcip ciągły”, czyli powtarzany kilka razy w krótkim odstępie czasu lub „dowcip abstrakcyjny”, obecny np. w krajach Europy Środkowej – głównie w Czechach i Polsce. Znany jest także jako pure nonsense[1] czy humor angielski. Można też natrafić na pojęcie żartu „hermetycznego”, który może opierać się na memie lub jest zrozumiały tylko dla docelowej grupy odbiorców, np. kolegów z pracy czy też informatyków. "

def fbkTo(message):
  if any(u in message for u in fbkbadlist):
    return "powiem mamie ;-;"
  elif any(u in message for u in fbkgoodlist):
    return "Miło mi to słyszeć <3"
  else:
    return "Skoro tak sądzisz"

def fbkCoSadzisz(message, usrid):
  if "mnie" in message:
    return "Jesteś moim przyjacielem ;3"
  elif any(u in message for u in vtuberspolskalist):
    return "To mój twórca. Bardzo się cieszę, że mnie stworzył ^^"
  elif "amogus" in message:
    return "Amogus jest bardzo sus"
  elif "polic" in message:
    return "Policja jest bardzo potrzebna dla utrzymania porządku"
  elif "vtuberach" in message:
    return "Bardzo ich lubię. Szczególnie lubię Matsuri tylko jej nie mówcie ;3"
  else:
    return "Przepraszam. Nie wiem co to takiego"

def fbkIleSoji(message, usrid):
  if usrid == 412296331588272129:
    return " Detected 0% soja"
  elif usrid == 647203228747825162:
    return " Error 69: Soja overflow. Too much soja to measure"
  else:
    return " Detected " + str(random.randrange(0, 100)) + "% soja"

async def fbkPrzytul(msg, message, tag):
  if "mnie" in msg:
    embed=discord.Embed(title="Przytulas", description=" <@!900069469286723675> tuli " + tag, color=0x00f2e7)
    embed.set_image(url=random.choice(vtuberhugslist))
    return embed
  else:
    newstring1 = msg.replace("fbk przytul ", "")
    newstring = newstring1.replace("fubuki przytul ", "")
    embed=discord.Embed(title="Przytulas", description=tag + " tuli " + newstring, color=0x00f2e7)
    embed.set_image(url=random.choice(vtuberhugslist))
    return embed
    
def fbkCoTo(msg):
  if "vtuber" in msg:
    return "Vtuberzy to grupa streamerów z animowanym awatarem 2d/3d. Jeśli chcesz dowiedzieć się więcej polecam kanał Vtubers Polska https://www.youtube.com/channel/UCLhDzprBSIOtE0KX53LiG-w"
  elif any(u in msg for u in ["żart", "dowcip"]):
    return zartdefinicja
  else:
    return "Nie wiem. A czy to cmaczne?"

def fbkKimJest(msg):
  if "vtuber" in msg:
    return "Vtuberzy to grupa streamerów z animowanym awatarem 2d/3d. Jeśli chcesz dowiedzieć się więcej polecam kanał Vtubers Polska https://www.youtube.com/channel/UCLhDzprBSIOtE0KX53LiG-w"
  else:
    return "Niestety nie znam kogoś takiego :<"

def fbkKto(msg):
  if any(u in msg for u in ["cię stworzył", "twoim twórcą"]):
    return "Vtubers Polska!"
  else:
    return "Niewidzialna ręka wolnego rynku"
