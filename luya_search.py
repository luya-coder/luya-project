from playsound import playsound
from ursina import *
import pygame
import random 
from time import sleep
import pyautogui
import os
import sys
from random import randint
from tkinter import *
import tkinter
from time import strftime
from tkinter.ttk import*
from pymsgbox import NO_TEXT, YES_TEXT
import requests
import tkinter as tk
import time
db = {}
print('starting')
import os
from tkinter import Tk, Label
from tkinter import *
print('Copyright (c) 2021 luya corparation. All rights reserved.')
playsound = playsound
while True:
    print('search anything')
    action = input()
    if action == 'data':
        k = input('code: ')
        d = input('input a word: ')
        db[k] = d
    elif action == 'word':
        k = input('code: ')
        if not k in db:
            print('wrong code')
        else:
            print('your data: %s' % db[k])
    elif action == 'L':
        print('DB contents:')
        print(db)
    elif action == 'disagree':
        sys.exit
    elif action == 'start edge':
        print('now opennig msedge')
        os.startfile("msedge.exe")
    elif action == 'pubg':
        playsound('D://Music/pubg mobile song mongolia.mp3')
    elif action == 'unaa':
        playsound('D://Music/Gee & Desant - Unaa (Micronii Boss OST).mp3')
    elif action == 'huuhdeeree boy':
        playsound('D://Music/Vande - Huuhdeeree Boy -Monstar Live.mp3')
    elif action == 'man on the moon':
        playsound('D://Music/Vandebo & Man On The Moon - Duuren (Official Music Video).mp3')
    elif action == 'nasa':
        playsound('D://Music/BABU - NASA [Official music video].mp3')
    elif action == 'zogsohgui':
        playsound('D://Music/zogsohgui.mp3')
    elif action == 'dandaa daardag ohin':
        playsound('D://Music/ThunderZ - Dandaa Daardag Ohin (Official Music Video).mp3')
    elif action == 'dungundangan':
        playsound('D://Music/Vandebo - Dungun Dangan ft. Saryuna (Official Music Video).mp3')
    elif action == 'zamen':
        playsound('D://Music/Vandebo - Zamen (Official Music Video) BRATAN OST.mp3')
    elif action == 'oyutan':
        playsound('D://music/ThunderZ - Oyutan (Official Music Video).mp3')
    elif action == 'dajgui baival yaahuu':
        playsound('D://Music/ThunderZ - Dajgui Baival Yah Uu_ (Official Music Video).mp3')
    elif action == 'er hun shig er hun bai':
        playsound('D://Music/ThunderZ - Er hun shig er hun bai (Official Music Video).mp3')
    elif action == 'shaasangui':
        playsound('D://Music/ThunderZ - Shaasangui (Official Music Video).mp3')
    elif action == 'late night':
        playsound('D://Music/Vandebo, Fla - Late Night (Official Lyric Video).mp3')
    elif action == 'haru haru':
        playsound('D://Music/Vandebo x Anir - Haru Haru (Official Video).mp3')
    elif action == 'boroo':
        playsound('D://Music/Ginjin & Mrs M - Boroo (Official Music Video).mp3')
    elif action == 'atm':            
        print('atm now playing')
        playsound('D://Music/Ginjin & Mrs M - ATM (Official Music Video).mp3')
    elif action == 'suvgaa soli':
        while True:
            print(' now playing')
            playsound('D://Music/Ginjin - Suvgaa Soli ft. Mrs M (Official Music Video).mp3')
    elif action == 'ping pong':
        app = Ursina()
        window.color = color.olive
        table = Entity(
            model='cube',
            color=color.black,
            scale=(2,1,3),
            rotation=(90,0,0)
        )
        ball = Entity(
           model='sphere',
           color=color.cyan,
           z=-1,
           scale=0.1,
           collider='box'
        )
        player1 = Entity(
            model='cube',
            color=color.cyan,
            scale=(0.6,0.1,1),
            position=(0,-1.4,-1),
            collider='box'
        )
        player2 = duplicate(player1, y=1.4)

        speed_x = speed_y = 0.5

        def update():
            global speed_x, speed_y
            player1.x += held_keys['d'] * time.dt
            player1.x -= held_keys['a'] * time.dt
            player2.x += held_keys['right arrow'] * time.dt
            player2.x -= held_keys['left arrow'] * time.dt
            ball.x += speed_x * time.dt
            ball.y += speed_y * time.dt
            if abs(ball.x) > 0.9:
                speed_x = -speed_x
            if abs(ball.y) > 1.4:
                ball.x = ball.y = 0
            if ball.intersects().hit:
                speed_y = -speed_y
                speed_x *= 1.1
                speed_y *= 1.1


        camera.orthographic = True
        camera.fov= 4

        app.run()
    elif action == 'weather':
        def getWeather(canvas):
            city = textField.get()
                
            api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            temp = int(json_data['main']['temp'] - 273.15)
            min_temp = int(json_data['main']['temp_min'] - 273.15)
            max_temp = int(json_data['main']['temp_max'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
            sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

            final_info = condition + "\n" + str(temp) + "°C" 
            final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
            label1.config(text = final_info)
            label2.config(text = final_data)


        canvas = tk.Tk()
        canvas.geometry("600x500")
        canvas.title("luya Weather App")
        f = ("poppins", 15, "bold")
        t = ("poppins", 35, "bold")

        textField = tk.Entry(canvas, justify='center', width = 20, font = t)
        textField.pack(pady = 20)
        textField.focus()
        textField.bind('<Return>', getWeather)

        label1 = tk.Label(canvas, font=t)
        label1.pack()
        label2 = tk.Label(canvas, font=f)
        label2.pack()
        canvas.mainloop() 
    elif action == 'bn uu':
        print('bn bn')
    elif action == 'bingo':
        for i in range(5):
            number = randint(10,99)
            print("The newly generated number is %s" % number)
            if (number > 75 ):
               print("Better luck next time")
        else:
            print("Bingo!!!, You are the winner")
            break
    elif action == 'restart':
        sleep(5)
        continue

    elif action == 'hi':
        print('okay')
    elif action == 'youtube':
        os.startfile('http://youtube.com')
    elif action == 'play mix':
        os.startfile('https://www.youtube.com/watch?v=Gcpp5uHMsbY&list=RDGcpp5uHMsbY&index=1')
    elif action == 'facebook':
        os.startfile('https://facebook.com')
    elif action == 'messenger':
        os.startfile('https://mesenger.com')
    elif action == 'turn off':
        print('turned off')
        sleep(5)

        if input() == 'turn on':
            continue
    elif action == 'add user':
        k = input('code: ')
        d = input('user name: ')
        db[k] = d
    elif action == 'login':
        k = input('code: ')
        if not k in db:
            print('wrong code')
        else:
            print('your code: %s' % db[k])
        print('code:')
        print(db)
    
    elif action == 'plan a':
        print('plan a open youtube and play superster')
        os.startfile('https://youtube.com')
        playsound('d://Music/Ebo x Tengo - SupaSTA (Official Music Video).mp3')
    elif action == 'snooze without playsound':
        print('no sound 10 minute')
        sleep(600)
    elif action == 'haha1':
        print('you can up more like this == haha2')
        os.startfile('d://funny screen shots/haha1.jpg')
    elif action == 'playsound':
      print('nasa')
      playsound('D://Music/BABU - NASA [Official music video].mp3')
      print('yaasan')                                                                       
      playsound('D://Music/Big Gee - Yaasan (Official Music Video).mp3')
      print('born to rap')
      playsound('D://Music/Born Rap.mp3')
      print('supesta')
      playsound('D://Music/Ebo x Tengo - SupaSTA (Official Music Video).mp3')
      print('mnad hony')
      playsound('D://Music/FLA - Manaid Honoy ft. Vandebo (Official Music Video).mp3')
      print('mogjoohon huu')
      playsound('D://Music/Gangbay - Mogjookhon Khuu (Official Video) Directed by Sanga.mp3')
      print('suvgaa soli')
      playsound('D://Music/Ginjin - Suvgaa Soli ft. Mrs M (Official Music Video).mp3')
      print('atm')
      print('fall in love')
      playsound('D://Music/O.Z - Fall in Love (Official Music Video).mp3')
      print('pubg song')
      playsound('D://Music/pubg mobile song mongolia.mp3')
      print('dajgu bval yaahuu')
      playsound('D://Music/ThunderZ - Dajgui Baival Yah Uu_ (Official Music Video)_256k.mp3')
      print('dandaa daardag ohin')
      playsound('D://Music/ThunderZ - Dandaa Daardag Ohin (Official Music Video).mp3')
      print('oyutan')
      playsound('D://Music/ThunderZ - Oyutan (Official Music Video).mp3')
      print('shaasangui')
      playsound('D://Music/ThunderZ - Shaasangui (Official Music Video).mp3')
      print('bi chinii nz zaluu bj bolohuu')
      playsound('D://Music/ThunderZ, Bilgang - Bi Chinii Naiz Zaluu Baij Bolhuu (Official Music Video).mp3')
      print('tomm reves')
      playsound('D://Music/Tomm - Reves (Official Audio) ft. Vandebo.mp3')
      print('minii puuz')
      playsound('D://Music/TsetseMinii puuz.mp3')
      print('huuhdeeree boy')
      playsound('D://Music/Vande - Huuhdeeree Boy Monstar Live.mp3')
      print('nadad itgeeree')
      playsound('D://Music/Vande - Nadad Itgeerei ft. FLA (Official Music Video).mp3')
      print('3r tun')
      playsound('D://Music/Vandebo - 3r Tun (Official Video).mp3')
      print('18 savage')
      playsound('D://Music/Vandebo - 18 Savage (Official Music Video).mp3')
      print('aaban beeben')
      playsound('D://Music/Vandebo - Aaban Beeben (Official Lyric Video) ft. Tomm.mp3')
      print('buruugui')
      playsound('D://Music/Vandebo - Buruugui (Official Music Video) prod.by 976Beatz.mp3')
      print('chadahguinee')
      playsound('D://Music/Vandebo - Chadahguinee (Official Music Video) - 2019.mp3')
      print('chamin ym')
      playsound('D://Music/Vandebo - Chamin Yum (Official Lyric Video).mp3')
      print('dungun dangan')
      playsound('D://Music/Vandebo - Dungun Dangan ft. Saryuna (Official Music Video).mp3')
      print('galt tereg')
      playsound('D://Music/Vandebo - Galt Tereg (Official Music Video).mp3')
      print('hair')
      playsound('D://Music/Vandebo - Hair (Official Music Video).mp3')
      l = print
      l('huuhdiin 100')
      playsound('D://Music/Vandebo - Huuhdiin 100 (Official Music Video).mp3')
      l('k.o')
      playsound('D://Music/Vandebo - K.O (Official Music Video).mp3')
      l('mangar tom zurh')
      playsound('D://Music/Vandebo - Mangar Tom Zurh (Official Audio).mp3')
      l('mid')
      playsound('D://Music/Vandebo - Mid (Official Audio).mp3')
      l('namaig too')
      playsound('D://Music/Vandebo - Namaig Too (Official Music Video).mp3')
      l('no1')
      playsound('D://Music/Vandebo - NO1 (Official Music Video).mp3')
      l('olon')
      playsound('D://Music/Vandebo - Olon (Official Audio).mp3')
      l('sain bodoj uzsenuu')
      playsound('D://Music/Vandebo - Sain Bodoj Uzsen Uu (Official Music Video).mp3')
      l('suun zam')
      playsound('D://Music/Vandebo - Suun Zam (Official Music Video).mp3')
      l('trap bank')
      playsound('D://Music/Vandebo - Trap Bank (Official Music Video).mp3')
      l('yaanaa')
      playsound('D://Music/Vandebo - Yaanaa (Official Music Video).mp3')
      l('zamen')
      playsound('D://Music/Vandebo - Zamen (Official Music Video) BRATAN OST.mp3')
      l('man on the moon')
      playsound('D://Music/Vandebo & Man On The Moon - Duuren (Official Music Video).mp3')
      l('unana')
      playsound('D://Music/Vandebo ft. Enerel - Unana (Official Music Video).mp3')
      l('haru haru')
      playsound('D://Music/Vandebo x Anir - Haru Haru (Official Video).mp3')
      l('odoo yarii')
      playsound('D://Music/Vandebo x Anir - Odoo Yarii (Official Quarantine Video).mp3')
      l('ayo')
      playsound('D://Music/Vandebo X Bold - AYO (Official Music Video).mp3')
      l('late night')
      playsound('D://Music/Vandebo, Fla - Late Night (Official Lyric Video).mp3')
      l('zogsohgui')
      playsound('D://Music/zogsoghui.mp3')
      l('thanks for listenning')
    elif action == 'fix error genuine':
        os.startfile('notepad')
        sleep(5)
        pyautogui.typewrite('fix error genuine')
        sleep(1)
        pyautogui.typewrite('ver == 1.0')
        sleep(1)
        pyautogui.typewrite('started')
        sleep(1)
        os.startfile('cmd')
        sleep(4)
        pyautogui.typewrite('slmgr -rearm')
        sleep(1)
        pyautogui.press('enter')
    elif action == 'games':
        print('snake, ghost door flower we will add some games')
    elif action == 'flower':
        import turtle
        for i in range(50):
            turtle.forward(300)
            turtle.left(170)
        turtle.done()
    elif action == 'ghost door':
        print('ghost door by luya')
        score = 0
        feeling_brave = True
        while feeling_brave:
            ghost_door = randint(1, 3)
            print('three doors given')
            print('ghost behind one')
            print('choose your door 1 to 3')
            door = input('1, 2, 3')
            door_num = int(door)
            if door_num == ghost_door:
                print('u are unlucky by YOU')
                feeling_brave = False
            else:
                print('no ghost')
                score = score + 1
        print('game OVER you scored', score)
    elif action == 'game':
        table = 7
        for i in range(1, 13):
            print('what\'s', i, 'x', table, '?')
            guess = input()
            if guess == 'stop':
               break
            if guess == 'exit':
                break
            if guess == 'skip':
                print('skiped')
                continue
            ans = i * table
            if int (guess) == ans:
                 print('correct')
            else:
                print('no it\'s', ans)
        print('finished')
    elif action == 'exit':
        print('byebye')
        break
    elif action == 'snake':
        pygame.init()
        white = (255, 255, 255)
        yellow = (255, 255, 102)
        black = (0, 0, 0)
        red = (213, 50, 80)
        green = (0, 255, 0)
        blue = (50, 153, 213)
        dis_width = 600
        dis_height = 400
        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game by ariunbold')
        clock = pygame.time.Clock()
        snake_block = 10
        snake_speed = 15
        font_style = pygame.font.SysFont("bahnschrift", 25)
        score_font = pygame.font.SysFont("comicsansms", 35)
        def our_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])
        def gameLoop():
            game_over = False
            game_close = False
            x1 = dis_width / 2
            y1 = dis_height / 2
            x1_change = 0
            y1_change = 0
            snake_List = []
            Length_of_snake = 1
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            while not game_over: 
                while game_close == True:
                    dis.fill(blue)
                    message("You Lost! Press C-Play Again or Q-Quit", red)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0
                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(blue)
                pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]
                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True
                our_snake(snake_block, snake_List)
                pygame.display.update()
                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1
                clock.tick(snake_speed)
            pygame.quit()
            gameLoop()