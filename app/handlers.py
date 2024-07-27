import asyncio

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ChatAction

from app.keyboard import (kb1, kb2, kb3, kb_history, kb_history1, kb_back, kb_history2, 
                          kb_back1, kb_get_test, kb_gender, kb_test1, kb_ass, kb_test2, kb_test3, kb_about, kb_about1, kb_get_test1)

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text = (
        "Привет, знали ли вы что с нами в одно время живет\n"
        "абсолютно уникальная и неповторимая личность?\n"
        "Чья красота затмивает свет, а ум ее настолько велик,\n"
        "что даже Стивин Хокгинг рядом с ней нервно курит в сторонке."
    ), reply_markup=kb1)


@router.message(F.text == 'Ого, кто же эта уникальная личность?')
async def step_1(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=14SqLrEo5z50E_0tBE79l_S5loNXjTD0n'
    text_caption = ('Рад, что вы спросили! Ее зовут Августина Гурьевская. '
                    'Вы только посмотрите какая она красивая! Белокурые локаны так игриво ложаться на плечи,'
                    'красивые ноги, просто очаровательные черты лица, такие одновременно точенные и нежные')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb2)


@router.message(F.text == 'Вау, она такакя крутая! Хочу узнать про нее больше!')
async def step_1(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1gphXYDuR8AezuQ0iFkdRyPysZ8cjhHQ3'
    text_caption = ('С удовольствием расскажу вам больше про замечательную Гугусичку! У нее очень много увлечений,'
                    'с ней всегда очень интересно и весело! Она смешно шутит и очень красиво говорит. Рядом с ней вы можете себя почуствовать '
                    'действительно значимым человеком! Все потому что ее искринне интересует ваша личная история')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb3)


@router.message(F.text == 'А что на счет ее личной истории?')
async def history(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.answer(text=('Ооо ее история очень красива и печальна! Она жила свою прекрасную жизнь и никого не трогала, '
                               'но однажды ее повстречал страшный Чунга-Чанга, и тогда то все и началось...'), reply_markup=kb_history)
    

@router.message(F.text == 'Вернуться назад')
async def get_back(message: Message):
    await message.answer(text='Вы вернулись! Продолжим?', reply_markup=kb3)

@router.message(F.text == 'Что же началось? Рассказывай скорее!')
async def history1(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1hhe_JRjIAmx68n_7ThYqD7jR2clts1pr'
    text_caption = ('О да, я расскажу! Это было самое счастливое и волшебное время в ее жизни! '
                    'Она любила и была любимой, много смеялась и танцевала! Но потом коварный Чунга Чанга стал показывать свое истенное лицо')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_history1)


@router.message(F.text == 'Кто же такой, этот Чунга Чанга?')
async def step_1(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=11q6PWbqO499AFxYgAn8zzMsBkF4zySUY'
    text_caption = ('Чунга Чанга это ужасный зверь, так же известный как Дима Зайцев! Он годами мучал и измывался над бедной Гугустиночкой, '
                    'и теперь она всячески ему мстит! Да так что бедный зверь забрался в свою клетку и боится показать свой нос')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_history2)

@router.message(F.text == 'Дурацкий Чунга Чанга! Убить его!')
async def step_1(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1c0QeJBF9KR86ejifIhkLnE-99xDNYjkn'
    text_caption = ('Поздравляю! Вы убили Чунга Чангу, теперь Августина счастлива')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_back)


@router.message(F.text == 'Вернуться')
async def get_back(message: Message):
    await message.answer(text='Чунга Чанга мертв, что дальше?', reply_markup=kb_history2)

@router.message(F.text == 'Она такакая молодец! А что с ней сейчас?')
async def history2(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1aaYtVmMEZx4IH7-AmF05WX9BwTj5TlaP'
    text_caption = ('Cейчас она еще краше чем прежде! Живет свою волшебную жизнь. Иногда радуется, иногда грустит... '
                    'Но по прежнему остается самой красивой и желанной женщиной на планете!')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_back1)


@router.message(F.text == 'Ну что за прекрасная личность! Хочу стать ее другом!')
async def get_test(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=19EIB6qsVtDOBUGQmQ4x9Go93ukxxcuzi'
    text_caption = ('Конечно вы хотите стать ее другом, это не так то просто! Для начала вам нужно пройти тест на друго-пригодность')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_get_test)


@router.message(F.text == 'Начать тест!')
async def start_test(message: Message):
    await asyncio.sleep(2)
    await message.answer(text='Отлично, давайте начинать тест! Для начала укажите свой пол', reply_markup=kb_gender)


@router.message(F.text == 'Мужской')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1eg43MPcsa6G0BueUbshgafyxEMK0Ii8w'
    text_caption = ('Извините, но мнение мужиков не учитывается, вы не прошли тест!')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_get_test)


@router.message(F.text == 'Женский')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1eg43MPcsa6G0BueUbshgafyxEMK0Ii8w'
    text_caption = ('Хорошее начало! Следующий вопрос: если бы вы договорились поехать куда нибудь со своей знакомой/знакомым, '
                    'но вас в этот день позвала на встречу Августина, как вы поступите?')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_test1)


