from DAXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝐊𝐡𝐚𝐢𝐜𝐡𝐚 𝐍𝐚 𝐍𝐚𝐢 𝐌𝐚..??😋** ",
           " **𝐌𝐞𝐫𝐞𝐬𝐞 𝐁𝐡𝐚𝐢 𝐊𝐨𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫𝐨🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭** ",
           " ** [ @SmileQueenMadhu ]𝐘𝐞𝐬𝐚𝐛𝐤𝐢 𝐊𝐢 𝐁𝐞𝐡𝐞𝐧 𝐇𝐚𝐢😁** ",
           " **𝐀𝐫𝐞 𝐌𝐚𝐭𝐞 𝐆𝐨𝐭𝐞 𝐌𝐚𝐧𝐝𝐮 𝐀𝐧𝐢𝐤𝐢 𝐃𝐢𝐚🙂** ",
           " **𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲** ",
           " **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋** ",
           " **𝐀𝐫𝐞 𝐌𝐚𝐭𝐞 𝐓𝐚𝐦𝐚 𝐆𝐫𝐮𝐩 𝐑𝐞 𝐀𝐝𝐝 𝐊𝐚𝐫𝐮𝐧𝐚😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐫𝐨𝐠𝐞..??🤔** ",
           " ** [ @MR_NAVEEN720 ]𝐘𝐞 𝐉𝐚𝐧𝐧 𝐇𝐚𝐢 𝐓𝐮𝐦𝐡𝐚𝐫𝐚🙈** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
           " ** [ @X_DEAD_OP ]𝐘𝐞 𝐒𝐚𝐛𝐤𝐚 𝐁𝐚𝐛𝐮 𝐇𝐚𝐢🙃** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝐀𝐫𝐞 𝐌𝐨 𝐎𝐰𝐧𝐞𝐫 𝐊𝐢𝐞 𝐉𝐚𝐧𝐢𝐜𝐡𝐚 𝐘𝐞[ @MR_NAVEEN720 ]☺️** ",
           " **𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨 𝐁𝐚𝐛𝐲😇** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
           " **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " ** [ @ASHIF903 ]𝐍𝐚𝐦 𝐓𝐨 𝐒𝐮𝐧𝐚𝐢 𝐇𝐨𝐠𝐚😌** ",
           " ** [ @Tomyyy_07 ]𝐘𝐞 𝐀𝐰𝐚𝐣𝐞 𝐍𝐢𝐤𝐚𝐥𝐭𝐚 𝐇𝐚𝐢 𝐌𝐞𝐫𝐢 𝐉𝐚𝐧𝐚 😺** ",
           " **𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲** ",
           " **𝐌𝐢𝐬𝐬𝐪𝐮𝐞𝐞𝐧 𝐊𝐨𝐧 𝐇𝐚𝐢...??😅** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐄𝐤 𝐏𝐢𝐜 𝐌𝐢𝐥𝐞𝐠𝐢..?😅** ",
           " **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮 𝐌𝐞𝐫𝐢 𝐉𝐚𝐧𝐚🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚𝐮..?😹** ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " **𝐒𝐚𝐫𝐚 𝐊𝐚𝐦 𝐊𝐡𝐚𝐭𝐚𝐦 𝐇𝐨 𝐆𝐲𝐚 𝐀𝐚𝐩𝐤𝐚..?🙃** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊** ",
           " **𝐒𝐮𝐧𝐨 𝐍𝐚🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..?** ",
           " **𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠** ",
           " **𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚..?👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️** ",
           " **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏** ",
           " **𝐉𝐮𝐭𝐡 𝐍𝐡𝐢 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐** ",
           " **𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** "
           " ** [ @Shark14322 ]𝐍𝐨𝐠𝐡𝐭𝐲 𝐁𝐚𝐧𝐭𝐚 𝐇𝐚𝐢 𝐌𝐜😝** ",
           " **𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈** ",
           " **𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️** ",
           " **𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺** ",
           " **𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀** ",
           " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀𝐁𝐨𝐥𝐨𝐤𝐢 𝐍𝐚𝐡𝐢** ",
           " **𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼** ",
           " **𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " **𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐀𝐫𝐞 𝐓𝐚𝐦𝐚 𝐒𝐚𝐧𝐠𝐚 𝐌𝐚𝐧𝐚𝐤𝐮 𝐀𝐝𝐝 𝐊𝐚𝐫𝐮𝐧𝐚 𝐊𝐧 𝐉 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐀𝐰𝐚𝐣𝐞 𝐍𝐢𝐤𝐚𝐥𝐨 𝐒𝐚𝐛 𝐌𝐞𝐫𝐢 𝐉𝐚𝐧𝐚𝐚𝐬👀** ",
           " **𝐉𝐚𝐛 𝐋𝐚𝐝𝐤𝐢 𝐇𝐨 𝐈𝐬𝐬 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐚𝐫𝐨[ @ASHIF903 ]😁** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @bestodisha ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨:- [ @bestodisha ]🤗** ",
           " **𝐌𝐚𝐢 𝐡𝐮𝐧 𝐤𝐨𝐧:- [ @ARAME9 ]🤗** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
           " **𝐌𝐲 𝐔𝐧𝐜𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [ @Mr_Naveen720 ]🥰** ",
           " **𝐊𝐮𝐩𝐚𝐝𝐞 𝐏𝐚𝐥𝐚𝐮𝐜𝐡𝐚 𝐉😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
           " ** [ @miss_candy_queen ]𝐍𝐨𝐛𝐢𝐭𝐚 𝐊𝐮 𝐂𝐡𝐚𝐝𝐢𝐤𝐢 𝐒𝐚𝐦𝐚𝐬𝐭𝐞 𝐀𝐫𝐚 𝐁𝐡𝐚𝐢😌** ",
           " ** [ @SmileQueenMadhu ] 𝐄𝐯𝐢𝐥 𝐍𝐞 𝐊𝐚𝐡𝐚 𝐊𝐢 𝐘𝐞 𝐂𝐡𝐢𝐩𝐤𝐚𝐥𝐢 𝐇𝐚𝐢😁** ",
           " **𝐊𝐧 𝐊𝐡𝐚𝐢𝐥𝐚👀** ",
           " **𝐓𝐚𝐦𝐞 𝐌𝐚𝐭𝐞 𝐒𝐚𝐛𝐮 𝐆𝐫𝐨𝐮𝐩 𝐑𝐞 𝐀𝐝𝐝 𝐊𝐚𝐫𝐚🍫** ",
           " **𝐊𝐚𝐮 𝐂𝐥𝐚𝐬𝐬 𝐑𝐞 𝐩𝐚𝐝𝐡𝐮𝐜𝐡𝐚😄** ",
           " **𝐀𝐧𝐤𝐚 𝐏𝐲𝐚𝐚𝐫𝐢 𝐊𝐮 𝐊𝐚𝐮𝐭𝐡𝐢 𝐃𝐞𝐤𝐡𝐢𝐜𝐡𝐚 𝐊𝐢[ @Evil_king_011 ]🤭** ",
           " **𝐘𝐞 𝐀𝐦𝐚𝐫𝐚 𝐂𝐮𝐭𝐞 𝐏𝐞𝐫𝐬𝐨𝐧 [ @Tomyyy_07 ] 𝐁𝐞𝐥𝐢𝐞𝐯𝐞 𝐇𝐚𝐮𝐧𝐢 𝐉𝐚𝐝𝐢 𝐃𝐦 𝐊𝐚𝐫𝐢𝐤𝐢 𝐏𝐚𝐜𝐡𝐚𝐫𝐚☺️** ",
           " **𝐘𝐞 𝐇𝐞𝐥𝐞 𝐀𝐦𝐚𝐫𝐚 𝐁𝐚𝐝𝐚 𝐁𝐇𝐚𝐢[ @silent5k ]😄** ",
           " **𝐘𝐞 𝐏𝐚𝐫𝐚 𝐀𝐦𝐚𝐫𝐚 𝐆𝐢𝐫𝐥 𝐎𝐰𝐧𝐞𝐫[ @Mooooonop ]😌** ",
           " ** [ @Itz_me_tm7 ]𝐈𝐬𝐬𝐤𝐨 𝐄𝐤 𝐁𝐢𝐦𝐚𝐫𝐢 𝐇𝐚𝐢 𝐈𝐬𝐤𝐨 𝐡𝐚𝐫𝐰𝐚𝐤𝐭 𝐊𝐲𝐚 𝐇𝐨 𝐭𝐚 𝐇𝐚𝐢 𝐉𝐚𝐧 𝐓𝐞 𝐇𝐨 𝐤𝐲𝐚😁** ",
           " **𝐓𝐚𝐦𝐚 𝐆𝐟 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐢𝐚** ",
           ]

