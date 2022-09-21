def who_get_to_21():
    score_sequence = input('Please type in the score (using l L m M): ')
    manu = 0
    luifa = 0
    for letter in score_sequence:
        shot_value = get_points(letter)
        if letter.lower() == 'm':
            manu = manu + shot_value
        else:
            luifa = luifa + shot_value
        if manu >= 21 or luifa >= 21:
            if manu > luifa:
                print("Manu is the winner!")
            else:
                print("Luifa is the winner!")
            print(f"score \nManu: {manu}\nLuifa: {luifa}")
            break
    if manu < 21 and luifa < 21:
        print('In this match, nobody won... check out the score')

def get_points(letter):
    if letter.lower() not in ['m', 'l']:
        return 0
    if letter in ['m', 'l']:
        return 2
    return 3

if __name__ == "__main__":
    who_get_to_21()
