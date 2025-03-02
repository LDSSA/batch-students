# LDSSA Hackathon #5 - Hotel Recommendation Systems

## **Schedule**

| Hour  | Activity                          |
|-------|-----------------------------------|
| 08:15 | Arrival, Student setup            |
| 08:30 | Hackathon Prompt, Team Assignment |
| 09:00 | Start Hacking!                    |
| 12:30 | Lunch (keep hacking if you like)  |
| 14:00 | Goal - First Submission           |
| 15:00 | Goal - Improved Submission        |
| 16:00 | Start Working on Presentation     |
| 17:00 | Stop Hacking!                     |
| 17:30 | Team Presentations                |
| 18:20 | Instructor’s Presentation         |
| 18:30 | Winners Announced                 |
| 18:45 | Closing Remarks                   |

---

## **Overview**

Welcome to the **LDSSA Hackathon #5 - Hotel Recommendation Systems**! 🚀

You have been hired by **Trippy™, an emerging hotel review and recommendation platform**. Trippy helps travelers
discover and book the best hotels based on reviews from other users. The company wants to leverage data science and
machine learning to **improve hotel recommendations** for its users, making sure they get highly relevant hotel
suggestions based on past experiences and preferences.

Your goal is to build a **hotel recommendation system** that helps Trippy users find the best hotel recommendations
tailored to their past interactions.

---

## **Task**

Your task is to build a **personalized hotel recommendation system** using user reviews.
The system should generate hotel recommendations for users based on the available review dataset.

---

## **Dataset**

You will be working with the **HotelRec Dataset**, which consists of:

- **Filtered_HotelRec_Main_CSV.zip** – The primary dataset containing date, user_id, hotel_id and rating.
- **Filtered_HotelRec_Metadata_CSV.zip** – Additional metadata related to the hotels.

### **Columns in the dataset**:

- `user_id`  - Unique ID representing a user.
- `hotel_id`  - Unique ID representing a hotel.
- `rating`  - User rating for the hotel.
- `title`  - Review title (only reviews with titles are included).
- `text`  - Full review text.
- `sleep_quality`, `value`, `rooms`, `service`, `cleanliness`, `location` (float) - Additional review categories.
- `date`  - Date of review.

**Objective:**
Using this dataset, generate a **ranked list of hotel recommendations** for each user.

---

## **Evaluation Criteria**

- **performance Rank (50%)** – How well your recommendations perform, measured by MAP@10.
- **Presentation Rank (50%)** – How well your team presents its work.

---

## **Submission Format**

Your team should submit a json file in the following format:

```json
{
    "user_id1": ["recommended_hotel1", "recommended_hotel2", "recommended_hotel3", "recommended_hotel4", "recommended_hotel5"],
    "user_id2": ["recommended_hotel2", "recommended_hotel1", "recommended_hotel34", "recommended_hotel22", "recommended_hotel11"]
}

```

The users for submission should be the ones in submission.json file.

Each user should have a list of **up to 10 recommended hotels**, ranked from most to least relevant.

---

## **Hackathon Rules**

- **Team Formation:** Teams will be randomly assigned.
- **Instructor Support:** Instructors will be available to help with technical questions, but will not provide
  solutions.
- **Submission Limits:** Each team can submit up to **5 times**.
- **Final Presentation:** Each team must present their work in a **4-minute presentation**.

---

## **Presentation Guidelines**

Your presentation should be clear, structured, and informative. Suggested format:

1. **Problem description**
2. **Data cleaning and exploration**
3. **Feature engineering and modeling approach**
4. **Evaluation and results**
5. **Future work & improvements**
6. **A funny pun at the end (VERY IMPORTANT!)**

---

## **Tips for Success, but you are free to do what works best for you**

✅ **Start with a simple baseline** before improving your model.

🔹 A simple most popular hotels approach is a good first step. (print the Top-N Most Popular Hotels)

🔹 A random recommender can also serve as a baseline to compare performance.

✅ **Leverage user and hotel metadata** to improve predictions.

🔹 Is it better to use only rows with non-null metadata? Or fill them with the mean?

🔹 Print a sample of recommendations for random users after training.

🔹 Include an easy sanity check function (e.g., do top-rated hotels actually get recommended?).

✅ **Optimize for memory and performance** – the dataset is large and preprocessing and memory efficiency are key!

🔹 Use pandas astype() to reduce memory footprint by converting data types.

🔹 Apply data filtering early (e.g., remove inactive users, missing values) to speed up the processing.

🔹 Use batch processing when loading large files.

🔹 Consider sparse matrices for large-scale collaborative filtering.

✅ **Debugging & Model Evaluation**

🔹 Run small-scale tests before processing the full dataset.

🔹 Check distributions of user reviews – do some users/hotels dominate?

🔹 Visualize recommendation results to spot anomalies.

✅ **Communicate well within your team** to distribute tasks efficiently.

✅ **Enjoy the hackathon and learn as much as you can!** 🎉

---

**Good luck, and may the best recommendations win!** 🎯