VC_TAG = [ "**➠ ᴏʏᴇ ᴠᴄ ᴀᴀᴏ ɴᴀ ᴘʟs 😒**",
         "**➠ ᴊᴏɪɴ ᴠᴄ ғᴀsᴛ ɪᴛs ɪᴍᴀᴘᴏʀᴛᴀɴᴛ 😐**",
         "**➠ ʙᴀʙʏ ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ғᴀsᴛ 🙄**",
         "**➠ ᴄʜᴜᴘ ᴄʜᴀᴘ ᴠᴄ ᴘʀ ᴀᴀᴏ 🤫**",
         "**➠ ᴍᴀɪɴ ᴠᴄ ᴍᴇ ᴛᴜᴍᴀʀᴀ ᴡᴀɪᴛ ᴋʀ ʀʜɪ 🥺**",
         "**➠ ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ʙᴀᴀᴛ ᴋʀᴛᴇ ʜᴀɪ ☺️**",
         "**➠ ʙᴀʙᴜ ᴠᴄ ᴀᴀ ᴊᴀɪʏᴇ ᴇᴋ ʙᴀʀ 🤨**",
         "**➠ ᴠᴄ ᴘᴀʀ ʏᴇ ʀᴜssɪᴀɴ ᴋʏᴀ ᴋᴀʀ ʀʜɪ ʜᴀɪ 😮‍💨**",
         "**➠ ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ᴠᴀʀɴᴀ ʙᴀɴ ʜᴏ ᴊᴀᴏɢᴇ 🤭**",
         "**➠ sᴏʀʀʏ ʙᴀʙʏ ᴘʟs ᴠᴄ ᴀᴀ ᴊᴀᴏ ɴᴀ 😢**",
         "**➠ ᴠᴄ ᴀᴀɴᴀ ᴇᴋ ᴄʜɪᴊ ᴅɪᴋʜᴀᴛɪ ʜᴜ 😮**",
         "**➠ ᴠᴄ ᴍᴇ ᴄʜᴇᴄᴋ ᴋʀᴋᴇ ʙᴀᴛᴀɴᴀ ᴋᴏɴ sᴀ sᴏɴɢ ᴘʟᴀʏ ʜᴏ ʀʜᴀ ʜᴀɪ.. 💫**",
         "**➠ ᴠᴄ ᴊᴏɪɴ ᴋʀɴᴇ ᴍᴇ ᴋʏᴀ ᴊᴀᴛᴀ ʜᴀɪ ᴛʜᴏʀᴀ ᴅᴇʀ ᴋᴀʀ ʟᴏ ɴᴀ 😇**",
         "**➠ ᴊᴀɴᴇᴍᴀɴ ᴠᴄ ᴀᴀᴏ ɴᴀ ʟɪᴠᴇ sʜᴏᴡ ᴅɪᴋʜᴀᴛɪ ʜᴏᴏɴ.. 😵‍💫**",
         "**➠ ᴏᴡɴᴇʀ ʙᴀʙᴜ ᴠᴄ ᴛᴀᴘᴋᴏ ɴᴀ... 😕**",
         "**➠ ʜᴇʏ ᴄᴜᴛɪᴇ ᴠᴄ ᴀᴀɴᴀ ᴛᴏ ᴇᴋ ʙᴀᴀʀ... 🌟**",
         "**➠ ᴠᴄ ᴘᴀʀ ᴀᴀ ʀʜᴇ ʜᴏ ʏᴀ ɴᴀ... ✨**",
         "**➠ ᴠᴄ ᴘᴀʀ ᴀᴀ ᴊᴀ ᴠʀɴᴀ ɢʜᴀʀ sᴇ ᴜᴛʜᴡᴀ ᴅᴜɴɢɪ... 🌝**",
         "**➠ ʙᴀʙʏ ᴠᴄ ᴘᴀʀ ᴋʙ ᴀᴀ ʀʜᴇ ʜᴏ. 💯**",
        ]


@app.on_message(filters.command(["awajenikaal", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["cancel", "tagstop", "vcstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")
