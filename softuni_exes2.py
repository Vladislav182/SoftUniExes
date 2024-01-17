team = input()
souvenir = input()
count_souvenirs = int(input())
total_sum = 0
if (team == 'Argentina' or team == 'Brazil' or team == 'Croatia' or team == 'Denmark') and (souvenir == 'flags' or souvenir == 'caps' or souvenir == 'posters' or souvenir == 'stickers'):
    if team == 'Argentina':
        if souvenir == 'flag':
            total_sum = 3.25 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 7.20 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 5.10 * count_souvenirs
        elif souvenir == 'stickers':
            total_sum = 1.25 * count_souvenirs



    elif team == 'Brazil':
        if souvenir == 'flag':
            total_sum = 4.20 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 8.50 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 5.35 * count_souvenirs
        elif souvenir == 'stickers':
            total_sum = 1.20 * count_souvenirs




    elif team == 'Croatia':
        if souvenir == 'flag':
            total_sum = 2.75 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 6.90 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 4.95 * count_souvenirs
        elif souvenir == 'stickers':
            total_sum = 1.10 * count_souvenirs



    elif team == 'Denmark':
        if souvenir == 'flag':
            total_sum = 3.10 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 6.50 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 4.80 * count_souvenirs
        elif souvenir == 'stickers':
            total_sum = 0.90 * count_souvenirs
    print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {total_sum}")
elif not team == ('Argentina' or team == 'Brazil' or team == 'Croatia' or team == 'Denmark'):
    print("Invalid country!")
elif not souvenir == (souvenir == 'flags' or souvenir == 'caps' or souvenir == 'posters' or souvenir == 'stickers'):
    print("Invalid stock!")

