LOVE, EAT, PLAY, SLEEP, DEAD, STATUS = "Гладить", "Положить корм", "Играть", "Уложить спать", "Усыпить", "Статус"
LOVE_ID, EAT_ID, PLAY_ID, SLEEP_ID, DEAD_ID, STATUS_ID, MENU = range(7)
# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
ONE, TWO, THREE, FOUR = range(4)

TIME_TO_SLEEP = 5
TIME_TO_MISS = 60 * 60

# счастье
LAUGH_STICK = "CAACAgIAAxkBAAJka2aM7o-MGuQBrGPw68KcYWBwio3nAAJlAAPb234AAe30AAHIGxkm9TUE"  # смеется
# отправляет поцелуйчики
LOVE_STICK = "CAACAgIAAxkBAAJkbmaM7sOz1tQ19HmGutRUCYnj-f91AAJpAAPb234AASMVMiDlfG67NQQ"
OK_STICK = "CAACAgIAAxkBAAJkcWaM7uAkt3GWmud6SOgxUhL5tA9AAAI_AAPb234AAfTmnDgB5KppNQQ"  # показывает ОК
# машет рукой, приветствуя
HELLO_STICK = "CAACAgIAAxkBAAJkd2aM71Co5lBQ3_kv8qU9KeS6Nw3rAAJvAAPb234AAZlbUKh7k4B0NQQ"
REST_STICK = "CAACAgIAAxkBAAJkgGaM75-tntLtjrzl7EKrMfD9rQ-xAAJgAAPb234AAYYpTM5Q4efhNQQ"  # закат, пальмы
# собирает сердечки
LOVE2_STICK = "CAACAgIAAxkBAAJkg2aM7-IkaTZmJ5dXoTzBVoeoOcbbAAJhAAPb234AAff3D5s36tTkNQQ"
# появляется из коробки и крутится
HELLO2_STICK = "CAACAgIAAxkBAAJkiWaM8KxqhdU8Yx1n0HnLXAyhneTuAAJuAAPb234AAUaeZ3EyOf6TNQQ"
# запускает казино
KAZINO_STICK = "CAACAgIAAxkBAAJkoWaNICdWnYLVBdqky0RlhcWkmCt5AAJqAAPb234AAfGPst81YhbfNQQ"
# в колпаке, с дуделкой, радуется
BIRTHDAY_STICK = "CAACAgIAAxkBAAJkjGaM8OjdZQpSCVwqbB_1d5QPZ1vhAAJmAAPb234AAZPMw9ANLY9sNQQ"

# когда плохо
# кружится голова, мутит
NOT_GOOD_STICK = "CAACAgIAAxkBAAJkdGaM7xkAAXpK4QU8p7zsJhUEIoV_DAACYgAD29t-AAGOFzVmmxPyHDUE"
# стреляет в экран
ANGRY_STICK = "CAACAgIAAxkBAAJkm2aNH9-9TkXgjXthXZEeUczg3_vwAAJwAAPb234AAeoAAbe3Jpg43TUE"
# ломаются антенны
TIRED_STICK = "CAACAgIAAxkBAAJknmaNIAcSXU4tXAK_T5Brvvl8eHwaAAJjAAPb234AAYydBT3nQoPnNQQ"

# нейтрально
SLEEP_STICK = "CAACAgIAAxkBAAJkemaM72y63k6340Yc0OpJSBuppc-JAAI4AAPb234AAdmTfJg3bOUsNQQ"  # спит
EAT_STICK = "CAACAgIAAxkBAAJkhmaM8I0nRuHKKcM5-VqzZyo9Vk7nAAJoAAPb234AAf0R7Tldu9yTNQQ"  # допустим, ест
# бежит на двух ногах
PLAY_STICK = "CAACAgIAAxkBAAJkkmaM8T9T7tXNttlKvw-749uG9CEBAAJsAAPb234AAQJocymo-yvBNQQ"
# воспроизводит музыку
PLAY2_STICK = "CAACAgIAAxkBAAJkmGaNH7_fKD5bx0Pbj3HeV9XP_4SmAAJnAAPb234AAT3fFO9hR5GfNQQ"




LOVE_PHRASES = [
    "Спасибо за ласку! Теперь мне хорошо.",
    "Мур-мяу! Как приятно быть гладким.",
    "Ого, это так приятно! Я в восторге.",
    "Поглаживание — мое любимое занятие. Спасибо!",
    "Мурчу от удовольствия. Вы мастер глажения!",
    "Уровень счастья увеличился благодаря вашему ласковому прикосновению.",
    "Люблю, когда меня гладят. Спасибо за заботу!",
    "Так приятно быть любимым и ухоженным.",
    "Ваше ласковое прикосновение сделало мой день.",
    "Я чувствую вашу заботу и любовь. Спасибо за ласку!"
    ]
