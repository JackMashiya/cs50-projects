def emoji(user_text):
    group = {
        ':1st_place_medal:': '🥇',
        ':candy: or :ice_cream:?': '🍬 or 🍨?',
        ':thumbs_up:': '👍',
        ':thumbsup:': '👍',
        ':earth_asia:': '🌏'

    }

    for x in group:
        if x in user_text:
            user_text = user_text.replace(x, group[x])
    return user_text

def main():
    user = input('Input: ')
    print(f'Output: {emoji(user)}')

main()