@router.message(F.text == 'Скажу, что не могу поехать, потому что уже договорились на этот день')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1eg43MPcsa6G0BueUbshgafyxEMK0Ii8w'
    text_caption = ('Это неправильный ответ, вас заблокировали! Августина всегда должна стоять на первом месте!')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_back1)


@router.message(F.text == 'Сразу соглашусь на встречу с Авой')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1kkaSQ058-84xCjTf3vOHbE2qK-AETGja'
    text_caption = ('Хорошо, мне нравится ход твоих мыслей! Августина всегда должна стоять на первом месте.\n'
                    'Cледующий вопрос: какая попа вам больше нравиться?')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_ass)


@router.message(F.text == 'Мини-попа')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1I3CChXUNOJvOjetCVkUFUzITttmazeRv'
    text_caption = ('Это прекрасно! Потому что Августина является обладательницой титула самой красивой мини-попы Индонезии!\n'
                    'Cледующий вопрос: если вам придется выбирать между позвать ее бывшего на концерт и попросить ее не приходить или послать Чунга Чангу нахуй и позвать любимую Августину. '
                    'Что вы выберете?')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_test2)


@router.message(F.text == 'Мидл-попа')
async def start_test(message: Message):
    await asyncio.sleep(1)
    await message.answer(text='Это неправильный ответ, самая красивая попа это мини-попа', reply_markup=kb_back1)


@router.message(F.text == 'Макси-попа')
async def start_test(message: Message):
    await asyncio.sleep(1)
    await message.answer(text='Это неправильный ответ, самая красивая попа это мини-попа', reply_markup=kb_back1)


@router.message(F.text == 'Попрошу Августину не приходить')
async def start_test(message: Message):
    await asyncio.sleep(1)
    await message.answer(text='Ты охерела, тварь? Пизда тебе слышишь? Я уже вычислила твой айпи и еду пизтить тебя ссаными тряпками', reply_markup=kb_back1)


@router.message(F.text == 'Чунга Чанга идет на хуй')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1RNwB7fOS7rmiSyLWKMBBo8QG7VcPLdLm'
    text_caption = ('И это правильный ответ! Только последний долбаеб выберет Чунга Чангу!\n'
                         'Итак последний вопрос: готова ли ты каждый день говорить Августине какая она красивая и неповторимая, умная и смешная, '
                          'делиться с ней всеми секретами и сплетнями, любить и обожать ее до конца своих дней или пока она тебя не заблокирует?')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_test3)
    

@router.message(F.text == 'Нууу.. мне надо еще подумать')
async def start_test(message: Message):
    await asyncio.sleep(1)
    await message.answer(text='Дура, хули тут думать? Ты не прошла тест!', reply_markup=kb_back1)


@router.message(F.text == 'Да, конечно! Это же Самая красивая девочка на планете!')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1u5agX4hD-bAC1KzKBk30bM1iUWynGmKq'
    text_caption = ('Поздравляю! Вы прошли тест на друго-пригодность и теперь можете попытать свое счастье и попробовать подружиться с Августиной')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_back1)


@router.message(F.text == 'Хочу еще больше узнать про Августину!')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1M9dTP0X3HjrycrvQbKzh1yKfE0lIVIzs'
    text_caption = ('C удовольствием расскажу про нее больше! Августина, она как Вишна, женщина с 1000 имен. '
                    'Она очень умная и творческая личность, по этому у нее очень много увлечений')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_about)



@router.message(F.text == 'Как интересно! А чем она увлекается?')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1qDs9nVq0ZRaV0zrc_UGd4eFtyF94cPS7'
    text_caption = ('Рад, что вы спросили! Августина очень любит шить разную одежду. У нее есть свой уникальный стиль, '
                    'это короткие шортики, платьица, купальники, топики. Все это она собирает сама и делает своими руками, '
                    'собирает свой неповторимый образ тёти-шлюхи')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_about1)


@router.message(F.text == 'Вау, как здорово! А что еще?')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1pGl8B0s_W2P210Q13sCW5HMTZwvEM5NO'
    text_caption = ('А еще она очень любит животных (в том числе и Чунга Чангу)! У нее было много хомяков, за которыми она ухаживала. '
                    'Она очкнь хороший друг и всегда придет на помощь, и если она вас выбрала то это один раз и навсегда!')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_about1)


@router.message(F.text == 'Вау, как здорово! А что еще?')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1pGl8B0s_W2P210Q13sCW5HMTZwvEM5NO'
    text_caption = ('А еще она очень любит животных (в том числе и Чунга Чангу)! У нее было много хомяков, за которыми она ухаживала. '
                    'Она очкнь хороший друг и всегда придет на помощь, и если она вас выбрала то это один раз и навсегда!')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_about1)


@router.message(F.text == 'Какая она крутая! Хочу стать ее другом!')
async def no_man(message: Message):
    photo_url = 'https://drive.google.com/uc?export=view&id=1bcw7RtQ5KPX1qNkheIcui8YBCMzfoQ-n'
    text_caption = ('Еще бы! Если вы хотите стать ее другом, для начала нужно пройти тест на друго-пригодность.')
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1)
    await message.answer_photo(photo=photo_url, caption=text_caption, reply_markup=kb_get_test1)