import pandas as pd
from faker import Faker
import random

fake = Faker()

# Configurações
num_members = 200000
num_contents = 10000

# Gerar membros
members = []
for _ in range(num_members):
    members.append([
        _,  # ID
        fake.name(),
        fake.email(),
        fake.date_between(start_date='-2y', end_date='today'),
        random.choice(['Free', 'Premium', 'VIP']),
        random.choice(['Active', 'Inactive']),
        fake.country(),
        fake.state(),
        fake.city()
    ])

members_df = pd.DataFrame(members, columns=[
    'ID', 'Name', 'Email', 'Signup_Date', 'Subscription_Type', 'Status', 'Country', 'State', 'City'])

# Gerar conteúdo
contents = []
for i in range(num_contents):
    contents.append([
        i,  # ID
        fake.sentence(nb_words=6),
        random.choice(['Article', 'Video', 'Podcast']),
        fake.date_between(start_date='-2y', end_date='today'),
        fake.name(),
        random.choice(['Technology', 'Health', 'Business', 'Entertainment', 'Education'])
    ])

contents_df = pd.DataFrame(contents, columns=['ID', 'Title', 'Type', 'Publication_Date', 'Author', 'Category'])

# Gerar transações
transactions = []
for member in members_df['ID']:
    num_transactions = random.randint(1, 3)
    for _ in range(num_transactions):
        transactions.append([
            len(transactions),  # ID
            member,
            fake.date_between(start_date='-2y', end_date='today'),
            round(random.uniform(5.0, 200.0), 2),
            random.choice(['Subscription', 'Content Purchase']),
            random.choice(['Credit Card', 'PayPal', 'Bank Transfer']),
            random.choice(['Completed', 'Pending', 'Canceled'])
        ])

transactions_df = pd.DataFrame(transactions, columns=[
    'ID', 'Member_ID', 'Transaction_Date', 'Amount', 'Transaction_Type', 'Payment_Method', 'Transaction_Status'])

# Gerar atividade no site
site_activities = []
for member in members_df['ID']:
    num_activities = random.randint(5, 10)
    for _ in range(num_activities):
        site_activities.append([
            len(site_activities),  # ID
            member,
            fake.date_time_between(start_date='-2y', end_date='now'),
            random.choice(['Login', 'Content View', 'Comment', 'Download']),
            random.randint(1, 180),
            random.choice(['Desktop', 'Mobile', 'Tablet'])
        ])

site_activities_df = pd.DataFrame(site_activities, columns=[
    'ID', 'Member_ID', 'Activity_Date', 'Activity_Type', 'Session_Duration', 'Device'])

# Gerar feedback dos membros
feedbacks = []
for member in members_df['ID']:
    if random.random() < 0.1:  # 10% dos membros deixam feedback
        feedbacks.append([
            len(feedbacks),  # ID
            member,
            fake.date_between(start_date='-2y', end_date='today'),
            random.randint(1, 5),
            fake.sentence(nb_words=12),
            random.choice(['Suggestion', 'Complaint', 'Praise']),
            fake.sentence(nb_words=8)
        ])

feedbacks_df = pd.DataFrame(feedbacks, columns=[
    'ID', 'Member_ID', 'Feedback_Date', 'Rating', 'Comment', 'Feedback_Type', 'Support_Response'])

# Gerar visualizações de conteúdo
content_views = []
for member in members_df['ID']:
    num_views = random.randint(5, 20)
    for _ in range(num_views):
        content_views.append([
            len(content_views),  # ID
            member,
            random.randint(0, num_contents-1),  # Content_ID
            fake.date_between(start_date='-2y', end_date='today'),
            random.randint(1, 60),
            random.choice(['Like', 'Share', 'Comment'])
        ])

content_views_df = pd.DataFrame(content_views, columns=[
    'ID', 'Member_ID', 'Content_ID', 'View_Date', 'View_Duration', 'Interaction_Type'])

# Gerar assinaturas
subscriptions = []
for member in members_df['ID']:
    subscriptions.append([
        len(subscriptions),  # ID
        member,
        fake.date_between(start_date='-2y', end_date='today'),
        fake.date_between(start_date='today', end_date='+2y'),
        random.choice(['Active', 'Expired', 'Canceled'])
    ])

subscriptions_df = pd.DataFrame(subscriptions, columns=[
    'ID', 'Member_ID', 'Start_Date', 'End_Date', 'Subscription_Status'])

# Salvar em arquivos CSV
members_df.to_csv('data/members.csv', index=False)
contents_df.to_csv('data/contents.csv', index=False)
transactions_df.to_csv('data/transactions.csv', index=False)
site_activities_df.to_csv('data/site_activities.csv', index=False)
feedbacks_df.to_csv('data/feedbacks.csv', index=False)
content_views_df.to_csv('data/content_views.csv', index=False)
subscriptions_df.to_csv('data/subscriptions.csv', index=False)

print("Data generation complete.")
