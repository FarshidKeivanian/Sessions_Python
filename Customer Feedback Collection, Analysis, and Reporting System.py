#pip install textblob
import nltk
nltk.download('brown')
nltk.download('punkt')
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
from textblob import TextBlob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# Initialize feedback data list
feedback_data = []

# Function to collect customer feedback
def collect_feedback():
    name = name_entry.get()
    try:
        rating = int(rating_entry.get())
        if rating < 1 or rating > 5:
            messagebox.showerror("Invalid Input", "Rating must be between 1 and 5.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the rating.")
        return
    comment = comment_entry.get()
    feedback_data.append({'Name': name, 'Rating': rating, 'Comment': comment, 'Timestamp': datetime.datetime.now()})
    name_entry.delete(0, tk.END)
    rating_entry.delete(0, tk.END)
    comment_entry.delete(0, tk.END)
    messagebox.showinfo("Feedback Collected", "Thank you for your feedback!")

# Function to analyze feedback
def analyze_feedback():
    if not feedback_data:
        messagebox.showwarning("No Feedback", "No feedback data to analyze.")
        return
    
    df = pd.DataFrame(feedback_data)
    
    # Perform sentiment analysis
    df['Sentiment'] = df['Comment'].apply(lambda comment: TextBlob(comment).sentiment.polarity)
    df['Sentiment_Category'] = df['Sentiment'].apply(lambda polarity: 'Positive' if polarity > 0 else ('Negative' if polarity < 0 else 'Neutral'))
    
    # Display summary
    summary_text.set(f"Average Rating: {df['Rating'].mean():.2f}\nTotal Feedbacks: {len(df)}")
    
    # Display detailed feedback
    for i in tree.get_children():
        tree.delete(i)
    for idx, row in df.iterrows():
        tree.insert("", tk.END, values=(row['Name'], row['Rating'], row['Comment'], row['Sentiment_Category']))
    
    # Display chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    ax1.hist(df['Rating'], bins=range(1, 7), align='left', edgecolor='black')
    ax1.set_xlabel('Rating')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Distribution of Ratings')
    
    sentiment_counts = df['Sentiment_Category'].value_counts()
    ax2.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
    ax2.set_title('Sentiment Distribution')
    
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    # Save feedback data to CSV
    df.to_csv('feedback_data.csv', index=False)

# Function to send email report
def send_email_report():
    df = pd.DataFrame(feedback_data)
    if df.empty:
        messagebox.showwarning("No Feedback", "No feedback data to send.")
        return
    
    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient_email@example.com'
    msg['Subject'] = 'Weekly Feedback Report'
    
    body = f"""
    Average Rating: {df['Rating'].mean():.2f}
    Total Feedbacks: {len(df)}
    Sentiment Distribution: 
    {df['Sentiment_Category'].value_counts().to_string()}
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('your_email@example.com', 'your_password')
    text = msg.as_string()
    server.sendmail('your_email@example.com', 'recipient_email@example.com', text)
    server.quit()
    messagebox.showinfo("Email Sent", "Weekly feedback report has been sent.")

# Create main window
root = tk.Tk()
root.title("Customer Feedback Collection and Analysis")

# Create input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Customer Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Rating (1-5):").grid(row=1, column=0, padx=5, pady=5)
rating_entry = tk.Entry(input_frame)
rating_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Feedback Comment:").grid(row=2, column=0, padx=5, pady=5)
comment_entry = tk.Entry(input_frame)
comment_entry.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(input_frame, text="Submit Feedback", command=collect_feedback)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create output frame
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

summary_text = tk.StringVar()
summary_label = tk.Label(output_frame, textvariable=summary_text)
summary_label.pack()

tree = ttk.Treeview(output_frame, columns=("Name", "Rating", "Comment", "Sentiment"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Rating", text="Rating")
tree.heading("Comment", text="Comment")
tree.heading("Sentiment", text="Sentiment")
tree.pack()

analyze_button = tk.Button(root, text="Analyze Feedback", command=analyze_feedback)
analyze_button.pack(pady=10)

email_button = tk.Button(root, text="Send Email Report", command=send_email_report)
email_button.pack(pady=10)

# Create chart frame
chart_frame = tk.Frame(root)
chart_frame.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