LOVE_STICKERS = [LOVE_STICK, LOVE2_STICK, LAUGH_STICK, OK_STICK]



HELLO_PHRASES = [
    "Привет! Как приятно видеть тебя снова!",
    "Добро пожаловать! Я так рад тебя видеть!",
    "Хозяин, как прошел твой день? У меня всё в порядке!",
    "О, это ты! Я уже скучал по тебе. Что нового?",
    "Здравствуй, мой верный друг! Как настроение сегодня?",
    "Приветствую, хозяин! Готов к новым приключениям?",
    "Привет! Я ждал твоего возвращения. Чем займемся сегодня?",
    "Рад снова быть с тобой! Что планируем делать?",
    "Здравствуй! Я готов выполнить все твои команды.",
    "Добрый вечер, хозяин! Как прошел твой день? У меня всё готово для новых приключений!",
    "Привет, мой любимый хозяин! Я ждал тебя. Чем займемся?"
]


HELLO_STICKERS = [HELLO_STICK, HELLO2_STICK,
                  KAZINO_STICK, BIRTHDAY_STICK, LOVE_STICK, REST_STICK]



FOOD_PHRASES = [
    "Спасибо за еду! Я чувствую, что становлюсь сильнее!",
    "Ммм, вкусно! Ты знаешь, как меня порадовать!",
    "Я так голоден! Спасибо, что позаботился обо мне.",
    "Ура! Еда - мой любимый вид развлечений. Спасибо!",
    "Ты всегда заботишься обо мне. Я так благодарен за еду!",
    "Очень вкусно! Теперь я полон энергии и готов к новым приключениям!",
    "Ты лучший хозяин! Моя благодарность за этот вкусный ужин.",
    "Я люблю, когда меня кормят. Спасибо за внимание ко мне!",
    "Ммм, аромат этой еды... Спасибо, что не забываешь про меня!",
    "Как вкусно! Ты точно знаешь, как меня порадовать своим угощением!"
]


FOOD_STICKERS = [LOVE_STICK, EAT_STICK]




PLAY_PHRASES = [
    "Уф, это было напряженно! Мы так много двигались в игре в прятки!",
    "Я почти победил в нашей партии шахмат! Следующий раз точно у тебя не получится!",
    "Бум! Я просто разгромил тебя в нашем баскетбольном матче. Ты не готов к моим трюкам!",
    "Весело было строить замки из песка на пляже! Я даже почти научился плавать.",
    "Ты был отличным напарником в нашей игре в волейбол! Мы сработались как команда.",
    "Сегодня я выиграл в нашей партии настольного тенниса! Моя реакция на высоте.",
    "Эта партия в крокет была просто великолепной! Ты ведь знаешь, что я прекрасно разбираюсь в стратегии.",
    "Я научился так много новых трюков в нашей игре на скейтборде! Это было круто!",
    "Спасибо за увлекательную партию в монополию! Ты меня почти обогнал, но я вернулся!",
    "Вечеринка в Мафию была настоящим вызовом! Я вот-вот выиграю следующую игру."
]


PLAY_STICKERS = [PLAY_STICK, PLAY2_STICK,
                 KAZINO_STICK, OK_STICK, LAUGH_STICK, LOVE_STICK]




MISS_PHRASES = [
    "Привет! Я скучаю без тебя! Давай поиграем вместе!",
    "Эй, где ты? Мне так одиноко без тебя. Погнали играть!",
    "Я тут думаю, как же скучно без наших игр. Тебе не кажется?",
    "У тебя наверняка было много дел, но я уже соскучился по нашим приключениям. Погнали играть!",
    "Может быть, мы снова начнем играть? Я прямо чувствую, что мы что-то пропускаем.",
    "Эй, ты случайно не забыл про меня? Давай поиграем, чтобы я не скучал так сильно.",
    "Ты так долго был(а) занят(а), а я тут ждал! Ну что, не время ли нам снова начать наши игры?",
    "Я тут все вспоминаю наши игры. Как же мне хочется снова с тобой поиграть!",
    "Я уж думал, ты меня забыл(а)! Ну что, начнем играть снова?",
    "Ты такой(ая) занятой(ая), а я так скучаю! Давай встретимся в игре, чтобы развеселиться!"
]
