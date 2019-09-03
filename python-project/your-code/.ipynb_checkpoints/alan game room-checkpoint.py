#OBJETOS
couch = {
    'key' : False,
    'textFalse': 'There is nothing here.',
    'type': 'furniture'
}

piano ={
    'key' : True,
    'textTrue': 'You find key for door A.',
    'textFalse': 'There is nothing here.',
    'type': 'furniture',
    'get': 'key A'
}

door_A = {
    'locked': True,
    'textLocked': "It is locked and you don't have the key.",
    'textOpen': "You unlock it with the key A you have.",
    'textPass': "You passed the door",
    'type': 'door',
    'unlock' : 'key A'
}

queen_bed = {
    'key' : True,
    'textTrue': 'You find key for door B.',
    'textFalse': 'There is nothing here.',
    'type': 'furniture',
    'get': 'key B'
}

door_C = {
    'locked': True,
    'textLocked': "It is locked and you don't have the key.",
    'textOpen': "You unlock it with the key C you have.",
    'textPass': "You passed the door",
    'type': 'door',
    'unlock' : 'key C'
}

door_B = {
    'locked': True,
    'textLocked': "It is locked and you don't have the key.",
    'textOpen': "You unlock it with the key B you have.",
    'textPass': "You passed the door",
    'type': 'door',
    'unlock' : 'key B'
}

double_bed ={
    'key': True,
    'textTrue': 'You find key for door C.',
    'textFalse': 'There is nothing here.',
    'type': 'furniture',
    'get': 'key C'
}

dresser = {
    'key': True,
    'textTrue': 'You find key for door D.',
    'textFalse': 'There is nothing here.',
    'type': 'furniture',
    'get': 'key D'
}

dining_table = {
    'key': False,
    'textFalse': 'There is nothing here.',
    'type': 'furniture'
}

door_D = {
    'locked' : True,
    'textLocked': "It is locked and you don't have the key.",
    'textOpen': 'You unlock it with the key D you have.',
    'textPass': "You passed the door",
    'type': 'door',
    'unlock' : 'key D'
}

# VARIAVEIS
game_room = {
    'nome' : 'Game Room',
    'texto_objetos': ['couch' , 'piano', 'door A'],
    'objetos':{
        1 : couch,
        2 : piano,
        3 : door_A
    }
}
bedroom1 = {
    'nome': 'Bedroom 1',
    'texto_objetos': ['Queen bed', 'door A', 'door B', 'door C'],
    'objetos': {
        1: queen_bed,
        2: door_A,
        3: door_B,
        4: door_C
    }
}

bedroom2 = {
    'nome': 'Bedroom 2',
    'texto_objetos':['Double bed', 'Dresser', 'door B'],
    'objetos':{
        1: double_bed,
        2: dresser,
        3:door_B
    }
}

living_room = {
    'nome': 'Living Room',
    'texto_objetos':['Dining table', 'door C', 'door D'],
    'objetos':{
        1: dining_table,
        2: door_C,
        3: door_D
    }
}

outside = {
    'nome': 'Outside',
    'texto_objetos': [],
    'objetos':{}
}

GAME_STATE = {
    'room' : game_room,
    'keys' : []
}

# FUNÇÕES
def save_game_state(room, game_state):
    game_state['room'] = room
    new_game_state = game_state
    return new_game_state

def checa_se_pode_passar_pela_porta(keys, how_to_unlock, objetoEscolhido):
    locked = objetoEscolhido['locked']
    if locked == False:
        return True
    else :
        for key in keys:
            if key == how_to_unlock:
                return True
    return False


def explore_room(game_state):
    room = game_state['room']
    nome = room['nome']
    if room == outside:
        return 'game over'

    i = 0
    texto_objetos = room['texto_objetos']
    tamanho_objetos = len(texto_objetos)
    print('Você está em', nome)
    for i in range(len(texto_objetos )):
        print(str(i+1),'-', texto_objetos[i])
    input_do_jogador = input('Escolha uma das opções acima para examinar:\n')
    verifica_input_jogador(input_do_jogador, tamanho_objetos , game_state, room )

def verifica_input_jogador(input_do_jogador, contador, game_state, room ):
    try:
        if (int(input_do_jogador) <= 0) | (int(input_do_jogador) > contador):
            print('Escolha uma das opções acima')
            explore_room(game_state)
        else:
            texto = define_acao(room, input_do_jogador, game_state)
            print(texto)
    except ValueError:
        print("Escolha uma das opções acima")
        explore_room(game_state)

def define_acao(room, contador, game_state):
    objetos = room['objetos']
    objetoEscolhido = objetos[int(contador)]
    tipo = objetoEscolhido['type']
    room = game_state['room']

    if tipo == 'furniture':
        key  = objetoEscolhido['key']
        if key == False:
            text = objetoEscolhido['textFalse']
        else :
            key_get = objetoEscolhido['get']
            text =  objetoEscolhido['textTrue']
            game_state['keys'].append(key_get)
            objetoEscolhido['key'] = False
    elif tipo == 'door':
        pode_passar = open_door(objetoEscolhido, game_state)
        if pode_passar == True:
            objetoEscolhido['locked'] = False
            new_game_state = move(room, objetoEscolhido, game_state)
            explore_room(new_game_state)
            text = ''
        else:
            text = objetoEscolhido['textLocked']
    return text

def move(room, objetoEscolhido, game_state):
    print('Mover para a próxima sala?')
    booleana = False
    room_atual = room['nome']
    new_game_state = game_state
    input1 = input('1 - Sim\n2 - Não\n')
    while booleana == False:
        try:
            if int(input1) == 1:
                if room_atual == 'Game Room':
                    if objetoEscolhido == door_A:
                        next_room = bedroom1
                        new_game_state = save_game_state(next_room , game_state)
                        booleana = True
                elif room_atual == 'Bedroom 1':
                    if objetoEscolhido == door_B:
                        next_room = bedroom2
                        new_game_state = save_game_state(next_room, game_state)
                        booleana = True
                    elif objetoEscolhido == door_C:
                        next_room = living_room
                        new_game_state = save_game_state(next_room, game_state)
                        booleana = True
                    elif objetoEscolhido == door_A:
                        next_room = game_room
                        new_game_state = save_game_state(next_room, game_state)
                        booleana = True
                elif room_atual == 'Bedroom 2':
                    if objetoEscolhido == door_B:
                        next_room = bedroom1
                        new_game_state = save_game_state(next_room,game_state)
                        booleana = True
                elif room_atual == 'Living Room':
                    if objetoEscolhido == door_C:
                        next_room = bedroom1
                        new_game_state = save_game_state(next_room, game_state)
                        booleana = True
                    elif objetoEscolhido == door_D:
                        next_room = outside
                        new_game_state = save_game_state(next_room, game_state)
                        booleana = True
            elif int(input1) == 2:
                new_game_state = save_game_state(room, game_state)
                booleana == True
        except ValueError:
            print("Escolha uma das opções acima")
    return new_game_state

def open_door(objetoEscolhido, game_state):
    locked = objetoEscolhido['locked']
    keys   = game_state['keys']
    how_to_unlock = objetoEscolhido['unlock']
    if locked == True:
        booleana = checa_se_pode_passar_pela_porta(keys,how_to_unlock, objetoEscolhido)
        if booleana == True:
            return True
        else :
            return False
    else:
        return True

def start_game(room):
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    while SAVE_GAME_STATE['room'] != outside:
        game_over  = explore_room(room)
        if game_over == 'game over':
            break
    print('Parabéns você escapou')

SAVE_GAME_STATE = GAME_STATE
start_game(SAVE_GAME_STATE)

