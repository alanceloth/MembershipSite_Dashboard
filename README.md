# Membership Site Dashboard

[Dashboard Tableau Public link](https://public.tableau.com/views/membership_site_dashboard/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)



This project creates a comprehensive dashboard for a membership site, utilizing a synthetic dataset generated with the Faker library. The dashboard provides key insights into member activities, transactions, content interactions, and feedback.

## Project Overview

The primary objective of this project is to demonstrate data analysis and visualization skills by creating a dashboard that showcases the performance of a membership site. The dataset includes multiple related tables to simulate real-world data scenarios.

## Dataset Description

![image](docs/imgs/Membership%20Site.png)

The dataset consists of the following tables:

1. **Members**
    - `ID`: Integer, Primary Key
    - `Name`: String
    - `Email`: String
    - `Signup_Date`: Date
    - `Subscription_Type`: String (Free, Premium, VIP)
    - `Status`: String (Active, Inactive)
    - `Country`: String
    - `State`: String
    - `City`: String

2. **Transactions**
    - `ID`: Integer, Primary Key
    - `Member_ID`: Integer, Foreign Key
    - `Transaction_Date`: Date
    - `Amount`: Float
    - `Transaction_Type`: String (Subscription, Content Purchase)
    - `Payment_Method`: String (Credit Card, PayPal, Bank Transfer)
    - `Transaction_Status`: String (Completed, Pending, Canceled)

3. **Site Activity**
    - `ID`: Integer, Primary Key
    - `Member_ID`: Integer, Foreign Key
    - `Activity_Date`: DateTime
    - `Activity_Type`: String (Login, Content View, Comment, Download)
    - `Session_Duration`: Integer (in minutes)
    - `Device`: String (Desktop, Mobile, Tablet)

4. **Member Feedback**
    - `ID`: Integer, Primary Key
    - `Member_ID`: Integer, Foreign Key
    - `Feedback_Date`: Date
    - `Rating`: Integer (1-5)
    - `Comment`: String
    - `Feedback_Type`: String (Suggestion, Complaint, Praise)
    - `Support_Response`: String

5. **Content**
    - `ID`: Integer, Primary Key
    - `Title`: String
    - `Type`: String (Article, Video, Podcast)
    - `Publication_Date`: Date
    - `Author`: String
    - `Category`: String

6. **Content Views**
    - `ID`: Integer, Primary Key
    - `Member_ID`: Integer, Foreign Key
    - `Content_ID`: Integer, Foreign Key
    - `View_Date`: Date
    - `View_Duration`: Integer (in minutes)
    - `Interaction_Type`: String (Like, Share, Comment)

7. **Subscriptions**
    - `ID`: Integer, Primary Key
    - `Member_ID`: Integer, Foreign Key
    - `Start_Date`: Date
    - `End_Date`: Date
    - `Subscription_Status`: String (Active, Expired, Canceled)

## Metrics and Visualizations

### Key Metrics

1. **Total Active Members**
    - Number of members with status "Active".

2. **New Members**
    - Number of new members registered over a specific period.

3. **Cancellation Rate**
    - Percentage of canceled subscriptions.

4. **Distribution of Subscription Types**
    - Percentage of members in each subscription type (Free, Premium, VIP).

5. **Monthly Recurring Revenue (MRR)**
    - Monthly revenue from subscriptions.

6. **Average Subscription Duration**
    - Average time members stay subscribed.

7. **Total Revenue**
    - Total revenue generated from transactions.

8. **Average Transaction Value**
    - Average value of transactions.

9. **Total Site Activities**
    - Number of activities on the site.

10. **Average Session Duration**
    - Average time spent per session.

11. **Device Distribution**
    - Percentage of activities by device type (Desktop, Mobile, Tablet).

12. **Most Viewed Content**
    - Content with the highest number of views.

13. **Average View Duration**
    - Average time spent viewing content.

14. **Average Member Rating**
    - Average rating given by members.

15. **Frequent Feedback Comments**
    - Most common comments from feedback.

### Join-Based Metrics

1. **Average Revenue per Member**
    - Average revenue generated per member.
    ```sql
    SELECT 
        M.ID AS Member_ID,
        M.Name,
        AVG(T.Amount) AS Avg_Revenue_Per_Member
    FROM 
        MEMBERS M
    JOIN 
        TRANSACTIONS T ON M.ID = T.Member_ID
    GROUP BY 
        M.ID, M.Name
    ORDER BY 
        Avg_Revenue_Per_Member DESC;
    ```

2. **Average Activities per Member**
    - Average number of activities per member.
    ```sql
    SELECT 
        M.ID AS Member_ID,
        M.Name,
        AVG(SA.Activity_Count) AS Avg_Activities_Per_Member
    FROM 
        MEMBERS M
    JOIN 
        (SELECT 
             Member_ID, COUNT(*) AS Activity_Count
         FROM 
             SITE_ACTIVITY
         GROUP BY 
             Member_ID) SA ON M.ID = SA.Member_ID
    GROUP BY 
        M.ID, M.Name
    ORDER BY 
        Avg_Activities_Per_Member DESC;
    ```

3. **Average Feedback Rating by Subscription Type**
    - Average feedback rating by subscription type.
    ```sql
    SELECT 
        M.Subscription_Type,
        AVG(FB.Rating) AS Avg_Rating
    FROM 
        MEMBERS M
    JOIN 
        MEMBER_FEEDBACK FB ON M.ID = FB.Member_ID
    GROUP BY 
        M.Subscription_Type
    ORDER BY 
        Avg_Rating DESC;
    ```

## How to Generate the Dataset

To generate the synthetic dataset, use the provided Python script `generate_data.py`. The script utilizes the Faker library to create realistic fake data for the membership site.

## Contact
If you have questions feel free to ask me.
- [LinkedIn](https://www.linkedin.com/in/alanlanceloth/)
- [GitHub](https://github.com/alanceloth/)
- [alan.lanceloth@gmail.com](mailto:alan.lanceloth@gmail.com)