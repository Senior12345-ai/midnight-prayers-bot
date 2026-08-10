import os
import random
import asyncio
from telegram import Bot


# ============================================================
# CHRIS MINISTRIES — AUTOMATIC CHANNEL POSTER
# ============================================================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "@ChrisMinistries")


# ============================================================
# BIBLE VERSES
# ============================================================

BIBLE_VERSES = [
    """📖 Psalm 91:1

"Whoever dwells in the shelter of the Most High
will rest in the shadow of the Almighty." """,

    """📖 Isaiah 41:10

"So do not fear, for I am with you;
do not be dismayed, for I am your God.
I will strengthen you and help you." """,

    """📖 Philippians 4:13

"I can do all this through him who gives me strength." """,

    """📖 Jeremiah 29:11

"For I know the plans I have for you," declares the Lord,
"plans to prosper you and not to harm you,
plans to give you hope and a future." """,

    """📖 Psalm 23:1

"The Lord is my shepherd, I lack nothing." """,

    """📖 Psalm 46:1

"God is our refuge and strength,
an ever-present help in trouble." """,

    """📖 Joshua 1:9

"Be strong and courageous.
Do not be afraid; do not be discouraged,
for the Lord your God will be with you wherever you go." """,

    """📖 Isaiah 43:19

"See, I am doing a new thing!
Now it springs up; do you not perceive it?" """,

    """📖 Psalm 121:7-8

"The Lord will keep you from all harm—
he will watch over your life;
the Lord will watch over your coming and going
both now and forevermore." """,

    """📖 Proverbs 3:5-6

"Trust in the Lord with all your heart
and lean not on your own understanding;
in all your ways submit to him,
and he will make your paths straight." """
]


# ============================================================
# PROPHETIC DECLARATIONS
# ============================================================

DECLARATIONS = [
    """🔥 PROPHETIC DECLARATION

I declare that I am covered by the grace and mercy of God.

I will not be destroyed by the plans of the enemy.

The Lord is my strength, my refuge, and my defender.

I am walking in God's purpose for my life.

I will finish what God has started in me.

In Jesus' mighty name! 🔥🙏""",

    """🔥 PROPHETIC DECLARATION

I declare that every limitation standing against my progress
must give way to the purpose of God.

I receive wisdom, strength, favor, courage,
and divine direction.

I will move forward.

I am entering a new season by God's grace.

In Jesus' name! 🙏🔥""",

    """🔥 PROPHETIC DECLARATION

I declare that fear will not control my life.

I receive courage to face every challenge before me.

God is with me.
God is strengthening me.
God is guiding me.

I will not give up.

I will finish well by the grace of God.

Amen! 🔥🙏""",

    """🔥 PROPHETIC DECLARATION

I declare that doors of divine opportunity
are opening according to God's purpose for my life.

I receive wisdom to recognize the right opportunities
and courage to walk through them.

I will not be distracted from God's purpose.

I am moving forward by grace.

In Jesus' name! 🔥🙏""",

    """🔥 PROPHETIC DECLARATION

I declare that my household is under the covering
and protection of Almighty God.

Peace will reign in my home.

The Lord will guide our decisions,
strengthen our faith,
and order our steps.

We will serve the Lord.

In Jesus' mighty name! 🙏🔥""",

    """🔥 PROPHETIC DECLARATION

I declare that I will not give up in the middle
of what God has started.

I receive strength for today,
wisdom for tomorrow,
and grace for every assignment.

I will finish strong.

I will finish well.

In Jesus' name! 🔥🙏""",

    """🔥 PROPHETIC DECLARATION

I declare that confusion is giving way to divine direction.

My steps are ordered by the Lord.

I receive clarity concerning my decisions,
my work, my relationships,
and my future.

I will walk in wisdom.

In Jesus' name! 🧭🔥🙏""",

    """🔥 PROPHETIC DECLARATION

I declare that the Lord is my provider.

I will walk in wisdom, diligence,
integrity, and faithful stewardship.

I trust God for every legitimate need
and every opportunity He provides.

I will not live in fear of tomorrow.

In Jesus' name! 🙏🔥"""
]


# ============================================================
# CREATE MESSAGE
# ============================================================

def create_post():
    verse = random.choice(BIBLE_VERSES)
    declaration = random.choice(DECLARATIONS)

    return f"""🌙🔥 CHRIS MINISTRIES 🔥🌙

🙏 TAKE A MOMENT AND PRAY

━━━━━━━━━━━━━━━━━━

{declaration}

━━━━━━━━━━━━━━━━━━

{verse}

━━━━━━━━━━━━━━━━━━

🙏 Keep praying.
📖 Keep trusting God's Word.
🔥 Keep your faith alive.

CHRIS MINISTRIES
Preaching the Word • Igniting Prayer

🔥 @ChrisMinistries
"""


# ============================================================
# SEND POST
# ============================================================

async def send_post():

    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is missing. "
            "Add it to GitHub Actions Secrets."
        )

    print("==============================================")
    print("🔥 CHRIS MINISTRIES AUTOMATIC POSTER")
    print("==============================================")
    print(f"📢 Channel: {CHANNEL_USERNAME}")
    print("📖 Bible verse: READY")
    print("🔥 Declaration: READY")
    print("==============================================")

    message = create_post()

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text=message
    )

    print("✅ Post successfully sent to Telegram channel.")
    print("==============================================")


# ============================================================
# MAIN
# ============================================================

def main():
    asyncio.run(send_post())


if __name__ == "__main__":
    main()
