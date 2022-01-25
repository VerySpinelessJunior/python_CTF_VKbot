import config
import flags
import time
from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor
from vkwave.bots import SimpleLongPollBot
from vkwave.bots.core.dispatching import filters

bot = SimpleLongPollBot(tokens=config.settings['token'],
                        group_id=config.settings['groupID'])

# Начальное меню
@bot.message_handler(
    filters.TextFilter(["начало", "старт", "привет", "начать"])
    | bot.text_filter("начальное меню")
) 
async def start(event: bot.SimpleBotEvent) -> str:

    kb = Keyboard(inline=True)
    kb.add_text_button("CTF", color=ButtonColor.PRIMARY)
    kb.add_text_button("Информация о нас", color=ButtonColor.SECONDARY)
    
    await event.answer(message="Добро пожаловать!", keyboard=kb.get_keyboard())

    # ответ на кнопку информация
    @bot.message_handler(filters.TextFilter("информация о нас"))
    async def info(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("CTF", color=ButtonColor.PRIMARY)

        await event.answer(message="https://vk.com/@qwertycodepub-informaciya-o-nas", keyboard=kb.get_keyboard())

# CTF кнопка
@bot.message_handler(filters.TextFilter("ctf"))
async def CTF(event: bot.SimpleBotEvent) -> str:

    kb = Keyboard(inline=True)
    kb.add_text_button("Ввести флаг", color=ButtonColor.PRIMARY)
    kb.add_row()
    kb.add_text_button("Получить подсказку", color=ButtonColor.POSITIVE)
    kb.add_row()
    kb.add_text_button("Начальное меню", color=ButtonColor.SECONDARY)
    kb.add_text_button("Получить первый таск", color=ButtonColor.NEGATIVE)

    await event.answer(message="Мы QwertyCode и мы проводим первый CTF на базе КПИТ'а. Он кривой, косой, с бюджетом в ящик пива и пачку сигарет. И вообще может упасть в любой момент, если ещё этого не сделал. Но он работает, вроде, а это самое главное.", keyboard=kb.get_keyboard())

    #Получить первый таск
    @bot.message_handler(filters.TextFilter("получить первый таск"))
    async def testers_button(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("Ввести флаг", color=ButtonColor.PRIMARY)
        kb.add_row()
        kb.add_text_button("Получить подсказку", color=ButtonColor.POSITIVE)
        kb.add_row()
        kb.add_text_button("Начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="Ну короче вот\n https://anonfiles.com/vdk7S3C9xb/task1_zip", keyboard=kb.get_keyboard())

# Проверка флагов и ответ
@bot.message_handler(filters.TextFilter("ввести флаг"))
async def Flags(event: bot.SimpleBotEvent) -> str:

    kb = Keyboard(inline=True)
    kb.add_text_button("Получить подсказку", color=ButtonColor.POSITIVE)
    kb.add_row()
    kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

    await event.answer(message="Отправь мне флаг и я его проверю! Всё просто. Формат флага qCTF{flag}", keyboard=kb.get_keyboard())
    
    # Блок ловли флагов и ответов
    @bot.message_handler(filters.TextFilter(flags.flags["taskKPIT_jpg"]))
    async def check(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("Получить подсказку", color=ButtonColor.POSITIVE)
        kb.add_row()
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="Это было легко, теперь думаю ты готов отринуть свою человечность и стать на чуточку больше машиной. Вперёд Сервитор, хе-хе! Найди лишний и отправь его номер мне - https://anonfiles.com/p6ncS0Cbx8/QR_Trash_zip Название - qr коды", keyboard=kb.get_keyboard())

    @bot.message_handler(filters.TextFilter(flags.flags["taskQRcodes"]))
    async def check(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="Ну теперь то тебе не нужен сканер на телефоне, ведь ты научился читать QR глазами. Там в qr-коде следующий таск, вперёд и только вперёд!", keyboard=kb.get_keyboard())


    @bot.message_handler(filters.TextFilter(flags.flags["win_form"]))
    async def check(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="Охохо, было неплохо, да? Ты хорошо дружишь с логикой, это радует. Время шифрования, расшифруй и увидишь флаг - https://vk.com/@qwertycodepub-a-nu-ka-poprobui-svoi-sily-v-shifrovanii", keyboard=kb.get_keyboard())

    @bot.message_handler(filters.TextFilter(flags.flags["encrypt"]))
    async def check(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("Получить подсказку", color=ButtonColor.POSITIVE)
        kb.add_row()
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="дальше у нас кодировка ASCII. Название - ascii. Это кстати HEX значения, а % указывает на номер. Вперёд! Расшифруй - %4a%75%73%74%20%61%75%74%6f%6d%61%74%65%5f%74%68%69%73%5f%73%68%69%74%20%61%6e%64%20%79%6f%75%20%77%69%6c%6c%20%67%65%74%20%74%68%65%20%66%6c%61%67%20%2d%20%69%5f%64%6f%6e%74%5f%6c%6f%76%65%5f%61%73%63%69%69%2e%20%59%6f%75%72%20%6e%65%78%74%20%74%61%73%6b%20%74%68%65%72%65%3a%20%68%74%74%70%73%3a%2f%2f%67%69%74%68%75%62%2e%63%6f%6d%2f%71%43%6f%64%65%2d%74%65%63%68%2f%43%54%46%5f%73%74%75%66%73%2f%74%72%65%65%2f%6d%61%69%6e%2f%48%65%78%46%6f%72%6d%61%74%73",attachment="photo-203718063_457239046", keyboard=kb.get_keyboard())
    
    @bot.message_handler(filters.TextFilter(flags.flags["ascii"]))
    async def check(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="На самом деле ascii таблици довольно полезная штука, с помощью них можно кодировать символы, которые мешают. Например при вводе команд в консоли или отправки POST/GET запросов. Если не нашёл следующий таск, он зашифрован в прошлом", keyboard=kb.get_keyboard())
    
    @bot.message_handler(filters.TextFilter(flags.flags["hexFormats"]))
    async def check(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="Ты на финишной прямой, - https://github.com/3d6Master/JS_FUCK", keyboard=kb.get_keyboard())
    
    @bot.message_handler(filters.TextFilter(flags.flags["JSFuck"]))
    async def check(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="конец, не мой, а ваш. Поздравляю, ты прошёл!", keyboard=kb.get_keyboard())
    # Конец блока ловли флагов


# Блок подсказок
@bot.message_handler(filters.TextFilter("получить подсказку"))
async def prompt(event: bot.SimpleBotEvent) -> str:

    kb = Keyboard(inline=True)
    kb.add_text_button("Ввести флаг", color=ButtonColor.PRIMARY)
    kb.add_row()
    kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

    await event.answer(message="Отправь мне команду /h {название твоего таска} и я дам тебе совет. Поможет ли он тебе? Вопрос уже дискуссионный", keyboard=kb.get_keyboard())

    # Блок ловли названия и ответов подсказок
    @bot.message_handler(filters.TextFilter("/h qr коды"))
    async def answer(event: bot.SimpleBotEvent) -> str:
        
        kb = Keyboard(inline=True)
        kb.add_text_button("Ввести флаг", color=ButtonColor.PRIMARY)
        kb.add_row()
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)
        
        await event.answer(message="Сортируй, смотри глазами, адаптируйся! Флагом будет номер врага среди своих, удачи друг!", keyboard=kb.get_keyboard())

    @bot.message_handler(filters.TextFilter("/h ascii"))
    async def answer(event: bot.SimpleBotEvent) -> str:

        kb = Keyboard(inline=True)
        kb.add_text_button("Ввести флаг", color=ButtonColor.PRIMARY)
        kb.add_row()
        kb.add_text_button("начальное меню", color=ButtonColor.SECONDARY)

        await event.answer(message="Ок, ты должен был понять что руками делать это не круто, ну так и дейлай это не руками. Автоматизируй!", keyboard=kb.get_keyboard())

bot.run_forever()
