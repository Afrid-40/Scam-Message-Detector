import pandas as pd
import random
import os

random.seed(42)

safe_messages = [
    "Hey, are we still meeting tomorrow?",
    "Your order has been shipped and will arrive tomorrow.",
    "Reminder: your appointment is scheduled for 10 AM.",
    "Can you send me the project report?",
    "Your electricity bill is ready to view in the official app.",
    "Thanks for your payment. Your transaction was successful.",
    "Your OTP for login is 483921. Do not share it with anyone.",
    "Your Amazon order has been delivered.",
    "Meeting has been moved to 3 PM.",
    "Your monthly statement is now available.",
    "Please call me when you reach home.",
    "Happy birthday! Have a wonderful day.",
    "Your college assignment deadline is tomorrow.",
    "The package you ordered is out for delivery.",
    "Your train ticket booking is confirmed."
]

scam_messages = [
    "Congratulations! You have won ₹50,000. Click this link to claim your prize.",
    "URGENT! Your bank account will be blocked. Verify your account immediately.",
    "You have been selected for a cash reward of ₹1,00,000. Claim now.",
    "Your account has been suspended. Click here to restore access.",
    "WINNER! You have won a brand new iPhone. Send your details to claim.",
    "Your ATM card will be blocked today. Call this number immediately.",
    "Congratulations! You are eligible for a guaranteed loan. Pay processing fee now.",
    "Your KYC has expired. Update immediately using this link.",
    "You won a lottery prize of ₹25,00,000. Pay the tax to receive your money.",
    "URGENT: suspicious activity detected. Verify your banking details now.",
    "Exclusive job opportunity! Earn ₹50,000 per month from home. Pay registration fee.",
    "Your UPI account is at risk. Click the link to secure your account.",
    "You have received a reward. Provide your OTP to confirm the transaction.",
    "FINAL NOTICE! Your account will be permanently deleted today.",
    "Claim your free gift card now. Limited time offer!"
]

# Generate additional variations
safe_variations = [
    "Please check the document I sent you.",
    "The class starts at 9 AM tomorrow.",
    "Your payment receipt is available.",
    "Don't forget to bring your ID card.",
    "Can you share the meeting link?",
    "Your subscription has been renewed successfully.",
    "The delivery agent will arrive shortly.",
    "Your exam results are now available.",
    "Please confirm your attendance for tomorrow.",
    "Your reservation has been confirmed."
]

scam_variations = [
    "Click now to receive your free reward.",
    "Act immediately to avoid account suspension.",
    "Send your OTP to verify your prize.",
    "Pay a small fee to unlock your reward.",
    "Your bank account needs urgent verification.",
    "You have won a special cash bonus.",
    "Claim your exclusive reward before it expires.",
    "Verify your card details immediately.",
    "Limited offer! Send your information now.",
    "Your account has suspicious activity. Click here now."
]

safe_messages.extend(safe_variations)
scam_messages.extend(scam_variations)

data = []

# Create 500 safe messages
for _ in range(500):
    message = random.choice(safe_messages)
    data.append([message, 0])

# Create 500 scam messages
for _ in range(500):
    message = random.choice(scam_messages)
    data.append([message, 1])

# Shuffle dataset
random.shuffle(data)

df = pd.DataFrame(
    data,
    columns=["message", "label"]
)

# Save dataset
output_path = os.path.join(
    os.path.dirname(__file__),
    "messages.csv"
)

df.to_csv(output_path, index=False)

print("Dataset created successfully!")
print(f"Number of messages: {len(df)}")
print("\nClass distribution:")
print(df["label"].value_counts())

print("\nFirst 5 rows:")
print(df.head())