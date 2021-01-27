В период пандемии 2020 все сотрудники Газпром добыча Астрахань должны были отписываться в ватсап ежедневно в 8:30 о состоянии своего здоровья.
Бот крутился на кроне, на raspberry pi =)

crontab -e

DISPLAY=:1.0
XAUTHORITY=/home/pi/.Xauthority
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
30 8 * * * python3 /home/pi/morning_clicker.py
    