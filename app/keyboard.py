from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Ого, кто же эта уникальная личность?')]], 
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Вау, она такакя крутая! Хочу узнать про нее больше!')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb3 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='А что на счет ее личной истории?')],
                                    [KeyboardButton(text='Ну что за прекрасная личность! Хочу стать ее другом!')],
                                    [KeyboardButton(text='Хочу еще больше узнать про Августину!')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_history = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Что же началось? Рассказывай скорее!')],
                                           [KeyboardButton(text='Вернуться назад')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_history1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Кто же такой, этот Чунга Чанга?')],
                                            [KeyboardButton(text='Вернуться назад')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_history2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Она такакая молодец! А что с ней сейчас?')],
                                            [KeyboardButton(text='Дурацкий Чунга Чанга! Убить его!')],
                                            [KeyboardButton(text='Вернуться назад')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_back = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Вернуться')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_back1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Вернуться назад')]],
                                                         resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_get_test = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать тест!')]],
                                  resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_gender = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Мужской')], [KeyboardButton(text='Женский')]],
                                resize_keyboard=True,
                          input_field_placeholder='Выберете вариант ответа')

kb_test1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Сразу соглашусь на встречу с Авой')],
                                         [KeyboardButton(text='Скажу, что не могу поехать, потому что уже договорились на этот день')]],
                                resize_keyboard=True,
                          input_field_placeholder='Выберете вариант ответа')

kb_test1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Сразу соглашусь на встречу с Авой')],
                                         [KeyboardButton(text='Скажу, что не могу поехать, потому что уже договорились на этот день')]],
                                resize_keyboard=True,
                          input_field_placeholder='Выберете вариант ответа')

kb_ass = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Макси-попа')],
                                            [KeyboardButton(text='Мидл-попа')],
                                            [KeyboardButton(text='Мини-попа')]],
                          resize_keyboard=True,
                          input_field_placeholder='Выберете вариант ответа')

kb_test2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Чунга Чанга идет на хуй')],
                                         [KeyboardButton(text='Попрошу Августину не приходить')]],
                                resize_keyboard=True,
                          input_field_placeholder='Выберете вариант ответа')

kb_test3 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Да, конечно! Это же Самая красивая девочка на планете!')],
                                         [KeyboardButton(text='Нууу.. мне надо еще подумать')]],
                                resize_keyboard=True,
                          input_field_placeholder='Выберете вариант ответа')

kb_about = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Как интересно! А чем она увлекается?')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_about1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Вау, как здорово! А что еще?')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')

kb_about1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Какая она крутая! Хочу стать ее другом!')]],
                          resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')


kb_get_test1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать тест!')],
                                            [KeyboardButton(text='Вернуться назад')]],
                                  resize_keyboard=True,
                          input_field_placeholder='Нажмите на кнопку, чтобы продолжить')